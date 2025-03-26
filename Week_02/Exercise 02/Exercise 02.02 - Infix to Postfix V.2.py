"""Exercise 02.02 - Infix to Postfix V.2"""
class ArrayStack:

    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.size += 1
            self.data.append(input_data)

    def pop(self):
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            self.size -= 1
            return self.data.pop()

    def is_empty(self):
        return self.size == 0

    def get_stack_top(self):
        if self.is_empty():
            print("Underflow: Cannot get stack top from an empty list")
            return None
        else:
            x = self.data.pop()
            self.data.append(x)
            return x

    def infixToPostfix(self, expression):
        stack = ArrayStack()
        postf = list()
        for i in expression:
            if i.isalpha():
                postf.append(i)
            elif i in "+-*/":
                while not stack.is_empty() and ((stack.get_stack_top() in "*/" and i in "*/") or (stack.get_stack_top() in "*/" and i in "+-") or (stack.get_stack_top() in "+-" and i in "+-")):
                    postf.append(stack.pop())
                stack.push(i)
            elif i == "(":
                stack.push(i)
            elif i == ")":
                while stack.get_stack_top() != "(":
                    postf.append(stack.pop())
                stack.pop()
        while not stack.is_empty():
            postf.append(stack.pop())
        return "".join(postf)

def main():
    print(ArrayStack().infixToPostfix(input()))
main()
