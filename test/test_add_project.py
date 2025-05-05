from model.project import Project


def test_add_project(app):
    username = "administrator"
    password = "root"
    old_project = app.soap.get_project_list(username, password)
    app.project.create(Project(name="test14", status="release", inheritance=True, view_status="private", description="description test"))
    new_project = app.soap.get_project_list(username, password)
    assert len(old_project) + 1 == len(new_project)
