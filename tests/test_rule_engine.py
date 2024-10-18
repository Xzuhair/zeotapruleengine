import unittest
from app.check_rules import create_rule, combine_rules, evaluate_rules

class TestRuleEngine(unittest.TestCase):

    def test_create_rule(self):
        # Test case: Create an individual rule and check AST representation
        rule = create_rule("income < 50000 AND age > 25")
        expected_ast = {
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
        self.assertEqual(rule, expected_ast)

    def test_combine_rules(self):
        # Test case: Combine rules and ensure the resulting AST is correct
        rule1 = create_rule("income < 50000 AND age > 25")
        rule2 = create_rule("department = 'HR'")
        combined_rule = combine_rules(rule1, rule2)
        expected_combined_ast = {
            'type': 'AND',
            'left': rule1,
            'right': rule2
        }
        self.assertEqual(combined_rule, expected_combined_ast)

    def test_evaluate_rules(self):
        # Test case: Evaluate rules with sample data
        sample_data = {
            'age': 30,
            'income': 60000,
            'department': 'HR'
        }
        # This assumes that evaluate_rules checks against these sample_data correctly.
        result = evaluate_rules(sample_data)
        self.assertIn("Rule passed", result)  

    def test_edge_cases(self):
        # Test case: Explore combining additional rules and test functionality
        rule1 = create_rule("age > 30")
        rule2 = create_rule("income < 40000")
        combined_rule = combine_rules(rule1, rule2)
        # Update sample data to include the 'department' key
        sample_data = {
            'age': 31,
            'income': 35000,
            'department': 'HR'  
        }
        result = evaluate_rules(sample_data)
        self.assertIn("Rule passed", result)  

if __name__ == "__main__":
    unittest.main()
