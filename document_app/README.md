### Generate fine tuning conf
```
python -m document_app.generate_fine_tuning_config --fine_tuning_dataset_path /Users/volpea/Documents/projects/document-generator-job/data/fine_tuning_dataset --document_id {document_id}
```

### Train Model
```
# fine tuning
python tools/train.py -c configs/det/document_{document_id}_fine_tuning.yml

# export
python tools/export_model.py -c configs/det/document_{document_id}_fine_tuning.yml -o Global.pretrained_model="./models/document_{document_id}_model/best_accuracy"
```

### Serving

specify the model to serve in deploy/hubserving/ocr_system/params.py

```
hub install deploy/hubserving/ocr_system

hub serving start -m ocr_system
```

### Using docker
#### Training
```
docker build -f ./document_app/Dockerfile_training -t paddle-ocr-document-training:latest .
docker run --rm \
           --mount type=bind,source=/Users/volpea/Documents/projects/document-generator-job/data,target=/data \
           --mount type=bind,source=/Users/volpea/Documents/projects/PaddleOCR/models,target=/models \
           --name document-generator-jobs \
           --shm-size=2gb \
           paddle-ocr-document:latest ./document_app/train_new_model.sh /data/fine_tuning_dataset {document_id}
```

#### Inference
```
DOCUMENT_ID={document_id} docker compose up
```