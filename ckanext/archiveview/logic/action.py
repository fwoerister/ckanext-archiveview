import zipfile
from io import BytesIO

import requests
from ckan import logic
from ckan.lib import uploader
from ckan.logic import get_action


def add_dir_to_file_tree(file_tree, dir_path):
    splitted_path = dir_path.split('/')

    path = splitted_path[:-2]
    new_dir = splitted_path[-2]

    current_item = file_tree
    for item in path:
        current_item = current_item.get(item)

    current_item[new_dir] = {}


def add_file_to_file_tree(file_tree, dir_path):
    splitted_path = dir_path.split('/')

    path = splitted_path[:-1]
    new_file = splitted_path[-1]

    current_item = file_tree
    for item in path:
        current_item = current_item.get(item)

    current_item[new_file] = None


def zipfile_to_tree(zipfiles):
    result = {}
    for file in zipfiles:
        if file.is_dir():
            add_dir_to_file_tree(result, file.filename)
        else:
            add_file_to_file_tree(result, file.filename)
    return result


@logic.side_effect_free
def unzip_resource(context, data_dict):
    resource = get_action('resource_show')(None, {'id': data_dict['resource_id']})
    url_type = resource.get('url_type')

    if url_type == 'upload':
        upload = uploader.ResourceUpload(resource)
        resource_file = open(upload.get_path(resource['id']), 'rb')
    else:
        resource_file = BytesIO(requests.get(resource.get('url')).content)

    zip_file = zipfile.ZipFile(resource_file)
    return zipfile_to_tree(zip_file.filelist)
