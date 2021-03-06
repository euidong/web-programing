# HTTP
: 웹 서버와 웹 클라이언트 사이에서 데이터를 주고받기 위해 사용하는 통신 방식
<BR> TCP/IP 를 기본으로 한다.
<BR> HTML, XML과 같은 하이퍼텍스트뿐만 아니라 이미지, 음성, 동영상, 자바스크립트, 각종 문서 파일 등을 전송할 수 있다.


# 구조
  1. Start Line (요청라인)
  2. Header (헤더)
  3. Blank Line (빈줄)
  4. Body (바디)

### 1. Start Line

<p>1) 요청 메세지 </p>

```
  GET http://example.com:80/book/shakespeare HTTP/1.1
```

```
(1) 요청 방식 
POST, GET, PUT, DELETE 가 메인으로 사용되고 각각은 CRUD와 대응된다. 
Create, Read, Update, Delete

(2) 요청 URI 
URL(Resource의 위치) + URN(Resource의 이름)
http://www.example.com:80/services?category=2&kind=patents#n10

ㄱ. 스킴 : 프로토콜을 의미한다.
ㄴ. 호스트명 : IP주소 OR 도메인명을 의미한다.
ㄷ. 포트번호 : 포트번호로, 공백 시 HTTP = 80, HTTPS = 443
ㄹ. 경로 : 해당 리소스의 경로를 의미한다.(URL)
ㅁ. 쿼리스트링 : &로 서로를 구분한다. 형태는 <STRONG>키=값</STRONG>이다. (URI)
ㅂ. 프라그먼트 : 문서 내에서의 앵커를 지정합니다.

(3) 프로토콜 버전 
프로토콜과 이에 해당하는 버전을 명시한다.
```

<p>2) 응답 메세지</p>

```
  HTTP/1.1 200 OK
```

```
(1) 프로토콜 버전
프로토콜과 이에 해당하는 버전을 명시한다.

(2) 상태 코드
1XX = 임시 응답
2XX = 성공
3XX = URI의 정보가 변경되었음.
4XX = 클라이언트에 의한 Error 요청 메세지가 잘못됨.
5XX = 서버에 의한 Error 서버 부하 등.

(3) 상태 텍스트
상태 코드에 대한 설명이 붙는다.
```
