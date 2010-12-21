from django.db import models
from django.utils.translation import ugettext_lazy as _

class ExtractedPattern(models.Model):
    name = models.CharField(_('name'), max_length=250, help_text=_('Enter a pattern name'))
    subject = models.CharField(_('subject'), max_length=250, null=True, blank=True, help_text=_('Enter a subject of pattern'))
    relation = models.CharField(_('relation'), max_length=250, null=True, blank=True, help_text=_('Enter a relation'))
    object = models.CharField(_('object'), max_length=250, null=True, blank=True, help_text=_('Enter an object'))
    count = models.IntegerField(_('count'), help_text=_('Enter '))