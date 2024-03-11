from collections import defaultdict
import re

# the minimum amount of times a word must appear in the dataset to be considered
minimum_word_quantity = 1

def logistic_regression(listings):
    # ! TESTING ONLY
    listings = listings[:10]
    # !

    word_to_reviews_per_month = defaultdict(list)
    # iterate through the listings
    for listing in listings:
        reviews_per_month = listing['reviews per month']

        # if reviews per month does not exist, skip this listing
        if not reviews_per_month:
            continue

        title = listing['NAME']

        # Split the string based on non-letter characters
        words = [word.lower() for word in re.findall(r'\b[a-zA-Z]+\b', title)]
        # iterate through the words
        for word in words:
            word_to_reviews_per_month[word].append(float(reviews_per_month))
            pass
        
    # calculate the average reviews per month for each word
    word_scores = {}
    for word, reviews in word_to_reviews_per_month.items():
        # if the word appears less than the minimum amount of times, skip it
        if len(reviews) < minimum_word_quantity:
            continue
        word_scores[word] = sum(reviews) / len(reviews)
    
    return word_scores