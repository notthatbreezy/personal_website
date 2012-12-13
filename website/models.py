from django.db import models
from django.contrib import admin
# Create your models here.


class TopicAreas(models.Model):
    """ Model for presenting information and links from the HomePage """
    topic_title = models.TextField(blank=False)
    topic_description = models.TextField(blank=False)
    url = models.CharField(max_length=200, blank=False)  # link information
    topic_key = models.IntegerField(primary_key=True)
    homepage = models.IntegerField(blank=False)

    class Meta:
        db_table = u'topictable'

    def home_page(self):
        pass

    def __unicode__(self):
        return self.topic_title


class Research(models.Model):
    """ Model for presenting research """
    research_title = models.TextField(blank=False)
    research_abstract = models.TextField(blank=False)
    id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return self.research_title


class ResearchAdmin(admin.ModelAdmin):
    fields = ['research_title', 'research_abstract']


class TopicAreasAdmin(admin.ModelAdmin):
    fields = ['topic_title', 'topic_description', 'url', 'homepage']

admin.site.register(TopicAreas, TopicAreasAdmin)
admin.site.register(Research, ResearchAdmin)
