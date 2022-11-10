import numpy as np

CARDS = ["ACE", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class BlackJackEnv:
    def __init__(self, seed=None):
        self.rng = np.random.default_rng(seed=seed)
        self.dealer_hand = []
        self.player_hand = []

    def deal_cards(self):
        """
        Deals 2 cards for both player and dealer
        returns 2 cards for player, one face-up card dealer card. 
        """
        self.dealer_hand = self.rng.choice(CARDS, 2).tolist()
        self.player_hand = self.rng.choice(CARDS, 2).tolist()

        player_val = calc_hand_value(self.player_hand)
        while player_val < 12:
            card = self.rng.choice(CARDS)
            self.player_hand.append(card)
            player_val = calc_hand_value(self.player_hand)

        if calc_hand_value(self.player_hand) == 21:
            dealer_val = calc_hand_value(self.dealer_hand)
            if dealer_val == 21:
                return 0, None, None
            else: 
                return 1, None, None
        return None, self.player_hand, self.dealer_hand[0]

    def hit(self):
        """
        Deals 1 card to player
        """
        card = self.rng.choice(CARDS)
        self.player_hand.append(card)
        player_val = calc_hand_value(self.player_hand)
        if player_val > 21:
            return -1, None
        return None, self.player_hand

    def stick(self):
        """
        Just keep adding cards to dealer deck until 17, 
        then call evaluate and end game
        """
        while calc_hand_value(self.dealer_hand) < 17:
            # print(self.dealer_hand)
            self.dealer_hand.append(self.rng.choice(CARDS))
        player_val = calc_hand_value(self.player_hand)
        dealer_val = calc_hand_value(self.dealer_hand)
        if dealer_val > 21 or dealer_val < player_val:
            return 1
        elif dealer_val == player_val:
            return 0
        else:
            return -1


def calc_hand_value(hand):
    # print(f"Hand: {hand}")
    rep_hand = [int(x) if x != "ACE" else 11 for x in hand]
    # print(f"Rep_hand: {rep_hand}")
    sum = np.sum(np.array(rep_hand))
    num_aces = hand.count("ACE")
    while sum > 21 and num_aces > 0:
        sum = sum - 10
        num_aces -= 1
    return sum

def calc_hand_value_usable_ace(hand):
    rep_hand = [int(x) if x != "ACE" else 11 for x in hand]
    sum = np.sum(np.array(rep_hand))
    num_aces = hand.count("ACE")
    while sum > 21 and num_aces > 0:
        sum = sum - 10
        num_aces -= 1
    return sum, num_aces