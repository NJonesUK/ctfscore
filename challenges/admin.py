from django.contrib import admin

# Register your models here.
from django.contrib import admin
from challenges.models import Challenge, ChallengeEntry

class ChallengeAdmin(admin.ModelAdmin):
    pass

class ChallengeEntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(ChallengeEntry, ChallengeEntryAdmin)