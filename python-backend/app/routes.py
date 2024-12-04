# app/routes.py
from flask import Blueprint, request, jsonify
from crewai import Agent
from flask_cors import cross_origin
from langchain_google_genai import GoogleGenerativeAI
from app.config import Config
from app.features.content_moderation import moderate_content



app = Blueprint('app', __name__)

# Initialize Google API Client
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=Config.GOOGLE_API_KEY)

@app.route('/create-agent', methods=['POST'])
def create_agent():
    data = request.json
    agent_name = data.get('agentName')
    
    # Create the agent
    role = "Research Analyst"
    goal = "Conduct thorough research on the importance of CSS in web development"
    backstory = "An expert analyst with a keen eye for web development trends."

    try:
        agent = Agent(role=role, goal=goal, backstory=backstory, llm=llm)
        
        return jsonify({"message": f"Agent {agent_name} created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/assign-task', methods=['POST'])
def assign_task():
    data = request.json
    task_description = data.get('taskDescription')

    # This is where you'd normally process the task with the agent
    try:
        # Call the agent's logic to perform the research
        # This is a placeholder for task execution logic
        result = llm.predict(f"Research the importance of CSS in web development: {task_description}")

        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/check-content', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def check_content():
    # Get content from the request
    

    data = request.json
    print(data)
    title = data.get('title')
    description = data.get('description')
    image_url = request.get('image_url', None)

    if not title or not description:
        return jsonify({"error": "Title and Description are required"}), 400

    # Call the content moderation function
    moderation_result = moderate_content(title, description, image_url)

    return jsonify(moderation_result), 200