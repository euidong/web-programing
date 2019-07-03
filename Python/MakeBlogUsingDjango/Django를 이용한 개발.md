# 개발 순서 

### 1. python을 설치한다.
  - 가상환경 설정했는지 잘 확인 합시다.
  
### 2. python code를 개발할 IDE를 선택한다.
  - pycharm , Atom, anaconda, visual 등 등
  
### 3. virtual envirment를 구성한다.
  - 안해주면 여러가지 module들이 엉켜서 완전 망가질 수 있습니다.
  - pip를 최신 버전으로 업데이트 합니다. `python -m pip install --upgrade pip`
  - consol에 `python -m venv myvenv`를 한다.
  - 또는, 알아서 가상환경을 IDE에서 구성해준다.
  
### 4. virtual envirment에 pip를 이용하여 API를 설치한다.
  - Django 설치 `pip install django`
  
### 5. Django를 이용하여 project를 시작한다.
  - 프로젝트 시작 : `django-admin startproject [프로젝트명] . `
  - 프로젝트에서 새로운 app 시작 : `python manage.py startapp [app의 이름]`
  
### 6. 만들어진 file의 settings.py를 입맛에 따라 수정한다.
  - 새로운 model을 추가하거나 다른 형태의 개발을 수행하고자 한다면, 이를 settings.py의 INSTALLED_APPS에 추가한다.
  - database 어떤 것을 사용할 것인지 작성(sqlite가 django의 기본 db) [다른 db연동하기](https://github.com/euidong/web-programing/blob/master/Python/MakeBlogUsingDjango/Mysql%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0.md)
  - timezone 확인 하기.
  - INSTALLED_APPS에 사용할 app 추가. (물론 처음 시작할 때 만든 app도 마찬가지) 
  - TEMPLATES에서 'DIRS'는 기본 경로인데 이를 'DIRS': [os.path.join(BASE_DIR, 'templates')] 로 하면 settings.py의 경로에서 templates폴더 안에 있는 것을 기본 경로로 한다. (여기서 os는 python에서 경로를 지정할 때 쓰이는 모듈이다.)
  - 그 밖에 추가 사항 반드시 기록할 것
  
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'khu_alarm',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]    
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```

### 7. DB와 MODEL을 연결하기
  - model은 DB의 table과 mapping 됩니다.
  - 해당 model에서 만들고 그 형태를 migration으로 만들고(makemigrations), 이를 바탕으로 DB에 반영합니다.(migrate) 
  - 어떤 model을 사용할 것인지 정의해야합니다.
  - 해당 model을 정의하였다면, 이를 바탕으로 database를 생성할 수 있도록 consol을 키고 명령어를 실행해주어야합니다.


migration 생성

```
(myvenv) ~/djangogirls$ python manage.py makemigrations blog
Migrations for 'blog':
  blog/migrations/0001_initial.py:
  - Create model [model명]
```

DB에 model 저장

```
(myvenv) ~/djangogirls$ python manage.py migrate blog
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Rendering model states... DONE
  Applying blog.0001_initial... OK
```

migration은 data를 db에 저장하기 위해 model의 형태를 저장하고 이에 model에 알맞게 데이터를 저장한다.

<strong>역순으로 DB에 이미 있는 것을 Model과 연동하는 것도 해보고 싶지만, 아직 필요성을 못느껴서 일단은 다음 기회에.... </strong>

### 8. html 문서를 작성한다.
  static 일반적인 html문서를 작성한다.
  보통 base.html 같은 형태로 기본적인 틀을 갖추는 html문서이다.
  어떤 css를 적용할 것이고, site에서나 공통적으로 보여줄 어는 요소를 선택한다.
  
```html
{% load static %}

<html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <title>KHUropBox</title>

    <script src="/static/js/app.js"></script>

    <link href="/static/css/app.css" rel="stylesheet">
    <link href="/static/css/common.css" rel="stylesheet">
    <link href="/static/css/override.css" rel="stylesheet">
    <link href="/static/css/layout.css" rel="stylesheet">
    <link href="/static/css/filebrowser.css" rel="stylesheet">
    <link href="/static/css/font-awesome.min.css" rel="stylesheet">


</head>
<body>
    <div id="wrapper">
        <div id="page-content-wrapper">

             <div id="header">
                <div id="logo">
                    <a href="/"></a>
                </div>
             </div>

             <div id="content">
                 <div class="panel panel-default">
                    <div class="panel-heading">
                        {{ request.user.username }}  님 안녕하세요.
                        <button type="submit" class="btn right" onclick="location.href='/logout/';">로그아웃</button>
                        <button type="submit" class="btn right" onclick="location.href='/blog/';">게시판</button>
                        {% if user.is_authenticated %}
                            <button type="submit" class="btn right" onclick= location.href='/';>메인메뉴</button>
                            <button type="submit" class="btn right" onclick="location.href='{% url 'post_new' %}';">글쓰기</button>
                            <button type="submit" class="btn right" onclick="location.href='{% url 'post_draft_list' %}';">미리보기</button>

                        {% endif %}
                    </div>
                    <div class="panel-body">
                        {% block content %}
                        {% endblock %}
                   </div>
      </div>
  </div>

</body>
</html>
```
  - {% load static %} = static 폴더의 내용을 참고하겠다. import의 기능을합니다. 보통 font, css, image 등을 불러옵니다.
  - `<meta charset ="utf-8">`은 필수입니다. (한국어 입력을 위함)
  - static에 있는 css, logo 등을 활용해줍니다.
  - {{ if }} 내용 {{ endif }} if 구문 잘 활용합시다.
  - {% block content %} {% endblock %} 은 다른 html 문서에서 해당 base.html문서를 불러오고 block 내부만 정의 할 수 있습니다.
    <br> {% extends 'blog/base.html' %} {% block content %} 내용 {% endblock %}

### 9. 해당 html 문서를 어떤 식으로 보여줄지를 views.py를 통해 결정한다.
  - html에 어떤 인자를 넘겨줄지 어떤식으로 보여줄지를 판단하여 이를 정합니다.
  - render형태로 return을 수행합니다.
  - render(request, html문서, 추가로 보내줄 요소) 형태로 return 하는 것을 기본으로 한다.
  - model로 부터 인자를 건내받을 수 있습니다. 즉, DB에 데이터를 넣거나 빼고 조회하는 행위를 수행할 수 있습니다.
  
```python
from django.shortcuts import render
from .models import Notice

# Create your views here.

def test_view(request) :
    notices = Notice.objects.all()
    context = {'notices':notices}
    return render(request, 'main.html', context)
```
  
  
### 10. urls.py에 해당 view를 어떤 경우 보여줄지 결정한다.
  - 주소창에 어떤 값을 입력했을 때 어떤 view를 보여줄 것인지를 urls.py를 통해 판단합니다.
```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_view, name ='test'),
    path('admin/', admin.site.urls),
]
```
[URL 설정 방법](https://github.com/euidong/web-programing/blob/master/Python/MakeBlogUsingDjango/URL%20%EC%84%A4%EC%A0%95%EB%B2%95.md)
