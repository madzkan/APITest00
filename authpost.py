import requests
import json


def get_me():
    #head = {
    #"accessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvcWEtYXV0b21hdGlvbjAxLnV3Mi5kZXZlbG9wYmIuZGV2OnJlc3QtYXBpIiwiaWF0IjoxNzA4NTg5ODkzLCJuYmYiOjE3MDg1ODk4OTMsImV4cCI6MTcxNjM2NTg5MywianRpIjoiS2Q2RnFhOSQpcXFTd3NEQndHNkt2eGI1Y09jbFNYJUtFMHFQJlM0dTJBRSIsImRhdGEiOnsidXNlciI6eyJpZCI6IjI5In19fQ.2iS4zK6OKZ2m-v3qD1b1O2Rd-6f69PTiTatJ2jfmtQM",
    #}
    body = {
        "id": 34,
        "name": "buddyone bossone",
        "user_login": "bbuser1",
    }
    ENDPOINT = "https://qa-automation01.uw2.developbb.dev/wp-json/buddyboss/v1/members"

    response = requests.get(ENDPOINT, json=body)

    print(response.json())
    assert response.status_code