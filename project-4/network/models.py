from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="post_user")
    body = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    num_likes = models.IntegerField(blank=True)
    post_pic = models.ImageField(null=True, blank=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user.id,
            "user": self.user.username,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%b %#d %Y, %#I:%M %p"),
            "num_likes": self.num_likes
        }

class Like(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="like_user")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="like_post")
    currently_like = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def serialize(self):
        return {
        "user_id": self.user.id,
        "username": self.user.username,
        "email": self.user.email,
        "post_id": self.post.id,
        "post_owner": self.post.user.username,
        "post_body": self.post.body,
        "post_date": self.post.timestamp.strftime("%b %#d %Y, %#I:%M %p"),
        "like_id": self.id,
        "currently_like": self.currently_like,
        "timestamp": self.timestamp.strftime("%b %#d %Y, %#I:%M %p"),
        }

class Following(models.Model):
    following = models.ForeignKey("User", on_delete=models.CASCADE, related_name="following_user")
    following_list = models.ManyToManyField(User,null=True, blank=True, related_name="following_list")

    def serialize(self):
        return {
        "id": self.following.id,
        "username": self.following.username,
        "email": self.following.email,
        "following_list": [user.email for user in self.following_list.all()]
        }

class Follower(models.Model):
    follower = models.ForeignKey("User", on_delete=models.CASCADE, related_name="follower_user")
    follower_list = models.ManyToManyField(User,null=True, blank=True, related_name="follower_list")
    def serialize(self):
        return {
        "id": self.follower.id,
        "username": self.follower.username,
        "email": self.follower.email,
        "followers_list": [user.email for user in self.follower_list.all()]
        }