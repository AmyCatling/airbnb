import configparser

config = configparser.ConfigParser()
config.read('Table_config.ini')

Amenities = {}
Amenities['Amenity_ID'] = config['Amenities'].get('Amenity_ID')
Amenities['Amenity_name'] = config['Amenities'].get('Amenity_name')

List_amen_junction = {}
List_amen_junction['Listing_ID'] = config['List_amen_junction'].get('Listing_ID')
List_amen_junction['Amenity_ID'] = config['List_amen_junction'].get('Amenity_ID')

Locations = {}
Locations['Location_ID'] = config['Locations'].get('Location_ID')
Locations['neighbourhood'] = config['Locations'].get('neighbourhood')
Locations['Area'] = config['Locations'].get('Area')

Reviews = {}
Reviews['Review_ID'] = config['Reviews'].get('Review_ID')
Reviews['Reviewer_ID'] = config['Reviews'].get('Reviewer_ID')
Reviews['Location_ID'] = config['Reviews'].get('Location_ID')
Reviews['Comments'] = config['Reviews'].get('Comments')

Reviewers = {}
Reviewers['Reviewer_ID'] = config['Reviewers'].get('Reviewer_ID')
Reviewers['Name'] = config['Reviewers'].get('Name')

Hosts = {}
Hosts['Host_ID'] = config['Hosts'].get('Host_ID')
Hosts['Host_Name'] = config['Hosts'].get('Host_Name')
Hosts['Host_Since'] = config['Hosts'].get('Host_Since')
Hosts['Host_Location'] = config['Hosts'].get('Host_Location')
Hosts['Host_Response_Time'] = config['Hosts'].get('Host_Response_Time')
Hosts['Host_Response_Rate'] = config['Hosts'].get('Host_Response_Rate')
Hosts['Host_Acceptance_Rate'] = config['Hosts'].get('Host_Acceptance_Rate')
Hosts['Host_Is_Superhost'] = config['Hosts'].get('Host_Is_Superhost')
Hosts['Host_Listings_Count'] = config['Hosts'].get('Host_Listings_Count')
Hosts['Host_Total_Listings_Count'] = config['Hosts'].get('Host_Total_Listings_Count')

Listings = {}
Listings['Listing_ID'] = config['Listings'].get('Listing_ID')
Listings['Host_ID'] = config['Listings'].get('Host_ID')
Listings['Location_ID'] = config['Listings'].get('Location_ID')
Listings['Last_Scraped'] = config['Listings'].get('Last_Scraped')
Listings['Name'] = config['Listings'].get('Name')
Listings['Description'] = config['Listings'].get('Description')
Listings['Latitude'] = config['Listings'].get('Latitude')
Listings['Longitude'] = config['Listings'].get('Longitude')
Listings['Price'] = config['Listings'].get('Price')
Listings['Property_Type'] = config['Listings'].get('Property_Type')
Listings['Room_Type'] = config['Listings'].get('Room_Type')
Listings['Accommodates'] = config['Listings'].get('Accommodates')
Listings['Bedrooms'] = config['Listings'].get('Bedrooms')
Listings['Bathrooms'] = config['Listings'].get('Bathrooms')
Listings['Availability_30'] = config['Listings'].get('Availability_30')
Listings['Availability_60'] = config['Listings'].get('Availability_60')
Listings['Availability_90'] = config['Listings'].get('Availability_90')
Listings['Availability_365'] = config['Listings'].get('Availability_365')

# print(Amenities)
# print(List_amen_junction)
# print(Locations)
# print(Reviews)
# print(Reviewers)
# print(Hosts)
# print(Listings)
