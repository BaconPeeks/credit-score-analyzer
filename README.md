# credit-score-analyzer

A simple Python script that classifies a given credit score into categories based on standard FICO score ranges. The program also logs each user input along with the classification and a timestamp.

---

## Features

- Accepts user input for a credit score.
- Validates input to ensure it is a numeric value.
- Classifies credit scores into one of five categories:
  - Poor (300–579)
  - Fair (580–669)
  - Good (670–739)
  - Very Good (740–799)
  - Excellent (800–850)
- Logs each classification with the score, category, and timestamp to a file (`log.txt`).

---

## Usage

1. Run the script:

   ```bash
   python credit_classifier.py
   ```
2. When prompted, enter your credit score as an integer between 300 and 850.

3. The script will print the credit score category and save the result with a timestamp in log.txt.

---

## Example

```text
Credit score:
720
Your credit is 720, in the category Good
```
---
## Requirements

1. Python 3.10 or higher (due to the use of match statement).

---

## Code Overview

1. check_credit(score: int) -> str
Classifies the credit score into a category using Python's structural pattern matching.

2. main()
Handles user input, calls the classification function, prints the result, and logs the interaction.

