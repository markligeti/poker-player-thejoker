class Player:
    VERSION = "2.3"

    players = None
    my_id = None
    round = None
    hand = None
    com_cards = None

    def betRequest(self, game_state):
        self.players = game_state["players"]
        self.my_id = game_state["in_action"]
        self.round = game_state["round"]
        self.hand = self.players[self.my_id]["hole_cards"]
        self.com_cards = game_state["community_cards"]


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

        for key, val in self.com_cards.items():
            for card in self.hand:
                if key == 'rank' and card['rank'] == val:
                    return True


        return False

