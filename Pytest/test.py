import yaml

with open("test.yaml",encoding="utf-8") as f:
	f = yaml.load(f)
print(f)
print(type(f))