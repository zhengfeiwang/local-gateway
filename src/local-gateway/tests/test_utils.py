from local_gateway.utils.redirect import HostMatcher


class TestHostRegex:
    def test_aoai(self):
        text = "gpt-test.openai.azure.com"
        endpoint = HostMatcher.parse_endpoint_from_aoai(text)
        assert endpoint == "gpt-test"
