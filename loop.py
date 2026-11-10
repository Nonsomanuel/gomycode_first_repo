#For Loop

students = ["Ayo", "Victor", "Lekan", "Waris", "Elizabeth"]

#
# for student in students:
#     # print(student)

word = "Data Science"
# for alphabet in word:
#     print(alphabet)

# for number in range(1, 11):
#     print(number)

#MUltiples of 2 (for loop(Range))
# for number in range(2, 21, 5):
#     print(number)

# Break statement
# for student in students:
#     if student == "Lekan":
#         print("Lekan is found. Stopping the loop.")
#         break
#     print(student)

#While Loop
# x = 6
# while x > 0:
#     print(x)
#     x -= 1
# else:
#     print("Countdown complete. Blast off!")

# #Break in While Loop
# x = 6
# while x > 0:
#     print(x)
#     x -= 1
#     if x == 3:
#         print("Breaking the loop, x is now 3.")
#         break

#Break in While Loop with else
# x = input("Enter your Instructor's name: ")
# while x:
#     if x == "Nonso":
#         print("Welcome, Nonso!")
#         break
#     else:
#         print("Incorrect name. Please try again.")
#         x = input("Enter your Instructor's name: ")

#Randomization in For Loop
import random

# random_numbers = [random.randint(1, 100)]
#
# for number in random_numbers:
#     print(f"Random number: {number}")

#Number guessing game
secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 3

guess = int(input("Guess the secret number between 1 and 10: "))
while guess != secret_number:
    attempts += 1
    if attempts >= max_attempts:
        print(f"Sorry, you've reached the maximum attempts. The secret number was {secret_number}.")
        break
    print("Incorrect guess. Please try again.")
    guess = int(input("Guess the secret number between 1 and 10: "))
else:
    print(f"Congratulations! You've guessed the secret number {secret_number} correctly.")
