#IMPORTS #
import random

#CONSTANTS, GLOBAL VARIABLES #
SUITS = {'h','s','c','d'}
VALUES = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'j':11,'q':12,'k':13,'a':14}

class Deck:
    def __init__(self): self.deck = [(s+k,v) for s in SUITS for k,v in VALUES.items()]
    def __str__(self): return ', '.join([str(elem) for elem in self.deck])
    def shuffle_deck(self): random.shuffle(self.deck)
    def split_deck(self, n=2): return [[(self.deck[m]) for m in range(x,len(self.deck), n)] for x in range(n)]


class Player:
    def __init__(self, name): self.name = name
    def get_name(self): return self.name
    def get_deck(self): return self.deck
    def add_deck(self, deck): self.deck = deck
    def draw_card(self): return self.deck.pop(0)
    def add_cards_to_deck(self, cards): self.deck.extend(cards)
    def shuffle_deck(self): random.shuffle(self.deck)

class Game:
    def __init__(self, player_n=2):
        self.players = [Player('player' + str(p)) for p in range(player_n)]
        self.decks = Deck()
        self.decks.shuffle_deck()
        self.decks = self.decks.split_deck(player_n)
        for n in range(len(self.players)): self.players[n].add_deck(self.decks[n])
    def get_players(self): return self.players
    def remove_player(self, p): self.players.remove(p)
    def add_player(self, p): self.players.append(p)

    ##### Set up for N players #####
    def game_is_finished(self):
        for p in self.get_players():
            if not p.get_deck():
                print(p.get_name().capitalize() + ' lost and ended the game!')
                self.remove_player(p)
        if len(self.get_players()) == 1:
            print(self.get_players()[0].get_name().capitalize() + ' won')
            return True
        return False

    def end_war(self, cards, players, card_list):
        cards  = sorted(cards,key=lambda x: x[1][1], reverse=True)
        temp_max_list = [elem for elem in cards if elem[1][1] == cards[0][1][1]]
        if len(temp_max_list) == 1:
            for ind, p in enumerate(self.get_players()):
                if p.get_name() == temp_max_list[0][0]:
                    p.add_cards_to_deck(card_list)
                    return True
        names = [elem[0] for elem in temp_max_list]

        for p in players[:]:
            if not(p.get_name() in names):
                players.remove(p)
        return False

    def play(self):
        round, game_on = 1, True
        # Game Starts
        while game_on:
            if self.game_is_finished(): break

            if not round % 200:
                for p in self.get_players():
                    p.shuffle_deck()
            print('Round ',round)
            card_list, player_list, war_on = [], self.get_players()[:],True
            # Comparing player cards
            while war_on:
                if self.game_is_finished():
                    game_on = False; break
                cards = [[p.get_name(),p.draw_card()] for p in list(set(player_list) & set(self.get_players()))]
                card_list.extend([c[1] for c in cards])
                print('CARDS DREW:',*cards)
                print('PLAYERS CARDS NUMBER',[(p.get_name(),len(p.get_deck())) for p in player_list])
                # input('Turn')
                if self.end_war(cards, player_list, card_list):
                    round += 1
                    break
                else:
                    print('Its a tie')
                    for _ in range(3):
                        if self.game_is_finished():
                            game_on = False; war_on = False; break
                        cards = [[p.get_name(),p.draw_card()] for p in self.get_players() if p in list(set(player_list) & set(self.get_players()))]
                        # In case where only one player is left with the cards, then all cards are gifted to that player by default
                        if len(cards) == 1:
                            p = list(set(player_list) & set(self.get_players()))[0]
                            card_list.extend([c[1] for c in cards])
                            p.add_cards_to_deck(card_list)
                            war_on = False; break
                        # If players which had tie, all lost cards at teh same time, then none of them is a winner and cards are split between remaiing players
                        if not len(cards):
                            for ind, p in enumerate(self.get_players()):
                                for ind in range(ind, len(card_list), len(self.get_players())):
                                    p.add_cards_to_deck([card_list[ind]])
                            war_on = False; break
                        card_list.extend([c[1] for c in cards])

    ##### Set up for Two players #####
    # def game_is_finished(self):
    #     for p in self.get_players():
    #         if not p.get_deck():
    #             print(p.get_name().capitalize() + ' lost')
    #             return True
    #     return False
    #
    # def play(self):
    #     round, game_on = 1, True
    #     # Game Starts
    #     while game_on:
    #         if self.game_is_finished(): break
    #
    #         if not round % 200:
    #             for p in self.players:
    #                 p.shuffle_deck()
    #         print('Round ',round)
    #         card_list, war_on = [], True
    #         # Comparing player cards
    #         while war_on:
    #             if self.game_is_finished():
    #                 game_on = False; break
    #             cards = [[p.get_name(),p.draw_card()] for p in self.players]
    #             card_list.extend([c[1] for c in cards])
    #             print('cards drew:',cards, 'p0 ',len(self.players[0].deck),'p1 ',len(self.players[1].deck),)
    #
    #             if cards[0][1][1] < cards[1][1][1]:
    #                 self.players[1].add_cards_to_deck(card_list)
    #                 round += 1
    #                 break
    #             elif cards[0][1][1] > cards[1][1][1]:
    #                 self.players[0].add_cards_to_deck(card_list)
    #                 round += 1
    #                 break
    #             else:
    #                 print('Its a tie')
    #                 for _ in range(3):
    #                     if self.game_is_finished():
    #                         game_on = False; war_on = False; break
    #                     cards = [[p.get_name(),p.draw_card()] for p in self.players]
    #                     card_list.extend([c[1] for c in cards])


if __name__ == '__main__':
    g = Game(6)
    g.play()
