from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from home import views 



urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('/', views.home_view, name='home'),
    
]
