from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from .blocks import BaseStreamBlock

# Create your models here.

class StandardPage(Page):
    body = StreamField(BaseStreamBlock)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]