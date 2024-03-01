import requests



def test_can_call():

    body = {
        "id": 34,
        "name": "buddyone bossone",
        "user_login": "bbuser1",
    }
    ENDPOINT = "https://qa-automation01.uw2.developbb.dev/wp-json/buddyboss/v1/members"

    response = requests.get(ENDPOINT, json=body)

    print(response.json())
    assert response.status_code