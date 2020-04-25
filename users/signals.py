from django.db.models.signals import post_save, pre_save
from .models import AdtaaUser, Profile
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

superusers_emails = AdtaaUser.objects.filter(is_superuser=True).values_list('email', flat='true')


@receiver(post_save, sender=AdtaaUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=AdtaaUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=AdtaaUser)
def send_email_to_root(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'User {} has been created'.format(instance.username),
            'A new user has been created.  Access requested: {}'.format(instance.returnUserRequested()),
            'coffeeloversusa2020@gmail.com',
            superusers_emails,
            fail_silently=False,

        )

@receiver(pre_save, sender=AdtaaUser, dispatch_uid='active')
def active(sender, instance, **kwargs):
    current_site = get_current_site(instance)
    if instance.is_active and AdtaaUser.objects.filter(pk=instance.pk, is_active=False).exists():
        subject = 'Active account'
        message = '{}, Your ADTAA account is now active.  You may login here: %s/login '.format(instance.username) % current_site.name
        # from_email = settings.EMAIL_HOST_USER
        from_email = 'coffeeloversusa2020@gmail.com'
        to_email = [instance.email]
        send_mail(subject,message,from_email,to_email,fail_silently=False)
