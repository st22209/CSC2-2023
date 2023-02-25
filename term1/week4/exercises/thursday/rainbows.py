import os
import time
import webbrowser

from rich.console import Console
from rich.prompt import Confirm
from simple_term_menu import TerminalMenu

# why am i using classes?
# 1. Because i can
# 2. To make my code spicy wicy no cap all fax my G

console = Console()
PRICES: dict[str, tuple[float, float]] = {
    "ADULT": (67.99, 62.99),
    "CHILD": (57.99, 52.99),
    "PENSION": (34, 34),
}


class Superpass:
    def __init__(self, price: float, discount: float) -> None:
        self.discounted = False

        self._normal_price = price
        self._discounted_price = discount

    @property
    def price(self):
        return (
            self._normal_price
            if not hasattr(self, "discounted") or not self.discounted
            else self._discounted_price
        )


class Adult(Superpass):
    def __init__(self) -> None:
        super().__init__(*PRICES["ADULT"])


class Child(Superpass):
    def __init__(self) -> None:
        super().__init__(*PRICES["CHILD"])


class Pensioner(Superpass):
    def __init__(self) -> None:
        super().__init__(*PRICES["PENSION"])
        del self.discounted


class Spectator:
    price = 19.99


class SpicySpectator:
    price = 19.99


OPTIONS = [
    "[p] buy superpass",
    "[s] become a spectator (lame tbh)",
    "[r] get a surprise",
    "[q] complete order",
]
cart = []

while (
    term_index := TerminalMenu(OPTIONS, title="What would you like to do?").show()
) != 3:
    # because i can
    match term_index:
        case 0:
            try:
                age = int(console.input("[red]Please enter your age: "))
            except ValueError:
                print("Age should be a number, You are a fool for not knowing that")
                quit(0)

            if 2 <= age <= 13:
                superpass = Child()
            elif age < 64:
                superpass = Adult()
            else:  # bug: if you enter an age less than 2 it will give you this adult pass ^
                # but stfu nobody asked we justgonna not talk about it
                superpass = Pensioner()

            sure = Confirm.ask(
                f"[blue]Are you sure you want add 1 '{superpass.__class__.__name__} Superpass' to the cart?",
                default=True,
            )
            if sure:
                cart.append(superpass)
                console.print(
                    f"[green]'{superpass.__class__.__name__} Superpass' Added to cart ✅"
                )
                time.sleep(0.5)
        case 1:
            spicy = Confirm.ask(
                f"[blue]Would you like the spectator pass to include Ultimate Spectra 7D Theatre Ride?",
                default=True,
            )

            passname = (
                "Spectator"
                if not spicy
                else "Spectator with Ultimate Spectra 7D Theatre Ride"
            )

            sure = Confirm.ask(
                f"[blue]Are you sure you want add 1 '{passname}' to the cart?",
                default=True,
            )
            if sure:
                cart.append(Spectator() if not spicy else SpicySpectator())
        case 2:
            webbrowser.open("https://youtube.com/watch?v=dQw4w9WgXcQ")  # hehe
    os.system("clear")

superpasses = list(filter(lambda x: hasattr(x, "discounted"), cart))
toggle_discount = all(
    [
        len(superpasses) > 3,  # make sure there are more than 3+ superpasses
        len(set(map(lambda x: x.__class__.__name__, superpasses)))
        > 1,  # make sure its a mix of child and adult
    ]
)
if toggle_discount:
    console.print(
        "[red]Yay you're in luck.\nYou spent enough money for us to let you have a discount and still make a shit ton of money :)"
    )
    for spass in cart:
        if hasattr(spass, "discounted"):
            spass.discounted = True

total_price = round(sum(list(map(lambda x: x.price, cart))), 2)
console.print(f"[bold green]Your total price comes out to: ${total_price}")
