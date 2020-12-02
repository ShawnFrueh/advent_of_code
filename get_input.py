import os
import urllib.request
from urllib.request import urlopen

path = os.path.dirname(__file__)

year = 2020
day = 2
url = "http://adventofcode.com/{}/day/{}/input".format(year, day)
# Cookie for your login info. Each user gets a special series if input data.
session_id = "53616c7465645f5f2ee10a06bd5c341d4ed52cb913321a608b4de7223122f2f743633271cbbf2039749f30cbfa99f2f7"
session_id = "53616c7465645f5fe56e13fa2fbaa3f38f9d694265ac7d35bfb76517d601eb50a679b426c1584e9f7164a26b9ba00bb1"

url_req = urllib.request.Request(url)
# Add the session id to the request
url_req.add_header(key='Cookie', val='session={}'.format(session_id))
# Open the URL
response = urlopen(url_req)

# Get the path for the input data.
input_path = os.path.join(path, str(year), f"day_{day:02}")
input_file = os.path.join(input_path, "input.txt")
os.makedirs(input_path, exist_ok=True)

# Write out the input data.
with open(input_file, "w") as in_file:
    # Decode the response into string
    in_file.write(response.read().decode("utf-8"))

