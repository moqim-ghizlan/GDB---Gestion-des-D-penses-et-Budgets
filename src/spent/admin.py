from django.contrib import admin
from .models import Spent




class SpentAdminConfig(admin.ModelAdmin):
    list_display = ('get_simple_title', 'get_amout', 'get_month', 'get_user')
    list_display_links = ('get_simple_title', 'get_amout', 'get_month', 'get_user')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


    def get_user(self, obj):
        return obj.get_user()

    def get_month(self, obj):
        return obj.get_month_with_id()

    def get_simple_title(self, obj):
        return obj.get_simple_title()

    def get_amout(self, obj):
        return obj.get_amout()



    get_month.short_description = 'Mois'
    get_simple_title.short_description = 'Titre'
    get_amout.short_description = 'Montant (€)'
    get_user.short_description = 'Utilisateur'

admin.site.register(Spent, SpentAdminConfig)
