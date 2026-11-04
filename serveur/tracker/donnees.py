from skyfield.api import load, wgs84

URL_STATIONS = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"


def charger_satellites():
    liste_satellites = load.tle_file(URL_STATIONS, filename="stations.tle")
    satellites = {}
    for satellite in liste_satellites:
        satellites[satellite.name] = satellite
        
    return satellites

def afficher_position(satellite):

    echelle_temps = load.timescale()
    maintenant = echelle_temps.now()

    position = satellite.at(maintenant)

    latitude, longitude = wgs84.latlon_of(position)
    altitude = wgs84.height_of(position)
    print("\n"+satellite.name)
    print("Latitude :", round( latitude.degrees, 2))
    print("Longitude :", round( longitude.degrees, 2))
    print("Altitude :", round( altitude.km, 2), "km")
    

if __name__ == "__main__":
    satellites = charger_satellites()
    iss = satellites["ISS (ZARYA)"]
    tian = satellites["CSS (TIANHE)"]
    liste = [iss, tian]
    for satellite in liste : 
        afficher_position(satellite)

        
    
        
        
       