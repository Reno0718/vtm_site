import app

def test_area_tank():
    assert app.area_tank(360,180) == 3532.50

def test_price_tank():
    assert app.price_tank(3532.50) == 141300




    