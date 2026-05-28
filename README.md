<div align="center">

<a href="https://github.com/Kushal9889">
  <img src="https://raw.githubusercontent.com/Kushal9889/Kushal9889/main/assets/hero.svg" alt="kushal gaddamwar — agentic ai engineer" width="100%"/>
</a>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=16&duration=2600&pause=900&color=58A6FF&center=true&vCenter=true&width=820&lines=supervisor+%E2%86%92+router+%E2%86%92+ReAct+%E2%86%92+tools+%E2%86%92+memory+%E2%86%92+stream;the+demo+is+easy.+production+is+a+different+sport.;context+drift+%E2%80%A2+token+budgets+%E2%80%A2+thread+isolation+%E2%80%A2+hybrid+RAG;BU+MSCS+%E2%80%A2+IEEE+published+%E2%80%A2+open+to+hire+%E2%80%9426" alt="typing"/>

<br/><br/>

<a href="https://linkedin.com/in/kushal-gaddamwar"><img src="https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="mailto:kushal7887pd@gmail.com"><img src="https://img.shields.io/badge/email-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://bulife-ai.netlify.app"><img src="https://img.shields.io/badge/live_demo-00C7B7?style=for-the-badge&logo=netlify&logoColor=white"/></a>
<a href="https://github.com/Kushal9889?tab=followers"><img src="https://img.shields.io/github/followers/Kushal9889?style=for-the-badge&color=58A6FF&labelColor=0d1117&label=follow"/></a>

<br/>

<sub><img src="https://komarev.com/ghpvc/?username=Kushal9889&style=flat-square&color=58A6FF&label=profile+views"/></sub>

</div>

---

### hey

I got into this work because most "AI products" are a prompt wrapped in a UI, and I couldn't stop thinking about what happens when you actually engineer the system *around* the model. That's where things get interesting, and where everything also tends to break.

Now I spend my days building multi-agent systems that handle real concurrent users. Thread-isolated sessions, token-budgeted context, hybrid retrieval that doesn't fold on keyword queries. Some of it is in production. Most of it taught me something the tutorials skipped.

Finishing my **MS CS at Boston University (Dec 2026)**. Before that, **B.Tech at IIIT Jabalpur**. Published in **IEEE** along the way. Currently open to hire for **AI / Agentic roles starting 2026**, full-time or summer.

---

## how I think about agentic systems

The thing I debug against when production breaks at 2 AM:

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

The interesting parts nobody puts in tutorials: **context drift** after the 20th turn, **cold-start retriever latency**, **state bleed across concurrent sessions**, **tool-call hallucinations on ambiguous schemas**, **cost explosion under load**. Every one of those is a story I can tell you.

---

## stuff I've shipped

🤖 **[BU Life AI](https://bulife-ai.netlify.app)** — live, real users, real traffic. LangGraph supervisor routing to three ReAct agents over a PGVector + BM25 hybrid index, NVIDIA NV-EmbedQA 1024-dim. SSE streaming on async FastAPI. Redis caching cut model API calls by 70%. LangSmith for tracing what the agent actually did vs what it claimed it did. The whole thing is Dockerized and runs on Render + Netlify with zero-downtime deploys via GitHub Actions. *This is the project I'd point at if you want to know how I think.*

🧮 **[Sorting Visualizer](https://sorting-algorithm-visualizerrr.netlify.app)** — built this in 2022 to internalize how Redux works as a state machine. Six sorting algorithms, four quicksort pivot strategies, live O(n²) vs O(n log n) comparison. Still ships. *Old work, but I keep linking it because it still does its job.*

📄 **[IEEE Paper, ICAICCIT '24](https://github.com/Kushal9889/Deep-Learning-for-Contextual-Bug-Detection-and-Automated-Fixes-in-Software-Systems)** — first author, deep learning for bug detection that learns code context instead of relying on rules. And a [chapter in IGI Global](https://github.com/Kushal9889/Cyber-Physical-Systems-and-the-Future-of-Urban-Living-Decision-Making-Challenges-and-Opportunities) on cyber-physical systems security.

---

## where I've actually done this work

Real production, not just side projects:

- **IMG Systems** (Boston / Remote, Aug '24 – Apr '25) — built the agentic document pipeline + screening workflows. Apache Tika + LLM extraction handling 5K profiles/month, Pydantic-validated screening that cut manual review by 70%, FastAPI microservices on K8s where I shaved 25% off API latency. Also wired the CI/CD that made zero-downtime deploys actually zero-downtime.
- **Growaza** (India, Jan – Jul '24) — SaaS work. Redis caching that bumped API speed 30%, a D3.js analytics dashboard tracking 2K+ SKUs at 98% data accuracy, secure REST APIs with JWT + RBAC on AWS EC2/S3.

Full bullet-pointed version on [LinkedIn](https://linkedin.com/in/kushal-gaddamwar). A GitHub README is not the place for a CV dump.

---

## what I actually know

> Not a skills list. A map of the problem space I work inside.

| layer | what I can reason about end-to-end |
|---|---|
| orchestration | LangGraph state graphs · supervisor pattern · conditional edges · parallel nodes · A2A · Google ADK |
| reasoning | ReAct internals · scratchpad vs final answer · CoT · self-reflection · when CoT *hurts* |
| tool calling | typed schemas · Pydantic validation · failure modes · registry patterns · MCP |
| memory | in-context budgeting · episodic threads · semantic retrieval · forgetting |
| RAG | BM25 + dense hybrid · EnsembleRetriever · chunking · re-ranking · why pure semantic dies on keywords |
| context engineering | drift · token budgets · sliding-window compression · intent re-anchoring · prompt-injection surface |
| cost control | model cascade routing · response caching · batching · **when not to call an LLM** |
| streaming | SSE vs WS · async FastAPI generators · backpressure · token-level UX |
| observability | LangSmith tracing · reasoning replay · per-node latency + cost attribution |
| multi-model | OpenAI · Claude · Gemini · Groq · NVIDIA NIM · AWS Bedrock · Llama — when each one matters |
| stores | PGVector · ChromaDB · Pinecone · Redis · Postgres · Mongo · Neo4j · HNSW indexes |
| infra | Docker · K8s · GitHub Actions CI/CD · zero-downtime · singleton init · cold-start mitigation |
| security | prompt injection · tool sandboxing · output validation before exec · untrusted input |

<div align="center">

<sub>

`Python` · `FastAPI` · `Async Python` · `Pydantic` · `LangChain` · `LangGraph` · `LangSmith` · `ReAct` · `MCP` ·
`PGVector` · `ChromaDB` · `Pinecone` · `Redis` · `PostgreSQL` · `MongoDB` · `Neo4j` ·
`OpenAI` · `Claude` · `Gemini` · `Groq` · `Llama` · `AWS Bedrock` · `NVIDIA NIM` ·
`AWS` · `EC2` · `S3` · `Lambda` · `Docker` · `Kubernetes` · `GitHub Actions` · `SSE` ·
`React` · `Next.js` · `Redux` · `TypeScript` · `Node.js` · `Express` · `C++` · `Java` · `SQL`

</sub>

</div>

---

## now  ·  may 2026

- shipping **peer-to-peer agent networks** — no central supervisor. Agents that research, critique, evaluate, and loop with coherent shared memory across the whole collective. The coordination problem is genuinely hard.
- prototyping a **context-engineering middleware** — drift detection, intent re-anchoring, and dynamic prompt compression as a reusable layer for any LangGraph project.
- thinking about **evaluation for non-deterministic systems** — `accuracy` is a lie for generative outputs. Currently looking at trace-diffing and replayable rubrics.

If you're working on coordinated multi-agent systems or agent evaluation, ping me. I'd rather compare notes than network.

---

## github

<div align="center">

<img height="170" src="https://github-readme-stats-sigma-five.vercel.app/api?username=Kushal9889&show_icons=true&hide_border=true&bg_color=0d1117&title_color=58A6FF&icon_color=58A6FF&text_color=c9d1d9&rank_icon=github&include_all_commits=true&count_private=true"/>
<img height="170" src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=Kushal9889&layout=compact&hide_border=true&bg_color=0d1117&title_color=58A6FF&text_color=c9d1d9&langs_count=7&hide=jupyter%20notebook"/>

<br/>

<img width="62%" src="https://streak-stats.demolab.com/?user=Kushal9889&theme=dark&hide_border=true&background=0d1117&ring=58A6FF&fire=58A6FF&currStreakLabel=58A6FF"/>

<br/><br/>

<img width="90%" src="https://github-readme-activity-graph.vercel.app/graph?username=Kushal9889&bg_color=0d1117&color=58A6FF&line=58A6FF&point=ffffff&area=true&hide_border=true&custom_title=contribution%20pulse"/>

<br/>

<img width="90%" src="https://raw.githubusercontent.com/Kushal9889/Kushal9889/output/github-contribution-grid-snake-dark.svg" alt="contribution snake"/>

</div>

---

<div align="center">

<sub>

hiring for **agentic AI · applied AI · ML engineering · AI-focused SWE** — full-time '26 or summer? I'm around.<br/>
[linkedin](https://linkedin.com/in/kushal-gaddamwar)  ·  [kushal7887pd@gmail.com](mailto:kushal7887pd@gmail.com)  ·  [live demo](https://bulife-ai.netlify.app)

</sub>

</div>
