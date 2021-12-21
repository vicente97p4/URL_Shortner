import string
import random

from django.db import models
from django.contrib.auth.models import User as U

# Create your models here.
class TimeStampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True # django는 클래스를 테이블을 만들어서 관리한다.
        # 그래서 이렇게 상속시키는 class를 만드려면
        # Meta class에서 abstract = True를 해줘야 한다.


class PayPlan(TimeStampedModel):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    


class Organization(TimeStampedModel):
    class Industries(models.TextChoices):
        PERSONAL = 'personal'
        RETAIL = 'retail'
        MANUFACTURING = 'manufacturing'
        IT = 'it'
        OTHERS = 'others'
    name = models.CharField(max_length=50) # ?쉶?궗 ?씠由?
    industry = models.CharField(max_length=15, choices=Industries.choices, default=Industries.OTHERS) # ?쐞 5媛? 以? 1媛?
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True)


class Users(models.Model):
    user = models.OneToOneField(U, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)


class EmailVerification(TimeStampedModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, null=True)
    verified = models.BooleanField(default=False)
    
    
class Categories(TimeStampedModel):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    
class ShortenedUrls(TimeStampedModel):
    class UrlCreatedVia(models.TextChoices):
        WEBSITE = "web"
        TELEGRAM = "telegram"

    def rand_string():
        str_pool = string.digits + string.ascii_letters
        return ("".join([random.choice(str_pool) for _ in range(6)])).lower()

    nick_name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, null=True)
    prefix = models.CharField(max_length=50) # /1234 ?씪?뒗 url?씠 ?엳?떎怨? ?빐蹂댁옄, 洹몃읆 9999源뚯??諛뽰뿉 留뚮뱾 ?닔 ?뾾?떎. 洹몃옒?꽌 ?븵?뿉 ?엫?쓽?쓽 臾몄옄瑜? ?몢湲? ?쐞?빐 留뚮뱾?뿀?떎. ?굹以묒뿉?뒗 臾몄옄 ????떊 ?썝?븯?뒗 identity瑜? ?꽔?뒗?떎.
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    target_url = models.CharField(max_length=2000)
    shortened_url = models.CharField(max_length=6, default=rand_string)
    created_via = models.CharField(max_length=8, choices=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
    expired_at = models.DateTimeField(null=True)
    