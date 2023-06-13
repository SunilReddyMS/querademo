from django.shortcuts import render,redirect
from .models import signup

# Create your views here.
def sign(request):
    if request.method=='POST':
        l=request.POST['l']
        p=request.POST['p']
        c1=signup.objects.create(user=l,passwd=p)
        c1.save()
        return redirect('/login')
    return render(request,'signup.html')


def login(request):
    if request.method=='POST':
        l=request.POST['l']
        p=request.POST['p']
        c1=signup.objects.all()
        for i in c1:
            if l==i.user:
                if p==i.passwd:
                    return redirect('/post')
        return render(request,'login.html',{'r':'INVALID DETAILS'})
    return render(request,'login.html')
        

