from django.shortcuts import render
from curdapp2.models import ProductData
from django.http.response import HttpResponse

def Home_view(request):
    return render(request,'home2.html')

def Create_view(request):
    if request.method=='POST':
        pid1=request.POST.get('pid')
        pname1=request.POST.get('pname')
        pcost1=request.POST.get('pcost')
        pclass1=request.POST.get('pclass')
        pcolor1=request.POST.get('pcolor')
        nop1=request.POST.get('nop')
        mfg1=request.POST.get('mfg')
        exp1=request.POST.get('exp')
        cname=request.POST.get('cname')
        mobile1=request.POST.get('mobile')
        email=request.POST.get('email')

        data=ProductData(
            product_id=pid1,
            product_name=pname1,
            product_cost=pcost1,
            product_class=pclass1,
            product_color=pcolor1,
            no_of_products=nop1,
            mfg_date=mfg1,
            exp_date=exp1,
            customer_name=cname,
            mobile_number=mobile1,
            email_id=email
        )
        data.save()
        return render(request,'create2.html')
    else:
        return render(request,'create2.html')

def Retrieve_view(request):
    data2=ProductData.objects.all()
    return render(request,'retrieve.html',{'data2':data2})

def Update_view(request):
    if request.method=='POST':
        pid=request.POST.get('pid')
        pcost=request.POST.get('pcost')

        data3=ProductData.objects.filter(product_id=pid)

        if not data3:
            return HttpResponse('Product is not available...')
        else:
            data3.update(product_cost=pcost)
            return render(request,'update.html')
    else:
        return render(request,'update.html')

def Delete_view(request):
    if request.method=='POST':
        pid=request.POST.get('pid')

        data4=ProductData.objects.filter(product_id=pid)

        if not data4:
            return HttpResponse('Product is not available...')
        else:
            data4.delete()
            return render(request,'delete2.html')
    else:
        return render(request,'delete2.html')