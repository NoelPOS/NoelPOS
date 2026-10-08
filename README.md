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
<tr>
<td colspan="2" valign="top">

### Kiddee Lab LMS <sub>· production · private codebase</sub>
The learning management system and CRM that runs Kiddee Lab, a coding and robotics school for kids in Bangkok. I built and maintained it for a year.

- Replaced paper-based workflows for **800+ users**: students, parents, class scheduling, courses, enrolment and CRM
- Migrated and reconciled **10,000+ legacy records** into the new system, with validation so nothing was lost
- Also built the school's public landing page → [kiddeelab.co.th](https://www.kiddeelab.co.th)

`Next.js` `NestJS` `TypeORM` `PostgreSQL` `Docker`

</td>
</tr>
</table>

## 🛠️ Toolbox

| Area | Tools |
|---|---|
| **Languages** | TypeScript · Java · C# · Go · Python |
| **Backend** | NestJS · Spring Boot · ASP.NET Core · Node.js |
| **Frontend** | React · Next.js · React Native |
| **Data** | PostgreSQL · Redis · MongoDB · MySQL · RabbitMQ |
| **Cloud & DevOps** | AWS · Docker · Terraform · GitHub Actions · Nginx |
| **Testing** | Playwright · Testcontainers · JUnit · Robot Framework |
