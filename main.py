from app import *
import views.views as views

FLASK_APP = "app"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='4000', debug=True)