import re
import typing


class HostMatcher:
    AOAI_PATTERN = re.compile(r"^([^.]+)\.openai\.azure\.com$")

    @staticmethod
    def parse_endpoint_from_aoai(host: str) -> typing.Optional[str]:
        match = re.match(HostMatcher.AOAI_PATTERN, host)
        if match:
            endpoint = match.group(1)
            return endpoint
        else:
            return None
