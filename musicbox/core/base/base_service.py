from django.db.models import QuerySet
from django.forms import model_to_dict
from django_filters import utils


class BaseService:
    queryset_list = None
    queryset_detail = None
    serializer = None
    filter_set_class = None

    @staticmethod
    def check_queryset(param_queryset, base_queryset):
        if param_queryset:
            return param_queryset
        elif base_queryset:
            return base_queryset
        else:
            raise Exception('QuerySet이 지정되지 않았습니다.')

    @staticmethod
    def check_serializer(param_serializer, base_serializer):
        if param_serializer:
            return param_serializer
        elif base_serializer:
            return base_serializer
        else:
            return None

    def create(self, params):
        serializer = self.serializer(data=params)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer

    def modify(self, path_param: dict, params: dict = None, partial=False):
        instance = self.select_model(path_param=path_param)
        serializer = self.serializer(instance, data=params, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return serializer

    def select(self, path_param: dict, query: QuerySet = None, serializer=None):
        qs = self.select_model(path_param, query)
        serializer = self.check_serializer(serializer, self.serializer)

        print(model_to_dict(qs))

        if serializer:
            return serializer(qs, many=False)
        else:
            return qs

    def select_model(self, path_param: dict, query: QuerySet = None):
        return self.check_queryset(query, self.queryset_detail).get(**path_param)

    def select_all(self, params: dict = None, query: QuerySet = None, serializer=None):
        qs = self.filter_queryset(self.check_queryset(query, self.queryset_list), params)
        serializer = self.check_serializer(serializer, self.serializer)

        if serializer:
            return serializer(qs, many=True)
        else:
            return qs

    def select_all_model(self, params: dict = None, query: QuerySet = None):
        return self.filter_queryset(self.check_queryset(query, self.queryset_list), params)

    def filter_queryset(self, queryset: QuerySet, params: dict) -> QuerySet:
        """지정된 필터가 존재할 경우 queryset 내 필터를 적용하고, 존재하지 않은 경우 queryset을 반환합니다.
        Args:
            queryset: 지정된 queryset
            params: queryset 내 적용할 params(dict)
        Returns: 필터가 적용된 queryset
        """
        filter_set = self.get_filter_set(params, queryset, self)

        if filter_set is None:
            return queryset

        if not filter_set.is_valid():
            raise utils.translate_validation(filter_set.errors)

        return filter_set.qs

    def get_filter_set(self, params: dict, queryset: QuerySet, service):
        filter_set_class = self.get_filter_set_class(service, queryset)

        if filter_set_class is None:
            return None

        kwargs = self.get_filter_set_kwargs(params, queryset)

        return filter_set_class(**kwargs)

    @classmethod
    def get_filter_set_class(cls, service, queryset: QuerySet = None):
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
        return {
            'data': params,
            'queryset': queryset
        }
