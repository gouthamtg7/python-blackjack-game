import random

s1 = input("Do you want to play BLACKJACK??\n[Type 'y' or 'n']\n=>")
game_over = False
if s1 == "n":
    print("Sure! Have a great day ahead bummer!!")
else :
    while(game_over==False):
        print("\n"*1000)
        print('''
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              '------'                           |__/           
        ''')
        K = 10
        Q = 10
        J = 10
        A = 11
        j=0
        cards = [1,2,3,4,5,6,7,8,9,10,A,K,Q,J]
        user_cards = list()
        computer_cards = list()
        user_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        if A in computer_cards:
            A = 11
        print(f"Your cards : {user_cards}\n")
        print(f"Computer's first card: {computer_cards[0]}")
        while(j==0):
            s2 = input("HIT or STAND??\n[For rules, type 'rules']\n**CASE SENSITIVE**\n=>")
            if s2 == "rules":
                print("HIT - Pick another card\nSTAND - Call out for blackjack to see who's the winner\n")
            elif s2 == "HIT":
                user_cards.append(random.choice(cards))
                print(f"Your cards : {user_cards}\n")
                if sum(user_cards) > 21:
                    print("BUST!! You lost 😭")
                    j = 0
            elif s2 == "STAND":
                if A in user_cards:
                    s4 = input("Do you want to reassign value to A? Type(Y/N)\n")
                    if s4 == "Y":
                        y = int(input("You got an Ace, would you like to count it as 1 or 11?\n==>"))
                        if y == 1:
                            A = 1
                        elif y == 11:
                            A = 11
                if sum(computer_cards) < 17:
                    computer_cards.append(random.choice(cards))
                    print(f"Computer's cards : {computer_cards}\n")
                if A in computer_cards:
                    w = computer_cards.index(A)
                    e = 1 - w
                    if 21 - computer_cards[e] > 11:
                        A = 1
                print(f"Final Cards in your hand: {user_cards}\nFinal Cards in computer's hand: {computer_cards}")
                if sum(computer_cards) > 21:
                    print("Congrats!! You won 🥳🥳")
                    j = 1
                    break
                if sum(computer_cards) > sum(user_cards):
                    print("Ohho!! You lost 😭")
                    j = 1
                elif sum(computer_cards) < sum(user_cards):
                    print("Congrats!! You won 🥳🥳")
                    j = 1
            else:
                game_over = True

        if j!=0:
            s3 = input("Another game?? Type(Yes/No)\n ")
            if s3=="Yes":
                continue
            elif s3=="No":
                game_over= True














