import requests

ENDPOINT = "https://todo.pixegami.io/"

def test_call_endpoint1():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_task1():
    payload = {
        "user_id": "Testuser",
        "task_id": "testID",
        "is_done": False,
    }
    response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert response.status_code == 422

    data = response.json()
    print(data)
