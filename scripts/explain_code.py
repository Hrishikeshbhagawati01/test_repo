import ast

def explain_code(file_path):
    with open(file_path, "r") as f:
        code = f.read()
    tree = ast.parse(code)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            print(f"Function '{node.name}' - {ast.dump(node)}")
        elif isinstance(node, ast.Assign):
            print(f"Variable Assignment - {ast.dump(node)}")



# Run the explanation on the target file
explain_code("privacy_python.py")
