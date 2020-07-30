# Geocoding Code
# Also I would recommend looking into the google geocoding API
# as google gives free $300 credit and has a python client that's
# easy(ish) to use. Here's link:
# https://github.com/googlemaps/google-maps-services-python

# Needed modules for geocoder
# Probably will need to conda install or pip install some?
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut

# geocoding information
geolocator = Nominatim(user_agent="myGeocoder") #Change name for project
geocode = RateLimiter(geolocator.geocode, min_delay_seconds = 1)

# Input: df with column "Address" with addresses 
# Format ex: 209 Exchange St Chicopee, MA 1013 USA
# Cannot handle certain addresses 
# Format ex: 16 N Day St # 26 Orange, NJ 7050 USA
# Output: df with column "Temp" with the address the geocoder used
# and column "Coordinates" with (lat,long,alt) coordinates
def geocoding(df):
    try:
        df["Temp"] = df["Address"].apply(geocode)
        df["Coordinates"] = df["Temp"].apply(
            lambda loc: tuple(loc.point) if loc else None)
    except GeocoderTimedOut as e:
        print("Error geocode failed with message %s" , e.message)

    return df #With NaNs

# Drops NaNs from df if desired and reads "Coordinate" column to
# 3 separate columns
def dropnans(df):
    
    print("Before dropping NaNs:", df.shape)
    df.dropna(inplace=True)
    print("After dropping NaNs:", df.shape)
    
    df[["Latitude", "Longitude", "Altitude"]] = pd.DataFrame(df['Coordinates'].tolist(), index=df.index)
    
    return df #No NaNs and coordinates in separate columns
