# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import messages
from django.db.models import Prefetch
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import UpdateView
from django_filters.views import FilterView
from filters.views import FilterMixin

from accounts.models import Entity, ACTIVE
from accounts.views import ProviderFilter
from core.mixins.AjaxTemplateResponseMixin import AjaxTemplateResponseMixin
from core.mixins.ExportAsCSVMixin import ExportAsCSVMixin
from core.mixins.ListItemUrlMixin import ListItemUrlMixin
from social_balance.forms.entity_year import EntityYearBalanceForm
from social_balance.models import SocialBalanceBadge, EntitySocialBalance


class SocialBalanceYear(FilterView, FilterMixin, ExportAsCSVMixin, ListItemUrlMixin, AjaxTemplateResponseMixin):
    template_name = 'balance/year/list.html'
    ajax_template_name = 'balance/year/query.html'
    model = Entity
    queryset = Entity.objects.filter(status=ACTIVE)
    model = Entity
    paginate_by = 35

    filterset_class = ProviderFilter

    def get_queryset(self):
        qs = super().get_queryset()
        year = self.kwargs.get('year', settings.CURRENT_BALANCE_YEAR)
        return qs.prefetch_related(
            Prefetch(
                "social_balances",
                queryset=EntitySocialBalance.objects.filter(year=year),
                to_attr="social_balance"
            )
        )


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = EntitySocialBalance.objects.all().order_by('year').values_list('year', flat=True).distinct()
        context['current_year'] = int(self.kwargs.get('year', settings.CURRENT_BALANCE_YEAR))
        return context


class SocialBalanceEditView(UpdateView):
    form_class = EntityYearBalanceForm
    template_name = 'balance/year/detail.html'
    queryset = EntitySocialBalance.objects.all()
    model = EntitySocialBalance

    def get_object(self, queryset=None):
        entity_id = self.kwargs['entity_pk']
        year = self.kwargs['year']

        return EntitySocialBalance.objects.get(entity__pk=entity_id, year=year)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = Entity.objects.get(pk=self.object.entity.pk)
        context['badge'] = SocialBalanceBadge.objects.filter(year=self.object.year).first()

        return context


    def get_success_url(self):
        messages.success(self.request, _('Datos de balance actualizados satisfactoriamente.'))
        return reverse('balance:entity_year', kwargs={'entity_pk': self.object.entity.pk, 'year':self.object.year })