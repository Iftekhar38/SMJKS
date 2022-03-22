from django.contrib import admin
from myapp.models import Team, Gallery, Msg
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ['photo', 'name', 'designation', 'address', 'mobile']
    
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['pics']
    
class MsgAdmin(admin.ModelAdmin):
    list_display = ['name','email', 'message']
    
admin.site.register(Team, TeamAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Msg, MsgAdmin)