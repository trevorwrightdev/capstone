from collections import defaultdict
import re

# the minimum amount of times a word must appear in the dataset to be considered
minimum_word_quantity = 100

def logistic_regression(listings):
    word_to_reviews_per_month = defaultdict(list)
    # iterate through the listings
    for listing in listings:
        reviews_per_month = listing['reviews per month']

        # if reviews per month does not exist, skip this listing
        if not reviews_per_month:
            continue

        # convert the string to a float
        reviews_per_month = float(reviews_per_month)

        title = listing['NAME'].lower()

        # Split the string based on non-letter characters
        words = re.findall(r'\b[a-zA-Z]+\b', title)
        # iterate through the words
        for word in words:
            word_to_reviews_per_month[word].append(reviews_per_month)
        
    # calculate the average reviews per month for each word
    word_scores = {}
    highest_avg_reviews_per_month = 0
    for word, reviews in word_to_reviews_per_month.items():
        # if the word appears less than the minimum amount of times, skip it
        if len(reviews) < minimum_word_quantity:
            continue
        # calculate the average reviews per month for the word
        average_reviews_per_month = sum(reviews) / len(reviews)

        # if the average reviews per month is the highest so far, update the variable
        if average_reviews_per_month > highest_avg_reviews_per_month:
            highest_avg_reviews_per_month = average_reviews_per_month

        score = (average_reviews_per_month / highest_avg_reviews_per_month) * 10
        word_scores[word] = round(score, 2)

    # Convert dictionary to a list of dictionaries with 'word' and 'score' keys
    word_list = [{"word": word, "score": score} for word, score in word_scores.items()]

    # Sort the list by 'score' in descending order
    word_list_sorted = sorted(word_list, key=lambda x: x['score'], reverse=True)
    
    return [word_scores, word_list_sorted]