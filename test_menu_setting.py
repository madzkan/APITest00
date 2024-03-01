import requests
from utils import appID


def test_menu_settings():
    body = {         
         "tabbar": [
              {
            "label": "Home",
            "icon": {
                "id": "home",
                "uri": "https://qa-automation01.uw2.developbb.dev/wp-content/plugins/buddyboss-app/assets/icons/bb-icons/svg/lined/home.svg",
                "uri_active": "https://qa-automation01.uw2.developbb.dev/wp-content/plugins/buddyboss-app/assets/icons/bb-icons/svg/filled/home.svg",
                "type": "buddyboss",
                "style": "lined",
                "box_style": "none",
                "color": "#000000",
                "fg_color": "",
                "fill_color": True,
                "tint_color": "#000000",
                "monochrome": True,
                "icon_style": "outlined"
            },
            "id": "64400ba327378",
            "object": "app_page",
            "data": {
                "id": "9",
                "parent": "",
                "open_external": False
            },
            "type": "post_type",
            "bb_access": {
                "can_access": True,
                "restrict_message": "null"
            }
        }
         ]
    }

    ENDPOINT = "https://qa-automation01.uw2.developbb.dev/wp-json/buddyboss-app/core/v1/menu/"

    response = requests.get(ENDPOINT + "0c64cb", json=body)
    
    print(response.json())
    assert response.status_code