import json
import argparse
import pandas as pd
from pathlib import Path
from typing import List, Tuple
import numpy as np


def load_dataset(input_dataset_path):
    """Load the dataset from the specified path."""
    # Determine file extension to handle different formats
    ext = Path(input_dataset_path).suffix.lower()

    if ext == ".json":
        with open(input_dataset_path, "r") as f:
            data = json.load(f)
        return pd.DataFrame(data)
    elif ext == ".jsonl":
        return pd.read_json(input_dataset_path, lines=True)
    elif ext == ".csv":
        return pd.read_csv(input_dataset_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")


def parse_spans(span_data):
    """Convert span string or list to list of tuples (start, end, label)."""
    if not span_data or span_data == "[]":  # Handle empty cases
        return []

    if isinstance(span_data, str):
        try:
            spans = json.loads(span_data)
        except json.JSONDecodeError:
            print(f"Warning: Could not parse span data: {span_data}")
            return []
    else:
        spans = span_data

    return [(span[0], span[1], span[2]) for span in spans]


def calc_span_f1_strict(span_1, span_2) -> int:
    """
    Calculate the strict F1 score for two spans
    if the spans have same start and end and label -> 1
    otherwise -> 0
    """
    s1, e1, l1 = span_1
    s2, e2, l2 = span_2

    # return 1 if spans line up and label is same
    if s1 == s2 and e1 == e2 and l1 == l2:
        return 1

    # return zero otherwise
    return 0


def calc_span_f1_relaxed(span_1, span_2) -> float:
    """
    Calculate the overlap between two spans with the same label
    if the labels are different -> 0
    if the spans do not overlap -> 0
    if the spans overlap -> overlap / union_length (value between 0 and 1)
    """
    s1, e1, l1 = span_1
    s2, e2, l2 = span_2

    # return 0 if labels are not the same
    if l1 != l2:
        return 0

    # get the overlap
    overlap_start = max(s1, s2)
    overlap_end = min(e1, e2)

    if overlap_start <= overlap_end:
        union_length = max(e1, e2) - min(s1, s2)
        return (overlap_end - overlap_start) / union_length

    # return 0 if no overlap
    return 0


def calculate_scores(gold_spans: List[Tuple], pred_spans: List[Tuple]):
    """
    Calculate strict and relaxed F1 scores between gold and predicted spans
    Returns average scores across all spans
    """
    if not gold_spans and not pred_spans:
        return 1.0, 1.0  # Both empty = perfect match
    if not gold_spans or not pred_spans:
        return 0.0, 0.0  # One empty = no match

    strict_scores = []
    relaxed_scores = []

    # Compare each gold span against each predicted span
    for gold_span in gold_spans:
        span_strict_scores = []
        span_relaxed_scores = []

        for pred_span in pred_spans:
            strict_score = calc_span_f1_strict(gold_span, pred_span)
            relaxed_score = calc_span_f1_relaxed(gold_span, pred_span)
            span_strict_scores.append(strict_score)
            span_relaxed_scores.append(relaxed_score)

        # Take best matching predicted span for each gold span
        strict_scores.append(max(span_strict_scores) if span_strict_scores else 0)
        relaxed_scores.append(max(span_relaxed_scores) if span_relaxed_scores else 0)

    # Calculate average scores
    avg_strict = np.mean(strict_scores)
    avg_relaxed = np.mean(relaxed_scores)

    return avg_strict, avg_relaxed


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate span predictions against gold standard"
    )
    parser.add_argument(
        "--input_path", required=True, help="Path to input file (json, jsonl, or csv)"
    )
    parser.add_argument(
        "--gold_span_col", required=True, help="Column name for gold standard spans"
    )
    parser.add_argument(
        "--predicted_span_col", required=True, help="Column name for predicted spans"
    )

    args = parser.parse_args()

    # Load dataset
    df = load_dataset(args.input_path)

    # Calculate scores for each row
    strict_scores = []
    relaxed_scores = []

    for _, row in df.iterrows():
        gold_spans = parse_spans(row[args.gold_span_col])
        pred_spans = parse_spans(row[args.predicted_span_col])

        strict, relaxed = calculate_scores(gold_spans, pred_spans)
        strict_scores.append(strict)
        relaxed_scores.append(relaxed)

    # Calculate and print overall metrics
    print(f"\nEvaluation Results:")
    print(f"Average Strict F1: {np.mean(strict_scores):.4f}")
    print(f"Average Relaxed F1: {np.mean(relaxed_scores):.4f}")


def test():
    """Test the span evaluation functionality with various scenarios"""
    # Test case 1: Exact match
    gold_spans_1 = [(0, 5, "PERSON")]
    pred_spans_1 = [(0, 5, "PERSON")]
    strict_1, relaxed_1 = calculate_scores(gold_spans_1, pred_spans_1)
    assert (
        strict_1 == 1.0 and relaxed_1 == 1.0
    ), "Test 1 failed: Exact match should give perfect scores"

    # Test case 2: No overlap
    gold_spans_2 = [(0, 5, "PERSON")]
    pred_spans_2 = [(6, 10, "PERSON")]
    strict_2, relaxed_2 = calculate_scores(gold_spans_2, pred_spans_2)
    assert (
        strict_2 == 0.0 and relaxed_2 == 0.0
    ), "Test 2 failed: No overlap should give zero scores"

    # Test case 3: Partial overlap, same label
    gold_spans_3 = [(0, 5, "PERSON")]
    pred_spans_3 = [(3, 8, "PERSON")]
    strict_3, relaxed_3 = calculate_scores(gold_spans_3, pred_spans_3)
    assert (
        strict_3 == 0.0 and relaxed_3 > 0.0
    ), "Test 3 failed: Partial overlap should give non-zero relaxed score"

    # Test case 4: Same span, different label
    gold_spans_4 = [(0, 5, "PERSON")]
    pred_spans_4 = [(0, 5, "ORG")]
    strict_4, relaxed_4 = calculate_scores(gold_spans_4, pred_spans_4)
    assert (
        strict_4 == 0.0 and relaxed_4 == 0.0
    ), "Test 4 failed: Different labels should give zero scores"

    # Test case 5: Empty spans
    gold_spans_5 = []
    pred_spans_5 = []
    strict_5, relaxed_5 = calculate_scores(gold_spans_5, pred_spans_5)
    assert (
        strict_5 == 1.0 and relaxed_5 == 1.0
    ), "Test 5 failed: Empty spans should give perfect scores"

    # Test case 6: Multiple spans
    gold_spans_6 = [(0, 5, "PERSON"), (10, 15, "ORG")]
    pred_spans_6 = [(0, 5, "PERSON"), (10, 15, "ORG")]
    strict_6, relaxed_6 = calculate_scores(gold_spans_6, pred_spans_6)
    assert (
        strict_6 == 1.0 and relaxed_6 == 1.0
    ), "Test 6 failed: Multiple exact matches should give perfect scores"

    # Test parsing functionality
    test_str = '[[0, 5, "PERSON"], [10, 15, "ORG"]]'
    parsed_spans = parse_spans(test_str)
    assert (
        len(parsed_spans) == 2
    ), "Test 7 failed: String parsing should handle multiple spans"
    assert parsed_spans[0] == (
        0,
        5,
        "PERSON",
    ), "Test 7 failed: Incorrect parsing of first span"

    print("All tests passed!")


if __name__ == "__main__":
    main()
    # test()
