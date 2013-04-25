#standard model stuff
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="program_images",null=True,blank=True)
    international = models.BooleanField(default=False)

    @models.permalink
    def get_absolute_url(self):
        return ('program_detail', [self.pk])
    def __unicode__(self):
        return self.name

admin.site.register(Program)

class Course(models.Model):
    program = models.ForeignKey(Program)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="program_images",null=True,blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('course_detail', [self.pk])
    def __unicode__(self):
        return str(self.program) + ": " + self.name

admin.site.register(Course)

class CETCourse(models.Model):
    name = models.CharField(max_length=300)
    def __unicode__(self):
        return self.name
admin.site.register(CETCourse)

class CertificateApplication(models.Model):
    student_id = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    major = models.CharField(max_length=200)
    courses = models.ManyToManyField(CETCourse,verbose_name="CET courses taken",blank=True)
    address = models.CharField(max_length=200)
    GPA = models.FloatField(blank=False)
    comments = models.TextField(blank=True,null=True)
    def __unicode__(self):
        return self.full_name + ", GPA:" + str(self.GPA)

admin.site.register(CertificateApplication)

