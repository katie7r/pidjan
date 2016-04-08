from django.views import generic

from .models import Gene


class IndexView(generic.ListView):
    template_name = 'genes/index.html'
    context_object_name = 'gene_pool'

    def get_queryset(self):
        """Return the pool of genes."""
        return Gene.objects.order_by('symbol')


class DetailView(generic.DetailView):
    model = Gene
    template_name = 'genes/detail.html'
