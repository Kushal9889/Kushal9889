I build multi-agent systems and the retrieval that keeps them honest.

AI Engineer at **Boston University's Questrom Computational Lab**, MSCS candidate, graduating December 2026. First author on an IEEE paper in automated program repair. Available January 2027.

[Portfolio](https://kushal-portfolio-223.netlify.app) · [LinkedIn](https://linkedin.com/in/kushal-gaddamwar) · [ORCID 0009-0009-9318-1616](https://orcid.org/0009-0009-9318-1616) · kushal7887pd@gmail.com

---

### recently

<!--START_ACTIVITY-->
- CompositeBackend.ls("/") and als("/") silently swallow default-backend errors, returning a successful route-only listing in [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)
- null in [Kushal9889/BU-Life-AI](https://github.com/Kushal9889/BU-Life-AI)
- null in [Kushal9889/CF_Ladder](https://github.com/Kushal9889/CF_Ladder)
- null in [Kushal9889/Cyber-Physical-Systems-and-the-Future-of-Urban-Living-Decision-Making-Challenges-and-Opportunities](https://github.com/Kushal9889/Cyber-Physical-Systems-and-the-Future-of-Urban-Living-Decision-Making-Challenges-and-Opportunities)
- null in [Kushal9889/Deep-Learning-for-Contextual-Bug-Detection-and-Automated-Fixes-in-Software-Systems](https://github.com/Kushal9889/Deep-Learning-for-Contextual-Bug-Detection-and-Automated-Fixes-in-Software-Systems)
<!--END_ACTIVITY-->

---

### what I've built

**[BU Life AI](https://bulife-ai.netlify.app)** · [source](https://github.com/Kushal9889/BU-Life-AI)
A campus assistant for Boston University students, live with real traffic. A LangGraph supervisor classifies intent and routes to one of **3 specialised ReAct agents**, each owning its own thread so concurrent users never share state. Retrieval fuses BM25 with **NV-Embed 1024-dimension** vectors over pgvector through an EnsembleRetriever. That routing decision is what cut **redundant LLM calls by 70%**.

The trade-off worth asking about: orchestration complexity bought state isolation. One agent with a long prompt was simpler and mixed tool namespaces across housing, dining, and events until retrieval started contaminating.

**[Contextual bug detection](https://github.com/Kushal9889/Deep-Learning-for-Contextual-Bug-Detection-and-Automated-Fixes-in-Software-Systems)** · IEEE ICAICCIT 2024, first author
A transformer reads tokens and syntax; a graph network reads module dependencies; the two are concatenated and scored together. The combined model reached **91.4% accuracy** against 88.2% for the transformer alone. The graph branch scores lowest on its own at 85.7%, which is the point: structure without content cannot tell a correct function from a broken one.

**Enterprise document intelligence** · Boston University, Questrom Computational Lab
A production agentic RAG platform on Azure for an enterprise consulting client, owned from ingestion through deployment. A LangGraph agent exposing **14 tools** for document question answering, comparison, and template-driven generation. Hybrid retrieval with LLM query rewriting and Cohere re-ranking, LLM-as-a-Judge evaluation for hallucination rate, PII redaction guardrails, and a Cosmos DB Gremlin knowledge graph linking clients, projects, and technologies.

---

### open source

**Reported** [langchain-ai/deepagents#4846](https://github.com/langchain-ai/deepagents/issues/4846): `CompositeBackend.ls("/")` aggregated results at the root and discarded errors from the default backend, so a caller whose backend had failed saw a healthy but nearly empty filesystem. Filed with a reproduction and a proposed fix mirroring the existing `grep` root-merge check. A LangChain maintainer authored and merged the fix in [#4925](https://github.com/langchain-ai/deepagents/pull/4925) three days later, crediting the report by name.

I did not write the patch. `deepagents` restricts merges to organisation contributors. What the report demonstrates is the part that transfers: reading an unfamiliar production SDK closely enough to find where it contradicts its own documented invariant, and writing it up precisely enough that someone senior acted without needing to ask a question.

---

### publications

**Deep Learning for Contextual Bug Detection and Automated Fixes in Software Systems**
ICAICCIT 2024, IEEE, pp. 624–629. First author.
[IEEE Xplore](https://ieeexplore.ieee.org/document/10912101) · [doi:10.1109/ICAICCIT64383.2024.10912101](https://doi.org/10.1109/ICAICCIT64383.2024.10912101) · [repository](https://github.com/Kushal9889/Deep-Learning-for-Contextual-Bug-Detection-and-Automated-Fixes-in-Software-Systems)

**Cyber-Physical Systems and the Future of Urban Living**
IGI Global, 2024. Co-author.
[Repository](https://github.com/Kushal9889/Cyber-Physical-Systems-and-the-Future-of-Urban-Living-Decision-Making-Challenges-and-Opportunities)

Both repositories carry a `CITATION.cff`, so GitHub's **Cite this repository** button returns the correct BibTeX rather than a citation for the code.

---

### where this breaks

Written because a profile that only lists strengths is not worth reading, and because these are the questions an interviewer asks anyway.

**BU Life AI does not survive its own success.** It runs on a Render free tier. The first thing to fail under load is CPU throttling and cold starts, then Neon connection limits. The fix is a paid tier with persistent workers and PgBouncer pooling. I have not needed it and have not pretended otherwise.

**The paper's method needs data most teams do not have.** It depends on a large corpus of code annotated with bugs and their fixes, plus runtime metadata. Where that corpus is thin, accuracy degrades. Generalisation across languages is untested, and the paper says so.

**My first Pydantic schemas at IMG Systems were too strict.** Documents that were merely unusual got rejected alongside genuinely malformed ones. I fixed it with fallback validators and logging on the rejection path, which turned silent data loss into a visible signal. That is the mistake I would tell you about unprompted.

---

### where I have done this

**Boston University, Questrom Computational Lab**, AI Engineer, Graduate Researcher. May 2026 to present.

**IMG Systems**, Software Engineering Intern, Remote. August 2024 to April 2025.
Extended a Python document-parsing pipeline on Apache Tika, raising extraction accuracy **20%** across more than **5,000** candidate profiles a month and cutting recruiter screening time **15%**. Pydantic structured-output validation against a JSON Schema reached **95% schema accuracy**. Containerised services on PostgreSQL and Redis with Docker trimmed REST latency **25%**.

**Growaza**, Associate Software Engineer Intern, India. January to July 2024.
Cut API response time **30%** with in-memory caching and asynchronous request handling, lifting engagement **22%** for more than **1,000** daily active users. MySQL inventory dashboard tracking **2,000+** SKUs. JWT and role-based access control on AWS EC2 and S3.

---

### credentials

[NVIDIA-Certified Professional: Agentic AI](https://www.credly.com/badges/c8f105aa-1815-40cc-85a1-e5a2ef20c920/public_url) is a proctored vendor exam, verifiable on Credly. Plus AWS Cloud Technical Essentials, Google Cloud Fundamentals, and three completed courses of IBM's RAG and Agentic AI programme, each individually verifiable.

---

If you are working on multi-agent coordination or agent evaluation, I would rather compare notes than network.
