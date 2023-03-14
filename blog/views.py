from django.shortcuts import render, redirect
from .models import Post, Contact
from django.http import HttpResponse
from .forms import CommentForm, ContactForm

def index(request):

    posts = Post.objects.all()     

    params = {'posts':posts}

    return render(request, "blog/index.html", params)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    
    form = ""
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()

                return redirect('post_detail', slug=post.slug)
        else:
            form = CommentForm()
    #Slide

    params = {'post':post, 'form':form}

    return render(request, 'blog/post_detail.html', params)


def contacts(request):
      form = ''

      if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False) 
            return render(request, 'blog/successful.html')
        else:
             form = ContactForm()

      params = {'form':form}

      return render(request, 'blog/contact.html', params)

def blogs(request):
    posts = Post.objects.all()     
    params = {'posts':posts}
    return render(request, "blog/blogs.html", params)