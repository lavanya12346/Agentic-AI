# Day 2 - AI Student Study Planner

## Project Description
The AI Student Study Planner is a beginner-friendly Python application that uses the **OpenAI API directly, without LangChain**, to create a personalized exam preparation timetable.

The student enters their subjects, difficult topics, exam date, and available study hours. The application sends these details to an OpenAI model and displays a practical study plan.

## Objectives
- Learn how to connect a Python program to the OpenAI API.
- Send a prompt to an OpenAI model and receive a response.
- Collect user input and use it to generate a personalized result.
- Practice handling API configuration and errors safely.

## Technologies Used
- Python
- OpenAI Python SDK
- OpenAI API
- Google Colab or a local Python environment

## Features
1. Accepts the student's name and subjects.
2. Collects difficult topics, exam date, and daily study hours.
3. Generates a day-wise study timetable.
4. Includes revision sessions and breaks.
5. Saves the generated plan in `study_plan.txt`.

## Installation
Install the OpenAI Python package:

```bash
pip install openai
```

## API Key Setup
Create an API key from the OpenAI Platform.

Set it as an environment variable named `OPENAI_API_KEY`.

**Windows PowerShell:**
```powershell
$env:OPENAI_API_KEY="your_api_key"
```

**macOS/Linux:**
```bash
export OPENAI_API_KEY="your_api_key"
```

For Google Colab, store the key in Colab Secrets as `OPENAI_API_KEY`, then load it securely:

```python
from google.colab import userdata
import os

os.environ["OPENAI_API_KEY"] = userdata.get("OPENAI_API_KEY")
```

Never write the real API key in `task.py`, `README.md`, notebook outputs, or a public GitHub repository.

## How to Run
Run:

```bash
python task.py
```

Enter the requested details when prompted. The generated study plan will be displayed and saved to `study_plan.txt`.

## How It Works
1. The program collects student details using Python `input()`.
2. The OpenAI client reads the API key from the environment.
3. The program sends a prompt and the student details to the OpenAI API.
4. The model generates a personalized study plan.
5. The program prints the result and saves it to a text file.

## Learning Outcome
This task demonstrates how to use the OpenAI API directly from Python without using LangChain.
