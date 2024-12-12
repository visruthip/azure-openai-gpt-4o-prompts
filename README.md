# Azure OpenAI GPT-4 Prompts Project

This project demonstrates how to interact with the Azure OpenAI API using Python. It loads prompts from a JSON file, sends them to the Azure OpenAI GPT model, and displays the responses.

## Project Structure

```
gpt-12Dec/
├── .env                # Environment variables for API authentication
├── app.py              # Main application to interact with OpenAI API
├── prompts.json        # JSON file containing user prompts
├── venv/               # Virtual environment directory (created via `python -m venv venv`)
└── .git/               # Git repository metadata
```

### Key Files:

- **.env**: Stores sensitive information such as API keys and endpoints.
- **app.py**: Main script to load prompts, interact with the Azure OpenAI API, and print responses.
- **prompts.json**: Contains the list of user prompts that are sent to the OpenAI API.
- **venv/**: The virtual environment directory to isolate project dependencies.

---

## Prerequisites

- Python 3.x
- Azure OpenAI account with API access
- Git (for version control and pushing to GitHub)
- AWS instances(ip address) --optional

---
Once the files in the repo were cloned to vscode/local, follow below steps:

## Setup Instructions

### 1. Clone the Repository

Clone the project from GitHub to your local machine:

```bash
git clone <repo-url>
cd azure-openai-gpt-4o-prompts
```

### 2. Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage the project dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 3. Install Dependencies

Install the necessary Python packages (`openai` and `python-dotenv`):

```bash
pip install openai python-dotenv
```

### 4. Create the `.env` File

Create a `.env` file in the root directory of the project. This file will store the environment variables required to authenticate with the Azure OpenAI API.

Example `.env` file:

```
AZURE_OPENAI_DEPLOYMENT_NAME="gpt-4o"
OPENAI_API_KEY="your-api-key-here"
OPENAI_API_BASE="https://your-api-endpoint"
OPENAI_API_VERSION="2024-08-01-preview"
```

Replace the placeholders with your actual Azure OpenAI API key and endpoint.

### 5. Add Your Prompts to `prompts.json`

The `prompts.json` file contains the list of prompts that will be sent to the API. You can add or modify the prompts in this file.

Example `prompts.json` file:

```json
{
  "prompts": [
    {
      "role": "user",
      "content": "How far away is the moon from the Earth?"
    },
    {
      "role": "user",
      "content": "What is the capital of India?"
    }
  ]
}
```

### 6. Run the Application

Run the Python script to interact with the Azure OpenAI API:

```bash
python app.py
```
The script will process each prompt from `prompts.json` and print the responses from the GPT model.

```bash
Response for prompt: How far away is the moon from the Earth?
The average distance from the Earth to the Moon is about 384,400 kilometers, or roughly 238,855 miles. This distance can vary slightly due to the Moon's elliptical orbit around the Earth. At its closest approach, known as perigee, the Moon can be about 363,300 kilometers (225,623 miles) away, and at its farthest point, known as apogee, it can be about 405,500 kilometers (251,966 miles) away.
==================================================
Response for prompt: What is the capital of India?
The capital of India is New Delhi.
==================================================
```
Run below code for latency results for prompts:
```bash
python latency.py
```
```bash
Response for prompt: How far away is the moon from the Earth?
The average distance from the Earth to the Moon is about 384,400 kilometers, or roughly 238,855 miles. This distance can vary slightly due to the Moon's elliptical orbit around the Earth, ranging from about 363,300 km (225,700 miles) at its closest (perigee) to 405,500 km (251,900 miles) at its farthest (apogee).
Latency: 8.0342 seconds
==================================================
Response for prompt: What is the capital of India?
The capital of India is New Delhi.
Latency: 0.5042 seconds
==================================================
```
---


# Optional:
Steps to save the project to Git
## Git Version Control

If you'd like to track changes and push the project to GitHub, follow these steps:

### 1. Initialize Git

```bash
git init
```

### 2. Configure Git User Details

Set your Git username and email:

```bash
git config user.email "<your-email>"
git config user.name "<your-username>"
```

### 3. Commit Changes

Stage and commit your changes:

```bash
git add .
git commit -m "Initial commit with project files"
```

### 4. Push to GitHub

Add your remote GitHub repository and push the project:

```bash
git remote add origin <your-repository-url>
git push -u origin master
```

---

## Notes

- **API Key**: Be sure to keep your OpenAI API key secure and do not commit your `.env` file to version control. Consider adding `.env` to your `.gitignore` file.
  
- **Model Selection**: The project uses `gpt-4o` as the deployment name. You can change this to another model if needed.

- **Error Handling**: If there are issues interacting with the API, the app will print the error messages to the terminal.



### Thank you :)
