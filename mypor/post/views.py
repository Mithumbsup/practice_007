from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm
from django.http import HttpResponse

# def main(request):
#     post_list = Post.objects.all().order_by('Modified_date')[:10]
#     context = {'post_list': post_list }
#     return render(request, 'post/post_list.html', context)

class IndexView(ListView):
    model = 'Post'
    template_name = 'post/post_list.html' # 디폴트 템플릿명: <app_label>/<model_name>_list.html
    context_object_name = 'post_list' # 디폴트 컨텍스트 변수명 :  object_list
    
    def get_queryset(self): # 컨텍스트 오버라이딩
      return Post.objects.order_by('Modified_date')[:5]

class DetailView(DetailView):
    model = 'Post'# 해당 모델 - URLConf 의 PK 변수를 활용하여 해당 모델의 특정 record를 컨텍스트 변수(object)에 담는다.
    template_name = 'post/post_detail.html' # 디폴트 템플릿명: <app_label>/<model_name>_detail.html
    context_object_name = 'posts' # 디폴트 컨텍스트 변수명 :  object


#create
def post_new(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            # post.Modified_date = request.META['Modified_date']
            post.save()
            return redirect('post:IndexView')
    else:
        form = PostForm()
    return render(request, 'post/post_new.html',{'form':form,})



def word_filter(field_names):
    # data_file = open("C:/Users/user/Desktop/욕목록.txt","r") 
    # words = data_file.read().split(",")
    # sentence = ""
    # for field_name in field_names:
    #     for term in words: 
    #         if term in field_name: 
    #             field_name =  field_name.replace(term, "초롱이") 
    #     sentence = sentence + " " + field_name
    # return(sentence)    
    pass