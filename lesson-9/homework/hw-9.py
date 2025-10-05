#Lesson-9\
#Homework

#Object-Oriented Programming (OOP) Exercises



#1. Circle Class
#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Example usage
circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())




#2. Person Class
#Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1
        return age

# Example usage
person = Person("Tolibjon", "UZB", "2010-05-20")
print("Name:", person.name)
print("Country:", person.country)
print("Age:", person.age())






#3. Calculator Class
#Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero error"

# Example usage
calc = Calculator()
print("Addition:", calc.add(5, 3))
print("Subtraction:", calc.subtract(5, 3))
print("Multiplication:", calc.multiply(5, 3))
print("Division:", calc.divide(5, 3))





#4. Shape and Subclasses
#Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        # Assuming it's an equilateral triangle for simplicity
        return 3 * self.base

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

# Example usage
shapes = [
    Circle(5),
    Triangle(4, 6),
    Square(3)
]

for shape in shapes:
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())




#5. Binary Search Tree Class
#Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return node

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

# Example usage
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)

# Search for elements
print("Search for 3:", bst.search(3) is not None)
print("Search for 6:", bst.search(6) is not None)





#6. Stack Data Structure
#Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

# Example usage
stack = Stack()
stack.push(5)
stack.push(10)
print("Top element:", stack.peek())
print("Pop element:", stack.pop())
print("Is stack empty?", stack.is_empty())




#7. Linked List Data Structure
#Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        current = self.head
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
            current = None

# Example usage
ll = LinkedList()
ll.insert(5)
ll.insert(10)
ll.insert(15)
ll.display()
ll.delete(10)
ll.display()




#8. Shopping Cart Class
#Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append((item, price))

    def remove_item(self, item):
        self.items = [i for i in self.items if i[0] != item]

    def calculate_total(self):
        return sum(price for item, price in self.items)

# Example usage
cart = ShoppingCart()
cart.add_item("Apple", 1.0)
cart.add_item("Banana", 0.5)
print("Total price:", cart.calculate_total())
cart.remove_item("Apple")
print("Total price after removing Apple:", cart.calculate_total())




#9. Stack with Display
#Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def display(self):
        if not self.is_empty():
            print("Stack elements:", end=" ")
            for item in reversed(self.items):
                print(item, end=" ")
            print()
        else:
            print("Stack is empty")

# Example usage
stack = Stack()
stack.push(5)
stack.push(10)
stack.display()
print("Pop element:", stack.pop())
stack.display()




#10. Queue Data Structure
#Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"

    def display(self):
        if not self.is_empty():
            print("Queue elements:", end=" ")
            for item in self.items:
                print(item, end=" ")
            print()
        else:
            print("Queue is empty")

# Example usage
queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
queue.display()
print("Dequeue element:", queue.dequeue())
queue.display()




#11. Bank Class
#Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, customer_name, initial_balance=0):
        if customer_name not in self.customers:
            self.customers[customer_name] = initial_balance
            return "Account created successfully"
        return "Account already exists"

    def deposit(self, customer_name, amount):
        if customer_name in self.customers:
            self.customers[customer_name] += amount
            return "Deposit successful"
        return "Account not found"

    def withdraw(self, customer_name, amount):
        if customer_name in self.customers:
            if self.customers[customer_name] >= amount:
                self.customers[customer_name] -= amount
                return "Withdrawal successful"
            return "Insufficient funds"
        return "Account not found"

    def get_balance(self, customer_name):
        if customer_name in self.customers:
            return self.customers[customer_name]
        return "Account not found"

# Example usage
bank = Bank()
print(bank.create_account("Alice", 100))
print(bank.deposit("Alice", 50))
print("Alice's balance:", bank.get_balance("Alice"))
print(bank.withdraw("Alice", 30))
print("Alice's balance:", bank.get_balance("Alice"))




