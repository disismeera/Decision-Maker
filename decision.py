#This is the basic python code of the project

def decision_maker():
    print("Welcome to the Decision Maker!")
    print("Please enter your choices separated by commas:")
    choices = input().split(",")
    import random
    decision = random.choice(choices)
    print("The Decision Maker has decided:", decision)

decision_maker()
