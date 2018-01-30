from __future__ import absolute_import, unicode_literals

from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def sitename(context):
    try:
        current_site = context['request'].site
    except (KeyError, AttributeError):
        return 'Site name error'

    return current_site.site_name

