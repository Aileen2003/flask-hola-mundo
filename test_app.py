from app import app

def test_home():
    cliente = app.test_client()
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert b"API funcionando en Flask" in respuesta.data

def test_saludo():
    cliente = app.test_client()
    respuesta = cliente.get("/saludo")
    assert respuesta.status_code == 200
    data = respuesta.get_json()
    assert data["mensaje"] == "Hola mundo"