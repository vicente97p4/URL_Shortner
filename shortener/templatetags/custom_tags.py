from django import template
from django.utils.html import mark_safe

from datetime import time, datetime, date, timedelta

register = template.Library()

@register.filter(name='email_ma') 
def email_masker(value, arg): # 함수 이름은 의미없다 위에 있는 filter name을 따른다.
    email_split = value.split('@') # value에는 템플릿에서 받은 변수가 들어온다.(u.email)
    return f'{email_split[0]}@*******.***' if arg&2 == 0 else value

@register.simple_tag(name='test_tags', takes_context=True) # context를 사용하기 위해서는 takes_context=True로 해줘야 한다.
def test_tags(context):

    tag_html = '<span class="badge badge-primary">테스트 태그</span>'
    
    return mark_safe(tag_html)