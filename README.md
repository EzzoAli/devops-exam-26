# PGR301 EKSAMEN 2024 Couch Explorers - Bærekraftig turisme fra sofakroken ! 
# kandidat nr. 26

### Requierments:
- Python version 3.8
- `pip install -r requirements.txt`
- Terraform v1.9.8

### En Tabell av alle leveransene ligger neders i siden


##oppgave 1

### Oppgave 1a: AWS Lambda og API Gateway


### Denne komandoen er for å finne filstien til SAM-applicationen
```bash
cd devops-exam-26/sam_lambda/image-gen-26
```

### Denne komandoen bygger SAM-applikasjonenen 
```bash
sam build
```

### Denne komandoen deployer SAM-applikasjonen til AWS
```bash
sam deploy --guided
```

### Denne Komandoen er for å generer et bilde til PGR301-couch-explorers/26/images
```bash
curl -X POST https://s7u83tlgy1.execute-api.eu-west-1.amazonaws.com/Prod/generate-image/ \
-H "Content-Type: application/json" \
-d '{"prompt": "Vintage Paris Trip"}'\
--output json
```
### Her er url-en til PGR301-couch-explorers/26/images for å verifisere at et bilde blir generert
[PGR301-couch-explorers/26/images](https://eu-west-1.console.aws.amazon.com/s3/buckets/pgr301-couch-explorers?region=eu-west-1&bucketType=general&prefix=26/images/&showversions=false)

### leveranse 1a:

```
https://s7u83tlgy1.execute-api.eu-west-1.amazonaws.com/Prod/generate-image/
```


### Oppgave 1b: GitHub Actions Workflow for SAM Deploy
- **Lenke til workflow**: [Klikk for å se GitHub Actions Workflow for SAM Deploy](https://github.com/EzzoAli/devops-exam-26/actions/runs/11900918322/job/33162795154)



Oppgave 2 A & B

- **Lenke til terraform plan workflow (non-main branch)**: [GitHub Actions Workflow for Terraform plan](https://github.com/EzzoAli/devops-exam-26/actions/runs/11964862446/job/33357904173)
- 
- **Lenke til terraform apply workflow (main branch)**: [GitHub Actions Workflow for Terraform apply](https://github.com/EzzoAli/devops-exam-26/actions/runs/11945111658/job/33297209272)
```
https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26
```



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
- 


## oppgave 1
### Oppgave 1a: AWS Lambda og API Gateway
- **API Gateway URL**: https://s7u83tlgy1.execute-api.eu-west-1.amazonaws.com/Prod/generate-image/
- **generert bilde: 26/titan_1932720648.png**
### Oppgave 1b: GitHub Actions Workflow for SAM Deploy
- **Lenke til workflow**: [Se workflow-kjøring](https://github.com/EzzoAli/devops-exam-26/actions/runs/11900918322/job/33162795154)

