from flask_swagger_ui import get_swaggerui_blueprint

swagger_bp = get_swaggerui_blueprint(
    '/swagger-docs',
    '/static/swagger/config.json',
    config={
        "API Service App": "Collection of endpoints"
    }
)
