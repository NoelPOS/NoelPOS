<h1 align="center">Noel Paing Oak Soe</h1>

<p align="center">
  <b>Software Engineer · Backend &amp; Distributed Systems</b><br/>
  <sub>Event-driven systems, cloud infrastructure and reliability — owned from design to production.</sub>
</p>

<p align="center">
  <a href="https://noelpos-dev.vercel.app"><img src="https://img.shields.io/badge/Portfolio-noelpos--dev.vercel.app-2F81F7?style=flat-square&logo=vercel&logoColor=white" alt="Portfolio" /></a>
  <a href="https://www.linkedin.com/in/noelpos"><img src="https://img.shields.io/badge/LinkedIn-noelpos-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:noelpaingoaksoe@gmail.com"><img src="https://img.shields.io/badge/Email-noelpaingoaksoe%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <img src="https://img.shields.io/badge/Based_in-Bangkok%2C_TH-6E7681?style=flat-square" alt="Bangkok, Thailand" />
</p>

---

I build backends that stay correct under pressure: bookings that can't be oversold, payments that can't be charged twice, and notifications that arrive exactly once. I've spent 2+ years shipping and running production platforms, from design through deployment and on-call debugging.

## 💼 Experience

| When | Role | Highlights |
|---|---|---|
| **Sep 2025 – now** | **Software Developer** · [EffortX Foundation](https://www.effort.foundation) · remote | Next.js, React Native, NestJS and PostgreSQL · Redis/BullMQ background jobs · RBAC, JWT and MFA/TOTP · **cut p95 API latency from 850 ms to 350 ms** |
| **Jul – Sep 2026** | **QA Automation Intern** · KBTG (Kasikorn Business-Technology Group) | Robot Framework and Python suites for SIT, UAT and regression testing of enterprise financial apps |
| **Apr 2025 – Mar 2026** | **Full Stack Developer** · [Kiddee Lab Thailand](https://www.kiddeelab.co.th) | LMS/CRM that replaced paper workflows for **800+ users** · migrated and reconciled **10,000+ legacy records** |
| **Jun 2023 – Jun 2025** | **WordPress Developer & Teaching Assistant** · Assumption University | Merged two legacy sites into one platform for 1,000+ students · mentored 20+ students in DSA and OOP |
| **2022 – 2026** | **B.Sc. Computer Science** · Assumption University | GPA **3.88 / 4.00** |

## 🚀 Featured work

<table>
<tr>
<td width="50%" valign="top">

### [AU-Van](https://github.com/NoelPOS/au-van-platform)
LINE-integrated van seat booking for Assumption University.

- Concurrent seat holds, booking expiry and waitlist promotion, with PostgreSQL constraints as the source of truth
- Transactional outbox → LINE Flex Message notifications with retries and dead-lettering
- Terraform on AWS (ECS Fargate across 2 AZs, ALB, RDS Multi-AZ, CloudFront), with 9 CI checks including Playwright

`Spring Boot` `React` `PostgreSQL` `Terraform` `AWS`
<br/>[Live demo](https://auvan.duckdns.org) · [Code](https://github.com/NoelPOS/au-van-platform)

</td>
<td width="50%" valign="top">

### [VetMiMi](https://github.com/VetMiMi) <sub>· in development</sub>
Booking and online sessions for an art therapy practice in Sydney.

- Go API: appointment booking, content management, media and email, with an OpenAPI-first design
- One-to-one WebRTC video sessions with Go signaling, TURN, and MFA/TOTP for the admin
- Bilingual Next.js site (English and Burmese) plus an admin console, with background jobs on Redis

`Go` `Next.js` `PostgreSQL` `Redis` `WebRTC`
<br/>[Live](https://vetmimi-next.vercel.app) · [API](https://github.com/VetMiMi/vetmimi-api) · [Web](https://github.com/VetMiMi/vetmimi-next)

</td>
</tr>
</table>

## 🛠️ Toolbox

<p>
  <img src="https://skillicons.dev/icons?i=ts,java,cs,go,py&perline=12" alt="TypeScript, Java, C#, Go, Python" /><br/>
  <img src="https://skillicons.dev/icons?i=nestjs,spring,dotnet,nodejs,react,nextjs,prisma&perline=12" alt="NestJS, Spring, .NET, Node.js, React, Next.js, Prisma" /><br/>
  <img src="https://skillicons.dev/icons?i=postgres,mysql,mongodb,redis,rabbitmq&perline=12" alt="PostgreSQL, MySQL, MongoDB, Redis, RabbitMQ" /><br/>
  <img src="https://skillicons.dev/icons?i=aws,docker,kubernetes,terraform,nginx,githubactions&perline=12" alt="AWS, Docker, Kubernetes, Terraform, Nginx, GitHub Actions" />
</p>

<details>
<summary><b>More projects</b></summary>
<br/>

| Project | What it is | Stack |
|---|---|---|
| [Kiddee Lab LMS](https://github.com/Kiddee-Lab-Company-Limited) | Production LMS/CRM that replaced paper workflows for 800+ users ([web](https://github.com/Kiddee-Lab-Company-Limited/kdl-frontend), [api](https://github.com/Kiddee-Lab-Company-Limited/kdl-backend)) | Next.js · NestJS · PostgreSQL |
| [CodePilot](https://github.com/NoelPOS/codepilot) | AI prompt-to-code workspace with live Sandpack preview and a bring-your-own-key model | Next.js · Convex · Gemini |
| [Disease Predictor](https://github.com/NoelPOS/disease-predictor) | Compares ML classifiers for predicting a disease from symptoms | Python · ML · ONNX |
| [Conserve](https://github.com/NoelPOS/Conserve-App) | Hackathon app that helps people cut their carbon footprint (TriValley Hackathon) | React Native · Express · MongoDB |
| [100 Days of DevOps](https://github.com/NoelPOS/KobeCloud_100_Days_of_Devops) | Lab notes from the KodeKloud 100 Days of DevOps challenge | Linux · Docker · K8s |

</details>
