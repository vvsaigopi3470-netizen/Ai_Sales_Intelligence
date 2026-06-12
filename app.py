from flask import Flask
from config import Config

from database.mysql_db import mysql

# Routes

from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.sales import sales_bp
from routes.ai import ai_bp
from routes.intelligence import intelligence_bp
from routes.product import product_bp
from routes.customer import customer_bp
from routes.inventory import inventory_bp

# APIs

from api.forecast_api import forecast_api

app = Flask(__name__)

# Configuration

app.config.from_object(Config)

# Initialize MySQL

mysql.init_app(app)

# Register Blueprints

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(sales_bp)
app.register_blueprint(ai_bp)
app.register_blueprint(intelligence_bp)
app.register_blueprint(forecast_api)
app.register_blueprint(product_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(inventory_bp)

@app.route("/")
def home():
    return "AI Sales Intelligence Platform Running Successfully"

if __name__ == "__main__":
    print(app.url_map)
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
