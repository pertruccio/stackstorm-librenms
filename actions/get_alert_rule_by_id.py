from lib.actions import LibreNMSBaseAction


class GetDevice(LibreNMSBaseAction):
    """Get a single alert rule by ID"""

    method = "get"

    def run(self, id: str):
        self.api_call = f"rules/{id}"
        return self._request()
