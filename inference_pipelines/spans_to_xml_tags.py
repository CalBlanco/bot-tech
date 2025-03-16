import re
import json
import yaml
import argparse
import pandas as pd
from pathlib import Path


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


def insert_xml_tags(text, spans):
    """Insert XML tags into text based on span annotations."""
    # Sort spans by start position, then by end position (longer spans first)
    sorted_spans = sorted(spans, key=lambda x: (x[0], -x[1]))

    # Create list of tag insertions (position, tag)
    insertions = []
    for start, end, label in sorted_spans:
        insertions.append((start, f"<{label}>"))
        insertions.append((end, f"</{label}>"))

    # Sort insertions in reverse order to maintain positions
    insertions.sort(key=lambda x: x[0], reverse=True)

    # Insert tags
    result = text
    for pos, tag in insertions:
        result = result[:pos] + tag + result[pos:]

    return result


def process_dataset(df, text_column, span_column, xml_column):
    """Process dataset to add XML annotations."""
    df[xml_column] = df.apply(
        lambda row: insert_xml_tags(row[text_column], parse_spans(row[span_column])),
        axis=1,
    )
    return df


def save_dataset(df, output_path):
    """Save the dataset in the appropriate format based on file extension."""
    ext = Path(output_path).suffix.lower()

    if ext == ".json":
        df.to_json(output_path, orient="records", indent=2)
    elif ext == ".jsonl":
        df.to_json(output_path, orient="records", lines=True)
    elif ext == ".csv":
        df.to_csv(output_path, index=False)
    else:
        raise ValueError(f"Unsupported output format: {ext}")


def test():
    """Test the XML tag insertion functionality with sample data."""
    # Create test DataFrame
    test_data = [
        {
            "text": "The world needs to wake up, read a book, listen to the very few remaining survivors, see the obvious, stand up to that hate. Control the narrative before we slip into darkness once again.",
            "spans": '[[0, 123, "emotional_fallacy"], [125, 186, "emotional_fallacy"]]',
        },
        {
            "text": "This is a test with overlapping spans.",
            "spans": [[0, 20, "span1"], [15, 30, "span2"]],  # Overlapping spans
        },
        {
            "text": "Multiple labels in same text.",
            "spans": [
                [0, 8, "label1"],
                [9, 15, "label2"],
                [16, 25, "label3"],
            ],  # Adjacent spans
        },
    ]

    # df = pd.DataFrame(test_data)
    df = load_dataset("generation_outputs/generation_inputs_70_30.csv")

    # Process the test data
    result_df = process_dataset(df, "generated_text", "label", "vizualize_spans")

    # Print results
    print("\nTest Results:")
    for i, row in result_df.iterrows():
        print(f"\nTest case {i + 1}:")
        print(f"Original text: {row['text']}")
        print(f"Spans: {row['spans']}")
        print(f"XML result: {row['xml_text']}")
        print("-" * 80)


def main():
    parser = argparse.ArgumentParser(description="Convert span annotations to XML tags")
    parser.add_argument("--input_path", required=True, help="Path to input dataset")
    parser.add_argument(
        "--output_path", required=True, help="Path to save output dataset"
    )
    parser.add_argument(
        "--text_column", required=True, help="Column containing input text"
    )
    parser.add_argument(
        "--span_annotation_col",
        required=True,
        help="Column containing span annotations",
    )
    parser.add_argument(
        "--xml_column", required=True, help="Name for the new XML-formatted column"
    )

    args = parser.parse_args()

    # Load dataset
    df = load_dataset(args.input_path)

    # Process dataset
    df = process_dataset(
        df, args.text_column, args.span_annotation_col, args.xml_column
    )

    # Save results
    save_dataset(df, args.output_path)


if __name__ == "__main__":
    main()  # Comment out main()
    # test()  # Run test() instead
