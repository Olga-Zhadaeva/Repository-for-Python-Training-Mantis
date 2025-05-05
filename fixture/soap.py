from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_project_list(self, username, password):
        client = Client('http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl')
        try:
            project_list = client.service.mc_projects_get_user_accessible(username, password)
            return list(project_list)
        except WebFault:
            print("SOAP ERROR")