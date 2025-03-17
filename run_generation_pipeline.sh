#!/bin/bash

# Input files
INPUT_FILE="generation_inputs/generate_200_samples.csv"

# Directory paths
GENERATION_INPUTS_DIR="generation_inputs"
GENERATION_OUTPUTS_DIR="generation_outputs"
INFERENCE_PIPELINES_DIR="inference_pipelines"

# Dataset paths
GENERATION_DATASET="generation_inputs_70_30_v3"
DATASET_PATH="datasets/${GENERATION_DATASET}"
OUTPUT_FILE="${GENERATION_OUTPUTS_DIR}/${GENERATION_DATASET}.jsonl"

# Config files
CONFIG_FILE="${INFERENCE_PIPELINES_DIR}/inference_configs.yaml"

# convert the base label .csv file to a hf dataset for the inference_engine
python ${INFERENCE_PIPELINES_DIR}/dataset_conversion.py --input_path ${INPUT_FILE} --output_path ${DATASET_PATH}

# run the inference engine on the hf dataset and add a new column with the llm responses
python -m inference_pipelines.inference_engine --input-dataset-path ${DATASET_PATH} --result-dataset-path ${DATASET_PATH} --section data_generation --config ${CONFIG_FILE}

# convert the hf dataset into a .csv or .jsonl
python ${INFERENCE_PIPELINES_DIR}/dataset_conversion.py --input_path ${DATASET_PATH} --output_path ${OUTPUT_FILE}

# for each row in the input dataset, the llm will generate multiple sample outputs. These need to be cleaned and exploded.
python ${INFERENCE_PIPELINES_DIR}/collect_generations.py --input_path ${OUTPUT_FILE} --output_path ${OUTPUT_FILE} --column_to_explode "generated_text"

# the llm generated reponse is a text sentence with xml tags, for ex : <emotional_fallacy>this is a bad script</emotional_fallacy>.
# This raw llm outputs need to be converted to span labels ie. [[0, 23, "emotional_fallacy"]]
python ${INFERENCE_PIPELINES_DIR}/get_spans.py --input_path ${OUTPUT_FILE} --output_path ${OUTPUT_FILE} --config ${CONFIG_FILE} --section convert_llm_response_to_span_annotations_for_generation

# The previous script will clean all xml tags from the llm outputs. for easier vizualization of the text spans we create a new column with the xml tags added back into the text sentence.
python ${INFERENCE_PIPELINES_DIR}/spans_to_xml_tags.py --input_path ${OUTPUT_FILE} --output_path ${OUTPUT_FILE} --text_column "generated_text" --span_annotation_col label --xml_column "vizualize_spans"