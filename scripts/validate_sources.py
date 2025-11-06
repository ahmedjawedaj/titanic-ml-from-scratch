from pathlib import Path
import ast, json, re
import nbformat
from IPython.core.inputtransformer2 import TransformerManager
root = Path(__file__).resolve().parents[1]
transformer = TransformerManager()
notebooks = list(root.glob("notebooks/*.ipynb"))
for path in notebooks:
    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    for i, cell in enumerate(nb.cells):
        if cell.cell_type == "code":
            compile(transformer.transform_cell(cell.source), f"{path.name}:cell-{i}", "exec")
            assert not cell.get("outputs"), "Published notebook must not contain captured data/output"
for path in root.rglob("*.py"):
    if ".git" not in path.parts:
        ast.parse(path.read_text(), filename=str(path))
for path in root.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    assert path.suffix.lower() not in {".pt", ".pth", ".ckpt", ".safetensors", ".gguf", ".zip", ".csv"} or str(path.relative_to(root)) == "results/consolidated_table.csv", f"Unexpected dataset/model/archive: {path}"
print(f"Validated {len(notebooks)} notebook(s), Python sources and publication exclusions. No training was run.")
