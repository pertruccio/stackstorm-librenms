from lib.actions import LibreNMSBaseAction


class GetAlerts(LibreNMSBaseAction):
    """Get alerts"""

    method = "get"

    def run(self, **kwargs):
        self.api_call = "alerts"

        for key in kwargs:
            self.params[key] = kwargs[key]

        return self._request()