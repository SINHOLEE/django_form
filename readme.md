# 복습 및 새로 시작.

#### Reference

**# Managing static files**
https://docs.djangoproject.com/ko/2.2/howto/static-files/

**# Static Files**
https://docs.djangoproject.com/ko/2.2/ref/settings/#static-files

**# Null vs Blank**
https://wayhome25.github.io/django/2017/09/23/django-blank-null/
https://stackoverflow.com/questions/4384098/in-django-models-py-whats-the-difference-between-default-null-and-blank

**# HTML enctype**
https://www.w3schools.com/tags/att_form_enctype.asp

**# 이미지 파일 필드 사용**
https://docs.djangoproject.com/ko/2.2/faq/usage/#how-do-i-use-image-and-file-fields

**# ImageField**
https://docs.djangoproject.com/en/2.2/ref/models/fields/#imagefield

**# Media Root**
https://docs.djangoproject.com/ko/2.2/ref/settings/#media-root

**# 사용자가 업로드한 파일 제공하기**
https://docs.djangoproject.com/ko/2.2/howto/static-files/#serving-files-uploaded-by-a-user-during-development

**# Favicon 의 모든 것**
https://www.favicon-generator.org/ (edited) 

1. 모델링까지 스킵



2. `python manage.py createsupersuer`

```bash

(venv) C:\Users\student\Django\Django_form>python manage.py createsuperuser
사용자 이름 (leave blank to use 'student'): sinho
이메일 주소:
Password:
Password (again):
Superuser created successfully.
```



3. admin.py

```python
from django.contrib import admin
from .models import Article 
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
```



4. url 설정

   1. <project>/urls.py

      ```python
      from django.contrib import admin
      from django.urls import path, include
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('articles/', include('articles.url')),
      ]
      
      ```

   2. <app>/urls.py 생성하기

      ```python
      # path라는 함수는 당고가 제공하는 메소드
      from django.urls import path
      
      urlpatterns = [
          
      ]
      
      ```

5. <protect>/templates/base.html 생성

6.  project 안에 있는 templates는 당고가 인식을 못함. 이것를 인식하도록 설정하기 위해  settings.py에서 다음과 같이 설정

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           #아래와 같이 설정
           'DIRS': [os.path.join(BASE_DIR, 'myform', 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   
   ```

7. <project>/temlates/base.html 생성 

   ```django
   <!DOCTYPE html>
   <html lang="ko">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
   {% block title %}
   
   {% endblock title %}
   </head>
   {% block body %}
   {% endblock body %}
   </html>
   ```

8. <app>/index 페이지 만들기

   1) urls.py 접근하기

   ```python
   from django.urls import path
   # views 메소드를 사용하기 위해 임포트 한다.
   from . import views
   
   app_name = 'articles'
   # domain/articles/
   urlpatterns = [
       path("", views.index, name='index'),
   ]
   
   ```

   2) views.py 작성

   ```python
   # 모델을 가지고 와야 하므로 임포트 한다.
   from django.shortcuts import render
   from .models import Article
   # Create your views here.
   def index(request):
       articles = Articles.obhects.all()
       context = {'articles' : articles}
       return render(request,'articles/index.html', cntext)
   ```

   3) temlates/articles 폴더 생성

   4) index.html 생성

   ```django
   {% extends 'base.html' %}
   
   {% block title %}
   아티클::Articles
   {% endblock title %}
   
   
   {% block body %}
     <h1>Articles</h1>
     <a href="#">[New]</a>
     <hr>
     {% for article in articles  %}
       <div>
         <h3>{{ article.pk }}번째 글 : {{ article.title }}</h3>
         <p>{{ article.created_at }}</p>
         <a href="#">[Detail]</a>
       </div>
     {% empty %}
     <p>아직 게시글이 없습니다..</p>
       
     {% endfor %}
   {% endblock body %}
   ```

9. 게시글 생성 기능 만들기(임시로 생성)

   1) urls.py 추가

   ```python
       path('create/', views.create, name='create'),
   
   ```

   2) views.py

   ```
   # GET으로 들어오면 생성하는 페이지 rendering
   # POST 로 들어오면 생성하는 로직 수행
   def create(request):
       return render(request, 'articles/create.html') 
   ```

   3)  create.html

   ```
   {% extends 'base.html' %}
   
   {% block title %}
   아티클 생성::Article
   {% endblock title %}
   
   {% block body %}
   <h1>생성하는 페이지 입니다.</h1>
   <a href="{% url 'articles:index' %}">[뒤로가기]</a>
   <hr>
   <form action="#" method='POST'>
     {% csrf_token %}
     <label for="title">타이틀: </label> <br>
     <input type="text" name="title" id="title"><br>
     
     <label for="content">내용:</label><br>
     <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
     <button type="submit">Create</button>
   </form>
   
   {% endblock body %}
   ```

10. 다시 제대로 구성

    - views.py

    ```python
    from django.shortcuts import render, redirect
    # GET으로 들어오면 생성하는 페이지 rendering
    # POST 로 들어오면 생성하는 로직 수행
    def create(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:index')
        return render(request, 'articles/create.html') 
    ```

11. detail page 생성

12. forms.py 만들기 (새로운 개념)

    - form을 사용하는 이유 1: 사용자가 입력하는 모든 입력값을 한번에 받아 그 유효성을 확인할 수 있기 때문

    - form을 사용하는 이유 2: 검증된 데이터(빈공간인지 아닌지, max_length보다 더 썼는지 확인)를 불러옴

    - form을 사용하는 이유 3: html에서 자동으로 생성할 수 있다.

      

    1) forms.py 생성 후 아래와 같이 작성

    ```python
    from django import forms
    
    # 사용자에게 입력받는 Field만 작성
    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=20)
        content = forms.CharField()
    ```

    2) views.py를 다음과 같이 수정

    ```python
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
    ```

    - 주석 다시 확인!

    3) create.html 다음과 같이 수정

    ```django
    {% extends 'base.html' %}
    
    {% block title %}
    아티클 생성::Article
    {% endblock title %}
    
    {% block body %}
    <h1>생성하는 페이지 입니다.</h1>
    <a href="{% url 'articles:index' %}">[뒤로가기]</a>
    <hr>
    <form action="#" method='POST'>
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit">Create</button>
    </form>
    
    {% endblock body %}
    ```

    