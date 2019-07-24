from django.utils  import timezone
from datetime import date 
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
city_location = (
            ('S','Study_Room'), 
            ('P','Practice_Room'),
            ('C','Concert_Room'),
            ('E','etc'),
            ('?','etc_what'),
            )


def default_city(): # user가 회원가입할 때 지정한? 도시 or seoul
    return "seoul"

class Post(models.Model):
    ITEM_category = (  
        ('study','StudyRoom'), 
        ('performance','PerformanceRoom'),
        ('practice','PracticeRoom'),
        ('etc','etc'),
        )
        
    title = models.CharField(max_length=50)
    context = models.TextField()
    choose_date = models.DurationField() #일정 기간을 저장하는 필드를 만들기
    location = models.CharField(choices=city_location , max_length=30, default=default_city)
    category = MultiSelectField(choices=ITEM_category, max_length=50,default = 'study', blank=True)
    etc_what = models.CharField(max_length=50, null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)  # 글 작성 시간 :  시간이 있는 날짜를 저장하는 datetime 필드를 만들기 
    Modified_date = models.DateTimeField(auto_now=True) # 글 게시 날짜 

    def __str__(self):
        return "RoomShare : {}".format(self.title)
    
    def ROOM_TYPE(self):
        if self.category =='etc':
            return "ROOM etc :{}".format(self.etc_what) 
     