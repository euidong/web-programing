# Web
web상에는 client와 server가 존재한다.

client는 리소스를 요청하여, server에 저장하거나 받아 온다.

server는 client가 요청하는 리소스를 전송하거나, 저장한다.

이때 사용하는 대표적인 프로토콜이 http이다.

# Web client
http를 통해 받아온 데이터를 사용자에게 보여주는 방식을 정의해 놓은 프로그램이다.

  1. browser(chrome,edge,firefox 등)
  2. curl (linux)
  3. telent (linux)
  4. postman
  5. 직접 만드는 Web client <br>
  (python에 경우 urlib를 통해 구현)
  

# Web server
http로 데이터를 전송하기 위하여 각종 html, xml, 이미지, 동영상과 같은 resource를 갖고 있는 주체이다.
그리고 이러한 resource를 어떻게 전송할지를 정의하는 것을 Web server를 구축한다고 한다.

## web page 구성하기

1. 정적 페이지
누가, 언제 요구하더라도 항상 같은 내용을 표시하는 웹 페이지를 말한다.

2. 동적 페이지
누가, 언제, 무엇을 요구하느냐에 따라 각각 다른 내용이 반환되는 페이지를 말한다.
필요한 데이터를 저장하고 꺼내오는 등의 DB 처리에 대한 요구가 증가하였다.
따라서, 이를 관리하는 별도의 프로그램과 웹서버와의 정보 교환을 정의한 것이 CGI(Common Gateway Interface)이다.
<img src ="https://docs.oracle.com/cd/E19146-01/820-0874/images/training3.gif">
CGI 방식을 이용하게 되면 프로세스가 많아질 수록 비례적으로 프로세스가 점유하는 메모리 요구량도 커져서 시스템에 부하를 주는 원인이 된다.
따라서 사용하지 않는 방식이 됩니다.

따라서, 웹 서버 자체에 스크립트 엔진(인터프리터)을 내장시켜서 프로세스를 가동시킨다. (python에서는 wsgi)


## 두 개의 Web server
1. 웹 서버

html, css, javascript 등으로 작성된 정적 페이지를 정의하는 요소를 갖고, 
웹 어플리케이션 서버가 제공하는 정보를 토대로 정적 페이지를 client에게 제공하는 서버이다.
또한, 서버의 분리를 통해 남는 이득을 캐시 기능, 프록시 기능, client 요청 제어 등의 추가적인 기능을 수행한다.

2. 웹 어플리케이션 서버

python, php, c++ 등  여러가지 언어를 통해 형태와 동작을 구현하는 서버이다. 이러한 연산은 많은 처리를 필요로 한다.

<img src="http://basolutions.co.kr/wp-content/uploads/2015/12/web-apps.gif">
