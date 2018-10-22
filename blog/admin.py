from django.contrib import admin
from .models import Post #Post모델 import

#관리자 페이지에서 만든 모델을 보기 위해
admin.site.register(Post)