# Model 기본 설정법

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

# Model Method 

save() - 저장 시 마다 특정 동작을 추가할 수 있습니다.

# Model Relation
두 개 이상의 Model이 서로 관계를 가지는 경우가 존재한다.<br>
예를 들어 게시판의 댓글 기능을 만든다고 하자. <br>
이때, 어느 게시글에 어떤 댓길이 달렸는지를 지정해줄 필요가 있다.
이 기능을 구현하기 위해 post table에 모든 chat을 추가하는 것은 매우 제한적인 선택이다. <br>
따라서, 테이블을 두 개로 분리하고 post의 name을 통해 chat에서 post에 해당하는 db를 불러오도록하는 것이 효과적이다.
이때 쓸 수 있는 keyword가 foriegn key와 many to many 등이다. 검색해볼 것. 설명은 참고자료에 잘 나와 있음.

# META CLASS

META CLASS를 통해 초기값 등을 설정해줄 수 있다.

정렬 기준을 정해주거나 db에 저장되는 table명을 지정할 수 있다.

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()            
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'post'
        ordering = ['title']
        
```



***

참고자료 :[https://nukggul.tistory.com/17](https://nukggul.tistory.com/17)
