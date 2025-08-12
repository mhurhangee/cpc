# CPCGraphRag Classifier

This is a CPC (Classification of Patent Claims) graph-based classifier. 

## Project goal
Unlike existing approaches that rely on static fine-tuned language models for CPC classification, this project intends to use method a GraphRAG pipeline over a Neo4j CPC knowledge graph, retrieving and ranking CPC codes based on a dynamically updated taxonomy enriched with definitions, synonyms, and relationships. Instead of treating classification as a single model prediction, it converts patents into feature graphs, searches the CPC graph for matching nodes via keyword/embedding similarity, applies graph reasoning to aggregate candidates, and outputs interpretable results that adapt instantly to CPC changes—eliminating retraining and offering full transparency.

## Project progress

- [x] Initialise project