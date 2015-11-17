The Tate Collection
===================

Here we present the metadata for around 70,000 artworks that [Tate](http://www.tate.org.uk/) owns or jointly owns with the [National Galleries of Scotland](http://www.nationalgalleries.org) as part of [ARTIST ROOMS](http://www.tate.org.uk/artist-rooms). Metadata for around 3,500 associated artists is also included.

The metadata here is released under the Creative Commons Public Domain [CC0](http://creativecommons.org/publicdomain/zero/1.0/) licence. Please see the enclosed LICENCE file for more detail.

Images are not included and are not part of the dataset. Use of Tate images is covered on the
[Copyright and permissions](http://www.tate.org.uk/about/who-we-are/policies-and-procedures/website-terms-use/copyright-and-permissions) page. You may also [license images](http://tate-images.com) for commercial use.

Please review the full [usage guidelines](#usage).

## Examples

Here are some examples of Tate data usage in the wild. Please submit a pull request with your creation added to this list.

* [Tate Explorer](http://shardcore.org/tatedata/) by [Shardcore](http://www.shardcore.org)
* [Adding RDFa to Tate artwork pages](http://commonsmachinery.se/2013/11/tate-metadata-mashup/) by Peter Liljenberg at [Commons Machinery](http://commonsmachinery.se/)
* [Data visualisations](http://research.kraeutli.com/index.php/2013/11/the-tate-collection-on-github/) by [Florian Kräutli](http://www.kraeutli.com/)
* [machine imagined art](http://www.shardcore.org/cgi-bin/getArtwork.pl?id=a_96_19_f_26_b_1a_b_26_47_90_1d3_6_10_2d_) by [Shardcore](http://www.shardcore.org)
* [autoserota](http://www.shardcore.org/autoserota/) by [Shardcore](http://www.shardcore.org)
* [The Dimensions of Art](http://www.ifweassume.com/2013/11/the-dimensions-of-art.html) by [Jim Davenport](http://www.ifweassume.com)
* [Art as Data as Art](http://blog.ironholds.org/art-as-data-as-art/) and [Part II](http://blog.ironholds.org/art-as-data-as-art-part-ii/) by [Oliver Keyes](https://twitter.com/quominus)
* [Tate Acquisition Data](http://zenlan.com/tate/rickshaw.html) by [Zenlan](http://twitter.com/zenlan)
* [Artist Rooms](http://goodlemons.com/artist-rooms/) by [Jue Yang](http://twitter.com/jue_yang)
* [As Stated] (http://noemata.net/as/stated/) by [noemata/Bjørn Magnhildøen] (http://noemata.net)
* [Cultural Heritage Website with Neo4j] (http://larkin.io/index.php/category/tate/) by Larkin Cunningham
* [As Mutated] (http://noemata.net/as/mutated/) by [noemata/Bjørn Magnhildøen] (http://noemata.net)

We are also inviting you to create [GitHub Issues](https://github.com/tategallery/collection/issues) if you notice any bugs or have any ideas for improving the data. Thanks for your help!

## Repository Contents

We offer two data formats:

1. A richer dataset is provided in the JSON format, which is organised by the directory structure of the Git repository. JSON supports more hierarchical or nested information such as subjects.

2. We also provide CSVs of flattened data, which is less comprehensive but perhaps easier to grok. The CSVs provide a good introduction to overall contents of the Tate metadata and create opportunities for artistic pivot tables.

### JSON

#### Artists

Each artist has his or her own JSON file. They are found in the `artists` folder, then filed away by first letter of the artist’s surname.

#### Artworks

Artworks are found in the `artworks` folder. They are filed away by _accession number_. This is the unique identifier given to artworks when they come into the Tate collection. In many cases, the format has significance. For example, the `ar` accession number prefix indicates that the artwork is part of ARTIST ROOMS collection. The `n` prefix indicates works that once were part of the [National Gallery](http://www.nationalgallery.org.uk/) collection.

### CSV

There is one CSV file for artists (`artist_data.csv`) and one (very large) for artworks (`artwork_data.csv`), which we may one day break up into more manageable chunks. The CSV headings should be helpful. Let us know if not. Entrepreneurial hackers could use the CSVs as an index to the JSON collections if they wanted richer data. **NB CSV files are encoded as UTF-8 text, on which older versions of Excel may choke. We have inserted a UTF-8 BOM to help Excel detect the encoding, which may or may not be a terrible mistake.**


## <a name="usage"></a>Usage guidelines for open data
  

These usage guidelines are based on goodwill. They are not a legal contract but Tate requests that you follow these guidelines if you use Metadata from our Collection dataset.

The Metadata published by Tate is available free of restrictions under the [Creative Commons Zero Public Domain Dedication](http://creativecommons.org/publicdomain/zero/1.0/).

This means that you can use it for any purpose without having to give attribution. However, Tate requests that you actively acknowledge and give attribution to Tate wherever possible. Attribution supports future efforts to release other data.  It also reduces the amount of ‘orphaned data’, helping retain links to authoritative sources.

### Give attribution to Tate

Make sure that others are aware of the rights status of Tate and are aware of these guidelines by keeping intact links to the Creative Commons Zero Public Domain Dedication.

If for technical or other reasons you cannot include all the links to all sources of the Metadata and rights information directly with the Metadata, you should consider including them separately, for example in a separate document that is distributed with the Metadata or dataset.

If for technical or other reasons you cannot include all the links to all sources of the Metadata and rights information, you may consider linking only to the Metadata source on Tate’s website, where all available sources and rights information can be found, including in machine readable formats.

### Metadata is dynamic

When working with Metadata obtained from Tate, please be aware that this Metadata is not static. It sometimes changes daily. Tate continuously updates its Metadata in order to correct mistakes and include new and additional information. Museum collections are under constant study and research, and new information is frequently added to objects in the collection.

### Mention your modifications of the Metadata and contribute your modified Metadata back
Whenever you transform, translate or otherwise modify the Metadata, make it clear that the resulting Metadata has been modified by you. If you enrich or otherwise modify Metadata, consider publishing the derived Metadata without reuse restrictions, preferably via the Creative Commons Zero Public Domain Dedication.

### Be responsible

Ensure that you do not use the Metadata in a way that suggests any official status or that Tate endorses you or your use of the Metadata, unless you have prior permission to do so.

### Ensure that you do not mislead others or misrepresent the Metadata or its sources
Ensure that your use of the Metadata does not breach any national legislation based thereon, notably concerning (but not limited to) data protection, defamation or copyright.
Please note that you use the Metadata at your own risk.
Tate offers the Metadata as-is and makes no representations or warranties of any kind concerning any Metadata published by Tate.


The writers of these guidelines are deeply indebted to the [Smithsonian Cooper-Hewitt, National Design Museum](http://www.cooperhewitt.org/); and [Europeana](http://www.europeana.eu/).


