from django.shortcuts import render
from .models import Post
from django.views import generic 
from django.views.generic import TemplateView
from .models import Contact


class HomePageView(TemplateView):
  template_name = "home.html"


class ResumeView(TemplateView):
  template_name = "resume.html"


class AboutView(TemplateView):
  template_name = "about_us.html"


class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'


class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'
  

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        
    return render(request, 'contact.html')
