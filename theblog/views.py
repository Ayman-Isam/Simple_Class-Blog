from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy

#def home(request):
    #return render(request, 'home.html',{})
class Homeview(ListView):
    model = Post
    template_name = 'home.html'
    cats = Category.objects.all()
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all
        context = super(Homeview, self).get_context_data(*args, **kwargs)
        context ["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categories_list.html', {'cat_menu_list':cat_menu_list})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__iexact=cats.title().replace('-',' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context ["cat_menu"] = cat_menu
        return context

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_post.html'    
    fields = '__all__'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

