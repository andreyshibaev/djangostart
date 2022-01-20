from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.myblog, name='myblog'),
    path('<int:post_id>/', views.showpost, name="post_detail"),

]