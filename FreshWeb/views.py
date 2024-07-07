from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, Http404
from django.http import JsonResponse
from FreshAdmin.models import *
from FreshWeb.models import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from decimal import Decimal
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render

def EmailSend(request):
    if request.method == 'POST':
        data=request.POST
        uname=data.get('name')
        con=data.get('contact')
        print(uname,con)
        subject = uname
        message = 'Helloooooo'
        from_email = 'shivanisuman1968@gmail.com'
        recipient_list = ['shivanisharma0713@gmail.com']
        send_mail(subject, message, from_email, recipient_list)
    return render(request, 'Email.html')

def indexShows(request):
    # Fetch all categories
    categories = Category.objects.all()
    a = list( Category.objects.all())
    category_pairs = [(a[i], a[i+1]) for i in range(0, len(a), 2)]
    b = Inventry.objects.all()
    c = Products.objects.all()
    d = subCategory.objects.all()
    e = Products.objects.all()[:6]
    w = Wishlist.objects.all().count()
    print(w)

    # Dictionary to store category-wise product counts
    category_counts = {}

    # Iterate over categories
    for category in categories:
        # Get the name of the category
        category_name = category.name

        # Initialize count for the category
        category_count = 0

        # Fetch subcategories for the category
        subcategories = subCategory.objects.filter(category=category_name)

        # Iterate over subcategories
        for subcategory in subcategories:
            # Count the number of products for each subcategory
            product_count = Products.objects.filter(productCat=subcategory.name).count()
            
            # Debugging print statement
            # print(f"Subcategory: {subcategory.name}, Product count: {product_count}")

            category_count += product_count

        # Store the total count for the category
        category_counts[category_name] = category_count

    context = {
        'category_counts': category_counts,
        'inventry': b,
        'categories': categories,
        'product':c,
        'subCat':d,
        'popular':e,
        'category_pairs': category_pairs,
        'w':w
    }
    return render(request, 'indexWeb.html', context)

def aboutShows(request):
    queryset=Products.objects.all()
    categories = Category.objects.all()
    w = Wishlist.objects.all().count()
    context={
        'proShow': queryset,
        'categories': categories,
        'w':w
    }
    return render(request,'about.html',context)

def contactShows(request):
    if request.method == 'POST':
        data=request.POST
        uname=data.get('name')
        con=data.get('phone')
        email = data.get("email")
        msg = data.get("msg")
        subject = uname
        message = f"Hello {uname},\n\n\t{msg}\n\nBest Regards,\n\tFreshGarden"
        from_email = 'shivanisuman1968@gmail.com'
        recipient_list = [email]
        
        send_mail(subject, message, from_email, recipient_list)
    queryset=Products.objects.all()
    categories = Category.objects.all()
    w = Wishlist.objects.all().count()
    context={
        'proShow': queryset,
        'categories': categories,
        'w':w
    }
    return render(request,'contact-us.html',context)


def blogShows(request):
    queryset=Products.objects.all()
    w = Wishlist.objects.all().count()
    categories = Category.objects.all()
    context={
        'proShow': queryset,
        'categories': categories,
        'w':w
    }
    return render(request,'blog.html',context)

def registerShows(request):
    if request.method == 'POST':
        username = request.POST.get('first_name')
        password = request.POST.get('password')
        # last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            return redirect('./register')  # Adjust the URL name as needed
        user = User.objects.create(email = email,password=password,username=username)
        user.set_password(password)
        user.save()
        return redirect('./login')  # Adjust the URL name as needed
    queryset=Products.objects.all()
    categories = Category.objects.all()
    w = Wishlist.objects.all().count()
    context={
        'proShow': queryset,
        'categories': categories,
        'w':w
    }
    return render(request, 'register.html',context)

def loginShows(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email,password=password)
        if user is not None:
            request.session['username'] = email
            return redirect("./indexWeb")
        else:
            return render(request,"register.html",{'error_message': 'Invaild Credentials'})
    queryset=Products.objects.all()
    categories = Category.objects.all()
    w = Wishlist.objects.all().count()
    context={
        'proShow': queryset,
        'categories': categories,
        'w':w
    }
    return render(request,'login.html',context)

def logoutShows(request):
    del request.session['username']
    return render(request,'login.html')

def wishlistShows(request):
    queryset=Products.objects.all()
    categories = Category.objects.all()
    w = Wishlist.objects.all().count()
    context={
        'proShow': queryset,
        'categories': categories,
        'w':w
    }
    return render(request,'wishlist.html',context)


def faqShows(request):
    queryset=Products.objects.all()
    categories = Category.objects.all()
    w = Wishlist.objects.all().count()
    context={
        'proShow': queryset,
        'categories': categories,
        'w':w
    }
    return render(request,'faqWeb.html',context)

def forgetShows(request):
    queryset=Products.objects.all()
    categories = Category.objects.all()
    w = Wishlist.objects.all().count()
    context={
        'proShow': queryset,
        'categories': categories,
        'w':w
    }
    return render(request,'forgot.html',context)

def policyShows(request):
    queryset=Products.objects.all()
    categories = Category.objects.all()
    w = Wishlist.objects.all().count()
    context={
        'proShow': queryset,
        'categories': categories,
        'w':w
    }
    return render(request,'policy.html',context)

def blogDetailShows(request):
    queryset=Products.objects.all()
    categories = Category.objects.all()
    w = Wishlist.objects.all().count()
    context={
        'proShow': queryset,
        'categories': categories,
        'w':w
    }
    return render(request,'blog-details.html',context)


def shopShows(request, cat=None):
     # Fetch all categories
    categories = Category.objects.all()
    a = list( Category.objects.all())
    category_pairs = [(a[i], a[i+1]) for i in range(0, len(a), 2)]
    c = Products.objects.all()
    e = Products.objects.all()[:6]

    # Dictionary to store category-wise product counts
    category_counts = {}

    # Iterate over categories
    for category in categories:
        # Get the name of the category
        category_name = category.name

        # Initialize count for the category
        category_count = 0

        # Fetch subcategories for the category
        subcategories = subCategory.objects.filter(category=category_name)

        # Iterate over subcategories
        for subcategory in subcategories:
            # Count the number of products for each subcategory
            product_count = Products.objects.filter(productCat=subcategory.name).count()
            
            # Debugging print statement
            # print(f"Subcategory: {subcategory.name}, Product count: {product_count}")

            category_count += product_count

        # Store the total count for the category
        category_counts[category_name] = category_count

    # Fetch all necessary data
    i = Inventry.objects.all()
    d = subCategory.objects.all()
    w = Wishlist.objects.all().count()
    categories = Category.objects.all()

    # If a category is specified, filter products based on the category
    if cat:
        subcategories = subCategory.objects.filter(category=cat)
        p = Products.objects.filter(productCat__in=[sub.name for sub in subcategories])
    else:
        p = Products.objects.all()

    ####### category name and count ##########
    category_counts = {}
    for category in categories:
        category_name = category.name
        subcategories = subCategory.objects.filter(category=category_name)
        category_count = Products.objects.filter(productCat__in=[sub.name for sub in subcategories]).count()
        category_counts[category_name] = category_count

    # Pagination
    paginator = Paginator(p, 12)  # 12 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'count': p.count(),
        'invent': i,
        'product': p,
        'page_obj': page_obj,
        'category_counts': category_counts,
        'categories': categories,
        'subCat': d,
        'w': w,
        'category_counts': category_counts,
        'inventry': i,
        'product':c,
        'popular':e,
        'category_pairs': category_pairs,
    }
    return render(request, 'shop.html', context)



def shopShowsAll(request, cat=None):
     # Fetch all categories
    categories = Category.objects.all()
    a = list( Category.objects.all())
    category_pairs = [(a[i], a[i+1]) for i in range(0, len(a), 2)]
    c = Products.objects.all()
    e = Products.objects.all()[:6]

    # Dictionary to store category-wise product counts
    category_counts = {}

    # Iterate over categories
    for category in categories:
        # Get the name of the category
        category_name = category.name

        # Initialize count for the category
        category_count = 0

        # Fetch subcategories for the category
        subcategories = subCategory.objects.filter(category=category_name)

        # Iterate over subcategories
        for subcategory in subcategories:
            # Count the number of products for each subcategory
            product_count = Products.objects.filter(productCat=subcategory.name).count()
            
            # Debugging print statement
            # print(f"Subcategory: {subcategory.name}, Product count: {product_count}")

            category_count += product_count

        # Store the total count for the category
        category_counts[category_name] = category_count

    # Fetch all necessary data
    i = Inventry.objects.all()
    d = subCategory.objects.all()
    w = Wishlist.objects.all().count()
    categories = Category.objects.all()

    # If a category is specified, filter products based on the category
    if cat:
        subcategories = subCategory.objects.filter(category=cat)
        p = Products.objects.filter(productCat__in=[sub.name for sub in subcategories])
    else:
        p = Products.objects.all()

    ####### category name and count ##########
    category_counts = {}
    for category in categories:
        category_name = category.name
        subcategories = subCategory.objects.filter(category=category_name)
        category_count = Products.objects.filter(productCat__in=[sub.name for sub in subcategories]).count()
        category_counts[category_name] = category_count

    # Pagination
    paginator = Paginator(p, 12)  # 12 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'count': p.count(),
        'invent': i,
        'product': p,
        'page_obj': page_obj,
        'category_counts': category_counts,
        'categories': categories,
        'subCat': d,
        'w': w,
        'category_counts': category_counts,
        'inventry': i,
        'product':c,
        'popular':e,
        'category_pairs': category_pairs,
    }
    return render(request, 'shopAll.html', context)



################# Product ###################
def productShows(request,id):
    print(id)
    queryset=Products.objects.get(id=id)
    categories = Category.objects.all()
    w = Wishlist.objects.all().count()
    context={
        'proShow': queryset,
        'categories': categories,
        'w':w
    }
    return render(request,'product.html',context)

def policyShows(request):
    w = Wishlist.objects.all().count()
    context={
        'w':w
    }
    return render(request,'policy.html',context)

def termShows(request):
    w = Wishlist.objects.all().count()
    context={
        'w':w
    }
    return render(request,'terms.html',context)

def wishlistShows(request,id=None, email=None):
    if id is not None and email is not None:  # Check both id and email
        try:
            # Check if the product with the given id already exists in the cart
            if Wishlist.objects.filter(wishId=id, username=email).exists():
               return redirect('/freshWeb/wishlist/')

            # If the product doesn't exist in the cart, proceed to add it
            queryset = Products.objects.get(id=id)
            productid = id
            productname = queryset.name
            productimage = queryset.photoM
            productprice = queryset.price

            Wishlist.objects.create(
                wishId=productid,
                wishName=productname,
                wishImg=productimage,
                wishValue=productprice,
                username=email
            )
        except Products.DoesNotExist:
            raise Http404("Product does not exist")

        # Redirect to the same view without parameters to remove them from the URL
        return HttpResponseRedirect('/freshWeb/wishlist/')
    elif id is not None and email is None:
        return redirect('/freshWeb/login/')
    else:  
        all_wishes = Wishlist.objects.all()
        w = Wishlist.objects.all().count()
        return render(request, 'wishlist.html', {'wishes': all_wishes,'w':w})


############## Cart #############
def removeFromCart(request, id):
    try:
        cart_item = NewCart.objects.get(productId=id, username=request.session['username'])
        cart_item.delete()
    except NewCart.DoesNotExist:
        pass
    return redirect('/freshWeb/cart/')

# @login_required
def cartShows(request, id=None, email=None):
    # Handling addition of products to the cart
    if id is not None and email is not None:  
        try:
            product = get_object_or_404(Products, id=id)
            cart_item, created = NewCart.objects.get_or_create(productId=id, username=email,productQuantity=1)
            if not created:
                cart_item.productQuantity = (cart_item.productQuantity or 0) + 1
                cart_item.save()
            else:
                # If it's a new item, fetch its details from the Products model
                product = Products.objects.get(id=id)
                cart_item.productName = product.name
                cart_item.productImg = product.photoM
                cart_item.productValue = product.price
                cart_item.save()
            return redirect('/freshWeb/cart/')
        except Products.DoesNotExist:
            raise Http404("Product does not exist")

    # Redirect to login page if user is not logged in
    elif id is not None and email is None:
        return redirect('/freshWeb/login/')
    
    # Handling checkout process
    if request.method == 'POST':
        email = request.POST.get('email')
        # Fetch all products in the cart for the specified user
        all_products = NewCart.objects.filter(username=email)
        total_subtotal = Decimal('0.0')  # Initialize total subtotal as Decimal
        # Loop through each product in the cart
        for product in all_products:
            if product.productValue is not None and product.productQuantity is not None:
                # Calculate subtotal for the current product
                product_value = float(product.productValue)  # Convert Decimal to float
                product_quantity = int(product.productQuantity)
                # Calculate subtotal for the current product
                subtotal = Decimal(product_value * product_quantity)  # Convert result to Decimal
                total_subtotal += subtotal  # Add subtotal to the total
                # Save or update data in Checkouts model
                existing_checkout_item = Checkouts.objects.filter(productName=product.productName, username=email).first()
                if existing_checkout_item:
                    # If the product exists, update quantity and subtotal
                    existing_checkout_item.quantity += product_quantity
                    existing_checkout_item.subtotal += subtotal
                    existing_checkout_item.save()
                else:
                    # If the product doesn't exist, create a new Checkout entry
                    Checkouts.objects.create(
                        productName=product.productName,
                        productValue=product.productValue,
                        quantity=product.productQuantity,
                        subtotal=subtotal,
                        username=product.username
                    )
        
        # Clear the cart after saving data to Checkouts model
        # all_products.delete()
        # Redirect to the checkout page
        return render(request, 'checkout.html', {'total_subtotal': total_subtotal})

    # Fetch cart items
    all_products = NewCart.objects.all()
    categories = Category.objects.all()
    w = Wishlist.objects.all().count()
    context={
        'w':w,
        'all_product': all_products, 
        'categories': categories
    }

    return render(request, 'cart.html',context)

def cart_update(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')

        # Get the quantity from the request
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity is not provided
        print(action)
        # Perform actions based on the action
        cart_item, created = NewCart.objects.get_or_create(productId=product_id)
        
        # Update the quantity based on the action
        if action == 'increase':
            cart_item.productQuantity += 1
            print(cart_item.productQuantity)
        elif action == 'decrease':
            if cart_item.productQuantity> 1:
                cart_item.productQuantity -= 1
                print(cart_item.productQuantity)

        # Save the updated cart item
        cart_item.save()
        return JsonResponse({'message': 'Cart updated successfully', 'quantity': cart_item.productQuantity}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def checkOutShows(request,email=None):
    queryset=Products.objects.all()
    categories = Category.objects.all()
    checkouts = Checkouts.objects.filter(username=email)
    product = NewCart.objects.all()
    total = checkouts.aggregate(Sum('subtotal'))['subtotal__sum'] or 0
    w = Wishlist.objects.all().count()
    context = {
        'checkouts': checkouts,
        'total': total,
        'products' : product,
        'proShow': queryset,
        'categories': categories,
        'w':w
    }
    
    return render(request, 'checkout.html', context)



