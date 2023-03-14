from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model: (Class, Module, Topics, Assignment ,AssignmentReport)
    
class Module(models.Model):
    module_name = models.CharField(max_length=255, unique=True, null=False)
    description = models.TextField()
    
    def __str__(self):
        return self.module_name
    
class Topics(models.Model):
    topic_title = models.CharField(max_length=255, null=False, unique=True)
    content = models.TextField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.topic_title

class ClassRoom(models.Model):
    class_name = models.CharField(max_length=255, unique=True, null=False)
    created_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.class_name
    
class OngoingModule(models.Model):
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    startPeriod_date = models.DateField()
    endPeriod_date = models.DateField()
    
    def __str__(self):
        return self.module.module_name
    
class Assignment(models.Model):
    title = models.CharField(max_length=255, null=False, unique=True)
    task_file = models.FileField(upload_to='static/assignment/', max_length=255)
    created_date = models.DateField(auto_now=True)
    due_date = models.DateField()
    on_module = models.ForeignKey(OngoingModule, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class AssignmentReport(models.Model):
    student_report = models.FileField(upload_to='static/assignment/report/', max_length=100)
    submited_date = models.DateField(auto_now=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignmet = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.student_report.url
    
class AssignmentReportComment(models.Model):
    comment = models.TextField()
    created_date = models.DateField(auto_now=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(AssignmentReport, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} - {}'.format(self.assignment, self.comment)