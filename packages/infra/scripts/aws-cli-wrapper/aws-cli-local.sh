#!/bin/bash

function before() {
	readonly execDir=`pwd`
	readonly scriptDir=$(cd $(dirname $0); pwd)
	cd $scriptDir
}

function after() {
	cd $execDir
}

function getPort() {
  case $1 in
  "ec2")
    echo "4597";;

  "kms")
    echo "4599";;

  "iam")
    echo "4593";;

  "sts")
    echo "4592";;

  # TODO: aws commandだとevens??
  # "eventbridge")
  #   echo "4587";;

  "cloudwatch")
    echo "4586";;

  "stepfunctions")
    echo "4585";;

  "secretsmanager")
    echo "4584";;

  "ssm")
    echo "4583";;

  "cloudwatch")
    echo "4582";;

  "cloudformation")
    echo "4581";;

  "route53")
    echo "4580";;

  "ses")
    echo "4579";;

  "elasticsearch")
    echo "4578";;

  "redshift")
    echo "4577";;

  "sqs")
    echo "4576";;

  "sns")
    echo "4575";;

  "lambda")
    echo "4574";;

  "firehose")
    echo "4573";;

  "s3")
    echo "4572";;

  "dynamodbstreams")
    echo "4570";;

  "dynamodb")
    echo "4569";;

  "kinesis")
    echo "4568";;

  "API")
    echo "4567";;

  "s3")
    echo "4572";;

  "s3")
    echo "4567";;

  *)
    exit 1;
  esac
}

function main() {
  local port=`getPort $1`
  aws $@ --endpoint-url=${BASE_URL}:${port}
}

before
. ./.env-local
main $@
after
