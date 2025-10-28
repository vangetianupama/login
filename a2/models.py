from django.db import models

class HRLogin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='Hyderabad')
    experience = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.CharField(max_length=255)
    posted_on = models.DateField(auto_now_add=True)
    last_date_to_apply = models.DateField()

    def __str__(self):
        return self.job_title
