def find_differences(json_old, json_new, diff_list):
    result = {}

    for key in diff_list:
        old_value = json_old['data'].get(key)
        new_value = json_new['data'].get(key)

        if old_value != new_value:
            result[key] = new_value

    return result
