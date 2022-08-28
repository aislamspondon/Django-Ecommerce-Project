from django import template
from store.models import MyLogo, MyFavicon

register = template.Library()


@register.filter
def logo(request):
    if request:
        logo_image = MyLogo.objects.filter(is_active=True).order_by('-id').first()
        return logo_image.image.url


@register.filter
def favicon(request):
    if request:
        favicon_image = MyFavicon.objects.filter(is_active=True).order_by('-id').first()
        return favicon_image.img.url


