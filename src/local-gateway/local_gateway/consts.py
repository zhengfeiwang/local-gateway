GATEWAY_HOST = "127.0.0.1"
GATEWAY_PORT = 12345

# we need this header, otherwise gateway will forever forward the request
NO_INTERCEPTION_HEADER_NAME = "no-interception"
# Azure OpenAI
AOAI_API_KEY_HEADER_NAME = "api-key"
AOAI_ENDPOINT_HEADER_NAME = "aoai-endpoint"

TRACE_DESTINATION_DEFAULT_VALUE = "traces.json"
TRACE_DESTINATION_ENVIRON = "GATEWAY_TRACE_DESTINATION"
