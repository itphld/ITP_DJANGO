from django.shortcuts import render,HttpResponse
from store.models import Product
def home(request):
    product=Product.objects.all()
    context={'product':product}
    #return HttpResponse("welcome to my page")
    return render(request,'home.html',context)
