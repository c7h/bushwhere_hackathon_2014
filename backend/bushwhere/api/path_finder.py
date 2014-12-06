from models import Place

def get_next_place(current_location, visited_locations):
    lat, lon = current_location
    all_places = Place.objects.raw('SELECT * FROM api_place order by (lat - %s) * (lat - %s) + ((lon - %s) * 2) * ((lon - %s) * 2)', [lat, lat, lon, lon])
    possible_places = [p for p in all_places if (p.lat, p.lon) not in set(visited_locations)]
    return possible_places and possible_places[0] or None
