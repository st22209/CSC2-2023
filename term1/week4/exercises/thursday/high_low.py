# no python if statements were used
import os
import ctypes
import random

PATH = os.path.dirname(__file__)
C_CODE = "0a696e7420636865636b5f616e7377657228696e74206e756d2c20696e74206775657373290a7b0a09696620286e756d203d3d206775657373290a090972657475726e20313b0a09656c736520696620286775657373203e206e756d290a090972657475726e20323b0a09656c736520696620286775657373203c206e756d290a090972657475726e20303b0a09656c73650a090972657475726e2036393b0a7d0a"
with open(os.path.join(PATH, "check.c"), "w") as f:
    f.write(bytearray.fromhex(C_CODE).decode())
os.system(
    f'gcc -fPIC -shared {os.path.join(PATH, "check.c")} -o {os.path.join(PATH, "check.so")}'
)

ANSWER = random.randint(1, 100)
LIB = ctypes.CDLL(os.path.join(PATH, "check.so"))

responses = [
    "get good",
    "skill issue",
    "bad",
    "dog water",
    "trash",
    "bad",
    "imagine not guessing right",
    "tbh sounds like a skill issue",
    "lmao bad get good",
]


def check_answer(num) -> bool:
    ans = LIB.check_answer(ANSWER, num)
    res: dict[int, tuple[str, bool]] = {
        0: (
            "The number you guessed is too low! {}".format(random.choice(responses)),
            False,
        ),
        2: (
            "The number you guessed is too high! {}".format(random.choice(responses)),
            False,
        ),
        1: ("Yay you guessed it!", True),
    }
    answ, ret = res.get(ans, ["", False])

    print(answ)
    return ret  # type: ignore


def cleanup():
    os.remove(os.path.join(PATH, "check.c"))
    os.remove(os.path.join(PATH, "check.so"))
    exit(0)


print("The number is between 1 and 100")
print("You get 10 guesses and each incorrect guess removes one")
print("If you loose you are bad at the game. Just get better imo")
print("Enter a guess to start:")

guess_count = 9

while guess_count > -1:
    try:
        user_guess = int(input("> "))
    except ValueError:
        print("Number must be an int! {}".format(random.choice(responses)))
        continue

    do_next = {True: cleanup}
    func = do_next.get(check_answer(user_guess), lambda: ())
    func()

    print(
        "You have {} guesses remaining! {}".format(
            guess_count, random.choice(responses)
        )
    )
    guess_count -= 1
else:
    print(
        "Imagine loosing, you dont have to cause you did.\n{}".format(
            random.choice(responses)
        )
    )
