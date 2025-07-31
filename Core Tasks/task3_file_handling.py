file_path = "sample.txt"
with open(file_path, "w") as file:
    file.write("Welcome to Python File Handling")

with open(file_path, "r") as file:
    content = file.read()
    print(content)