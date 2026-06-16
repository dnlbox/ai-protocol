import json
from collections import Counter

try:
    with open('analysis_results.json', 'r') as f:
        results = json.load(f)
        
    print(f"Total analyzed files: {len(results)}")
    
    all_constraints = []
    all_workflows = []
    all_innovations = []
    
    for r in results:
        all_constraints.extend(r.get('core_constraints', []))
        all_workflows.extend(r.get('workflow_directives', []))
        all_innovations.extend(r.get('unique_innovations', []))
        
    print("\n--- SAMPLE CONSTRAINTS ---")
    for c in all_constraints[:15]: print(f"- {c}")
    
    print("\n--- SAMPLE WORKFLOWS ---")
    for w in all_workflows[:10]: print(f"- {w}")
    
    print("\n--- TOP INNOVATIONS ---")
    for i in all_innovations[:10]: print(f"- {i}")
    
except Exception as e:
    print(f"Error: {e}")
