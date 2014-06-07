__author__ = 'sigurros'

import os
from calibre.customize import FileTypePlugin

class HelloWorld(FileTypePlugin):

    name                = 'Metadata messer Plugin' # Name of the plugin
    description         = 'Mess with metadata on import'
    supported_platforms = ['windows', 'osx', 'linux'] # Platforms this plugin will run on
    author              = 'Thorsa' # The author of this plugin
    version             = (1, 1, 0)   # The version number of this plugin
    file_types          = set(['epub', 'mobi']) # The file types that this plugin will be applied to
    on_import      = True # Run this plugin after importing into the library
    minimum_calibre_version = (0, 7, 53)



    def run(self, path_to_ebook):
        from calibre.ebooks.metadata.meta import get_metadata, set_metadata
        file = open(path_to_ebook, 'r+b')
        ext  = os.path.splitext(path_to_ebook)[-1][1:].lower()
        mi = get_metadata(file, ext)
        mi.rating = 5
        set_metadata(file, mi, ext)
        f = open('workfile', 'w')
        s = str('File: ' + file + ' ext: ' + ext)
        f.write()
        return path_to_ebook