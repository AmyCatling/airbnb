from server_config import Server
from Airbnb_Data_transform import Airbnb


data_insert = Airbnb('edinburgh_listings.csv', 'edinburgh_reviews.csv', Server)