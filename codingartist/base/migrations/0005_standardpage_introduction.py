# Generated by Django 2.1.5 on 2019-02-11 11:44

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_standardpage_background_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='introduction',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.CharBlock(template='base/blocks/heading.html')), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='base/blocks/paragraph.html')), ('image_block', wagtail.images.blocks.ImageChooserBlock(template='base/blocks/image.html')), ('embed_block', wagtail.embeds.blocks.EmbedBlock(template='base/blocks/embed.html')), ('code_block', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', label='Language')), ('code', wagtail.core.blocks.TextBlock(label='Code'))])), ('plain_html_block', wagtail.core.blocks.CharBlock(max_length=4048, template='base/blocks/plain_html.html'))], blank=True),
        ),
    ]
