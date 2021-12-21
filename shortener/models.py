import string
import random

from django.db import models
from django.contrib.auth.models import User as U

# Create your models here.
class TimeStampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True # django´Â Å¬·¡½º¸¦ Å×ÀÌºíÀ» ¸¸µé¾î¼­ °ü¸®ÇÑ´Ù.
        # ±×·¡¼­ ÀÌ·¸°Ô »ó¼Ó½ÃÅ°´Â class¸¦ ¸¸µå·Á¸é
        # Meta class¿¡¼­ abstract = True¸¦ ÇØÁà¾ß ÇÑ´Ù.


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
    name = models.CharField(max_length=50) # ?šŒ?‚¬ ?´ë¦?
    industry = models.CharField(max_length=15, choices=Industries.choices, default=Industries.OTHERS) # ?œ„ 5ê°? ì¤? 1ê°?
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
    prefix = models.CharField(max_length=50) # /1234 ?¼?Š” url?´ ?ˆ?‹¤ê³? ?•´ë³´ì, ê·¸ëŸ¼ 9999ê¹Œì??ë°–ì— ë§Œë“¤ ?ˆ˜ ?—†?‹¤. ê·¸ë˜?„œ ?•?— ?„?˜?˜ ë¬¸ìë¥? ?‘ê¸? ?œ„?•´ ë§Œë“¤?—ˆ?‹¤. ?‚˜ì¤‘ì—?Š” ë¬¸ì ????‹  ?›?•˜?Š” identityë¥? ?„£?Š”?‹¤.
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    target_url = models.CharField(max_length=2000)
    shortened_url = models.CharField(max_length=6, default=rand_string)
    created_via = models.CharField(max_length=8, choices=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
    expired_at = models.DateTimeField(null=True)
    