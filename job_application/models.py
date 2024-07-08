from django.db import models


class FormDatabase(models.Model):
    firstName = models.CharField(max_length=80)
    lastName = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
