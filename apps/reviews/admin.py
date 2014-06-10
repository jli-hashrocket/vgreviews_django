from django.contrib import admin
from apps.reviews.models import Review
import pdb

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'pros', 'cons', 'score', 'likes', 'author')
    fieldsets = [
        (None, { 'fields': [('title','summary','pros','cons','score','likes')] } ),
    ]
    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()

admin.site.register(Review, ReviewAdmin)
