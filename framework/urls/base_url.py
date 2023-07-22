class BaseUrl:

    def __init__(self):
        self._projects_list_page_url = 'company/personal/user/1/tasks/projects/'
        self._base_url = 'https://poznokosme.bitrix24.eu/'

    @property
    def base_url(self):
        return self._base_url

    @property
    def project_page_url(self):
        return self._base_url + self._projects_list_page_url
