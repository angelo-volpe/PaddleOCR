### Generate fine tuning conf
```
python -m document_app.generate_fine_tuning_config --fine_tuning_dataset_path /Users/volpea/Documents/projects/document-generator-job/data/fine_tuning_dataset --document_id 1
```

### Using docker
#### Training
```
docker build -f ./document_app_docker/Dockerfile_training -t paddle-ocr-document:latest .
docker run --rm \
           --mount type=bind,source=/Users/volpea/Documents/projects/document-generator-job/data,target=/data \
           --mount type=bind,source=/Users/volpea/Documents/projects/PaddleOCR/models,target=/models \
           --name document-generator-jobs \
           --shm-size=1gb \
           paddle-ocr-document:latest ./document_app/train_new_model.sh /data/fine_tuning_dataset 5
```