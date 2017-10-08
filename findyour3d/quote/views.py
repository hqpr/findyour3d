import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from findyour3d.payment.views import starter_charge
from findyour3d.utils.views import custom_redirect

from findyour3d.company.models import Company
from .models import QuoteRequest


logger = logging.getLogger(__name__)


@login_required
def request_quote(request, pk):
    if request.method == 'POST':
        try:
            company = Company.objects.get(id=pk)
            company_owner = company.user
            company_plan = company.user.plan
            user = request.user
            if not QuoteRequest.objects.filter(company=company, user=request.user).exists():
                if company_plan == 1:
                    starter_charge(company_owner)
                quote = QuoteRequest.objects.create(user=request.user, company=company)

                subject, from_email, to = 'Request Confirmation', settings.DEFAULT_FROM_EMAIL, company.email

                html_content = render_to_string('email/customer_request.html',
                                                {'user': user, 'company': company, 'quote': quote})
                text_content = strip_tags(html_content)

                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                try:
                    msg.send()
                except Exception as e:
                    logger.error(str(e))

                return custom_redirect('dashboard:company', quote='requested')
            else:
                logger.error('already requested')
                return redirect('dashboard:company')
        except Company.DoesNotExist:
            logger.error('no company found')
            return redirect('dashboard:company')
    else:
        logger.error('throw an request error')
        return redirect('dashboard:company')
