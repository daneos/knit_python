from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 5

class PollAdmin(admin.ModelAdmin):
	search_fields = ['question']
	fieldsets = [
		(None, {'fields': ['question']}),
		('Date information', {'fields': ['date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)