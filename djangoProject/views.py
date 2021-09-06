from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
def index(request):
    return render(request,"index.html")
def timer(request):
    import time
    ctime=time.time()
    return render(request,"timer.html", {"time":ctime},)
def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else :
        print(request.GET)
        print(request.POST)
        user = request.POST.get("username")
        pwd = request.POST.get("pwd")
        print(user)
        print(pwd)
        log = reverse('log')
        print(type(log))
        if user=="hyk" and pwd=="hyk":
            return HttpResponse("<h1>登录成功</h1>")
        else:
            return render(request,"loginf.html")
    return render(request,"login.html",{"log":log})
def login_t(request):
    html="<h1>登录成功<h1>"
    return HttpResponse(html)
def login_f(request):
    html = "<h1>登录失败<h1>"
    return HttpResponse(html)
def re_path(request):
    return HttpResponse("login_1.html")

# Create your views here.
