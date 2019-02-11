from wagtailmetadata.models import MetadataPageMixin

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from base.blocks import BaseStreamBlock


class HomePage(MetadataPageMixin, Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = RichTextField(blank=True, null=True)
    body = StreamField(BaseStreamBlock, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('background_image'),
        FieldPanel('description', classname='full'),
        StreamFieldPanel('body', )
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['page'] = self
        return context
