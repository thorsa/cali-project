__author__ = 'Thorsa'

import os
from calibre.customize import FileTypePlugin

class TagFilter(FileTypePlugin):

    name                = 'Tag Filter Plugin' # Name of the plugin
    description         = 'Remove any tags that do not fit our genres on import'
    supported_platforms = ['windows', 'osx', 'linux'] # Platforms this plugin will run on
    author              = 'Thorsa' # The author of this plugin
    version             = (1, 0, 0)   # The version number of this plugin
    file_types          = set(['epub', 'mobi']) # The file types that this plugin will be applied to
    on_import      = True # Run this plugin after importing into the library
    minimum_calibre_version = (0, 7, 53)

    def new_genre_list(self, genresonbook):

        genres = [u'drama',u'adventure',u"children's",u'young-adult',u'satire',u'comedy',u'erotic', u'historical',
                  u'literary',u'memoir',u'thriller',u'horror',u'science',u'saga',u'steampunk',u'dystopian',
                  u'post-apocalyptic',u'alien',u'gothic',u'supernatural',u'paranormal',u'ghost ',u'vampire',
                  u'fiction',u'werewolf',u'occult',u'fantasy',u'contemporary',u'epic',u'medieval',u'romance',
                  u'suspense',u'crime',u'detective',u'mystery',u'westerns',u'tragedy',u'urban',u'tragicomedy',
                  u'fable',u'folklore',u'history',u'philosophy']
        newgenres = set(genres).intersection(genresonbook)
        for tag in genres:
            for tag2 in genresonbook:
                if tag2.find(tag) > -1:
                    newgenres.add(tag)

        return sorted(newgenres)

    def run(self, path_to_ebook):

        from calibre.ebooks.metadata.meta import get_metadata, set_metadata
        file = open(path_to_ebook, 'r+b')
        ext  = os.path.splitext(path_to_ebook)[-1][1:].lower()
        mi = get_metadata(file, ext)
        genresonbook = [element.lower() for element in mi.tags]
        mi.tags = self.new_genre_list(genresonbook)

        set_metadata(file, mi, ext)

        print(mi)
        print(genresonbook)

        return path_to_ebook