# CKAN Archive Resource View
<img src="https://raw.githubusercontent.com/fwoerister/ckanext-mongodatastore/master/images/TU_Signet_SW_rgb.png" align="right" width="150px"/>

A ckan extension that provides a resource view for zipped archives. The plugin parses zip files (stored locally or URLs of zip archives) and presents its structure using [jsTree](https://www.jstree.com/) a javascript library to display file tree structures.

The current implementaiton supports `.zip` archives only.


## Requirement
This CKAN extension is compatible with CKAN 2.9 and requires Python >3.6

## Installation

1) Activate the virtual environment of your CKAN instance and install the extension via `pip`:
    ```
    pip install ckanext-archiveview
    ```

2) Configure the Plugin in the CKAN configuration file (e.g. `/etc/ckan/default/ckan.ini`)

    ```
    ckan.plugins= [...] archiveview
    ```

3) Configure the Archive View as default default view:
    ```
    ckan.views.default_view = archiveview
    ```

4) Restart CKAN

## Preview
<img src="https://raw.githubusercontent.com/fwoerister/ckanext-archiveview/main/img/ckanext-archive.png"/>
