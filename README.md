# Project Summary

JobIntel is a fully cloud-native, cert-mapped job application tracker that uses Terraform, AWS, GitHub Actions, and Slack automation to track applications like a production system. [See full breakdown.] (PROJECT_OVERVIEW.md)

## JobIntel-DevOps-Driven Job Tracker Platform

**Cloud-Native, DevOps-Powered Job Application Tracker**
_A fully automated, infrastructure-as-code system that helps manage job searches like a real production pipeline._

---

## Badges

[![Terraform CI](https://github.com/destiny-malone/jobintel-infra/actions/workflows/terraform.yml/badge.svg)](https://github.com/destiny-malone/jobintel-infra/actions/workflows/terraform.yml)

---

## **Overview**

JobIntel is a cloud-native project I built while studying for certifications and job hunting remotely. I wanted something more powerful than a spreadsheet or Notion board — I wanted infrastructure, automation, and insights.

This project deploys a job application tracker with:
    - Full Terraform infrastructure
    - Slack integration for logging job events
    - CI/CD pipelines
    - OpenAI intelligence layer for analyzing feedback and rejection patterns
    - Resume version tracking + recruiter-facing S3 resume site

Every part of the project is mapped to a real certification and career-relevant DevOps skill.

---

## 📊 Architecture Diagrams

This section provides versioned diagrams of the infrastructure and automation powering JobIntel.
Each diagram evolveed with the project, showcasing best practives, real-world patterns, and cloud-native growth over time.

---

### 🛠 Infra Overview (Terraform to AWS S3)  

Terraform provisioning to AWS S3 using secure IAM access.

- **Terraform-Provisioned Infrastructure** — declarative IaC to deploy a randomized, public-blocked S3 bucket via `random_id`, ownership control, and seecure authentication.

[![Infra Overview - Phase 1](docs/diagrams/infra-overview-v1.png)](docs/diagrams/infra-overview-v1.svg)

- **Phase 1 Scope** - Terraform CLI → AWS Provider → IAM Auth → S3 Provisioning (no root user, secure bucket)

---

### 🚀 CI/CD Pipeline (GitHub Actions)  

Pipeline enforcing Terraform quality standards and enabling automation.

- **CI/CD Pipeline via GitHub Actions** — validates Terraform format, runs `terraform validate`, and auto-deploys Iac.

[![CI/CD Pipeline - Phase 2](docs/diagrams/ci-cd-pipeline-v1.png)](docs/diagrams/ci-cd-pipeline-v1.svg)

### 🧠 Phase 2: CI/CD Pipeline with Slack & Artifacts

Terraform CI/CD pipeline powered by GitHub Actions and Slack. Built for security, clarity, and real-world DevOps readiness.

### 🚀 Key Features

- Format, validate, and plan with each push
- JSON plan artifact creation
- Comment tfplan on PRs and pushes
- Slack notifications for success/failure
- Environment-based alert filtering (production only)
- Full workflow logs stored as artifacts

### 🧩 Diagrams

| Version | Description |
|---------|-------------|
| v1      | Basic CI pipeline: fmt, validate, plan |
| v2      | Advanced: tfplan output, Slack, logs, environment logic |

[![CI/CD Pipeline v2](docs/diagrams/ci-cd-pipeline-v2.png)](docs/diagrams/ci-cd-pipeline-v2.svg)

---

### 🔍 Observability Flow (Fail → Detect → Recover)  

Mapping system errors, logs, and fallback response flow for production-grade observability.

- **Observability & Failure Flow** — “What breaks and what happens next?” diagram for real-time logging, alerting, and recovery pipelines.

[![Observability Flow](docs/diagrams/observability-flow.png)](docs/diagrams/observability-flow.svg)

- **Layered Strategy**: Track job rejections, Slack alerts, and feeds analytics to ML/NLP layer

---

## **Cert Mapped Layers**

| **Layer**                   | **Tool/Tech Used**                       | **Cert it Maps To**                        | **Status**     |
|-----------------------------|------------------------------------------|--------------------------------------------|----------------|
| Infrastructure as Code      | Terraform, AWS (S3, Lambda, IAM)         | Terraform Associate, AWS SA Pro            | [ ] |
| Backend API                 | Python (FastAPI or Flask), Boto3         | Python Certification             | [ ]            |
| Automation & Bot Logic      | Slack SDK, Python Scheduler, GitHub Actions | DevOps Core, Python                        | [ ]            |
| Containerization            | Docker, Kubernetes             | Docker DCA, CKA                             | [ ]            |
| CI/CD Pipelines             | GitHub Actions                           | DevOps Mastery, CI/CD Systems               | [ ]            |
| Monitoring & Logging        | AWS CloudWatch, IAM Policies             | AWS SA Pro, Cloud Security (Future)        | [ ]            |
| Intelligence Layer  | OpenAI API, NLP Tagging, Resume Scoring  | AI Curiosity Flex, ML/AI Enthusiast         | [ ]            |

---

## **Live Features**

- [ ] Slack `/logjob` command → logs job to database
- [ ] Auto-send weekly job hunt stats via email or Slack DM
- [ ] Resume hosting on S3 with version tracking
- [ ] Web dashboard (minimal UI or Streamlit)

---

## **Cert Tracking**

| Certification               | Status        | Date Completed   |
|-----------------------------|---------------|------------------|
| Terraform Associate         | [ ]  |                  |
| Docker Certified Associate  | [ ]  |                  |
| Kubernetes CKA              | [ ]   |                  |
| AWS Solutions Architect Pro | [ ]   |                  |
| Python Certification        | [ ]   |                  |
| Cloud Security (TBD)        | [ ]    |                  |

---

## **Why I Built This**

Because job hunting deserves DevOps, too.

I was studying, building, and applying all at the same time — and this project let me do all three in one place. It’s my resume, my tracker, and my case study in infrastructure-as-career.

---

## **Repos in JobIntel**

- [`jobintel-infra`](https://github.com/destiny-malone/jobintel-infra) → Terraform IaC
- [`jobintel-api`](https://github.com/destiny-malone/jobintel-api) → Python backend
- [`jobintel-bot`](https://github.com/destiny-malone/jobintel-bot) → Slack integration
- [`jobintel-ui`](https://github.com/destiny-malone/jobintel-ui) → Resume/metrics frontend
- [`jobintel-ml`](https://github.com/destiny-malone/jobintel-ml) → NLP/feedback analytics
- [`jobintel-cicd`](https://github.com/destiny-malone/jobintel-cicd) → GitHub Actions, Terraform CI, Backend auto-deploy workflows
- [`jobintel-cli`](https://github.com/destiny-malone/jobintel-cli) → Terminal-based app tracker
- [`jobintel-docs`](https://github.com/destiny-malone/jobintel-docs) → Project notes, cert writeups, LinkedIn content

---

## **License**

MIT — Feel free to fork, build, and remix.
