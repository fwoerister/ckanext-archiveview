from zipfile import BadZipFile

import ckan.plugins as p
import ckan.plugins.toolkit as toolkit

from ckanext.archiveview.logic.action import unzip_resource

SUPPORTED_FORMATS = ['zip']


class ArchiveViewPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.IActions)

    @staticmethod
    def get_actions():
        return {
            'unzip_resource': unzip_resource
        }

    @staticmethod
    def update_config(config):
        toolkit.add_public_directory(config, 'theme/public')
        toolkit.add_template_directory(config, 'theme/templates')
        toolkit.add_resource('theme/assets', 'ckanext-archiveview')

    @staticmethod
    def setup_template_variables(context, data_dict):
        try:
            unzip_resource(None, {'resource_id': data_dict['resource']['id']})
        except BadZipFile:
            return {'bad_zip_file': True}
        return {'file_tree_dict': unzip_resource(None, {'resource_id': data_dict['resource']['id']}).items()}

    @staticmethod
    def can_view(data_dict):
        resource = data_dict['resource']
        return resource.get('format').lower() in SUPPORTED_FORMATS

    @staticmethod
    def view_template(context, data_dict):
        return 'archiveview/archive_view.html'

    @staticmethod
    def info():
        return {
            'name': 'archive_view',
            'title': 'Archive View',
            'filterable': False,
            'icon': 'file-archive',
            'requires_datastore': False,
            'default_title': 'Archive View'
        }
