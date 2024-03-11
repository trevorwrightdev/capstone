from read_csv import read_csv
from algorithm import logistic_regression
from output import output

# read the csv file and get a list of dictionaries 
listings = read_csv('dataset.csv')

def main():
    # call the logistic_regression function and pass the dataset
    [word_scores, sorted_scores] = logistic_regression(listings)

    while True:
        output('blue', '<----------------------------------------->')
        output('magenta', 'AIRBNB KEYWORD ANALYSIS TOOL')
        output('green', '1. See the top keywords for listing titles')
        output('green', '2. Search for a specific keyword')
        output('blue', '<----------------------------------------->')

        choice = input('Input: ')

        if choice == '1':
            output('blue', '<----------------------------------------->')
            output('magenta', 'TOP KEYWORDS FOR LISTING TITLES')
            for word in sorted_scores[:100]:
                # ANSI escape code for green and to reset the color
                green = "\033[92m"
                reset = "\033[0m"
                
                # Constructing the string with 'word' in default color and 'score' in green
                word_score_str = f"{word['word']}: {green}{word['score']}{reset}"
                
                # Using the output function to print with magenta as a placeholder color
                # Since we are manually handling color codes here, the color passed to output is not used for the word and score
                print(word_score_str)
            output('blue', '<----------------------------------------->')


main()