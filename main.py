from utils.sort_keys import *
from utils.serializer import save_trees, load_trees
from cli.interface import parse_args
from cli.print import print_search_results
from rb_tree.tree import RBTree, print_rbtree
from indexer.scanner import scan_directory
from pathlib import Path
from indexer.metadata import format_size, format_mtime
from rich import print




def main():
    args = parse_args()

    if args.command == "scan":
        print(f"Scanning: {args.path}")

        #build the tree by path
        tree_by_file = RBTree()
        scan_directory(args.path, tree_by_file)

        print("[green]Scan complete![/green]")

        #serialize the trees (default is data/index.pk1)
        save_trees(tree_by_file)

    elif args.command == "search":
        #load the trees (default is data/index.pk1)
        tree_by_file, = load_trees()
        
        if args.by == "size":
            min_size = args.min_size if args.min_size is not None else 0
            max_size = args.max_size if args.max_size is not None else float("inf")
            results = tree_by_file.range_search_by(min_size, max_size, unit=args.unit)


        elif args.query:
           results = tree_by_file.search_by(args.query, args.by, contains=args.contains)

        else:
            print("❌ Either provide a --query or a valid size range with --min-size/--max-size")
            return


        print_search_results(results)
        


if __name__=="__main__":
    main()

