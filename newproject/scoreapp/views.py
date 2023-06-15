
from django.http import HttpResponse

from django.shortcuts import render


def demo(request):
    name="india"
    return render(request,"index.html",{'obj':name})

def operation(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    sum=x+y
    difference=x-y
    multiplying=x*y
    division=x/y

    return render(request,"result.html",{'result1':sum,'result2':difference,'result3':multiplying,'result4':division})




# Create your views here.
