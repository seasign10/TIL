from rest_framework.response import Response
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny # AllowAny 전체 허용
# from rest_framework.authentication import JSONWebTokenAuthentication
from django.contrib.auth import get_user_model
from .serializers import TodoSerializer, UserCreationSerializer, UserSerializer
from .models import Todo

User = get_user_model()

# Create your views here.


@api_view(['POST'])
# 아래의 두가지는 생략이 가능, settings.py에서 DEFAULT 로 REST_FRAMEWORK 설정을 했기 때문
# 1. 인증 받은 사용자만 허가(로그인 여부만 체크)
# @permission_classes((IsAuthenticated, ))
# 2. jwt 인증
# @authentication_classes((JSONWebTokenAuthentication))
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400) # bad request => 400

@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, id): # django안에서만 사용하는 것이 아닌, 범용적이기 때문에 api사용시에는 id 사용
    todo = get_object_or_404(Todo, pk=id) # djago에서 가리키는 id => pk, 기존의 todo
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data) # 현재 데이터 정보, data => 새로 작성할 todo
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        todo.delete()
        # 204 : 해당하는 컨텐츠가 없는 경우 (삭제를 했기 때문에 해당 데이터가 이제 존재하지 않음을 알려줌)
        return Response(status=204)

@api_view(['POST'])
# 모두에게 접근 허용(로그인 여부 판단 안함)
@permission_classes((AllowAny, ))
def user_signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        # print(serializer.data)
        return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})

@api_view(['GET'])
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    if request.user != user:
        # return Response(status=403) 
        # 클라이언트는 콘텐츠에 접근할 권리를 가지고 있지 않음. 
        # 401과 다르게 403은 클라이언트가 누구인지 알고 있다. 
        # (인증은 맞지만 권한이 없는 유저)
        return HttpResponseForbidden()
    serializer = UserSerializer(user)
    return Response(serializer.data)
