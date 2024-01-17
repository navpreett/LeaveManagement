from app.routes import app
from app import app, db
import os

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5003)
print(os.getcwd())
