"""Lab 01.03 - SwapVar"""
def convert_string_to_tuples(text_in):
    values = text_in.strip("()").split(", ")
    n1 = float(values[0])
    n2 = float(values[1])
    print(f"({n2}, {n1})")

def main():
    convert_string_to_tuples(input())
main()
