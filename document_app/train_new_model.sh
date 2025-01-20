#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <fine_tuning_dataset_path> <document_id>"
    exit 1
fi

fine_tuning_dataset_path=$1
document_id=$2

# generate new config file
python document_app/generate_fine_tuning_config.py \
    --fine_tuning_dataset_path ${fine_tuning_dataset_path} \
    --document_id ${document_id}

# fine tuning
python tools/train.py -c configs/det/document_${document_id}_fine_tuning.yml

# export
python tools/export_model.py -c configs/det/document_${document_id}_fine_tuning.yml \
    -o Global.pretrained_model=/models/document_${document_id}_model/best_accuracy
