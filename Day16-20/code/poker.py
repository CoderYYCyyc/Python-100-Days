"""
经验：符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择
"""
from enum import Enum, unique

import random


@unique
class Suite(Enum):
    """花色"""

    SPADE, HEART, CLUB, DIAMOND = range(4)
    # self.value 是枚举类型中每个成员的一个属性，用于存储该成员对应的整数值
    def __lt__(self, other):
        return self.value < other.value


class Card:
    """牌"""

    def __init__(self, suite, face):
        """初始化方法"""
        self.suite = suite
        self.face = face

    def show(self):
        """显示牌面"""
        suites = ['♠︎', '♥︎', '♣︎', '♦︎']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite]}{faces[self.face]}'

    def __repr__(self):
        return self.show()


class Poker:
    """扑克"""

    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in range(4)
                      for face in range(1, 14)]

    def shuffle(self):
        """洗牌（随机乱序）"""
        random.shuffle(self.cards)
        self.index = 0

    def deal(self):
        """发牌"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)


class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def sort(self, comp=lambda card: (card.suite, card.face)):
        """整理手上的牌"""
        self.cards.sort(key=comp)


def main():
    """主函数"""
    # 生成一副扑克牌
    poker = Poker()
    # 洗牌
    poker.shuffle()
    # 确定玩家是谁
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    # 只要还有牌，就发牌
    while poker.has_more:
        for player in players:
                player.get_one(poker.deal())
    for player in players:
        player.sort()
        print(player.name, end=': ')
        print(player.cards)


if __name__ == '__main__':
    main()