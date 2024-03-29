class Player:
    VERSION = "8.3"

    players = None
    my_id = None
    round = None
    hand = None
    com_cards = None
    all_cards = None
    bet_index = None
    current_buy_in = None
    minimum_raise = None
    player_info = None

    def betRequest(self, game_state):
        self.players = game_state["players"]
        self.my_id = game_state["in_action"]
        self.round = game_state["round"]
        self.com_cards = game_state["community_cards"]
        self.hand = self.get_hand()
        self.all_cards = self.hand + self.com_cards
        self.bet_index = game_state["bet_index"]
        self.current_buy_in = game_state["current_buy_in"]
        self.minimum_raise = game_state["minimum_raise"]
        self.player_info = self.get_player_info()

        bet = self.set_own_bet()
        return bet

    def get_player_info(self):
        for player in self.players:
            if player["id"] == self.my_id:
                return player

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
        elif self.check_flush():
            return self.get_my_stack()
        # elif self.check_straight():
        #     return self.get_my_stack()
        elif self.get_minimum_amount_to_bet() > 400:
            return 0
        else:
            return self.get_minimum_amount_to_bet()

    def get_minimum_amount_to_bet(self):
        return int(self.current_buy_in) - int(self.player_info["bet"])

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

    def check_flush(self):
        diamonds = []
        hearts = []
        spades = []
        clubs = []

        for card in self.all_cards:
            if card["suit"] == "diamonds":
                diamonds.append(card)
            elif card["suit"] == "hearts":
                hearts.append(card)
            elif card["suit"] == "spades":
                spades.append(card)
            elif card["suit"] == "clubs":
                clubs.append(card)

        if len(diamonds) >= 4 or len(hearts) >= 4 or len(spades) >= 4 or len(clubs) >= 4:
            return True
        else:
            return False

    # def check_straight(self):
    #     sorted_cards = sorted(self.all_cards, key=lambda c: c["rank"])
    #     boolean = False
    #
    #     for card, n in enumerate(sorted_cards):
    #         try:
    #             if abs(card - sorted_cards[n + 1]) == 1:
    #                 boolean = True
    #             else:
    #                 boolean = False
    #         except IndexError:
    #             continue
    #     return boolean
