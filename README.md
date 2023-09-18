# GECCO app

## About
[GECCO (Gene Cluster prediction with Conditional Random Fields)](https://github.com/zellerlab/GECCO) is a fast and scalable method for identifying putative novel Biosynthetic Gene Clusters (BGCs) in genomic and metagenomic data using Conditional Random Fields (CRFs). 
This repo dockerizes GECCO to make it available cross-plattform. 

##
Running using docker
```code
docker build -t gecco:latest <path-to-folder>
docker run -p 8080:8080 gecco
```
Access the app from localhost:8080 in your browser.