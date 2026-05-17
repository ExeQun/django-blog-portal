from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Article, Comment

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 5
    
    def get_queryset(self):
        return Article.objects.filter(status='published').order_by('-published_at')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'
    
    def get_queryset(self):
        return Article.objects.filter(status='published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(is_visible=True)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        author_name = request.POST.get('author_name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        
        if author_name and email and text:
            Comment.objects.create(
                article=self.object,
                author_name=author_name,
                email=email,
                text=text
            )
            messages.success(request, 'Комментарий добавлен!')
        else:
            messages.error(request, 'Ошибка: заполните все поля')
        
        return redirect('article_detail', slug=self.object.slug)