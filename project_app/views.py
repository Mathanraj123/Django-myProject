from django.shortcuts import render
from .models import table3
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'index.html')
def checkout(request):
    return render(request,'checkout.html')
def order(request):
    name=request.POST.get("name")
    mobno=request.POST.get("mobno")
    email=request.POST.get("email")
    address1=request.POST.get("address1")
    address2=request.POST.get("address2")
    district=request.POST.get("district")
    state=request.POST.get("state")
    country=request.POST.get("country")
    data={
        "name":name,
        "mobno":mobno,
        "email":email,
        "address1":address1,
        "address2":address2,
        "district":district,
        "state":state,
        "country":country,
        }
    data1=table3(name=name,mobno=mobno,email=email,address1=address1,address2=address2,district=district,state=state,country=country)
    data1.save()
    send_mail(
        "LeoWatch's",
        "Thanks Ordering in our Website Here your Order will reach soon as soon.",
        "m2raj@example.com",
        [email],
        fail_silently=False,
    )
    return render(request,'order.html',data)