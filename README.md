<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,40:0f2027,100:1a3a4a&height=210&section=header&text=Kushal%20Gaddamwar&fontSize=52&fontColor=ffffff&fontAlignY=36&desc=I%20build%20AI%20systems%20that%20actually%20work%20in%20production&descAlignY=57&descSize=16&animation=fadeIn"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=17&duration=2800&pause=1000&color=58A6FF&center=true&vCenter=true&width=800&lines=Supervisor+%E2%86%92+Router+%E2%86%92+ReAct+Agent+%E2%86%92+Tool+%E2%86%92+Memory+%E2%86%92+Output;Context+drift.+Token+budgets.+Thread+isolation.+Hybrid+RAG.;Not+just+prompting+LLMs+%E2%80%94+orchestrating+them+as+systems.;BU+MSCS+Dec+2026+%7C+IEEE+Published+%7C+F-1+OPT+2026;Open+to+Agentic+AI+%2F+Applied+AI+%2F+SWE+roles" alt="typing"/>

<br/><br/>
<a href="https://linkedin.com/in/kushal-gaddamwar"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>&nbsp;
<a href="mailto:kushal7887pd@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>&nbsp;
<a href="https://bulife-ai.netlify.app"><img src="https://img.shields.io/badge/%F0%9F%9A%80_BU_Life_AI-00C7B7?style=for-the-badge&logo=netlify&logoColor=white"/></a>&nbsp;
<img src="https://komarev.com/ghpvc/?username=Kushal9889&style=for-the-badge&color=58A6FF&label=VISITORS"/>

</div>

---

## Hey, I'm Kushal

I'm an agentic AI engineer finishing my MSCS at Boston University (December 2026). I build multi-agent systems — not the demo kind, the kind that handles real concurrent users with thread-isolated sessions, token-budgeted context, and hybrid RAG pipelines that stay fast and cheap in production.

The thing that got me into this space: most "AI products" are just a prompt wrapped in a UI. I got obsessed with what happens when you actually engineer the system around the model — routers, memory layers, tool registries, cost controls, observability. That's what I spend my time on.

---

## How I think about agentic systems

Every system I build follows this architecture. It's not a diagram from a textbook — it's the actual mental model I debug against when things break in production.

```text
  USER INTENT
      │
      ▼
  SUPERVISOR / ROUTER  ──── semantic routing · context drift check · token budget gate
      │
      ├──────────────────────────────────┐
      ▼                                  ▼
  AGENT A (ReAct)              AGENT B (ReAct)   ← parallel · thread-isolated
  Reason → Act → Observe       Reason → Act → Observe
  Scratchpad ≠ Final Answer    Scratchpad ≠ Final Answer
      │                                  │
      └──────────────┬───────────────────┘
                     ▼
               TOOL LAYER
     search() · retrieve() · compute() · write()
     Pydantic-typed outputs — no unvalidated JSON reaching the agent
                     │
                     ▼
               MEMORY LAYER
     In-context   →  LangGraph state, token-budgeted, never unbounded
     Episodic     →  per-session thread store, concurrent-safe
     Semantic     →  PGVector + BM25 hybrid retrieval
     Procedural   →  tool schemas + agent instructions
                     │
                     ▼
         STREAMING OUTPUT  (SSE · FastAPI · Redis cache · LangSmith traces)
```

The hard parts nobody talks about: **context drift** (long conversations leaving the original intent), **cold-start retriever latency** (solved with singleton init), and **concurrent session state bleed** (solved with LangGraph thread isolation). These are the things that break real systems.

---

## 🧠 What I Actually Know — The Full Agentic Stack

> This is not a skills list. This is a **map of the problem space** I operate in.  
> Every row below is something I can reason about end-to-end, not just name-drop.

| Domain | What I understand deeply |
|--------|--------------------------|
| **Orchestration** | LangGraph state graphs · supervisor pattern · conditional edges · parallel node execution · human-in-the-loop checkpoints |
| **Reasoning** | ReAct loop internals · scratchpad vs final_answer · chain-of-thought prompting · self-reflection patterns · when CoT fails |
| **Tool Calling** | Typed tool schemas · function calling API · Pydantic output validation · tool selection failure modes · registry patterns |
| **Memory** | In-context window limits · episodic thread stores · semantic vector retrieval · procedural memory (system prompts) · forgetting strategies |
| **RAG** | Hybrid BM25 + dense retrieval · EnsembleRetriever · chunking strategies · re-ranking · why pure semantic fails on keyword queries |
| **Context Engineering** | Token budgeting · context drift · sliding window compression · intent re-anchoring · prompt injection attack surface |
| **Cost Control** | Model routing (fast→slow cascade) · response caching (Redis) · batching · when NOT to call an LLM |
| **Streaming** | SSE vs WebSocket tradeoffs · async FastAPI generators · backpressure · token-level UX vs batch |
| **Observability** | LangSmith tracing · reasoning chain replay · latency attribution per node · cost per trace |
| **Protocols** | MCP (Model Context Protocol) · tool schema standards · agent communication interfaces |
| **Multi-Model** | OpenAI API · Claude · Groq (low-latency) · NVIDIA NIM · AWS Bedrock · Llama · when to use which |
| **Vector DBs** | PGVector · ChromaDB · embedding dimensions · HNSW index · cosine vs dot product · when RAG breaks |
| **Deployment** | Docker · Kubernetes · GitHub Actions CI/CD · zero-downtime · singleton init patterns · cold-start mitigation |
| **Security** | Prompt injection · tool call sandboxing · output validation before execution · untrusted input handling |

---

## Stack — grouped by what it does in the system

<div align="center">

**Orchestration**<br/>
<img src="https://img.shields.io/badge/LangGraph-1a3a4a?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/LangChain-1a3a4a?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/LangSmith-1a3a4a?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/ReAct-111111?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/MCP-111111?style=flat-square&logoColor=white"/>
<br/><br/>

**Models**<br/>
<img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/Claude-CC785C?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/Groq-F55036?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/NVIDIA_NIM-76B900?style=flat-square&logo=nvidia&logoColor=white"/>
<img src="https://img.shields.io/badge/AWS_Bedrock-FF9900?style=flat-square&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/Llama-0467DF?style=flat-square&logoColor=white"/>
<br/><br/>

**Memory & Retrieval**<br/>
<img src="https://img.shields.io/badge/PGVector-316192?style=flat-square&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/ChromaDB-FF6B35?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/BM25_Hybrid-4F98A3?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/EnsembleRetriever-4F98A3?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/>
<br/><br/>

**Backend**<br/>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/Async_Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/SSE-4F98A3?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white"/>
<br/><br/>

**Cloud & Data**<br/>
<img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=FF9900"/>
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/MongoDB-4EA94B?style=flat-square&logo=mongodb&logoColor=white"/>
<img src="https://img.shields.io/badge/Neo4j-008CC1?style=flat-square&logo=neo4j&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white"/>
<br/><br/>

**Frontend**<br/>
<img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB"/>
<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=next.js&logoColor=white"/>
<img src="https://img.shields.io/badge/Redux-593D88?style=flat-square&logo=redux&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
<img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white"/>

</div>

---

## What I've shipped

**[BU Life AI](https://bulife-ai.netlify.app)** — LangGraph multi-agent system, live with real users. Supervisor routes to three ReAct agents, backed by hybrid BM25 + NVIDIA NV-EmbedQA 1024-dim vector search over PGVector. Redis caching cut LLM API calls by 70%. SSE streaming, LangSmith tracing, full Docker deploy on Render + Netlify.

**[Sorting Visualizer](https://sorting-algorithm-visualizerrr.netlify.app)** — Redux async state machine, 6+ algorithms, 4 quicksort pivot strategies, live O(n²) vs O(n log n) comparison. Built this in 2022, still runs perfectly.

---

## GitHub activity

<div align="center">
<img height="165" src="https://github-readme-stats.vercel.app/api?username=Kushal9889&show_icons=true&hide_border=true&bg_color=0d1117&title_color=58A6FF&icon_color=58A6FF&text_color=c9d1d9&rank_icon=github&include_all_commits=true&count_private=true"/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Kushal9889&layout=compact&hide_border=true&bg_color=0d1117&title_color=58A6FF&text_color=c9d1d9&langs_count=7&hide=jupyter%20notebook"/>
<br/>
<img width="62%" src="https://streak-stats.demolab.com/?user=Kushal9889&theme=dark&hide_border=true&background=0d1117&ring=58A6FF&fire=58A6FF&currStreakLabel=58A6FF"/>
</div>

---

## A few other things worth knowing

- 📄 **IEEE-published** at ICAICCIT 2024 — [deep learning for automated bug detection](https://github.com/Kushal9889/Deep-Learning-for-Contextual-Bug-Detection-and-Automated-Fixes-in-Software-Systems)
- 📄 **IGI Global co-author** — [cyber-physical systems security](https://github.com/Kushal9889/Cyber-Physical-Systems-and-the-Future-of-Urban-Living-Decision-Making-Challenges-and-Opportunities)
- 🎓 **BU MSCS, GPA 3.6** — graduating December 2026, coursework in Generative AI, AI Systems, Web Mining
- 🏅 **[JEE Mains 99.1 percentile](https://drive.google.com/file/d/1XbK1T7RZahWRamhUVBGbnRBu_8fGOR47/view)** — top 0.08% of 1.2 million students
- 📜 **[AWS Cloud Technical Essentials](https://www.coursera.org/account/accomplishments/verify/4L1ZWS6VK2L8)** verified · **NVIDIA Agentic AI Pro** · **IBM RAG & Agentic AI** (~75%, building projects)

---

<div align="center">

*If you're building agentic networks where agents coordinate peer-to-peer — research, critique, evaluate, loop — and actually need coherent shared memory across all of them, that's what I am working on in my space.*

<br/>
<a href="https://linkedin.com/in/kushal-gaddamwar"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>&nbsp;
<a href="mailto:kushal7887pd@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>&nbsp;
<a href="https://bulife-ai.netlify.app"><img src="https://img.shields.io/badge/Live_Demo-00C7B7?style=for-the-badge&logo=netlify&logoColor=white"/></a>
<br/><br/>
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:1a3a4a,50:0f2027,100:0d1117&height=100&section=footer"/>

</div>
