import json

with open('testazure.json') as f:
  data = json.load(f)
  for i, x in enumerate(data):
    with open(str(i) + '.json', 'w') as f_out:
      json.dump(x, f_out)
