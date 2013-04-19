from rdflib.term import URIRef
from hashuri.rdf import RdfUtils

def preprocess(quads, hashstr=None, baseuri=None):
    newquads = []
    bnodemap = []
    for q in quads:
        c = transform(q[0], hashstr, baseuri, bnodemap)
        s = transform(q[1], hashstr, baseuri, bnodemap)
        p = transform(q[2], hashstr, baseuri, bnodemap)
        o = q[3]
        if isinstance(q[3], URIRef):
            o = transform(q[3], hashstr, baseuri, bnodemap)
        newquads.append((c, s, p, o));
    return newquads

def transform(uri, hashstr, baseuri, bnodemap):
    if uri is None: return None
    if baseuri is None:
        return URIRef(RdfUtils.normalize(uri, hashstr))
    return RdfUtils.get_hashuri(uri, baseuri, " ", bnodemap)
