from django.db import models


class Resume(models.Model):
    
    full_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.full_name
