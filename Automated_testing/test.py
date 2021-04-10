import Collect
import yaml

with open("CLAIM_RESULT_DATAS.yaml",encoding="utf-8") as f:
    f = yaml.load(f)
print(f)