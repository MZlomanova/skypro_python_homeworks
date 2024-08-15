from lesson8.classes.employee import Employee, Company

employee = Employee()
company = Company()


# авторизация (получение токена)
def test_auth(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)


# получение id компании
def test_get_company_id():
    company_id = company.last_active_company()
    assert company_id is not None
    assert str(company_id).isdigit()


# добавление сотрудника
def test_add_employee(get_token):
    token = str(get_token)
    comp_id = company.last_active_company()
    body_employee = {
        "id": 0,
        "firstName": "Marina",
        "lastName": "Zlomanova",
        "middleName": "string",
        "companyId": comp_id,
        "email": "abc@mail.com",
        "url": "string",
        'phone': "string",
        "birthdate": "2024-08-11T09:54:00.900Z",
        "isActive": True,
    }
    new_employee_id = (employee.add_new_employee(token, body_employee))["id"]
    assert new_employee_id is not None
    assert str(new_employee_id).isdigit()

    info = employee.get_info(new_employee_id)
    assert info.json()["id"] == new_employee_id
    assert info.status_code == 200


# получение списка сотрудников по компании
def test_get_employee():
    comp_id = company.last_active_company()
    list_employers = employee.get_list(comp_id)
    print(list_employers)
    assert isinstance(list_employers, list)


# изменение данных о сотруднике
def test_change_employee_info(get_token):
    comp_id = company.last_active_company()
    body_employee = {
        "id": 0,
        "firstName": "Marina",
        "lastName": "Zlomanova",
        "middleName": "string",
        "companyId": comp_id,
        "email": "abc@mail.com",
        "url": "string",
        "phone": "string",
        "birthdate": "2024-08-11T09:54:00.900Z",
        "isActive": "true",
    }
    just_employee = employee.add_new_employee(get_token, body_employee)
    id = just_employee["id"]
    body_change_employee = {
        "lastName": "Slomanova",
        "email": "abcd@mail.com",
        "url": "string",
        "phone": "string",
        "isActive": "true",
    }
    employee_changed = employee.change_info(
        get_token, id, body_change_employee)
    assert employee_changed.status_code == 200

    # проверка обязательности полей


# наличие токена
def test_add_employee_no_token():
    comp_id = company.last_active_company()
    token = ""
    body_employee = {
        "id": 0,
        "firstNme": "Vasya",
        "lastName": "Pupkin",
        "middleName": "string",
        "companyId": comp_id,
        "email": "test@nail.com",
        "url": "string",
        "phone": "string",
        "birthdate": "2024-08-11T09:54:00.900Z",
        "isActive": True,
    }
    new_employee = employee.add_new_employee(token, body_employee)
    assert new_employee["message"] == "Unauthorized"


# информация о сотруднике без id
def test_get_empl_info_no_id():
    try:
        employee.get_info()
    except TypeError as e:
        assert (
            str(e) == "Employee.get_info() "
            "missing 1 required positional argument: 'employee_id'"
        )


# проверка запроса на получение списка сотрудников без id компании


def test_get_list_employee_no_comp_id():
    res = employee.get_list(None)
    assert 500 == res["statusCode"]


# запрос без тела
def test_add_employee_no_body(get_token):
    body_employee = {}
    new_employer = employee.add_new_employee(
        token=get_token, body=body_employee)
    assert new_employer["message"] == "Internal server error"
