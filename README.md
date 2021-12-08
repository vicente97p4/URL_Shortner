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

## 장고 템플릿 테그

- DB 자료와 보여줘야 하는 자료가 다를 때 사용한다.

- 반복적으로 같은 템플릿 코드를 작성할 때 사용한다.

{% csrf_token %}
{% cycle "a" "b" %} : for loop를 돌면서 한 번은 a, 한 번은 b를 출력한다. 만일 c가 있으면 3번째에는 c를 출력한다.
{% extends %} : 사이트에 공통으로 들어가는 반복되는 코드를 들고와 확장해서 쓸 때 사용하는 태그
{% block %} : extends를 사용할 때 어떤 부분인지를 나타내는 블록을 나타내는 태그
{% if %} {% else %}
{% for i in items %}
{% includes %} : 다른 HTML을 그대로 include해서 사용할 때 사용

## Django 로그인 방식

장고는 기본적으로 session 방식을 사용한다.

1. 유저가 Django 서버에 로그인 정보를 전달한다.

2. Django는 이 정보를 보고 유효한 정보면 session key를 발급하고 session data를 DB에 저장한다.

3. Django에서 유저에게 session key를 전달한다. 이 session key는 session data를 가져오기 위한 일종의 ID 값이다.

결론적으로 session에 관한 정보는 DB에 있다.

session 방식을 사용하고 싶지 않으면 settings.py에 MIDDLEWARE에서 sessions 부분을 지우면 된다.

## Session engine

명시하지 않으면 DB로 작동한다.(Database backed session)

DB로 세션을 작동하고 싶지 않으면 cache 방식, file 방식 등을 택할 수 있다.(Cached session, File based session, cookie based session 등)

- cache는 디스크가 아닌 메모리에 있는 정보라 더 빠르다.

- file based는 안정성이 좋다.

## JWT와 차이점

JWT는 앞에는 헤더, . 뒤에는 payload다.

시크릿 키를 보고 앱 서버가 인증 여부를 판단한다.

- JWT는 서버로 요청이 들어올 때마다 DB를 확인하지 않아도 된다. signature만 맞춰보고 signature가 정확하다면 바로 payload 부분을 사용하면 된다.
  반면 장고는 반드시 DB를 봐야한다.

- 근데 signature 외 부분은 암호화가 되지 않아 그 부분에 데이터가 많을 시 공격에 취약할 수 있다.

- JWT와 장고 모두 정보 변경이 가능하다. 장고의 경우 session id는 그대로 유지되고 session data가 변경된다.

정보 변경 시 장고는 클라이언트 측에서 변화가 없고 JWT는 클라이언트 측에서 새로운 JWT를 발급받아야 한다.

- 저장 방식

JWT는 Local storage, local session, cookie, index DB 모두 가능

장고 session은 cookie base로만 사용되고 있다.

다른 뤱프레임워크와 달리 장고는 풀스택이기 때문에 렌더링을 해줘야 한다 이때 로그인 여부를 알기 위해 cookie를 사용한다.

- JWT는 life span이 짧아서 안전성이 높다.

- 장고는 HTTPS를 쓰기 때문에 cookie 탈취 위협이 적다.

장고는 request 인자에 session을 가지고 있다.

반드시 key는 string으로 설정하고 호출 해야 한다.
