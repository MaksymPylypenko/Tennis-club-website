#!/home/c/cl80114/pyenv/bin/python3.4

import yaml
from collections import OrderedDict

def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)
     
def getStrings(path):
    with open(path,'r',encoding="utf-8") as stream:
        try:
            s = ordered_load(stream, yaml.SafeLoader)
        except yaml.YAMLError as exc:
            print(exc)
    return s
    
#print(getStrings("strings.yaml"))