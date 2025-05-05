from model.project import Project
import random


def test_delete_project(app):
    if app.project.count() == 0:
        app.project.create(Project(name="test"))

    username = "administrator"
    password = "root"
    old_project = app.soap.get_project_list(username, password)
    project = random.choice(old_project)
    app.project.delete_project_by_id(project.id)
    new_project = app.soap.get_project_list(username, password)
    assert len(old_project) - 1 == len(new_project)

