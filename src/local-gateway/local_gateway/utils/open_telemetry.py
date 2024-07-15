import time

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider, ReadableSpan
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, SpanExporter, SpanExportResult


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
    file_exporter = FileExporter("./spans.json")
    span_processor = SimpleSpanProcessor(file_exporter)
    tracer_provider: TracerProvider = trace.get_tracer_provider()
    tracer_provider.add_span_processor(span_processor)


def setup_otel():
    setup_tracer_provider()
    setup_exporter()
