from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class ResumeStyle(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='original.jpg', upload_to='resume_style_pics')
    css_file = models.FileField(default='builder/static/builder/resume_style_original.css', upload_to='resume_style_css_files')

    def __str__(self):
        return self.name


class Resume(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(default='Untitled', max_length=300)
    updated_at = models.DateTimeField(auto_now=True)
    style = models.ForeignKey(ResumeStyle, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resume-detail', kwargs={'pk': self.pk})


class PersonalInfo(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=100)
    address = models.TextField()
    personal_profile = models.TextField()
    image = models.ImageField(upload_to='resume_pics')

    def get_absolute_url(self):
        return reverse('resume-detail', kwargs={'pk': self.resume.pk})


class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    from_date = models.CharField(max_length=100)
    to_date = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"Work Experience #{self.pk} at {self.company}"

    def get_absolute_url(self):
        return reverse('resume-detail', kwargs={'pk': self.resume.pk})


class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('resume-detail', kwargs={'pk': self.resume.pk})


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    alma_mater = models.CharField(max_length=300)
    from_date = models.CharField(max_length=100)
    to_date = models.CharField(max_length=100)
    qualification = models.TextField()

    def get_absolute_url(self):
        return reverse('resume-detail', kwargs={'pk': self.resume.pk})










    
