from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class DatetimeUtil:
    @staticmethod
    def datetime_delta(reference_time: datetime = None, years: int = 0, months: int = 0, days: int = 0,
                       hours: int = 0, minutes: int = 0, seconds: int = 0, microseconds: int = 0, is_str: bool = False,
                       format: str = '%Y-%m-%d %H:%M:%S.%f') -> datetime or str:
        """
            시간에서 년, 월, 일, 시간, 분, 초, 밀리초를 더하거나 뺀값을 계산합니다.
        Args:
            reference_time: 기준시간
            years: 더하거나 뺄 연도 숫자 (음수 사용가능, 생략 가능)
            months: 더하거나 뺄 월 숫자 (음수 사용가능, 생략 가능)
            days: 더하거나 뺄 날짜 (-음수 사용가능, 생략 가능)
            hours: 더하거나 뺄 시간 (음수 사용가능, 생략 가능)
            minutes: 더하거나 뺄 분 (음수 사용가능, 생략 가능)
            seconds: 더하거나 뺄 초 (음수 사용가능, 생략 가능)
            microseconds: 더하거나 뺄 밀리초 (음수 사용가능, 생략 가능)
            is_str: string 타입으로 변환 여부 (생략 가능)
            format: 날짜 양식
        Returns:
            시간(datetime)
        """
        if reference_time is None:
            reference_time = datetime.now()
        if type(reference_time) is not datetime:
            raise ValueError('기준시간의 유형(datetime.datetime)을 확인해 주세요.')

        return_date = reference_time + relativedelta(years=years) + relativedelta(months=months) + relativedelta(
            days=days) + relativedelta(hours=hours) + relativedelta(minutes=minutes) + relativedelta(
            seconds=seconds) + relativedelta(microseconds=microseconds)

        if is_str:
            return return_date.strftime(format)

        return return_date
