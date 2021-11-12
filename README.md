## Reference genebank no nlm
### Using most recent assemby from genebank: 
1) https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.28_GRCh38.p13/
2) Manual download of cDNA sequences as well as protein sequences per each chromosome at such URL:
3) https://www.ncbi.nlm.nih.gov/nuccore/NC_000006.12 for human chromosome 6
4) download default name sequence.txt, I named sequence-homo-38-chrNN-coding-nucleotides/protein.txt
5) PLAN: save data in separate folder, main code in a folder with git
6) README.md
7) read-write-gb-fasta-coding-nucletide-protein.py: 
 a) import libraries: hashlib, sys, os, collections, matplotlib
 b) define path to read file
 c) file is in FASTA format: first line with open angle bracket, label, second line with sequence.
 d) read label, hash. Read sequence line-by-line, keeping new line in between, hash
 e) create a dictionary object with fields: label, lableMd5, fastaMd5
 f) add dictionary object to chromosome object: an object of objects
 g) Once chromosome object is built, save with same name plus extension "dict.out".
 h) Save into a file two columns: labelMd5 and fasta Md5 (hashes)
 i) count duplicates of chromosome object (no need to sort based on fastaMd5, in order to keep order within chromosome)
 j) Display duplicates as bars in a png format. 
8) for loop in enumerate(file) needed to read line-by-line
9) In summary: input a fasta file, output file with label hash and fasta hash, and a png few png files with bar representing the number of duplicate sequences within chromosome.

