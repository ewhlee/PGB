## PGB: A PubMed Graph Benchmark for Heterogeneous Network Representation Learning
PubMed Graph Benchmark (PGB) aggregates the metadata associated with the biomedical articles from PubMed into a unified source. 
The benchmark contains metadata including title, abstract, authors, in/out citations, MeSH terms, MeSH hierarchy, venue, publication type, and chemicals.

## Metadata schema
pmid: str-valued field; PubMed identifier.
pmcid: str-valued field; PubMed Central identifier.
title: str-valued field
abstract: str-valued field
authors: List[Dict]-valued field
year: int-valued field
venue: str-valued field
publication_type: List[str]-valued field
chemicals: List[str]-valued field
mesh: List[Dict]-valued field
outbound_citations: List[str]-valued field
inbound_citations: List[str]-valued field
has_outbound_citations: bool-valued field
has_inbound_citations: bool-valued field

### Authors
Each author has keys "first", "middle", "last", and "suffix". Except "middle", which is List[str]-valued field, other keys are str-valued field.

### Publication type
The publication type identifies the type of article indexed for MEDLINE and characterize the nature of the information
(ex. Review, Letter, Retracted Publication, Research Support, NIH, or Clicial Conference).

### Chemicals
The chemical list contains the name of the chemical substances assigned by the Chemical Abstracts Service.

### MeSH
The MeSH field contains the "term" (str-valued field), "is_major" (bool-valued field), and "tree_num" (str-valued field).
The "term" contains the MeSH term, "is_major" contains the information whether the MeSH term is the major topic or not, and "tree-num" contains the MeSH hierarchical information.

## Download
The PGB benchmark is publicly available (https://zenodo.org/record/6406776#.YqtUwnbMKUk).

## License
PGB dataset is released under the CC BY-NC 4.0 license and for non-commercial use.
