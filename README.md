# rbfs_indexer - red-black-file-system-indexer

## About

rbfs_indexer is a command-tool that indexes a directory using a Red-Black Tree. It allows fast lookups and traversal of file paths and metadata.

This is my first unguided project! I wanted to learn how to actually use a self-balancing binary tree, and how to apply it to a practical problem.
I also got to practice my python knowledge.

## Features

- Efficient indexing of directories and files using a Red-Black Binary Tree
- Command-line interface for indexing and querying
- Customizable sorting (by path, size)
- Easy to read output

## installation

1. clone my repo: "git clone https://github.com/npayetteraynauld/red-black-file-system-indexer"
2. cd into it
3. (optional) set up a virtual environment: "python3 -m venv venv && source venv/bin/activate"
4. install requirements: pip install -r requirements.txt
5. another requirement is to have python3 installed on your machine
6. Done!

## Usage

### Indexing the Directory

- To scan a directory you have to run main.py with the "scan" command.
  - python3 main.py scan /path/to/target_directory

- You should then see a Scan complete message if it was successful

### Searching the Tree

- To search the newly made tree you have to use the "search" command.
  - "python3 main.py search"

- Default lookup is by exact file path matching which is the fastest option O(log n)
- When not searching by range use --query:
  - "python3 main.py search --query QUERY"

- If you want to fuzzy search (slower), use --contains:
  - "python3 main.py search --query QUERY --contains"

- Another option is to sort by size, use --by, default unit is "KB":
  - "python3 main.py search --by size"
- You can also add a max size or a min size, use --max-size and/or --min-size:
  - "python3 main.py search --by size --min-size SIZE"
- Units used can also be changed with --unit (B, KB, MB, GB):
  - "python3 main.py search --by size --max-size SIZE --unit UNIT"

- If input was correct, you should see a table containing metadata of each file found.

## Project Structure

<pre>  rbfs_indexer/ 
  ├── tree/ # Red-Black Tree implementation 
  ├── indexer/ # Logic for traversing filesystem and inserting into the tree 
  ├── cli/ # Command-line interface 
  └── utils/ # Helper functions  </pre>

## Plans for Future

- I want to polish up the CLI interface so that it is more user friendly.
- Would like to make the searching by size O(log n) eventually.
- Add an option to search by modification time
- Add an insert and delete option to the CLI to avoid rescanning after every change



