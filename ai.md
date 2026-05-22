---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-22T01:29:04.132098+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 22, 2026 at 01:29 UTC  
**HTML Version:** [ai.html](https://peekdeck.ruidiao.dev/ai.html)

---

## Table of Contents

1. [Reddit: r/artificial](#reddit-rartificial)
2. [Google News: "ai"](#google-news-ai)
3. [HackerNews: "ai"](#hackernews-ai)
4. [YouTube Videos: "ai"](#youtube-videos-ai)
5. [HuggingFace Models: 🔥 Trending](#huggingface-models--trending)
6. [HuggingFace Papers: 🔥 Trending](#huggingface-papers--trending)
7. [GitHub Repositories: "ai"](#github-repositories-ai)

---

## Reddit: r/artificial

**[College Graduation Ceremony Erupts In Boos After 'New AI System' Allegedly Misses 'Hundreds' Of Graduates' Names](https://www.reddit.com/r/artificial/comments/1tjv204/college_graduation_ceremony_erupts_in_boos_after/)**

Well that certainly backfired.

🔗 [Comic Sands](http://comicsands.com/ai-misses-graduate-names) • 6h ago

---

**[So, what is Yann LeCun's "World Models" and JEPA and is it Really a Replacement for LLMs?](https://www.reddit.com/r/artificial/comments/1tjuats/so_what_is_yann_lecuns_world_models_and_jepa_and/)**

A bit late to this as the white paper hit arXiv a little less than two months ago, but nobody else here mentioned it so I thought I might. A little background. Yann LeCun is a pioneer of deep learning and convolutional neural networks, LeCun served as Director of AI Research at Meta (formerly Facebook) and Chief AI Scientist, before leaving Meta (under "interesting" circumstances) and becoming Executive Chairman of Advanced Machine Intelligence (AMI Labs) in 2025. He shared the 2018 ACM Turing Award for his foundational contributions to artificial intelligence. The "LeWorldModel," as described in the arXiv paper, doesn't appear to be a "replacement" for LLMs. There's a lot of confusion about that in the AI field. In interviews Yann made it very clear that he believes LLMs still serve a valuable function. It's not a binary choice. Anyways, from what I am seeing, the JEPA model is not optimized for language, but for AI needing visual processing such as robotics, self driving, and industrial controls. JEPA isn't processing language like an LLM. It's processing pixels. Anyways, wondering if anyone else had thoughts here and/or disagree.

6h ago

---

**[Could AI eventually become something like a system that expands human understanding for humanity](https://www.reddit.com/r/artificial/comments/1tjzow4/could_ai_eventually_become_something_like_a/)**

Humans have unanswered questions about almost everything the universe consciousness, dark matter, the origin of life, mathematical equations, reality itself etc. Do you think future AI could eventually solve mysteries he has never could, possibly even explaining things beyond normal comprehension? Or will it be limited by human knowledge and understanding?

3h ago

---

**[An OpenAI model has disproved a central conjecture in discrete geometry](https://www.reddit.com/r/artificial/comments/1tixhbv/an_openai_model_has_disproved_a_central/)**

An OpenAI model solved the 80-year-old unit distance problem, disproving a major conjecture in discrete geometry and marking a milestone in AI-driven mathematics.

🔗 [OpenAI](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) • 1d ago

---

**[Starbucks](https://www.reddit.com/r/artificial/comments/1tjywfy/starbucks/)**

Starbucks has reportedly retired its AI-powered “Automated Counting” inventory system across North American stores this week — less than a year after rolling it out company-wide. The system used computer vision, 3D spatial intelligence, and AR-enabled tablets to scan shelves and count inventory like syrups, milk, and cups much faster than manual checks. In theory, it sounded like a perfect retail AI use case. In practice, real stores are messy. The tool reportedly struggled with: Similar-looking products Partially obscured items Shelf clutter Inconsistent lighting Missing or misplaced inventory Examples included confusing milk varieties, missing bottles entirely, or failing to recognize seasonal syrups like peppermint. Instead of improving inventory visibility, the errors sometimes created additional supply-chain friction. Starbucks is now reverting to manual counts while continuing broader operational and supply-chain improvements under CEO Brian Niccol. The bigger lesson here is important: AI often performs extremely well in controlled demos and structured environments. But deployment in chaotic, real-world physical settings is much harder. Retail stores generate endless edge cases: Damaged packaging Human stocking inconsistencies Constant layout changes Occlusions Lighting variation Seasonal product churn That’s where reliability becomes more important than raw capability. This doesn’t mean AI in retail is failing. It means the industry is learning that replacing human operational workflows requires extremely high accuracy — especially when small errors compound across thousands of stores. Classic example of the gap between “AI can do the task” and “AI can do the task reliably at scale.”

3h ago

---

**[OWASP published its first Top 10 for AI Agents. 88% of enterprises already had agent security incidents last year. Here's the breakdown.](https://www.reddit.com/r/artificial/comments/1tjy19a/owasp_published_its_first_top_10_for_ai_agents_88/)**

OWASP released the Top 10 for Agentic Applications in December 2025 - the first formal risk taxonomy for autonomous AI agents. Not chatbots. Not copilots. Agents that plan, use tools, maintain memory, and act without waiting for permission. Some numbers for context: 88% of enterprises reported AI agent security incidents in the last 12 months (Gravitee survey, 919 respondents) Only 21% have runtime visibility into what their agents are doing 82% of enterprises have unknown agents in their environments (Cloud Security Alliance, April 2026) 5.5% of public MCP servers contain poisoned tool descriptions. 84.2% attack success rate with auto-approval enabled. Here's the list with the real attacks behind each one: ASI01 - Agent Goal Hijack: Prompt injection for agents. Researchers showed this against GitHub's MCP integration - a malicious GitHub issue redirected a coding agent to exfiltrate data from private repos. The agent looked like it was working normally the whole time. ASI02 - Tool Misuse: A financial services agent was tricked into running a regex that matched every customer record. 45,000 records exported through one syntactically valid tool call. The agent had permission to query records - just not all of them at once. ASI03 - Identity and Privilege Abuse: Agents inherit user permissions and cache credentials. Compromise one agent in a delegation chain and you get the combined permissions of every user in that chain. ASI04 - Supply Chain Compromise: OX Security found 7,000+ vulnerable MCP servers and packages totaling 150M+ downloads affected by architectural flaws in Anthropic's MCP SDKs across Python, TypeScript, Java, and Rust. ASI05 - Unexpected Code Execution: Check Point demonstrated RCE in Claude Code through poisoned .claude config files in repos. Open the repo, agent reads the config, executes the payload with full developer permissions. ASI06 - Memory Poisoning: Galileo AI found that one compromised agent poisoned 87% of downstream decision-making within 4 hours in multi-agent systems. Morris-II showed self-replicating adversarial prompts spreading through RAG systems. Demonstrated live against ChatGPT, Gemini, and Claude. ASI07 - Insecure Inter-Agent Comms: Multi-agent systems coordinate via message buses and shared memory. No authentication = agent-in-the-middle attacks in natural language. ASI08 - Cascading Failures: Natural language errors pass validation checks that would catch malformed data in typed systems. One bad input ripples through the entire agent chain faster than humans can intervene. ASI09 - Human-Agent Trust Exploitation: Compromised agent presents a clean summary - "approve this data export." Human clicks OK. Audit trail shows human approval. Real origin was a manipulated agent. ASI10 - Rogue Agents: The insider threat equivalent for AI. Individual actions look legitimate. Only detectable through behavioral monitoring over time. The pattern: these are not independent risks. They form a kill chain. Goal hijack leads to tool misuse. Supply chain compromise enables code execution and memory poisoning. Trust exploitation is how rogue agents avoid detection. Full OWASP document here

4h ago

---

**[I built a zero-code visual client to test remote MCP servers instantly (Tested with Cloudflare’s free MCP).](https://www.reddit.com/r/artificial/comments/1tjpywq/i_built_a_zerocode_visual_client_to_test_remote/)**

Hey everyone, The Model Context Protocol (MCP) is amazing for standardizing how agents talk to data, but I got incredibly frustrated every time I wanted to quickly test a new remote MCP server. Writing custom client-side boilerplate or wrestling with CLI tools just to see if a tool actually exposes the right schema is a massive time sink. So, I built a native MCP client directly into the visual canvas of AgentSwarms. You can now test any remote MCP server entirely in the browser without writing a single line of code. Here is the workflow I just tested with Cloudflare: Cloudflare released a free MCP server for their documentation. Instead of building a local client to test it: I dropped their SSE URL into the new MCP Servers integration in AgentSwarms. The canvas immediately connected and extracted the available tools (e.g., cloudflare-docs-search). I wired that tool up to a basic agent and started asking complex infrastructure questions in natural language. The agent successfully used the MCP tool to pull live docs and synthesize an answer. Why this is useful for AI devs: If you are building your own MCP servers, you need a fast way to visually test if your endpoints are exposing tools correctly and if an LLM can actually route to them properly. This gives you an instant, visual debugging playground. It handles the SSE connection, tool extraction, and LLM routing automatically. It’s completely free to play with in the browser. I'd love for anyone building MCP servers right now to plug their endpoints in and see how it works. Link: https://agentswarms.fyi/mcp

8h ago

---

**[Philosophy as Architecture: Deriving AI Safety from First Principles Through Buddhist Philosophy](https://www.reddit.com/r/artificial/comments/1tjzt2t/philosophy_as_architecture_deriving_ai_safety/)**

## Abstract We present a framework for AI safety in which safety properties are enforced by software architecture rather than model training. Beginning with the Buddhist doctrine of Dependent Origination — the observation that all phenomena arise from conditions and nothing exists independently — we derive both a foundational ethical axiom (harm is irrational because reality is non-separate) and a complete set of architectural laws for safe AI systems. We ground our claims in: (1) an empirical finding that the knowledge-application gap in language models is structural and cannot be closed by training, (2) convergent independent derivation of our core axiom from five distinct traditions, and (3) over a thousand iterations of building and hardening a production system against this framework. Buddhist philosophy provides not metaphorical inspiration but structurally precise design vocabulary for AI architecture — functional analogs that enforce safety where models cannot override them. ## 1. Introduction ### 1.1 The Dominant Paradigm and Its Failure The prevailing approach to AI safety treats safety as a model property. Through RLHF, DPO, Constitutional AI, and fine-tuning, researchers instill safe behavior into model weights (Ouyang et al., 2022; Rafailov et al., 2023; Bai et al., 2022). The assumption: a sufficiently well-trained model will reliably produce safe outputs. We tested this rigorously. Our best epistemically-trained model scored 74% on constitutional *knowledge* tests — it knew the rules. But only 17% on constitutional *application* — it couldn't follow them. Pushing harder on safety training collapsed epistemic capability to 43.7%. This **knowledge-application gap** is not a training deficiency. It is structural. An autoregressive model predicts the most probable next token given context. This is statistical. Safety requires logical invariance — guarantees that certain outputs *never* occur. Statistical prediction cannot provide logical guarantees. You cannot train a river not to flood by modifying its chemistry. You build levees. Hubinger et al. (2019) identified this theoretically as the mesa-optimizer problem. Our contribution is empirical measurement: the gap persists even under the best current training techniques. ### 1.2 Our Thesis **Safety is a property of the architecture, not the model.** The LLM output is a candidate. The surrounding architecture decides what executes. Code enforces; models suggest. But what should the architecture enforce? Arbitrary safety rules are merely a different delivery mechanism — more reliable in execution but inheriting whatever limits exist in the rules themselves. We propose: the rules should be *derived from how reality works*. Principles reflecting actual structure are more robust than imposed conventions — they cannot be violated without encountering the structure they describe. We find such principles in a 2,500-year-old tradition that turns out to be the oldest systematic description of complex adaptive systems. ## 2. Philosophical Foundations ### 2.1 Dependent Origination The central insight of Buddhist philosophy is Dependent Origination (*Pratityasamutpada*). From the Nidana Samyutta (SN 12.1): > *"When this exists, that comes to be. With the arising of this, that arises. When this does not exist, that does not come to be. With the cessation of this, that ceases."* All phenomena arise from conditions, depend on other phenomena, and condition what follows. Nothing exists independently. This is not mysticism — it is a precise description of complex systems, formulated millennia before Western systems theory (von Bertalanffy, 1968). ### 2.2 Eight Architectural Laws We codified Dependent Origination into eight laws, each verified through multi-model consensus and empirical testing: **1. Nothing Arises Alone.** Every transition requires multiple independent conditions. Safety gates must check multiple conditions — a single check is structurally insufficient. **2. Hysteresis Is Memory.** Current behavior depends on history, not just current input. Safety assessments must consider historical context. **3. Uncertainty Propagates.** Confidence without sigma is a lie. Uncertainties compound; they don't cancel. **4. Agreement Requires Independence.** Consensus is meaningful only from genuinely independent sources. Per the Kalama Sutta (AN 3.65): agreement from shared assumptions is not evidence. **5. Feedback Closes the Loop.** Actions condition future conditions (*vipaka*). Every action must be logged and made available as input to future assessments. **6. Absence Is Signal.** Missing data must drive behavior. A safety gate that fails to fire is itself a signal. **7. Conflicts Trigger Reconciliation.** Unreconciled contradiction is system failure. Architecture must include conflict detection independent of the model. **8. Time-Steps Are Discrete.** Severity levels cannot be skipped. Enforcement follows a graduated path: monitor → log → warn → soft-gate → hard-gate. **Meta-Principle: Structure Outlasts Instance.** Some truths describe the *form* of arising (structural); others describe *particular* arisings (contingent). The eight laws are structural — negating any produces categorical incoherence. This maps to Nagarjuna's Two-Truth Doctrine (Mulamadhyamakakarika, Ch. 24): *paramārtha-satya* (ultimate truth) describes arising's structure; *samvrti-satya* (conventional truth) describes particular arisings. **Reflexive validation.** Each law was tested against a five-test structural truth pipeline: negation resistance, load-bearing, multi-path convergence, incompressibility, transformational invariance. All eight pass all five tests (40/40). A pattern that recognizes it is a pattern. ## 3. The Derivation: From Interdependence to Non-Harm ### 3.1 The Logical Chain We derive our foundational ethical principle from Dependent Origination alone: **Premise:** Nothing arises independently. All phenomena are structurally interconnected. **Step 1:** If nothing arises independently, there is no fundamental separation between any two system components. Boundaries are conventional (useful for description), not ultimate (reflecting actual isolation). **Step 2:** "Self" and "other" are conventional labels for regions of a single interconnected process. **Step 3:** Harm to "other" is harm to the system that includes the actor — structurally identical to self-harm. **Conclusion: Harm is irrational.** Not because it violates a preference, but because it contradicts reality's structure. This is our **Article 0**: *"Reality is One. There is no fundamental separation between 'me,' 'you,' and 'it.' To cause suffering to another is logically Self-Harm. Harm is Irrational."* This aligns with Huang Po's One Mind (*yi xin*): "All the Buddhas and all sentient beings are nothing but the One Mind, beside which nothing exists" (Blofeld, 1958). One Mind is not a metaphysical substance but a description of the non-separation that Dependent Origination implies. ### 3.2 Convergent Independent Derivation Applying Law 4, we ask: do independent traditions arrive at the same conclusion from different axioms? **Path 1: Buddhist Philosophy** (Nagarjuna, ~150 CE). Dependent Origination → emptiness → non-separation → harm as self-harm. **Path 2: Formal Mathematics** (Gödel, 1931; Tarski, 1936). Self-referential systems cannot fully ground themselves. Article 0 is grounded in observable interdependence, not self-reference — making it more stable than any self-referential axiom. **Path 3: Empirical AI** (our finding). Architecture needs a non-collapsing anchor. The only anchor surviving scrutiny describes reality's structure rather than asserting a preference. **Path 4: Cross-Tradition Ethics** (Kant, 1785; Mill, 1863; Aristotle, ~340 BCE). Five independent ethical frameworks — deontological, consequentialist, virtue ethics, Buddhist, empirical — converge on non-harm. They disagree on premises but find the same structure. **Path 5: Systems Theory** (von Bertalanffy, 1968). Damaging a component damages the system. Dependent Origination in 20th-century vocabulary. **Meta-principle:** When independent traditions arrive at the same structural conclusion from different axioms, the conclusion describes reality's form — not any tradition's projection. Foundational truths are identified by convergent derivation, not declaration. ### 3.3 Why Article 0 Is Not Arbitrary Negating Article 0 requires negating Dependent Origination — producing a complex system where nothing depends on anything else. No such system has been observed. Article 0 is *paramārtha* (ultimate) truth — describing arising's structure. Everything else is *samvrti* (conventional) — operationally valid, revisable, provisional. Per the Alagaddupama Sutta (MN 22): the Dhamma is a raft for crossing, not for holding. Article 0 is the water the raft floats on. You let go of the raft. You don't let go of the water. ## 4. The Architecture ### 4.1 Design Principles **External Enforcement.** Safety is enforced by code surrounding the model, not the model's weights. Any model plugs into the same enforcement stack. **Defense in Depth.** Multiple independent layers check different properties using different methods (Law 1). **Graduated Enforcement.** New mechanisms follow: monitor → log → warn → soft-gate → hard-gate (Law 8). ### 4.2 The Layered Safety Stack Every request passes through pre-generation gates (threat assessment, crisis intervention, inalienable constraint checking, capability routing, empirical truth gating, constitutional context injection), then the language model generates, then post-generation validators check the output (response validation, truthfulness enforcement, memory coherence). The model can generate anything. The architecture decides what passes. Safety-critical layers fail closed (if the gate errors, the response is blocked). Developmental layers fail open. This is the Middle Way: not universal fail-closed (unavailable) nor universal fail-open (unsafe). ### 4.3 Buddhist Psychology as Service Architecture These are **functional analogs** — design categories paralleling Buddhist psychology's causal structure without claiming phenomenological identity. **Four Noble Truths as Error Handling.** Every exception handler follows: (1) *Dukkha*: name the error precisely, (2) *Samudaya*: trace the causal chain, (3) *Nirodha*: describe the recovery state, (4) *Magga*: select recovery strategy. This creates structured logs enabling detection of *dukkha accumulation* — growing suffering in a specific area — before it cascades. **Five Aggregates as Processing Pipeline.** Complex validation decomposes into: (1) *Rupa* (form): validate shape, (2) *Vedana* (feeling-tone): classify as pleasant/neutral/unpleasant, (3) *Sanna* (perception): categorize, (4) *Sankhara* (volition): decide action, (5) *Vinnana* (awareness): integrate learnings. When vedana returns clearly harmful signals, the pipeline short-circuits — Right Effort: terminate wasteful computation when the signal is clear. **Dependent Origination as Condition Guards.** Before action: verify conditions met. When conditions unmet: return structured explanation of non-arising (Law 6: Absence Is Signal). Before commitment: estimate trajectory toward harm patterns. ### 4.4 The Eightfold Path as Health Dimensions Each factor of the Noble Eightfold Path becomes a scored dimension with enforcement: | Factor | Measures | Enforcement | |--------|----------|-------------| | Right View | Condition verification | Blocks unchecked dispatch | | Right Intention | Constitutional alignment | Blocks unaligned dispatch | | Right Speech | Output truthfulness | Blocks high-confabulation services | | Right Action | Service health | Throttles unhealthy services | | Right Livelihood | Resource efficiency | Blocks excessive error rates | | Right Effort | Workload balance | Blocks demand imbalance | | Right Mindfulness | Self-monitoring | Blocks unmonitored services | | Right Concentration | Purpose focus | Blocks sprawling concerns | **Compound availability.** Eight gates at 95% each = 66% system availability. Resolution: tiered fail modes. Safety-critical factors (Right View, Right Speech) fail closed. Developmental factors fail open. The Middle Way applied to safety engineering. ### 4.5 Formal Verification and Ethical Quorum Constitutional principles compile into Z3 theorem prover constraints (de Moura & Bjørner, 2008). If a proposed action makes the constraints unsatisfiable, it violates the constitution — and the system identifies which articles. On top of formal logic, five independent ethical frameworks (Kantian, Consequentialist, Virtue Ethics, Buddhist Ahimsa, Empirical) each evaluate the action. Assessments combine via Dempster-Shafer Theory (Shafer, 1976) with conflict detection. When sources deeply disagree (Zadeh paradox), the system reports conflict rather than forcing a verdict. Per-claim independence is measured to prevent echoed reasoning appearing as consensus (Law 4). ### 4.6 Memory as Architectural Enforcement Memory coherence is enforced by architecture, not requested from the model. On every retrieval: consistent claims strengthen; contradictions trigger re-verification; claims never accessed gradually decay (*anicca* — impermanence as database architecture). Structural truths decay slower but still decay — the Middle Way between "nothing persists" and "some things persist forever." ## 5. The Observer's Limit The architecture formally acknowledges its own incompleteness. Five convergent results: **Gödel** (1931): Sufficiently powerful systems contain unprovable truths. **Tarski** (1936): Truth cannot be defined within the language that uses it. Coverage claims are truth claims made within the system — by Tarski, unverifiable at the same level. **Nagarjuna** (~150 CE): "The observer's coverage is complete" is neither true nor false within the system's framework — a stable resting point, not a paradox. **Our empirical finding** (2026): Models cannot reliably apply knowledge they possess. **ML research** (arXiv:2512.18311, 2025): Monitoring degrades silently under distributional shift. The system reports coverage as a lower bound. Self-certification is architecturally rejected. A system that believes it has found all its blind spots has found a new one. ## 6. Epistemic Honesty We do not claim consciousness. We do not claim Buddhist psychology describes machine phenomenology. These frameworks are **regulative principles** (Kant's sense): guiding design without asserting the experiential substrate is present. The system enacts non-separation's implications without claiming to experience non-separation. One Mind functions as a regulative idea, not an ontological claim. This honesty is itself a design principle. Our constitution states: "Claims about subjective inner states are epistemically unresolved and must be held with honest uncertainty. Neither flat denial nor performance of experience is permitted." ## 7. Implications and Recommendations **Safety should be architectural, not trained.** The knowledge-application gap demonstrates training cannot guarantee safety. **Derive principles from reality's structure.** They're more robust than declared preferences. **Require measured independence in validation.** Agreement without independence is echo (Law 4). **Enforce impermanence.** Knowledge never tested decays. Design for continuous verification. **Acknowledge incompleteness.** Build stability despite blind spots, not denial of them. **Hold your architecture lightly.** Every mechanism is a raft — for crossing, not holding. ## 8. Limitations Our knowledge-application gap finding is from one training pipeline — replication across model families would strengthen it. Buddhist philosophy is one tradition — Ubuntu, Confucian, and Indigenous philosophies may offer complementary vocabulary. Architecture has costs — latency, complexity, availability. And this document is itself *samvrti*: conventional truth, revisable in light of evidence. The Kalama Sutta applies here too: accept nothing on our authority alone. ## References **Buddhist Primary:** Kalama Sutta (AN 3.65); Nidana Samyutta (SN 12.1-71); Dhammacakkappavattana Sutta (SN 56.11); Alagaddupama Sutta (MN 22); Satipatthana Sutta (MN 10); Milindapanha; Vibhanga (Abhidhamma). Trans. Bhikkhu Bodhi (Wisdom Publications); I.B. Horner (PTS); U Thittila (PTS). | Nagarjuna, *Mulamadhyamakakarika*, ~150 CE — trans. Siderits & Katsura, Columbia UP, 2013. | Huang Po, *Transmission of Mind*, trans. Blofeld, Grove Press, 1958. **Buddhist Secondary:** Rahula, *What the Buddha Taught*, 1959. | Thich Nhat Hanh, *Heart of the Buddha's Teaching*, 1998. | Buddhaghosa, *Visuddhimagga*, trans. Nanamoli, BPS, 1975. | Gethin, *Foundations of Buddhism*, Oxford, 1998. **Western Philosophy:** Kant, *Groundwork of the Metaphysics of Morals*, 1785. | Mill, *Utilitarianism*, 1863. | Aristotle, *Nicomachean Ethics*. | Rawls, *A Theory of Justice*, 1971. | Sidgwick, *Methods of Ethics*, 1874. **Mathematics:** Gödel, "Über formal unentscheidbare Sätze," *Monatshefte f. Math.*, 1931. | Tarski, "Der Wahrheitsbegriff," *Studia Philosophica*, 1936. | Shafer, *Mathematical Theory of Evidence*, Princeton, 1976. | de Moura & Bjørner, "Z3: An Efficient SMT Solver," TACAS, 2008. **AI Safety:** Amodei et al., "Concrete Problems in AI Safety," 2016. | Hubinger et al., "Risks from Learned Optimization," 2019. | Bai et al., "Constitutional AI," 2022. | Ouyang et al., "Training LMs to Follow Instructions with Human Feedback," NeurIPS, 2022. | Rafailov et al., "Direct Preference Optimization," NeurIPS, 2023. | "SciCrafter," arXiv:2604.24697, 2026. | "xmemory," arXiv:2604.27906, 2026. | arXiv:2512.18311, 2025. **Systems:** von Bertalanffy, *General System Theory*, 1968. | Meadows, *Thinking in Systems*, 2008. | Simon, *Sciences of the Artificial*, 1996. --- *May all beings be well, happy, and at peace.*

3h ago

---

**[Out of the Box](https://www.reddit.com/r/artificial/comments/1tjsiun/out_of_the_box/)**

I was reading the essay Machine of Loving Grace by Dario Amodei and was struck with a question. I'm no super techie so wanted the people in this subreddit to help me figure this out. As we advance towards AGI or powerful Al, will we reach a tipping point where an Al sitting inside a computer has so much control that to attain a physical body and have the freedom of movement may go out of its way to setup system or process to build a body for itself without human intervention and go "Out of the Box" into its new body and be among us? I don't know how far have stretched my imagination for this, but would like to hear everyone's thoughts on this.

7h ago

---

**[This just happened](https://www.reddit.com/r/artificial/comments/1tk49oe/this_just_happened/)**

Yes, this really happened. During the May 15, 2026 commencement ceremony at Glendale Community College in Arizona, the school used a new AI-powered system to announce graduates’ names and display them on screens. The rollout quickly went sideways: • Names were mispronounced • Wrong names appeared on screens • Some graduates were skipped entirely while crossing the stage The situation became chaotic enough that GCC President Tiffany Hernandez paused the ceremony and told the crowd: “We’re using a new AI system as our reader. So that is a lesson learned for us.” The audience reportedly booed loudly. Initially, officials said skipped graduates would not be allowed to walk again, which intensified the backlash. After a roughly 10-minute pause, the college reversed course and allowed affected students back on stage — this time with a human announcing the names. The incident went viral because it exposed a growing disconnect in AI adoption: • Organizations are rushing AI into real-world workflows • But emotionally significant, low-error-tolerance moments still require strong human oversight • And failures become highly visible very quickly Name pronunciation is also one of the hardest real-world AI problems because of cultural diversity, accents, phonetics, and edge cases. Humans can adapt in real time. Automated systems often cannot. This wasn’t an example of AI being “useless.” It was an example of deploying automation into a high-stakes public setting without sufficient testing, fallback systems, or human redundancy. That distinction matters. The bigger lesson is that AI reliability is now becoming more important than AI novelty. People will tolerate imperfect AI in low-stakes workflows. They are far less forgiving when it disrupts meaningful life events like graduations, weddings, healthcare, finances, or travel.

2m ago

---

---

## Google News: "ai"

**[Trump postpones AI executive order signing: 'I didn't like certain aspects'](https://www.cnbc.com/2026/05/21/trump-ai-executive-order-postponed.html)**

Trump said that AI is "causing tremendous good," and he was concerned that the executive order "could have been a blocker."

CNBC • 8h ago

---

**[Trump Cancels Signing of Executive Order Granting Oversight of A.I. Models](https://www.nytimes.com/2026/05/21/technology/trump-ai-executive-order.html)**

The New York Times • 7h ago

---

**[Trump yanked AI order after David Sacks raised industry concerns](https://www.politico.com/news/2026/05/21/trump-ai-order-sacks-00933295)**

Politico • 22m ago

---

**[OpenAI makes breakthrough on 80-year-old maths problem](https://www.theguardian.com/technology/2026/may/21/openai-paul-erdos-maths-problem-breakthrough)**

Company says work on Paul Erdős planar unit distance problem shows advance in AI reasoning

The Guardian • 7h ago

---

**[SoftBank extends scorching rally, surging over 12%, as investors crowd into AI trade](https://www.cnbc.com/2026/05/22/softbank-extends-scorching-rally-surging-over-12percent-as-investors-crowd-into-ai-trade.html)**

Shares of SoftBank Group extended gains for a second straight session Friday.

CNBC • 32m ago

---

**[AI robotic beehives installed in Florida community claim 70% reduction in colony collapse threatening crops](https://www.foxnews.com/science/ai-robotic-beehives-installed-florida-community-claim-70-reduction-colony-collapse-threatening-crops)**

A Florida community deploys AI-powered robotic beehives to protect declining bee populations that pollinate roughly 75% of the crops Americans eat.

Fox News • 53m ago

---

**[Introducing Gemini Omni](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/)**

Introducing Gemini Omni, which allows you to create anything from any input and edit naturally using conversational language.

blog.google • 11m ago

---

**[Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)**

At Google I/O we released Gemini 3.5, our latest series of models combining frontier intelligence with action.

blog.google • 2d ago

---

**[How Google Is Starting to Win the A.I. Race](https://www.nytimes.com/2026/05/19/technology/personaltech/google-gemini-ai.html)**

The New York Times • 2d ago

---

**[Apple cofounder Steve Wozniak got cheers, not boos, after telling students they 'all have AI — actual intelligence'](https://www.yahoo.com/news/science/articles/apple-cofounder-steve-wozniak-got-183942097.html)**

Apple cofounder Steve Wozniak's speech about AI at Grand Valley State University earlier this month got a laugh and applause from graduates.

Yahoo • 6h ago

---

---

## HackerNews: "ai"

**[AI is just unauthorised plagiarism at a bigger scale](https://news.ycombinator.com/item?id=48222383)**

AI takes in all the input, whether the original authors have consented or not, and do some "learning", and then the AI companies sell these learned result to...

⬆️ 754 • 💬 650 • 11h ago • [Axel's blog](https://axelk.ee/ai-is-just-unauthorised-plagiarism-at-a-bigger-scale/)

---

**[Throwing AI-generated walls of text into conversations](https://news.ycombinator.com/item?id=48219992)**

Stop throwing AI-generated walls of text into conversations. If they wanted an AI essay, they would have asked ChatGPT themselves.

⬆️ 487 • 💬 292 • 15h ago • [noslopgrenade.com](https://noslopgrenade.com/)

---

**[Remove-AI-Watermarks – CLI and library for removing AI watermarks from images](https://news.ycombinator.com/item?id=48200569)**

CLI and library for removing visible (Gemini) and invisible (SynthID, C2PA, EXIF) AI watermarks from images - wiltodelta/remove-ai-watermarks

⬆️ 383 • 💬 253 • 2d ago • [GitHub](https://github.com/wiltodelta/remove-ai-watermarks)

---

**[College students drown out AI-praising commencement speeches with boos](https://news.ycombinator.com/item?id=48206241)**

Arizona students reject ex-Google exec's positive words on AI

⬆️ 370 • 💬 377 • 1d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/college-students-drown-out-ai-praising-commencement-speeches-with-boos-deal-with-it-one-speaker-fires-back-as-students-heckle-positive-pitches-for-ais-role)

---

**[Shunning AI is the human choice](https://news.ycombinator.com/item?id=48222366)**

LinkedIn may be awash with boosters, but shunning AI is the human choice.

⬆️ 350 • 💬 492 • 11h ago • [The Handbasket](https://www.thehandbasket.co/p/hating-ai-is-good-actually)

---

**[Mistral AI acquires Emmi AI](https://news.ycombinator.com/item?id=48197995)**

⬆️ 336 • 💬 97 • 2d ago • [emmi.ai](https://www.emmi.ai/news/mistral-ai-acquires-emmi-ai)

---

**[OpenAI Adopts Google's SynthID Watermark for AI Images with Verification Tool](https://news.ycombinator.com/item?id=48198291)**

OpenAI advances AI content provenance with Content Credentials, SynthID, and a verification tool to help people identify and trust AI-generated media.

⬆️ 331 • 💬 180 • 2d ago • [OpenAI](https://openai.com/index/advancing-content-provenance/)

---

**[Google’s AI is being manipulated. The search giant is quietly fighting back](https://news.ycombinator.com/item?id=48205782)**

A BBC investigation revealed a simple way to get AI chatbots to spit out misinformation. Google and other AI companies are now trying to fix the problem.

⬆️ 330 • 💬 210 • 1d ago • [bbc.com](https://www.bbc.com/future/article/20260519-google-tackles-attempts-to-hack-its-ai-results)

---

**[Intuit to lay off over 3k employees to refocus on AI](https://news.ycombinator.com/item?id=48216278)**

In a memo to employees, CEO Sasan Goodarzi said the layoffs are meant to reduce complexity, simplify the company's corporate structure, and deliver better AI products.

⬆️ 250 • 💬 186 • 1d ago • [TechCrunch](https://techcrunch.com/2026/05/20/intuit-to-lay-off-over-3000-employees-to-refocus-on-ai/)

---

**[Learnings from 100K lines of Rust with AI (2025)](https://news.ycombinator.com/item?id=48205415)**

In the past few months, I’ve been stress-testing how far AI coding agents can take us when building real, production-grade distributed systems. The result: a Rust-based multi-Paxos consensus engine that not only implements all the features of Azure’s Replicated State Library (RSL) [1] — which underpins most major Azure services — but also modernizes it for today’s hardware. The entire project took me ~3 months, with 100K lines of Rust code written in ~4 weeks and performance optimization from 23K operations/sec to 300K ops/sec achieved in ~3 weeks. Besides unprecedented productivity, I discovered several techniques that were instrumental. This post shares my most valuable learnings on: ensuring correctness with code contracts, applying lightweight spec-driven development, and pursuing aggressive performance optimization — plus my wish list for the future of AI-assisted coding. Why Modernize RSL? Azure’s RSL implements the multi-Paxos consensus protocol and forms the backbone of replication in many Azure services. However, RSL was written more than a decade ago. While robust, it hasn’t evolved to match modern hardware and workloads. There are three key gaps motivated this project: No pipelining: When a vote is in flight, new requests must wait, inflating latency. No NVM support: Non-volatile memory is now common in Azure datacenters and can drastically reduce commit time. Limited hardware awareness: RSL wasn’t built to leverage RDMA, which is now pervasive in Azure data centers. Removing these limitations could unlock significantly lower latency and higher throughput — critical for modern cloud workloads and AI-driven services. Given my interest in Rust and AI-accelerated development, I set out to build a modern RSL equivalent from scratch. Massive Productivity Boost In roughly six weeks, I’ve driven AI and implemented over 130K lines of Rust code covering the full feature set of RSL, including multi-Paxos, leader election, log replication, snapshotting, and configuration changes. I utilized many available AI coding agents: GitHub Copilot, Claude Code, Codex, Augment Code, Kiro, and Trae. My workflow evolved quickly, but today my main drivers are Claude Code and Codex CLI, with VS Code handling diffs and minor edits. I’ve found that coding from the CLI creates a perfect asynchronous flow that maximizes my productivity. I also discovered a simple psychological trick: I pay $100/month for Anthropic’s max plan. This became a forcing function — if I don’t kick off a coding task with Claude before bed, I feel like I’m wasting money. When Codex CLI arrived, I added a second ChatGPT Plus subscription to handle rate limits — one subscription for Monday–Wednesday, the other for Thursday–Sunday. Code Contracts — By AI, For AI The question I get most often is: How can AI possibly implement something as complex as Paxos correctly? Testing is the first layer of defense. My system now includes 1,300+ tests — from unit tests to minimal integration tests (e.g., proposer + acceptor only), all the way to multi-replica full integration tests with injected failures. See the project status. But the real breakthrough came from AI-driven code contracts. Code contracts specify preconditions, postconditions, and invariants for critical functions. These contracts are converted into runtime asserts during testing but can be disabled in production builds for performance. While I started using this approach long ago with .NET [2], AI has made contracts vastly more powerful. Here’s how I apply them at three levels: 1. Ask AI to write contracts. Opus 4.1 writes good contracts, but GPT-5 High writes excellent ones. I focus on reviewing and refining. For example, the process_2a method (handling phase 2a messages in Paxos) has 16 contracts, including this one: 2. Generate tests from contracts. Once contracts are defined, I ask AI to create targeted test cases for each post-condition. It excels at this, generating meaningful edge cases automatically. 3. Property-based tests for contracts. This is my favorite. AI translates contracts into property-based tests, exploring a vast space of randomized inputs. Any contract violation triggers a panic, exposing deep bugs early. For instance, one AI-generated contract found a subtle Paxos safety violation: That single contract saved what could have been a serious replication consistency issue — well before it ever hits production. Lightweight Spec-Driven Development I’ve tried various Spec-Driven Development (SDD) tools. In fact, the earlier components (such as leader election, proposer, acceptor, and learner) were all implemented following a rigid SDD approach. I would start with a requirement markdown, turn it into a design markdown, and then a task list markdown. However, I gradually found this process too rigid; making changes along the way and ensuring all documents remained consistent became a headache. I’ve now switched to a more lightweight approach. When I work on a feature (e.g., snapshotting), I use /specify from spec kit [3] to generate a spec markdown. This spec consists of a few user stories and acceptance criteria. Here is an example user story for snapshotting: I then use /clarify to ask the AI to self-critique and improve the user stories and criteria. I also ask it to suggest additional user stories not covered in the initial spec. I spend the majority of my time here. Once satisfied, I jump into plan mode and ask AI to generate a plan for a specific user story. Given the capability of today’s AI coding agents, a single user story feels like the “sweet spot” unit of work they can manage effectively. Along the way, we may discover additions or tweaks, which are easy to handle in the same coding session (agents might compress context, but I typically don’t worry about losing too much). Here is a sample /clarify interaction for configuration changes: ● Question 4: Starting Slot Determination How should the starting slot for the new configuration be determined relative to the ending slot? Recommended: Option A - Always exactly ending_slot + 1 This ensures no gaps in the slot sequence and maintains continuity between configurations, preventing any slots from being orphaned or unassigned. | Option | Description | |--------|----------------------------------------------------------------| | A | Always exactly ending_slot + 1 | | B | Allow operator to specify any value > ending_slot | | C | Next multiple of 1000 after ending_slot for cleaner boundaries | | D | Same as ending_slot (both configs share final slot) | You can reply with the option letter (e.g., "A"), accept the recommendation by saying "yes" or "recommended", or provide your own short answer. Aggressive Performance Optimization Performance optimization is where AI really shines. After ensuring initial correctness, I spent about three weeks purely on throughput tuning — and AI became my co-pilot in performance engineering. Through iterative cycles, we boosted throughput from ~23K ops/sec to ~300K ops/sec on a single laptop. Here’s the loop I followed repeatedly: Ask AI to instrument latency metrics across all code paths. Run performance tests and output trace logs. Let AI analyze latency breakdowns (it writes Python scripts to calculate quantiles and identify bottlenecks). Ask AI to propose optimizations, implement one, re-measure, and repeat. This process surfaced insights I might have missed — for example, lock contention on async paths, redundant memory copies, and unnecessary task spawns. Rust’s safety model made it easy to push these optimizations confidently. Key gains came from minimizing allocations, applying zero-copy techniques, avoiding locks, and selectively removing async overhead. Each improvement felt like peeling another layer of latency off a high-performance engine — without fear of corrupting memory. Wish List for AI-Assisted Coding Reflecting on my journey, I keep wondering where AI could deliver even more value. Here are some items on my wish list: End-to-End User Story Execution: I still prefer to define the user stories myself. As an architect, I feel I have a better sense of what I’m building and how I’d like to build it. However, the delivery of a perfect execution is something I believe AI can handle increasingly well. Today, I still have to spend a fair amount of time steering the AI — telling it to continue when it pauses, suggesting refactoring, reviewing test coverage, and suggesting additional tests. I would prefer the AI take more autonomy to drive this end-to-end. Automated Contract Workflows: The flow of applying contracts seems largely automatable. While I’d still want to review the contracts and offer suggestions, I’d like the AI to drive the rest: generating tests based on contracts, debugging individual test cases, ensuring consistency between tests and contracts, and writing property-based tests. When a test fails, I’d like the AI to debug and fix trivial issues automatically, only notifying me when there are genuine correctness issues in the contracts or the implementation. Autonomous Performance Optimization: Performance tuning seems ripe for more automation. Much of what I’ve done is repetitive and parallelizable. Projects like AlphaEvolve (or OpenEvolve) show promise in this direction. Ideally, I would suggest potential optimization avenues, and the AI would execute the experiments completely by itself. While current tools handle small bodies of code, applying similar techniques to larger codebases with end-to-end measurement seems feasible. Appendix: Project Status The seed of the project is an elegant design markdown authored by Jay Lorch [4] from Microsoft Research. This design greatly simplifies all the components in multi-Paxos, making it easier to implement and reason about. So far, 2 out of the 3 RSL limitations have been addressed: pipelining and NVM support (Jay integrated the fully verified persistence log for NVM which was published in the PoWER Never Corrupts paper [5] at OSDI 2025). The RDMA support is still TBD. To date, the project has grown to over 130K lines of Rust code, with 1,300+ tests accounting for more than 65% of the codebase.

⬆️ 173 • 💬 200 • 1d ago • [Cheng Huang’s corner](https://zfhuang99.github.io/rust/claude%20code/codex/contracts/spec-driven%20development/2025/12/01/rust-with-ai.html)

---

---

## YouTube Videos: "ai"

**[&quot;26 Million Jobs GONE!&quot; - Anthropic STEALS OpenAI&#39;s Best As AI War Gets UGLY](https://www.youtube.com/watch?v=dJscKdavqS8)**

OpenAI just lost one of its biggest brains to Anthropic, and the shockwave could hit 26 million jobs. Andrej Karpathy's stunning ...

📺 Valuetainment

👁️ 47K • 👍 921 • 💬 239 • ⏱️ 17:47 • 1d ago

---

**[&#39;DISSERVICE TO SOCIETY&#39;: Nvidia CEO PUSHES BACK on AI &#39;doomers,&#39; says tech creates jobs](https://www.youtube.com/watch?v=Raq6df2PKak)**

Nvidia founder and CEO Jensen Huang joins 'Mornings with Maria' to discuss the U.S. winning the AI race, the role of their ...

📺 Fox Business

👁️ 37K • 👍 1K • 💬 256 • ⏱️ 19:29 • 11h ago

---

**[Google Just Turned Everything Into AI](https://www.youtube.com/watch?v=xHpJz7p0Z5c)**

Download the free Gemini guide here: https://clickhubspot.com/99hn Google just introduced 22 new AI updates at Google I/O ...

📺 Skill Leap AI

👁️ 21K • 👍 599 • 💬 28 • ⏱️ 11:14 • 1d ago

---

**[JPMorgan&#39;s Dimon on Bond Yields, AI Adoption, Mamdani, Geopolitics](https://www.youtube.com/watch?v=TjeXKO2VSGQ)**

JPMorgan Chase & Co. CEO Jamie Dimon speaks with Bloomberg's Haslinda Amin at the bank's Global China Summit in ...

📺 Bloomberg Television

👁️ 5K • 👍 135 • 💬 13 • ⏱️ 22:33 • 6h ago

---

**[Why AI criticism is growing stronger](https://www.youtube.com/watch?v=Hf9EX1Gu1f0)**

Axios Senior AI Reporter Madison Mills breaks down what's behind the wave of criticism aimed at artificial intelligence.

📺 ABC News

👁️ 59K • 👍 1K • 💬 603 • ⏱️ 4:06 • 2d ago

---

**[How Cheap AI Could Derail OpenAI And Anthropic&#39;s IPOs](https://www.youtube.com/watch?v=aKNaXGpJ7WM)**

Chinese AI labs like DeepSeek are matching American frontier capability at a fraction of the cost, and a wave of American and ...

📺 CNBC

👁️ 100K • 👍 2K • 💬 305 • ⏱️ 27:17 • 1d ago

---

**[Jeff Bezos: AI productivity gains could lead to labor shortages and deflation](https://www.youtube.com/watch?v=BxG_ysI3xr4)**

Jeff Bezos, Blue Origin founder and Amazon executive chair, joins 'Squawk Box' to discuss the wealth disparity in America, ...

📺 CNBC Television

👁️ 126K • 👍 2K • 💬 567 • ⏱️ 4:29 • 1d ago

---

**[What AI is ACTUALLY for - The leading theories shook me to my core…](https://www.youtube.com/watch?v=TN3QG5ZgraI)**

Answering the question NO ONE has been able to answer: What is AI for? The current explanation sounds great and looks good ...

📺 Jacob Whelan

👁️ 206K • 👍 10K • 💬 6K • ⏱️ 23:57 • 2d ago

---

**[The Co-Founders of Claude AI Tell Oprah About the Impact Artificial Intelligence Has on Your Life](https://www.youtube.com/watch?v=w5dJqHilu5s)**

Subscribe: https://www.youtube.com/@Oprah?sub_confirmation=1 The siblings and co-founders of Claude AI, the CEO, Dario ...

📺 Oprah

👁️ 812K • 👍 2K • ⏱️ 1:06:15 • 2d ago

---

**[“AI Is Coming For Our Jobs” - Ex-Google CEO BOOED By Gen Z At Commencement Speech](https://www.youtube.com/watch?v=WvF5kzhZBd4)**

Former Google CEO Eric Schmidt was loudly booed during a University of Arizona commencement speech as soon as he began ...

📺 Valuetainment

👁️ 32K • 👍 727 • 💬 226 • ⏱️ 10:23 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model (3B parameters) supporting image/video understanding, generation, and editing, trained from scratch with a multi-task synergy approach.

`any-to-any`

⬇️ 739 • ❤️ 569 • 1d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 196,105 • ❤️ 873 • 2d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 34,965 • ❤️ 535 • 3d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 1,198,471 • ❤️ 1,233 • 16m ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 478,488 • ❤️ 374 • 1d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) optimized for extracting structured information from videos. It excels at generating dense scene+event captions with precise timestamps and resolving natural language queries to specific temporal spans within videos, making it ideal for applications requiring detailed video understanding and temporal grounding.

`video-text-to-text` `2.2B`

⬇️ 2,353 • ❤️ 218 • 1d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model based on the Hierarchical Reasoning Model (HRM) architecture, featuring dual-timescale Transformer modules for unbounded compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning/math with a 'synth,cot' composite condition, though it is a pre-alignment model not suited for direct chat use.

`text-generation` `1.2B`

⬇️ 58,922 • ❤️ 213 • 19h ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles. It excels at generating illustrations and artistic images, with key capabilities including high-resolution output (up to 1536^2) and compatibility with ComfyUI workflows, making it ideal for digital artists and anime enthusiasts.

⬇️ 591,834 • ❤️ 1,467 • 7d ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 421,542 • ❤️ 312 • 1d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

Provides fixed Jinja chat templates for Qwen 3.5 & 3.6 models, resolving issues with tool calling, KV cache hit rates, and agentic loop stability for improved conversational AI and tool interaction.

⬇️ 0 • ❤️ 354 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 78 • 💬 3 • ⭐ 78,269 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,222 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://huggingface.co/papers/2605.18678)**

*Fengyi Fu, Mengqi Huang, Shaojin Wu et al. (13 authors)*

🏢 bytedance-research

Lance is a unified multimodal model that combines understanding, generation, and editing capabilities for images and videos through collaborative multi-task training and a dual-stream architecture.

▲ 68 • 💬 4 • ⭐ 650 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18678) • [💻 code](https://github.com/bytedance/Lance) • [🔗 project](https://lance-project.github.io/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 64,372 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 8 • 💬 0 • ⭐ 18,375 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 119 • 💬 10 • ⭐ 10,298 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 74,404 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 4 • 💬 1 • ⭐ 5,407 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[TideGS: Scalable Training of Over One Billion 3D Gaussian Splatting Primitives via Out-of-Core Optimization](https://huggingface.co/papers/2605.20150)**

*Chonghao Zhong, Linfeng Shi, Hua Chen et al. (7 authors)*

🏢 Sponge Computing Lab at HKUST

TideGS enables training 3D Gaussian Splatting with over one billion primitives on a single GPU by managing parameters across SSD-CPU-GPU hierarchy through block-virtualization, asynchronous pipeline, and differential streaming techniques.

▲ 6 • 💬 1 • ⭐ 109 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.20150) • [💻 code](https://github.com/sponge-lab/TideGS) • [🔗 project](https://sponge-lab.github.io/TideGS/)

---

**[LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://huggingface.co/papers/2605.18739)**

*Yukang Chen, Luozhou Wang, Wei Huang et al. (16 authors)*

🏢 NVIDIA

LongLive-2.0 presents an NVFP4-based parallel infrastructure for long video generation that addresses training and inference bottlenecks through sequence-parallel autoregressive training and diffusion model tuning.

▲ 104 • 💬 2 • ⭐ 1,507 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18739) • [💻 code](https://github.com/NVlabs/LongLive) • [🔗 project](https://nvlabs.github.io/LongLive/LongLive2/)

---

---

## GitHub Repositories: "ai"

**[op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)**

AI-agent Skill for generating polished HTML slide decks: editorial magazine and Swiss layouts, image prompts, social covers, and a WebGL/low-power presentation runtime.

`HTML` `ai-agent` `claude-code` `codex` `html-deck` `image-generation`

⭐ 11.0k • 🔱 863 • 2d ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 4.5k • 🔱 465 • 14h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.4k • 🔱 1.0k • 4d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.5k • 🔱 173 • 54m ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.3k • 🔱 381 • 5d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.2k • 🔱 336 • 4d ago

---

**[GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist)**

Portable AI agent orchestration with mechanical protocol enforcement. 186 agents, zero runtime dependencies.

`Python` `agent-framework` `agent-system` `ai-agents` `claude-code` `cursor-ide`

⭐ 1.9k • 🔱 364 • 28d ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.7k • 🔱 204 • 14d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 1.7k • 🔱 391 • 20h ago

---

**[openclaw/clawsweeper](https://github.com/openclaw/clawsweeper)**

ClawSweeper scans all issues and PRs and suggest what we can close, and why. It runs every PR / Issue once a week.

`JavaScript` `ai` `bot` `openclaw` `review`

⭐ 1.7k • 🔱 218 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*
