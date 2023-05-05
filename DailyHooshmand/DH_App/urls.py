from . import views
from django.urls import path

urlpatterns = [
  path('',views.HomePageView.as_view(), name='home'),
  path('resume/',views.ResumeView.as_view(), name='resume'),
  path('about_us/',views.AboutView.as_view(), name='about_us'),
  path('blog/', views.PostList.as_view(), name="blog"),
  path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
  path('/contact/', views.contact, name="contact"),
]