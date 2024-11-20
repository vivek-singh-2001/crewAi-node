from google.cloud import vision
from google.cloud.vision import types 

# Initialize Google Vision API client
vision_client = vision.ImageAnnotatorClient()

def moderate_image(image_url):
    # Request to analyze the image
    image = types.Image()
    image.source.image_uri = image_url

    # Perform image annotation to check for inappropriate content
    try:
        response = vision_client.safe_search_detection(image=image)
        safe_search = response.safe_search_annotation

        # Check for explicit content in the image
        if safe_search.adult > 2 or safe_search.violence > 2:
            return {"status": "inappropriate", "message": "Image contains inappropriate content"}

        return {"status": "appropriate", "message": "Image is appropriate"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
