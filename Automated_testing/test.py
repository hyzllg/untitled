import yaml
def data():
    with open("repay.yaml",encoding="utf-8") as f:
        datas = yaml.load(f, Loader=yaml.SafeLoader)
        return  datas

