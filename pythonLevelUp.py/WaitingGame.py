import time
import random

def waiting_game():
    print("Welcome to waiting game!")
    wait_time = random.randint(2,9)
    print(f"Press Enter after {wait_time} seconds!")
    time.sleep(wait_time)
    start = time.time()
    input("Press Enter now!")
    end = time.time()
    reaction = end - start
    print(f"Your reaction time was {reaction:.3f} seconds.")
waiting_game()