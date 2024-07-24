from mitmproxy import http

from local_gateway.consts import AOAI_ENDPOINT_HEADER_NAME, GATEWAY_HOST, GATEWAY_PORT
from local_gateway.utils.redirect import HostMatcher


def request(flow: http.HTTPFlow) -> None:
    if "no-interception" in flow.request.headers:
        return

    # Azure OpenAI
    # try to parse endpoint following AOAI pattern
    # if so, set endpoint to header for gateway consumption
    endpoint = HostMatcher.parse_endpoint_from_aoai(flow.request.host)
    if endpoint is not None:
        flow.request.host = GATEWAY_HOST
        flow.request.port = GATEWAY_PORT
        flow.request.headers[AOAI_ENDPOINT_HEADER_NAME] = endpoint

    if flow.request.pretty_url.startswith("http://www.google.com"):
        flow.request.host = "www.baidu.com"

    # remove duplicated slashes, THOUGH don't know why...
    if flow.request.path.startswith("//"):
        flow.request.path = flow.request.path[1:]
