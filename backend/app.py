from flask import Flask
from flask_cors import CORS
from routes.news import news_bp
from routes.metrics import metrics_bp
from routes.aggregates import aggregates_bp
from routes.exchanges import exchanges_bp
from routes.twitter import twitter_bp
from routes.admin import admin_bp

def create_app():
    app = Flask(__name__)
    
    # Enable CORS for frontend communication
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(news_bp, url_prefix='/news')
    app.register_blueprint(metrics_bp, url_prefix='/metrics')
    app.register_blueprint(aggregates_bp, url_prefix='/aggregates')
    app.register_blueprint(exchanges_bp, url_prefix='/exchanges')
    app.register_blueprint(twitter_bp, url_prefix='/twitter')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    @app.route('/')
    def health_check():
        return {
            'status': 'ok',
            'message': 'CryptoBuzz Backend API',
            'version': '1.0.0'
        }
    
    return app

app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5001)