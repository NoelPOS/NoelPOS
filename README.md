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

```ts
const noel = {
  role:       "Software Developer @ EffortX Foundation",
  experience: "2+ years building and running production web platforms",
  focus:      ["backend architecture", "event-driven systems", "cloud & reliability", "auth & security"],
  shipping:   "VetMiMi — booking and WebRTC video sessions (Go + Next.js)",
  education:  "B.Sc. Computer Science, Assumption University (GPA 3.88 / 4.00)",
  openTo:     "backend and full-stack engineering roles",
};
```

## 🧭 Career, as a git log

```console
$ git log --graph --oneline career

*   e7f0x12 (HEAD -> main) Software Developer @ EffortX Foundation · remote, AU        2025-09 → now
|\            Next.js · React Native · NestJS · PostgreSQL · Redis/BullMQ
| |           ↳ p95 API latency 850 ms → 350 ms · 1,000+ users · RBAC, JWT, MFA/TOTP
| * k8t9b07 QA Automation Intern @ KBTG (Kasikorn Business-Technology Group)       2026-07 → 2026-09
|/            Robot Framework · Python · SIT / UAT / regression suites for financial apps
* kd1ab04 Full Stack Developer @ Kiddee Lab Thailand · hybrid                     2025-04 → 2026-03
|             React · Java · PostgreSQL — LMS/CRM for 800+ users, 10,000+ legacy records migrated
* au3web2 WordPress Developer + Teaching Assistant @ Assumption University        2023-06 → 2025-06
|             Unified vms/vme → vmes.au.edu for 1,000+ students · mentored 20+ students in DSA & OOP
* 0c5init init: B.Sc. Computer Science @ Assumption University                     2022-11
```

## 🚀 Featured work

<table>
<tr>
<td width="50%" valign="top">

### [AU-Van](https://github.com/NoelPOS/au-van-platform)
LINE-integrated van seat booking for Assumption University.

- Concurrent seat holds, booking expiry and waitlist promotion, with PostgreSQL constraints as the source of truth
- Transactional outbox → LINE Flex Message notifications with retries and dead-lettering
- Terraform on AWS (ECS Fargate across 2 AZs, ALB, RDS Multi-AZ, CloudFront), with 8 CI gates including Playwright

`Spring Boot` `React` `PostgreSQL` `Terraform` `AWS`
<br/>[Live demo](https://auvan.duckdns.org) · [Code](https://github.com/NoelPOS/au-van-platform)

</td>
<td width="50%" valign="top">

### [TaskFlow](https://github.com/NoelPOS/taskflow-distributed-job-platform)
Distributed async job processing across independent services.

- Accepts work immediately and processes it in a separate worker service
- Event-driven messaging over RabbitMQ with MassTransit
- Pushes job status to the browser in real time with SignalR, so the client never polls

`.NET 10` `RabbitMQ` `MassTransit` `SignalR`
<br/>[Code](https://github.com/NoelPOS/taskflow-distributed-job-platform)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Fortuner](https://github.com/NoelPOS/Fortuner)
Full-stack services marketplace with wallet payments and live sessions.

- Discovery and booking flows, plus credit-based payments and a payout lifecycle
- Real-time sessions over Socket.IO and Stream Video
- Admin moderation and financial operations tooling

`Next.js 15` `NestJS 11` `PostgreSQL` `Stripe`
<br/>[Code](https://github.com/NoelPOS/Fortuner)

</td>
<td width="50%" valign="top">

### [VetMiMi](https://github.com/VetMiMi) <sub>· in development</sub>
Booking and online sessions for an art therapy practice in Sydney.

- Go API: appointment booking, content management, media and email, with an OpenAPI-first design
- WebRTC video sessions with WebSocket signaling, TURN, and MFA/TOTP for the admin
- Bilingual Next.js site (English and Burmese) plus an admin console, with background jobs on Redis

`Go` `Next.js` `PostgreSQL` `Redis` `WebRTC` `AWS S3`
<br/>[Live](https://vetmimi-next.vercel.app) · [API](https://github.com/VetMiMi/vetmimi-api) · [Web](https://github.com/VetMiMi/vetmimi-next)

</td>
</tr>
</table>

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

## 🛠️ Toolbox

<p>
  <img src="https://skillicons.dev/icons?i=ts,java,cs,py,go&perline=12" alt="Languages" /><br/>
  <img src="https://skillicons.dev/icons?i=nestjs,spring,dotnet,nodejs,react,nextjs,prisma&perline=12" alt="Frameworks" /><br/>
  <img src="https://skillicons.dev/icons?i=postgres,mysql,mongodb,redis,rabbitmq&perline=12" alt="Data and messaging" /><br/>
  <img src="https://skillicons.dev/icons?i=aws,docker,kubernetes,terraform,nginx,githubactions&perline=12" alt="Cloud and DevOps" />
</p>

**Things I've built in production:** idempotent APIs · retry and failure handling · transactional outbox · background jobs (BullMQ) · caching and query tuning · RBAC, JWT, sessions, MFA/TOTP, step-up auth · rate limiting · structured logging and health checks · unit, integration and E2E tests (Playwright, Robot Framework)

## 📈 Activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NoelPOS/NoelPOS/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/NoelPOS/NoelPOS/output/github-contribution-grid-snake.svg" />
  <img alt="Contribution snake animation" src="https://raw.githubusercontent.com/NoelPOS/NoelPOS/output/github-contribution-grid-snake.svg" />
</picture>
