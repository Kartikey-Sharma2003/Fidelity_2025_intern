import json

class JSONDifference:
    def __init__(self, json1, json2):  
        if isinstance(json1, str):
            self.json1 = json.loads(json1)
        else:
            self.json1 = json1

        if isinstance(json2, str):
            self.json2 = json.loads(json2)
        else:
            self.json2 = json2

    def get_difference(self):
        diff = {}
        all_keys = set(self.json1.keys()).union(set(self.json2.keys()))

        for key in all_keys:
            if self.json1.get(key) != self.json2.get(key):
                diff[key] = {'json1': self.json1.get(key), 'json2': self.json2.get(key)}

        return diff

json1 = {"name": "kartikey", "age": 21, "city": "spain"}
json2 = {"name": "drakster", "marks": 45, "country": "berlin"}

diff_checker = JSONDifference(json1, json2)

print(diff_checker.get_difference())
