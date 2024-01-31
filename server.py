from flask_app import app
from flask_app.controllers import character_controller



if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.