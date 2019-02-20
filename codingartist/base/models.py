from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from .blocks import BaseStreamBlock
from wagtailmetadata.models import MetadataPageMixin
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)

from wagtail.contrib.settings.models import BaseSetting, register_setting

# Create your models here.


class StandardPage(MetadataPageMixin, Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    introduction = StreamField(BaseStreamBlock, blank=True)
    body = StreamField(BaseStreamBlock)

    content_panels = Page.content_panels + [
        ImageChooserPanel('background_image'),
        StreamFieldPanel('introduction'),
        StreamFieldPanel('body'),
    ]

@register_setting
class GeneralSettings(BaseSetting):
    google_site_verification_code = models.TextField(help_text='Google site verification code')

class FormField(AbstractFormField):
    """
    Wagtailforms is a module to introduce simple forms on a Wagtail site. It
    isn't intended as a replacement to Django's form support but as a quick way
    to generate a general purpose data-collection form or contact form
    without having to write code. We use it on the site for a contact form. You
    can read more about Wagtail forms at:
    http://docs.wagtail.io/en/latest/reference/contrib/forms/index.html
    """
    page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)


class FormPage(AbstractEmailForm, MetadataPageMixin):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    introduction = StreamField(BaseStreamBlock, blank=True)
    body = StreamField(BaseStreamBlock)
    thank_you_text = RichTextField(blank=True)

    # Note how we include the FormField object via an InlinePanel using the
    # related_name value
    content_panels = AbstractEmailForm.content_panels + [
        ImageChooserPanel('background_image'),
        StreamFieldPanel('introduction'),
        StreamFieldPanel('body'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]
