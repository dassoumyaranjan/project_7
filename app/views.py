from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'Ashu','age':'20'}
    return render(request,'h1.html',context=d)

def jinja_operation(request):
    d={'a':90,'b':560}
    return render(request,'h2.html',context=d)

def jinja_ifelif(request):
    d={'a':100}
    return render(request,'h3.html',context=d)

def jinja_nestedif(request):
    d={'a':50,'b':100,'c':200}
    return render(request,'h4.html',context=d)
