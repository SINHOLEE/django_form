# 복습 및 새로 시작.

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

   