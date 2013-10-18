The Tate Collection
===================

Here we present the metadata for ~69,000 artworks that [Tate](http://www.tate.org.uk/) owns or jointly owns with the [National Galleries of Scotland](http://www.nationalgalleries.org) as part of [ARTIST ROOMS](http://www.tate.org.uk/artist-rooms). Metadata for the contributing ~3,500 artists is also included.

The metadata here is released under the Creative Commons Public Domain [CC0](http://creativecommons.org/publicdomain/zero/1.0/) licence. Please see the enclosed LICENCE file for more detail.

Images are not included and are not part of the dataset. Use of Tate images is covered on the
[Copyright and permissions](http://www.tate.org.uk/about/who-we-are/policies-and-procedures/website-terms-use/copyright-and-permissions) page. You may also [license images](http://tate-images.com) for commercial use.

## Contents

We offer two data formats:

1. A richer dataset is provided in the JSON format, which is organised by the directory structure of the Git repository. JSON supports more hierarchical or nested information such as subjects.

2. We also provide CSVs of flattened data, which is less comprehensive but perhaps easier to grok. The CSVs provide a good introduction to overall contents of the Tate metadata and create opportunities for artistic pivot tables.

### JSON

#### Artists

Each artist has his or her own JSON file. They are found in the `artists` folder, then filed away by first letter of the artist’s surname.

#### Artworks

Artworks are found in the `artworks` folder. They are filed away by _accession number_. This is the unique identifier given to artworks when they come into the Tate collection. In many cases, the format has significance. For example, the `ar` accession number prefix indicates that the artwork is part of ARTIST ROOMS collection. The `n` prefix indicates works that once were part of the [National Gallery](http://www.nationalgallery.org.uk/) collection.

### CSV

There is one CSV file for artists (`artist_data.csv`) and one (very large) for artworks (`artwork_data.csv`), which we may one day break up into more manageable chunks. The CSV headings should be helpful. Let us know if not. Entrepreneurial hackers could use the CSVs as an index to the JSON collections if they wanted richer data.

