print("Hello! My name is Pie.")
print("I was created in 2021.")
print("Please, remind me your name.")

name = input()

print("What a great name you have, " + name + "!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())
age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print("Your age is " + str(age) + ": that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

number = int(input())
zero = 0
while zero <= number:
    print(zero, "!")
    zero = zero + 1

print("Let's test your multiplication skills.")
print("What is 2x2?")

answer = int(input())
correct = 4

if answer != correct:
    print("Please, try again.")

else:
    print("Completed, have a nice day!")

print("Congratulations, have a nice day!")
