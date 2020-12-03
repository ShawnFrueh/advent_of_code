import os
from pathlib import Path
import urllib.request
from urllib.request import urlopen

repo_path = Path(__file__).parent

year = 2015
day = 4
url = "http://adventofcode.com/{}/day/{}/input".format(year, day)
# Cookie for your login info. Each user gets a special series if input data.
session_id = "53616c7465645f5f2ee10a06bd5c341d4ed52cb913321a608b4de7223122f2f743633271cbbf2039749f30cbfa99f2f7"

url_req = urllib.request.Request(url)
# Add the session id to the request
url_req.add_header(key='Cookie', val='session={}'.format(session_id))
# Open the URL
response = urlopen(url_req)

# Get the path for the input data.
input_path = repo_path / str(year) / f"day_{day:02}"
input_file = input_path / "input.txt"
answer_file = input_path / "answer.py"
answer_temp = repo_path / "answer_temp.py"

# Make sure directory exists
os.makedirs(input_path, exist_ok=True)

# Write out the input data.
input_file.write_text(response.read().decode("utf-8"))
# Create the default answer python file.
answer_file.write_text(answer_temp.read_text())
