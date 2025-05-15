# JobIntel

**Cloud-Native, DevOps-Powered Job Application Tracker**  
_A fully automated, infrastructure-as-code system that helps manage job searches like a real production pipeline._

---

## **Overview**

JobIntel is a cloud-native project I built while studying for certifications and job hunting remotely. I wanted something more powerful than a spreadsheet or Notion board — I wanted infrastructure, automation, and insights.

This project deploys a job application tracker with:
- Full Terraform infrastructure
- Slack integration for logging job events
- CI/CD pipelines
- Optional OpenAI intelligence layer for analyzing feedback and rejection patterns
- Resume version tracking + recruiter-facing S3 resume site

Every part of the project is mapped to a real certification and career-relevant DevOps skill.

---

## **Architecture Diagrams**

> [Insert Draw.io/Excalidraw PNGs or markdown image links here]

- Terraform-provisioned infrastructure
- CI/CD pipeline using GitHub Actions
- “What breaks and what happens next?” observability diagram

---

## **Cert Mapped Layers**

| **Layer**                   | **Tool/Tech Used**                       | **Cert it Maps To**                        | **Status**     |
|-----------------------------|------------------------------------------|--------------------------------------------|----------------|
| Infrastructure as Code      | Terraform, AWS (S3, Lambda, IAM)         | Terraform Associate, AWS SA Pro            | [ ] Not Started |
| Backend API                 | Python (FastAPI or Flask), Boto3         | Python Certification (Optional)            | [ ]            |
| Automation & Bot Logic      | Slack SDK, Python Scheduler, GitHub Actions | DevOps Core, Python                        | [ ]            |
| Containerization            | Docker, Kubernetes (optional)            | Docker DCA, CKA                             | [ ]            |
| CI/CD Pipelines             | GitHub Actions                           | DevOps Mastery, CI/CD Systems               | [ ]            |
| Monitoring & Logging        | AWS CloudWatch, IAM Policies             | AWS SA Pro, Cloud Security (Future)        | [ ]            |
| Intelligence Layer (Bonus)  | OpenAI API, NLP Tagging, Resume Scoring  | AI Curiosity Flex, ML/AI Enthusiast         | [ ]            |

---

## **Live Features (in progress)**

- [ ] Slack `/logjob` command → logs job to database
- [ ] Auto-send weekly job hunt stats via email or Slack DM
- [ ] Resume hosting on S3 with version tracking
- [ ] Web dashboard (minimal UI or Streamlit)

---

## **Cert Tracking**

| Certification               | Status        | Date Completed   |
|-----------------------------|---------------|------------------|
| Terraform Associate         | [ ] Studying  |                  |
| Docker Certified Associate  | [ ] Studying  |                  |
| Kubernetes CKA              | [ ] Planned   |                  |
| AWS Solutions Architect Pro | [ ] Planned   |                  |
| Python Certification        | [ ] Optional  |                  |
| Cloud Security (TBD)        | [ ] Future    |                  |

---

## **Why I Built This**

Because job hunting deserves DevOps, too.

I was studying, building, and applying all at the same time — and this project let me do all three in one place. It’s my resume, my tracker, and my case study in infrastructure-as-career.

---

## **Repos in This Project**

- [`jobintel-infra`](https://github.com/yourusername/jobintel-infra) → Terraform IaC
- [`jobintel-api`](https://github.com/yourusername/jobintel-api) → Python backend
- [`jobintel-bot`](https://github.com/yourusername/jobintel-bot) → Slack integration
- [`jobintel-ui`](https://github.com/yourusername/jobintel-ui) → Resume/metrics frontend (optional)
- [`jobintel-ml`](https://github.com/yourusername/jobintel-ml) → NLP/feedback analytics (optional)

---

## **License**
MIT — Feel free to fork, build, and remix.
