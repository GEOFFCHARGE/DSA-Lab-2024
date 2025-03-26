"""Lab 02.02 - Student Groups"""
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
        if not self.is_empty():
            self.size -= 1
            return self.data.pop(-1)
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None

def main():
    s = ArrayStack()
    m = int(input())
    n = int(input())
    o = list(input() for _ in range(n))
    while o:
        s.push(o.pop())
    for i in range(m):
        o = list()
        print(f"Group {i + 1}:", end=" ")
        for j, k in enumerate(s.data):
            if j % m == i:
                o.append(k)
        print(*o, sep=", ")
main()
