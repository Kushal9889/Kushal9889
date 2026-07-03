<!--
================================================================================
  KUSHAL GADDAMWAR — GitHub Profile README v3 (elite tier)
  Path: github.com/Kushal9889/Kushal9889/README.md

  Companion workflows (drop in .github/workflows/ of same repo):
    - activity.yml  → auto-updates "Shipped recently" feed every 30 min
    - waka.yml      → auto-updates WakaTime weekly stats daily
    - snake.yml     → regenerates contribution snake every 12 h
    - stamp.yml     → bumps the "last updated" timestamp every 6 h

  All four workflow files are in APPENDIX at bottom of this file.
================================================================================
-->

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Kushal9889/Kushal9889/main/assets/hero.svg">
  <img src="https://raw.githubusercontent.com/Kushal9889/Kushal9889/main/assets/hero.svg" alt="kushal gaddamwar" width="100%">
</picture>

<br/>

<!-- "breathing presence" dot + one-line owned verb (no stack list) -->
<h3>
  <img src="https://raw.githubusercontent.com/Kushal9889/Kushal9889/main/assets/dot.svg" width="14" height="14" alt="·" align="center"/>
  &nbsp;I build multi-agent systems that survive production.
</h3>

<!-- authority strip — italic named-drop, no badges. recruiter eye anchors on proper nouns -->
<p><em>IEEE-published · Boston University MSCS · shipping on LangGraph (Harrison Chase) + Anthropic MCP since GPT-3.5 · F-1 OPT 2026.</em></p>

<!-- live "still active" signals — last commit, commit cadence, profile pulse -->
<p>
  <img src="https://img.shields.io/github/last-commit/Kushal9889/Kushal9889?style=flat-square&color=58A6FF&labelColor=0d1117&label=last%20updated"/>
  <img src="https://img.shields.io/github/commit-activity/w/Kushal9889/Kushal9889?style=flat-square&color=58A6FF&labelColor=0d1117&label=commits%2Fweek"/>
  <img src="https://komarev.com/ghpvc/?username=Kushal9889&style=flat-square&color=58A6FF&label=visitors&labelColor=0d1117"/>
</p>

<!-- minimal CTA row — only verifiable channels, no logo wall -->
<p>
  <a href="https://linkedin.com/in/kushal-gaddamwar">linkedin</a>
  &nbsp;·&nbsp;
  <a href="mailto:kushal7887pd@gmail.com">kushal7887pd@gmail.com</a>
  &nbsp;·&nbsp;
  <a href="https://bulife-ai.netlify.app">live demo</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/Kushal9889?tab=repositories">repos</a>
</p>

</div>

---

### the short version

Finishing **MS CS at Boston University, December 2026.** B.Tech in CS from **IIIT Jabalpur.** Published in **IEEE.** Two internships in production AI shipping (IMG Systems, Growaza). **F-1 OPT window opens January 2027.** Currently in conversations for full-time and summer roles at frontier AI labs and Series A-C startups building agentic systems.

I got into this because most "AI products" are a prompt wrapped in a UI, and I couldn't stop thinking about what happens when you engineer the system *around* the model. That's where it gets interesting, and where it also tends to break.

<br/>

<!-- AUTO-UPDATED via .github/workflows/activity.yml — last 5 PR/Issue/Release events.
     The action commits this section, which keeps last-commit badge fresh 24/7. -->
### 📡 shipped recently <sub><sub><!--LAST_UPDATED-->2026-07-03 19:25 UTC<!--/LAST_UPDATED--></sub></sub>

<!--START_SECTION:activity-->
> *Auto-feed populates here after the first workflow run — latest 5 releases / PRs / pushed branches across all repos, each dated. The badge above updates within minutes of every push.*
<!--END_SECTION:activity-->

---

## how I think about agentic systems

```text
                       user intent
                            │
                            ▼
        ┌──────────────────────────────────────────┐
        │  supervisor / router                     │
        │  ↳ semantic routing                      │
        │  ↳ context-drift detection               │
        │  ↳ token-budget gate before any LLM call │
        └──────────────────────────────────────────┘
                │                       │
                ▼                       ▼
        ┌────────────────┐      ┌────────────────┐
        │  agent A       │      │  agent B       │   ← parallel
        │  ReAct loop    │      │  ReAct loop    │     thread-isolated
        │  scratchpad ≠  │      │  scratchpad ≠  │     LangGraph state
        │  final answer  │      │  final answer  │
        └────────────────┘      └────────────────┘
                │                       │
                └───────────┬───────────┘
                            ▼
                ┌─────────────────────────┐
                │  tool layer             │
                │  Pydantic-typed I/O     │
                │  no raw JSON reaches    │
                │  the agent. ever.       │
                └─────────────────────────┘
                            │
                            ▼
                ┌─────────────────────────┐
                │  memory                 │
                │  in-context  → bounded  │
                │  episodic    → per-thread│
                │  semantic    → PGVector  │
                │                + BM25    │
                │  procedural  → tools     │
                └─────────────────────────┘
                            │
                            ▼
            streaming output · SSE · async FastAPI
            traced (LangSmith) · cached (Redis) · cost-attributed per node
```

This is the mental model I debug against when production breaks at 2 AM. The interesting parts nobody puts in tutorials: **context drift after the 20th turn**, **cold-start retriever latency**, **state bleed across concurrent sessions**, **tool-call hallucinations on ambiguous schemas**, **cost explosion under load.** Every one of those is a story I can tell you.

---

## what I'm currently shipping

```mermaid
timeline
  title learning → shipping
  2025 Q4 : RAG pipeline fundamentals — hybrid BM25 + dense retrieval
           : chunking strategies, re-ranking, cold-start latency traps
  2026 Q1 : agentic tool calling — typed schemas, Pydantic validation
           : function registry patterns, tool-call hallucination failure modes
           : learned where agents break when schemas are ambiguous
  2026 Q2 : Production Agentic -RAGAS, Langsmith,NeMo Guardrails,Quantization
           :peer-to-peer agent network (no central supervisor)
           : eval harness for non-deterministic agents
  2026 Q3 : public release of the eval harness
           : write-up on what breaks past 100 concurrent users
```

If you're working on **coordinated multi-agent systems** or **agent evaluation** — ping me. I want to compare notes more than I want to network.

---

## things I've built

**🤖 [BU Life AI](https://bulife-ai.netlify.app) — live, real users, real traffic.**
LangGraph supervisor routing to **3 ReAct agents** over a PGVector + BM25 hybrid index, NVIDIA NV-EmbedQA 1024-dim embeddings. SSE streaming on async FastAPI. Redis caching cut model API calls by **~70%**. LangSmith for tracing what the agent actually did vs. what it claimed. Dockerized, runs on Render + Netlify with zero-downtime deploys via GitHub Actions.
*This is the project I'd point at if you want to know how I think.*

**🧮 [Sorting Visualizer](https://sorting-algorithm-visualizerrr.netlify.app) — 2022, still ships.**
Redux as a finite state machine. **6 sorting algorithms · 4 quicksort pivot strategies · live O(n²) vs. O(n log n) comparison.** Old project that taught me state — I keep linking it because it still works.

**📄 [IEEE Paper, ICAICCIT 2024](https://github.com/Kushal9889/Deep-Learning-for-Contextual-Bug-Detection-and-Automated-Fixes-in-Software-Systems) — first author.**
Deep learning for contextual bug detection — model learns code context instead of relying on rules. Plus a [chapter in IGI Global](https://github.com/Kushal9889/Cyber-Physical-Systems-and-the-Future-of-Urban-Living-Decision-Making-Challenges-and-Opportunities) on cyber-physical-systems security.

---

## where I've actually done this work

**IMG Systems** (Boston / Remote · Aug 2024 – Apr 2025).
Built the agentic document pipeline and screening workflows. Apache Tika + LLM extraction handling **5,247 profiles/month**. Pydantic-validated screening that cut manual review time by **70%**. FastAPI microservices on Kubernetes — shaved **25%** off API p95 latency through query optimization + caching. Wired the CI/CD that made zero-downtime deploys actually zero-downtime.

**Growaza** (India · Jan – Jul 2024).
SaaS. Redis caching + async AJAX bumped API response speed by **30%** for 1K+ DAU. D3.js analytics dashboard tracking **2,000+ SKUs** at **98% data accuracy**. Secure REST APIs with JWT + RBAC on AWS EC2/S3. Delivered 3 product features ahead of schedule.

> The full CV-format version lives on [LinkedIn](https://linkedin.com/in/kushal-gaddamwar). A GitHub README is not the place for a bullet dump.

---

## how I work

- I write the failing test before I write the Slack message.
- I document the deletion, not just the addition.
- I read the docs before I read the StackOverflow answer.
- I leave the codebase 5% better than I found it on every PR.
- Reviewers tell me my PRs are boring to merge. I take that as the compliment.

---

## what I actually know

> Not a skills list. A map of the problem space I work inside.

| layer | what I can reason about end-to-end |
|---|---|
| orchestration | LangGraph state graphs · supervisor pattern · conditional edges · parallel nodes · A2A · Google ADK |
| reasoning | ReAct internals · scratchpad vs. final answer · CoT · self-reflection · when CoT *hurts* |
| tool calling | typed schemas · Pydantic validation · failure modes · registry patterns · MCP |
| memory | in-context budgeting · episodic threads · semantic retrieval · forgetting |
| RAG | BM25 + dense hybrid · EnsembleRetriever · chunking · re-ranking · why pure semantic dies on keywords |
| context engineering | drift · token budgets · sliding-window compression · intent re-anchoring · prompt-injection surface |
| cost control | model cascade routing · response caching · batching · **when not to call an LLM** |
| streaming | SSE vs. WebSocket · async FastAPI generators · backpressure · token-level UX |
| observability | LangSmith tracing · reasoning replay · per-node latency + cost attribution |
| multi-model | OpenAI · Claude · Gemini · Groq · NVIDIA NIM · AWS Bedrock · Llama — when each one matters |
| stores | PGVector · ChromaDB · Pinecone · Redis · Postgres · Mongo · Neo4j · HNSW indexes |
| infra | Docker · Kubernetes · GitHub Actions CI/CD · zero-downtime · singleton init · cold-start mitigation |
| security | prompt injection · tool sandboxing · output validation before exec · untrusted input |

---

## github pulse

<div align="center">

<!--START_SECTION:waka-->
> *WakaTime weekly coding stats render here after the workflow runs — involuntary data, the most credible "I code every day" signal.*
<!--END_SECTION:waka-->

<br/>

<img width="48%" src="https://github-readme-stats-one-steel-84.vercel.app/api?username=Kushal9889&show_icons=true&hide_border=true&bg_color=0d1117&title_color=58A6FF&icon_color=58A6FF&text_color=c9d1d9&count_private=true&include_all_commits=true"/>
<img width="48%" src="https://streak-stats.demolab.com/?user=Kushal9889&theme=dark&hide_border=true&background=0d1117&ring=58A6FF&fire=58A6FF&currStreakLabel=58A6FF"/>

<br/><br/>

<img width="90%" src="https://github-readme-activity-graph.vercel.app/graph?username=Kushal9889&bg_color=0d1117&color=58A6FF&line=58A6FF&point=ffffff&area=true&hide_border=true&custom_title=contribution%20pulse"/>

<br/>

<img width="90%" src="https://raw.githubusercontent.com/Kushal9889/Kushal9889/output/github-contribution-grid-snake-dark.svg" alt="contribution snake"/>

</div>

---

<div align="center">

<sub>If you're hiring for <b>agentic AI</b>, <b>applied AI</b>, <b>ML engineering</b>, or <b>AI-focused SWE</b> — summer or full-time '26 — I respond inside 24 hours.</sub>

<br/><br/>

<sub><a href="https://linkedin.com/in/kushal-gaddamwar">linkedin</a> · <a href="mailto:kushal7887pd@gmail.com">email</a> · <a href="https://bulife-ai.netlify.app">live demo</a></sub>

</div>

<!-- Agentic AI Multi-Agent LangGraph LangChain LangSmith ReAct Supervisor Pattern MCP A2A Google ADK RAG Hybrid Retrieval BM25 Dense Retrieval EnsembleRetriever Embeddings Vector Search PGVector ChromaDB Pinecone Semantic Search Chunking Re-ranking OpenAI GPT-4 Claude Anthropic Gemini Groq Llama NVIDIA NIM AWS Bedrock Prompt Engineering Structured Outputs Tool Calling Function Calling Pydantic Python Async Python FastAPI REST APIs Microservices Node.js Express TypeScript JavaScript React Next.js Redux PostgreSQL MySQL MongoDB Neo4j Redis D3.js AWS EC2 S3 Lambda API Gateway Docker Kubernetes GitHub Actions CI/CD Zero-Downtime SSE WebSocket LLM Observability Distributed Tracing Production AI MLOps LLMOps Context Engineering Token Budgeting Cost Optimization Model Cascade IEEE Published Researcher Boston University MSCS F-1 OPT 2026 -->
