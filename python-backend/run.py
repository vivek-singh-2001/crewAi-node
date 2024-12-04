import os
from app import app

# Set environment variable for Google API credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../../../cloud-vision.json"
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
