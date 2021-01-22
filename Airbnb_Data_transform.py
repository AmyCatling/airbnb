import csv


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
            self.listings.append(line)
        data2 = open(listing_file, encoding='utf-8')
        reviews = csv.reader(data2, delimiter=',')
        for line in reviews:
            self.reviews_data.append(line)




    def transform_amenity(self):
        pass


    def _check_db_amenity(self):
        pass


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
