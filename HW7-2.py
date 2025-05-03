class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.rank_value = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T' : 10, 'J': 11, 'Q': 12, 'K': 13}

    def __str__(self):
        return f"{self.suit}{self.rank}"

    def get_value(self):
        return self.rank_value[self.rank]
    

def process_input():
    bound = []
    card_on_deck = input().split(";")
    player_cards_str = input().split(",")
    player_cards = []
    for card_str in player_cards_str:
        suit = card_str[0]
        rank = card_str[1]
        player_cards.append(Card(suit, rank))
    for i in range(len(card_on_deck)):
        suit = card_on_deck[i][0]
        lower = card_on_deck[i][1]
        upper = card_on_deck[i][4]
        bound.append([Card(suit, lower), Card(suit, upper)])
    while True:
        can_put = False
        for card in player_cards:
            for i in range(len(bound)):
                result = can_connect(card, bound[i][0], bound[i][1])
                if result == "L":
                    bound[i][0] = card
                    can_put = True
                if result == "U":
                    bound[i][1] = card
                    can_put = True
        if not can_put:
            print_bounds(bound)
            break
        
def print_bounds(bounds):
    first = True
    for bound_pair in bounds:
        lower = bound_pair[0]
        upper = bound_pair[1]
        if first:
            print(f"{str(lower)},{str(upper)}", end="")
            first = False
        else:
            print(f";{str(lower)},{str(upper)}", end="")
    

def can_connect(player_card, lower_bound, upper_bound):
    if player_card.suit != lower_bound.suit:
        return False
    if player_card.get_value() == lower_bound.get_value() - 1:
        return "L"
    if player_card.get_value() == upper_bound.get_value() + 1:
        return "U"
    return None

process_input()