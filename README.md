<div align="center">

<!-- ANIMATED HERO BANNER ─────────────────────────────────────────────────── -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,30&height=240&section=header&text=Kushal%20Gaddamwar&fontSize=58&fontColor=ffffff&fontAlignY=34&desc=Agentic%20AI%20Engineer%20%C2%B7%20Multi-Agent%20Systems%20%C2%B7%20Production%20RAG&descAlignY=56&descSize=18&animation=fadeIn"/>

<!-- TYPING SVG — five rotating lines, recruiter-targeted ───────────────── -->
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=19&duration=2400&pause=900&color=58A6FF&center=true&vCenter=true&width=900&lines=I+architect+multi-agent+systems+that+run+in+production.;Thread-isolated+sessions+%E2%80%A2+Token-budgeted+context+%E2%80%A2+Hybrid+RAG.;LangGraph+%E2%80%A2+FastAPI+%E2%80%A2+PGVector+%E2%80%A2+Redis+%E2%80%A2+AWS+%E2%80%A2+Kubernetes.;Boston+University+MSCS+%E2%80%A2+IEEE+Published+%E2%80%A2+F-1+OPT+2026.;Open+to+Agentic+AI+%2F+Applied+AI+%2F+ML+Engineer+roles." alt="elevator pitch"/>

<br/><br/>

<!-- IDENTITY / STATUS LINE ─────────────────────────────────────────────── -->
<p>
  <img src="https://img.shields.io/badge/Boston%2C%20MA-0d1117?style=flat-square&logo=googlemaps&logoColor=58A6FF&labelColor=0d1117"/>
  <img src="https://img.shields.io/badge/Available-Summer%20%2F%20Full--Time%202026-2EA043?style=flat-square&labelColor=0d1117"/>
  <img src="https://img.shields.io/badge/Work%20Auth-F--1%20OPT%202026-58A6FF?style=flat-square&labelColor=0d1117"/>
  <img src="https://img.shields.io/badge/Response%20Time-%3C%2024h-D29922?style=flat-square&labelColor=0d1117"/>
</p>

<!-- CTA BAR — every link 1-click ──────────────────────────────────────── -->
<p>
  <a href="https://linkedin.com/in/kushal-gaddamwar"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>&nbsp;
  <a href="mailto:kushal7887pd@gmail.com"><img src="https://img.shields.io/badge/Email-Reach%20Out-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>&nbsp;
  <a href="https://bulife-ai.netlify.app"><img src="https://img.shields.io/badge/%F0%9F%9A%80%20BU%20Life%20AI-Live%20Demo-00C7B7?style=for-the-badge&logoColor=white"/></a>&nbsp;
  <a href="https://github.com/Kushal9889"><img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
</p>

<p>
  <img src="https://komarev.com/ghpvc/?username=Kushal9889&style=for-the-badge&color=58A6FF&label=PROFILE+VIEWS"/>
  <img src="https://img.shields.io/github/followers/Kushal9889?style=for-the-badge&color=58A6FF&labelColor=0d1117&label=FOLLOWERS"/>
  <img src="https://img.shields.io/github/stars/Kushal9889?style=for-the-badge&color=58A6FF&labelColor=0d1117&label=STARS"/>
</p>

</div>

---

> ### *"Most AI products are a prompt wrapped in a UI. I build the systems around the model."*
>
> Agentic AI Engineer pursuing **MS Computer Science at Boston University** (graduating December 2026). Internship experience shipping **multi-agent orchestration, RAG pipelines, and production APIs** for AI automation startups. **IEEE-published** in deep learning. I care about the parts of LLM systems that aren't in the demo: thread-safe concurrent sessions, token-budgeted context windows, hybrid retrieval that doesn't fall over on keyword queries, and cost ceilings that survive real traffic.

<br/>

## 🛰️ How I Think About Agentic Systems

> This is not a textbook diagram. This is the mental model I debug against when production breaks at 2 AM.

```text
                          USER  INTENT
                               │
                               ▼
        ┌─────────────────────────────────────────────────┐
        │  SUPERVISOR  /  ROUTER                          │
        │  ↳ semantic routing                             │
        │  ↳ context-drift detection                      │
        │  ↳ token-budget gate (hard cap before LLM call) │
        └─────────────────────────────────────────────────┘
                  │                              │
                  ▼                              ▼
        ┌───────────────────┐         ┌───────────────────┐
        │  AGENT  A  (ReAct)│         │  AGENT  B  (ReAct)│   ◀── parallel
        │  Reason→Act→Obs   │         │  Reason→Act→Obs   │      thread-isolated
        │  scratchpad≠final │         │  scratchpad≠final │      (LangGraph state)
        └───────────────────┘         └───────────────────┘
                  │                              │
                  └──────────────┬───────────────┘
                                 ▼
                  ┌─────────────────────────────┐
                  │   TOOL  LAYER               │
                  │   search · retrieve         │
                  │   compute · write           │
                  │   Pydantic-typed outputs    │
                  │   (no raw JSON to agent)    │
                  └─────────────────────────────┘
                                 │
                                 ▼
                  ┌─────────────────────────────┐
                  │   MEMORY  LAYER             │
                  │   ⏱  In-context  → bounded  │
                  │   🧵 Episodic    → per-thread│
                  │   📚 Semantic    → PGVector  │
                  │                    + BM25    │
                  │   📜 Procedural  → tool-defs │
                  └─────────────────────────────┘
                                 │
                                 ▼
              STREAMING  OUTPUT  (SSE · FastAPI · async)
              cached · traced · cost-attributed per node
```

**The hard parts nobody puts in a tutorial:**
`context drift` after 20+ turns · `cold-start retriever latency` (singleton init fixes it) · `concurrent session state bleed` (LangGraph thread isolation fixes it) · `tool-call hallucination on ambiguous schemas` (Pydantic + structured outputs) · `cost explosion under load` (model-cascade routing + Redis cache).

---

## 💼 Experience

<table>
<tr>
<td width="22%" valign="top">

**IMG Systems**<br/>
*Agentic AI & SWE Intern*<br/>
Boston, MA / Remote<br/>
**Aug 2024 — Apr 2025**

</td>
<td valign="top">

- Engineered an **intelligent document-processing pipeline** with Apache Tika, LLM-based extraction, and async Python — **+20% parsing accuracy** across **5K+ profiles/month**, **−15% recruiter processing time**.
- Designed **multi-step agentic screening workflows** in Python and Node.js with **Pydantic-enforced structured output validation** — **95% validation accuracy**, **−70% manual screening time**.
- Built and deployed **FastAPI + Express microservices** on PostgreSQL · Redis · Docker · Kubernetes — **−25% API latency** through query optimization and caching.
- Automated CI/CD with **GitHub Actions** + container orchestration — **zero-downtime releases**.

</td>
</tr>
<tr>
<td width="22%" valign="top">

**Growaza Pvt. Ltd.**<br/>
*Associate SWE Intern*<br/>
SaaS Platform · India<br/>
**Jan 2024 — Jul 2024**

</td>
<td valign="top">

- Integrated **Redis caching + async AJAX workflows** — **+30% API response speed**, **+22% user engagement** for **1K+ DAU**.
- Developed analytics dashboard with **MySQL + D3.js** — **98% data accuracy** across **2K+ SKUs**, enabling data-driven inventory decisions.
- Implemented secure REST APIs with **JWT auth + RBAC**; supported **AWS EC2 / S3** deployments.
- Delivered **3 major product features ahead of schedule** via agile sprint execution.

</td>
</tr>
</table>

---

## 🚀 What I've Shipped

<table>
<tr>
<td width="50%" valign="top">

### 🤖 [BU Life AI](https://bulife-ai.netlify.app) — Live

> **Production multi-agent campus assistant. Real users. Real traffic.**

- **LangGraph supervisor** routes to 3 specialized ReAct agents
- **Hybrid retrieval**: BM25 + **NVIDIA NV-EmbedQA 1024-dim** dense vectors on **PGVector**
- **Redis-cached** model responses — **−70% LLM API calls**
- **SSE streaming** via FastAPI async generators
- **LangSmith tracing** for replayable reasoning chains
- **Dockerized** · deployed on Render + Netlify · CI/CD via GitHub Actions

`Python` `LangGraph` `LangChain` `PGVector` `Redis` `FastAPI` `Docker` `NVIDIA NIM`

</td>
<td width="50%" valign="top">

### 🧮 [Sorting Visualizer](https://sorting-algorithm-visualizerrr.netlify.app) — Live

> **Algorithm pedagogy as state machine.**

- **Redux** as async state machine — 6+ sorting algorithms visualized
- **4 quicksort pivot strategies** — first / last / random / median-of-three
- Live **O(n²) vs O(n log n)** comparison view
- Built 2022 · still ships flawlessly

`React` `Redux` `JavaScript` `Algorithm Design`

</td>
</tr>
<tr>
<td valign="top">

### 📄 [IEEE Paper · Bug Detection](https://github.com/Kushal9889/Deep-Learning-for-Contextual-Bug-Detection-and-Automated-Fixes-in-Software-Systems)

> **Deep Learning for Contextual Bug Detection and Automated Fixes in Software Systems**
> *IEEE ICAICCIT 2024 · First Author*

Neural model that learns code context to surface and patch bugs without explicit rules.

</td>
<td valign="top">

### 📘 [IGI Global Chapter · Cyber-Physical Systems](https://github.com/Kushal9889/Cyber-Physical-Systems-and-the-Future-of-Urban-Living-Decision-Making-Challenges-and-Opportunities)

> **Cyber-Physical Systems: Security and Optimization Strategies**
> *IGI Global 2024 · Co-Author*

Decision-making, security trade-offs, and optimization in urban CPS environments.

</td>
</tr>
</table>

---

## 🧠 What I Actually Know — The Full Agentic Stack

> Not a skills list. A **map of the problem space** I operate in.
> Every row is something I can reason about end-to-end, not name-drop.

| Layer | What I understand deeply |
|---|---|
| **Orchestration** | LangGraph state graphs · supervisor pattern · conditional edges · parallel node execution · human-in-the-loop checkpoints · A2A Protocol · Google ADK |
| **Reasoning** | ReAct internals · scratchpad vs final answer · chain-of-thought · self-reflection patterns · when CoT actively *hurts* |
| **Tool Calling** | Typed tool schemas · function calling API · **Pydantic** output validation · tool-selection failure modes · registry patterns · **MCP (Model Context Protocol)** |
| **Memory** | Context-window budgeting · episodic thread stores · semantic vector retrieval · procedural memory (system prompts) · forgetting strategies |
| **RAG** | **Hybrid BM25 + dense** retrieval · EnsembleRetriever · chunking strategies · re-ranking · why pure semantic fails on keyword queries |
| **Context Engineering** | Token budgeting · drift detection · sliding-window compression · intent re-anchoring · prompt-injection attack surface |
| **Cost Control** | Model-cascade routing (fast→slow) · Redis response caching · batching · **when NOT to call an LLM** |
| **Streaming** | SSE vs WebSocket trade-offs · async FastAPI generators · backpressure · token-level UX vs batch |
| **Observability** | **LangSmith** tracing · reasoning-chain replay · latency attribution per node · cost per trace |
| **Multi-Model** | OpenAI · Claude · Gemini · Groq · NVIDIA NIM · AWS Bedrock · Llama — when to use which, and why |
| **Vector DBs** | PGVector · ChromaDB · Pinecone · HNSW · cosine vs dot product · when RAG breaks |
| **Deployment** | Docker · Kubernetes · GitHub Actions CI/CD · zero-downtime · singleton init · cold-start mitigation |
| **Security** | Prompt injection · tool-call sandboxing · output validation before execution · untrusted-input handling |

---

## 🛠 Stack — Grouped by What It Does in the System

<div align="center">

**Orchestration**<br/>
<img src="https://img.shields.io/badge/LangGraph-1a3a4a?style=flat-square"/>
<img src="https://img.shields.io/badge/LangChain-1a3a4a?style=flat-square"/>
<img src="https://img.shields.io/badge/LangSmith-1a3a4a?style=flat-square"/>
<img src="https://img.shields.io/badge/ReAct-111111?style=flat-square"/>
<img src="https://img.shields.io/badge/MCP-111111?style=flat-square"/>
<img src="https://img.shields.io/badge/A2A_Protocol-111111?style=flat-square"/>
<img src="https://img.shields.io/badge/Google_ADK-4285F4?style=flat-square&logo=google&logoColor=white"/>
<br/><br/>

**Models**<br/>
<img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/Claude-CC785C?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white"/>
<img src="https://img.shields.io/badge/Groq-F55036?style=flat-square"/>
<img src="https://img.shields.io/badge/NVIDIA_NIM-76B900?style=flat-square&logo=nvidia&logoColor=white"/>
<img src="https://img.shields.io/badge/AWS_Bedrock-FF9900?style=flat-square&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/Llama-0467DF?style=flat-square"/>
<br/><br/>

**Memory & Retrieval**<br/>
<img src="https://img.shields.io/badge/PGVector-316192?style=flat-square&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/ChromaDB-FF6B35?style=flat-square"/>
<img src="https://img.shields.io/badge/Pinecone-005EBC?style=flat-square"/>
<img src="https://img.shields.io/badge/BM25_Hybrid-4F98A3?style=flat-square"/>
<img src="https://img.shields.io/badge/EnsembleRetriever-4F98A3?style=flat-square"/>
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/>
<br/><br/>

**Backend**<br/>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white"/>
<img src="https://img.shields.io/badge/Async_Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/SSE-4F98A3?style=flat-square"/>
<img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white"/>
<br/><br/>

**Cloud / DevOps**<br/>
<img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=FF9900"/>
<img src="https://img.shields.io/badge/EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white"/>
<img src="https://img.shields.io/badge/Lambda-FF9900?style=flat-square&logo=awslambda&logoColor=white"/>
<img src="https://img.shields.io/badge/S3-569A31?style=flat-square&logo=amazons3&logoColor=white"/>
<img src="https://img.shields.io/badge/API_Gateway-FF4F8B?style=flat-square&logo=amazonapigateway&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white"/>
<br/><br/>

**Data**<br/>
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/MongoDB-4EA94B?style=flat-square&logo=mongodb&logoColor=white"/>
<img src="https://img.shields.io/badge/Neo4j-008CC1?style=flat-square&logo=neo4j&logoColor=white"/>
<img src="https://img.shields.io/badge/D3.js-F9A03C?style=flat-square&logo=d3.js&logoColor=white"/>
<br/><br/>

**Frontend**<br/>
<img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB"/>
<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=next.js&logoColor=white"/>
<img src="https://img.shields.io/badge/Redux-593D88?style=flat-square&logo=redux&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/>
<br/><br/>

**Languages**<br/>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
<img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white"/>
<img src="https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white"/>

</div>

---

## 🎓 Education & Credentials

<table>
<tr>
<td width="50%" valign="top">

### Boston University
**M.S. Computer Science** · Expected **December 2026** · GPA **3.6**
*Coursework: Generative AI · AI Systems · Web Mining & Graph Analytics · Software Engineering · Cloud Computing · DevOps*

</td>
<td width="50%" valign="top">

### IIIT Design & Manufacturing Jabalpur
**B.Tech Computer Science & Engineering** · 2020 – 2024
*Tier-1 Indian Institute of Information Technology · Algorithms · OS · DBMS · Distributed Systems*

</td>
</tr>
</table>

<div align="center">

**Publications · Certifications · Distinctions**

[![IEEE](https://img.shields.io/badge/IEEE_ICAICCIT_2024-Bug_Detection_Paper-00629B?style=for-the-badge&logo=ieee&logoColor=white)](https://github.com/Kushal9889/Deep-Learning-for-Contextual-Bug-Detection-and-Automated-Fixes-in-Software-Systems)
[![IGI](https://img.shields.io/badge/IGI_Global_2024-Cyber_Physical_Systems-1A3A4A?style=for-the-badge&logoColor=white)](https://github.com/Kushal9889/Cyber-Physical-Systems-and-the-Future-of-Urban-Living-Decision-Making-Challenges-and-Opportunities)
[![JEE](https://img.shields.io/badge/JEE_Mains-99.1_percentile-D29922?style=for-the-badge&logoColor=white)](https://drive.google.com/file/d/1XbK1T7RZahWRamhUVBGbnRBu_8fGOR47/view)

[![IBM RAG](https://img.shields.io/badge/IBM-RAG_&_Agentic_AI_Professional-052FAD?style=flat-square&logo=ibm&logoColor=white)](https://www.coursera.org)
[![IBM AI](https://img.shields.io/badge/IBM-AI_Engineering_Professional-052FAD?style=flat-square&logo=ibm&logoColor=white)](https://www.coursera.org)
[![AWS](https://img.shields.io/badge/AWS-Certified_Cloud_Practitioner-FF9900?style=flat-square&logo=amazonaws&logoColor=white)](https://www.coursera.org/account/accomplishments/verify/4L1ZWS6VK2L8)
[![NVIDIA](https://img.shields.io/badge/NVIDIA-Agentic_AI_Professional-76B900?style=flat-square&logo=nvidia&logoColor=white)](https://www.nvidia.com)

</div>

---

## 📊 GitHub Activity — Built in Public

<div align="center">

<img height="180" src="https://github-readme-stats.vercel.app/api?username=Kushal9889&show_icons=true&hide_border=true&bg_color=0d1117&title_color=58A6FF&icon_color=58A6FF&text_color=c9d1d9&rank_icon=github&include_all_commits=true&count_private=true"/>
<img height="180" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Kushal9889&layout=compact&hide_border=true&bg_color=0d1117&title_color=58A6FF&text_color=c9d1d9&langs_count=8&hide=jupyter%20notebook"/>

<br/>

<img width="62%" src="https://streak-stats.demolab.com/?user=Kushal9889&theme=dark&hide_border=true&background=0d1117&ring=58A6FF&fire=58A6FF&currStreakLabel=58A6FF"/>

<br/>

<!-- ACTIVITY GRAPH ─────────────────────────────────────────────────────── -->
<img width="92%" src="https://github-readme-activity-graph.vercel.app/graph?username=Kushal9889&bg_color=0d1117&color=58A6FF&line=58A6FF&point=ffffff&area=true&hide_border=true&custom_title=Contribution%20Pulse"/>

<br/>

<!-- SNAKE ANIMATION ────────────────────────────────────────────────────── -->
<!-- Requires GitHub Actions workflow — see below -->
<img width="92%" src="https://raw.githubusercontent.com/Kushal9889/Kushal9889/output/github-contribution-grid-snake-dark.svg?v=2" alt="contribution snake animation"/>

<br/><br/>

<!-- TROPHY WALL ────────────────────────────────────────────────────────── -->
<img src="https://github-profile-trophy.vercel.app/?username=Kushal9889&theme=darkhub&no-frame=true&no-bg=true&margin-w=8&column=7"/>

</div>

---

## 🔬 Currently Building

- **Peer-to-peer agentic networks** — agents that research, critique, evaluate, and loop with coherent shared memory across the entire collective (no central supervisor).
- **Context-engineering toolkit** — drift detection, intent re-anchoring, and dynamic prompt compression as a reusable middleware layer for any LangGraph project.
- **Production-grade evaluation harness** — replayable trace diffing for non-deterministic agent outputs, because `eval=accuracy` is a lie for generative systems.

> If you are working on coordinated multi-agent systems, agent-evaluation tooling, or context engineering — **let's talk.** I want to compare notes.

---

## ✍️ Writing & Talks

> *Coming soon — drafting a series on what actually breaks when agentic systems scale past 100 concurrent users. Subscribe via the LinkedIn link above.*

---

<div align="center">

## 📬 Let's Talk

**I'm actively interviewing for Summer 2026 internships and full-time roles in Agentic AI, Applied AI, ML Engineering, and AI-focused SWE positions.**

I respond to thoughtful messages within 24 hours.

<br/>

<a href="https://linkedin.com/in/kushal-gaddamwar"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>&nbsp;
<a href="mailto:kushal7887pd@gmail.com"><img src="https://img.shields.io/badge/Email-kushal7887pd%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>&nbsp;
<a href="tel:+18573284611"><img src="https://img.shields.io/badge/Phone-%2B1%20(857)%20328--4611-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/></a>&nbsp;
<a href="https://bulife-ai.netlify.app"><img src="https://img.shields.io/badge/Live%20Project-BU%20Life%20AI-00C7B7?style=for-the-badge&logoColor=white"/></a>

<br/><br/>

*Based in Boston · Authorized to work in the U.S. via F-1 OPT (2026) · Open to relocation for the right team.*

<br/>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,30&height=120&section=footer"/>

</div>

<!--
================================================================================
  APPENDIX A — SNAKE ANIMATION GITHUB ACTIONS WORKFLOW
  Create file at:  .github/workflows/snake.yml
  in a repo named `Kushal9889/Kushal9889` (your profile repo).
  The output branch hosts the SVG that's referenced above.
================================================================================

name: Generate Snake Animation
on:
  schedule:
    - cron: "0 */12 * * *"   # every 12 hours
  workflow_dispatch:
  push:
    branches: [main]
jobs:
  generate:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: Platane/snk/svg-only@v3
        with:
          github_user_name: Kushal9889
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
      - uses: crazy-max/ghaction-github-pages@v3
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

================================================================================
  APPENDIX B — KEYWORDS FOR ATS / RECRUITER SEARCH (hidden, scrape-friendly)
================================================================================

Agentic AI · Multi-Agent Systems · LangGraph · LangChain · LangSmith · ReAct ·
Supervisor Pattern · MCP · Model Context Protocol · A2A Protocol · Google ADK ·
RAG · Retrieval Augmented Generation · Hybrid Retrieval · BM25 · Dense Retrieval ·
EnsembleRetriever · Embeddings · Vector Search · PGVector · ChromaDB · Pinecone ·
Semantic Search · Chunking Strategies · Re-ranking ·
OpenAI · GPT-4 · Claude · Anthropic · Gemini · Groq · Llama · NVIDIA NIM ·
AWS Bedrock · Prompt Engineering · Structured Outputs · Tool Calling · Function Calling ·
Pydantic · Python · Async Python · FastAPI · REST APIs · Microservices ·
Node.js · Express · TypeScript · JavaScript · React · Next.js · Redux ·
PostgreSQL · MySQL · MongoDB · Neo4j · Redis · D3.js ·
AWS · EC2 · S3 · Lambda · API Gateway · Docker · Kubernetes · GitHub Actions ·
CI/CD · Zero-Downtime Deployment · SSE · Server-Sent Events · WebSocket ·
LLM Observability · Distributed Tracing · Production AI · MLOps · LLMOps ·
Context Engineering · Token Budgeting · Cost Optimization · Model Cascade ·
IEEE · Published Researcher · Boston University · MSCS · F-1 OPT 2026.
-->
