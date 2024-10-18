import sqlite3

def get_db_connection():
    conn = sqlite3.connect('rules.db')  
    conn.row_factory = sqlite3.Row  # Enables access by column name
    return conn

def fetch_rules():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Fetch all rules from the rules table
    cursor.execute('SELECT * FROM rules')
    rules = cursor.fetchall()

    # Print each rule
    for rule in rules:
        print(f"ID: {rule['id']}, Rule: {rule['rule_string']}")

    cursor.close()
    connection.close()
    return rules  # Make sure to return the rules

def create_rule(rule_string):
    # Logic to create a rule from the rule string and return its AST
    # Example logic; adjust according to your implementation
    ast = {
        'type': 'AND',  
        'left': {
            'type': 'LESS_THAN',
            'left': 'income',
            'right': 50000
        },
        'right': {
            'type': 'GREATER_THAN',
            'left': 'age',
            'right': 25
        }
    }
    return ast

def combine_rules(rule1, rule2):
    # Logic to combine two rules
    return {
        'type': 'AND',
        'left': rule1,
        'right': rule2
    }

def evaluate_rules(data):
    rules = fetch_rules()  
    results = []
    for rule in rules:
        # Example evaluation logic
        # Replace this with your actual evaluation logic
        if rule['rule_string'] == "income < 50000 AND age > 25":
            if data['income'] < 50000 and data['age'] > 25:
                results.append("Rule passed")
        elif rule['rule_string'] == "department = 'HR' AND age < 40":
            if data['department'] == 'HR' and data['age'] < 40:
                results.append("Rule passed")
        # Add more rule checks based on your actual rules
    return results

if __name__ == '__main__':
    fetch_rules()
