from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):

    user = models.ForeignKey('auth.User')

    CLASS_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('ST', 'Staff'),
    )

    in_class = models.CharField(
        max_length=1,
        choices=CLASS_CHOICES,
        help_text='For identifying your bingo group',
    )

    GENDERS = (
        ('B', 'Bro'),
        ('S', 'Sis'),
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDERS,
        help_text='For identifying your bingo group',
    )

    # homegroups have different boards
    HG_CHOICES = (
        (1, 'HG1'),
        (2, 'HG2'),
        (3, 'HG3'),
    )

    in_hg = models.CharField(
        primary_key=True,
        max_length=1,
        choices=HG_CHOICES,
        help_text='The homegroup you are in',
    )

    def __str__(self):
        return self.of_user


class Board(models.Model):
    BOARD_NAME_CHOICES = (
        (1, 'HG1'),
        (2, 'HG2'),
        (3, 'HG3'),
    )

    name = models.CharField(
        primary_key=True,
        max_length=1,
        choices=BOARD_NAME_CHOICES,
        help_text='Name of board.',
    )

    def __str__(self):
        return self.name, " Board"


class Square(models.Model):
    square_text = models.CharField(
        max_length=200,
        unique=True,
        help_text='Text in board\'s square.',
    )

    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Square: ", self.name, " in Board ", self.of_board


class Commitment(models.Model):
    user = models.ForeignKey('auth.User')

    square = models.ForeignKey(
        Square,
        on_delete=models.CASCADE,
    )

    completed = models.BooleanField(
        max_length=1,
        default='False',
    )

    completed_date = models.DateField(
        blank=True,
        null=True,
    )

    def mark_finished(self):
        self.completed = 'True'
        self.completed_date = timezone.now()
        self.save()
