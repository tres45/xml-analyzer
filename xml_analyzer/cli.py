from .analyzer import Analyzer

import sys


def main():
    original_path = sys.argv[1]
    target_path = sys.argv[2]
    id = sys.argv[3]

    analyzer = Analyzer(original_path, target_path, id)
    print(analyzer.diff_report)
