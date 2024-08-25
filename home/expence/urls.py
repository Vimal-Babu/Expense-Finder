from django.contrib import admin
from django.urls import path,include
from expence import views

urlpatterns = [
    # path('', admin.site.urls),
    path('', views.home, name='home'),
    path('expense',views.expense,name='expense')
]
