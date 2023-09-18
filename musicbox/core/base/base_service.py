from django.db import transaction
from django.db.models import QuerySet, Model
from django.forms import model_to_dict
from django_filters import utils


class BaseService:
    """
    베이스 서비스
    """
    queryset_list = None
    queryset_detail = None
    serializer = None
    serializer_list = None
    serializer_detail = None
    filter_set_class = None

    @staticmethod
    def check_queryset(param_queryset: QuerySet, base_queryset: QuerySet):
        """ QuerySet 확인 후 적절한 QuerySet 반환
        Args:
            param_queryset: 인자로 받은 QuerySet
            base_queryset: 기본값 QuerySet
        Returns:
            QuerySet
        """
        if param_queryset is not None:
            return param_queryset
        elif base_queryset is not None:
            return base_queryset
        else:
            raise Exception('QuerySet을 지정해 주세요.')

    @staticmethod
    def check_serializer(param_serializer, base_serializer):
        """ Serializer 확인 후 적절한 Serializer 반환
        Args:
            param_serializer: 인자로 받은 Serializer
            base_serializer: 기본값 Serializer
        Returns:
            Serializer
        """
        if param_serializer:
            return param_serializer
        elif base_serializer:
            return base_serializer
        else:
            raise Exception('Serializer를 지정해 주세요.')

    def create(self, params: dict):
        """ 모델 생성
        Args:
            params: 등록할 모델의 구성 정보
        Returns:
            모델 Serializer
        """
        serializer = self.serializer(data=params)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer

    def modify(self, path_param: dict, params: dict = None, partial=False):
        """ 모델 수정
        Args:
            path_param: 모델 pk 정보
            params: 모델 수정 정보
            partial: 부분 수정 여부
        Returns:
            수정된 모델 Serializer
        """
        instance = self.select_model(path_param=path_param)
        serializer = self.serializer(instance, data=params, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return serializer

    @transaction.atomic
    def remove(self, path_params: dict):
        """지정된 모델을 삭제합니다.
        Args:
            path_params: 삭제할 모델 pk params(dict)
        Returns:
        """
        instance: Model = self.select_model(path_params)
        if instance:
            instance.delete()

    def select(self, path_param: dict, query: QuerySet = None, serializer=None):
        """ 모델 단일 조회 - Detail Serializer 사용
        Args:
            path_param: 조회할 모델 조건 정보
            query: 지정 QuerySet
            serializer: 지정 Serializer
        Returns:
            모델 Serializer
        """
        qs = self.select_model(path_param, query)
        serializer = self.check_serializer(serializer, self.serializer_detail)

        return serializer(qs, many=False)

    def select_plain(self, path_param: dict, query: QuerySet = None, serializer=None):
        """ 모델 단일 조회 - 기본 Serializer 사용
        Args:
            path_param: 조회할 모델 조건 정보
            query: 지정 QuerySet
            serializer: 지정 Serializer
        Returns:
            모델 Serializer
        """
        qs = self.select_model(path_param, query)
        serializer = self.check_serializer(serializer, self.serializer)

        return serializer(qs, many=False)

    def select_model(self, path_param: dict, query: QuerySet = None):
        """ 모델 단일 조회
        Args:
            path_param: 조회할 모델 조건 정보
            query: 지정 QuerySet
        Returns:
            모델 객체
        """
        return self.check_queryset(query, self.queryset_detail).get(**path_param)

    def select_all(self, params: dict = None, query: QuerySet = None, serializer=None):
        """ 모델 목록 조회
        Args:
            params: 조회할 모델 목록 조건 정보
            query: 지정 QuerySet
            serializer: 지정 Serializer
        Returns:
            조회된 모델 목록 Serializer
        """
        qs = self.filter_queryset(self.check_queryset(query, self.queryset_list), params)
        serializer = self.check_serializer(serializer, self.serializer_list)

        return serializer(qs, many=True)

    def select_all_model(self, params: dict = None, query: QuerySet = None):
        """ 모델 목록 조회
        Args:
            params: 조회할 모델 목록 조건 정보
            query: 지정 QuerySet
        Returns:
            조회된 모델 목록 QuerySet
        """
        return self.filter_queryset(self.check_queryset(query, self.queryset_list), params)

    def filter_queryset(self, queryset: QuerySet, params: dict) -> QuerySet:
        """지정된 필터가 존재할 경우 QuerySet 내 필터를 적용하고, 존재하지 않은 경우 QuerySet을 반환
        Args:
            queryset: 지정된 QuerySet
            params: QuerySet 내 적용할 조건 정보
        Returns:
            필터가 적용된 QuerySet
        """
        filter_set = self.get_filter_set(params, queryset, self) if params else None

        if filter_set is None:
            return queryset

        if not filter_set.is_valid():
            raise utils.translate_validation(filter_set.errors)

        return filter_set.qs

    def get_filter_set(self, params: dict, queryset: QuerySet, service):
        """서비스 내 정의된 필터를 가져와 QuerySet 내 적용
        Args:
            params: 조회할 모델 params
            queryset: 지정된 QuerySet
            service: 지정된 Service
        Returns:
            필터가 적용된 QuerySet
        """
        filter_set_class = self.get_filter_set_class(service, queryset)

        if filter_set_class is None:
            return None

        kwargs = self.get_filter_set_kwargs(params, queryset)

        return filter_set_class(**kwargs)

    @classmethod
    def get_filter_set_class(cls, service, queryset: QuerySet = None):
        """서비스 내 지정된 필터 클래스 가져옵니다.
        Args:
            service: 지정된 Service
            queryset: 지정된 QuerySet
        Returns:
            지정된 필터 클래스
        """
        filter_set_class = getattr(service, 'filter_set_class', None)

        if filter_set_class:
            filter_set_model = filter_set_class._meta.model

            # FilterSets do not need to specify a Meta class
            if filter_set_model and queryset is not None:
                assert issubclass(queryset.model, filter_set_model), \
                    'FilterSet model %s does not match queryset model %s' % \
                    (filter_set_model, queryset.model)

            return filter_set_class

        return None

    @classmethod
    def get_filter_set_kwargs(cls, params: dict, queryset: QuerySet) -> dict:
        """ 조회할 모델 조건 정보와 QuerySet을 딕셔너리로 반환합니다.
        Args:
            params: 조회할 모델 조건 정보
            queryset: 지정된 QuerySet
        Returns:
            조회할 모델 조건 정보와 QuerySet을 담은 딕셔너리
        """
        return {
            'data': params,
            'queryset': queryset
        }
