from __future__ import absolute_import, unicode_literals

import datetime
from django.db import models
from django.utils.timezone import now

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages import blocks as imageblocks
from wagtail.wagtailembeds.blocks import EmbedBlock

class BlogPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(BlogPage, self).get_context(request, *args, **kwargs)
        posts = self.get_descendants().live()
        context['posts'] = posts
        return context

class BlogPost(Page):
    date = models.DateField(default=now)
    body = StreamField([
        ('heading', blocks.CharBlock(template="blog/block/heading.html")),
        ('paragraph', blocks.RichTextBlock(template="blog/block/paragraph.html")),
        ('image', imageblocks.ImageChooserBlock(template="blog/block/image.html")),
        ('embed', EmbedBlock(template="blog/block/embed.html")),
        ('code', blocks.TextBlock(template="blog/block/code.html")),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(BlogPost, self).get_context(request, *args, **kwargs)
        parent = self.get_parent()
        context['parent'] = parent
        return context