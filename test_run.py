import requests

ENDPOINT = "https://todo.pixegami.io/"

def can_create_task():
    payload = {
        "content": "string",
        "user_id": "string",
        "task_id": "string",
        "is_done": False
    }

    response = requests.put(ENDPOINT, + "/create task", json=payload)
    assert response.status_code == 200

    data = response.json()
    print(data)
