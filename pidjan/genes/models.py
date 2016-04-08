from __future__ import unicode_literals

from django.db import models


class Gene(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=5)
    sex_linked = models.BooleanField(default=False)

    def __str__(self):
        return '[%s] %s' % (self.symbol, self.name)

    def wild_type(self):
        return self.allele_set.get(wild_type=True)


class Allele(models.Model):
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=5)
    wild_type = models.BooleanField(default=False)
    dominance = models.IntegerField(default=0)

    def __str__(self):
        return '[%s] %s' % (self.symbol, self.name)

    def compare_dominance(self, comparison):
        if self.dominance > comparison:
            return 1
        elif self.dominance < comparison:
            return -1
        else:
            return 0

    def dominant_to(self, comparison):
        return self.compare_dominance(comparison) == 1

    def recessive_to(self, comparison):
        return self.compare_dominance == -1
