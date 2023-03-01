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

## License
PGB dataset is released under the CC BY-NC 4.0 license and for non-commercial use.

## Node Classification & Clustering
We also evaluated the network embedding methods on node classification and node clustering tasks.
For both tasks, we use the labels provided by Namata et al. (MLG 2012) which consists of PubMed papers about diabetes.
Articles are labeled with 3 classes, 'Diabetes Mellitus, Experimental', 'Diabetes Mellitus Type 1', and 'Diabetes Mellitus Type 2'.
For the node classification task, we adopt micro and macro F1-score as the evaluation metrics as it is a multi-classification task (i.e., 3 classes). 
To assess the quality of the clusters, we use normalized mutual information (NMI) and adjusted rand index (ARI). 
For the number of clusters, we follow the number of classes used for the node classification task.

| Baline  | Macro-F1 | Micro-F1 | NMI   | ARI   |
| ------- | -------- | -------- | ----- | ----- |
| LINE    | 36.47   | 39.67     | 6.56  | 5.38  |
| GCN     | 42.13   | 43.19     | 6.98  | 5.96  |
| HAKE    | 48.71   | 50.85     | 10.73 | 10.11 |
| GAHNE   | 50.44   | 53.37     | 13.86 | 13.52 |
| ie-HGCN | 50.37   | 36.47     | 13.71 | 13.27 |

The heterogeneous network embedding models (HAKE, GAHNE, and ie-HGCN) outperform the homogeneous network embedding models (LINE and GCN), illustrating that modeling the multiple node types and link types is beneficial.
Both GAHNE and ie-HGCN have similar scores across all four metrics.
The difference between LINE and GCN shows the importance of using the word information as GCN uses the TF-IDF weighted word vectors for the node feature on top of the citation network while LINE only uses the citation network.
Unfortunately, a major limitation of existing heterogeneous network embedding models is the memory footprint.
