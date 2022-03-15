from django.contrib import admin
from radar.models import UserProfile, Category, Post

# Register your models here.

admin.site.register(UserProfile)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post)

