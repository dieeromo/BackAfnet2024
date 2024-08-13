# En signals.py dentro de tu aplicación Django
from django.db.models.signals import post_save
from django.dispatch import receiver
#from djoser.signals import user_logged_in

#@receiver(user_logged_in)
def handle_user_logged_in(sender, request, user, **kwargs):

    user_data = {
        'id': user.id,
        'username': user.first_name,
    
        # Agrega más campos según tus necesidades
    }
    request.user_data = user_data
