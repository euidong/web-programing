# QuerySet
Django에서 CRUD의 효율적인 사용을 위해 제공하는 opensource.

models.objects.get(조건)

ex) Notice.objects.get(id= 30)

해당 모델로 구현된 데이터베이스에서 특정 조건에 맞는 데이터 하나를 가져옵니다.

models.objects.filter(조건)

ex) Notice.objects.filter(id=30)

해당 모델로 구현된 데이터베이스에서 특정 조건에 맞는 데이터를 모두 가져옵니다.

models.objects.all()

ex) Notice.objects.all()

해당 모델로 구현된 데이터베이스의 모든 데이터를 가져옵니다. 

가져온 형태는 QUERYSET으로 ALL처럼 여러 개로 가져온 경우, 배열처럼 index로 접근할 수 있다.

또한, 각 각의 value에 접근하기위해서는 .attribute를 해주면된다.


ex)

```python
  personal_notice = Personal_notice.objects.filter(userId_id=request.user.id)
  result_notice = []
  for checker in personal_notice :
      result_notice.append(Khu_ce_notice.objects.get(id=checker.noticeId))
  context ={'context': result_notice}
  return render(request, 'my_notice.html', context)
```
