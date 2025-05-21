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
        required = True,
        help = "what to search for"
    )

    search_parser.add_argument(
        "--by",
        default = "path",
        help = "Field to search by: path(default), size, modified"
    )

    search_parser.add_argument(
        "--contains",
        action = "store_true",
        help = "Enable partial string matching(slower)"
    )

    return parser.parse_args()
