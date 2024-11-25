# PGR301 EKSAMEN 2024 Couch Explorers - Bærekraftig turisme fra sofakroken ! 
# kandidat nr. 26

### Requierments:
- Python version 3.8
- `pip install -r requirements.txt`
- Terraform v1.9.8

### En Tabell av alle leveransekravene ligger nederst siden siden



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



# Oppgave 2 A & B

### Klikk på den blå teksten for å se GitHub Actions workflow av en non-main branch

- **Lenke til terraform plan workflow (non-main branch)**: 
- [GitHub Actions Workflow for Terraform plan](https://github.com/EzzoAli/devops-exam-26/actions/runs/11964862446/job/33357904173)

### Klikk på den blå teksten for å se GitHub Actions workflow av en main branch
- **Lenke til terraform apply workflow (main branch)**: 
- [GitHub Actions Workflow for Terraform apply](https://github.com/EzzoAli/devops-exam-26/actions/runs/11945111658/job/33297209272)

### Her er min SQS Queue URL
```
https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26
```


# Automatisering og kontinuerlig levering (CI/CD)

## Serverless i CI/CD

Serverless tilbyr en strømlinjeformet opplevelse for CI/CD ved å automatisere nøkkelprosesser i utviklingslivssyklusen, redusere driftsbelastning og muliggjøre sømløse utrullinger. Imidlertid kan integrering av serverless i tradisjonelle CI/CD-pipelines kreve tilpasning til dens hendelsesdrevne og skyspesifikke arbeidsflyter.

### Fordeler:
- **Automatisering og forenkling**:  
  Serverless forbedrer automatisering ved å integrere med CI/CD-pipelines for å utløse bygg, tester og utrullinger ved kodeendringer, noe som akselererer utgivelsessykluser betydelig.
- **Raske iterasjoner**:  
  Automatisert testing og utrulling i serverless-pipelines forbedrer pålitelighet og hastighet i programvareleveransen.

### Ulemper:
- **Pipeline-tilpasning**:  
  Tilpasning av CI/CD-pipelines for serverless kan introdusere utfordringer, spesielt når det gjelder integrering med hendelsesdrevne, skyspesifikke plattformer.
- **Risiko for hot patching**:  
  Den enkle muligheten til å modifisere serverless-funksjoner direkte i produksjon kan føre til at strukturerte CI/CD-praksiser omgås, noe som kan resultere i inkonsekvenser.

---

## Mikrotjenester i CI/CD

Mikrotjenester passer godt med tradisjonelle CI/CD-tilnærminger på grunn av deres modulære natur, som tillater uavhengig utrulling av tjenester. Imidlertid introduserer den distribuerte naturen til mikrotjenester operasjonell kompleksitet.

### Fordeler:
- **Detaljert kontroll**:  
  Mikrotjenestenes modulære design støtter isolert testing og utrulling, noe som sikrer stabilitet for andre deler av systemet.
- **Tradisjonell kompatibilitet**:  
  Eksisterende CI/CD-pipelines kan ofte gjenbrukes med minimale justeringer for containerbaserte mikrotjenester.

### Ulemper:
- **Operasjonell belastning**:  
  Å opprettholde separate CI/CD-pipelines for flere mikrotjenester øker kompleksiteten og krever robust koordinering.
- **Begrenset skalerbarhet**:  
  Skalering av mikrotjenesteinfrastruktur er mindre dynamisk sammenlignet med serverless, noe som potensielt kan bremse CI/CD-prosesser under høy etterspørsel.

---

# Observability (Overvåkning)

## Hvordan endres overvåkning, logging og feilsøking når man går fra mikrotjenester til en serverless arkitektur?

### Serverless Arkitektur

Serverless-arkitekturer introduserer nye paradigmer for overvåkning og logging, samtidig som de gir fordeler som enklere oppsett og kostnadseffektive løsninger. Imidlertid fører den kortvarige og statsløse naturen til utfordringer innen feilsøking og logging.

#### Fordeler:
- **Effektive overvåkningsverktøy**:  
  Plattformspesifikke verktøy som Serverless Framework og AWS Lambda gir omfattende metrikker, spor, logger og feilmeldinger. Distribuerte sporingsverktøy som AWS X-Ray og OpenTelemetry gir innsikt i forsinkelser og samhandling mellom tjenester.
- **Enkel oppsett**:  
  Automatisert instrumentering, inkludert IAM-rolleintegrasjon og Lambda-lag, forenkler oppsamling av logger og spor. Sentralisert logging gjennom verktøy som AWS CloudWatch forenkler aggregering av kortvarige funksjonslogger.
- **Kostnadseffektivitet gjennom prøvetaking**:  
  Automatisk prøvetaking av sporingsdata optimaliserer overvåkningskostnader, spesielt for funksjoner med høy trafikk.

#### Utfordringer:
- **Økt kompleksitet i logging og feilsøking**:  
  Kortvarige funksjoner gjør det utfordrende å opprettholde loggingskontekster på tvers av flere kall. Krever standardiserte loggingsformater og sentraliserte aggregeringsverktøy.
- **Spredt overvåkningskontekst**:  
  Applikasjoner deles opp i mange små funksjoner, noe som kan skape utfordringer i distribuert logging. Overvåkning krever separate oppsett for hundrevis av funksjoner.
- **Overvåkning av "cold starts"**:  
  "Cold starts" introduserer latens som påvirker brukeropplevelsen. Spesifikke verktøy må brukes for å spore og måle disse forsinkelsene.
- **Avhengighet av plattformspesifikke verktøy**:  
  Plattformverktøy kan være vanskelig å integrere med eksterne løsninger og migrasjon til andre plattformer.

---

### Mikrotjenester Arkitektur

Mikrotjenester er modulære og uavhengige, noe som gir mer strukturert overvåkning og feilsøking. Likevel kan den distribuerte naturen føre til operasjonell kompleksitet.

#### Fordeler:
- **Strukturert overvåkning**:  
  Mikrotjenester benytter containere med en veldefinert livssyklus, noe som gjør integrasjon med eksisterende overvåkningsverktøy enklere. Tradisjonelle loggings- og overvåkningsarbeidsflyter kan brukes på nytt.
- **Komponentbasert feilsøking**:  
  Isolert logging og feilsøking på tvers av uavhengige tjenester. Modulenes uavhengighet sikrer at problemer kan isoleres uten å påvirke hele systemet.

#### Utfordringer:
- **Operasjonell kompleksitet**:  
  Krever separate overvåkningsoppsett for hver tjeneste, noe som øker administrasjonsbelastningen. Spor og logger må samles og aggregeres fra flere kilder.
- **Ressursadministrasjonsbelastning**:  
  Mikrotjenester krever dedikert infrastruktur, noe som øker kostnadene og administrativ kompleksitet. Overvåkningsløsninger må kontinuerlig justeres under høy trafikk.

---

# Skalerbarhet og kostnadskontroll

## Serverless

Serverless utmerker seg med dynamisk skalering og kostnadseffektivitet, noe som gjør det ideelt for applikasjoner med varierende arbeidsbelastninger. Modellen introduserer imidlertid utfordringer som uforutsigbare kostnader og kaldstartlatens.

### Fordeler:
- **Dynamisk skalering**:  
  Serverless justerer seg automatisk til endringer i arbeidsbelastning, noe som sikrer effektiv ressursbruk uten manuell inngripen.
- **Kostnadseffektivitet**:  
  Betal-for-bruk-prising eliminerer utgifter til inaktiv infrastruktur, noe som tilpasser kostnadene til faktisk bruk.

### Ulemper:
- **Uforutsigbare kostnader**:  
  Autoskalering kan føre til svingende utgifter, noe som utfordrer utviklere til å holde budsjettet under kontroll.
- **Kaldstartlatens**:  
  Serverless-funksjoner kan oppleve forsinkelser under oppstart, noe som påvirker ytelsen for tidskritiske oppgaver.

---

## Mikrotjenester

Mikrotjenester gir presis kontroll over ressursallokering og forutsigbare driftskostnader, men de er mindre smidige i skalering sammenlignet med serverless-arkitekturer.

### Fordeler:
- **Kontrollert ressursallokering**:  
  Ressurser kan tilpasses hver tjenestes behov, noe som optimaliserer ytelse og kostnader.
- **Forutsigbare kostnader**:  
  Forhåndskonfigurert infrastruktur sikrer konsistente utgifter og unngår uforutsigbare serverless-kostnader.

### Ulemper:
- **Manuell skalering**:  
  Skalering av mikrotjenester krever manuell innsats eller kompleks orkestrering, noe som gjør dem mindre responsive til plutselige trafikkøkninger.
- **Høyere infrastrukturkostnader**:  
  Å opprettholde infrastruktur for kontinuerlig kjørende tjenester kan føre til høyere grunnkostnader sammenlignet med serverless.

---

# Eierskap og ansvar

## Hvordan påvirkes DevOps-teamets eierskap og ansvar for applikasjonens ytelse, pålitelighet og kostnader ved overgang til en serverless tilnærming sammenlignet med en mikrotjeneste-tilnærming?

## Serverless: Eierskap og ansvar

I en serverless-tilnærming blir mange operasjonelle oppgaver overført til skyleverandøren. Dette frigjør DevOps-teamet fra mye av infrastrukturansvaret, men gir også nye utfordringer relatert til observabilitet, sikkerhet og kostnadshåndtering.

### Fordeler:
- **Redusert operasjonell belastning**:  
  Skyleverandøren tar seg av serverklargjøring, vedlikehold og skalering, noe som lar DevOps-teamet fokusere på applikasjonslogikk og ytelse.
- **Granulært ansvar**:  
  Individuelle funksjoner håndteres separat med minimal tilgang, i tråd med prinsippet om minst privilegium. Dette forbedrer sikkerheten og begrenser påvirkningen av potensielle feil.
- **Bedret samarbeid og CI/CD-integrasjon**:  
  Automatisering av serverless-pipelines reduserer tiden brukt på infrastrukturadministrasjon og støtter en modell med delt ansvar på tvers av team.

### Ulemper:
- **Kompleks rolle- og tillatelseshåndtering**:  
  Å tildele riktige roller til mange små funksjoner kan være komplekst og risikere feilkonfigurasjoner, noe som kan føre til sikkerhetsbrudd eller ineffektiv drift.
- **Utfordringer med kortvarige funksjoner**:  
  Tilstandsfrie funksjoner krever avhengighet av sentralisert overvåkningsverktøy for feilsøking og observabilitet, noe som legger til et ekstra lag av kompleksitet.
- **Uforutsigbare kostnader**:  
  Dynamisk skalering kan føre til varierende kostnader, og DevOps-team må kontinuerlig overvåke og optimalisere bruken for å unngå budsjettoverskridelser.

---

## Mikrotjenester: Eierskap og ansvar

Mikrotjeneste-tilnærmingen gir DevOps-teamet mer kontroll over infrastruktur og applikasjonskomponenter, men medfører også et høyere operasjonelt ansvar.

### Fordeler:
- **Klare eierskapsgrenser**:  
  Den modulære arkitekturen til mikrotjenester gjør det enklere for team å ha spesifikt ansvar for enkelte tjenester, noe som forenkler administrasjon og vedlikehold.
- **Forutsigbar ressursallokering**:  
  Dedikert infrastruktur gir teamet mulighet til å forutsi ressursbruk og kostnader, noe som gir bedre kontroll over budsjetter.

### Ulemper:
- **Økt operasjonell belastning**:  
  Administrasjon av infrastruktur og opprettholdelse av pipelines for flere mikrotjenester kan kreve betydelig tid og ressurser fra DevOps-teamet.
- **Orkestreringsutfordringer**:  
  Skalering av mikrotjenester krever ofte manuell innsats eller avanserte orkestreringsverktøy, noe som kan forsinke responstider.
- **Utvidet ansvarsområde**:  
  DevOps-teamet har ansvar for hele livssyklushåndteringen, inkludert sikkerhet, klargjøring og skalering, noe som kan være ressurskrevende.

---

## Oppsummering

**Serverless** reduserer operasjonelle oppgaver ved å flytte mye ansvar til skyleverandøren, men gir utfordringer med observabilitet og kostnadskontroll. **Mikrotjenester** gir mer kontroll og forutsigbarhet, men krever betydelig innsats for å håndtere infrastrukturen. Valget mellom serverless og mikrotjenester bør baseres på teamets kapasitet, systemets kompleksitet og applikasjonens krav.


kilder:
https://www.harness.io/blog/cicd-for-serverless (oppg 1 og 3)

https://www.serverless.com/framework/docs/guides/dashboard/monitoring (oppgave 2)
https://www.withcoherence.com/articles/serverless-monitoring-7-best-practices-2024 (oppgave 2)

https://medium.com/@jorgenlybeck/serverless-et-paradigmeskifte-i-systemutvikling-556a24fb9bd6 (oppgave 1 og 3)

https://devops.com/5-serverless-challenges-of-devops-teams-and-how-to-overcome-them/?utm_source=chatgpt.com (oppgave 4)
https://www.simform.com/blog/devops-best-practices-for-serverless/?utm_source=chatgpt.com (oppgave 4)
https://devops.com/running-serverless-in-production-7-best-practices-for-devops/?utm_source=chatgpt.com (oppgave 4)






## task 3a
##task 3b
###begrunnelse
- For mitt Docker-image har jeg bestemt meg for å velge latest som tag. Dette sikrer at man alltid har tilgang til den nyeste versjonen av klienten, uten å måtte velge en spesifikk versjon. I tillegg står det i Docker-dokumentasjonen at taggen latest er standardtaggen, noe som gjør den enklere å bruke.
- url til github workflow: https://github.com/EzzoAli/devops-exam-26/actions/runs/11965712974
- Docker Hub Image: ezzoali/java-sqs-client:latest
- **SQS Queue URL**: `https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26`
- 

## 


## oppgave 1
### Oppgave 1a: AWS Lambda og API Gateway
- **API Gateway URL**: https://s7u83tlgy1.execute-api.eu-west-1.amazonaws.com/Prod/generate-image/
- **generert bilde: 26/titan_1932720648.png**
### Oppgave 1b: GitHub Actions Workflow for SAM Deploy
- **Lenke til workflow**: [Se workflow-kjøring](https://github.com/EzzoAli/devops-exam-26/actions/runs/11900918322/job/33162795154)

### Deliverables
- **Lambda Function ARN**: `arn:aws:lambda:eu-west-1:244530008913:function:image-gen-lambda-26`
- **SQS Queue URL**: `https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26`
- **generert bilde: 26/images/titan_1821139106.png**

## Task 2B: GitHub Actions Workflow for Terraform
### Deliverables
- **Terraform Apply Workflow (main branch)**: https://github.com/EzzoAli/devops-exam-26/actions/runs/11945111658/job/33297209272
- **Terraform Plan Workflow (non-main branch)**: https://github.com/EzzoAli/devops-exam-26/actions/runs/11964862446/job/33357904173
- **SQS Queue URL**: [https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26](https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26)


##task 3
###begrunnelse
- For mitt Docker-image har jeg bestemt meg for å velge latest som tag. Dette sikrer at man alltid har tilgang til den nyeste versjonen av klienten, uten å måtte velge en spesifikk versjon. I tillegg står det i Docker-dokumentasjonen at taggen latest er standardtaggen, noe som gjør den enklere å bruke.
- url til github workflow: https://github.com/EzzoAli/devops-exam-26/actions/runs/11965712974
- Docker Hub Image: ezzoali/java-sqs-client:latest
- **SQS Queue URL**: `https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26`



## Tabell for leveranse krav


| Oppgave      | Leveransekrav                                         | Leveranse                                                                          |
|--------------|-------------------------------------------------------|------------------------------------------------------------------------------------|
| Oppgave 1a   | HTTP Endepunkt                                        | https://s7u83tlgy1.execute-api.eu-west-1.amazonaws.com/Prod/generate-image/        |
| Oppgave 1b   | SAM-application Lenke til GitHub Actions workflow     | https://github.com/EzzoAli/devops-exam-26/actions/runs/11900918322/job/33162795154 |
| Oppgave 2    | Lenke til Terraform Apply workflow (main branch)      | https://github.com/EzzoAli/devops-exam-26/actions/runs/11945111658/job/33297209272 |
|              | Lenke til Terraform Plan workflow (non-main branch)   | https://github.com/EzzoAli/devops-exam-26/actions/runs/11964862446/job/33357904173 |
|              | SQS-Kø URL                                            | https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26                |
| Oppgave 3    | Beskrivelse av taggestrategi                          | For mitt Docker-image har jeg bestemt meg for å velge `latest` som tag. Dette sikrer at man alltid har tilgang til den nyeste versjonen av klienten, uten å måtte velge en spesifikk versjon. I tillegg står det i Docker-dokumentasjonen at taggen `latest` er standardtaggen, noe som gjør den enklere å bruke. |
|              | Container image + SQS URL                             | Docker Hub Image: ezzoali/java-sqs-client                                          |
|              |                                                       | SQS URL: `https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26`     |
|              | Lenke til GitHub Actions workflow                     | https://github.com/EzzoAli/devops-exam-26/actions/runs/11965712974                 |

