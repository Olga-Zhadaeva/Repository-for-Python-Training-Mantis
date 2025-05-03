from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app
        self.project_cache = None

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Manage").click()
        wd.find_element(By.LINK_TEXT, "Manage Projects").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.input_type("name", project.name)
        self.select_type("status", project.status)
        self.checkbox_type("inherit_global", project.inheritance)
        self.select_type("view_state", project.view_status)
        self.input_type("description", project.description)

    def input_type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def select_type(self, select_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, select_name).click()
            Select(wd.find_element(By.NAME, select_name)).select_by_visible_text(text)

    def checkbox_type(self, field_name, value):
        wd = self.app.wd
        checkbox = wd.find_element(By.NAME, field_name)
        if value is not None:
            if checkbox.is_selected() != value:
                checkbox.click()

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element(By.XPATH, "//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        # submit project creation
        wd.find_element(By.XPATH, '//*[@value="Add Project"]').click()
        self.project_cache = None

    def count(self):
        wd = self.app.wd
        self.open_project_page()
        return len(wd.find_elements(By.CSS_SELECTOR, "table.width100 tr[class^='row-']")[1:])

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for row in wd.find_elements(By.CSS_SELECTOR, "table.width100 tr[class^='row-']")[1:]:
                cells = row.find_elements(By.TAG_NAME, "td")
                name = cells[0].text
                link_elem = cells[0].find_element(By.TAG_NAME, "a")
                link = link_elem.get_attribute("href")
                project_id = link.split("=")[-1]
                self.project_cache.append(Project(name=name, id=project_id))
        return list(self.project_cache)

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, f"a[href='manage_proj_edit_page.php?project_id={id}']").click()

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_id(id)
        #submit deletion
        wd.find_element(By.XPATH, '//*[@value="Delete Project"]').click()
        wd.find_element(By.XPATH, '//*[@value="Delete Project"]').click()
        self.project_cache = None