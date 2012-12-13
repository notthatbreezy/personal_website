from django.db import models
from django.contrib import admin
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class LinksToRead(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=125)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __unicode__(self):
        return self.title


class Code(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()

    def __unicode__(self):
        return self.title


class Research(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()

    def __unicode__(self):
        return self.title


### Admin

class ResearchAdmin(admin.ModelAdmin):
    search_fields = ["title"]


class ProjectsAdmin(admin.ModelAdmin):
    search_fields = ["title"]


class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]


class LinksAdmin(admin.ModelAdmin):
    search_fields = ["title"]


class CodeAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)
admin.site.register(LinksToRead, LinksAdmin)
admin.site.register(Code, CodeAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(Projects, ProjectsAdmin)
