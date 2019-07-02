# Django-restframework

Django에서 restframework를 구현하기 위해서는 serializer라는 대상을 사용해야한다.
해당 대상을 통해 model의 값을 받고, 이를 JSON형태로 출력할 수 있다.

따라서, 기존 방식대로 models.py를 작성하고, 이를 import하여 serializers.py를 만든다.<br>
그 후에 views.py에서 models.py와 serializers를 같이 import하여 JSON형태로 출력할 수 있도록 한다.


`models.py`
```python
from django.db import models

# Create your models here.

class User(models.Model) :
    email = models.EmailField(primary_key = True)
    password = models.CharField(max_length = 20)
    first_name = models.CharField(max_length= 10)
    last_name = models.CharField(max_length = 10)
        
    class Meta :
        ordering = ('first_name', )

```


`serializers.py`
```python

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 20)
    first_name = serializers.CharField(max_length= 10)
    last_name = serializers.CharField(max_length = 10)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.url = validated_data.get('url', instance.url)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
```


`views.py`
```python
from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def user_list(request) :
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
***
참고 : [django-restframework 홈페이지](https://django-rest-framework.org)
