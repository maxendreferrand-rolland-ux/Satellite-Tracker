from skyfield.api import wgs84

LATITUDE_RODEZ = 44.35
LONGITUDE_RODEZ = 2.57
HAUTEUR_MINIMALE_DEGRES = 10.0

def calculer_position(satellite, instant):

    position = satellite.at(instant)

    latitude, longitude = wgs84.latlon_of(position)
    altitude = wgs84.height_of(position)
    return latitude.degrees, longitude.degrees, altitude.km

def trouver_evenements(satellite, debut, fin):
    observateur = wgs84.latlon(LATITUDE_RODEZ, LONGITUDE_RODEZ)
    return satellite.find_events(observateur, debut, fin, HAUTEUR_MINIMALE_DEGRES)