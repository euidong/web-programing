# API
Application<br>
Programming<br>
Interface

### Device API

API(Application Programming Interface, 응용 프로그램 프로그래밍 인터페이스)는 응용 프로그램에서 사용할 수 있도록, 
운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻한다.
주로 파일 제어, 창 제어, 화상 처리, 문자 제어 등을 위한 인터페이스를 제공한다.

### Remote API

Remote API(WEB을 포함함)는 표준 기반 기술을 사용하여 통신 네트워크를 통해 먼 거리에서 호출할 수 있는 소프트웨어 구성요소에 대한 인터페이스
예를 들어 블로그 API를 이용하면 블로그에 접속하지 않고도 다른 방법으로 글을 올릴 수 있다. 

그 외에 우체국의 우편번호 API, 구글과 네이버의 지도 API등 유용한 API들이 많으므로, 
요즘은 홈페이지 구축이나 추가개편 시 따로 추가로 개발하지 않고 이런 오픈 API를 가져와 사용하는 추세다.

Web 정보를 표현하는 다양한 platform의 등장과 이를 지원하는 것이 무엇보다 중요하다는 회사의 통찰이 생겨났고,
이에 따라 사람들은 API에 주목했다.

[참고](https://www.redhat.com/ko/topics/api/what-are-application-programming-interfaces)


# REST

REpresentational <br>
State <br>
Transfer <br>

웹 서버에 존재하는 요소들을 모두 리소스라고 정의하고, URI를 통해 웹 서버의 특정 리소스를 표현한다는 개념이다.<br>
기존의 방식과의 차별점은 API의 표현을 쿼리스트링 없이 경로만을 가진 URL을 통해 표현합니다.<br>
그렇기에 모든 URI의 구성이 대게 명사형으로 이루어진다.

EX)
```
http://blog.example.com/keyword/test
```
