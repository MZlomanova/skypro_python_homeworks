import requests
import json
from lesson8.constants import X_client_URL

path = "/employee/"


class Company:
    def __init__(self, url=X_client_URL):
        self.url = url

    # create company
    def create_company(self, token: str, body: json):
        headers = {"x-client-token": token}
        response = requests.post(
            self.url + "/company", headers=headers, params=body)
        return response.json()

    # последняя активная созданная компания

    def last_active_company(self):
        active_params = {"active": "true"}
        response = requests.get(self.url + "/company", params=active_params)
        return response.json()[-1]["id"]


class Employee:
    def __init__(self, url=X_client_URL):
        self.url = url

    # список сотрудников
    def get_list(self, company_id: int):
        body = {"company": company_id}
        response = requests.get(
            self.url + "/employee", params=body)
        return response.json()

    # добавить сотрудника
    def add_new_employee(self, token: str, body: json):
        headers = {"x-client-token": token}
        response = requests.post(
            self.url + "/employee", headers=headers, json=body)
        return response.json()

    # получить инфо о сотруднике
    def get_info(self, employee_id: int):
        response = requests.get(self.url + path + str(employee_id))
        return response

    # изменении инфо о сотруднике
    def change_info(self, token: str, employee_id: int, body: json):
        headers = {"x-client-token": token}
        response = requests.patch(
            self.url + path + str(employee_id), headers=headers, json=body
        )
        return response
