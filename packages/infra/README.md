
# infra

## 前提

- 以下がインストールされていること
  - git
  - docker
  - docker-compose
  - awscli

- bashが動作する環境であること

## セットアップ

- localstackの起動

```
cd geranium/packages/infra/
docker-compose up -d
```

## 使い方
基本的に、awscliコマンドに対してエンドポイントを指定するだけでOK  
(local-dev -> aws-prd への切替を考えると、
localstack用コマンド <-> AWS本番用コマンドに
自動コンバートできる仕組みが欲しくなる。)

### awscliの事前準備
```
$ aws configure --profile localstack
AWS Access Key ID [None]: dummy
AWS Secret Access Key [None]: dummy
Default region name [None]: us-east-1
Default output format [None]: text
```
Ex)
```
- To AWS service
$ aws cloudformation create-stack --template-body file://XXX.yaml --stack-name YYY

- To localstack
$ aws cloudformation --endpoint-url=http://localhost:4581 create-stack --template-body file://XXX.yaml --stack-name YYY
```

### endpoint 一覧 (デフォルト)
API Gateway at http://localhost:4567  
Kinesis at http://localhost:4568  
DynamoDB at http://localhost:4569  
DynamoDB Streams at http://localhost:4570  
S3 at http://localhost:4572  
Firehose at http://localhost:4573  
Lambda at http://localhost:4574  
SNS at http://localhost:4575  
SQS at http://localhost:4576  
Redshift at http://localhost:4577  
Elasticsearch Service at http://localhost:4578  
SES at http://localhost:4579  
Route53 at http://localhost:4580  
CloudFormation at http://localhost:4581  
CloudWatch at http://localhost:4582  
SSM at http://localhost:4583  
SecretsManager at http://localhost:4584  
StepFunctions at http://localhost:4585  
CloudWatch Logs at http://localhost:4586  
EventBridge (CloudWatch Events) at http://localhost:4587  
STS at http://localhost:4592  
IAM at http://localhost:4593  
EC2 at http://localhost:4597  
KMS at http://localhost:4599  
