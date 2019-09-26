from django.shortcuts import render, redirect, get_object_or_404  # 데이터 하나만 꺼내올 때
from .models import Article
from .forms import ArticleForm # 이제 CREATE 함수를 바꿔야 함


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request,'articles/index.html', context)


# GET으로 들어오면 생성하는 페이지 rendering
# POST 로 들어오면 생성하는 로직 수행
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:index')
        # else:  # 사용자가 입력한 값이 잘못되어 있다면 다시 사용자에게 보내준다. 왜? 사용자에게 재입력을 권유하기 위해
        #     context = {'form': form}
        #     return render(request, 'articles/create.html', context)
    else:
        form = ArticleForm()
    context = {'form':form}
    return render(request, 'articles/create.html',context)
        


# detail
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)