Thoughts on subject data structure
---

The `subjects` field of the artwork jsons reveal the archival approach of the Tate Gallery.

                               subject
                                  |
                                  |
                 +++++++++++++++++++++++++++++++++
                 |                |              |
                 |                |              |
    level0     child            child          child
                 |                |              |
                 |                |              |
              +++++++             |              |
              |     |             |              |
              |     |             |              |
    level1  child child         child          child
              |     |             |              |
              |     |             |              |
              |     |             |          ++++++++
              |     |             |          |      |
              |     |             |          |      |
    level2  child child         child      child  child


If a level 2 child is present, the child's parent and grandprarent will come with it. Sample content of the levels:

    level 0 - people
    level 1 - actions: postures and motions
    level 2 - sitting

### Useful structures

- An index of all level0/1/2/3 ids/names as a lookup file. `level2.json` would be the base for all needed parent ids. Example:

  - level0.json
    
    `[{"name":"people", "id":91, "parent1":"none", "parent0":"none"}]`
    
  - level1.json
    
    `[{"name":"actions: postures and motions", "id":92,"parent1":"none","parent0":91}]`
    
  - level2.json
    
    `[{"name":"sitting","id":694,"parent1":92,"parent0":91}]`

- Flat indexing. This could represent one strand of archival relationships in one artwork.
    
    {
		"name0":"people",
		"name1":"actions: postures and motions",
		"name2":"sitting"
	}
