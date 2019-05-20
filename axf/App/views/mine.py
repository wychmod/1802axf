from django.shortcuts import render,redirect,reverse,HttpResponse
from django.contrib.auth import login,logout,authenticate
from App.models import User


def mine(req):
    return render(req,'mine/mine.html')


# 注册
def Register(req):
    if req.method == 'POST':
        username = req.POST.get('userAccount')
        userpass = req.POST.get('userPass')
        email = req.POST.get('email')
        u = User.objects.create_user(username,email,userpass)
        u.save()
        return redirect(reverse('App:login'))
    return render(req,'mine/register.html')


# 登录
def Login(req):
    if req.method == 'POST':
        username = req.POST.get('userAccount')
        userpass = req.POST.get('userPass')
        u = authenticate(username=username, password=userpass)
        if u:
            if u.is_active:
                login(req,u)
                print('登录成功')
                return redirect(reverse('App:mine'))
        return HttpResponse('请输入正确的用户或者密码')
    return render(req,'mine/login.html')


# 退出登录
def Logout(req):
    logout(req)
    return redirect(reverse('App:mine'))