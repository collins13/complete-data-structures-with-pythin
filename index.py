class Stack:
    def __init__(self):
        self.items = [];
    def is_empty(self):
        return self.items == [];
    def push(self, item):
        self.items.append(item);
    def peek(self):
        return self.items[len(self.items) - 1];
    def size(self):
        return len(self.items);
    def pop(self):
        return self.items.pop();

    def reverse(self, mystr):
        mystack = [];
        for i in mystr:
            mystack.append(i);
        revstr = '';
        print(mystack)
        print(len(mystack))
        while len(mystack):
            revstr = revstr + mystack.pop();
        return revstr;


def divide_by_2(dec_number):
        rem_stack = Stack()

        while dec_number > 0:
            rem = dec_number % 2
            rem_stack.push(rem)
            dec_number = dec_number // 2

        bin_string = ""
        while not rem_stack.is_empty():
            bin_string = bin_string + str(rem_stack.pop())

        return bin_string

print(divide_by_2(42))
print(21 // 2)

