def test_index_route(app,client):
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Verticle Tank Maintainance" in res.data
        assert b"Welcome to VTM" in res.data

def test_about_route(app,client):
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"About Verticle Tank Maintainance" in res.data



def test_estimate_route(app,client):
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert b"VTM Estimater" in res.data



def test_estimate_route(app,client):
    with app.test_client() as test_client:
        estimate_vtm = {"Radius":"180","Height":"360"}
        res = test_client.post('/estimate', data=estimate_vtm)
        assert res.status_code == 200
        