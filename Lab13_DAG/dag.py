# DAG Construction for Common Subexpression Elimination

class DAGNode:
    def __init__(self, operator=None, left=None, right=None, value=None):
        self.operator = operator
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        if self.operator:
            return f"({self.left} {self.operator} {self.right})"
        return str(self.value)


dag_nodes = {}


def get_node(operator=None, left=None, right=None, value=None):
    key = (operator, left, right, value)

    if key not in dag_nodes:
        dag_nodes[key] = DAGNode(operator, left, right, value)

    return dag_nodes[key]


def build_dag(expressions):
    results = {}

    for expr in expressions:
        lhs, rhs = expr.split("=")
        rhs = rhs.strip()

        if "+" in rhs:
            left, right = rhs.split("+")
            node = get_node("+", left.strip(), right.strip())

        elif "*" in rhs:
            left, right = rhs.split("*")
            node = get_node("*", left.strip(), right.strip())

        else:
            node = get_node(value=rhs)

        results[lhs.strip()] = node

    return results


expressions = [
    "a=b+c",
    "d=b+c",
    "e=a*d"
]

dag = build_dag(expressions)

print("DAG Representation:\n")

for var, node in dag.items():
    print(f"{var} -> {node}")

print("\nCommon subexpressions are shared in DAG nodes.")
