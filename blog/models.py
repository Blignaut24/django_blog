# Import necessary modules
from django.db import models
from django.contrib.auth.models import User

# Define status options
STATUS = ((0, "Draft"), (1, "Published"))

# ---------------------
# Define Post Model
# ---------------------
# The 'Post' model is defined here with various fields.
# The 'Meta' class is used to specify additional options.
# The '__str__' method is overridden to return a user-friendly representation of the model.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
            ordering = ["-created_on", "author"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

# ---------------------
# Define Comment Model
# ---------------------
# The 'Comment' model is defined here with various fields.
# The 'Meta' class is used to specify additional options.
# The '__str__' method is overridden to return a user-friendly representation of the model.
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
