from routes import api
from config import app, db

app.register_blueprint(api)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    