import sys

def add_dir_to_path(filepath = '.'):
    if filepath not in sys.path:
        sys.path.append(filepath)

add_dir_to_path('..')