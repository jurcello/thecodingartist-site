from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtailmetadata.models import MetadataPageMixin

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(MetadataPageMixin, Page):
    description = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['page'] = self
        return context
