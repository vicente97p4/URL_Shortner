from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from shortener.forms import RegisterForm
from shortener.models import Users

# Create your views here.

# �옣怨좊뒗 �뿬�윭 誘몃뱾�썾�뼱瑜� 嫄곗퀜�꽌 �뱾�뼱�삤怨� �떎�뻾�릺寃� �맂�떎.
# 誘몃뱾�썾�뼱瑜� 嫄곗퀜�꽌 �굹�삱 �븣 �븿�닔�뿉 諛섎뱶�떆 request瑜� �씤�옄濡� 二쇨쾶 �릺�뼱�엳�떎.
# 洹몃옒�꽌 views�뿉 �엳�뒗 �븿�닔�뿉�뒗 request瑜� �씤�옄濡� 諛섎뱶�떆 �쟻�뼱以섏빞 �븳�떎.
def index(request):
    user = Users.objects.filter(id=request.user.id).first()
    email = user.email if user else 'Anonymous User!'
    print(request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = 'Anonymous User!'
    print(email)
    return render(request, 'base.html', {'welcome_msg': f'Hello!! {email}', })


@csrf_exempt
def get_user(request, user_id):
    print(user_id)
    if request.method == 'GET':
        abc = request.GET.get('abc')
        xyz = request.GET.get('xyz')
        user = Users.objects.filter(pk=user_id).first()
        return render(request, 'base.html', {'user':user, 'params': [abc, xyz]})
    elif request.method == 'POST':
        username = request.GET.get('username')
        if username:
            user = Users.objects.filter(pk=user_id).update(username=username)
            
            return JsonResponse(status=201, data=dict(msg='You just reached with Post Method!!'), safe=False)
        
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        msg = '올바르지 않은 데이터입니다.'
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg = '회원가입 완료'
        return render(request, 'register.html', {'form':form, 'msg':msg})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        msg = '가입되어 있지 않거나 로그인 정보가 잘못 되었습니다.'
        print(form.is_valid)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password = raw_password)
            if user is not None:
                msg='로그인 성공'
                login(request, user)
        return render(request, 'login.html', {'form':form, 'msg':msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    
def logout_view(request):
    logout(request)
    return redirect('index')