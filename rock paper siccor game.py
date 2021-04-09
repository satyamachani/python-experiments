import sys
user1 = input("first player name")
user2 = input("second player name")
user1_answer = input("%s,what do you want to choose rock,paper,sciccors?:"%user1)
user2_answer = input("%s,what do you want to choose rock,paper,sciccors?:"%user2)
def compare(u1,u2):
    if u1 == u2:
        return ("its a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return (user1,"wins!")
        else:
            return (user2,"wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return (user1,"wins!")
        else:
            return (user2,"wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return (user1,"wins!")
        else:
            return (user2,"wins!")
    else:
        return ("invalid entry please check your input")
        sys.exit()
print(compare(user1_answer,user2_answer))