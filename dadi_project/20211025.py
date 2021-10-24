import yaml

get_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
res_url = get_data('./setting/Config.yaml')["api_url_tc"]
print(res_url)