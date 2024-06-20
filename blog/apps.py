# Import necessary modules
from django.apps import AppConfig

# ---------------------
# Define Blog Configuration
# ---------------------
# The 'BlogConfig' class is defined and extends 'AppConfig'.
# The 'default_auto_field' attribute is set to 'django.db.models.BigAutoField'.
# The 'name' attribute is set to 'blog'.
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
