# 공부하며 만드는 URL SHORTENER PROJECT

## 장고의 장점

- 커뮤니티가 잘 되어 있어 정보를 얻기 좋고 다양한 기능을 제공한다. HTML, XML, JSON 등 종류에 상관없이 장고로 처리 가능하다.

- 보안적 측면에서 안전하다. XSS, CSRF, SQL injection, click hijacking 공격 등을 프레임워크에서 기본적으로 방어해준다. 유저의 ID, PW 안전하게 관리, 세션을 쿠키로도 제공하지만 DB에도 보관해서 유저의 연결 컨트롤 가능,

- 모듈 간 의존성이 낮아 확장성이 좋다. 그래서 아키텍쳐의 변화가 자유롭다. DB 서버, 어플리캐이션 서버 등 어디에서나 하드웨어를 추가하거나 제거하여 트래픽이 늘어거나 줄어들면 유연하게 대응할 수 있다.

- 인스타그램, 유투브, 토스 등에서 사용

## 장고의 구조

- MTV 구조

![이미지](https://t1.daumcdn.net/cfile/tistory/993FB83359869E051C)

## 미들웨어

urls.py에서 views.py로 갈 때 middle ware를 거쳐서 가게 된다.

logging, 인증, 트래픽 감시 등에 유용하다.

## views.py에 있는 함수들의 request

views.py에 함수를 정의할 때는 반드시 인자에 request를 적어줘야 한다.

장고에서는 urls.py에서 미들웨어를 거쳐서 views.py에 들어와서 함수를 실행하게 되는데 이때 반드시 request를 매개변수로 주게 된다.

따라서 오류를 방지하기 위해 views.py에 함수를 정의할 때 request를 인자로 둬야 한다.

## template 폴더의 위치 지정

프로젝트 폴더에 있는 settings.py에서 TEMPLATES 리스트에 DIRS 키에 속한 value에 경로를 추가해준다.

## Redirect를 하는 경우

- 로그인을 하지 않고 로그인이 필요한 페이지에 접근하는 경우

- 권한이 없는데 권한이 필요한 페이지(ex - admin page에 접근)에 접근하려는 경우

redirect로 접근 차단 가능

## @csrf_exempt

장고는 위변조 방지를 위해 처음 rendering을 할 때 csrf 토큰을 해당 페이지에 준다.

이 csrf 토큰을 가지고 요청을 해야 csrf 미들웨어에서 valid한 요청이라고 인지하고 통과시켜준다.

이때 @csrf_exempt를 하면 csrf 체크를 하지 않는 설정이다.

csrf 토큰을 헤더에 넣어야 하는데 csrf토큰은 계속 바뀐다. 따라서 테스트의 편의를 위해 @csrf_exempt를 추가해준다.

(또는 settings.py에 가서 csrfViewMiddleware부분을 주석처리 해도 된다.)

## Frontend가 DB에 직접 접속할 수 없는 이유

Frontend는 사용자에게 노출되기 때문에 DB에 직접 접속하게 되면 민감한 정보들이 노출될 수 있고 또한 시스템에 문제가 생길 위험이 커지기 때문

그래서 Backend를 두어서 DB에 간접적으로 접근한다.

## ORM

- Object Relational Mapping(객체-관계 매핑)

- 객체와 RDBMS를 매핑해주는 모듈

- SQL 쿼리를 자동으로 생성한다.

- 여기서는 DB에 있는 데이터와 Python 객체를 매핑한다.

- 객체를 통해 간접적으로 DB 데이터와 테이블을 다룬다.

- Django ORM. SQLAlchemy, Pony 등이 있다. 통상 SQLAlchemy를 많이 쓴다. Django ORM은 async 즉, 비동기를 지원하지 않기 때문에 잘 사용하지 않는다. 심지어 장고를 쓰면서도 SQLAlchemy를 쓰는 경우도 있다. 여기서는 Django ORM을 쓴다.

- 장점

> **직관적이다.**

> **SQL 학습 시간이 필요없고 Business logic에 더 집중할 수 있다.**

> **가독성이 좋아진다.**

> **코드 재사용 및 유지보수가 수월하다.**

> **DBMS 종속성이 줄어든다. DBMS를 바꿔도 코드를 수정하지 않아도 된다. 예를 들어 MySQL을 사용했다가 Postgress를 사용해도 쿼리를 안 바꿔도 된다.**

> **SQL injection 공격을 막아준다.**

- 단점

> **Raw 쿼리가 필요한 구간이 있기 마련이다. ORM만으로는 대처가 안 된다.**

> **프로젝트의 복잡도가 올라가면 ORM의 난이도도 올라간다.**

## 기타

개발자 도구 > application > cookies를 보면

sessionid와 csrftoken이 있다.

sessionid로 로그인을 한다.

로그인 상태를 sessionid로 알 수 있다.

로그아웃을 하면 sessionid가 사라진다.

csrftoken은 매번 바뀌어서 이 페이지에서 하는 요청인지, 외부 페이지에서 요청을 날리는지 확인이 가능하다. 그렇게 위변조를 막을 수 있다.
