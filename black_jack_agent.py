import numpy as np

class BlackJackAgent:
    """
    On policy first visit MC control (epsilon soft policy)
    """

    def __init__(self, policy, seed=42):
        """
        Define state as:
        3D index of: has_usable_ace, player_value, dealer_card
        index calculated by: 
            - usable_ace = 0 or 1, player_value = 0 - 10, dealer_card = 0 - 10
            - usable_ace * 100 + player_value * 10 + dealer_card

        """
        # np array of shape num_actions x num_states
        # p (a | s)
        self.rng = np.random.default_rng(seed)
        self.policy = policy

    def take_action(self, state_idx):
        """
        0 for hit, 1 for stick
        """
        action = self.rng.choice([0, 1], p=self.policy[:, state_idx])
        return action


def get_state_idx(has_usable_ace, player_value, dealer_card):
    usable_idx = 1 if has_usable_ace else 0
    idx = usable_idx * 100
    player_idx = player_value - 12
    idx += player_idx * 10
    dealer_idx = 0 if dealer_card == "ACE" else int(dealer_card) - 1
    idx += dealer_idx
    return idx
