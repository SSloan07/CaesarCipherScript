def valid_type(message, valid_options=None):
    while True:
        try:
            number = int(input(message))

            if valid_options is not None and number not in valid_options:
                print(f"Invalid option. Choose one of: {valid_options}")
                continue

            return number

        except ValueError:
            print("Invalid input. You must enter an integer.")