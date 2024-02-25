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

    def get_input(self, userQuery):
        return input(userQuery)

    def get_inputs(self, userQueries):
        answers = []
        for userQuery in userQueries:
            answers.append(input(userQuery))
        return answers

    def get_password(self):
        return getpass("Enter your password: ")
    
    def print_dictionary(self, dictionary):
        print("\n")
        for key, value in dictionary.items():
            print(f"{key}: {value}")

    def get_int_input(self, userQuery):
        try:
            user_input = int(input(userQuery))
            return user_input
        except Exception as e:
            if isinstance(e, ValueError) or isinstance(e, TypeError):
                print("Please enter only numbers.")
                return self.get_int_input(userQuery)
            else:
                print(e)
    
    def print_error(self, error):
        print(f"{error}")
        input()