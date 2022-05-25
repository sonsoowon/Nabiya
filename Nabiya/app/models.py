
from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit



# Create your models here.

class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name="followers")


class Emotion(models.Model):
    EMOTIONS = (
        ('H', 'happy'),
        ('S', 'sad'),
        ('A', 'angry'),
        ('D', 'depressed'),
        ('E', 'exciting')
    )

    status = models.CharField(max_length=1, choices=EMOTIONS)
    emoji = models.ImageField(upload_to="emoji/")

    def __str__(self):
        return self.status


class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pets")
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = (('owner', 'name'))

    def __str__(self):
        return self.name



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/post/user_<id>/<filename>
    return 'post/user_{0}/{1}'.format(instance.user.id, filename)

class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="posts")
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, related_name="posts")
    uploaded = models.DateField(auto_now_add=True)
    photo = ProcessedImageField(
        upload_to=user_directory_path,
        processors=[ResizeToFit(500, 500)],
        format='JPEG'
        )
    content = models.TextField(max_length=100)

    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=50)
    uploaded = models.DateField(auto_now_add=True)

