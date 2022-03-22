from django.contrib import admin
from .models import session


@admin.register(session)
class SessionAdmin(admin.ModelAdmin):
    pass

