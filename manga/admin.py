from django.contrib import admin
from .models import Manga, Author, Chapter, Genre
# Register your models here.

class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 1
    list_per_page = 1

class MangaAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]

admin.site.register(Manga, MangaAdmin)
admin.site.register(Author)
admin.site.register(Chapter)
admin.site.register(Genre)

