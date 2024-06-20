# Import necessary modules
from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# ---------------------
# Post Admin
# ---------------------
# A custom admin model for 'Post' is defined here. It inherits from 'SummernoteModelAdmin'.
# It includes a list display, search fields, list filters, and prepopulated fields.
# The 'summernote_fields' attribute specifies that the 'content' field of the 'Post' model should use Summernote's WYSIWYG editor.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# ---------------------
# Register Models
# ---------------------
# The 'Comment' model is registered with the admin site.
# The 'Post' model is already registered through the '@admin.register()' decorator.
# admin.site.register(Post)
admin.site.register(Comment)
