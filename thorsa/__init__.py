__author__ = 'Thorsa'

import os
from calibre.customize import FileTypePlugin

class TagFilter(FileTypePlugin):

    name                = 'Tag Filter Plugin' # Name of the plugin
    description         = 'Remove any tags that do not fit our genres on import'
    supported_platforms = ['windows', 'osx', 'linux'] # Platforms this plugin will run on
    author              = 'Thorsa' # The author of this plugin
    version             = (1, 2, 0)   # The version number of this plugin
    file_types          = set(['epub', 'mobi']) # The file types that this plugin will be applied to
    on_import      = True # Run this plugin after importing into the library
    minimum_calibre_version = (0, 7, 53)



    def run(self, path_to_ebook):
        from calibre.ebooks.metadata.meta import get_metadata, set_metadata
        file = open(path_to_ebook, 'r+b')
        ext  = os.path.splitext(path_to_ebook)[-1][1:].lower()
        mi = get_metadata(file, ext)
        mi.tags = ['fiction']
        set_metadata(file, mi, ext)
        print(str(mi.tags))
        return path_to_ebook