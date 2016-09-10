from django.db import models

# Create your models here.
class Post(models.Model): #장고 모델은 클래스에서 모델클래스를 상속받으면 모델이됨
    content = models.TextField(max_length = 500) # 255자 넘는 경우 TextField 씀
    tags = models.ManyToManyField('Tag')
    # 게시물에 tag를 다는거니깐! Many to many는 그냥 생각흐름대로.
    # Tag를 문자열로 넣어야 에러안남 - 왜냐면 Tag Class는 아래 선언되어있어서 현 시점에서는 모름(name error)

    created_at = models.DateTimeField(auto_now_add = True) # 처음으로 추가될 때 자동으로 시간 넣어줌
    updated_at = models.DateTimeField(auto_now = True) # 수정할때 마다 자동으로 시간 넣어줌
    # model filed는 모델필드 Class(ex. DateTimeField)로 만들면 됨
    # 이거하고 ./manage.py makemigrations photos
    # ./manage.py migrate photos
    # 이렇게하면 Table이 생성됨. 앱명_모델명 (photos_Post)

    def __str__(self):
        return '글 번호: {}'.format(self.pk)

    class Meta:
        ordering = ('-created_at', '-pk',) #작성된 시간 역순, pk역순 (-)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True) # 처음으로 추가될 때 자동으로 시간 넣어줌
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '댓글 번호: {}'.format(self.pk)


class Tag(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add = True) # 처음으로 추가될 때 자동으로 시간 넣어줌
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '태그 번호: {}'.format(self.pk)
