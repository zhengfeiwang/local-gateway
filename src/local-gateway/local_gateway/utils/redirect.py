import re
import typing

from local_gateway.consts import AOAI_API_KEY_HEADER_NAME, NO_INTERCEPTION_HEADER_NAME


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


def create_aoai_request_headers(api_key: str) -> typing.Dict[str, str]:
    return {
        "content-type": "application/json",
        AOAI_API_KEY_HEADER_NAME: api_key,
        NO_INTERCEPTION_HEADER_NAME: "true",
    }
