import yaml
import json
import os

# path = os.path.dirname(os.path.dirname(__file__))
# #json->yaml
# # yamlText = yaml.dump(a,default_flow_style=False,allow_unicode=True)#yaml.dump后加参数防止中文乱码
# #yaml->json
# dictText = yaml.load(open(f'{path}/conf/Config.yaml','r',encoding='utf-8'),Loader=yaml.FullLoader)
# print(dictText)
# keys = dictText.keys()
# for i in keys:
#     yamlText = yaml.dump(dictText[i], default_flow_style=False, allow_unicode=True)  # yaml.dump后加参数防止中文乱码
#     with open(f'{path}/conf/url_res/{i}.yaml', 'w' ,encoding='utf-8') as f:
#         f.write(yamlText)