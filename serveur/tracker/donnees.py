from skyfield.api import load
from tracker.calculs import calculer_position, trouver_evenements

URL_STATIONS = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"

AGE_MAX_JOURS = 1

NOM_FICHIER = "stations.tle"

maintenant = load.timescale().now()


def charger_satellites():
    if not load.exists(NOM_FICHIER) or load.days_old(NOM_FICHIER) > AGE_MAX_JOURS:
        load.download(URL_STATIONS, filename=NOM_FICHIER)

    liste_satellites = load.tle_file(NOM_FICHIER)
    satellites = {}
    for satellite in liste_satellites:
        satellites[satellite.name] = satellite

    return satellites

def afficher_position(satellite):
    maintenant = load.timescale().now()
    latitude, longitude, altitude = calculer_position(satellite, maintenant)

    print("\n" + satellite.name)
    print("Latitude :", round(latitude, 2))
    print("Longitude :", round(longitude, 2))
    print("Altitude :", round(altitude, 2), "km")



if __name__ == "__main__":
    satellites = charger_satellites()
    iss = satellites["ISS (ZARYA)"]
    tian = satellites["CSS (TIANHE)"]
    liste = [iss, tian]
    for satellite in liste : 
        afficher_position(satellite)
    print("\nPassages de l'ISS au-dessus de Rodez (24 h) :")
    instants, evenements = trouver_evenements(iss, maintenant, maintenant + 1)
    NOMS_EVENEMENTS = ["lever", "culmination", "coucher"]
    for instant, evenement in zip(instants, evenements):
        print(instant.utc_strftime("%d/%m %H:%M"), NOMS_EVENEMENTS[evenement])