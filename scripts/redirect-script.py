from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url.startswith("http://www.google.com"):
        flow.request.host = "www.baidu.com"
    # if flow.request.pretty_url.startswith("http://www.openai.com"):
    #     flow.request.host = "localhost"
    #     flow.request.port = 23333
    if flow.request.host == "www.openai.com":
        flow.request.host = "localhost"
        flow.request.port = 23333
    # TODO: recognize endpoint in host, and set it somewhere, maybe just in header
    # TODO: identify real request to remote with some identifier, e.g., header
    if flow.request.pretty_url.startswith("http://<endpoint>.openai.azure.com/"):
        flow.request.host = "localhost"
        flow.request.port = 23333
        flow.request.headers["endpoint"] = "<endpoint>"
