from django.contrib import admin
from .models import FormDatabase


class FormAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email')
    search_fields = ('firstName', 'email')
    list_filter = ('date', 'occupation')
    ordering = ('-firstName',)
    readonly_fields = ('occupation',)


admin.site.register(FormDatabase, FormAdmin)
