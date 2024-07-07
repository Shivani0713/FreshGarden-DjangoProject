from django.shortcuts import render,redirect
from FreshAdmin.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json

###################### Registration,login and logout ####################
def register(request):
    if request.method == 'POST':
        data=request.POST
        email = data.get('email')
        password = data.get('password')
        username = data.get('name') 
        user = User.objects.filter(username = email)
        if user.exists():
            return redirect('./register')
        user = User.objects.create(email = email,password=password,username=username)
        user.set_password(password)
        user.save()
        return redirect('./register')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email,password=password)
        if user is not None:
            request.session['username'] = email
            return redirect("./indexAdmin")
        else:
            return render(request,"signin.html",{'error_message': 'Invaild Credentials'})
    return render(request,'signin.html')

def logout(request):
    del request.session['username']
    return render(request,'signin.html')


# Create your views here.
def indexShows(request):
    p = Products.objects.all().count()
    c = Category.objects.all().count()
    s = subCategory.objects.all().count()
    i = Inventry.objects.all().count()
    context={
        "pCount" : p,
        'cCount' : c,
        'sCount' : s,
        'iCount' : i
    }
    return render(request,'indexAdmin.html',context)


# def categoryShows(request):
#     return render(request,'add-category.html')

###################### category ####################
def AddCategory(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        # slug = data.get('slug')
        sortdescription = data.get('sortdescription')
        fulldescription = data.get('fulldescription')
        group_tag = data.get('group_tag')
        Category.objects.create(
            name = name,
            # slug = slug,
            sortdescription = sortdescription,
            fulldescription = fulldescription,
            group_tag = group_tag
        )
        return redirect('../category/')
    a = Category.objects.all()
    context={
        'table':a
    }
    return render(request,"add-category.html",context)

def UpCategory(request,id):
    print(id)
    queryset=Category.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        data = request.POST
        name = data.get('name')
        # slug = data.get('slug')
        sortdescription = data.get('sortdescription')
        fulldescription = data.get('fulldescription')
        group_tag = data.get('group_tag')
        queryset.name = name
        # queryset.slug = slug
        queryset.sortdescription = sortdescription
        queryset.fulldescription = fulldescription
        queryset.group_tag = group_tag
        queryset.save()
        return redirect('../category/')
    context = {'update':queryset}
    return render(request,"update-category.html",context)
    
def delCategory(request,id):
    a = Category.objects.get(id=id)
    a.delete()
    return redirect('../category/')


############### Subcategory #######################
# def subCategoryShows(request):
#     return render(request,"add-sub-category.html")

def AddSubCategory(request):
    if request.method == 'POST':
        data = request.POST
        category = data.get('category')
        name = data.get('name')
        # slug = data.get('slug')
        sortdescription = data.get('sortdescription')
        fulldescription = data.get('fulldescription')
        group_tag = data.get('group_tag')
        subCategory.objects.create(
            category = category,
            name = name,
            # slug = slug,
            sortdescription = sortdescription,
            fulldescription = fulldescription,
            group_tag = group_tag
        )
        return redirect('../subcategory/')
    a = Category.objects.all()
    b = subCategory.objects.all()
    context={
        'table':a,
        'subtable':b
        }
    return render(request,"add-sub-category.html",context)

def UpsubCategory(request,id):
    print(id)
    queryset=subCategory.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        category = data.get('category')
        name = data.get('name')
        # slug = data.get('slug')
        sortdescription = data.get('sortdescription')
        fulldescription = data.get('fulldescription')
        group_tag = data.get('group_tag')
        queryset.category = category
        queryset.name = name
        # queryset.slug = slug
        queryset.sortdescription = sortdescription
        queryset.fulldescription = fulldescription
        queryset.group_tag = group_tag
        queryset.save()
        return redirect('../subcategory/')
    a = Category.objects.all()
    context = {'subupdate':queryset,'table':a}
    return render(request,"update-sub-category.html",context)
    
def delsubCategory(request,id):
    a = subCategory.objects.get(id=id)
    a.delete()
    return redirect('../subcategory/')

########################## Product ##########################
# def productShows(request):
#     return render(request,'add-product.html')
def AddProduct(request):
    if request.method == 'POST':
        data = request.POST
        photoM = request.FILES.get('photoM')
        # photo1 = request.FILES.get('photo1')
        # photo2 = request.FILES.get('photo2')
        # photo3 = request.FILES.get('photo3')
        name = data.get('name')
        productCat = data.get('productCat')
        # slug = data.get('slug')
        sortdescription = data.get('sortdescription')
        fulldescription = data.get('fulldescription')
        packtype = data.get('packtype')
        size = data.get('size')
        price = data.get('price')
        quantity = data.get('quantity')
        group_tag = data.get('group_tag')
        fulldescription = data.get('fulldescription')
        Products.objects.create(
            productCat = productCat,
            photoM = photoM,
            # photo1 = photo1,
            # photo2 = photo2,
            # photo3 = photo3,
            name = name,
            # slug = slug,
            sortdescription = sortdescription,
            fulldescription = fulldescription,
            packtype = packtype,
            size = size,
            price = price,
            quantity = quantity,
            group_tag = group_tag
        )
        return redirect('../product/')
    a = Category.objects.all()
    b = subCategory.objects.all()
    context={
        'table':a,
        'subtable':b
        }
    return render(request,"add-product.html",context)

def inventrylistShows(request):
    b = Products.objects.all()
    c = Inventry.objects.all()
    context={
        'product':b,
        'inventry':c
        }
    return render(request,'inventry-list.html',context)

def productlistShows(request):
    a = subCategory.objects.all()
    b = Products.objects.all()
    context={
        'product':b,
        'subcat':a
        }
    return render(request,'product-list.html',context)

def UpProduct(request,id):
    print(id)
    queryset=Products.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        photoM = request.FILES.get('photoM')
        # photo1 = request.FILES.get('photo1')
        # photo2 = request.FILES.get('photo2')
        # photo3 = request.FILES.get('photo3')
        name = data.get('name')
        productCat = data.get('productCat')
        # slug = data.get('slug')
        sortdescription = data.get('sortdescription')
        fulldescription = data.get('fulldescription')
        packtype = data.get('packtype')
        size = data.get('size')
        price = data.get('price')
        quantity = data.get('quantity')
        group_tag = data.get('group_tag')
        fulldescription = data.get('fulldescription')
        queryset.photoM = photoM
        # queryset.photoM = photo1
        # queryset.photoM = photo2
        # queryset.photoM = photo3
        queryset.productCat = productCat
        queryset.packtype = packtype
        queryset.size = size
        queryset.price = price
        queryset.quantity = quantity
        queryset.name = name
        # queryset.slug = slug
        queryset.sortdescription = sortdescription
        queryset.fulldescription = fulldescription
        queryset.group_tag = group_tag
        queryset.save()
        return redirect('./productlist/')
    a = Category.objects.all()
    b = subCategory.objects.all()
    context={
        'table':a,
        'subtable':b,
        'proupdate':queryset
        }
    return render(request,"update-product.html",context)
    
def delProduct(request,id):
    a = Products.objects.get(id=id)
    a.delete()
    return redirect('../productlist/')

########################### Inventry #####################
def AddInverty(request):
    if request.method == 'POST':
        data = request.POST
        photoM = request.FILES.get('photoM')
        name = data.get('name')
        offer = data.get('offer')
        stock = data.get('stock')
        purchase = data.get('purchase')
        date= data.get('date')
        status = data.get('status')
        Inventry.objects.create(
            photoM = photoM,
            name = name,
            offer = offer,
            stock = stock,
            purchase = purchase,
            date = date,
            status = status
        )
        return redirect('../inventrylist/')
    b = Products.objects.all()
    product_data = []
    for product in b:
        # Assuming 'image' is the field in your model containing the image URL
        product_data.append({
            'name': product.name,
            'image_url': product.photoM.url, # Adjust this according to your model
        })
        product_data_json = json.dumps(product_data)
    context = {
        'products': product_data_json,
        'product':b
    }
    return render(request,'add-inventry.html',context)

def UpInverty(request,id):
    print(id)
    queryset=Inventry.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        photoM = request.FILES.get('photoM')
        name = data.get('name')
        offer = data.get('offer')
        stock = data.get('stock')
        purchase = data.get('purchase')
        date_str = data.get('date') 
        status = data.get('status')
        queryset.photoM = photoM
        queryset.name = name
        queryset.offer = offer
        queryset.stock = stock
        queryset.purchase = purchase
        queryset.status = status
        queryset.date = date_str
        queryset.save()
        return redirect('../inventrylist/')
    context = {'invupdate':queryset}
    return render(request,"update-inventry.html",context)

def delInventry(request,id):
    a = Inventry.objects.get(id=id)
    a.delete()
    return redirect('../inventry/')

def faqShows(request):
    return render(request,'faq.html')
def faqShows(request):
    return render(request,'faq.html')
def forgotShows(request):
    return render(request,'forgot.html')

def invoiceShows(request):
    return render(request,'invoice.html')
def orderlistShows(request):
    return render(request,'order-list.html')
def rememberShows(request):
    return render(request,'remember.html')
def resetShows(request):
    return render(request,'reset-password.html')

########################### Vendor ################
def vendorProfileShows(request):
    if 'username' in request.session:
        username = request.session['username']
        user = User.objects.get(username=username)
        context = {
            'user': user
        }
    return render(request,'vendor-profile.html',context)

def vendorUpdateShows(request):
    if 'username' in request.session:
        username = request.session['username']
        user = User.objects.get(username=username)
        if request.method == 'POST':
            data=request.POST
            email = data.get('email')
            new_username = data.get('username')
            user.email = email
            user.username = new_username
            # Save the updated user object
            user.save()
            # Optionally, you can update the session with the new username
            request.session['username'] = new_username
        context = {
            'user': user
        }
        return render(request, 'vendor-profile.html', context)
