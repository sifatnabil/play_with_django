from django.contrib import admin

from .models import Meetup, Account
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username')
    list_filter = ('email',) 


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Account, AccountAdmin)
