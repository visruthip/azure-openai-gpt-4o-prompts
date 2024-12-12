import os
import json
import time  # For measuring latency
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    api_version=os.getenv("OPENAI_API_VERSION")
)

# Select the model
model = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# Loading prompts from json
def load_prompts_from_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
        return data.get("prompts", [])

prompts = load_prompts_from_json('prompts.json')

# Function to get responses for each prompt
def get_response_for_prompt(prompt):
    try:
        # Add system message along with the prompt
        messages = [{"role": "system", "content": "You are a helpful assistant."}, prompt]
        
        # Record the start time
        start_time = time.time()

        # Request to the Azure OpenAI API
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        
        # Record the end time and calculate latency
        end_time = time.time()
        latency = end_time - start_time

        # Print the prompt and the corresponding response
        print(f"Response for prompt: {prompt['content']}")
        print(response.choices[0].message.content)
        print(f"Latency: {latency:.4f} seconds")
        print("="*50)  # Separator for readability

    except Exception as e:
        print(f"Error for prompt '{prompt['content']}': {e}")

# Process each prompt
for prompt in prompts:
    get_response_for_prompt(prompt)
