class Solution:
    def parseBoolExpr(self, expression):
        index = [0] 
        return self._evaluate(expression, index)
    def _evaluate(self, expr, index):
        curr_char = expr[index[0]]
        index[0] += 1
        if curr_char == "t":
            return True
        if curr_char == "f":
            return False
        if curr_char == "!":
            index[0] += 1  
            result = not self._evaluate(expr, index)
            index[0] += 1
            return result
        values = []
        index[0] += 1
        while expr[index[0]] != ")":
            if expr[index[0]] != ",":
                values.append(self._evaluate(expr, index))
            else:
                index[0] += 1  
        index[0] += 1 
        if curr_char == "&":
            return all(values)
        if curr_char == "|":
            return any(values)
        return False 