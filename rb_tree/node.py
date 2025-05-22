from indexer.filemeta import FileMeta
from typing import Optional

class RBNode:
    def __init__(self, val: Optional[FileMeta] = None):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return self.val.file

    def __repr__(self):
        return f"file: {self.val.file}, path: {self.val.path} size: {self.val.size}, modified: {self.val.modified}, type: {self.val.type}"
        
