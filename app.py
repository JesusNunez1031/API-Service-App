from flask import Flask
from flask_cors import CORS
from routes import ping, swagger

app = Flask(__name__)
CORS(app)
app.register_blueprint(swagger.swagger_bp)
app.register_blueprint(ping.ping_bp)

if __name__ =='__main__':
    app.run(host="0.0.0.0", port=7701, debug=True)