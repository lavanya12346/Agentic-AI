
# Day 3 – AI Business Prompt Testing and Evaluation

## Objective
To develop and test an AI-powered customer support system for StyleHub Fashion Store using Groq API.

## Tools and Technologies
- Python
- Google Colab
- Groq API
- Pandas
- GPT-OSS-120B

## Tasks Completed

### Task 1: Business System Prompt
Created a SYSTEM prompt for StyleHub Fashion Store to handle customer questions.

### Task 2: Customer Testing
- Prepared 10 customer questions in tests.csv.
- Added must_include criteria for each question.
- Tested the original SYSTEM prompt.
- Calculated the original pass rate.

### Task 3: Prompt Improvement
- Added extra instructions to improve answer accuracy.
- Tested the improved SYSTEM prompt.
- Compared original and improved pass rates.

### Task 4: Temperature Testing
Changed temperature to 1.0 and executed the same 10 tests twice.

Results:
- Run 1 Pass Rate: 80%
- Run 2 Pass Rate: 80%

Observation: Both runs achieved the same pass rate.

### Task 5: Agent or Not?

| Business Job | Category |
|---|---|
| Calculate shopping bill | Plain Code |
| Answer customer questions | One LLM Call |
| Check stock and suggest alternatives | Agent |

### Before Day 4: Python Functions

Created two Python functions:

1. get_product_price() – Retrieves product prices.
2. check_availability() – Checks product availability.

Both functions include type hints and docstrings.

## Learning Outcomes
- Learned to create business-specific SYSTEM prompts.
- Learned to evaluate AI responses using test cases.
- Understood prompt improvement.
- Learned the effect of temperature on AI responses.
- Understood Plain Code, One LLM Call and AI Agents.
- Practiced Python functions with type hints and docstrings.

## Conclusion
Successfully completed Day 3 activities by testing and improving an AI-powered customer support system for StyleHub Fashion Store.
