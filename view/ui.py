from getpass import getpass

class ui:

    def print_header(self, title):
        width = 46  # Width of the banner
        print("\n" + "*" * width)
        print(f"*{title.center(width - 2)}*")
        print("*" * width)

    def print_options(self, options):
        print("\n")
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")

    def get_choice(self, maxOptions):
        selectedOption = None
        while (selectedOption is None):
            choice = input("Enter Choice:")
            try:
                if int(choice) in [x for x in range(1,maxOptions+1)]:
                    selectedOption = int(choice)
                else:
                    print("Invalid choice. Please selected from the available options.")
                    selectedOption = None
            except Exception as e:
                print("Invalid choice. Please try again")
                selectedOption = None

        return selectedOption


    def get_inputs(self, userQueries):
        answers = []
        for userQuery in userQueries:
            answers.append(input(userQuery))
        return answers

    def get_password(self):
        return getpass("Enter your password: ")