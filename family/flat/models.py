from django.db import models


# Create your models here.
class Member(models.Model):
    flat = models.CharField(max_length=10)  # Flat Number in Charachter field

    def __str__(self):
        return self.flat


class Parent(models.Model):
    family = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='parents')
    Name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)

    def __str__(self):
        return self.Name


class Children(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='childs')  # Foriegn Key for parents
    Name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)

    def __str__(self):
        return self.Name
