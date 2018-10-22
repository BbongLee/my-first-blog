#models : Post가 장고 모델임을 의미, 장고는 Post가 데이터베이스에 저장되어야 한다고 알게됨
from django.db import models
from django.utils import timezone

#모델(객체) 정의 / 항상 클래스 이름 첫글자는 대문자!
class Post(models.Model): 
	#ForeignKey : 다른 모델에 대한 링크(외래키)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    #CharField : 글자수에 제한된 텍스트. 글 제목같은 짧은 문자열 정보를 저장할 때 사용
    title = models.CharField(max_length=200)
    #TextField : 글자수에 제한이 없는 긴 텍스트. 블로그속성에 좋겠쬬?
    text = models.TextField()
    #DateTimeField : 날짜와 시간 의미
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    #def : 함수/메서드 만들때 예약어, publish 라는 이름의 메서드 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #던더 : 더블 언더스코어
        return self.title #제목 string 리턴