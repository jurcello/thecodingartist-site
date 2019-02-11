from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from .blocks import BaseStreamBlock
from wagtailmetadata.models import MetadataPageMixin
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.


class StandardPage(MetadataPageMixin, Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField(BaseStreamBlock)

    content_panels = Page.content_panels + [
        ImageChooserPanel('background_image'),
        StreamFieldPanel('body'),
    ]