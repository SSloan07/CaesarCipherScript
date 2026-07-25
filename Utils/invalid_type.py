def valid_type(message, valid_options=None, positive=False):
    while True:
        try:
            number = int(input(message))

            if valid_options is not None and number not in valid_options:
                print(f"Invalid option. Choose one of: {valid_options}")
                continue

            if positive and number <= 0:
                print("Invalid input. You must enter a positive integer.")
                continue

            return number

        except ValueError:
            print("Invalid input. You must enter an integer.")
