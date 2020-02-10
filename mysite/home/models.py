from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.models import Page
from wagtail_localize.models import TranslatablePageMixin


class HomePage(TranslatablePageMixin, Page):
    pass


class BlogPage(TranslatablePageMixin, Page):
    introduction = models.TextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]
