class UrlBase:

    def __init__(self):
        self._base_url = 'https://poznokosme.bitrix24.eu/'

    @property
    def base_url(self):
        return self._base_url
