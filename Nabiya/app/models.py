from django.db import models
from django.contrib.auth.models import User

from django.utils.timezone import now


# Create your models here.

class Emotion(models.Model):
    EMOTIONS = (
        ('H', 'happy'),
        ('S', 'sad'),
        ('A', 'angry')
    )
    status = models.CharField(max_length=1, choices=EMOTIONS)

    def __str__(self):
        return self.status

# 동물 프로필 이미지 저장 경로 설정
def profile_directory_path(user, filename):
    # file will be uploaded to MEDIA_ROOT/post/user_<id>/<filename>
    return 'pet_profile/user_{0}/{1}'.format(user.id, filename)

class Pet(models.Model):
    SPECIES = (
        ('D', 'dog'),
        ('C', 'cat')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pets")
    species = models.CharField(max_length=1, choices=SPECIES)
    name = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to=profile_directory_path)
    birth = models.DateField(default=now)

    class Meta:
        unique_together = (('owner', 'name'))

    def __str__(self):
        return self.name

# 자주 기록하는 할 일 태그로 등록
class Tag(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=6)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="tags")

class Tag(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=6)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="tags")

    def __str__(self):
        return self.name



def photo_directory_path(writer, filename):
    # file will be uploaded to MEDIA_ROOT/post/user_<id>/<filename>
    return 'diary/user_{0}/{1}'.format(writer.pk, filename)

class Diary(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="posts", null=True)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, related_name="posts", null=True)
    uploaded = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to=photo_directory_path, blank=True, null=True)
    content = models.TextField(max_length=100, null=True)


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    photo = models.ImageField(upload_to="post/%Y/%m/%d/")
    uploaded = models.DateField(auto_now_add=True)

# Post 모델 구현할 때 같이 구현
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=50)
    uploaded = models.DateField(auto_now_add=True)

