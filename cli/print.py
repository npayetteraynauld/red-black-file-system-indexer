from rich.console import Console
from rich.table import Table
from indexer.metadata import format_size, format_mtime

def print_search_results(results):
    console = Console()
    table = Table(title="Search Results")

    table.add_column("#", style="cyan", no_wrap=True)
    table.add_column("Path", style="magenta")
    table.add_column("Size", justify="right", style="green")
    table.add_column("Modified", style="yellow")
    table.add_column("Type", style="blue")

    for i, node in enumerate(results, 1):
        val = node.val
        # assuming val.path, val.size, val.modified, val.type exist
        table.add_row(
            str(i),
            val.path,
            format_size(val.size),
            format_mtime(val.modified),
            val.type
        )
    
    console.print(table)
