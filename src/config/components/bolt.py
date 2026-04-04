"""Настройки Bolt"""

from django_bolt import FileSize, OpenAPIConfig, SwaggerRenderPlugin

BOLT_MAX_UPLOAD_SIZE = FileSize.MB_50

openapi_config = OpenAPIConfig(
    title="Лучшие сборки компьютеров",
    version="1.0.0",
    description="Апи приложения «Лучшие сборки компьютеров»",
    enabled=True,
    path="/openapi",
    render_plugins=[
        SwaggerRenderPlugin(path="/"),
    ],
    servers=None,
)
