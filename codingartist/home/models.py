from __future__ import absolute_import, unicode_literals

from wagtailmetadata.models import MetadataPageMixin

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from base.blocks import BaseStreamBlock


class HomePage(MetadataPageMixin, Page):
    description = RichTextField(blank=True, null=True)
    body = StreamField(BaseStreamBlock, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        StreamFieldPanel('body', )
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['page'] = self
        return context
