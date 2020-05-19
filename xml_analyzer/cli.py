from .analyzer import Analyzer

import sys


def main():
    original_path = sys.argv[1]
    target_path = sys.argv[2]
    if len(sys.argv) == 3:
        id = 'make-everything-ok-button'
    else:
        id = sys.argv[3]

    analyzer = Analyzer(original_path, target_path, id)
    print(analyzer.diff_report)
