from django.contrib import admin
from .models import Attributes, Options, Setting, Labels


class LabelsInline(admin.TabularInline):
	model = Labels
	extra = 0
	max_num = 10


class OptionAdmin(admin.ModelAdmin):
	list_display = ['__str__']
	inlines = [
		LabelsInline
	]
	class Meta:
		model = Options

admin.site.register(Attributes)
admin.site.register(Options, OptionAdmin)
admin.site.register(Setting)
admin.site.register(Labels)

# Register your models here.
