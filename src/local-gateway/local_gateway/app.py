import json
import typing
import uuid

from fastapi import FastAPI, Request
from opentelemetry import trace
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import StreamingResponse

from local_gateway.api.v1.routes import router
from local_gateway.utils.open_telemetry import setup_otel

app = FastAPI(
    title="Local Gateway",
)

setup_otel()
app.include_router(router)


class TraceMiddleware(BaseHTTPMiddleware):
    _span = None

    async def dispatch(self, request: Request, call_next):
        tracer = trace.get_tracer("local-gatewstary")
        with tracer.start_as_current_span(name="interception-request", end_on_exit=False) as span:
            response = None
            try:
                self._span = span
                body = await request.body()
                body_data = body.decode("utf-8")
                body_json = json.loads(body_data)
                # TODO: can retrieve from url maybe
                self._span.set_attribute("llm.model", body_json.get("model", "unknown"))
                self._span.set_attribute("llm.prompt", body_json["messages"][1]["content"])
                response = await call_next(request)
                return response
            except Exception:
                raise
            finally:
                if not response:
                    pass
                if isinstance(response, StreamingResponse):
                    response.body_iterator = self.stream_iterator(response.body_iterator)
                else:
                    self._span.set_attribute("uuid.4", str(uuid.uuid4()))
                    self._span.end()

    async def stream_iterator(self, stream: typing.Callable):
        try:
            response_body = b""
            async for chunk in stream:
                response_body += chunk
                yield chunk
            await self.set_token(response_body)
        except Exception as e:
            self._span.record_exception(e)
            self._span.end()
            raise

    async def set_token(self, response_body):
        response_body = response_body.decode("utf-8")
        response_body = json.loads(response_body)
        self._span.set_attribute("usage.prompt", response_body["usage"]["prompt_tokens"])
        self._span.set_attribute("usage.completion", response_body["usage"]["completion_tokens"])
        self._span.set_attribute("usage.total", response_body["usage"]["total_tokens"])
        self._span.set_attribute("llm.output", response_body["choices"][0]["message"]["content"])
        self._span.end()


app.add_middleware(TraceMiddleware)
