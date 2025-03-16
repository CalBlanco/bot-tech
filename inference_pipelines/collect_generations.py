import re
import json
import yaml
import argparse
import pandas as pd
from pathlib import Path
import logging
import sys


def setup_logging(output_path):
    """Setup logging to both file and console."""
    log_file = Path(output_path).parent / "collect_generations.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )


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


def extract_labeled_texts(text):
    """Extract all texts between <labeled_text> tags from within generated_samples tags."""
    # First check if generated_samples tags exist
    generated_samples_pattern = r"<generated_samples>(.*?)</generated_samples>"
    generated_samples_match = re.search(generated_samples_pattern, text, re.DOTALL)

    if not generated_samples_match:
        return None

    # Extract texts between labeled_text tags
    labeled_text_pattern = r"<labeled_text>(.*?)</labeled_text>"
    labeled_texts = re.findall(
        labeled_text_pattern, generated_samples_match.group(1), re.DOTALL
    )

    return labeled_texts if labeled_texts else None


def process_dataset(df, column_to_explode):
    """Process the dataset and explode the specified column."""
    # Create a new list to store the exploded data
    exploded_data = []

    for idx, row in df.iterrows():
        text = row[column_to_explode]
        labeled_texts = extract_labeled_texts(text)

        if labeled_texts is None:
            logging.warning(
                f"Row {idx}: No valid generated samples found or missing tags"
            )
            continue

        # Create new rows for each labeled text, storing the text in the original column
        for labeled_text in labeled_texts:
            new_row = row.copy()
            new_row[column_to_explode] = labeled_text.strip()
            exploded_data.append(new_row)

    # Create new dataframe with the same column structure as the input
    return pd.DataFrame(exploded_data, columns=df.columns)


def main():
    parser = argparse.ArgumentParser(
        description="Process and explode generated samples from dataset."
    )
    parser.add_argument("--input_path", help="Path to input dataset")
    parser.add_argument("--output_path", help="Path to save processed dataset")
    parser.add_argument(
        "--column_to_explode", help="Column name containing the generated samples"
    )

    args = parser.parse_args()

    # Setup logging
    setup_logging(args.output_path)

    # Load dataset
    logging.info(f"Loading dataset from {args.input_path}")
    df = load_dataset(args.input_path)

    # Process and explode the dataset
    logging.info(f"Processing column: {args.column_to_explode}")
    processed_df = process_dataset(df, args.column_to_explode)

    # Save the processed dataset
    logging.info(f"Saving processed dataset to {args.output_path}")

    # Determine output format based on file extension
    output_ext = Path(args.output_path).suffix.lower()
    if output_ext == ".json":
        processed_df.to_json(args.output_path, orient="records", indent=2)
    elif output_ext == ".jsonl":
        processed_df.to_json(args.output_path, orient="records", lines=True)
    elif output_ext == ".csv":
        processed_df.to_csv(args.output_path, index=False)
    else:
        raise ValueError(f"Unsupported output format: {output_ext}")

    logging.info("Processing completed")


def test():
    """Test function to verify the script's functionality."""
    # Create a temporary test directory
    import tempfile
    import os
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test input data
        test_data = [
            {
                "id": 1,
                "other_col": "test1",
                "generations": """random text before
                <generated_samples>
                <labeled_text>
                Sample text 1
                </labeled_text>
                <labeled_text>
                Sample text 2
                </labeled_text>
                </generated_samples>
                random text after""",
            },
            {
                "id": 2,
                "other_col": "test2",
                "generations": "Invalid row without proper tags",
            },
            {
                "id": 3,
                "other_col": "test3",
                "generations": """<generated_samples>
                <labeled_text>
                Sample text 3
                </labeled_text>
                </generated_samples>""",
            },
        ]

        # Create test input file
        input_path = Path(tmpdir) / "test_input.json"
        with open(input_path, "w") as f:
            json.dump(test_data, f)

        # Set up output path
        output_path = Path(tmpdir) / "test_output.json"

        # Run the main processing
        df = load_dataset(input_path)
        setup_logging(output_path)
        processed_df = process_dataset(df, "generations")

        # Verify results
        assert len(processed_df) == 3, f"Expected 3 rows, got {len(processed_df)}"
        assert list(processed_df["generations"]) == [
            "Sample text 1",
            "Sample text 2",
            "Sample text 3",
        ], "Extracted text doesn't match expected output"
        assert all(
            processed_df["other_col"].isin(["test1", "test1", "test3"])
        ), "Other columns not preserved correctly"

        print("All tests passed!")

        # Test file format outputs
        for ext in [".json", ".jsonl", ".csv"]:
            test_output = Path(tmpdir) / f"test_output{ext}"
            if ext == ".json":
                processed_df.to_json(test_output, orient="records", indent=2)
            elif ext == ".jsonl":
                processed_df.to_json(test_output, orient="records", lines=True)
            else:
                processed_df.to_csv(test_output, index=False)
            assert test_output.exists(), f"Failed to create {ext} output file"

        print("File format tests passed!")

        # Test invalid input format
        try:
            invalid_path = Path(tmpdir) / "test.txt"
            invalid_path.touch()
            load_dataset(invalid_path)
            assert False, "Should have raised ValueError for invalid format"
        except ValueError:
            print("Invalid format test passed!")


if __name__ == "__main__":
    # test()
    main()
