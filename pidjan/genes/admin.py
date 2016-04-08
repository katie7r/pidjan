from django.contrib import admin

from .models import Allele, Gene


class AlleleInline(admin.TabularInline):
    model = Allele
    extra = 3
    fields = ['name', 'symbol', 'dominance', 'wild_type']


class GeneAdmin(admin.ModelAdmin):
    fields = ['name', 'symbol', 'sex_linked']
    inlines = [AlleleInline]
    list_display = ('name', 'symbol', 'sex_linked', 'list_alleles')
    search_fields = ['name']

    def list_alleles(self, obj):
        return ', '.join([str(a) for a in obj.allele_set.all()])
    list_alleles.short_description = 'Alleles'
    list_alleles.admin_order_field = 'gene__allele__symbol'

admin.site.register(Gene, GeneAdmin)
