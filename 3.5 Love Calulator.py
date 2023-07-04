# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# Answer

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

t = name1_lower.count("t") + name2_lower.count("t")
r = name1_lower.count("r") + name2_lower.count("r")
u = name1_lower.count("u") + name2_lower.count("u")
e = name1_lower.count("e") + name2_lower.count("e")

true = str(t + r + u + e)

l = name1_lower.count("l") + name2_lower.count("l")
o = name1_lower.count("o") + name2_lower.count("o")
v = name1_lower.count("v") + name2_lower.count("v")
e = name1_lower.count("e") + name2_lower.count("e")

love = str(l+o+v+e)

score = true + love
score_as_int = int(score)

if score_as_int < 10 or score_as_int > 90 :
    print(f"Your score is {score_as_int}, you go together like coke and mentos.")
elif score_as_int >= 40 and score_as_int <= 50 :
    print(f"Your score is {score_as_int}, you are alright together.")
else : 
    print(f"Your score is {score_as_int}.")
