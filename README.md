# CPC GraphRag Classifier

This is a CPC (Classification of Patent Claims) graph-based classifier. 

## Project goal
Unlike existing approaches that rely on static fine-tuned language models for CPC classification, this project intends to use method a GraphRAG pipeline over a Neo4j CPC knowledge graph, retrieving and ranking CPC codes based on a dynamically updated taxonomy enriched with definitions, synonyms, and relationships. Instead of treating classification as a single model prediction, it converts patents into feature graphs, searches the CPC graph for matching nodes via keyword/embedding similarity, applies graph reasoning to aggregate candidates, and outputs interpretable results that adapt instantly to CPC changes—eliminating retraining and offering full transparency.

## Project progress

- [x] Initialise project
- [x] Turn CPC into a graph
- [x] Create embeddings for each CPC definition
- [x] Trial vector search of CPC graph using embedded claims

## Future work

- [ ] **Eval:** Create evaluation pipeline and metrics.  Target is *"On the finest CPC granularity, 88% of test documents have at least one ground truth symbol in the top 10 predictions."* as per https://www.sciencedirect.com/science/article/abs/pii/S0172219025000274.
- [ ] **Eval:** Proximity to ground truth CPC codes.

- [ ] **Improve CPC graph:** Use graph reasoning to improve CPC graph vector search
- [ ] **Improve CPC graph:** LLM rewrite and improvement of definitions (local or batch?)
- [ ] **Improve CPC graph:** Split claims into features and perform multiple searches and aggregate results

- [ ] **Additional search method:** BM25 search for claims

- [ ] **Additional search method:** Claims as nodes with relationships to CPC nodes
- [ ] **Additional search method:** Embed claims and search to find CPC nodes

- [ ] **Result aggregation:** Aggregate results from multiple search methods
- [ ] **Result aggregation:** Re-rank results using graph reasoning
