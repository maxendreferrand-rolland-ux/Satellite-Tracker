from skyfield.api import load
from tracker.donnees import charger_satellites
from tracker.calculs import calculer_position


def test_longitude_iss_valide():
    iss = charger_satellites()["ISS (ZARYA)"]
    maintenant = load.timescale().now()

    latitude, longitude, altitude = calculer_position(iss, maintenant)

    assert -180 <= longitude <= 180