from django.contrib import admin
from .models import News, Category, Tags, Contact
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at', 'user']
    readonly_fields = ['view_count']
    prepopulated_fields = {"slug": ("title",),}

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Contact)
