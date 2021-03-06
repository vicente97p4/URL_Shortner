from shortener.utils import url_count_changer
from django.contrib import messages
from shortener.forms import UrlCreateForm
from django.shortcuts import redirect, render, get_object_or_404
from shortener.models import ShortenedUrls, Statistic
from django.contrib.auth.decorators import login_required
from ratelimit.decorators import ratelimit
from django.contrib.gis.geoip2 import GeoIP2

from shrinkers.settings import GEOIP_PATH


# 같은 요청을 계속 반복하면 중간에 요청을 막는다.
@ratelimit(key="ip", rate="3/m")
def url_redirect(request, prefix, url):
    was_limited = getattr(request, "limited", False) # request에 limited가 True가 되면 제한이 걸렸다는 의미이므로 다른 곳으로 redirect 시킨다.
    if was_limited:
        return redirect("index")
    get_url = get_object_or_404(ShortenedUrls, prefix=prefix, shortened_url=url)
    is_permanent = False
    target = get_url.target_url
    if get_url.creator.organization:
        is_permanent = True

    if not target.startswith("https://") and not target.startswith("http://"):
        target = "https://" + get_url.target_url

    history = Statistic()
    history.record(request, get_url)
    return redirect(target, permanent=is_permanent)


def url_list(request):
    # country = GeoIP2().country('http://naver.com')
    get_list = ShortenedUrls.objects.order_by("-created_at").all()
    return render(request, "url_list.html", {"list": get_list})


@login_required
def url_create(request):
    msg = None
    if request.method == "POST":
        form = UrlCreateForm(request.POST)
        if form.is_valid():
            msg = f"{form.cleaned_data.get('nick_name')} 생성 완료!"
            messages.add_message(request, messages.INFO, msg)
            form.save(request)
            return redirect("url_list")
        else:
            form = UrlCreateForm()
    else:
        form = UrlCreateForm()
    return render(request, "url_create.html", {"form": form})


@login_required
def url_change(request, action, url_id):
    if request.method == "POST":
        url_data = ShortenedUrls.objects.filter(id=url_id)
        if url_data.exists():
            if url_data.first().creator_id != request.user.id:
                msg = "자신이 소유하지 않은 URL 입니다."
            else:
                if action == "delete":
                    msg = f"{url_data.first().nick_name} 삭제 완료!"
                    try:
                        url_data.delete()
                    except Exception as e:
                        print(e)
                    else:
                        url_count_changer(request, False)
                    messages.add_message(request, messages.INFO, msg)
                elif action == "update":
                    msg = f"{url_data.first().nick_name} 수정 완료!"
                    form = UrlCreateForm(request.POST)
                    form.update_form(request, url_id)

                    messages.add_message(request, messages.INFO, msg)
        else:
            msg = "해당 URL 정보를 찾을 수 없습니다."

    elif request.method == "GET" and action == "update":
        url_data = ShortenedUrls.objects.filter(pk=url_id).first()
        form = UrlCreateForm(instance=url_data)
        return render(request, "url_create.html", {"form": form, "is_update": True})

    return redirect("url_list")
