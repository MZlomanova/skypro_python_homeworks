from lesson8.classes.todoclass import Task

todoshka = Task()


def test_to_do():
    # посмотреть список задач
    list = todoshka.get_list()
    assert list.status_code == 200

    # создать задачу
    params = {"title": "Задачка1", "completed": "false"}
    task = todoshka.create(params)
    assert task is not None

    # изменить название задачи
    params = {"title": "Задачка1 переименована"}
    renamed_task = todoshka.rename(task, params)
    assert renamed_task.json()["title"] == "Задачка1 переименована"

    # получить информацию по созданной задаче
    info = todoshka.info(task)
    assert info.json()["title"] == "Задачка1 переименована"
    assert info.json()["id"] == task

    # изменение статуса задачи на выполнено
    params = {"completed": "true"}
    status_true = todoshka.change_status(task, params)
    assert status_true == True

    # снятие отметки "выполнено", возвращение задачи
    params = {"completed": "false"}
    status_false = todoshka.change_status(task, params)
    assert status_false == False

    # удаление задачи
    print(task)
    delete = todoshka.delete(task)
    assert delete == 200
