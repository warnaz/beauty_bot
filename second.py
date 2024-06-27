def group_versions(list_version):
    version_count = {}

    for item in list_version:
        id_version_tuple = tuple(item)
        if id_version_tuple in version_count:
            version_count[id_version_tuple] += 1
        else:
            version_count[id_version_tuple] = 1

    grouped_list = [[id_version[0], id_version[1], count]
                    for id_version, count in version_count.items()]

    return grouped_list
