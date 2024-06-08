import requests


def get_data_from_fide(fide_id):
    player = requests.get(f'https://idgcb-3000.csb.app/player/{int(fide_id)}/info/').json()
    return player

#print(get_data_from_fide(13713442))