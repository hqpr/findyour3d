import logging
from django.shortcuts import render, redirect
from django.conf import settings

from findyour3d.users.email_template import send_templated_email
from .forms import ContactForm
from .models import SUBJECT_CHOICES

logger = logging.getLogger(__name__)


def contact(request):
    context = {}
    feedback_form = ContactForm(request.POST)
    context["form"] = feedback_form
    if request.method == 'POST':
        if feedback_form.is_valid():
            try:
                subject = SUBJECT_CHOICES[int(feedback_form.cleaned_data.get('subject'))][1]
                send_templated_email('Your3d Contact Form: {}'.format(subject),
                                     'email/contact_form_admin.html',
                                     {'body': feedback_form.cleaned_data.get('body'),
                                      'name': feedback_form.cleaned_data.get('name'),
                                      'email': feedback_form.cleaned_data.get('email'),
                                      'subject': subject,
                                      },
                                     [settings.DEREKS_EMAIL, ])
            except Exception as e:
                logger.exception(str(e))

            feedback_form.save()
            response = redirect('home')
            response['Location'] += '?message_sent=success'
            return response
        else:
            return render(request, 'pages/about.html', context)
    else:
        return render(request, 'pages/about.html', context)
