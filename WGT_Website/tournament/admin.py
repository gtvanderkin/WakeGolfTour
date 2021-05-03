from django.contrib import admin
from . models import Tournament, Round

class TournamentAdmin (admin.ModelAdmin):
	list_display = ['tourn_name', 'tourn_course', 'tourn_start_date']
	list_filter = ['tourn_course']
	ordering = ['tourn_start_date']
	exclude = ['tourn_id']
	actions_on_top = False

admin.site.register (Tournament, TournamentAdmin)