from django.db import models


class Contact(models.Model):

    SUBJECT_CHOICES = (
        (0, 'Comment'),
        (1, 'Suggestion'),
        (2, 'Question'),
        (3, 'General Inquiry'),
        (4, 'Business Inquiry')
    )

    name = models.CharField(max_length=50)
    email = models.EmailField()
    company = models.CharField(max_length=255, blank=True, null=True)
    subject = models.IntegerField(choices=SUBJECT_CHOICES, default=0)
    body = models.TextField()
    is_sent = models.BooleanField(default=False)
    from_email = models.EmailField(default='no-reply@findyour3d.com')
    reply_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Message from {}".format(self.name)
