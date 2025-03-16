#!/bin/bash

# Input files
INPUT_SPLIT_CSV="generation_inputs/generate_200_samples.csv"

# Directory paths
GENERATION_INPUTS_DIR="generation_inputs"
GENERATION_OUTPUTS_DIR="generation_outputs"
INFERENCE_PIPELINES_DIR="inference_pipelines"

# Dataset paths
GENERATION_DATASET="generation_inputs_70_30_v3"
DATASET_PATH="datasets/${GENERATION_DATASET}"
OUTPUT_CSV="${GENERATION_OUTPUTS_DIR}/${GENERATION_DATASET}.jsonl"

# Config files
CONFIG_FILE="${INFERENCE_PIPELINES_DIR}/inference_configs.yaml"

python ${INFERENCE_PIPELINES_DIR}/dataset_conversion.py --input_path ${INPUT_SPLIT_CSV} --output_path ${DATASET_PATH}
python -m inference_pipelines.inference_engine --input-dataset-path ${DATASET_PATH} --result-dataset-path ${DATASET_PATH} --section data_generation --config ${CONFIG_FILE}
python ${INFERENCE_PIPELINES_DIR}/dataset_conversion.py --input_path ${DATASET_PATH} --output_path ${OUTPUT_CSV}
python ${INFERENCE_PIPELINES_DIR}/collect_generations.py --input_path ${OUTPUT_CSV} --output_path ${OUTPUT_CSV} --column_to_explode "generated_text"
python ${INFERENCE_PIPELINES_DIR}/get_spans.py --input_path ${OUTPUT_CSV} --output_path ${OUTPUT_CSV} --config ${CONFIG_FILE} --section convert_llm_response_to_span_annotations_for_generation
python ${INFERENCE_PIPELINES_DIR}/spans_to_xml_tags.py --input_path ${OUTPUT_CSV} --output_path ${OUTPUT_CSV} --text_column "generated_text" --span_annotation_col label --xml_column "vizualize_spans"