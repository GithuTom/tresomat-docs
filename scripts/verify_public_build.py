from pathlib import Path
import json
import sys

site = Path(sys.argv[1] if len(sys.argv) > 1 else "site-public")
forbidden_dirs = [site / "api", site / "support"]
errors = [f"forbidden output exists: {p}" for p in forbidden_dirs if p.exists()]
search = site / "search" / "search_index.json"
if not search.is_file():
    errors.append("public search index missing")
else:
    data = search.read_text(encoding="utf-8").lower()
    for token in ('"location":"api/', '"location":"support/', '"location": "api/', '"location": "support/'):
        if token in data:
            errors.append(f"protected route found in public search index: {token}")
if errors:
    print("\n".join(errors))
    raise SystemExit(1)
print("Public build contains no /api/ or /support/ output and no protected search entries.")
