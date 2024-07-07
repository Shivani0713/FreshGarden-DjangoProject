"""
URL configuration for dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from FreshAdmin.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login',login, name='login'),
    path('register',register),
    path('logout/',logout),
    path('indexAdmin',indexShows),
    # path('category',categoryShows),
    path('category/',AddCategory,name="addCtgry"),
    path('delCategory/<id>',delCategory),
    path('UpCategory/<id>',UpCategory),
    # path('subcategory',subCategoryShows),
    path('subcategory/',AddSubCategory,name="addsubCtgry"),
    path('delsubCategory/<id>',delsubCategory),
    path('UpsubCategory/<id>',UpsubCategory),
    path('product/',AddProduct, name="addPro"),
    path('delProduct/<id>',delProduct),
    path('UpProduct/<id>',UpProduct),
    path('inventry',AddInverty,name="addInve"),
    path('delInventry/<id>',delInventry),
    path('UpInventry/<id>',UpInverty),
    path('faq',faqShows),
    path('forgot',forgotShows),
    path('invoice',invoiceShows),
    path('orderlist',orderlistShows),
    path('productlist/',productlistShows),
    path('inventrylist/',inventrylistShows),
    path('vendorProfile',vendorProfileShows),
    path('vendorUpdate',vendorUpdateShows,name="upvendor"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
