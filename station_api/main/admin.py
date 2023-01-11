from django.contrib import admin
from main.models import Station, Question, Flight


admin.AdminSite.site_header = 'QCS — Cервисы администрирования'
admin.AdminSite.site_title = 'QCS — Личный кабинет'
admin.AdminSite.index_title = 'QCS — Личный кабинет'


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    fields = ('id', 'api_key',)
    readonly_fields = ('id',)


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'aruco', 'get_status', 'get_busyness')
    list_display_links = ('id', 'aruco')
    fields = ('id', 'aruco', 'api_key', 'get_status', 'get_busyness')
    readonly_fields = ('id', 'get_status', 'get_busyness')
    list_filter = ('opened', 'done', 'disabled')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('truncate_text', 'truncate_contact', 'date', 'rewiewed')
    list_display_links = ('truncate_text', 'truncate_contact', 'date')
    fields = ('date', 'text', 'contact', 'rewiewed')
    readonly_fields = ('date', )
    list_filter = ('rewiewed', 'date')
