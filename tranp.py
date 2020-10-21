import random


class TrumpGame:
    def make_card_list(self):
        symbol_list = ['C', 'H', 'S', 'D']
        card_list = []

        for symbol in symbol_list:
            for number in range(1, 14):
                card = {
                    'number': number,
                    'symbol': symbol
                }
               
                if number == 1:
                    card['string'] = symbol + 'A'
                elif number == 11:
                    card['string'] = symbol + 'J'
                elif number == 12:
                    card['string'] = symbol + 'Q'
                elif number == 13:
                    card['string'] = symbol + 'K'
                else:
                    card['string'] = symbol + str(number)

                card_list.append(card)

        self.card_list = card_list

    def shuffle(self):
        random.shuffle(self.card_list)

    def reset_draw_cards(self, number):
        card_list = self.make_card_list()
        self.shuffle()
        self.draw_cards = []

        for i in range(0, number):
            self.draw_cards.append(
                self.card_list.pop(0)
            )

    def check_poker_hand(self):
        pair_count = 0
        match_count = 0
        match_number = 0
        flash_flag = True
        straight_flag = True

        cards = sorted(self.draw_cards, key=lambda x: x['number'])

        for i in range(1, 5):
            if cards[i]['number'] == cards[i - 1]['number']:
                match_count += 1
                if i == 4:
                    if match_count == 1:
                        pair_count += 1
                    elif match_count > 1:
                        match_number = match_count + 1
            else:
                if match_count == 1:
                    pair_count += 1
                elif match_count > 1:
                    match_number = match_count + 1
                match_count = 0
            if flash_flag == True and cards[i]['symbol'] != cards[i - 1]['symbol']:
                flash_flag = False
            if straight_flag == True and cards[i]['number'] != cards[i - 1]['number'] + 1:
                if cards[i]['number'] != 10 or cards[i - 1]['number'] != 1:
                    straight_flag = False

        if straight_flag == True and flash_flag == True:
            if cards[0]['number'] == 1 and cards[4]['number'] == 13:
                hand = 'ロイヤル\nストレートフラッシュ'
            else:
                hand = 'ストレートフラッシュ'
        elif match_number > 2:
            if match_number == 4:
                hand = '4カード'
            else:
                if pair_count > 0:
                    hand = 'フルハウス'
                else:
                    hand = '3カード'
        elif flash_flag == True:
            hand = 'フラッシュ'
        elif straight_flag == True:
            hand = 'ストレート'
        elif pair_count > 0:
            if pair_count > 1:
                hand = '2ペア'
            else:
                hand = '1ペア'
        else:
            hand = 'ぶた'

        return hand

if __name__ == '__main__':
    tg = TrumpGame()
    tg.reset_draw_cards(5)
    for card in tg.draw_cards:
        print(card['string'])
    print(tg.check_poker_hand())