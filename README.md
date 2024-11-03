# catnet
Need to create DOI in Zenodo and submit to pyOpenSci
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8365068.svg)](https://doi.org/10.5281/zenodo.8365068)

## What catnet does
catnet is a Python package that allows for transforming tabular data into a network structure. catnet can identify the coexistence of variables and categories in literature reviews and other tables and create a network dataframe that can be exported into a format that can be taken by other packages such as `networkx` and applications such as [Gephi](https://gephi.org/).

## How to install catnet
To install this package run:

`python -m pip install git+https://github.com/CamiBetancur/catnet/)`

## Get started using catnet

To be able to use `catnet` you need to format your dataframe in one of the following ways:
### 1. **"Long" format**
"Long" format refers to data that has a column for describing a categorical variable (`var_col`) and an identifier column (`id_col`) that identifies to which entity that variable belongs to. For example, in a literature review, a long dataframe that could be used by catnet could look like this (note that the column names `id_col` and `var_col` do not necessarily need to be named `id_col` and `var_col`):

| id_col | var_col            | other_data_cols |
| ------ | ------------------ | --------------- |
| doc_01 | Health             | ...             |
| doc_01 | Water access       | ...             |
| doc_01 | Water quality      | ...             |
| doc_02 | Health             | ...             |
| doc_02 | Energy generation  | ...             |
|  ...   |   ...              | ...             |

### Dataframes in a "long" format

For "long" dataframes, you can use the function [...] complement later.

## Community

Add information here about contributing to your package. Be sure to add links to your
`CODE_OF_CONDUCT.md` file and your development guide. For now this section might be
empty. You can go back and fill it in later.

## How to cite catnet

### APA 7

>Betancur Jaramillo, J. C. (2024). _catnet source code (Version 0.0)_ [source code]. [https://github.com/CamiBetancur/catnet/](https://github.com/CamiBetancur/catnet/). 

### BibTex


```
@misc{Betancur_2024,  
      title={catnet},  
      url={https://github.com/CamiBetancur/catnet},  
      publisher={Stockholm Environment Institute},  
      author={Betancur Jaramillo, Juan Camilo},  
      year={2024}}  
```