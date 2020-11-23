def display_confirmation_message_for_keywords(keywords):
    print(f'\nAre {keywords} the keywords you entered? (y/n)')


def display_confirmation_message_for_urls(urls):
    print(f'\nAre {urls} the urls you entered? (y/n)')


def display_farewell_message():
    print("\n**********************************************")
    print("* Thank you for using the Substring Matcher! *")
    print("* Goodbye!                                   *")
    print("**********************************************\n")


def display_help_tips_for_keyword_input():
    print("\nEnter keywords separated by pipes (i.e. ' | ' ).")
    print("Example 1: Hello|Hi|welcome")
    print("Example 2: Hello | Hi | welcome")
    print("NOTE: Whitespace (e.g. spaces) will get stripped out since they do not belong in a url.\n")


def display_help_tips_for_url_input():
    print("\nEnter URLs separated by pipes (i.e. ' | ' ).")
    print("Example 1: http://Hello.com|Hi.net|www.welcome.com")
    print("Example 2: http://Hello.com | Hi.net | www.welcome.com")
    print("NOTE: Whitespace (e.g. spaces) will get stripped out since they do not belong in a url.\n")


def display_incorrect_response_alert():
    """
    Displays a message when the user selects and
    invalid choice.
    """
    print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!! Please enter a valid choice.                     !!')
    print("!! Or, enter 'exit' or 'quit' to close the program. !!")
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')


def display_invalid_keyword_info(number_of_invalid_keywords: int, invalid_keywords: list):
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"!! Found {number_of_invalid_keywords} invalid keyword(s)!")
    print("!!")
    print(f"!! {invalid_keywords}")
    print("!!")
    print("!! They will be ignored during the matching process.")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


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


def display_options_for_starting_over():
    print("Do you want to:")
    print("[1] Start from the beginning")
    print("[2] Provide different URLs")


def display_ready_message_for_finding_keywords_in_url():
    print('\nYou are now ready to search URLs for keywords.')


def display_reminder_for_exiting_the_application():
    print(">>> Reminder: Enter 'exit' or 'quit' to exit the program. <<<")


def display_search_completion_notification():
    print("DONE! Here are your results:")
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def display_search_results_summary(total_number_of_urls: int, number_of_urls_with_matches: int):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Total number of urls: {total_number_of_urls}")
    print(f"URLs with Matching Keywords: {number_of_urls_with_matches}")
    print(
        ">> See the 'results' directory in 'substring_matcher' for result details. <<")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def display_url_keyword_match_data_in_file(url, matches, runtime):
    print("\n######################################")
    print("######################################\n")
    print(f"URL: {url}")
    print("\nMATCHING KEYWORDS:")
    print(matches)
    print(f"\nRuntime: {runtime} milliseconds")
    print("\n######################################")
    print("######################################\n")
    print("\n")


def display_waiting_message_during_keyword_matching():
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("\nOne moment while we search the URLs for keyword matches...")


def display_waiting_message_while_building_trie():
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nOne moment while we get everything ready for your search...')


def display_warning_to_request_more_urls():
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!! You must provide at least one URL. !!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")


def display_warning_to_request_more_keywords():
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!! You must provide at least one keyword. !!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")


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
