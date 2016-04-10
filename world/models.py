from django.db import models
from django.utils import timezone


class Branch(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=100)
    passport_data = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Suit(models.Model):
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100, null=True, blank=True)
    vendor_code = models.CharField(max_length=10)
    year_issue = models.IntegerField()
    details = models.TextField(max_length=100)
    colour = models.CharField(max_length=50)
    rent_price = models.IntegerField()
    item_price = models.IntegerField()
    note = models.CharField(max_length=50, null=True, blank=True)
    branch = models.ForeignKey(Branch)


    def __str__(self):
        return self.name


class SuitToSize(models.Model):
    suit = models.ForeignKey(Suit)
    size = models.IntegerField()
    count = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.suit.name


class SuitToRent(models.Model):
    suit_to_size = models.ForeignKey(SuitToSize)
    count = models.IntegerField()
    start_date = models.DateTimeField(
            default=timezone.now)
    end_date = models.DateTimeField(
            default=timezone.now)
    people = models.ForeignKey(People)
    total_price = models.IntegerField()
    user = models.ForeignKey('auth.User')
    published_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.suit_to_size.suit.name


class UserToBranch(models.Model):
    user = models.ForeignKey('auth.User')
    branch = models.ForeignKey(Branch)

    def __str__(self):
        return self.branch.name
