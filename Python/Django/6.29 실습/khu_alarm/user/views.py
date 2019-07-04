from django.shortcuts import render, redirect
from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def sign_in(request) :
    if request.method == "POST" :
        for valid_user in User.objects.all():
            if valid_user.email == request.POST['email'] and valid_user.password == request.POST['password'] :
                return redirect('notice/')
        return render(request, "sign_in.html", {"message" : "Email과 Password를 다시입력해주세요."})
    else :
        return render(request, 'sign_in.html', {})
    
@api_view(['GET', 'POST'])
def sign_up(request) :
    if request.method == "POST" :
        # email, password, first_name, last_name 모두 입력하였고
        # email이 중첩되지 않은 경우
        if  request.POST['email'] == '' or request.POST['password'] == '' or request.POST['first_name'] == '' or request.POST['last_name'] == '' :
            return render(request, 'sign_up.html',{"message" : "잘못된 입력입니다. 다시입력해주세요."})
        else :
            for already_user in User.objects.all() :
                if already_user.email == request.POST['email'] :
                     return render(request, 'sign_up.html',{"message" : "잘못된 입력입니다. 다시입력해주세요."})
            new_user = [request.POST['email'],request.POST['password'],request.POST['first_name'],request.POST['last_name']]
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():    
                serializer.save()
                return redirect('/')
    else :
        return render(request, 'sign_up.html', {})



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