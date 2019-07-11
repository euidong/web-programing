# template

Django에서는 html에 붙여서 사용할 수 있는 기능을 부여하였다.

이를 통해 page를 더 다채롭게 보여주는 것이 가능하다.

if, for, extends, block, context get 이 핵심 기능이고 이를 설명하겠다.

### context get

django에서는 context를 get하기 위해서 views.py에서 context라는 dictionary를 보내줄 수 있다.
해당 dictionary에 있는 모든 key값을 마음대로 사용할 수 있다.

ex) 

`views.py`
```python
    def post(self, request, format=None):
        context = {'id' : request.data['id'], 'password': request.data['password'], 'message': 'what the fuck'}
        return render(request,'output.html', context)
```

`output.html`
```html
    {{id}}
    {{password}}
    {{message}}
```

{{}}안에 context를 통해 보내주는 대상의 key값을 입력하면 value를 얻을 수 있다.


### extends, blcok
html파일을 엮을 수 있게한다.
여러 개의 html 파일의 중복되는 코드를 extends를 통해 불러오고 싶은 html 파일을 불러올 수 있다.<br>
그리고 불러오는 html 파일의 block부분을 필요에 따라 추가할 수 있다.
ex)

`base.html`
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        {% block more %}
        {% endblock %}
    </body>
</html>
```

`login.html`
```html
{% extends 'base.html' %}

{% block more %}
    <div>
        <form method ="POST">
            {% csrf_token %}
            <p> ID </p>
            <input type="text" name ="id">
            <P> PASSWORD </P>
            <input type="password" name ="password"> <br>
            <input type="submit" name = "sign_in" value ="Sign in">
            <input type="button" name ="sign_up" value ="Sign up" onClick="location.href='/sign_up'">
        </form>
    </div>
{% endblock %}
```

### if for

```html
{% if 조건 %}
{% endif %}

{% for a in list %}
{% endfor %}
```
로 구현함.
여기서 list는 context에서 get하는 것.
