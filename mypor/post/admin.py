from django.contrib import admin
from post.models import Post   # models.py로부터 Post 모델 가져오기 
# Register your models here.

admin.site.register(Post)  #Post를 관리자 페이지에 등록한다
