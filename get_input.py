import os
from pathlib import Path
import urllib.request
from urllib.request import urlopen

repo_path = Path(__file__).parent

year = 2020
day = 7
url = "http://adventofcode.com/{}/day/{}/input".format(year, day)
# Cookie for your login info. Each user gets a special series if input data.
session_id = "53616c7465645f5fb33ae07a0f3e46d59dff717f575af35290b79ec3443771cae3f1b989fe852e399896fdb4e8f954b0"
session_id = "53616c7465645f5f2ee10a06bd5c341d4ed52cb913321a608b4de7223122f2f743633271cbbf2039749f30cbfa99f2f7"

url_req = urllib.request.Request(url)
# Add the session id to the request
url_req.add_header(key="Cookie", val="session={}".format(session_id))
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
if not answer_file.exists():
    answer_file.write_text(answer_temp.read_text())

