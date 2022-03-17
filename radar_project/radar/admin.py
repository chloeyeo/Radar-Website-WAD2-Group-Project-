from django.contrib import admin
from radar.models import UserProfile, Category, Post
from django.contrib.auth.models import User

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class UserProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('user',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post)
