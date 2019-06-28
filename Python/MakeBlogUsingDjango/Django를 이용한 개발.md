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
  - database 어떤 것을 사용할 것인지 작성(sqlite가 django의 기본 db)
  - timezone 확인 하기.
  - 그 밖에 추가 사항 반드시 기록할 것
  
  ```python
    LANGUAGE_CODE = 'ko-kr'
    TIME_ZONE = 'Asia/Seoul'
  ```
* 그냥 html을 화면에 띄우고 싶다면 manage.py 폴더에서 templates 폴더를 만들고 그 안에 html 파일을 넣으면 된다. 

### 7. models.py에 만들고자 하는 model추가
  - 어떤 model을 사용할 것인지 정의해야합니다.
  - 해당 model을 정의하였다면, 이를 바탕으로 database를 생성할 수 있도록 consol을 키고 명령어를 실행해주어야합니다.

`migration 생성`
```
(myvenv) ~/djangogirls$ python manage.py makemigrations blog
Migrations for 'blog':
  blog/migrations/0001_initial.py:
  - Create model [model명]
```

`migrate에 model 저장`
```
(myvenv) ~/djangogirls$ python manage.py migrate blog
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Rendering model states... DONE
  Applying blog.0001_initial... OK
```
  * migration은 data를 db에 저장하기 위해 model의 형태를 저장하고 이에 model에 알맞게 데이터를 저장한다. <br>
  대신 'DIRS': [os.path.join(BASE_DIR, 'templates')],
  
### 8. html 문서를 우선적으로 작성한다.
  static하고 일반적인 html문서를 작성한다.
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
  - {% load static %} = static 폴더의 내용을 참고하겠다. import의 기능을합니다.
  - `<meta charset ="utf-8">`은 필수입니다. (한국어 입력을 위함)
  - static에 있는 css, logo 등을 활용해줍니다.
  - {{ if }} 내용 {{ endif }} if 구문 잘 활용합시다.
  - {% block content %} {% endblock %} 은 다른 html 문서에서 해당 base.html문서를 불러올 수 있습니다.
    <br> {% extends 'blog/base.html' %} {% block content %} 내용 {% endblock %}

### 9. 해당 html 문서를 어떤 식으로 보여줄지를 views.py를 통해 결정한다.
  - html에 어떤 인자를 넘겨줄지 어떤식으로 보여줄지를 판단하여 이를 정합니다.
  
### 10. html 문서를 수정한다.
  - html을 동적으로 볼 수 있도록 code를 수정하고 표현합니다.
  - div를 이용하는 방식이 동적으로 보여주기에는 좋습니다.
  
### 11. urls.py에 해당 view를 어떤 경우 보여줄지 결정한다.
  - 주소창에 어떤 값을 입력했을 때 어떤 view를 보여줄 것인지를 urls.py를 통해 판단합니다.
  
