# Django URL 설정법

### Base
```python
from django.contrib import admin
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



```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('user.urls')),
    path('notice/', views.notice_view, name ='notice'),
    path('admin/', admin.site.urls),
]
```
