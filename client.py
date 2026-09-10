class RDFSReasoner:
    """
    RDFS Semantic Forward-Chaining Rule Engine.
    Entailments:
    - Transitive subClassOf: (A subClassOf B) & (B subClassOf C) => (A subClassOf C)
    - Type inheritance: (X type A) & (A subClassOf B) => (X type B)
    """
    def __init__(self):
        self.triples = set()

    def add_triple(self, s, p, o):
        self.triples.add((s, p, o))

    def compute_closure(self):
        changed = True
        while changed:
            changed = False
            new_triples = set()
            for s, p, o in list(self.triples):
                if p == "subClassOf":
                    for s2, p2, o2 in list(self.triples):
                        if p2 == "subClassOf" and s2 == o:
                            cand = (s, "subClassOf", o2)
                            if cand not in self.triples:
                                new_triples.add(cand)

                if p == "type":
                    for s2, p2, o2 in list(self.triples):
                        if p2 == "subClassOf" and s2 == o:
                            cand = (s, "type", o2)
                            if cand not in self.triples:
                                new_triples.add(cand)

            if new_triples:
                self.triples.update(new_triples)
                changed = True
