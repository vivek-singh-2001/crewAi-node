# from google.cloud import vision





# # Initialize Google Vision API client
# # vision_client = vision.ImageAnnotatorClient()

# def moderate_image(image_url):
#     """
#     Check if the image contains inappropriate content using Google Vision API.
    
#     Args:
#         image_url (str): URL of the image to be analyzed.
        
#     Returns:
#         dict: Result of the moderation with status and message.
#     """
#     try:
#         # Construct the image request
#         image = vision.Image()
#         image.source.image_uri = image_url
#         print(image_url)

#         # Perform safe search detection
#         response = vision_client.safe_search_detection(image=image)
#         safe_search = response.safe_search_annotation
#         print(response)
#         print(safe_search)

#         # Check response
#         if not safe_search:
#             return {"status": "error", "message": "No safe search annotations found."}

#         # Analyze safe search scores (scale: 0 (Very Unlikely) to 5 (Very Likely))
#         moderation_flags = {
#             "adult": safe_search.adult,
#             "violence": safe_search.violence,
#             "racy": safe_search.racy,
#             "medical": safe_search.medical,
#             "spoof": safe_search.spoof,
#         }

#         # Determine if the image is inappropriate
#         if any(score > 2 for score in moderation_flags.values()):
#             return {
#                 "status": "inappropriate",
#                 "flags": moderation_flags,
#                 "message": "Image contains inappropriate content."
#             }

#         return {
#             "status": "appropriate",
#             "flags": moderation_flags,
#             "message": "Image is appropriate."
#         }
#     except Exception as e:
#         return {"status": "error", "message": str(e)}
