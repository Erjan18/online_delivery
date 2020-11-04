from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100,null=True)



class Products(models.Model):
    CATEGORY = (
        ('Телефон','Телефон'),
        ('Компьютер','Компьютер'),
        ('Видеокарта', 'Видеокарта'),
        ('Жесткий диск', 'Жесткий диск'),
    )
    name = models.CharField(max_length=50,null=True)
    category = models.CharField(max_length=50,null=True,choices=CATEGORY)
    price = models.FloatField(null=True)
    descryption = models.CharField(max_length=50,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tag = models.ManyToManyField(Tag,null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address =  models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100,null=True)
    img_field = models.ImageField(null=True,blank=True)
    github_link = models.CharField(null=True,blank=True,max_length=100)
    insta_link = models.CharField(null=True, blank=True,max_length=100)
    twitter_link = models.CharField(null=True, blank=True,max_length=100)
    facebook_link = models.CharField(null=True, blank=True,max_length=100)

    def __str__(self):
        return self.full_name



class Order(models.Model):
    Status = (
    ('Pending', 'Pending'),
    ('Delivered', 'Delivered'),
    ('Not delivered', 'Not delivered'),

    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,null=True,choices=Status)

    def __str__(self):
        return self.product.name