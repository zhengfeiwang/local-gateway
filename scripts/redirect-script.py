from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url.startswith("http://www.google.com"):
        flow.request.host = "www.baidu.com"
    if flow.request.pretty_url.startswith("http://www.openai.com"):
        flow.request.host = "localhost"
        flow.request.port = 5000
