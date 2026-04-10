# llm-evaluator
# Acne-Safe Makeup Checker

A Python tool that analyzes cosmetic product ingredients and flags acne-triggering (comedogenic) ingredients.

## Features
- Detects comedogenic ingredients
- Assigns acne risk scores
- Allows product search by name
- Uses real-world Sephora product data

## Tech Stack
- Python
- JSON

## How It Works
The program scans ingredient lists from foundations and compares them against a predefined list of pore-clogging ingredients. It then flags matches and calculates a simple risk score.

## Example
Product: Kosas Revealer Foundation  
Flagged Ingredients: coconut oil  
Acne Risk Score: 1

## Future Improvements
- Integrate Sephora API or web scraping
- Expand ingredient database
- Build a web interface
