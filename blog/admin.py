from django.contrib import admin

from .models import Post, Workout

class AdminPost(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'status',
        'created_on',
    )
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, AdminPost)

class AdminWorkout(admin.ModelAdmin):
    list_display = (
        'type',
        'date',
        'content',
    )
    list_filter = ("type",)
    search_fields = ['type', 'content']

admin.site.register(Workout, AdminWorkout)