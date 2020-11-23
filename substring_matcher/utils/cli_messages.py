# I alphabetized the functions in this file since
# they simply handle displaying messages. Also, functions
# with similar messages share the same naming pattern,
# so they are likely to be grouped together, anyway.

def display_confirmation_message_for_keywords(valid_keywords, invalid_keywords):
    display_confirmation_message_for_invalid_keywords(invalid_keywords)
    print("\nCONTINUE?----------CONTINUE?----------CONTINUE?----------CONTINUE?\n")
    print(f"Do you want to use {valid_keywords} as your keywords?")
    print("Enter 'yes' (y) to continue or 'no' (n) to re-enter the keywords.")
    print("\nCONTINUE?----------CONTINUE?----------CONTINUE?----------CONTINUE?\n")
    display_reminder_for_exiting_the_application()


def display_confirmation_message_for_invalid_keywords(invalid_keywords):
    if invalid_keywords:
        print(
            "\nFOUND-INVALID-KEYWORDS------------------------------FOUND-INVALID-KEYWORDS\n")
        print(f"\nYou entered these invalid keywords: {invalid_keywords}")
        print(
            "\nFOUND-INVALID-KEYWORDS------------------------------FOUND-INVALID-KEYWORDS\n")


def display_confirmation_message_for_urls(urls):
    print("\nCONTINUE?----------CONTINUE?----------CONTINUE?----------CONTINUE?\n")
    print(f"Do you want to use {urls} as your URLs?")
    print("Enter 'yes' (y) to continue or 'no' (n) to re-enter the URLs.")
    print("\nCONTINUE?----------CONTINUE?----------CONTINUE?----------CONTINUE?\n")
    display_reminder_for_exiting_the_application()


def display_farewell_message():
    print("\n**********************************************")
    print("* Thank you for using the Substring Matcher! *")
    print("* Goodbye!                                   *")
    print("**********************************************\n")


def display_help_tips_for_keyword_input():
    print("\nEnter keywords separated by pipes (i.e. ' | ' ).")
    print("Only letters, hyphens, and underscores. Case does not matter.")
    print("Example 1: Hello|Hi|welcome-home|what_is_up")
    print("Example 2: Hello | Hi | welcome | what_is_up")
    print("NOTE: Whitespace (e.g. spaces) gets stripped from the beginning and end of each keyword.\n")


def display_help_tips_for_url_input():
    print("\nEnter URLs separated by pipes (i.e. ' | ' ).")
    print("This version of the CLI ignores case, since we are trying to match keywords.")
    print("Example 1: http://Hello.com|Hi.net|www.welcome.com")
    print("Example 2: http://Hello.com | Hi.net | www.welcome.com")
    print("NOTE: Whitespace (e.g. spaces) gets stripped from the beginning and end of each URL.\n")
    print("DISCLAIMER: It is your responsibility to provide URLs with valid characters.\n")


def display_incorrect_response_alert():
    """
    Displays a message when the user selects and
    invalid choice.
    """
    print("\n!!!!!!!!!!!!-INVALID-SELECTION-!!!!!!!!!!!!!!-INVALID-SELECTION-!!!!!!!!!!!!")
    print("!!                                                                          !!")
    print("!!                       Please enter a valid choice.                       !!")
    print("!!             Or, enter 'exit' or 'quit' to close the program.             !!")
    print("!!                                                                          !!")
    print("!!!!!!!!!!!!-INVALID-SELECTION-!!!!!!!!!!!!!!-INVALID-SELECTION-!!!!!!!!!!!!\n")
    user_input = input("Press the 'Enter' or 'Return' key to continue.")


def display_invalid_keyword_info(number_of_invalid_keywords: int, invalid_keywords: list):
    print("\n!!!!!!!!!-FOUND-INVALID-KEYWORDS-!!!!!!!!!!!!!!!!!!-FOUND-INVALID-KEYWORDS-!!!!!!!!!")
    print("!!")
    print(f"!! Found {number_of_invalid_keywords} invalid keyword(s)!")
    print("!!")
    print(f"!! {invalid_keywords}")
    print("!!")
    print("!! They will be ignored during the matching process.")
    print("!!")
    print("!!!!!!!!!-FOUND-INVALID-KEYWORDS-!!!!!!!!!!!!!!!!!!-FOUND-INVALID-KEYWORDS-!!!!!!!!!\n")


def display_menu_options_for_keyword_source():
    """
    Displays a small menu with options related to how
    the user wants to provide the list of keywords.
    """
    print("\nSUPPLY-KEYWORDS----------KEYWORDS----------KEYWORDS----------SUPPLY-KEYWORDS\n")
    print("Please choose how you want to supply the keywords:")
    print("[1] Use the default keywords.txt file.")
    print("[2] Provide a list of keywords.")
    print("\nHint: Enter '1' or '2'.")
    print("\nSUPPLY-KEYWORDS----------KEYWORDS----------KEYWORDS----------SUPPLY-KEYWORDS\n")


def display_menu_options_for_url_source():
    """Displays options for the URL menu"""
    print("\nSUPPLY-URLS----------URLS----------URLS----------URLS----------SUPPLY-URLS\n")
    print("Please choose how you want to supply the URLs:")
    print("[1] Use the default urls.txt file.")
    print("[2] Provide a list of urls.")
    print("\nHint: Enter '1' or '2'.")
    print("\nSUPPLY-URLS----------URLS----------URLS----------URLS----------SUPPLY-URLS\n")


def display_options_for_starting_over():
    print("\nSTART-OVER?----------START-OVER?----------START-OVER?----------START-OVER?\n")
    print("Do you want to:")
    print("[1] Start from the beginning")
    print("[2] Provide different URLs")
    print("\nSTART-OVER?----------START-OVER?----------START-OVER?----------START-OVER?\n")


def display_ready_message_for_finding_keywords_in_url():
    print("\nREADY----------READY----------READY----------READY----------READY")
    print("\nYou are now ready to search URLs for keywords.")
    print("\nREADY----------READY----------READY----------READY----------READY\n")
    user_input = input("Press the 'Enter' or 'Return' key to continue.")


def display_reminder_for_exiting_the_application():
    print(">>> Reminder: Enter 'exit' or 'quit' to exit the program. <<<")


def display_search_completion_notification():
    print("DONE! Here are your results:")
    print("\n<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>")


def display_search_results_summary(total_number_of_urls: int, number_of_urls_with_matches: int):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("SEARCH RESULT SUMMARY\n")
    print(f"Total number of urls: {total_number_of_urls}")
    print(f"URLs with Matching Keywords: {number_of_urls_with_matches}")
    print(
        ">> See the 'results' directory in 'substring_matcher' for result details. <<")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    user_input = input("Press the 'Enter' or 'Return' key to continue.")


def display_url_keyword_match_data_in_file(url, matches, runtime):
    print("\n######################################")
    print(f"URL: {url}")
    print("\nMATCHING KEYWORDS:")
    print(matches)
    print(f"\nRuntime: {runtime}")
    print("\n######################################")
    print("\n-----------------------------------------------------------------\n")


def display_waiting_message_during_keyword_matching():
    print("\nSEARCHING----------SEARCHING----------SEARCHING----------SEARCHING")
    print("\nOne moment while we search the URLs for keyword matches...\n")
    print("\nSEARCHING----------SEARCHING----------SEARCHING----------SEARCHING\n")


def display_waiting_message_while_building_trie():
    print("\nBUILDING----------BUILDING----------BUILDING----------BUILDING")
    print("\nOne moment while we get everything ready for your search...\n")
    print("\nBUILDING----------BUILDING----------BUILDING----------BUILDING\n")


def display_warning_to_request_more_urls():
    print("\n!!!!!!!!!!!!-ERROR-!!!!!!!!!!!!-ERROR-!!!!!!!!!!!!")
    print("!!                                              !!")
    print("!!      You must provide at least one URL.      !!")
    print("!!                                              !!")
    print("!!!!!!!!!!!!-ERROR-!!!!!!!!!!!!-ERROR-!!!!!!!!!!!!\n")


def display_warning_to_request_more_keywords():
    print("\n!!!!!!!!!!!!-ERROR-!!!!!!!!!!!!-ERROR-!!!!!!!!!!!!")
    print("!!                                              !!")
    print("!!    You must provide at least one keyword.    !!")
    print("!!                                              !!")
    print("!!!!!!!!!!!!-ERROR-!!!!!!!!!!!!-ERROR-!!!!!!!!!!!!\n")


def display_welcome_message():
    """Displays a welcome message and warning. """

    print("#########################################")
    print("#                                       #")
    print("# WELCOME TO THE URL SUBSTRING MATCHER! #")
    print("#                                       #")
    print("#########################################\n")
    print("\nThis is an application that helps you determine if a URL contains keywords you are interested in.\n")
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!!                                                                               !!")
    print("!! ATTENTION: Please read the README.md for instructions on how to use this CLI. !!")
    print("!!                                                                               !!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    print("--------------------------------------\n")
