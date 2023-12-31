# Python-Django Portfolio

#### > [1. 프로젝트 개발환경 설정](#toc_10)
* OS: windows10 / ubuntu
* docker: 24.0.6
* python version: 3.10
* Django: 4.2.4
* Database: postgresql 13 (postgres:13)
* Redis: latest
* nginx: nginx:1.25.0-alpine
* gunicorn: 21.2.0
* pycharm (Professional Edition): 2023.2.5 
---
#### > [2. 프로젝트 테스트](#toc_10)
* 최초 시
  * 데이터베이스 마이그레이션 진행
    - docker-compose-migrate 이용해서 진행

* 서버 구동
  * docker-compose-runserver 이용해서 진행
---
#### > [3. 호스트](#toc_10)
* dev (docker-compose-runserver-dev build)
  * http://localhost:8000/
* prod (docker-compose-runserver-prod build)
  * http://localhost:1337/
---
#### > [4.어드민 페이지](#toc_10)
* dev (docker-compose-runserver-dev build)
  * http://localhost:8000/admin/
* prod (docker-compose-runserver-dev build)
  * http://localhost:1337/admin/
---
#### > [5. Swagger 페이지](#toc_10)  
* dev (docker-compose-runserver-dev build)
  * http://localhost:8000/swagger/
* prod (docker-compose-runserver-dev build)
  * http://localhost:1337/swagger/
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
---
#### > [99. 이슈 기록](#toc_10)
* backports.zoneinfo 라이브러리는 python 3.9 미만에서 동작하므로, requriements.txt의 관련 정보를 아래와 같이 기입하여야 docker 빌드가 성공적으로 진행될 수 있다.
  * backports.zoneinfo==0.2.1;python_version<"3.9"
* settings DEBUG=TRUE 일 경우 static을 알아서 처리해주고 실제 환경에서 테스트하려면 DEBUG=FALSE가 필수이다.
* nginx 연결 시 static file 관련 설정 반드시 필요
* nginx 연결 후 swagger에서 API 호출 시 CORS 확인
  * nginx 설정 중 host 관련 내용을 아래와 같이 세팅해야 정상 동작함..
  * proxy_set_header Host $host; -> proxy_set_header Host $http_host;
    * $http_host: HTTP Request의 Host 헤더값
    * $host: Host헤더가 없으면 server_name, Host 헤더를 사용하되, 포트값은 제외하고 모두 소문자로 표시
    * $host는 조건에 따라 변형이 일어나기 때문에 $host의 호출과, swagger test API 호출 시 host가 일치하지 않는 것