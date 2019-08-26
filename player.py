class Player:
    VERSION = "3.0"

    players = None
    my_id = None
    round = None
    hand = None
    com_cards = None

    def betRequest(self, game_state):
        self.players = game_state["players"]
        self.my_id = game_state["in_action"]
        self.round = game_state["round"]
        self.com_cards = game_state["community_cards"]
        self.hand = self.get_hand()

        bet = self.set_own_bet()
        return bet

    def get_my_stack(self):
        for player in self.players:
            if player["id"] == self.my_id:
                stack = int(player["stack"])
                return stack

    def showdown(self, game_state):
        pass

    def set_own_bet(self):
        if self.round == 0:
            return 0
        elif self.check_for_pairs():
            return self.get_my_stack()
        else:
            return 0

    def check_for_pairs(self):

        for c_card in self.com_cards:
            for card in self.hand:
                if c_card['rank'] == card['rank']:
                    return True
        return False

    def get_hand(self):
        for player in self.players:
            if player["id"] == self.my_id:
                return player["hole_cards"]
