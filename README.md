# ADA-NNS

ADA-NNS is a novel angular distance-gudied search method for graph-based approximate nearest neighbor search (ANNS). It effectively filters neighbors that are less relevantt to the query and computes distances to the query only for the candidate neighbors. It not only achieves the state-of-the art performance for various datasets, but also maintains good compatibility with existing proximity graphs, such as NSG, Vamana, and NSSG.

Please refer to the full paper ADA-NNS.

## Datasets

| Name     | Dimension | No. of base | No. of query |
|----------|-----------|-------------|--------------|
| [SIFT1M](http://corpus-texmex.irisa.fr/)   | 128       | 1,000,000   | 10,000       |
| [GIST1M](http://corpus-texmex.irisa.fr/)   | 960       | 1,000,000   | 1,000        |
| [CRAWL](http://commoncrawl.org/)    | 300       | 1,989,995   | 10,000       |
| [DEEP1M](https://research.yandex.com/blog/benchmarks-for-billion-scale-similarity-search)   | 256       | 1,000,000   | 1,000        |
| [DEEP100M](https://research.yandex.com/blog/benchmarks-for-billion-scale-similarity-search) | 96        | 100,000,000 | 1,000        |

## How to use

### Initialize

1. Clone submodules:

```shell
$ ./init.sh
```

2. Download datasets to the `ANNS_datasets` directory.

3. [NSG and NSSG] Build kNN graphs

NSG and NSSG requires kNN graphs. We provide the script to build kNN graphs in `efanna_graph`. Please refer to `efanna_graph/README.md`.

4. Run examples

Follow readme in NSG, DiskANN, and NSSG.
