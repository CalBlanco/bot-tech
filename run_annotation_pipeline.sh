#!/bin/bash

# Input files
INPUT_FILE="data/split_0.3_0.7/gold_0.7.csv"
ANNOTATION_OUTPUTS_DIR="annotation_outputs"
INFERENCE_PIPELINES_DIR="inference_pipelines"

# Dataset paths
ANNOTATION_DATASET="annotation_inputs_70_30_v3"
DATASET_PATH="datasets/${ANNOTATION_DATASET}"
OUTPUT_FILE="${ANNOTATION_OUTPUTS_DIR}/${ANNOTATION_DATASET}.jsonl"

# Config files
CONFIG_FILE="${INFERENCE_PIPELINES_DIR}/inference_configs.yaml"


# Step 1: Convert input dataset to desired format
# Converts the input JSONL file to a processed dataset, keeping only the "text" column
python -m inference_pipelines.dataset_conversion --input_path ${INPUT_FILE} --output_path ${DATASET_PATH}

# Step 2: Run LLM inference for data annotation
# Uses the configuration specified in inference_configs.yaml to run inference using the specified LLM
python -m inference_pipelines.inference_engine --input-dataset-path ${DATASET_PATH} --result-dataset-path ${DATASET_PATH} --config ${CONFIG_FILE} --section data_annotation 

# Step 3: Covert dataset to 
python -m inference_pipelines.dataset_conversion --input_path ${DATASET_PATH} --output_path ${OUTPUT_FILE}

# Step 4: Extract span annotations from LLM responses
# Converts XML-style tagged responses into span annotations in the format [start, end, label]
python -m inference_pipelines.get_spans --input_path ${OUTPUT_FILE} --output_path ${OUTPUT_FILE} --config ${CONFIG_FILE} --section convert_llm_response_to_span_annotations

# Step 5: Calculate F1 scores using IoU
# between annotations on a sample of 180 instances, excluding "non-fallacy" labels
python scripts/evaluate.py --input_path ${OUTPUT_FILE} --gold_span_col "final_annotation" --predicted_span_col "generated_annotations"
