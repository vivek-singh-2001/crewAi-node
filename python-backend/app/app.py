# app/app.py
from flask import Flask, request, jsonify
from crewai import Agent
from flask_cors import CORS
from langchain_google_genai import GoogleGenerativeAI
from crewai_tools import SerperDevTool
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS for all routes
CORS(app, supports_credentials=True)
# CORS(app)


llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=app.config['GOOGLE_API_KEY'])

@app.route('/create-agent', methods=['POST'])
def create_agent():
    data = request.get_json()
    role = data.get('role', 'Researcher')
    goal = data.get('goal', 'Conduct thorough research')
    backstory = data.get('backstory', 'An agent dedicated to research.')

    try:
        agent = Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            llm=llm,
            tools=[SerperDevTool()],
            allow_delegation=False,
            verbose=True,
            max_iter=25,
        )

        return jsonify({
            "status": "success",
            "role": agent.role,
            "goal": agent.goal
        }), 201
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
