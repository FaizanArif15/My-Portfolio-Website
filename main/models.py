from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField()
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    
     # Your fields here
    class Meta:
        app_label = 'main'  # Explicitly set the app label
        
class Certificate(models.Model):
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=200)  # e.g., "Coursera", "Udemy"
    description = models.TextField()
    credential_link = models.URLField(blank=True)
    #image = models.ImageField(upload_to='certificates/', blank=True)
    #image = models.ImageField(upload_to='certificate_images/', null=True, blank=True)

    def __str__(self):
        return self.title