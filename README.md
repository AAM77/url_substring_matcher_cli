# URL Substring Matcher

## Installation

#### Using Git:
1. Using the command line, navigate to the directory where you want to store the repository. 
3. Clone the repository to that location.

#### Using a Zipped File:
1. If using a zip file, unzip it.
2. Place the unzipped directory in a desired location.

## Description
The core algorithm for this application is the URL substring matching algorithm. It helps users determine which keywords (of a list of keywords of their choosing) exist inside of each URL of one or more URLs. A user is able to utilize this algorithm by interacting with the Command Line Interface (CLI). This allows users to specify the keywords (i.e. substrings) and target URLs through the command line or specify them inside of files --- keywords.txt for keywords and urls.txt for URLs.

Once the algorithm has the keywords and URLs it needs to run, it displays each URL with a list of matching keywords in alphabetical order. Since the challenge did not provide much detail on what the output should be, I decided to output it in a manner that was more useful for humans.

The current algorithm can process a 2,200 character URL with 367,000 keywords in about 3 - 4 ms. It takes less time the shorter the URL gets (as low as .04ms for a relatively normal sized URL). If the URL gets very large (e.g. 11,000+ characters), however, it slows down and takes approximately 16 ms to process 367,000 keywords. The number of substrings/keywords can affect it, of course, but its impact is relatively minor compared to a URL's length, since the algorithm creates a Trie from the provided substrings/keywords before accepting URLs. We can optimize the algorithm further, but I felt this was unnecessary for the time-being. I requested clarification, but received little. As a result, I decided to make a decision based on my own research.

To elaborate further, it seems that most browsers can safely handle URLs up to an approximate size of 2000 +/- 100. Furthermore, it appears that the only kinds of URLs that would go past 2,000 characters are data URLs, but they are usually composed of random combinations of letters (i.e. incomprehensible gibberish). As such, encountering a URL of 2,200 characters seems like the more likely scenario one would encounter. Therefore, I  weighed the pros and cons, and feel relatively comfortable leaving the current version of the algorithm in its less efficient form --- a 3 to 4 ms is not a bad runtime for a URL with 2,200 characters and a keyword list of approximately 367,000 words.

One of the scenarios where a more optimal algorithm will become necessary is when comparing partial genetic (e.g. DNA, RNA) sequences against a much larger genetic sequence, but that is not what this challenge was about.
## How to use

### DO THIS FIRST
1. Before anything, you need to install Python 3.9 or higher (preferably in a virtual environment). 
2. Use the command line (terminal on a Mac OS) to navigate to the project's directory (i.e. ROCKERBOX CHALLENGE).
3. Use the command line to navigate to the 'substring_matcher' directory.
4. Once inside the 'ROCKERBOX_CHALLENGE/substring_matcher' directory, you have a couple of options:
   <br>a. run tests
   <br>b. interact with the URL substring matching script using the CLI.

<br>

### Assuming you are inside of the 'ROCKERBOX_CHALLENGE/substring_matcher' directory:

#### Running Tests:
If you want to run tests, type `python3 tests.py` and press the 'Enter' or Return key.

<br>

#### Running the Command Line Interface (CLI):
If you want to interact with the CLI, there are a few things you should set up before using it.

*NOTE: If you do not plan on using files for your keywords and URLs (i.e. you want to enter the keywords and URLs via the command line), you can skip steps (1) and (2).*
<br>
<br>

1. If you plan to use a file for your keywords, you need to add the keywords to the keywords.txt file.
   - From the project's root directory, navigate to the 'data' directory.
   - Open the 'keywords.txt' file and add your keywords there. Each keywords should be on a new line.
   - OR, if you want to use a text file you already have:
     1. Delete or rename the existing 'keywords.txt' inside of the 'ROCKERBOX_CHALLENGE/substring_matcher/data' directory
     2. Now, go to your file that contains the keywords you want to use.
     3. Convert your file to a text file (has a .txt extension), if it is not one already.
     4. Rename it to 'keywords.txt'.
     5. Move it to the 'ROCKERBOX_CHALLENGE/substring_matcher/data' directory.
     6. Make sure that all of the keywords (substrings) are on separate lines without single or double quotes around them.
   
2. If you plan to use a file for your URLs, you need to add the URLs to the keywords.txt file.
   - From the project's root directory, navigate to the 'data' directory.
   - Open the 'urls.txt' file and add your URLs there. Each URL should be on a new line.
   - OR, if you want to use a text file you already have:
     1. Delete or rename the existing 'urls.txt' inside of the 'ROCKERBOX_CHALLENGE/substring_matcher/data' directory
     2. Now, go to your file that contains the URLs you want to use.
     3. Convert your file to a text file (has a .txt extension), if it is not one already.
     4. Rename it to 'urls.txt.'
     5. Move it to the 'ROCKERBOX_CHALLENGE/substring_matcher/data' directory.
     6. Make sure that all of the URLs are on separate lines without single or double quotes around them.
   
3. Using the command line, make sure you are in the project's root directory.
4. Type `python3 substring_matcher_cli.py` and press the 'Enter' or 'Return' key.
5. This will display a welcome message.
6. Follow the instructions on the screen from here on out.

## Contributing

Bug reports and pull requests are welcome on GitHub at -URL-. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## Code of Conduct

Everyone interacting in the Url Substring Matcher project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/AAM77/rockerbox_challenge/blob/main/CODE_OF_CONDUCT.md).

## License
The Url Substring Matcher project has an AGPL-3.0 license. You may view the contents of the license at [license](https://github.com/AAM77/rockerbox_challenge/blob/main/LICENSE.md).
