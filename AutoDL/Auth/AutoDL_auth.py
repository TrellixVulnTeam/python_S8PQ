import requests
import config.adss


def get_captcha():
    base_url = config.adss.server_ip()
    url = base_url + 'debug/captcha/get'
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    r = requests.get(url=url, headers=headers)
    cap_id = r.json()['data']['id']
    cap_val = r.json()['data']['value']
    return cap_id, cap_val


def login():
    base_url = config.adss.server_ip()
    url = base_url + 'new_login'
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    r = requests.post(url=url, json={
        "picture_id": "",
        "v_code": "",
        "phone": "16666666666",
        "password": "f865b53623b121fd34ee5426c792e5c33af8c227"
    }, headers=headers)
    ticket = r.json()["data"]["ticket"]
    return ticket


def change_ticket():
    ticket = login()
    base_url = config.adss.server_ip()
    url = base_url + 'passport'
    json = {
        "ticket": ticket
    }
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    r = requests.post(url=url, json=json, headers=headers)
    token = r.json()["data"]["token"]
    print(token)
    return token


if __name__ == '__main__':
    login()
