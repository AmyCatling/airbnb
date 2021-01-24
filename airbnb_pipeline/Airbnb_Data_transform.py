import csv
import ast
import pandas as pd


class Airbnb:

    def __init__(self, listing_file, review_file):
        self.server = 'localhost,1433'
        self.database = 'Airbnb'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.listings_data = []
        self.reviews_data = []
        data = open(listing_file, encoding='utf-8')
        listing = csv.reader(data, delimiter=",")
        for line in listing:
            self.listings_data.append(line)
        data2 = open(listing_file, encoding='utf-8')
        reviews = csv.reader(data2, delimiter=',')
        for line in reviews:
            self.reviews_data.append(line)

    def transform_amenity(self):
        amenity_data = []
        amenity_index = self.listings_data[0].index('amenities')
        for listing in self.listings_data[1:]:
            amenity_data.append(listing[amenity_index])

        amenities = []
        for amenity_list in amenity_data:
            amenity_list = ast.literal_eval(amenity_list)
            for amenity in amenity_list:
                if amenity not in amenities:
                    amenities.append(amenity)
        self.amenities_df = pd.DataFrame(amenities)
        print(self.amenities_df)

    def _pull_amenity(self):

    def transform_locations(self):
        pass

    def _check_db_locations(self):
        pass

    def transform_reviewers(self):
        pass

    def _check_db_reviewers(self):
        pass

    def transform_hosts(self):
        pass

    def _check_db_hosts(self):
        pass

    def transform_reviews(self):
        pass

    def _check_db_reviews(self):
        pass


    def transform_listings(self):
        pass


    def _check_db_listings(self):
        pass


    def transform_list_amen_junction(self):
        pass


    def _check_db_list_amen_junction(self):
        pass


a = Airbnb('edinburgh_listings.csv', 'edinburgh_reviews.csv')

a.transform_amenity()