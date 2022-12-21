# ADA-NNS: Angular Distance-Guided Candidate Selection for Fast Graph-Baseed Approximate Nearest Neighbor Search

ADA-NNS is a novel angular distance-gudied search method for graph-based approximate nearest neighbor search (ANNS). It effectively filters neighbors that are less relevantt to the query and computes distances to the query only for the candidate neighbors. It not only achieves the state-of-the art performance for various datasets, but also maintains good compatibility with existing proximity graphs, such as NSG, Vamana, and NSSG.

Please refer to the full paper ADA-NNS.

## How to use

### Initialize

1. Clone submodules:

```shell
$ ./init.sh
```

2. Download datasets to the `ANNS\_datasets` directory.

3. [NSG and NSSG] Build kNN graphs

NSG and NSSG requires kNN graphs. We provide the script to build kNN graphs in `efanna\_graph`. Please refer to `efanna\_graph/README.md`.

4. Run examples

Follow readme in NSG, DiskANN, and NSSG.
