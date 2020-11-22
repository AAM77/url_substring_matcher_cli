# URL Substring Matcher

## Author:
### Mohammad Adeel
#### First version released on November 22, 2020

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
## HOW TO USE

**CAUTION**: These Instructions are for a Mac OS only.

#### Users can interact with this project in two ways:
<br>(1) By using the executable version (a directory with an executable file)
<br>(2) By using the development version (the raw code)

### **EXECUTABLE VERSION (DISTRIBUTABLE)**
This requires less work to setup, but it limits what users can or cannot do. The executable version can be found inside the 'dist' directory, which is located inside of the project's root directory. 'Dist' stands for distributable. It contains another directory called 'cli.' This contains a number of scary looking files, but also one file named 'cli.' This is the executable file you will use to launch the script for finding keyword matches in URLs.

To use it:
1. Double click on the file named **cli**, located in the 'ROCKERBOX_CHALLENGE/dist/cli' directory.
2. It will launch the terminal (the command line on Mac OS).
3. Once it presents the welcome message, press the 'Enter' or 'Return' key.
4. The first set of options will ask you if you want to provide the keywords (substrings) using a file or if you want to enter them into the command line, separated by the pipe (' | ') character.
5. If you want to use a file, then navigate to the 'ROCKERBOX_CHALLENGE/dist/cli' directory and open the 'substring_matcher' directory. Then, open the 'data' directory.
6. Open the 'keywords.txt' and replace the text with the keywords you want to use.
   - Make sure they are on separate lines without single or double quotes around them.
   - If you want to use your own file, then rename or delete the 'keywords.txt' in this directory.
   - Then convert your file to a plain text file with the .txt extension and rename it to 'keywords.txt.'
   - You still need to make sure that your keywords are all on separate lines.
   - ***Note:*** *You can modify the keywords.txt file while the script is waiting for you to select and option (i.e. you do not need to restart it).*
7. Once you are done with that step, the CLI will ask you if you want to use a text file for your list of URLs or if you want to enter them manually.
8. Steps (4), (5), and (6) apply for the URLs as well, so you can follow those. Just make sure you are editing or replacing the 'urls.txt' file inside of the 'ROCKERBOX_CHALLENGE/dist/cli/substring_matcher/data' directory.
9.  Once you complete that step, the keyword (substring) matching algorithm will run and it will display a summary of how many URLs there were and how many had matching keywords.
    - For more details, navigate to the 'results' directory, located at ROCKERBOX_CHALLENGE/dist/cli/substring_matcher.'
    - You have the option of viewing the JSON format, which provides a compact view of the URLs, their matching keywords (substrings) --- if any --- and the runtime (how many milliseconds it took to find matching keywords).
    - The text displays the same information. It's just bulkier because of the extra styling.

    - ***Note:*** *Each run, will replace these files, so move them somewhere else or rename them if you want to run the algorithm more than once (you don't have to stop the CLI to move the result files).*

10. Afterwards, the CLI will give the option of starting from the beginning, entering new URLs while using the same keywords, or exiting/quitting. Starting over allows you to change the keywords you want to use (but, if you chose to use the keywords.txt file, you can just modify that without starting over).




### **DEVELOPMENTAL VERSION (RAW CODE)**
This requires the most amount of work, but also offers you more control.

### DO THIS FIRST
1. You should start up a virtual environment.
2. Next, you need to install Python 3.9.0 or higher.
   - Download Link for Mac OS: [Python 3.9.0 for Mac OS](https://www.python.org/downloads/)
   - Download Link for Windows: [Python 3.9.0 for Windows](https://www.python.org/downloads/windows/)
   - Download Link for Linux: [Python 3.9.0 for Linux/UNIX](https://www.python.org/downloads/)
3. Use the command line (terminal on a Mac OS) to navigate to the project's directory (i.e. ROCKERBOX CHALLENGE).
4. Once inside the 'ROCKERBOX_CHALLENGE' directory, you have a few options:
   <br>a. Run tests
   <br>b. Get average runtimes for 1000 runs of the algorithm using varying URL sizes with approximately 369,000 keywords.
   <br>c. Interact with the URL substring matching script using the CLI.

<br>

### Assuming you are inside of the 'ROCKERBOX_CHALLENGE' directory (the project's root directory):

#### Running Tests:
If you want to run tests, remain in the root directory and type `python3.9 tests.py` into the command line. Then, press the 'Enter' or Return key to run the tests.

<br>

#### Getting Average Runtimes:
If you want to get the average run times in milliseconds (ms), remain in the root directory and type `python3.9 determine_average_runtimes.py` into the command line. Then press the 'Enter' or Return key and wait. It will take a few moments to finish running.

##### This will run the algorithm 1000 times while using 369,985 keywords to match against URLs for four different URL lengths:

1. Short URL: 22 characters long.
2. Medium URL: 283 characters long.
3. Long URL: 2,511 characters long.
4. Super Long URL: 11,778 characters long.

You can find them inside of the 'constants.py' file of the 'substring_matcher' directory.

##### My own tests on a Mid-2012 Macbook Pro with 8 GB RAM and a 2.3 Ghz i7 Quad Core processor while under heavy load revealed average runtimes in the range of the following (out of multiple sets of 1000 runs):

1. Short URL: 0.045 ms - 0.052 ms
2. Medium URL: 0.55 ms - 0.65 ms
3. Long URL: 3.63 ms - 4.25 ms
4. Super Long URL: 14.71 ms - 16.96 ms


##### To change the number of times the algorithm runs, open the constants.py file inside of ROCKERBOX_CHALLENGE/substring_matcher and change the NUMBER_OF_DESIRED_RUNS value to whatever you like (e.g. 100000).
<br>

#### Running the Command Line Interface (CLI):
If you want to interact with the CLI and you want to use files to supply your keywords and URLs, you should take a moment to set up the relevant files before using it. Steps (1) and (2) cover how to do this.

*NOTE: If you do not plan on using files for your keywords and URLs (i.e. you want to enter the keywords and URLs via the command line), you can skip steps (1) and (2).*
<br>
<br>

1. If you plan to use a file for your keywords, you need to add the keywords to the 'keywords.txt' file. If not, then skip this step.
   - From the project's root directory, navigate to the 'data' directory.
   - Open the 'keywords.txt' file and add your keywords there. Each keyword should be on a new line.
   - OR, if you want to use a text file you already have:
     1. Delete or rename the existing 'keywords.txt' inside of the 'ROCKERBOX_CHALLENGE/substring_matcher/data' directory.
     2. Now, go to your file that contains the keywords you want to use.
     3. Convert your file to a plain text file (has a .txt extension), if it is not one already.
     4. Make sure you add the '.txt' extension to it.
     5. Make sure that all of the keywords (substrings) are on separate lines without single or double quotes around them.
     6. Now, move your file to the 'ROCKERBOX_CHALLENGE/substring_matcher/data' directory.
     7. Rename it to 'keywords.txt'.
     8. ***NOTE:*** *As an alternative to steps (6), you can edit the value for the DEFAULT_KEYWORDS_FILE constant in 'substring_matcher/constants.py' by changing it to the name of your file. It must still be a text file with the .txt extension, however.*
   
2. If you plan to use a file for your URLs, you need to add the URLs to the keywords.txt file. If not, then skip this step.
   - From the project's root directory, navigate to the 'data' directory.
   - Open the 'urls.txt' file and add your URLs there. Each URL should be on a new line.
   - OR, if you want to use a text file you already have:
     1. Delete or rename the existing 'urls.txt' inside of the 'ROCKERBOX_CHALLENGE/substring_matcher/data' directory
     2. Now, go to your file that contains the URLs you want to use.
     3. Convert your file to a text file (has a .txt extension), if it is not one already.
     4. Make sure that all of the URLs are on separate lines without single or double quotes around them.
     5. Move it to the 'ROCKERBOX_CHALLENGE/substring_matcher/data' directory.
     6. Rename it to 'urls.txt.'
     7. ***NOTE:*** *As an alternative to steps (6), you can change the value for the DEFAULT_URLS_FILE constant in 'substring_matcher/constants.py' to be the name of your file. It must still be a text file with the .txt extension, however.*
   
3. Using the command line, make sure you are in the 'ROCKERBOX_CHALLENGE' (root) directory.
4. Type `python3.9 cli.py` into the command line and press the 'Enter' or 'Return' key.
5. This will display a welcome message.
6. Follow the instructions on the screen from here on out.
7. Once the keyword search finishes, the results will be sent as `.json` and `.txt` files to the 'results' directory inside of the 'substring_matcher' directory. Each run, will replace these files, so move them somewhere else or rename them if you want to run the algorithm more than once (you don't have to stop the CLI to move the result files).
8. Afterwards, the CLI will give the option of starting from the beginning, entering new URLs while using the same keywords, or exiting/quitting. Starting over allows you to change the keywords you want to use (but, if you chose to use the keywords.txt file, you can just modify that without starting over).

## Contributing

Bug reports and pull requests are welcome on GitHub at -URL-. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## Code of Conduct

Everyone interacting in the Url Substring Matcher project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/AAM77/rockerbox_challenge/blob/main/CODE_OF_CONDUCT.md).

## License
The Url Substring Matcher project has an AGPL-3.0 license. You may view the contents of the license at [license](https://github.com/AAM77/rockerbox_challenge/blob/main/LICENSE.md).

## Future Plans
1. Clean the code inside of the substring_matcher_cli.py file.
   - Since the individuals who requested this challenge did not seem to care about the CLI, I left the code that manages the CLI with some repetition.

2. Optimize the code further to use even less time than it does now.
   - The search/lookup for any single known keyword is O(n), but this is not the case for a URL with an unkown amount of unknown mixed and overlapping keywords.
   - Since the time complexity in a worst case scenario for iterating through the URL to match all possible keywords is O( n^2). I would like to get this down to O(n) or O(n * log(n)), if possible.

3. Provide users with the option to supply a unique file name or path for the file containing the keywords or URLs.
   
4. Provide unique names for the result files, add timestamps, and potentially move them to another folder when the program ends.

5. Validate URLs and keywords. I did not do it in this instance because the requirements did not ask for it. It's a simple addition.