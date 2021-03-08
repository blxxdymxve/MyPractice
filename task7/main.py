class Stack():
    def __init__(self, data):
        self.data = data

    def push(self, x):
        return (self.data.append(x))

    def pop(self):
        return (self.data.pop())

    def peak(self):
        return (self.data[-1])

    def contains(self, x):
        return (self.data.count(x))

    def show_all(self):
        return (self.data)

    def length(self):
        return len(self.data)


if __name__ == "__main__":
    stack = Stack([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("Исходный стек: ", stack.show_all())
    even = Stack([])
    odd = Stack([])

    while (stack.length() > 0):
        value = stack.pop()
        even.push(value) if value % 2 == 0 else odd.push(value)

    print("Чётный: ", even.show_all())
    print("Нечётный: ", odd.show_all())