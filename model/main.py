from read_csv import read_csv
from algorithm import logistic_regression
from output import output, capitalize

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
            count = len(sorted_scores)
            for word in sorted_scores:
                # ANSI escape code for green and to reset the color
                green = "\033[92m"
                yellow = "\033[93m"
                red = "\033[91m"
                magenta = "\033[35m"
                blue = "\033[94m"
                reset = "\033[0m"

                if word['score'] > 7:
                    color = green
                elif word['score'] > 5:
                    color = yellow
                elif word['score'] > 3:
                    color = magenta
                else:
                    color = red
                
                word_name = word['word']
                if word_name == 'cleaning':
                    word_name = 'no cleaning fee'
                elif word_name == 'entry':
                    word_name = 'private entry'
                
                # Constructing the string with 'word' in default color and 'score' in green
                word_score_str = f"{count} {blue}{capitalize(word_name)}{reset}: {color}{word['score']}{reset}"

                count -=1
                
                # Using the output function to print with magenta as a placeholder color
                # Since we are manually handling color codes here, the color passed to output is not used for the word and score
                print(word_score_str)
            output('blue', '<----------------------------------------->')
        elif choice == '2':
            keyword = input('Enter the keyword: ').lower()
            output('blue', '<----------------------------------------->')
            if keyword in word_scores:
                output('green', f'The score for "{capitalize(keyword)}" is {word_scores[keyword]}')
            else:
                output('red', f'The keyword "{capitalize(keyword)}" is not found in the dataset')
            output('blue', '<----------------------------------------->')

main()