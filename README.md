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
### leveranse 1b:

### Oppgave 1b: GitHub Actions Workflow for SAM Deploy
- **Lenke til workflow**: https://github.com/EzzoAli/devops-exam-26/actions/runs/11900918322/job/33162795154



# Oppgave 2 A & B

### Denne komandoen er for å finne filstien til infra
```bash
cd devops-exam-26/infra
```

### konfiguere backend og provider
```
terraform init
```

### vertifisere at koden er skrevet riktig:
```
terraform validate
```

### se hva som vil bli opprettet
```
terraform plan
```

### opprette applicationen, bekreft yes hvis den ber om det
```
terraform apply
```

### test applicationen SQS:
```
aws sqs send-message \
    --queue-url https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26 \
    --message-body '{
        "title": "Sunset Safari",
        "description": "Place me in a jeep on an African savanna with lions and elephants in the background under a golden sunset. Use an analog 1980s photo effect with warm color tones, and give it a grainy texture for an authentic safari experience."
    }' \
    --output json
```

### leveranse oppgave 2:

- **Lenke til terraform plan workflow (non-main branch)**: 
https://github.com/EzzoAli/devops-exam-26/actions/runs/11964862446/job/33357904173

- **Lenke til terraform apply workflow (main branch)**: 
https://github.com/EzzoAli/devops-exam-26/actions/runs/11945111658/job/33297209272

### SQS Queue URL for image-gen-queue-26
```
https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26
```

# Oppgave 3 A & B

## bygge jave koden som en JAR-fil:
```bash
cd devops-exam-26/java_sqs_client
mvn package
```

###sette variablen for SQS-queue url og kjør jar filen:
```bash
export SQS_QUEUE_URL=https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26
java -jar target/imagegenerator-0.0.1-SNAPSHOT.jar "Me on top of K2"
```

### hvis aws keys er nødvendig erstatt XXX og YYY med aws keys:
```bash
export AWS_ACCESS_KEY_ID= XXX
export AWS_SECRET_ACCESS_KEY= YYY
export SQS_QUEUE_URL=https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26
java -jar target/imagegenerator-0.0.1-SNAPSHOT.jar "Me on top of K2"
```

###

```bash
docker run \
    -e AWS_ACCESS_KEY_ID=xxx \
    -e AWS_SECRET_ACCESS_KEY=yyy \
    -e SQS_QUEUE_URL=https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26 \
    ezzoali/imagegenerator-client:latest "Me on top of a pyramid"
```

### leveranse for oppgave 3 A & B:

### valgte dockertaggen `latest`:
- For mitt Docker-image har jeg bestemt meg for å velge `latest` som tag. Dette sikrer at man alltid har tilgang til den nyeste versjonen av klienten, uten å måtte velge en spesifikk versjon. I tillegg står det i Docker-dokumentasjonen at taggen `latest` er standardtaggen, noe som gjør den enklere å bruke.

### image-navnet fra min dockerhub konto:

- med latest taggen:
```bash
ezzoali/java-sqs-client:latest
```
-uten latest taggen:
```bash
ezzoali/java-sqs-client
```

## leveranse for oppgave 4:

### først endre email placeholder i:

```
devops-exam-26/infra/terraform.tfvars
```


### slå av event sourch mapping:

```bash
aws lambda update-event-source-mapping \
  --uuid 581928cf-635d-443f-b3b5-2ef20d491f97 \
  --no-enabled \
  --output json
```
### test applicationen SQS:
```
aws sqs send-message \
    --queue-url https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26 \
    --message-body '{
        "title": "Sunset Safari",
        "description": "Place me in a jeep on an African savanna with lions and elephants in the background under a golden sunset. Use an analog 1980s photo effect with warm color tones, and give it a grainy texture for an authentic safari experience."
    }' \
    --output json
```

### slå på event sourch mapping:

```bash
aws lambda update-event-source-mapping \
  --uuid 581928cf-635d-443f-b3b5-2ef20d491f97 \
  --enabled \
  --output json
```



# Automatisering og kontinuerlig levering (CI/CD)

## Serverless i CI/CD

Serverless tilbyr en strømlinjeformet opplevelse for CI/CD ved å automatisere nøkkelprosesser i utviklingslivssyklusen, redusere driftsbelastning og muliggjøre sømløse utrullinger (Harness, n.d.). Imidlertid kan integrering av serverless i tradisjonelle CI/CD-pipelines kreve tilpasning til dens hendelsesdrevne og skyspesifikke arbeidsflyter (Harness, n.d.).

### Fordeler:
- **Automatisering og forenkling**:  
  Mikrotjenestenes modulære design støtter isolert testing og utrulling, noe som sikrer stabilitet for andre deler av systemet (Lybeck, 2018).
- **Raske iterasjoner**:  
  Automatisert testing og utrulling i serverless-pipelines forbedrer pålitelighet og hastighet i programvareleveransen (Harness, n.d.).

### Ulemper:
- **Pipeline-tilpasning**:  
  Tilpasning av CI/CD-pipelines for serverless kan introdusere utfordringer, spesielt når det gjelder integrering med hendelsesdrevne, skyspesifikke plattformer (Harness, n.d.).
- **Risiko for hot patching**:  
  Eksisterende CI/CD-pipelines kan ofte gjenbrukes med minimale justeringer for containerbaserte mikrotjenester (Lybeck, 2018).

---

## Mikrotjenester i CI/CD

Mikrotjenester passer godt med tradisjonelle CI/CD-tilnærminger på grunn av deres modulære natur, som tillater uavhengig utrulling av tjenester (Lybeck, 2018). Imidlertid introduserer den distribuerte naturen til mikrotjenester operasjonell kompleksitet.

### Fordeler:
- **Detaljert kontroll**:  
  Mikrotjenestenes modulære design støtter isolert testing og utrulling, noe som sikrer stabilitet for andre deler av systemet.
- **Tradisjonell kompatibilitet**:  
  Eksisterende CI/CD-pipelines kan ofte gjenbrukes med minimale justeringer for containerbaserte mikrotjenester.

### Ulemper:
- **Operasjonell belastning**:  
  Å opprettholde separate CI/CD-pipelines for flere mikrotjenester øker kompleksiteten og krever robust koordinering (Harness, n.d., Lybeck, 2018).  
- **Begrenset skalerbarhet**:  
  Skalering av mikrotjenesteinfrastruktur er mindre dynamisk sammenlignet med serverless, noe som potensielt kan bremse CI/CD-prosesser under høy etterspørsel (Lybeck, 2018).

---

# Observability (Overvåkning)

## Hvordan endres overvåkning, logging og feilsøking når man går fra mikrotjenester til en serverless arkitektur?

### Serverless Arkitektur

#### Fordeler:
- **Effektive overvåkningsverktøy**:  
  Plattformspesifikke verktøy som Serverless Framework og AWS Lambda gir omfattende metrikker, spor, logger og feilmeldinger(Serverless Framework, n.d.). Distribuerte sporingsverktøy som AWS X-Ray og OpenTelemetry gir innsikt i forsinkelser og samhandling mellom tjenester(Faruqui, 2024
).
- **Enkel oppsett**:  
  Automatisert instrumentering, inkludert IAM-rolleintegrasjon og Lambda-lag, forenkler oppsamling av logger og spor(Serverless Framework, n.d.). Sentralisert logging gjennom verktøy som AWS CloudWatch forenkler aggregering av kortvarige funksjonslogger(Faruqui, 2024
).
- **Kostnadseffektivitet gjennom prøvetaking**:  
  Automatisk prøvetaking av sporingsdata optimaliserer overvåkningskostnader, spesielt for funksjoner med høy trafikk(Serverless Framework, n.d.).

#### Utfordringer:
- **Økt kompleksitet i logging og feilsøking**:  
  Kortvarige funksjoner gjør det utfordrende å opprettholde loggingskontekster på tvers av flere kall. Krever standardiserte loggingsformater og sentraliserte aggregeringsverktøy(Serverless Framework, n.d., Faruqui, 2024).
- **Spredt overvåkningskontekst**:  
  Applikasjoner deles opp i mange små funksjoner, noe som kan skape utfordringer i distribuert logging. Overvåkning krever separate oppsett for hundrevis av funksjoner(Serverless Framework, n.d.).
- **Overvåkning av "cold starts"**:  
  "Cold starts" introduserer latens som påvirker brukeropplevelsen. Spesifikke verktøy må brukes for å spore og måle disse forsinkelsene(Faruqui, 2024).
- **Avhengighet av plattformspesifikke verktøy**:  
  Plattformverktøy kan være vanskelig å integrere med eksterne løsninger og migrasjon til andre plattformer(Serverless Framework, n.d., Faruqui, 2024).

---

### Mikrotjenester Arkitektur

Mikrotjenester er modulære og uavhengige, noe som gir mer strukturert overvåkning og feilsøking. Likevel kan den distribuerte naturen føre til operasjonell kompleksitet.

#### Fordeler:
- **Strukturert overvåkning**:  
  Mikrotjenester benytter containere med en veldefinert livssyklus, noe som gjør integrasjon med eksisterende overvåkningsverktøy enklere. Tradisjonelle loggings- og overvåkningsarbeidsflyter kan brukes på nytt(Faruqui, 2024).
- **Komponentbasert feilsøking**:  
  Isolert logging og feilsøking på tvers av uavhengige tjenester. Modulenes uavhengighet sikrer at problemer kan isoleres uten å påvirke hele systemet(Faruqui, 2024).

#### Utfordringer:
- **Operasjonell kompleksitet**:  
  Krever separate overvåkningsoppsett for hver tjeneste, noe som øker administrasjonsbelastningen. Spor og logger må samles og aggregeres fra flere kilder(Faruqui, 2024).
- **Ressursadministrasjonsbelastning**:  
  Mikrotjenester krever dedikert infrastruktur, noe som øker kostnadene og administrativ kompleksitet. Overvåkningsløsninger må kontinuerlig justeres under høy trafikk(Faruqui, 2024).

---

# Skalerbarhet og kostnadskontroll

## Serverless

Serverless utmerker seg med dynamisk skalering og kostnadseffektivitet, noe som gjør det ideelt for applikasjoner med varierende arbeidsbelastninger (Harness, n.d.). Modellen introduserer imidlertid utfordringer som uforutsigbare kostnader og kaldstartlatens (Harness, n.d.).

### Fordeler:
- **Dynamisk skalering**:  
  Serverless justerer seg automatisk til endringer i arbeidsbelastning, noe som sikrer effektiv ressursbruk uten manuell inngripen (Harness, n.d., Lybeck, 2018).
- **Kostnadseffektivitet**:  
  Betal-for-bruk-prising eliminerer utgifter til inaktiv infrastruktur, noe som tilpasser kostnadene til faktisk bruk (Harness, n.d., Lybeck, 2018).

### Ulemper:
- **Uforutsigbare kostnader**:  
  Autoskalering kan føre til svingende utgifter, noe som utfordrer utviklere til å holde budsjettet under kontroll (Harness, n.d.).
- **Kaldstartlatens**:  
  Serverless-funksjoner kan oppleve forsinkelser under oppstart, noe som påvirker ytelsen for tidskritiske oppgaver (Harness, n.d.).
  
---

## Mikrotjenester

Mikrotjenester gir presis kontroll over ressursallokering og forutsigbare driftskostnader, men de er mindre smidige i skalering sammenlignet med serverless-arkitekturer (Harness, n.d., Lybeck, 2018).

### Fordeler:
- **Kontrollert ressursallokering**:  
  Ressurser kan tilpasses hver tjenestes behov, noe som optimaliserer ytelse og kostnader (Harness, n.d., Lybeck, 2018).
- **Forutsigbare kostnader**:  
  Forhåndskonfigurert infrastruktur sikrer konsistente utgifter og unngår uforutsigbare serverless-kostnader (Harness, n.d.).

### Ulemper:
- **Manuell skalering**:  
  Skalering av mikrotjenester krever manuell innsats eller kompleks orkestrering, noe som gjør dem mindre responsive til plutselige trafikkøkninger (Harness, n.d., Lybeck, 2018).
- **Høyere infrastrukturkostnader**:  
  Å opprettholde infrastruktur for kontinuerlig kjørende tjenester kan føre til høyere grunnkostnader sammenlignet med serverless (Lybeck, 2018).

---

# Eierskap og ansvar

## Hvordan påvirkes DevOps-teamets eierskap og ansvar for applikasjonens ytelse, pålitelighet og kostnader ved overgang til en serverless tilnærming sammenlignet med en mikrotjeneste-tilnærming?

## Serverless: Eierskap og ansvar

I en serverless-tilnærming blir mange operasjonelle oppgaver overført til skyleverandøren. Dette frigjør DevOps-teamet fra mye av infrastrukturansvaret, men gir også nye utfordringer relatert til observabilitet, sikkerhet og kostnadshåndtering.

### Fordeler:
- **Redusert operasjonell belastning**:  
  I serverless tar skyleverandøren ansvar for infrastrukturhåndtering, inkludert serverklargjøring, vedlikehold og skalering. Dette frigjør DevOps-team til å fokusere på forretningslogikk og applikasjonsytelse (DevOps.com, n.d., DevOps.com, 2023).
- **Granulært ansvar**:  
  Serverless-arkitektur oppmuntrer team til å håndtere individuelle funksjoner med minimal nødvendige roller, i tråd med prinsippet om minst privilegium. Dette forbedrer sikkerheten og isolerer problemer til spesifikke funksjoner (DevOps.com, 2023).
- **Bedret samarbeid og CI/CD-integrasjon**:  
   Automatisering i serverless-pipelines lar utviklere konsentrere seg om å utvikle funksjonalitet i stedet for å administrere infrastruktur. Dette tilrettelegger for en modell med delt eierskap på tvers av team (Simform, n.d.).

### Ulemper:
- **Kompleks rolle- og tillatelseshåndtering**:  
   Å tildele riktige roller til mange serverless-funksjoner skaper kompleksitet og øker risikoen for feilkonfigurasjoner, noe som kan føre til sikkerhetsproblemer eller ineffektivitet (DevOps.com, 2023).
- **Utfordringer med kortvarige funksjoner**:  
  Den tilstandsfrie og kortvarige naturen til serverless-funksjoner kompliserer feilsøking og krever stor avhengighet av sentraliserte overvåkningsverktøy, noe som legger til et ekstra lag av ansvar for observabilitet (DevOps.com, n.d., Simform, n.d.).
- **Uforutsigbare kostnader**:  
  Selv om serverless eliminerer faste infrastrukturkostnader, kan dynamisk skalering gjøre kostnadsstyring utfordrende. DevOps-team må ta eierskap for å overvåke og optimalisere bruken for å unngå budsjettoverskridelser (DevOps.com, n.d., DevOps.com, 2023).

---

## Mikrotjenester: Eierskap og ansvar

Mikrotjeneste-tilnærmingen gir DevOps-teamet mer kontroll over infrastruktur og applikasjonskomponenter, men medfører også et høyere operasjonelt ansvar.

### Fordeler:
- **Klare eierskapsgrenser**:  
  Mikrotjenestenes modulære natur gjør det mulig for team å ha tydelig definert eierskap over spesifikke tjenester, noe som gjør det enklere å administrere og vedlikeholde individuelle komponenter (DevOps.com, 2023).
- **Forutsigbar ressursallokering**:  
  I motsetning til serverless opererer mikrotjenester på dedikert infrastruktur, noe som lar DevOps-team forutsi kostnader og kontrollere ressursutnyttelse mer effektivt (DevOps.com, 2023).

### Ulemper:
- **Økt operasjonell belastning**:  
  Behovet for å administrere infrastruktur og opprettholde pipelines for flere mikrotjenester øker den operasjonelle belastningen på DevOps-team (DevOps.com, n.d., Simform, n.d., DevOps.com, 2023).
- **Orkestreringsutfordringer**:  
  Skalering av mikrotjenester krever ofte manuell innsats eller komplekse orkestreringssystemer, noe som kan føre til langsommere responstider sammenlignet med serverless (DevOps.com, n.d., DevOps.com, 2023).
- **Utvidet ansvarsområde**:  
  DevOps-team er ansvarlige for hele livssyklushåndteringen, inkludert klargjøring, skalering og sikkerhet. Dette kan være ressurskrevende og utfordrende å vedlikeholde på tvers av distribuerte tjenester (DevOps.com, 2023).

---

## Oppsummering

**Serverless** reduserer operasjonelle oppgaver ved å flytte mye ansvar til skyleverandøren, men gir utfordringer med observabilitet og kostnadskontroll. **Mikrotjenester** gir mer kontroll og forutsigbarhet, men krever betydelig innsats for å håndtere infrastrukturen. Valget mellom serverless og mikrotjenester bør baseres på teamets kapasitet, systemets kompleksitet og applikasjonens krav.


### referanser:
- Harness. (n.d.). CI/CD for Serverless. Harness Blog. https://www.harness.io/blog/cicd-for-serverless

- Lybeck, J. (2018, September 24). Serverless: Et paradigmeskifte i systemutvikling. Medium. https://medium.com/@jorgenlybeck/serverless-et-paradigmeskifte-i-systemutvikling-556a24fb9bd6

- Serverless Framework. (n.d.). Monitoring Guide. Serverless Framework. https://www.serverless.com/framework/docs/guides/dashboard/monitoring
- Faruqui, Z. (2024, September 18). Serverless Monitoring: 7 Best Practices. With Coherence. https://www.withcoherence.com/articles/serverless-monitoring-7-best-practices-2024

- DevOps.com. (n.d.). 5 Serverless Challenges of DevOps Teams and How to Overcome Them. DevOps.com. https://devops.com/5-serverless-challenges-of-devops-teams-and-how-to-overcome-them/
- Simform. (n.d.). DevOps Best Practices for Serverless. Simform Blog. https://www.simform.com/blog/devops-best-practices-for-serverless/
- DevOps.com. (2023, February 15). Running Serverless in Production: 7 Best Practices for DevOps. DevOps.com. https://devops.com/running-serverless-in-production-7-best-practices-for-devops/








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
|              |                                                       | Docker Hub Image: ezzoali/java-sqs-client:latest                                   |
|              |                                                       | SQS URL: `https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-26`     |
|              | Lenke til GitHub Actions workflow                     | https://github.com/EzzoAli/devops-exam-26/actions/runs/11965712974                 |

