import json
import requests
import config.adss

captcha_url = '/api/v1/debug/captcha/get'
login_url = '/api/v1/login'
passport_url = '/api/v1/passport'


class AuthManager:
    def __init__(self, base_url):
        self.base_url = base_url

        cap_id, cap_val = get_captcha(self.base_url)
        self.cap_id = cap_id
        self.cap_val = cap_val

        self.ticket = login(self.cap_id, self.cap_val, self.base_url)

        self.token = passport(self.base_url, self.ticket)

    def showToken(self):
        return self.token

    def show(self):
        print("base_ip: ", self.base_url)
        print("captcha_id: ", self.cap_id)
        print("captcha_value: ", self.cap_val)
        print("ticket: ", self.ticket)
        print("token: ", self.token)


def get_captcha(base_url):
    """获取验证码接口"""
    url = base_url + captcha_url
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    r = requests.get(url=url, headers=headers)
    print(r)
    cap_id = r.json()["data"]["id"]
    cap_val = r.json()["data"]["value"]
    return cap_id, cap_val


def login(cap_id, cap_val, base_url):
    url = base_url + login_url
    r = requests.post(url=url, json={
        "user_name": "admin",
        "password": "7af2d10b73ab7cd8f603937f7697cb5fe432c7ff",
        "app_name": "kpl",
        "captcha_id": cap_id,
        "captcha_value": cap_val})
    rt = r.json()
    ticket = rt["data"]["ticket"]
    return ticket


def passport(base_url, ticket):
    url = base_url + passport_url
    data = {
        "ticket": ticket
    }
    r = requests.post(url=url, data=data)
    return r.json()["data"]["token"]


if __name__ == '__main__':
    manager = AuthManager(config.adss.server_ip())
    manager.show()
    # print(manager.showToken())
