from collections import defaultdict

def logistic_regression(listings):
    # ! TESTING ONLY
    listings = listings[:10]
    # !

    word_to_reviews_per_month = defaultdict(list)
    # iterate through the listings
    for listing in listings:
        title = listing['NAME']