"""Lab 02.04 - Parentheses Matching"""
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

    def get_size(self):
        return self.size

    def print_stack(self):
        print(self.data)

    def copy_stack(stack1, stack2):
        stackx = ArrayStack()
        while not stack2.is_empty():
            stack2.pop()
        while not stack1.is_empty():
            stackx.push(stack1.pop())
        while not stackx.is_empty():
            temps = stackx.pop()
            stack1.push(temps)
            stack2.push(temps)

    def is_parentheses_matching(input_data):
        stack = ArrayStack()
        state = True
        for i in input_data:
            if i == "(":
                stack.push(i)
            elif i == ")":
                if stack.is_empty():
                    state = False
                stack.pop()
        if state and stack.is_empty():
            print(f"Parentheses in {input_data} are matched")
            return True
        else:
            print(f"Parentheses in {input_data} are unmatched")
            return False

def main():
    print(ArrayStack.is_parentheses_matching(input()))
main()
