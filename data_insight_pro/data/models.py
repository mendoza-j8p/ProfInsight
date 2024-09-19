from django.db import models

class Professor(models.Model):
    date_joined = models.DateField()
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    years_of_experience = models.PositiveIntegerField()
    publications = models.PositiveIntegerField()
    extra_courses = models.PositiveIntegerField()
    current_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.asignatura}"

