# Rule Engine Application

## Purpose
The Rule Engine Application allows users to create, combine, and evaluate rules based on user attributes such as age, income, and department. It is designed for use cases like customer segmentation, risk assessment, fraud detection, and workflow automation.

## Key Features
- **Simple UI:** User-friendly interface for creating and evaluating rules.
- **Rule Combination:** Combine multiple rules into a single rule for complex evaluations.
- **API Integration:** Provides REST API endpoints for programmatic access to the rule engine.
- **Dynamic Rule Evaluation:** Evaluate user attributes against dynamically created rules to determine eligibility.
- **Extensible:** Designed with flexibility to allow future enhancements.
- **Unit Testing:** Comprehensive unit tests implemented to verify rule creation, combination, and evaluation logic.

## Project Structure

<project-folder(zeotap)>/
│
├── app/
│   ├── __init__.py            # Initializes the Flask app
│   ├── api.py                 # Handles API routes for rule management
│   ├── check_rules.py         # Logic for checking and evaluating rules
│   ├── database.py            # Database connection and queries
│   ├── evaluate_rules.py      # Script to evaluate rules against user data
│   ├── view_rules.py          # Handles the display of existing rules
│
├── database/
│   ├── schema.sql             # SQL schema for setting up the SQLite database
│
├── templates/
│   ├── index.html             # Main landing page for the app
│   ├── evaluate_user.html     # Page to evaluate user rules
│   ├── combine_rules.html     # Page to combine multiple rules
│
├── ui/
│   ├── simple_ui.py           # Simple interface for interacting with the rule engine
│
├── tests/
│   ├── test_rule_engine.py     # Unit tests for the rule engine logic
│
├── run.py                     # Main entry point to run the Flask app
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation

## Note
Delete rules.db if u want to create your own rules and delete old rules

## Requirements
- Python 3.x
- SQLite (for local database)
- Flask (for web framework)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <my-repo-url>
   cd <my-repo-folder>

2. Create a Virtual Environment:
python -m venv zeoapp
source zeoapp/bin/activate   # On Windows use: zeoapp\Scripts\activate

3. Install Dependencies:
pip install -r requirements.txt

4. Set Up the Database:
Ensure the schema.sql file is properly placed in the database/ folder.
Run the schema to create the necessary tables:
sqlite3 app.db < database/schema.sql

5. Run the Application:
python run.py

6. Access the Application:
Open your browser and go to http://127.0.0.1:5000 to interact with the UI.

------------------------------------------------------------------------------

## API Endpoints
1. Evaluate Rules
URL: /api/evaluate
Method: POST
Description: Submit user data to evaluate against the rules.
Example request body:
{
  "age": 30,
  "income": 60000,
  "department": "Sales"
}

2. Combine Rules
URL: /api/combine
Method: POST
Description: Combine multiple rules to create complex evaluations.


## Usage Example
Here’s how you can evaluate a rule:
curl -X POST http://127.0.0.1:5000/api/evaluate \
-H "Content-Type: application/json" \
-d '{"age": 30, "income": 60000, "department": "Sales"}'
This will return whether the user satisfies the rules you've created.


## Future Enhancements
1. **Expand Unit Testing:** Currently, unit tests are implemented in `tests/test_rule_engine.py`. Future enhancements could include additional test cases to cover more edge cases and different rule combinations, ensuring comprehensive validation of the rule engine's logic.
2. **User Authentication and Permissions:** Implement user authentication and access control to manage permissions for rule creation and evaluation.
3. **Complex Rule Combinations:** Support for more complex rule combinations and nested rules for advanced use cases, allowing for greater flexibility in rule evaluation.
4. **Performance Optimization:** Optimize rule evaluation performance, especially for large datasets, to enhance user experience and scalability.
5. **Detailed Logging and Error Handling:** Introduce comprehensive logging and error handling mechanisms to improve debugging and track rule evaluation processes.
