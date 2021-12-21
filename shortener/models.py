import string
import random

from django.db import models
from django.contrib.auth.models import User as U

# Create your models here.


class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)


class Organization(models.Model):
    class Industries(models.TextChoices):
        PERSONAL = 'personal'
        RETAIL = 'retail'
        MANUFACTURING = 'manufacturing'
        IT = 'it'
        OTHERS = 'others'
    name = models.CharField(max_length=50) # 회사 이름
    industry = models.CharField(max_length=15, choices=Industries.choices, default=Industries.OTHERS) # 위 5개 중 1개
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Users(models.Model):
    user = models.OneToOneField(U, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)


class EmailVerification(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, null=True)
    verified = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Categories(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class ShortenedUrls(models.Model):
    class UrlCreatedVia(models.TextChoices):
        WEBSITE = "web"
        TELEGRAM = "telegram"

    def rand_string():
        str_pool = string.digits + string.ascii_letters
        return ("".join([random.choice(str_pool) for _ in range(6)])).lower()

    nick_name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, null=True)
    prefix = models.CharField(max_length=50) # /1234 라는 url이 있다고 해보자, 그럼 9999까지밖에 만들 수 없다. 그래서 앞에 임의의 문자를 두기 위해 만들었다. 나중에는 문자 대신 원하는 identity를 넣는다.
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    target_url = models.CharField(max_length=2000)
    shortened_url = models.CharField(max_length=6, default=rand_string)
    created_via = models.CharField(max_length=8, choices=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
