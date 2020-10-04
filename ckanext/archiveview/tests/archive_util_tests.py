import unittest
import zipfile

from ckanext.archiveview.archive_util import add_path_to_file_tree, zipfile_to_tree


class TestArchiveUtil(unittest.TestCase):
    def test_add_dir_to_empty_file_tree(self):
        file_dir_dict = {}
        add_path_to_file_tree(file_dir_dict, 'path/to/new/folder/')

        expected_dict = {
            'path': {
                'to': {
                    'new': {
                        'folder': {}
                    }
                }
            }
        }

        assert file_dir_dict == expected_dict

    def test_add_file_to_file_tree(self):
        file_dir_dict = {}
        add_path_to_file_tree(file_dir_dict, 'path/to/new/folder/test.xml')

        expected_dict = {
            'path': {
                'to': {
                    'new': {
                        'folder': {
                            'test.xml': None
                        }
                    }
                }
            }
        }

        assert file_dir_dict == expected_dict

    def test_zipfile_to_tree(self):
        zip_file = zipfile.ZipFile('test_assets/testcase.zip')
        result = zipfile_to_tree(zip_file.filelist)

        expected_file_tree = {
            'testcase': {
                'subdir1': {
                    'file5': None
                },
                'subdir2': {
                    'file6': None
                },
                'subdir3': {},
                'file1': None,
                'file2': None,
                'file3': None,
                'file4': None}
        }

        assert result == expected_file_tree
