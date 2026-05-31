import random

# Snakes and Ladders positions
snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 2,
    95: 72
}

ladders = {
    6: 25,
    11: 40,
    60: 85,
    46: 90,
    17: 69
}

player_pos = 0
ai_pos = 0

print("=== SNAKE AND LADDER ===")
print("You vs AI")
print()

while True:
    input("Press Enter to roll the dice...")

    # Human turn
    dice = random.randint(1, 6)
    print(f"\nYou rolled: {dice}")

    if player_pos + dice <= 100:
        player_pos += dice

    if player_pos in ladders:
        print("You found a ladder!")
        player_pos = ladders[player_pos]

    elif player_pos in snakes:
        print("Oops! Snake bite!")
        player_pos = snakes[player_pos]

    print("Your Position:", player_pos)

    if player_pos == 100:
        print("\n🎉 Congratulations! You Win!")
        break

    # AI turn
    print("\nAI is rolling...")
    ai_dice = random.randint(1, 6)
    print("AI rolled:", ai_dice)

    if ai_pos + ai_dice <= 100:
        ai_pos += ai_dice

    if ai_pos in ladders:
        print("AI found a ladder!")
        ai_pos = ladders[ai_pos]

    elif ai_pos in snakes:
        print("AI got bitten by a snake!")
        ai_pos = snakes[ai_pos]

    print("AI Position:", ai_pos)

    if ai_pos == 100:
        print("\n🤖 AI Wins!")
        break

    print("\n--------------------------")