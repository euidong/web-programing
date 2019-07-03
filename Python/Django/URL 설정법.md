# Django URL 설정법
2가지 방식이 있다.<br>
- path를 쓰는 방식
- re_path를 쓰는 방식

# Path

## 1. Base
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name ='sign_in'),
    path('sign_up/', views.sign_up, name ='sign_up'),
    path('user_list/', views.user_list, name = 'user_list')
]
```
Django에서는 view를 통해 화면을 구성한다.<br>
그리고, url에 따른 view를 선택해주는 방식을 사용한다.


```python
from django.urls import path
from . import views

urlpatterns = [
    path('url주소', 대게 뷰의 함수를 호출함(HttpResponse), name = '이름지어주기'),
]
```

## 2. include
### 1) 외부 include
```python
from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', include('user.urls')),
    path('notice/', include('notice.urls')),
]
```
Django에서는 하나의 web_server를 두고, 여러 개의 app을 만들어서 프로젝트를 만들어 나간다. <br>
이때, main으로 만든 app의 urls.py에서 각 각의 app의 urls.py를 include해주어야 한다. <br>
대게 이때에 url의 이름은 해당 app의 이름으로 하는 것이 일반적이다.

### 2) 내부 include
```python
from django.urls import path, include
from . import views

extra_patterns = [
    path('extra1/', views.get_extra1),
    path('extra2/', views.get_extra2),
]

urlpatterns = [
    ... 생략
    path('extra/', include(extra_patterns)),
]
```
path안에 path 배열을 넣는 것이 가능하다는 것이다.

## 3. url로 변수받기 
### 1) Base
`urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('<username>/', views.get_list_by_user),
]
```
(url 갯수의 제한은 없습니다. ,를 통해 계속 이어줄 수 있습니다. 이렇게 되면 url상에서는 /로 구분된다.) <br>
username에 해당하는 url을 입력받으면, 

`views.py`
```python
from django.http import HttpResponse

def get_list_by_user(request, username):
    return HttpResponse("{}님 안녕하세요!".format(username))
```

이를 view에게 넘겨주고, 이를 변수로 사용할 수 있다.

### 2) use converter
받을 수 있는 변수의 type을 제한하는 기능을 수행한다.

str : 경로 구분자를 제외한 비어 있지 않은 문자열 <br>
path: 경로 구분자를 포함한 비어 있지 않은 문자열 <br>
int : 0 또는 임의의 양의 정수와 일치한다. <br>
slug : 문자 또는 숫자와 하이픈 및 밑줄 문자로 구성된 슬러그 문자열과 일치한다. <br>

`urls.py`
```python
urlpatterns = [
    path('<username>/<int:articleId>', views.get_user_article),  
]

```

`views.py`
```python
def get_user_article(request, username, articleId):
    print("username : ", username)
    print("articleId", articleId)
    return HttpResponse("{}의 블로그 {}번 글이 출력됩니다!".format(username, articleId))
```
ex. http://127.0.0.1:8000/euidong/1

## 4. 추가 인자 넘겨주기
`urls.py`
```python
urlpatterns = [
    path('<username>/', views.get_list_by_user, {'foo':'bar'}),
]
```

`views.py`
```python
def get_list_by_user(request, username, foo):
    print("username : ", username)
    return HttpResponse("{}의 블로그 글 리스트가 출력됩니다!{}".format(username, foo))
```

# Re_path
정규식을 통해서 url을 표현한다. <br>
이를 통해 조금 더 추가적인 기능을 구현하기 편리하다.
    - r는 정규식임을 알립니다.
    - ^는 정규식 시작 기호
    - $는 정규식 종료 기호

## 1. Base
`views.py`
```python
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^startEnd/$', views.get_start_end),
    re_path(r'^startOnly/', views.get_start_only),
]
```

시작 후에 반드시 종료해줄 필요는 없지만 종료하지 않으면 뒤로 오는 url이 무엇이든 모두 해당 url로 이동한다.

`views.py`
```python
from django.http import HttpResponse


def get_start_end(request):
    return HttpResponse("정규식 시작기호 종료기호 둘 다 있는 경우")


def get_start_only(request):
    return HttpResponse("정규식 시작기호만 있는 경우")
```

http://127.0.0.1:8000/repath/startEnd <br>
http://127.0.0.1:8000/repath/startEnd/abc <br>
http://127.0.0.1:8000/repath/startOnly <br>
http://127.0.0.1:8000/repath/startOnly/abc <br>
http://127.0.0.1:8000/repath/startOnly/abc/1/2/3 <br>
를 실행하는 경우, 2번째만 실패한다.

## 2. url로 변수받기
`urls.py`
```python
urlpatterns = [
    re_path(r'^position-parameter/(010[1-9]\d{7})$', views.get_cellphone)
]
```

- [1-9]는 입력값을 1~9로 제한한다는 뜻이다.
- \d{7}은 입력값을 7개 입력해야한다는 뜻이다.

`views.py`
```python
def get_cellphone(request, cellphone):
    return HttpResponse("휴대폰번호는 {} 입니다.".format(cellphone)
```

http://127.0.0.1:8000/repath/position-parameter/01055557777 <br>
http://127.0.0.1:8000/repath/position-parameter/01099995555 <br>
http://127.0.0.1:8000/repath/position-parameter/0105555777 <br>
를 실행하는 경우, 2번째만 실패한다.
