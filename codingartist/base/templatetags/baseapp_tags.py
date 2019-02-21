from __future__ import absolute_import, unicode_literals

from django import template

from wagtail.embeds import embeds
from wagtail.embeds.format import embed_to_frontend_html
from wagtail.embeds.exceptions import EmbedException

register = template.Library()

@register.simple_tag(takes_context=True)
def sitename(context):
    try:
        current_site = context['request'].site
    except (KeyError, AttributeError):
        return 'Site name error'

    return current_site.site_name

@register.inclusion_tag('base/responsive_image_static.html', takes_context=True)
def responsive_image_static(context, image_path, size, size_mobile, grayscale=False):
    media_desktop = "(min-width: 600px)"
    media_mobile = "(max-width: 600px)"
    image_format = "width={}&static=true&mode=scale"
    if grayscale:
        image_format += "&grayscale=true"
    context['image_path'] = image_path
    context['size'] = image_format.format(size)
    context['size_mobile'] = image_format.format(str(size_mobile))
    context['size_mobile_double'] = image_format.format(str(size_mobile * 2))
    context['size_double'] = image_format.format(str(size * 2))
    context['media_desktop'] = media_desktop
    context['media_mobile'] = media_mobile
    return context

@register.inclusion_tag('base/responsive_image_db.html', takes_context=True)
def responsive_image_db(context, image, size, size_mobile, classname=""):
    if image is not None:
        ratio = image.width / image.height
        media_desktop = "(min-width: 768px)"
        media_mobile = "(max-width: 768px)"
        image_format = "width-{0}"
        context['dekstop_normal'] = image.get_rendition(image_format.format(size))
        context['desktop_double'] = image.get_rendition(image_format.format(str(size * 2)))
        context['mobile_normal'] = image.get_rendition(image_format.format(str(size_mobile)))
        context['mobile_double'] = image.get_rendition(image_format.format(str(size_mobile * 2)))
        context['media_desktop'] = media_desktop
        context['media_mobile'] = media_mobile
        context['classname'] = classname
        return context

@register.simple_tag(name='embed')
def embed_tag(url):
    try:
        embed = embeds.get_embed(url)
        return embed_to_frontend_html(embed)
    except EmbedException:
        return ''

