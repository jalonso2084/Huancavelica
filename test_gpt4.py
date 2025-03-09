import pytest
from unittest.mock import patch

@pytest.fixture
def client():
    from main import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# ✅ Mock OpenAI to prevent failure
@patch("openai.ChatCompletion.create", return_value={"choices": [{"message": {"content": "Test response"}}]})
def test_health_check(mock_openai, client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "API is running! Use /predict to make predictions."}

def test_prediction(client):
    data = {
        "variety": 1,
        "humidity": 85,
        "weather": 2,
        "soil": 3,
        "feature_5": 0,
        "feature_6": 0,
        "feature_7": 0,
        "feature_8": 0,
        "feature_9": 0,
        "feature_10": 0,
        "feature_11": 0
    }
    response = client.post('/predict', json=data)
    assert response.status_code == 200
    assert "prediction" in response.json
