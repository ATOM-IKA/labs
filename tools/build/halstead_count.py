"""Подсчёт характеристик программы по методике Холстеда для функции или метода Python.

Правила подсчёта (по примеру из методических указаний):
  оператор  - служебное слово, знак операции, вызов функции, присваивание, любой
              управляющий оператор; каждое вхождение учитывается;
  операнд   - переменная или константа, используемая в теле; параметры в заголовке
              не считаются, строка документации и комментарии не учитываются.
"""
import ast
import math
from collections import Counter

OPERATOR_NAMES = {
    ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/", ast.FloorDiv: "//", ast.Mod: "%", ast.Pow: "**",
    ast.Eq: "==", ast.NotEq: "!=", ast.Lt: "<", ast.LtE: "<=", ast.Gt: ">", ast.GtE: ">=",
    ast.And: "and", ast.Or: "or", ast.Not: "not", ast.USub: "-(унарный)", ast.In: "in", ast.Is: "is",
}


class Counter2(ast.NodeVisitor):
    def __init__(self):
        self.operators = Counter()
        self.operands = Counter()

    def visit_FunctionDef(self, node):
        self.operators["def"] += 1
        for child in node.body[1:] if self._has_docstring(node) else node.body:
            self.visit(child)

    @staticmethod
    def _has_docstring(node):
        return bool(node.body) and isinstance(node.body[0], ast.Expr) and isinstance(getattr(node.body[0], "value", None), ast.Constant) \
            and isinstance(node.body[0].value.value, str)

    def visit_If(self, node):
        self.operators["if"] += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.operators["for"] += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.operators["while"] += 1
        self.generic_visit(node)

    def visit_Return(self, node):
        self.operators["return"] += 1
        self.generic_visit(node)

    def visit_Assign(self, node):
        self.operators["="] += 1
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        self.operators[OPERATOR_NAMES[type(node.op)] + "="] += 1
        self.generic_visit(node)

    def visit_BinOp(self, node):
        self.operators[OPERATOR_NAMES[type(node.op)]] += 1
        self.generic_visit(node)

    def visit_UnaryOp(self, node):
        self.operators[OPERATOR_NAMES[type(node.op)]] += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.operators[OPERATOR_NAMES[type(node.op)]] += len(node.values) - 1
        self.generic_visit(node)

    def visit_Compare(self, node):
        for op in node.ops:
            self.operators[OPERATOR_NAMES[type(op)]] += 1
        self.generic_visit(node)

    def visit_Subscript(self, node):
        self.operators["[]"] += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        name = node.func.id if isinstance(node.func, ast.Name) else ast.unparse(node.func)
        self.operators[name + "()"] += 1
        for arg in node.args:
            self.visit(arg)

    def visit_Name(self, node):
        self.operands[node.id] += 1

    def visit_Constant(self, node):
        self.operands[repr(node.value)] += 1


def count(source, function_name, class_name=None):
    tree = ast.parse(source)
    scope = tree
    if class_name:
        scope = next(node for node in ast.walk(tree) if isinstance(node, ast.ClassDef) and node.name == class_name)
    target = next(node for node in ast.walk(scope) if isinstance(node, ast.FunctionDef) and node.name == function_name)
    counter = Counter2()
    counter.visit(target)
    return counter.operators, counter.operands


def metrics(n1, n2, N1, N2, n2_star):
    """Метрики Холстеда по формулам 1-11 из методических указаний."""
    lg = math.log2
    r = {}
    r["n"] = n1 + n2
    r["N"] = N1 + N2
    r["N_calc"] = n1 * lg(n1) + n2 * lg(n2)                                 # 1. длина программы
    r["V"] = r["N"] * lg(r["n"])                                            # 2. объём
    r["V_pot"] = (2 + n2_star) * lg(2 + n2_star)                            # 3. потенциальный объём
    r["V_lim"] = (2 + n2_star * lg(n2_star)) * lg(2 + n2_star)              # 4. граничный объём
    r["A"] = n2_star / (n2_star + 2) * lg(n2_star / 2)                      # 5. коэффициенты
    r["B"] = n2_star - 2 * r["A"]
    r["n2_pred"] = r["A"] * n1 + r["B"]
    r["L"] = r["V_pot"] / r["V"]                                            # 6. уровень программы
    r["L_alt"] = 2 * n2 / (n1 * N2)                                         # 6. альтернативное определение, n1* = 2
    r["I"] = r["L_alt"] * r["V"]                                            # 7. интеллектуальное содержание
    r["E"] = r["V"] / r["L"]                                                # 8. работа по программированию
    r["T"] = r["E"] / 18                                                    # 9. время программирования, S = 18
    r["lambda"] = r["L"] * r["L"] * r["V"]                                  # 10. уровень языка
    r["E0"] = r["V_pot"] ** 3 / (r["lambda"] ** 2)                          # 11. ошибки
    r["Err"] = r["V"] / r["E0"]
    return r


if __name__ == "__main__":
    import sys
    path, name = sys.argv[1], sys.argv[2]
    ops, opd = count(open(path, encoding="utf8").read(), name, sys.argv[3] if len(sys.argv) > 3 else None)
    print(dict(ops), dict(opd))
