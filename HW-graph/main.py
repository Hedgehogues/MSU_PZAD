from arxiv import load_arxiv, ArxivTags

docs = load_arxiv("paperscape-data-master/")

vertex_deg = [len(doc[ArxivTags.Edges]) for doc in docs]
density_graph = 2 * sum(vertex_deg) / (len(vertex_deg) * (len(vertex_deg)) - 1)
print(density_graph)
