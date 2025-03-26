"""Exercise 02.03 - SPÄM"""
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

    def spam(self, operator):
        stack = ArrayStack()
        pairs = {"]" : "[", "}" : "{", ")" : "("}
        state = True
        for i in operator:
            if i in "[{(":
                stack.push(i)
            elif i in "]})":
                if stack.is_empty() or pairs[i] not in stack.data:
                    print("Underflow: Cannot pop data from an empty list")
                    state = False
                elif stack.get_stack_top() == pairs[i]:
                    stack.pop()
        if state and stack.is_empty():
            return True
        else:
            return False

def main():
    print(ArrayStack().spam(input()))
main()
