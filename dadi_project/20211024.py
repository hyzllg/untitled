import yaml
file_path = './setting/Config.yaml'

with open(file_path,encoding='utf-8') as f:
    datas = yaml.load(f,Loader=yaml.SafeLoader)
print(datas["xshx_oracle"]["xsxb_sit_oracle"])
