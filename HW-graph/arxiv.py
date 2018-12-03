from enum import Enum
import tqdm


class ArxivTags(Enum):
    Year = 0
    Id = 1
    Tags = 2
    GeneralTags = 3
    Ind1 = 4
    Ind2 = 5
    Edges = 6
    Authors = 7
    Name = 8


def get_density_graph(vertex_deg):
    return 2 * sum(vertex_deg) / (len(vertex_deg) * (len(vertex_deg)) - 1)


def load_arxiv(path):

    docs = []
    for year in tqdm.tqdm(range(1991, 2018)):
        fd = open(path+"pscp-%d.csv" % year)
        docs_year = []
        for line in fd:
            if line[0] == '#':
                continue
            fields = line.split(";", 7)
            edges = fields[4].split(',')
            tags = fields[1].split(',')
            docs_year.append({
                ArxivTags.Year: year,
                ArxivTags.Id: fields[0],
                ArxivTags.Tags: set(tags),
                ArxivTags.GeneralTags: set([tag.split('.')[0] for tag in tags]) ,
                ArxivTags.Ind1: fields[2],
                ArxivTags.Ind2: fields[3],
                ArxivTags.Edges: [] if edges[0] == '' else edges,
                ArxivTags.Authors: line.split(";")[5].split(','),
                ArxivTags.Name: line.split(";")[6],
            })
        docs += docs_year
    docs_dict = {}
    for doc in docs:
        if doc[ArxivTags.Id] in docs_dict:
            raise doc[ArxivTags.Id]
        docs_dict[doc[ArxivTags.Id]] = doc
    return docs_dict
