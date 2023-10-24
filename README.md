# Python-Django Portfolio

#### > [1. 프로젝트 개발환경 설정](#toc_10)
* OS: windows10
* python version: 3.8.1
* Django: 4.2.4

#### > [2. 프로젝트 테스트](#toc_10)
* 최초 시 
  * 데이터베이스 마이그레이션 진행
    * python manage.py makemigrations --settings=_musicbox.settings.dev
    * python manage.py migrate --settings=_musicbox.settings.dev
  * 슈퍼 유저 생성
    * python manage.py createsuperuser
    * 서버 구동 후 어드민에 접근해서 로그인 한 다음 기본 설정 진행하기

* 서버 구동
  * python manage.py runserver --settings=_musicbox.settings.dev
* 어드민 페이지
  * http://127.0.0.1:8000/admin/
* Swagger 페이지
  * http://127.0.0.1:8000/swagger/
  * 로그인 인증이 필요한 API 테스트 방법
    * 회원 > 회원 등록 진행 (이미 등록했다면 스킵)
    * 인증 > 인증 로그인 API 호출
      * 회신된 access token 확보
      * Swagger 페이지 최상단 우측의 Authorize 버튼 클릭
      * 팝업의 value 입력창에 아래와 같이 입력
        * Bearer [확보된 access token]
          * ex. Bearer eyJhbGciOiw...aj2mIufwjZNk
      * 팝업의 Authorize 버튼 클릭해서 승인
      * 인증이 필요한 다른 API 호출 가능