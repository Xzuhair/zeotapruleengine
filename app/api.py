from flask import Flask, request, jsonify, render_template
from app.database import get_db_connection
from app.evaluate_rules import evaluate_rules  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.form.get('rule_string')
    if not rule_string:
        return jsonify({"error": "No rule string provided"}), 400

    # Check if the rule already exists
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM rules WHERE rule_string = ?', (rule_string,))
    existing_rule = cursor.fetchone()

    if existing_rule:
        return jsonify({"error": "Rule already exists"}), 409  # Conflict

    # Insert the rule into the database
    cursor.execute('INSERT INTO rules (rule_string) VALUES (?)', (rule_string,))
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({'rule': rule_string}), 201  # Returns the rule that was added

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_route():
    # Get user data from form fields
    age = request.form.get('age')
    income = request.form.get('income')
    department = request.form.get('department')

    # Prepare the user_data dictionary for evaluation
    user_data = {
        'age': int(age),  
        'income': int(income),  
        'department': department
    }

    evaluation_results = evaluate_rules(user_data)

    return jsonify({"results": evaluation_results}), 200


@app.route('/evaluate_user', methods=['GET', 'POST'])
def evaluate_user():
    connection = get_db_connection()
    cursor = connection.cursor()

    if request.method == 'POST':
        # Check if the combine rules button was pressed
        if 'combine' in request.form:
            selected_rules = request.form.getlist('rules')
            if selected_rules:
                combined_rule = ' AND '.join(selected_rules)
                # Insert the combined rule into the database
                cursor.execute('INSERT INTO rules (rule_string) VALUES (?)', (combined_rule,))
                connection.commit()
                message = f"Combined Rule: {combined_rule}"
            else:
                message = "No rules selected for combination."

            # Fetch all available rules to display in the combine section
            cursor.execute('SELECT rule_string FROM rules')
            rules = cursor.fetchall()  
            rules = [rule[0] for rule in rules]  # Convert list of tuples to list of strings

            return render_template('evaluate_user.html', rules=rules, message=message)

        else:
            # Get user data from the form for evaluation
            age = request.form.get('age')
            income = request.form.get('income')
            department = request.form.get('department')

            # Prepare user data for evaluation
            user_data = {
                'age': int(age),
                'income': int(income),
                'department': department
            }

            # Evaluate rules against the user data
            results = evaluate_rules(user_data)

            # Fetch all available rules to display in the combine section
            cursor.execute('SELECT rule_string FROM rules')
            rules = cursor.fetchall() 
            rules = [rule[0] for rule in rules]

            return render_template('evaluate_user.html', results=results, rules=rules)

    # For GET requests, only fetch the rules to display
    cursor.execute('SELECT rule_string FROM rules')
    rules = cursor.fetchall()  
    rules = [rule[0] for rule in rules]  

    cursor.close()
    connection.close()

    return render_template('evaluate_user.html', rules=rules)





@app.route('/combine_rules', methods=['GET', 'POST'])
def combine_rules():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT rule_string FROM rules')
    rules = cursor.fetchall()
    cursor.close()
    connection.close()

    if request.method == 'POST':
        selected_rules = request.form.getlist('rules')  
        
        if not selected_rules:
            return jsonify({"error": "No rules selected for combination"}), 400

        # Combine the selected rules into a single rule string (example: using AND)
        combined_rule = ' AND '.join(selected_rules)

        # Insert the combined rule into the database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO rules (rule_string) VALUES (?)', (combined_rule,))
        connection.commit()
        cursor.close()
        connection.close()

        return render_template('combine_rules.html', rules=rules, combined_rule=combined_rule)

    return render_template('combine_rules.html', rules=rules)



