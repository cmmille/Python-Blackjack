import random

suits = ['♢', '♠', '♣', '♡']
values = {
  'A': 11,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  '10': 10,
  'J': 10,
  'Q': 10,
  'K': 10
}

def new_deck():
  """ Return a dictionary of cards with their values """
  deck = {}
  for suit in suits:
    for card_value in values:
      deck[card_value + suit] = values[card_value]
  return deck

def shuffle_deck(deck):
  """ Return a list of shuffled card key values """
  shuffled_deck = []

  for card in deck:
    shuffled_deck.append(card)

  random.shuffle(shuffled_deck)

  return shuffled_deck

def draw_card(hand, shuffled_deck):
  hand.append(shuffled_deck.pop())

def show_hand(hand, deck):
  hand_string = ' '.join(hand)
  print(hand_string)
  
  # Calculate values
  hand_value = 0
  num_aces = 0
  for card in hand:
    hand_value += deck[card]
    if 'A' in card:
      num_aces+=1

  if hand_value > 21:
    while num_aces > 0 and hand_value >21:
      hand_value-=10
      num_aces-=1
  print(f"Total: {hand_value}")

  return hand_value
  