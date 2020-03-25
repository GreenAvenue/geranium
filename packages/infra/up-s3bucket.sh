#!/bin/bash

CFN_INIT_TEMPLATE_FILE="s3bucket.yaml"
STACK_NAME_DEPLOY_BUCKET="apiTestS3Bucket"
BUCKET_HEADER="ga803-mts"

# TODO: Externalization.
ENVIRONMENT="local"

# TODO: Switching between LocalStack and AWS.
aws cloudformation create-stack \
    --template-body file://template/${CFN_INIT_TEMPLATE_FILE} \
    --stack-name ${STACK_NAME_DEPLOY_BUCKET} \
    --parameters ParameterKey=Header,ParameterValue=${BUCKET_HEADER} \
                 ParameterKey=Environment,ParameterValue=${ENVIRONMENT} \
    --profile localstack \
    --endpoint-url=http://localhost:4581
