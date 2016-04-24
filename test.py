import json, fnmatch, os

matches = []
for root, dirnames, filenames in os.walk('.'):
    for filename in fnmatch.filter(filenames, '*.json'):
        matches.append(os.path.join(root, filename))

for filename in matches:
  with open(filename) as data_file:
    data = json.load(data_file)
