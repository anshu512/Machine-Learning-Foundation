import random


def monty_hall_simulation(num_trials=10000):

    doors = [0, 1, 2]

    stay_win = 0
    switch_win = 0

    for _ in range(num_trials):

        # Randomly choose the door containing the car
        car_door = random.choice(doors)

        # Player randomly chooses a door
        player_choice = random.choice(doors)

        # Monty chooses a door that is neither
        # the player's choice nor the car door
        monty_options = []

        for door in doors:
            if door != car_door and door != player_choice:
                monty_options.append(door)

        monty_choice = random.choice(monty_options)

        # The remaining door is the switching choice
        for door in doors:
            if door != player_choice and door != monty_choice:
                switch_choice = door

        # Check if staying wins
        if car_door == player_choice:
            stay_win += 1

        # Check if switching wins
        if car_door == switch_choice:
            switch_win += 1

    # Calculate probabilities
    stay_win_probability = stay_win / num_trials * 100
    switch_win_probability = switch_win / num_trials * 100

    # Display results
    print(f"Results after {num_trials:,} trials:")
    print(
        f"Staying won {stay_win} times "
        f"({stay_win_probability:.2f}%)"
    )
    print(
        f"Switching won {switch_win} times "
        f"({switch_win_probability:.2f}%)"
    )


monty_hall_simulation()