from client import RDFSReasoner

def main():
    print("=== Testing RDFS Semantic Forward-Chaining Reasoner ===")
    rdfs = RDFSReasoner()
    rdfs.add_triple("Dog", "subClassOf", "Mammal")
    rdfs.add_triple("Mammal", "subClassOf", "Animal")
    rdfs.add_triple("Fido", "type", "Dog")

    print(f"Base triples ({len(rdfs.triples)}):", rdfs.triples)
    rdfs.compute_closure()
    print(f"Deductive closure triples ({len(rdfs.triples)}):", rdfs.triples)

    assert ("Dog", "subClassOf", "Animal") in rdfs.triples
    assert ("Fido", "type", "Animal") in rdfs.triples
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
