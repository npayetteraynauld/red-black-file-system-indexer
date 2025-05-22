from datetime import datetime

def format_size(size_bytes) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"

    elif size_bytes < 1024 ** 2:
        size_bytes /= 1024 
        return f"{int(size_bytes)} KB"

    elif size_bytes < 1024 ** 3:
        size_bytes /= 1024 ** 2
        return f"{int(size_bytes)} MB"

    else:
        size_bytes /= 1024 ** 3
        return f"{int(size_bytes)} GB"

def format_mtime(mtime: float) -> str:
    readable_time = datetime.fromtimestamp(int(mtime))
    return f"{readable_time}"
