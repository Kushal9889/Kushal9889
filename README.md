<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:0f2027,70:203a43,100:2c5364&height=220&section=header&text=Kushal%20Gaddamwar&fontSize=56&fontColor=ffffff&fontAlignY=36&desc=I%20build%20AI%20systems%20that%20think%2C%20route%2C%20and%20act&descAlignY=58&descSize=18&animation=fadeIn"/>

</div>

<div align="center">

[

<br/>

[
[
[
[

</div>

***

## The Thing I'm Actually Obsessed With

Most people use LLMs as smart autocomplete. I'm interested in the harder question:

> **How do you build a system where multiple AI agents coordinate, remember context, route intelligently, and stay within cost constraints — in production?**

That question led me to build **BU Life AI** — a LangGraph multi-agent system where a supervisor routes natural language queries to specialized ReAct agents (places, resources, events), backed by a hybrid BM25 + vector search RAG pipeline, with SSE streaming, LangSmith tracing, and a singleton retriever pattern that cut LLM API calls by 70%.

It's not a demo. It's deployed. It runs.

***

## What I'm Currently Thinking About

```
├── How context window management changes agent design at scale
├── When to use graph-state (LangGraph) vs linear chains vs raw tool calls
├── The cost/latency tradeoff between dense retrieval and BM25 in hybrid RAG
├── MCP (Model Context Protocol) as the emerging standard for tool-calling infra
└── Why most "agentic" systems aren't actually agentic — just long prompt chains
```

***

## Stack I Actually Use

<div align="center">

**Agent Orchestration**







**Models & Inference**







**RAG & Vector Search**







**Backend & Infra**










</div>

***

## What I've Shipped

### 🤖 [BU Life AI](https://bulife-ai.netlify.app) — Multi-Agent Campus Assistant
*The project where I learned what "production agentic AI" actually means*

Built a LangGraph supervisor that dispatches to three specialized ReAct agents. The hard parts weren't the agents themselves — they were **thread isolation for concurrent sessions**, **singleton retriever initialization** to avoid cold-start overhead, and **hybrid BM25 + 1024-dim vector search** that beats pure semantic retrieval on sparse queries.

Reduced per-query LLM API calls by **70%** via response caching. Streamed tokens end-to-end with SSE. Traced everything with LangSmith. Stack: LangGraph · FastAPI · Next.js · Groq · NVIDIA NIM · PGVector · Neon · Render · Netlify.

***

### 📊 [Sorting Algorithm Visualizer](https://sorting-algorithm-visualizerrr.netlify.app)
*Redux state machine powering async, configurable algorithm visualization*

Redux-driven React app — 6+ algorithms, async execution, 100–1500ms configurable timing, quicksort with 4 pivot strategies, O(n²) vs O(n log n) comparison at a glance.

***

## GitHub Activity

<div align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=Kushal9889&show_icons=true&hide_border=true&theme=github_dark&bg_color=0d1117&title_color=4F98A3&icon_color=4F98A3&text_color=c9d1d9&rank_icon=github&include_all_commits=true"/>
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Kushal9889&layout=compact&hide_border=true&theme=github_dark&bg_color=0d1117&title_color=4F98A3&text_color=c9d1d9&langs_count=6"/>
</div>

<div align="center">
  <img width="68%" src="https://github-readme-streak-stats.herokuapp.com/?user=Kushal9889&theme=github-dark-blue&hide_border=true&background=0d1117&ring=4F98A3&fire=4F98A3&currStreakLabel=4F98A3"/>
</div>

***

## A Few Things Worth Knowing

- 📄 **IEEE-published** at ICAICCIT 2024 on deep learning for automated bug detection
- 📄 **IGI Global co-author** on Cyber-Physical Systems security
- 🎓 **BU MSCS** (GPA 3.6) · graduating December 2026 · coursework in Generative AI, AI Systems, Web Mining
- 🏆 **JEE Mains 99.1 percentile** — top 0.08% of 1.2 million students
- ⚔️ **CodeChef 64th worldwide** — February Long Challenge 2022
- 🧑‍🏫 **Co-founded BITBYTE** at IIIT-DM — mentored 70+ students into Google Kickstart top 200, pre-final internships, and GSoC
- 🎪 Ran a cultural fest that raised ₹10L+ (~$12K) from 25+ sponsors across 13 colleges

***

<div align="center">

*Building systems that think. Open to Agentic AI / Applied AI / SWE roles — F-1 OPT 2026.*

[

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0d1117&height=100&section=footer"/>

</div>
