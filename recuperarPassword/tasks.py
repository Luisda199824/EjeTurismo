from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template import loader

from emailApp.models import PasswordRestaure
from modelsAdmin.models import Usuario

from celery import shared_task

@shared_task
def enviarCorreoRecuperarPassword(pr_id):
    pr = PasswordRestaure.objects.filter(id=pr_id)
    pr = pr[0]
    usuario = Usuario.objects.filter(usuario=pr.user)
    if len(usuario) > 0:
        usuario = usuario[0]
        subject = "Recuperación de contraseña - Eje Turismo"
        ctx = {
            'hash': pr.hash,
        }
        body = (loader.get_template('recuperarPassword/email_base.html')).render(ctx)
        from_email = settings.EMAIL_HOST_USER
        to_list = [usuario.email]
        # print "Enviando..."
        msg = EmailMessage(subject, body, from_email, to_list)
        msg.content_subtype = "html"
        # # # ---------------------------
        msg.send()
        # print "Finalizado"
    else:
        return False
