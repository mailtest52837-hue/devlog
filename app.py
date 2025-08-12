from flask import Flask
from flask_cors import CORS

from db import Base, engine
from routes import routes

import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
CORS(app)

Base.metadata.create_all(bind=engine)
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
