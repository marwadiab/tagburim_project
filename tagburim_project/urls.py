"""
URL configuration for tagburim_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_app',('main_app.urls')),
]

"Student page"
urlpatterns =[
    path('student/request-privet/', views.request_individual, name='request_privet'),
]
"""path('student/cancel-privet/', views.cancel_individual, name='cancel_privet')
    path('student/response/', views.response, name='response'),
    path('student/request-group/', views.request_group, name='request_group')
    path('student/cancel-group/', views.cancel_group, name='cancel_group')
    path('student/system/', views.system, name='system')"""

urlpatterns =[

]