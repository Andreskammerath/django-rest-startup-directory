from django.contrib import admin
from organiser.models import NewsLink, Startup, Tag


@admin.register(NewsLink)
class NewsLinkAdmin(admin.ModelAdmin):
    """Configure NewsLink panel"""

    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Configure Tag panel"""

    list_display = ("pk", "name", "slug")


@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    """Configure Startup panel"""

    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}