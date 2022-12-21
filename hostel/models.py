from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Room(models.Model):
    block_name_choices = [('A', 'A-block'), ('B', 'B-block'),
                          ('C', 'C-block'), ('D', 'D-block'), ('E', 'E-block')]
    room_no = models.IntegerField(primary_key=True, unique=True)
    block_name = models.CharField(
        choices=block_name_choices, max_length=1, default=None, null=True)
    capacity = models.IntegerField(default=1)
    vacancy = models.IntegerField(default=1)

    def __str__(self):
        return str(self.room_no)


class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    roll_no = models.CharField(max_length=10, primary_key=True, unique=True)
    contact_number = PhoneNumberField(null=False, blank=False, unique=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.roll_no)


class Admin(models.Model):
    position_choices = [
        ('G', 'Gsec'), ('H', 'Hall President'), ('W', 'Warden')]
    name = models.CharField(max_length=200, null=True)
    contact_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField()
    position = models.CharField(
        choices=position_choices,
        max_length=1,
        default=None,
        null=True)
