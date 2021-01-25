from table_config import Amenities, Listings, Reviews, Reviewers, Hosts, Locations, List_amen_junction
from server_config import Server
from Table_creation import *
from Airbnb_Data_transform import Airbnb

amenity_table = Table_create('Amenities', Amenities, Server)

Locations_table = Table_create('Locations', Locations, Server)

reviewers_table = Table_create('Reviewers', Reviewers, Server)

hosts_table = Table_create('Hosts', Hosts, Server)

reviews_table = Table_create('Reviews', Reviews, Server)

list_amen_junction = Table_create('Listing_Amenities', List_amen_junction, Server)

listings_table = Table_create('Listings', Listings, Server)



