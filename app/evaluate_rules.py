import sqlite3

def get_db_connection():
    conn = sqlite3.connect('rules.db')
    conn.row_factory = sqlite3.Row
    return conn

def evaluate_rules(sample_data):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT rule_string FROM rules')
    rules = cursor.fetchall()

    results = []  # Collect rule evaluation results

    for rule in rules:
        rule_string = rule['rule_string']

        # Replace the placeholders in the rule_string with actual sample_data
        for key, value in sample_data.items():
            if isinstance(value, str):
                rule_string = rule_string.replace(key, f'"{value}"')  # Wrap strings in quotes
            else:
                rule_string = rule_string.replace(key, str(value))  # Convert numbers to string

        # Replace Python's logical operators for evaluation
        rule_string = rule_string.replace('AND', 'and').replace('OR', 'or')

        # Correct single equals to double equals for string comparisons
        rule_string = rule_string.replace('=', '==')

        # Evaluate the rule
        try:
            if eval(rule_string):  # Evaluate the condition
                results.append(f"Rule passed: {rule_string}")
            else:
                results.append(f"Rule failed: {rule_string}")
        except Exception as e:
            results.append(f"Error evaluating rule: {rule_string} | {str(e)}")

    cursor.close()
    connection.close()

    return results  # Return the list of results

if __name__ == '__main__':
    # Sample data to evaluate rules against
    sample_data = {
        'age': 30,
        'income': 60000,
        'department': 'HR'
    }
    result = evaluate_rules(sample_data)
    print(result)  # Print results in case of standalone execution
