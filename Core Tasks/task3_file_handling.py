def collect_feedback():

 name = input("Enter your name: ")

 feedback = input("Enter your feedback: ")

 with open("feedback.txt", "a") as file:

 file.write(f"Name: {name}, Feedback: {feedback}\n")

 print("Thank you for your feedback!")

    collect_feedback()


    
