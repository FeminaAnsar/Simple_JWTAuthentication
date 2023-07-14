"""
URL configuration for Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from Book import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('registeruser',views.RegisterView.as_view(),name="register"),
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.BookList.as_view(),name="book-list"),
    path('create',views.BookCreateList.as_view(),name="create"),
    path('update/<int:pk>',views.BookUpdate.as_view(),name="book-update"),
    path('delete/<int:pk>',views.BookDelete.as_view(),name="book-delete"),
    path('detail/<int:pk>',views.BookDetail.as_view(),name="book-detail"),

]
