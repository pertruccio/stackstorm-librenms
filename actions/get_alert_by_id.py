from lib.actions import LibreNMSBaseAction


class GetDevice(LibreNMSBaseAction):
    """Get a single alert by ID"""

    method = "get"

    def run(self, id: str):
        self.api_call = f"alerts/{id}"
        return self._request()
