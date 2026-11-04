from skyfield.api import load, wgs84

URL_STATIONS = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"

AGE_MAX_JOURS = 1

NOM_FICHIER = "stations.tle"

def charger_satellites():
    if not load.exists(NOM_FICHIER) or load.days_old(NOM_FICHIER) > AGE_MAX_JOURS:
        load.download(URL_STATIONS, filename=NOM_FICHIER)

    liste_satellites = load.tle_file(NOM_FICHIER)
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

        
    
        
        
       