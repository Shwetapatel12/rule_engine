from flask import Flask, render_template, request, jsonify
from rules import create_rule, combine_rules, evaluate_rule

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/create_rule', methods=['POST'])
def create_rule_api():
    data = request.get_json()
    rule_string = data['rule_string']
    ast = create_rule(rule_string)
    return jsonify(ast)

@app.route('/api/combine_rules', methods=['POST'])
def combine_rules_api():
    data = request.get_json()
    rules = data['rules']
    combined_ast = combine_rules(rules)
    return jsonify(combined_ast)

@app.route('/api/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    data = request.get_json()

    # Check if 'attributes' is in the data
    if 'attributes' not in data:
        return jsonify({"error": "Missing 'attributes' key in request"}), 400
    
    attributes = data['attributes']
    result = evaluate_rule(attributes)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
