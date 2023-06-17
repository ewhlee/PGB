## PGB: A PubMed Graph Benchmark for Heterogeneous Network Representation Learning
PubMed Graph Benchmark (PGB) aggregates the metadata associated with the biomedical articles from PubMed into a unified source. 
The benchmark contains metadata including title, abstract, authors, in/out citations, MeSH terms, MeSH hierarchy, venue, publication type, and chemicals.

## Metadata schema
| Field              | Field Type              |
| ------------------ | ----------------------- |
| pmid               | str-valued field        |
| pmcid              | str-valued field        |
| title              | str-valued field        |
| abstract           | str-valued field        |
| authors            | List[Dict]-valued field |
| year               | int-valued field        |
| venue              | str-valued field        |
| publication_type   | List[str]-valued field  |
| chemicals          | List[str]-valued field  |
| mesh               | List[Dict]-valued field |
| outbound_citations | List[str]-valued field  |
| inbound_citations  | List[str]-valued field  |

### Authors
Each author has keys "first", "middle", "last", and "suffix".
| Field              | Field Type             |
| ------------------ | ---------------------- |
| first              | str-valued field       |
| middle             | List[str]-valued field |
| last               | str-valued field       |
| suffix             | str-valued field       |

### Publication type
The publication type identifies the type of article indexed for MEDLINE and characterize the nature of the information
(ex. Review, Letter, Retracted Publication, Research Support, NIH, or Clicial Conference).

### Chemicals
The chemical list contains the name of the chemical substances assigned by the Chemical Abstracts Service.

### MeSH
The MeSH field contains the "term", "is_major", and "tree_num".
The "term" contains the MeSH term, "is_major" contains the information whether the MeSH term is the major topic or not, and "tree-num" contains the MeSH hierarchical information.
| Field    | Field Type        |
| -------- | ------------------|
| term     | str-valued field  |
| is_major | bool-valued field |
| tree_num | str-valued field  |

## Download
The PGB benchmark is publicly available (https://zenodo.org/record/6406776#.YqtUwnbMKUk).

## How to use
The load_data.py shows an example to read the data file.

## License
PGB dataset is released under the CC BY-NC 4.0 license and for non-commercial use.

