from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField('Bio', max_length=150)
    image1 = models.ImageField(
        default='default.jpg', upload_to='profile_images/')
    banner = models.ImageField(
        default='default.jpg', blank=True, upload_to='banner_images/')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def following(self):
        user_ids = Relationship.objects.filter(
            from_user=self.user).values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

    def followers(self):
        user_ids = Relationship.objects.filter(
            to_user=self.user).values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)


class Post(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.content


class Relationship(models.Model):
    from_user = models.ForeignKey(
        User, related_name='relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='related_to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'
