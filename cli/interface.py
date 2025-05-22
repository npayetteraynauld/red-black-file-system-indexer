import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="RBFS Indexer CLI"
    )
    subparsers = parser.add_subparsers(dest="command", required = True)
    
    # Scan command
    scan_parser = subparsers.add_parser(
        "scan",
        help = "scan and index a directory"
    )
    scan_parser.add_argument(
        "path",
        help = "path to scan"
    )
    
    # Search command
    search_parser = subparsers.add_parser(
        "search",
        help = "Search the index"
    )
    
    search_parser.add_argument(
        "--query",
        help = "what to search for (only needed for non_range queries)"
    )

    search_parser.add_argument(
        "--by",
        default = "file",
        help = "Field to search by: file(default), path, size"
    )

    search_parser.add_argument(
        "--contains",
        action = "store_true",
        help = "Enable partial string matching(slower)"
    )

    search_parser.add_argument(
        "--min-size",
        type = int,
        help = "Minimum file size"
    )

    search_parser.add_argument(
            "--max-size",
            type = int,
            help = "Maximum file size"
    )

    search_parser.add_argument(
        "--unit",
        choices = ["B", "KB", "MB", "GB"],
        default = "KB",
        help = "Unit for size (default: KB)"
    )
    return parser.parse_args()
