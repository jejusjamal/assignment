#!/usr/bin/python

def get_nested_kv(obj_dict, obj_key):
    tmp_dict = obj_dict
    error_flag = 0
    for key in obj_key.split('/'):
        try:
            tmp_dict = tmp_dict[key]
        except:
            raise ValueError("Wrong key provided, try again:")
            error_flag = 1

    if not error_flag:
        return tmp_dict

object = {"a": {"b": {"c": "d"}}}
key = 'a/b/c'
result = get_nested_kv(object, key)
print(result)
