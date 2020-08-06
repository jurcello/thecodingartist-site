from wagtail.core.blocks import (StreamBlock, CharBlock, RichTextBlock, StructBlock, URLBlock)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailcodeblock.blocks import CodeBlock
from wagtailmarkdown.blocks import MarkdownBlock

class BaseStreamBlock(StreamBlock):
    heading_block = CharBlock(template="base/blocks/heading.html")
    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        template="base/blocks/paragraph.html"
    )
    image_block = ImageChooserBlock(template="base/blocks/image.html")
    embed_block = EmbedBlock(template="base/blocks/embed.html")
    code_block = CodeBlock()
    markdown = MarkdownBlock(icon="code")
    plain_html_block = CharBlock(template="base/blocks/plain_html.html", max_length=4048)
    call_to_action = StructBlock(
        [
            ('text', CharBlock()),
            ('url', URLBlock()),
        ],
        template="base/blocks/call_to_action.html"
    )
