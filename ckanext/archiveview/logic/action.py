import zipfile
from io import BytesIO

import requests
from ckan import logic
from ckan.lib import uploader
from ckan.logic import get_action

from ckanext.archiveview.archive_util import zipfile_to_tree


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
