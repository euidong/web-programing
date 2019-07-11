# authentication

무엇보다 중요한 것은 django에서 지원하는 authentication 기능을 이용하기 위해서는 django 기본 User class를 사용해야한다.

`from django.contrib.auth.models import User`

이를 통해서 확장을 수행해야 쉽게 개발을 진행할 수 있다.

`from django.contrib.auth import login, logout`<br>
을 수행하게 되면 django에서 알아서 login과 logout 상태를 keep해준다.

또한, 이러한 authentication 상황을 알 수 있는 request.user.is_authenticated가 있고,
이를 통해 유저의 authentication 상태를 확인할 수 있다. <br>
현재 authentication 되어 있는 user는 request의 user를 통해 알 수 있다.(name, 등등) <br>

ex)
```python
class main(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            context = {'user' : request.user}
            return render(request, 'main.html')
        else:
            return redirect('/sign_in')
    # logout
    def post(self, request, format=None):
        print (request.data)
        if request.data['logout'] == "logout":
            logout(request)
        return redirect('/')

class signIn(APIView):
    def get(self, request, format=None):
        context = {'message':'hello'}
        return render(request, 'sign_in.html', context)

    def post(self, request, format=None):
        users = User.objects.all()
        for user in users:
            if request.data['email'] == user.email:
                if request.data['password'] == user.password:
                    login(request, user)
                    return redirect('/')
                else :
                    context ={'message' : 'password is wrong'}
                    return render(request, 'sign_in.html', context)
        context = {'message': 'email is not exist!!'}
        return render(request, 'sign_in.html', context)

class signUp(APIView):
    def get(self, request, format=None):
        return render(request, 'sign_up.html')
    def post(self, request, format=None):
        return render(request, 'sign_in.html')

```

#permission

추후 추가
