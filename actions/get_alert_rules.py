from lib.actions import LibreNMSBaseAction


class GetAlerts(LibreNMSBaseAction):
    """Get alert rules"""

    method = "get"

    def run(self, **kwargs):
        self.api_call = "rules"

        for key in kwargs:
            self.params[key] = kwargs[key]

        return self._request()