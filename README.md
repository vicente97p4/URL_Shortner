## 장고의 장점

1. Batteries included

배터리가 포함된 상태?

개발자들이 개발하고 싶은 거의 모든 것이 들어가있다.

커뮤니티가 방대해서 커뮤니티에서 정보를 얻기 좋다.

2. 다양한 사용이 가능하다.

wiki, sns, news, blog, 쇼핑몰 html, xml, json 상관 없이 장고로 처리 가능하다.

다용도로 처리 가능한 프래임워크

3. 안전하다.

보안 문제에 대해 built-in으로 제공하고 있다.

- 유저의 계정, 비밀번호 안전하게 관리하는 방법 제공

- 세션 관리, 세션을 쿠키로 제공하고, 세션 값을 db에 보관한다. 그래서 백엔드에서 유저 강제 로그아웃 시키기 가능하다.

- xss, csrf, sql injection, clip hijacking 등의 공격을 기본적으로 막아준다.

4. Shared-nothing Architecture

- 확장성이 좋다.

- Architecture(모듈)가 독립적이어서(의존성이 없어서) 필요할 때 해당 layer에서 교체 가능하다.

- caching sever, db sever, application server 어디에 하드웨어를 추가해서 트래픽이 늘어나도 유연하게 대처 가능

- 사용자가 많아 트래픽이 많은 서비스에 유리(youtube, 인스타, 토스가 대표적인 예)

5. Very maintainable

- 유지보수가 쉽다.

- DRY(don't repeat yourself): 같은 일을 두 번 하지 말라!  
  불필요한 중복 코드 없애고 편리하게 유지보수할 수 있게 제공한다.

### Middle ware

Middle ware가 있다면 URLS에서 Views로 가기 전에 middle ware를 거쳐서 간다.

그럼 이 middle ware에서 로깅도 할 수 있고, 인증도 할 수 있고, 트래픽을 감시할 수 있다.

### PEP8 Coding Convention

- coding convention: 여러 사람이 협업을 해도 모두가 읽기 편한 코드를 작성하기 위한 관례

- 파이썬은 PEP8을 따른다.

> **한 줄의 문자열은 79자**  
> **DocString은 72자**  
> **snake_case** 사용  
> **모듈 레벨 상수는 모두 대문자**  
> **ClassName은 Capitalized Word(맨 앞 글자가 대문자)**  
> **한 줄로 된, if, try...except, for, while 구문은 사용하지 않는다.**

### PEP 20 - Zen of Python

- 파이썬의 20가지 정신

- 여러가지가 있지만 가독성이 중요하다!!
