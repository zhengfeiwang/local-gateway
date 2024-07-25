import os

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SimpleSpanProcessor, SpanExporter, SpanExportResult

from local_gateway.consts import TRACE_DESTINATION_DEFAULT_VALUE, TRACE_DESTINATION_ENVIRON


def setup_tracer_provider():
    attributes = {"service.name": "local-gateway"}
    resource = Resource(attributes=attributes)
    tracer_provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(tracer_provider)


class FileExporter(SpanExporter):
    def __init__(self, filename: str):
        self._filename = filename

    def export(self, spans):
        span_data = [span.to_json() for span in spans]
        for span_json in span_data:
            with open(self._filename, "a") as f:
                f.write(span_json + "\n")
        return SpanExportResult.SUCCESS

    def shutdown(self):
        pass


def setup_exporter():
    trace_dest = os.getenv(TRACE_DESTINATION_ENVIRON)
    if trace_dest is None:
        trace_dest = TRACE_DESTINATION_DEFAULT_VALUE
    file_exporter = FileExporter(trace_dest)
    span_processor = SimpleSpanProcessor(file_exporter)
    tracer_provider: TracerProvider = trace.get_tracer_provider()
    tracer_provider.add_span_processor(span_processor)


def setup_exporter2pfs():
    exporter = OTLPSpanExporter(endpoint="http://127.0.0.1:23333/v1/traces")
    tracer_provider: TracerProvider = trace.get_tracer_provider()
    tracer_provider.add_span_processor(
        BatchSpanProcessor(exporter, schedule_delay_millis=1000)
    )


def setup_otel():
    setup_tracer_provider()
    setup_exporter()
    if os.getenv("LOCAL_GATEWAY_LEVERAGE_PF") == "true":
        setup_exporter2pfs()
