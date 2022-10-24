import json

class Model:
    title = "title_val"
    text = "text_val"
    author = "author_val"

    def save(self):
        d = {}
        for attr in dir(Model):
            if attr == "save" or attr.startswith("_"):
                continue
            d[attr] = getattr(self, attr)
        with open('model.json', 'w') as f:
            json.dump(d, f)
        print(d)

m = Model()
m.save()