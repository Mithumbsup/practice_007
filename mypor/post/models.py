from django.utils  import timezone
from datetime import date 
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

def default_city(): # user가 회원가입할 때 지정한? 도시 or seoul
    return "seoul"

class Post(models.Model):
    Location_list =(
        ('서울특별시','서울특별시'),
        ('부산광역시','부산광역시'),
        ('세종특별시','세종특별시'),
        ('충청북도','충청북도'),
        ('충청남도','충청남도'),
        ('전라북도','전라북도'),
        ('전라남도','전라남도'),
        ('대구광역시','대구광역시'),
        ('제주특별시','제주특별시'),
        ('경상북도','경상북도'),
        ('경상남도','경상남도'),
        
    )

    Category_list = (  
        ('study','StudyRoom'), 
        ('performance','PerformanceRoom'),
        ('practice','PracticeRoom'),
        ('etc','etc'),
    )
    
    Option_list =(
        ('vim','vim'),
        ('board', 'board'),
        ('desk', 'desk'),
        ('multitap','multitap'),
        ('speaker','speaker'),
        ('lights','lights'),
        ('mirror','mirror'),
        ('air','airconditioner'),
        ('printer','printer'),
    )

        
    title = models.CharField(max_length=50)
    context = models.TextField()
    choose_date = models.DurationField() #!!!!!!! 일정 기간을 저장하는 필드를 만들기    
    '''지역 선택'''
    location = models.CharField(choices=Location_list  , max_length=30, default=default_city)
    '''공간 유형 선택'''
    category = MultiSelectField(choices=Category_list, max_length=50, blank=True)
    etc_what = models.CharField(max_length=50, null=True,blank=True)
    '''물건 대여 선택'''
    Option = MultiSelectField(choices=Option_list, max_length=50,default=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)  # 글 작성 시간 :  시간이 있는 날짜를 저장하는 datetime 필드를 만들기 
    Modified_date = models.DateTimeField(auto_now=True) # 글 게시 날짜 

    def __str__(self):
        return "RoomShare : {}".format(self.title)
    
    def ROOM_TYPE(self):
        if self.category=='etc' :
            return "ROOM etc :{}".format(self.etc_what) 
