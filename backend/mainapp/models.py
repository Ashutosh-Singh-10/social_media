from django.db import models
import random

def randomPostIdGeneration():
    a=random.randint(10000000,99999999)
    while(len(Post.objects.filter(postId=a))):
        a=random.randint(10000000,99999999)
    return a
    
def randomUserIdGeneration():
    a=random.randint(10000000,99999999)
    while(len(User.objects.filter(userId=a))):
        a=random.randint(10000000,99999999)
    return a
    
        
class User(models.Model):
    email=models.EmailField( max_length=254,blank=False,null=False)
    userId=models.CharField( max_length=254,default=randomUserIdGeneration,primary_key=True)
    password=models.CharField(max_length=50,null=False,blank=False)
    Name=models.CharField( max_length=30,null=False,blank=False)
  
    

class Post(models.Model):
    postId=models.CharField(max_length=50,primary_key=True,default=randomPostIdGeneration)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    postDesc=models.CharField( max_length=50)
    postImg=models.ImageField(upload_to='postImg/',height_field=None, width_field=None,null=True)
    postDate=models.DateField(auto_now_add=True)

class Likes(models.Model):
    room=models.ForeignKey(Post, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
