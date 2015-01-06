from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from ledger.models import Transaction
from main.models import Clinic
from django.utils.translation import ugettext_lazy as _


class ClinicTransactionFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Clinic')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'clinic'
    def lookups(self, request, model_admin):
        clinics = [(o['pk'], o['name']) for o in Clinic.objects.all().values('pk', 'name')]
        return clinics
    def queryset(self, request, queryset):
        try:
            clinic = Clinic.objects.get(pk=self.value())
            return queryset.filter(Q(agent_from_id=clinic.pk,
                                   agent_from_content_type=ContentType.objects.get_for_model(clinic)) | Q(agent_to_id=clinic.pk,
                                   agent_to_content_type=ContentType.objects.get_for_model(clinic)))
        except Clinic.DoesNotExist:
            pass


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['agent_from', 'agent_to', 'amount', 'batch_id', 'transaction_type', 'reason', 'from_deposit',
                    'date_created']
    list_filter = (ClinicTransactionFilter,)



    def agent_from(self, instance):
        return instance.agent_from

    agent_from.short_description = _("Money from")

    def agent_to(self, instance):
        return instance.agent_to

    agent_to.short_description = _("Money to")

    def reason(self, instance):
        return instance.reason

    reason.short_description = _("Reason")

    class Meta:
        model = Transaction

admin.site.register(Transaction, TransactionAdmin)