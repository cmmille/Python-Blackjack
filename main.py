############### Blackjack Project #####################
from cards import new_deck, shuffle_deck, draw_card, show_hand
from art import logo


# Start game
print(logo)

deck = new_deck()
shuffled_deck = shuffle_deck(deck)

your_hand = []
your_value = 0
dealer_hand = []
dealer_value = 0

game_over = False

print("Dealer shows: ")
draw_card(dealer_hand, shuffled_deck)
dealer_value = show_hand(dealer_hand, deck)
print('\n')

print("Your cards: ")
draw_card(your_hand, shuffled_deck)
draw_card(your_hand, shuffled_deck)
your_value = show_hand(your_hand, deck)

your_turn = True
while your_turn:
  if your_value > 21:
    print('Bust!\n Game Over.')
    your_turn = False
    game_over = True
  elif input("Hit? (y/n)\t").lower() == 'y':
    draw_card(your_hand, shuffled_deck)
    print('\n')
    your_value = show_hand(your_hand, deck)
  else:
    print(f'Holding at: {your_value}.')
    your_turn = False

dealer_turn = True
while dealer_turn and not game_over:
  if len(dealer_hand) == 1:
    print("\nDealer's turn:")
  if dealer_value > 21:
    print('Dealer busts!')
    dealer_turn = False
    print('\nYou Win!')
    game_over = True
  elif dealer_value <= 16:
    draw_card(dealer_hand, shuffled_deck)
    dealer_value = show_hand(dealer_hand, deck)
  else: 
    dealer_turn = False

if not game_over and your_value > dealer_value:
  print("\nYou win!")
elif not game_over and dealer_value > your_value:
  print("\nYou lose!")