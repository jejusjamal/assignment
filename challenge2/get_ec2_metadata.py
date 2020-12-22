import boto.utils
import json


def get_metadata():
    ec2_data = boto.utils.get_instance_metadata()
    return ec2_data


def get_metadata_json():
    metadata = get_metadata()
    metadata_json = json.dumps(metadata)
    return metadata_json


def get_key_recurs(search_dict, field):
    """Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    fields_found = []
    for key, value in search_dict.items():
        try:
            if key == field:
                fields_found.append(value)

            elif isinstance(value, dict):
                results = get_key_recurs(value, field)
                for result in results:
                    fields_found.append(result)

            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        more_results = get_key_recurs(item, field)
                        for another_result in more_results:
                            fields_found.append(another_result)
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
            exit(1)

    return fields_found


if __name__ == '__main__':

    print(get_metadata_json())
    print("#####################################################")
    key = input("What key would you like to find?\n")
    result = get_key_recurs(get_metadata(), key)
    if not result:
        print("Key not found, Please enter correct key")
    else:
        print(json.dumps(result))
