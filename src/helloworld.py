import random

# def hello_world(city):
#     print(f'Hello World from {city}')
#     print('This is a test')

# def main():
#     hello_world('OKC')

# def test():
#     print('This is another GitHub test, good luck')
    
# def test2():
#     print('The testing and practice continues!') 


# def test3():
#     print('Working by myself is borring but I need the practice.')
   
# main()


class deckOfCards():
    
    def __init__(self):
        suits = ["spades", "hearts", "dimonds", "clubs"]
        self.number = random.randint(1, 10)
        self.suit = random.choice(suits)
    
    def __repr__(self):
        return f"You have been delt a {self.number} of {self.suit}"

first_card = deckOfCards()
print(first_card)