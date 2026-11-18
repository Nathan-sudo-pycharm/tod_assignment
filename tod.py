import unittest

# Available art objects in the vending machine
ARTWORKS = {
    "1": {"name": "Silver Pendant", "price": 7.55},
    "2": {"name": "Mini German Flag", "price": 12.00},
    "3": {"name": "Clay Sculpture", "price": 15.00},
    "4": {"name": "Fulda Fridge Magnet", "price": 5.50},
}

MAX_ITEMS = 3


def format_machine_display(user_inputs):
    if len(user_inputs) > MAX_ITEMS:
        return "Display Error: Maximum 3 items allowed per transaction"

    if not user_inputs:
        return "Machine Idle"

    names = [ARTWORKS[item_id]["name"] for item_id in user_inputs]
    total = sum(ARTWORKS[item_id]["price"] for item_id in user_inputs)

    return f"Items: {', '.join(names)} | Total: {total:.2f} EUR"


def show_demo():
    print()
    print("=== Vending machine display demo ===")
    print()
    for selection in (["1", "2"], ["1", "2", "3"], ["1", "2", "3", "4"]):
        print(f"Selected {selection}")
        print(f"  Display: {format_machine_display(selection)}")
        print()
    print("====================================")
    print()


class VendingDisplayTest(unittest.TestCase):

    # Test Case 1: Display must show an error when more than 3 items are selected
    def test_display_shows_limit_error(self):
        user_inputs = ["1", "2", "3", "4"]
        expected_display = "Display Error: Maximum 3 items allowed per transaction"

        self.assertEqual(format_machine_display(user_inputs), expected_display)

    # Test Case 2: Display must show selected item names and the total price
    def test_display_shows_total_and_items(self):
        user_inputs = ["1", "2"]
        expected_display = "Items: Silver Pendant, Mini German Flag | Total: 19.55 EUR"

        self.assertEqual(format_machine_display(user_inputs), expected_display)


if __name__ == "__main__":
    show_demo()
    unittest.main(verbosity=2)