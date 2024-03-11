from read_csv import read_csv
from algorithm import logistic_regression
from output import output

# read the csv file and get a list of dictionaries 
listings = read_csv('dataset.csv')

def main():
    # call the logistic_regression function and pass the dataset
    [word_scores, sorted_scores] = logistic_regression(listings)
    print(sorted_scores[:100])

    while True:
        output('blue', '<----------------------------------------->')
        output('magenta', 'AIRBNB KEYWORD ANALYSIS TOOL')
        output('green', '1. See the top keywords for listing titles')
        output('green', '2. Search for a specific keyword')
        output('blue', '<----------------------------------------->')

        choice = input()


main()