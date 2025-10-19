def card_pair_to_emoji(*args):
    """
    Convert one or more card tuples (suit, rank) to their emoji.
    Each card: (suit, rank) where suit in 's', 'h', 'd', 'c' and rank in 'a','2'...'k'
    """
    suit_map = {'s': 0x1F0A1, 'h': 0x1F0B1, 'd': 0x1F0C1, 'c': 0x1F0D1}
    rank_order = ['a','2','3','4','5','6','7','8','9','10','j','q','k']

    emojis = []
    for card in args:
        suit, rank = card
        index = rank_order.index(rank.lower())
        code_point = suit_map[suit.lower()] + index
        emojis.append(chr(code_point))
    return emojis