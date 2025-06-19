from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    # description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    github = models.URLField(blank=True,null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
class Review(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField(blank=False, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    # approved = models.BooleanField(default=False)



    def __str__(self):
        return f"Review from {self.name}"

    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    subject = models.CharField( max_length=50)
    message = models.TextField()



    def __str__(self):
          return f"{self.name} - {self.subject}"