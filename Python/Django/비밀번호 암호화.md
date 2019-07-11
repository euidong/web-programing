# 비밀번호 암호화  

비밀번호를 암호화하여 저장하기 위한 각종 알고리즘이 존재한다. 하지만, django에서 기본으로 제공하는 hashing함수가 있다.

django.contrib.auth.models.User에 존재하는 함수를 이용하여 입력된 비밀번호를 set하고, check할 수 있다.
 
+ from django.contrib.auth.hashers import is_password_usable를 하여 해당 비밀번호의 타당성도 check할 수 있다.

user.check_password(암호화 전 password)

user.set_password(암호화 전 password)

```python
class signIn(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            raise PermissionDenied
        context = {'message':'hello'}
        return render(request, 'sign_in.html', context)

    def post(self, request, format=None):
        if request.user.is_authenticated:
            raise PermissionDenied
        users = User.objects.all()
        for user in users:
            if request.data['email'] == user.email:
                if user.check_password(request.data['password']):
                    login(request, user)
                    return redirect('/')
                else :
                    context ={'message' : 'password is wrong'}
                    return render(request, 'sign_in.html', context)
        context = {'message': 'email is not exist!!'}
        return render(request, 'sign_in.html', context)
```

```python
class signUp(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            raise PermissionDenied
        return render(request, 'sign_up.html')
    def post(self, request, format=None):
        if request.user.is_authenticated:
            raise PermissionDenied

        users = User.objects.all()
        for user in users:
            if user.email == request.data['email']:
                return render(request, 'sign_up.html', {'message':'already existed email.'})
        
        if is_password_usable(request.data['password']) and request.data['first_name'] != '' and request.data['last_name'] != '':
            user = User.objects.create_user(username= request.data['username'],email= request.data['email']) 
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.set_password(request.data['password'])
            user.save() 
            return redirect('/sign_in')
        else:
            return render(request, 'sign_up.html', {'message': 'wrong input.'})
```
