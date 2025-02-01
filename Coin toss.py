class Coin:
    def __innit_(self):
        self.sideup = 'Heads'

    def toss(self):
        import random
        toss = random.randint(0, 1) 
        if toss == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup
    
def main():
    coin_toss = Coin()
    coin_toss.toss()
    print("the coin landed on", coin_toss.get_sideup())

main()
