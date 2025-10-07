#Homework
#10-lesson


#Homework 1. ToDo List Application

# 1. Define Task Class:
#Create a Task class with attributes such as task title, description, due date, and status.

class Task:
    def __init__(self, title, description, due_date, status='Pending'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f"Task(title={self.title}, description={self.description}, due_date={self.due_date}, status={self.status})"

t1 = Task("Finish homework", "Math exercises", "2025-10-08")
print(t1)





# 2. Define ToDoList Class:
#Create a ToDoList class that manages a list of tasks.
#Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.status = 'Completed'
                return f"Task '{task_title}' marked as completed."
        return f"Task '{task_title}' not found."

    def list_all_tasks(self):
        return self.tasks

    def list_incomplete_tasks(self):
        return [task for task in self.tasks if task.status != 'Completed']
# Example usage:
todo_list = ToDoList()
todo_list.add_task(Task("Finish homework", "Math exercises", "2025-10-08"))
todo_list.add_task(Task("Grocery shopping", "Buy vegetables and fruits", "2025-10-09"))
print(todo_list.list_all_tasks())




# 3. Create Main Program:
#Develop a simple CLI to interact with the ToDoList.
#Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.

def main():
    todo_list = ToDoList()
    while True:
        print("\nToDo List:")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print("Task added.")

        elif choice == '2':
            title = input("Enter task title to mark as complete: ")
            print(todo_list.mark_complete(title))

        elif choice == '3':
            print("All Tasks:")
            for task in todo_list.list_all_tasks():
                print(task)

        elif choice == '4':
            print("Incomplete Tasks:")
            for task in todo_list.list_incomplete_tasks():
                print(task)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





# 4. Test the Application:
#Create instances of tasks and test the functionality of your ToDoList.

def test_todo_list():
    todo_list = ToDoList()
    todo_list.add_task(Task("Finish homework", "Math exercises", "2025-10-08"))
    todo_list.add_task(Task("Grocery shopping", "Buy vegetables and fruits", "2025-10-09"))

    print("All Tasks:")
    for task in todo_list.list_all_tasks():
        print(task)

    print(todo_list.mark_complete("Finish homework"))
    print("Incomplete Tasks:")
    for task in todo_list.list_incomplete_tasks():
        print(task)

if __name__ == "__main__":
    test_todo_list()





# 1. Define Post Class:
#Create a Post class with attributes like title, content, and author.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f"Post(title={self.title}, content={self.content}, author={self.author})"

p1 = Post("My First Post", "This is the content of my first post.", "Alice")
print(p1)





# 2. Define Blog Class:
#Create a Blog class that manages a list of posts.
#Include methods to add a post, list all posts, and display posts by a specific author.

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        return self.posts

    def list_posts_by_author(self, author):
        return [post for post in self.posts if post.author == author]
# Example usage:
blog = Blog()
blog.add_post(Post("My First Post", "This is the content of my first post.", "Alice"))
blog.add_post(Post("Another Post", "More content here.", "Bob"))
print(blog.list_all_posts())
print(blog.list_posts_by_author("Alice"))






# 3. Create Main Program:
#Develop a CLI to interact with the Blog system.
#Include options to add posts, list all posts, and display posts by a specific author.

def main():
    blog = Blog()
    while True:
        print("\nBlog Menu:")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter post author: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added.")

        elif choice == '2':
            print("All Posts:")
            for post in blog.list_all_posts():
                print(post)

        elif choice == '3':
            author = input("Enter author name: ")
            print(f"Posts by {author}:")
            for post in blog.list_posts_by_author(author):
                print(post)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





# 4. Enhance Blog System:
#Add functionality to delete a post, edit a post, and display the latest posts.

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        return self.posts

    def list_posts_by_author(self, author):
        return [post for post in self.posts if post.author == author]

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                break

    def list_latest_posts(self, n=5):
        return self.posts[-n:]

# Example usage:
blog = Blog()
blog.add_post(Post("My First Post", "This is the content of my first post.", "Alice"))
blog.add_post(Post("Another Post", "More content here.", "Bob"))
print(blog.list_all_posts())
print(blog.list_posts_by_author("Alice"))




# 5. Test the Application:
#Create instances of posts and test the functionality of your Blog system.

blog = Blog()
blog.add_post(Post("My First Post", "This is the content of my first post.", "Alice"))
blog.add_post(Post("Another Post", "More content here.", "Bob"))

# List all posts
print("All Posts:")
for post in blog.list_all_posts():
    print(post)

# List posts by a specific author
print("Posts by Alice:")
for post in blog.list_posts_by_author("Alice"):
    print(post)

# Delete a post
blog.delete_post("My First Post")
print("All Posts after deletion:")
for post in blog.list_all_posts():
    print(post)

# Edit a post
blog.edit_post("Another Post", "Updated content for another post.")
print("All Posts after editing:")
for post in blog.list_all_posts():
    print(post)

# List latest posts
print("Latest Posts:")
for post in blog.list_latest_posts():
    print(post)





# 1. Define Account Class:
#Create an Account class with attributes like account number, account holder name, and balance. 
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
        return f"Account({self.account_number}, {self.account_holder}, {self.balance})"
    
# Example usage:
acc1 = Account("123456", "Alice", 1000)
print(acc1)




# 2. Define Bank Class:
#Create a Bank class that manages a list of accounts.
#Include methods to add an account, check balance, deposit money, and withdraw money.

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def check_balance(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc.balance
        return None

    def deposit(self, account_number, amount):
        for acc in self.accounts:
            if acc.account_number == account_number:
                acc.balance += amount
                return True
        return False

    def withdraw(self, account_number, amount):
        for acc in self.accounts:
            if acc.account_number == account_number:
                if acc.balance >= amount:
                    acc.balance -= amount
                    return True
                else:
                    return False
        return False
    
# Example usage:
bank = Bank()
bank.add_account(Account("123456", "Alice", 1000))
bank.add_account(Account("654321", "Bob", 500))
print(bank.check_balance("123456"))
bank.deposit("123456", 200)
print(bank.check_balance("123456"))
print(bank.withdraw("123456", 300))
print(bank.check_balance("123456"))




# 3. Create Main Program:
#Develop a CLI to interact with the Banking system.
#Include options to add accounts, check balance, deposit money, and withdraw money.

def main():
    bank = Bank()
    while True:
        print("\n--- Banking System ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            acc_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.add_account(Account(acc_num, acc_holder, initial_balance))
            print("Account added successfully.")

        elif choice == "2":
            acc_num = input("Enter account number: ")
            balance = bank.check_balance(acc_num)
            if balance is not None:
                print(f"Account Balance: {balance}")
            else:
                print("Account not found.")

        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if bank.deposit(acc_num, amount):
                print("Deposit successful.")
            else:
                print("Account not found.")

        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if bank.withdraw(acc_num, amount):
                print("Withdrawal successful.")
            else:
                print("Account not found or insufficient funds.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




# 4. Enhance Banking System:
#Add functionality to transfer money between accounts, display account details, and handle account overdrafts.

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def check_balance(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc.balance
        return None

    def deposit(self, account_number, amount):
        for acc in self.accounts:
            if acc.account_number == account_number:
                acc.balance += amount
                return True
        return False

    def withdraw(self, account_number, amount):
        for acc in self.accounts:
            if acc.account_number == account_number:
                if acc.balance >= amount:
                    acc.balance -= amount
                    return True
                else:
                    return False
        return False

    def transfer(self, from_account, to_account, amount):
        if self.withdraw(from_account, amount):
            self.deposit(to_account, amount)
            return True
        return False

    def display_account_details(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                print(f"Account Number: {acc.account_number}")
                print(f"Account Holder: {acc.account_holder}")
                print(f"Account Balance: {acc.balance}")
                return
        print("Account not found.")
# Example usage:
bank = Bank()
bank.add_account(Account("123456", "Alice", 1000))
bank.add_account(Account("654321", "Bob", 500))
print(bank.check_balance("123456"))
bank.deposit("123456", 200)
print(bank.check_balance("123456"))
print(bank.withdraw("123456", 300))
print(bank.check_balance("123456"))




# 5. Test the Application:
# Create instances of accounts and test the functionality of your Banking system.

bank = Bank()
bank.add_account(Account("123456", "Alice", 1000))
bank.add_account(Account("654321", "Bob", 500))

# Check initial balances
print(bank.check_balance("123456"))
print(bank.check_balance("654321"))

# Test deposit
bank.deposit("123456", 200)
print(bank.check_balance("123456"))

# Test withdrawal
print(bank.withdraw("123456", 300))
print(bank.check_balance("123456"))

# Test transfer
bank.transfer("123456", "654321", 100)
print(bank.check_balance("123456"))
print(bank.check_balance("654321"))
print(bank.check_balance("123456"))
print(bank.check_balance("654321"))




