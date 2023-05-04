from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from blog.models import Article, Category

# Create your views here.
@login_required(login_url='login')
def list(request):

    # Sacar articulos
    articles = Article.objects.all()

    # Paginar articulos
    paginator = Paginator(articles, 2)

    # Recoger numero pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Aritculos',
        'articles': page_articles
    })

@login_required(login_url='login')
def category(request, category_id):
    
    category = Category.objects.get(id=category_id)

    return render(request, 'categories/category.html',{
        'category': category
    })
@login_required(login_url='login')
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html',{
        'article' : article
    })