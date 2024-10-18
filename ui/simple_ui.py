from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Rule Engine</title>
    </head>
    <body>
        <h1>Welcome to the Rule Engine</h1>
        <form action="/create_rule" method="POST">
            <label for="rule">Enter your rule:</label>
            <input type="text" id="rule" name="rule_string" required>
            <button type="submit">Create Rule</button>
        </form>
        
        <h2>Evaluate User Data Against Rules</h2>
        <form action="/evaluate_rule" method="POST" id="evaluateForm">
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" required>
            <br>
            <label for="income">Income:</label>
            <input type="number" id="income" name="income" required>
            <br>
            <label for="department">Department:</label>
            <input type="text" id="department" name="department" required>
            <br>
            <button type="submit">Evaluate Rule</button>
        </form>

        <script>
            document.getElementById('evaluateForm').onsubmit = function(event) {
                event.preventDefault(); // Prevent the form from submitting normally
                
                const age = document.getElementById('age').value;
                const income = document.getElementById('income').value;
                const department = document.getElementById('department').value;

                const userData = {
                    age: parseInt(age),
                    income: parseInt(income),
                    department: department
                };

                fetch('/evaluate_rule', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(userData)
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data); // Log the response data
                    alert('Rules evaluated successfully! Check the console for details.');
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error evaluating rules');
                });
            };
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
