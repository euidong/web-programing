# Django-restframework

Django에서 restframework를 구현하기 위해서는 serializer라는 대상을 사용해야한다.
해당 대상을 통해 model의 값을 받고, 이를 JSON형태로 출력할 수 있다.

따라서, 기존 방식대로 models.py를 작성하고, 이를 import하여 serializers.py를 만든다.<br>
그 후에 views.py에서 models.py와 serializers를 같이 import하여 JSON형태로 출력할 수 있도록 한다.


***
출처 : [django-restframework 홈페이지](https://django-rest-framework.org)
