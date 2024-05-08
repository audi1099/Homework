from django.db import models
import django


class Course(models.Model):
    title = models.CharField(max_length=70, verbose_name="Название курса")
    duration = models.DurationField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = django.db.models.CharField(max_length=200, verbose_name="Название темы")
    duration = models.DurationField()
    discription = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title





