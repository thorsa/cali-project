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

    def new_genre_list(self, genresonbook):
        genres = [u'drama', u'romance', u'satire', u'tragedy', u'comedy', u'tragicomedy',
                  u'horror', u'fiction', u'supernatural']
        newgenres = set(genres).intersection(genresonbook)
        for tag in genres:
            for tag2 in genresonbook:
                if tag2.find(tag) > -1:
                    newgenres.add(tag)

        return newgenres

    def run(self, path_to_ebook):

        from calibre.ebooks.metadata.meta import get_metadata, set_metadata
        file = open(path_to_ebook, 'r+b')
        ext  = os.path.splitext(path_to_ebook)[-1][1:].lower()
        mi = get_metadata(file, ext)
        genresonbook = [element.lower() for element in mi.tags]
        newgenres = self.new_genre_list(genresonbook)

        #set_metadata(file, mi, ext)
        print(genresonbook)
        print(newgenres)
        return path_to_ebook