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
from FreshWeb.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('indexWeb',indexShows,name='indexShow'),
    path('about',aboutShows),
    path('contact',contactShows),
    path('blog',blogShows),
    path('login',loginShows, name='loginShows'),
    path('logout/',logoutShows),
    path('register',registerShows),
    path('wishlist',wishlistShows),
    path('cart/', cartShows, name='cartShows'),
    path('cart/<str:email>/', cartShows, name='cartShow'),
    path('cart/<int:id>/', cartShows, name='cartShowsWithId'),
    path('cart/<int:id>/<str:email>/',cartShows, name='cartShowsWithIdAndEmail'),
    path('cart/remove/<int:id>/', removeFromCart, name='removeFromCart'),  # Ensure this view exists or create it
    path('update_quantity/', cart_update, name='cartupdate'),
    path('checkOut/',checkOutShows,name="checkShow"),
    path('checkOut/<str:email>/',checkOutShows,name="checkShow"),
    path('faq',faqShows),
    path('policy',policyShows),
    path('blog-details',blogDetailShows),
    path('forget',forgetShows),
    path('about',aboutShows),
    path('contact',contactShows),
    path('blog',blogShows),
    path('product/<id>',productShows),
    path('shop/', shopShowsAll, name='shopShowsAll'),
    path('shop/<str:cat>/', shopShows, name='shopShows'),
    path('policy',policyShows),
    path('terms',termShows),
    path('wishlist/',wishlistShows),
    path('wishlist/<int:id>/<str:email>/', wishlistShows),
    path("Email",EmailSend)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
