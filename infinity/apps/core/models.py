from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from .signals import _comment_post_save


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField(blank=False)
    notify = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        unique=False,
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False,
        null=False,
    )

    def __unicode__(self):
        return u"Comment #%s" % self.id

    def get_absolute_url(self):
        return "/"


class Goal(models.Model):
    name = models.CharField(
        unique=False,
        max_length=150,
        blank=False,
    )
    language = models.ForeignKey(
        'Language',
        blank=True,
        null=True,
    )
    personal = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        unique=False,
        null=False,
        blank=False,
    )
    reason = models.TextField(blank=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False,
        null=False,
        related_name='user_goals'
    )
    need = models.ForeignKey(
        'Need',
        blank=False,
        null=False,
    )
    quantity = models.PositiveIntegerField(
        unique=False,
        null=False,
        blank=False,
    )
    unit = models.CharField(
        unique=False,
        max_length=50,
        blank=True,
    )

    def __unicode__(self):
        return unicode(self.name[:50])

    def get_absolute_url(self):
        return "/"


class Work(models.Model):
    personal = models.BooleanField(default=False)
    language = models.ForeignKey(
        'Language',
        blank=True,
        null=True,
    )
    task = models.ForeignKey(
        'Task',
        related_name='task_works',
        blank=False,
        null=False,
    )
    name = models.CharField(
        unique=False,
        max_length=150,
        blank=False,
    )
    url = models.URLField(
        max_length=150,
        unique=False,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_works',
        blank=False,
        null=False,
    )
    file = models.FileField(
        null=True,
        upload_to='files',
        blank=True,
    )
    parent_work_id = models.PositiveIntegerField(
        unique=False,
        null=True,
        blank=True,
    )
    description = models.TextField(blank=True)

    def __unicode__(self):
        return unicode(self.name[:50])

    def get_absolute_url(self):
        return "/"


class Idea(models.Model):
    description = models.TextField(blank=False)
    language = models.ForeignKey(
        'Language',
        blank=True,
        null=True,
    )
    personal = models.BooleanField(default=False)
    name = models.CharField(
        unique=False,
        max_length=150,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    summary = models.CharField(
        unique=False,
        max_length=150,
        blank=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_ideas',
        blank=False,
        null=False,
    )
    goal = models.ForeignKey(
        'Goal',
        related_name='goal_ideas',
        blank=False,
        null=False,
    )

    def __unicode__(self):
        return unicode(self.name[:50])

    def get_absolute_url(self):
        return "/"


class Step(models.Model):
    personal = models.BooleanField(default=False)
    language = models.ForeignKey(
        'Language',
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_steps',
        blank=False,
        null=False,
    )
    name = models.CharField(
        unique=False,
        max_length=150,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    deliverables = models.CharField(
        unique=False,
        max_length=150,
        blank=False,
    )
    priority = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
    )
    plan = models.ForeignKey(
        'Plan',
        related_name='plan_steps',
        blank=False,
        null=False,
    )
    objective = models.TextField(blank=False)
    investables = models.CharField(
        unique=False,
        max_length=150,
        blank=False,
    )

    def __unicode__(self):
        return unicode(self.name[:50])

    def get_absolute_url(self):
        return "/"


class Task(models.Model):
    personal = models.BooleanField(default=False)
    language = models.ForeignKey(
        'Language',
        blank=True,
        null=True,
    )
    name = models.CharField(
        unique=False,
        max_length=150,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    priority = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
    )
    step = models.ForeignKey(
        'Step',
        related_name='step_tasks',
        blank=False,
        null=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_tasks',
        blank=False,
        null=False,
    )

    def __unicode__(self):
        return unicode(self.name[:50])

    def get_absolute_url(self):
        return "/"


class Need(models.Model):
    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    defined_meaning_id = models.PositiveIntegerField(null=True, blank=True)
    definition = models.CharField(max_length=255)
    type = models.ForeignKey(
        'Type',
        blank=True,
        null=True,
    )
    language = models.ForeignKey(
        'Language',
        blank=True,
        null=True,
    )
    name = models.CharField(
        unique=False,
        max_length=150,
        blank=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_needs',
        blank=False,
        null=False,
    )

    def __unicode__(self):
        return unicode(self.name[:50])

    def get_absolute_url(self):
        return "/"

    class Meta:
        unique_together = ('language', 'name', 'definition')



class Type(models.Model):
    name = models.CharField(
        unique=False,
        max_length=150,
        blank=False,
    )

    def __unicode__(self):
        return unicode(self.name[:50])

    def get_absolute_url(self):
        return "/"


class Plan(models.Model):
    personal = models.BooleanField(default=False)
    language = models.ForeignKey(
        'Language',
        blank=True,
        null=True,
    )
    name = models.CharField(
        unique=False,
        max_length=150,
        blank=False,
        verbose_name='means'
    )
    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        unique=False,
        null=False,
        blank=False,
    )
    idea = models.ForeignKey(
        'Idea',
        related_name='idea_plans',
        blank=False,
        null=False,
    )
    deliverable = models.TextField(blank=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_plans',
        blank=False,
        null=False,
    )
    situation = models.TextField(blank=False)

    def __unicode__(self):
        return unicode(self.name[:50])

    def get_absolute_url(self):
        return "/"


class Language(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    http_accept_language = models.CharField(max_length=255, blank=True,
                                            null=True)
    omegawiki_language_id = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        try:
            return unicode(self.name[:50])
        except TypeError:
            return unicode(self.pk)

# Signals register place
post_save.connect(_comment_post_save, sender=Comment)
