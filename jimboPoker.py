from collections import Counter

class Card:
    def __init__(self, suit: int, rank: int, flipped: bool = False):
        self.suit = suit
        self.rank = rank
        self.flipped = flipped

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def set_suit(self, suit):
        self.suit = suit

    def set_rank(self, rank):
        self.rank = rank

    def flip(self):
        self.flipped = not self.flipped

class River:
    def __init__(self, card1: Card, card2: Card, card3: Card, card4: Card, card5: Card):
        self.cards = [card1, card2, card3, card4, card5]

    def get_card(self, index):
        return self.cards[index]

    def set_card(self, index, card):
        self.cards[index] = card

class Hand:
    def __init__(self, card1: Card, card2: Card):
        self.cards = [card1, card2]

    def get_card(self, index):
        return self.cards[index]

    def set_card(self, index, card):
        self.cards[index] = card

class Poker:
    def __init__(self, hand: Hand, river: River):
        self.hand = hand
        self.river = river
        self.all_cards = hand.cards + river.cards

    def determine_best_hand(self):
        rank_count = Counter(card.get_rank() for card in self.all_cards)
        suit_count = Counter(card.get_suit() for card in self.all_cards)
        ranks = sorted(rank_count.keys(), reverse=True)

        # Check for Flush
        if any(count >= 5 for count in suit_count.values()):
            return "Flush"

        # Check for Four of a Kind, Full House, Three of a Kind, and Pairs
        four = any(count == 4 for count in rank_count.values())
        three = any(count == 3 for count in rank_count.values())
        pairs = sum(1 for count in rank_count.values() if count == 2)

        if four:
            return "Four of a Kind"
        if three and pairs:
            return "Full House"
        if three:
            return "Three of a Kind"
        if pairs == 2:
            return "Two Pair"
        if pairs == 1:
            return "Pair"

        return "High Card"


