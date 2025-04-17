from fairlearn.metrics import demographic_parity_difference

# Example fairness evaluation function
def evaluate_fairness(data, predictions, sensitive_feature):
    # Measure disparate impact for the sensitive feature
    parity_difference = demographic_parity_difference(data['sensitive_feature'], data['predictions'])
    print(f"Demographic Parity Difference: {parity_difference}")

# Mock example
data = {
    'sensitive_feature': [0, 1, 1, 0],
    'predictions': [1, 0, 1, 1]
}
evaluate_fairness(data, data['predictions'], 'sensitive_feature')
