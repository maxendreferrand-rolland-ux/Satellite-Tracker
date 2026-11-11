from skyfield.api import wgs84

def calculer_position(satellite, instant):

    position = satellite.at(instant)

    latitude, longitude = wgs84.latlon_of(position)
    altitude = wgs84.height_of(position)
    return latitude.degrees, longitude.degrees, altitude.km