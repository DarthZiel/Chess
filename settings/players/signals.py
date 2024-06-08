from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ChessPlayers
from .services import get_data_from_fide


@receiver(post_save, sender=ChessPlayers)
def update_data_from_fide(sender, instance, created, **kwargs):
    if created:
        additonal_data = get_data_from_fide(str(instance.fide_id))
        instance.first_name_fide = additonal_data['name'].split(',')[1].strip()
        instance.last_name_fide = additonal_data['name'].split(',')[0]
        instance.title = additonal_data['title']
        instance.gender = additonal_data['sex']
        instance.federation = additonal_data['federation']
        instance.rating_classical = additonal_data['standard_elo']
        instance.rating_rapid = additonal_data['rapid_elo']
        instance.rating_blitz = additonal_data['blitz_elo']
        instance.save()
        print(instance.first_name_fide)
        print(instance.last_name_fide)