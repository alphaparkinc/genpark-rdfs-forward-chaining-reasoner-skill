import sys
import json
from client import RDFSReasoner

reasoner = RDFSReasoner()

def handle_call(name, arguments):
    if name == "add_triple":
        reasoner.add_triple(arguments["s"], arguments["p"], arguments["o"])
        return {"triples_count": len(reasoner.triples)}
    elif name == "closure":
        reasoner.compute_closure()
        return {"triples": list(reasoner.triples)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
