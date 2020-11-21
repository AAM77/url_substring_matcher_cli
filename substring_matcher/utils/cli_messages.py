def display_farewell_message():
    print("\n**********************************************")
    print("* Thank you for using the Substring Matcher! *")
    print("* Goodbye!                                   *")
    print("**********************************************\n")


def display_incorrect_response_alert():
    """
    Displays a message when the user selects and
    invalid choice.
    """
    print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!! Please enter a valid choice.                     !!')
    print("!! Or, enter 'exit' or 'quit' to close the program. !!")
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')


def display_menu_options_for_keyword_source():
    """
    Displays a small menu with options related to how
    the user wants to provide the list of keywords.
    """
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nPlease choose how you want to supply the keywords:')
    print('[1] Use the default keywords.txt file.')
    print('[2] Provide a list of keywords.')
    print("\nHint: Enter '1' or '2'.")


def display_menu_options_for_url_source():
    """Displays options for the URL menu"""
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nPlease choose how you want to supply the URLs:')
    print('[1] Use the default urls.txt file.')
    print('[2] Provide a list of urls.')
    print("\nHint: Enter '1' or '2'.")


def display_welcome_message():
    """Displays a welcome message and warning. """

    print('#####################################')
    print('#                                   #')
    print('# WELCOME TO THE SUBSTRING MATCHER! #')
    print('#                                   #')
    print('#####################################\n')
    print('\nThis is an application that helps you determine if a URL contains keywords you are interested in.\n')
    print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!!                                                                               !!')
    print('!! ATTENTION: Please read the README.md for instructions on how to use this CLI. !!')
    print('!!                                                                               !!')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
    print('--------------------------------------\n')
