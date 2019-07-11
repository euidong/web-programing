# Model 설정법

makemigrations, migrate를 진행할 때 model을 기반으로 수행한다.

따라서, 프로젝트의 db의 table의 첫 번째 row의 값을 설정하는 단계이다.

방식은 다음과 같다.

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()            
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
```

1) 먼저 django의 db에 있는 models를 import해준다.
2) 원하는 데이터의 col을 원하는 만큼 생성한다. 이때 타입은 model의 field를 통해 결정해준다.
<br> [참고(django field 종류)](https://docs.djangoproject.com/en/2.2/ref/models/fields/)
3) db와 연동되는데 기본적으로 django는 postgreSQL을 사용할 것을 권장한다는 것을 알아두자.
4) PRIMARY KEY, FORIEN KEY 등 DB 연결 등에 쓰이는 각종 키워드도 존재한다.
