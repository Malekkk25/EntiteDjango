from audioop import reverse
from django.contrib import admin
from vol.models import Liste
from vol.models import Aeroport


class ListeAdmin(admin.ModelAdmin):
    list_display = ('destination', 'prixTicket', 'compagnie','air')
    list_filter = ('destination', 'prixTicket')
    date_hierarchy = 'dateDepart'
    ordering = ('dateDepart',)
    search_fields = ('destination', 'air')
    fields= ("numVol","destination","compagnie","prixTicket","dateDepart","air")
    def aerop_link(self, v):
            return mark_safe('<a href="{}">{}</a>'.format(
                reverse("admin:vol_aeroport_change",
                args=(v.air.pk,)),v.air.nomAir
    ))


class AeroportAdmin(admin.ModelAdmin):
    list_display= ('nomAir','apercu')
    list_filter=('nomAir','id')
    search_fields=('nomAir','prixTicket')
    def apercu(self,air):
        text=air.description[:40]
        if len(air.description)>40:
            return'{} ...'.format(text)
        else:
            return text

admin.site.register(Liste, ListeAdmin)
admin.site.register(Aeroport,AeroportAdmin)
