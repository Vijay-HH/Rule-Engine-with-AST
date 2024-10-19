class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left  # Left child (for operators)
        self.right = right  # Right child (for operators)
        self.value = value  # Value for operand nodes (e.g., number, string, etc.)

    def __repr__(self):
        if self.type == "operand":
            return f"Operand({self.value})"
        else:
            return f"Operator({self.type}, left={self.left}, right={self.right})"


def create_rule(rule_string):
    import ast

    # Parsing the rule string into AST (assuming simple comparisons and boolean logic)
    def parse_expression(expr):
        try:
            tree = ast.parse(expr, mode='eval')
        except SyntaxError:
            raise ValueError(f"Invalid rule expression: {expr}")

        # Recursively construct AST Nodes from the parsed Python AST
        if isinstance(tree.body, ast.BoolOp):
            op_type = 'AND' if isinstance(tree.body.op, ast.And) else 'OR'
            left_expr = tree.body.values[0]
            right_expr = tree.body.values[1]
            left_node = parse_expression(ast.dump(left_expr))
            right_node = parse_expression(ast.dump(right_expr))
            return Node(op_type, left_node, right_node)

        elif isinstance(tree.body, ast.Compare):
            left = tree.body.left
            op = tree.body.ops[0]
            right = tree.body.comparators[0]

            operator = type(op).__name__  # "Gt" for >, "Lt" for <, etc.
            left_node = Node("operand", value=left.id if isinstance(left, ast.Name) else left.n)
            right_node = Node("operand", value=right.n if isinstance(right, ast.Num) else right.id)
            return Node(operator, left_node, right_node)

    # Construct the AST for the entire rule string
    return parse_expression(rule_string)


def combine_rules(rules):
    # Combine multiple ASTs using "AND" as the default combination method
    combined_rule = None
    for rule_string in rules:
        rule_ast = create_rule(rule_string)
        if combined_rule:
            combined_rule = Node("AND", combined_rule, rule_ast)
        else:
            combined_rule = rule_ast
    return combined_rule


def evaluate_rule(ast_node, data):
    # Evaluate the rule AST against the given data
    if ast_node.type == "operand":
        return data[ast_node.value]

    elif ast_node.type == "AND":
        return evaluate_rule(ast_node.left, data) and evaluate_rule(ast_node.right, data)

    elif ast_node.type == "OR":
        return evaluate_rule(ast_node.left, data) or evaluate_rule(ast_node.right, data)

    elif ast_node.type == "Gt":  # Greater than
        return data[ast_node.left.value] > ast_node.right.value

    elif ast_node.type == "Lt":  # Less than
        return data[ast_node.left.value] < ast_node.right.value

    elif ast_node.type == "Eq":  # Equality comparison
        return data[ast_node.left.value] == ast_node.right.value

    else:
        raise ValueError(f"Unknown operation: {ast_node.type}")
