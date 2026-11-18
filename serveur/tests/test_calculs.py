from skyfield.api import load
from tracker.donnees import charger_satellites
from tracker.calculs import calculer_position

@pytest.fixture
def position_iss():
    iss = charger_satellites()["ISS (ZARYA)"]
    maintenant = load.timescale().now()
    return calculer_position(iss, maintenant)


def test_charger_satellites_contient_iss():

    assert "ISS (ZARYA)" in charger_satellites() 

def test_longitude_iss_valide(position_iss):

    latitude, longitude, altitude = calculer_position(iss, maintenant)

    assert -180 <= longitude <= 180

def test_latitude_iss_limitee_par_inclinaison(position_iss):

    latitude, longitude, altitude = calculer_position(iss, maintenant)

    assert abs(latitude) < 52


def test_altitude_iss_valide(position_iss):

    latitude, longitude, altitude = calculer_position(iss, maintenant)

    assert 370 <= altitude <= 460