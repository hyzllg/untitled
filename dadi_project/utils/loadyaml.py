#读取yaml文件数据
import yaml

def load_yaml(path):

    with open(path,'r',encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.SafeLoader)
    return data