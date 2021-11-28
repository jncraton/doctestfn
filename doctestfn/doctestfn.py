import doctest
import argparse
import importlib
import sys
import os

def main():
    ap = argparse.ArgumentParser(description="Run doctests for one function")
    ap.add_argument("module", help="Module to load")
    ap.add_argument("function", help="Function to test")
    ap.add_argument("-v", "--verbose", help="Enable verbose doctest output", default=False, action='store_true')

    args = ap.parse_args()

    # Add working directory to module search path
    sys.path.append(os.getcwd())

    # Remove .py from filename if included by mistake
    # This helps with shell filename completion
    if args.module.endswith('.py'):
        args.module = args.module[:-3]

    # Import the module
    m = importlib.import_module(args.module)

    # Hoist everything to the needed global scope
    for attr in dir(m):
        if not attr.startswith('_'):
            globals()[attr] = getattr(m, attr)

    doctest.run_docstring_examples(globals()[args.function], globals(), verbose=args.verbose)

if __name__ == '__main__':
    main()
