from model.project import Project


def test_add_project(app):
    old_project = app.project.get_project_list()
    app.project.create(Project(name="test7", status="release", inheritance=True, view_status="private", description="description test"))
    new_project = app.project.get_project_list()
    assert len(old_project) + 1 == len(new_project)
