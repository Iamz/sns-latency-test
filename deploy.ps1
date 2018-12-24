Remove-Item .\.aws-sam\ -Recurse -Force
sam build
Set-Location .aws-sam\build
sam package --output-template-file packaged.yaml --s3-bucket temp.codetism-poc --profile codetism-poc
sam deploy --template-file packaged.yaml --stack-name sns-latency-test --capabilities CAPABILITY_IAM --profile codetism-poc
Set-Location ..\..\