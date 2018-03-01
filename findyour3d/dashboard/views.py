from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db.models import Q
from django.views.generic import ListView

from findyour3d.company.models import Company


class DashboardView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'dashboard/company.html'
    context_object_name = 'companies'
    paginate_by = 50

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            if self.request.user.user_type == 1:
                if not self.request.user.customer_set.all():
                    return redirect('customers:add')
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user.customer_set.first()
        # showing metals with SLM / DMLS
        if user.material in [9, 12, 13, 14]:
            queryset = Company.objects.filter(Q(top_printing_processes='1') &
                                              Q(user__plan__isnull=False) &
                                              Q(budget__contains=str(user.budget)) &
                                              Q(is_cad_assistance=user.need_assistance) &
                                              Q(ideal_customer__contains=str(user.customer_type))).order_by(
                '-user__plan')
        else:
            queryset = Company.objects.filter(
                (Q(material__contains=str(user.material))) &
                Q(top_printing_processes__contains=str(user.process)) &
                Q(user__plan__isnull=False) &
                Q(budget__contains=str(user.budget)) &
                Q(is_cad_assistance=user.need_assistance) &
                Q(ideal_customer__contains=str(user.customer_type))).order_by('-user__plan')
        return queryset


