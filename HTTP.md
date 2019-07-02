# HTTP
: 웹 서버와 웹 클라이언트 사이에서 데이터를 주고받기 위해 사용하는 통신 방식
<BR> TCP/IP 를 기본으로 한다.
<BR> HTML, XML과 같은 하이퍼텍스트뿐만 아니라 이미지, 음성, 동영상, 자바스크립트, 각종 문서 파일 등을 전송할 수 있다.


# 구조
  1. Start Line (요청라인)
  2. Header (헤더)
  3. Blank Line (빈줄)
  4. Body (바디)
  
<p>1) 요청 메세지 </p>
```http
  GET http://example.com:80/book/shakespeare HTTP/1.1
```

<p>2) 응답 메세지</p>
```http
  HTTP/1.1 200 OK
  Content-Type: application/xhtml+xml; charset=utf-8
  
  <html>
  ...
  </html>
```

### 1. Start Line

<p>1) 요청 메세지 </p>
```http
  GET http://example.com:80/book/shakespeare HTTP/1.1
```

(1) 요청 방식 
POST, GET, PUT, DELETE 가 메인으로 사용되고 각각은 CRUD와 대응된다. 
Create, Read, Update, Delete

(2) 요청 URI 

(3) 프로토콜 버전 

<p>2) 응답 메세지</p>
```http
  HTTP/1.1 200 OK
  Content-Type: application/xhtml+xml; charset=utf-8
  
  <html>
  ...
  </html>
```
