from model.project import Project
import random


def test_delete_project(app):
    if app.project.count() == 0:
        app.project.create(Project(name="test"))

    old_project = app.project.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_id(project.id)
    new_project = app.project.get_project_list()
    assert len(old_project) - 1 == len(new_project)

