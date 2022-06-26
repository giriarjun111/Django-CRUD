from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        return self.title
    


class Employee(models.Model):
    fullname = models.CharField(max_length=150)
    mobile = models.CharField(max_length=15)
    emp_code = models.CharField(max_length=3)
    position = models.ForeignKey(Position, models.SET_NULL, blank=True,null=True,)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.fullname
    

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    subject = models.TextField()

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"

    def __str__(self):
        return self.name
    