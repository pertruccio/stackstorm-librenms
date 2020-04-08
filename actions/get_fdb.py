from lib.actions import LibreNMSBaseAction


class GetIPARP(LibreNMSBaseAction):
    """Get FDB information"""

    method = "get"

    def run(self, mac: str):
        self.api_call = f"resources/fdb/{mac}"
        return self._request()
