<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hello-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./assets/hello-light.svg" />
  <img alt="Terminal: I build backends that stay correct under pressure. curl -i localhost:8080/v1/engineers/noel returns HTTP 200 with JSON describing Noel Paing Oak Soe, a Software Engineer at EffortX Foundation in Bangkok focused on backend, distributed systems, cloud and reliability, currently building VetMiMi, open to work." src="./assets/hello-dark.svg" width="100%" />
</picture>

<br />

<p align="center">
  <a href="https://noelpos-dev.vercel.app"><img src="https://img.shields.io/badge/portfolio-noelpos--dev.vercel.app-2ea043?style=flat-square&labelColor=30363d&logo=vercel&logoColor=white" alt="Portfolio" /></a>&nbsp;
  <a href="https://www.linkedin.com/in/noelpos"><img src="https://img.shields.io/badge/linkedin-in%2Fnoelpos-2ea043?style=flat-square&labelColor=30363d&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>&nbsp;
  <a href="mailto:noelpaingoaksoe@gmail.com"><img src="https://img.shields.io/badge/email-noelpaingoaksoe%40gmail.com-2ea043?style=flat-square&labelColor=30363d&logo=gmail&logoColor=white" alt="Email" /></a>
</p>

<br />

## `~/projects`

<table>
<tr>
<td width="50%" valign="top">

### [AU-Van](https://github.com/NoelPOS/au-van-platform)
LINE-integrated van seat booking for Assumption University.

- Concurrent seat holds, booking expiry and waitlist promotion, with PostgreSQL constraints as the source of truth
- Transactional outbox → LINE Flex Message notifications with retries and dead-lettering
- AWS target in Terraform (Fargate across 2 AZs, Multi-AZ RDS, CloudFront), proven in an evidence session; live demo on EC2 with CI/CD gated by 9 checks

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
<br/>[Live](https://vetmimi-arts-therapy.vercel.app) · [API](https://github.com/VetMiMi/vetmimi-api) · [Web](https://github.com/VetMiMi/vetmimi-next)

</td>
</tr>
</table>

## `~/experience`

| When | Role | What I did |
|---|---|---|
| **Sep 2025 – now** | **Software Developer** · [EffortX Foundation](https://www.effort.foundation) · remote | Next.js, React Native, NestJS and PostgreSQL · Redis/BullMQ background jobs · RBAC, JWT and MFA/TOTP · **cut p95 API latency from 850 ms to 350 ms** |
| **Jul – Sep 2026** | **QA Automation Intern** · KBTG (Kasikorn Business-Technology Group) | Robot Framework and Python suites for SIT, UAT and regression testing of enterprise financial apps |
| **Apr 2025 – Mar 2026** | **Full Stack Developer** · [Kiddee Lab Thailand](https://www.kiddeelab.co.th) | LMS/CRM that replaced paper workflows for **800+ users** · migrated and reconciled **10,000+ legacy records** · built the public site [kiddeelab.co.th](https://www.kiddeelab.co.th) |
| **Jun 2023 – Jun 2025** | **WordPress Developer & Teaching Assistant** · Assumption University | Merged two legacy sites into one platform for 1,000+ students · mentored 20+ students in DSA and OOP |
| **2022 – 2026** | **B.Sc. Computer Science** · Assumption University | GPA **3.88 / 4.00** |

## `~/stack`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/neofetch-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./assets/neofetch-light.svg" />
  <img alt="neofetch-style card: a halftone portrait of Noel beside his stack - TypeScript, Java, Go, C#, Python; NestJS, Spring Boot, ASP.NET Core; React, Next.js; PostgreSQL, Redis, MongoDB, RabbitMQ; AWS, Docker, Terraform, GitHub Actions; Playwright, Testcontainers, JUnit - and live GitHub stats, refreshed daily." src="./assets/neofetch-dark.svg" width="100%" />
</picture>
