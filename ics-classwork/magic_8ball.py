import random


choice = random.randrange(1, 21)  # 1-20
response = ""

if choice == 1:
    response = "It is certain"
elif choice == 2:
    response = "It is decidedly so"
elif choice == 3:
    response = "Without a doubt"
elif choice == 4:
    response = "Yes - definitely"
elif choice == 5:
    response = "You may rely on it"
elif choice == 6:
    response = "As I see it, yes"
elif choice == 7:
    response = "Most likely"
elif choice == 8:
    response = "Outlook good"
elif choice == 9:
    response = "Signs point to yes"
elif choice == 10:
    response = "Yes"
elif choice == 11:
    response = "Reply hazy, try again"
elif choice == 12:
    response = "Ask again later"
elif choice == 13:
    response = "Better not tell you now"
elif choice == 14:
    response = "Cannot predict now"
elif choice == 15:
    response = "Concentrate and ask again"
elif choice == 16:
    response = "Don't count on it"
elif choice == 17:
    response = "My reply is no"
elif choice == 18:
    response = "My sources say no"
elif choice == 19:
    response = "Outlook not so good"
elif choice == 20:
    response = "Very doubtful"
else:
    response = "8-BALL ERROR!"

print("MAGIC 8-BALL SAYS: " + response)