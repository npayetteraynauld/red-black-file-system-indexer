from utils.sort_keys import *
from utils.serializer import save_trees, load_trees
from cli.interface import parse_args
from cli.print import print_search_results
from rb_tree.tree import RBTree, print_rbtree
from indexer.scanner import scan_directory
from pathlib import Path
from indexer.metadata import format_size, format_mtime




def main_test():
    args = parse_args()

    if args.command == "scan":
        print(f"Scanning: {args.path}")

        #build the tree by path
        tree_by_path = RBTree()
        scan_directory(args.path, tree_by_path)

        #serialize the trees (default is data/index.pk1)
        save_trees(tree_by_path)
        print_rbtree(tree_by_path.root)

    elif args.command == "search":
        #load the trees (default is data/index.pk1)
        tree_by_path, = load_trees()
        
        results = tree_by_path.search_by(args.query, args.by, contains=args.contains)

        print_search_results(results)
        
        if False:
            print(f"\n🔍 Searching for '{args.query}' by {args.by}")
            if results:
                print(f"✅ {len(results)} Results Found:\n")
                for i, node in enumerate(results, 1):
                    val = node.val
                    print(f"{i}. Path     : {val.path}")
                    print(f"   Size     : {format_size(val.size)}")
                    print(f"   Modified : {format_mtime(val.modified)}")
                    print(f"   Type     : {val.type}\n")
            else:
                print("❌ No results found.")



if __name__=="__main__":
    main_test()

