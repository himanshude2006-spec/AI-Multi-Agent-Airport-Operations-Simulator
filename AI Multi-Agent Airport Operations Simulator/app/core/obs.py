from app.core.config import a

def b(c):
    if a.sentry_dsn:
        import sentry_sdk
        sentry_sdk.init(dsn=a.sentry_dsn, environment=a.app_env)
    if a.otel_exporter_otlp_endpoint:
        from opentelemetry import trace
        from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor
        d = TracerProvider(resource=Resource.create({"service.name": a.app_name}))
        d.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=a.otel_exporter_otlp_endpoint, insecure=True)))
        trace.set_tracer_provider(d)
        from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
        FastAPIInstrumentor.instrument_app(c)
