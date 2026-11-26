"""
Day 2 - AI Student Study Planner
Uses the OpenAI API directly (without LangChain).

Setup:
    pip install openai

Set your API key before running:
    Windows PowerShell:  $env:OPENAI_API_KEY="your_api_key"
    macOS/Linux:         export OPENAI_API_KEY="your_api_key"

Never paste your API key into this file or upload it to GitHub.
"""

import os
from datetime import date
from openai import OpenAI


def get_student_details():
    print("\n===== AI STUDENT STUDY PLANNER =====\n")

    name = input("Enter your name: ").strip()
    subjects = input("Enter your subjects (comma-separated): ").strip()
    difficult_topics = input(
        "Enter topics you find difficult (comma-separated): "
    ).strip()
    exam_date = input("Enter your exam date (YYYY-MM-DD): ").strip()
    study_hours = input("How many hours can you study per day? ").strip()

    return name, subjects, difficult_topics, exam_date, study_hours


def generate_study_plan(name, subjects, difficult_topics, exam_date, study_hours):
    # The OpenAI client reads OPENAI_API_KEY from the environment.
    client = OpenAI()

    prompt = f"""
You are an encouraging and practical AI study-planning assistant.

Create a realistic study plan using the student's details below.

Student name: {name}
Subjects: {subjects}
Difficult topics: {difficult_topics}
Exam date: {exam_date}
Available study time per day: {study_hours} hours
Today's date: {date.today()}

Your response must include:
1. A short overview of the preparation strategy.
2. A day-wise timetable until the exam date.
3. Extra attention to the difficult topics.
4. Short breaks and revision sessions.
5. A final revision checklist.

Keep the plan achievable. If the exam date is invalid or has already passed,
politely point that out and ask the student to correct it. Do not invent
the student's syllabus or claim to know the exam question paper.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


def main():
    try:
        if not os.getenv("OPENAI_API_KEY"):
            print("ERROR: OPENAI_API_KEY was not found.")
            print("Set your OpenAI API key as an environment variable and try again.")
            return

        details = get_student_details()
        plan = generate_study_plan(*details)

        print("\n===== YOUR PERSONALIZED STUDY PLAN =====\n")
        print(plan)

        with open("study_plan.txt", "w", encoding="utf-8") as file:
            file.write(plan)

        print("\nYour study plan was also saved to study_plan.txt.")

    except ValueError:
        print("Please enter valid details and try again.")
    except Exception as error:
        print(f"Something went wrong: {error}")
        print("Check your API key, internet connection, and OpenAI API access.")


if __name__ == "__main__":
    main()
