from django.contrib import admin
from post.models import Post   # models.py로부터 Post 모델 가져오기 
# Register your models here.




#Post를 관리자 페이지에 등록한다
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category','Option','location','Modified_date')