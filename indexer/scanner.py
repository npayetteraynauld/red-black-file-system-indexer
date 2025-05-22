import os
from pathlib import Path
from rb_tree.tree import RBTree
from indexer.filemeta import FileMeta

def scan_directory(path: Path, tree: RBTree):
    for root, __, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)

            stat = os.stat(full_path)

            __, ext = os.path.splitext(full_path)

            file_info = {
                "file": file,
                "path": full_path,
                "size": stat.st_size,
                "mtime": stat.st_mtime,
                "type": ext.lstrip(".")
            }

            meta = FileMeta(file_info["file"],
                            file_info["path"],
                            file_info["size"],
                            file_info["mtime"],
                            file_info["type"]
                            )

            tree.insert(meta)
