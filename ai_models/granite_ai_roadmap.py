import os
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Optionally load environment variables from a .env file
load_dotenv()

# IBM Credentials - load from environment variables
API_KEY = os.environ.get("IBM_API_KEY")
PROJECT_ID = os.environ.get("IBM_PROJECT_ID")
MODEL_ID = os.environ.get("IBM_MODEL_ID", "ibm/granite-3-3-8b-instruct")
URL = os.environ.get("IBM_URL", "https://us-south.ml.cloud.ibm.com")

# Check for missing credentials
if not API_KEY or not PROJECT_ID:
    raise ValueError("IBM_API_KEY and IBM_PROJECT_ID environment variables must be set.")

# Authentication
authenticator = IAMAuthenticator(API_KEY)

# Initialize the inference model correctly
model = ModelInference(
    model_id=MODEL_ID,
    project_id=PROJECT_ID,
    credentials={
        "apikey": API_KEY,
        "url": URL
    }
)

# Function to generate roadmap
def generate_ai_roadmap(name, skill_level, interests, goal, hours):
    interests_str = ", ".join(interests)
    prompt = f"""
    You are LearnMate, an intelligent AI career assistant.

    Student name: {name}
    Skill Level: {skill_level}
    Interests: {interests_str}
    Career Goal: {goal}
    Weekly Study Time: {hours} hours

    Create a clear 10-week learning roadmap. For each week, include:
    - Topic name
    - Short description (1 line)

    Start each week with "Week X:" followed by topic and details.
    """

    # Send the prompt to IBM Granite
    params = {
        GenParams.DECODING_METHOD: "greedy",
        GenParams.MAX_NEW_TOKENS: 600,
        GenParams.TEMPERATURE: 0.7
        # Removed STOP_SEQUENCES to avoid early stopping
    }

    try:
        response = model.generate_text(prompt=prompt, params=params)
        return response  # response is already a string
    except Exception as e:
        return f"Error generating roadmap: {str(e)}"
if __name__ == "__main__":
    output = generate_ai_roadmap(
        name="Gugulothu Ganesh",
        skill_level="Beginner",
        interests=["Frontend Development", "UI/UX Design"],
        goal="Become a Full Stack Web Developer",
        hours=6
    )
    print(output)
