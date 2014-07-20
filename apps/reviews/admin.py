from django.contrib import admin
from apps.reviews.models import *
import pdb

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'pros', 'cons', 'score', 'author')
    fieldsets = [
        (None, { 'fields': [('title','summary','pros','cons','categories', 'consoles', 'score')] } ),
    ]
    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    pass

class LikeAdmin(admin.ModelAdmin):
    list_display = ['review','total_likes']

class ConsoleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Review, ReviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Console, ConsoleAdmin)


