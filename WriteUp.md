
# Rationale for Features

### Simple Features
These were naive features that were found by iterating over every
transaction and just making note of the amount and keeping track of
the vendor.
* salary: average sum of positive transactions per year
* spending: average sum of negative transactions per year
* Based on vendors to which the most money was spent
    * first_top_purchase
    * second_top_purchase
    * third_top_purchase

### vendor based features
These feature were found based on the specific names of the vendors.
More details on how this was done can be found in the comments here:
[vendor_based_feartures.py](intuitRitChallenge/vendor_based_feartures.py)
has_child
is_sports_fan
was_recently_divorced
favorite_restaurant

### Rational For MatchMaker
This algorithm was based on the distinct features and determines a score
between 0-1 that represents the confidence of compatibility between any two individuals.
This algorithm can be found in [views.py](intuitRitChallenge/views.py). It basically
goes through all of the transactions from both of the given users and determine
how similar the amount of money is spent at each vendor, then factors in the
likelyhood that they both shop at that vendor.