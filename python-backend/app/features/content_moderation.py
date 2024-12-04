from langchain_google_genai import GoogleGenerativeAI
from app.config import Config
# from app.features.image_moderation import moderate_image

# Initialize the AI client (Google's Gemini model)
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=Config.GOOGLE_API_KEY)

# Function to check content for moderation
def moderate_content(title, description, image_url=None):
    # Refined prompt for moderation (title and description)
    prompt = f"Please check the following content for any offensive or inappropriate language in  Title: {title}, Description: {description} \n if it is offensive or inappropriate then return yes else and if it is not inappropriate then return no."

    try:
        result = llm.predict(prompt)
        print(result)
        # Check if the AI model detects inappropriate content in title and description
         # Check if the AI model returns 'yes' for inappropriate content
        if "yes" in result.lower():
            return {"status": "inappropriate", "message": "Title or Description is inappropriate"}

        # If image moderation is enabled, check the image only if image_url is provided
        # if image_url:
        #     image_result = moderate_image(image_url)
        #     if image_result["status"] == "inappropriate":
        #         return image_result  # Return image moderation result if inappropriate

        # If both title, description, and image are appropriate, return appropriate message
        
        return {"status": "appropriate", "message": "Title and Description are appropriate"}

    except Exception as e:
        return {"status": "error", "message": str(e)}
