from django.contrib import admin

from .models import *
from authentication.models import User

admin.site.register(Game)
admin.site.register(Author)
admin.site.register(Studio)
admin.site.register(Genre)
admin.site.register(SystemRequirements)
admin.site.register(User)