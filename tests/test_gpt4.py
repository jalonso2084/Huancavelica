import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'OK'
    assert data['model_loaded'] is True

def test_prediction(client):
    data = {
        "variety": "INIA-303 Canchan",
        "humidity": 85,
        "weather_condition": "Rain",
        "soil_type": "Loamy",
        "plant_health_index": 0.85,
        "disease_pressure_index": 0.7,
        "growth_stage": "Vegetative",
        "canopy_coverage": 0.9,
        "rainfall": 120,
        "temperature_variability": 15,
        "soil_moisture": 0.3
    }
    response = client.post('/predict', json=data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['prediction'] in ["High Risk", "Low Risk"]
