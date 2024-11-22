# PGR301 EKSAMEN 2024 Couch Explorers - Bærekraftig turisme fra sofakroken ! 
# kandidat nr. 26


### requierments:
- python version 3.8
- pip install -r requirements.txt
- Terraform v1.9.8
- 

### filsti 
- python filen ligger i:
```bash
cd devops-exam-26/sam_lambda/image-gen-26



- 
## oppgave 1
### Oppgave 1a: AWS Lambda og API Gateway
- **API Gateway URL**: https://s7u83tlgy1.execute-api.eu-west-1.amazonaws.com/Prod/generate-image/
- **generert bilde: 26/titan_1932720648.png**
### Oppgave 1b: GitHub Actions Workflow for SAM Deploy
- **Lenke til workflow**: [Se workflow-kjøring](https://github.com/EzzoAli/devops-exam-26/actions/runs/11900918322/job/33162795154)

## oppgave 2
### Requierments
- **Terraform Version**: v1.9.8

### Deliverables
- **Lambda Function ARN**: `arn:aws:lambda:eu-west-1:244530008913:function:image-gen-lambda-26`
- **SQS Queue URL**: `https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26`
- **generert bilde: 26/images/titan_1821139106.png**

## Task 2B: GitHub Actions Workflow for Terraform
### Deliverables
- **Terraform Apply Workflow (main branch)**: https://github.com/EzzoAli/devops-exam-26/actions/runs/11945111658/job/33297209272
- **Terraform Plan Workflow (non-main branch)**: https://github.com/EzzoAli/devops-exam-26/actions/runs/11964862446/job/33357904173
- **SQS Queue URL**: [https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26](https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26)

## task 3a
##task 3b
###begrunnelse
- For mitt Docker-image har jeg bestemt meg for å velge latest som tag.
- Dette sikrer at man alltid har tilgang til den nyeste versjonen av klienten,
- uten å måtte velge en spesifikk versjon. I tillegg er latest standardtaggen
- ifølge Docker-dokumentasjonen, noe som gjør den enklere å bruke.
- url til github workflow: https://github.com/EzzoAli/devops-exam-26/actions/runs/11965712974
- Docker Hub Image: ezzoali/java-sqs-client:latest
- **SQS Queue URL**: `https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26`
