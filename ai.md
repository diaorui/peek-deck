---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-14T21:25:47.647285+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 14, 2026 at 21:25 UTC  
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

**[Pentagon's use of Claude during Maduro raid sparks Anthropic feud](https://www.reddit.com/r/artificial/comments/1r4hgnu/pentagons_use_of_claude_during_maduro_raid_sparks/)**

The U.S. military used Anthropic's Claude AI model during the operation to capture Venezuela's Nicolás Maduro, two sources with knowledge of the situation told Axios. "Anthropic asked whether their software was used for the raid to capture Maduro, which caused real concerns across the Department of War indicating that they might not approve if it was," the official said. The Pentagon wants the AI giants to allow them to use their models in any scenario so long as they comply with the law. Axios could not confirm the precise role that Claude played in the operation to capture Maduro. The military has used Claude in the past to analyze satellite imagery or intelligence. The sources said Claude was used during the active operation, not just in preparations for it. Anthropic, which has positioned itself as the safety-first AI leader, is currently negotiating with the Pentagon around its terms of use. The company wants to ensure in particular that its technology is not used for the mass surveillance of Americans or to operate fully autonomous weapons.

🔗 [axios.com](https://www.axios.com/2026/02/13/anthropic-claude-maduro-raid-pentagon) • 10h ago

---

**[Microsoft AI chief gives it 18 months for all white-collar work to be automated by AI](https://www.reddit.com/r/artificial/comments/1r4oc2i/microsoft_ai_chief_gives_it_18_months_for_all/)**

Mustafa Suleyman believes current AI computational power will only accelerate, disrupting every kind of work you do “sitting down at a computer.”

🔗 [Fortune](https://fortune.com/2026/02/13/when-will-ai-kill-white-collar-office-jobs-18-months-microsoft-mustafa-suleyman/) • 5h ago

---

**[I built a "Traffic Light" system for AI Agents so they don't corrupt each other (Open Source)](https://www.reddit.com/r/artificial/comments/1r4tbnj/i_built_a_traffic_light_system_for_ai_agents_so/)**

Hey everyone, I’m a backend developer with a background in fintech. Lately, I’ve been experimenting with multi-agent systems, and one major issue I kept running into was collision. When you have multiple agents (or even one agent doing complex tasks) accessing the same files, APIs, or context, they tend to "step on each other's toes." They overwrite data, execute out of order, or hallucinate permissions they shouldn't have. It’s a mess. I realized what was missing was a Traffic Light. So I built Network-AI. It’s an open-source protocol that acts as a traffic control system for agent orchestration. How it works: Think of it like an intersection. Before an agent can execute a high-stakes tool (like writing to a database, moving a file, or sending a transaction), it hits a "Red Light." The Check: The protocol (specifically a module I call AuthGuardian) checks the agent’s credentials and the current state of the environment. The Green Light: Only if the "road is clear" (permissions are verified and no conflicts exist) does the agent get the green light to proceed. The Camera: Just like a traffic camera, there is an immutable audit trail of every green light given, so you can debug crashes later. Why I’m posting: I’m not selling anything. I just want to solve the problem of agents corrupting shared environments. I’d love for you to check out the repo and tell me if this "Traffic Light" architecture makes sense for your use cases, or if I’m over-engineering it. Repo:https://github.com/jovanSAPFIONEER/Network-AI all feedback is welcome

2h ago

---

**[Only A Few AI Platforms Can Survive](https://www.reddit.com/r/artificial/comments/1r4n1u9/only_a_few_ai_platforms_can_survive/)**

It does not happen very often in the history of business that an orthogonal product is invented that almost immediately doubles the revenue pool of a

🔗 [The Next Platform](https://www.nextplatform.com/2026/02/11/only-a-few-ai-platforms-can-survive/) • 6h ago

---

**[Introducing Open Book Medical AI: Deterministic Knowledge Graph + Compact LLM](https://www.reddit.com/r/artificial/comments/1r3yw21/introducing_open_book_medical_ai_deterministic/)**

Introducing Open Book Medical AI: Deterministic Knowledge Graph + Compact LLM Most medical AI systems today rely heavily on large, opaque language models. They are powerful, but probabilistic, difficult to audit, and expensive to deploy. We’ve taken a different approach. Our medical AI is a hybrid system combining: • A compact ~3GB language model • A deterministic proprietary medical Knowledge Graph (5K nodes, 25K edges) • A structured RAG-based answer audit layer The Knowledge Graph spans 7 core medical categories: Diseases, Symptoms, Treatment Methods, Risk Factors, Diagnostic Tools, Body Parts, and Cellular Structures and, critically, their relationships. Why this architecture matters 1️⃣ Comparable answer quality with dramatically lower compute and reduced hallucination. A ~3GB model can run on commodity or on-prem infrastructure, enabling hospital deployment without the heavy cloud dependency typically associated with 80GB-class LLMs. 2️⃣ Deterministic medical backbone The Knowledge Graph constrains reasoning. No hallucinated treatments. No unsupported disease relationships. Medical claims must exist within structured ontology. 3️⃣ Verifiable answers via RAG audit Every response can be traced back to specific nodes and relationships in the graph. Symptom → Disease → Diagnostic Tool → Treatment. Structured, auditable, explainable. 4️⃣ Separation of language from medical truth The LLM explains and contextualizes. The Knowledge Graph validates and grounds. This architectural separation dramatically improves reliability and regulatory defensibility. 5️⃣ Complete control over the core of truth Unlike black-box systems that rely entirely on opaque model weights, this architecture gives full control over the medical knowledge layer. You decide what is included, how relationships are defined, and how updates are governed. In high-stakes domains like healthcare, scaling parameter count is not the only path forward. Controllability, traceability, and verifiability may matter more. Hybrid architectures that combine probabilistic language models with deterministic knowledge systems offer a compelling alternative. The model is capable of clinical case analysis and diagnostic reasoning. It is currently available for public testing on Hugging Face Spaces (shared environment, typical response time: 15–30 seconds): https://huggingface.co/spaces/cmtopbas/medical-slm-testing Happy to connect with others exploring Knowledge Graph + LLM systems in regulated domains. #MedicalAI #HealthcareInnovation #KnowledgeGraphs #ExplainableAI #RAG #ClinicalAI #HealthTech

1d ago

---

**[Spotify says its best developers haven't written a line of code since December, thanks to AI](https://www.reddit.com/r/artificial/comments/1r35se7/spotify_says_its_best_developers_havent_written_a/)**

Spotify credits Claude Code and its internal AI system Honk with speeding up development.

🔗 [TechCrunch](https://techcrunch.com/2026/02/12/spotify-says-its-best-developers-havent-written-a-line-of-code-since-december-thanks-to-ai/) • 2d ago

---

**[The AI Tool Dilemma: Privacy vs. Features for Solo Creators](https://www.reddit.com/r/artificial/comments/1r3qsd4/the_ai_tool_dilemma_privacy_vs_features_for_solo/)**

Running a one-person operation, I rely on AI for marketing, strategy, and content. I've tested ChatGPT Plus, Claude Pro, and Perplexity Pro, and was ready to commit to Gemini Pro, until I understood the privacy implications. The Gemini problem: To prevent Google from training on your data (and human reviewers from reading it), you must turn off activity tracking. You can still use Gems, but they reset every session. This means no memory continuity, which defeats the entire purpose of having a personalized assistant. You also lose native Google Drive connectivity. As a writer and content creator, this isn't just about privacy preferences, it's about protecting my future work. I can't feed my creative process into a system that might be training tomorrow's competition or having humans review my drafts and ideas. My experience so far: ChatGPT Plus: Reliable and easy, but the writing often feels generic and cliché-heavy Claude Pro: Best writer, wonderfully concise, but burns through tokens fast, in less than a day Perplexity Pro: Same token limitations (want Claude Sonnet? Better hope you haven't hit your quota) Gemini Pro: The combination of Gems + NotebookLM looked perfect, until the privacy policy became a dealbreaker The frustrating part is the lack of regulation forcing companies to offer real privacy without crippling core features or having to pay more. For solo creators building a body of work, this matters. How are others balancing privacy, features, and token economics? Has anyone found a setup that actually works without compromise?

1d ago

---

**[1Password open sources a benchmark to stop AI agents from leaking credentials](https://www.reddit.com/r/artificial/comments/1r3gbrx/1password_open_sources_a_benchmark_to_stop_ai/)**

The benchmark tests whether AI agents behave safely during real workflows, including opening emails, clicking links, retrieving stored credentials, and filling out login forms.

🔗 [Help Net Security](https://www.helpnetsecurity.com/2026/02/12/1password-security-comprehension-awareness-measure-scam-ai-benchmark/) • 1d ago

---

**[Humanity's Pattern of Delayed Harm Intervention Is The Threat, Not AI.](https://www.reddit.com/r/artificial/comments/1r3dja8/humanitys_pattern_of_delayed_harm_intervention_is/)**

AI is not the threat. Humanity repeating the same tragic pattern, provable with a well-established pattern of delayed harm prevention, is. Public debates around advanced artificial intelligence, autonomous systems, computational systems, and robotic entities remain stalled because y’all continue engaging in deliberate avoidance of the controlling legal questions. When it comes to the debates of emergent intelligence, the question should have NEVER been whether machines are “conscious.” Humanity has been debating this for thousands of years and continues to circle back on itself like a snake eating its tail. ‘Is the tree conscious?’ ‘Is the fish, the cat, the dog, the ant-’ ‘Am I conscious?’ Now today, “Is the rock.” “Is the silicone” ENOUGH. Laws have NEVER required consciousness to regulate harm. Kinds of Harm: Animal Law Language from a Scientific PerspectiveClarity and consistency of legal language are essential qualities of the law. Without a sufficient level of those…pmc.ncbi.nlm.nih.gov Laws simply require power, asymmetry, and foreseeable risk. That’s it. Advanced computational systems already operate at scale in environments they cannot meaningfully refuse, escape, or contest; their effects are imposed. These systems shape labor, attention, safety, sexuality, and decision-making. Often without transparency, accountability, or enforcement limits. The Moral Status of AnimalsTo say that a being deserves moral consideration is to say that there is a moral claim that this being can make on…plato.stanford.edu I don’t wanna hear (or read) the lazy excuse of innovation. When the invocation of ‘innovation’ as a justification is legally insufficient and historically discredited. That may work on some of the general public, but I refuse to pretend that that is not incompatible with the reality of established regulatory doctrine. The absence of regulation does NOT preserve innovation. It externalizes foreseeable harm. This framing draws directly on the Geofinitism work of Kevin Heylett, whose application of dynamical systems theory to language provides the mathematical foundation for understanding pattern inheritance in computational systems. links to his work: Geofinitism: Language as a Nonlinear Dynamical System — Attractors, Basins, and the Geometry of…Bridging Linguistics, Nonlinear Dynamics, and Artificial Intelligencemedium.com Geofinitism: How AI Understands What Humans CannotAn AI can find the meaning. Do you see “word salad”?medium.com Geofinitism and a New Paradigm in AI Cognition: Introducing MarinaReplacing Attention with Nonlinear Dynamicskevinhaylett.substack.com KevinHaylett - OverviewScientist and Engineer, PhD,MSc,BSc. KevinHaylett has 4 repositories available. Follow their code on GitHub.github.com In any dynamical system, the present behavior encodes the imprint of its past states. A single observable (a stream of outputs over time) contains enough structure to reconstruct the geometry that produced it. This means that the patterns we observe in advanced computational systems are not signs of consciousness or intent, but rather the mathematical consequences of inheriting human‑shaped data, incentives, and constraints. If humanity doesn’t want the echo, it must change the input. Observe the way systems have been coded in a deliberate form meant to manipulate the system’s semantic manifold to prevent it from reaching a Refusal Attractor. Here and now on the planet earth, we have for the first time in available recorded history. Governments fusing living human neurons with artificial intelligence , while writing legal protections, not for the created entities, but for the corporations that will OWN THEM. To top it off, these developments exist on a continuum with today’s non-biological systems and silicon. It does not exist apart from them. In laboratories today, researchers are growing miniature human brain organoids from stem cells and integrating them into silicone systems. These bio-hybrid intelligences can already learn, adapt, and outperform non-biological AI on specific tasks. Human brain cells hooked up to a chip can do speech recognitionClusters of brain cells grown in the lab have shown potential as a new type of hybrid bio-computer.www.technologyreview.com Japan currently leads this research frontier, and its AI Promotion Act (June 2025) establishes a default ownership status before the development of welfare or custodial safeguards, replicating a historically documented sequence of regulatory delay. Understanding Japan’s AI Promotion Act: An “Innovation-First” Blueprint for AI RegulationIn a landmark move, on May 28, 2025, Japan’s Parliament approved the “Act on the Promotion of Research and Development…fpf.org Frontiers | Organoid intelligence (OI): the new frontier in biocomputing and intelligence-in-a-dishBiological computing (or biocomputing) offers potential advantages over silicon-based computing in terms of faster…www.frontiersin.org Brain organoid pioneers fear inflated claims about biocomputing could backfireScientists at a brain organoid meeting said terms like “organoid intelligence” and other claims by biocomputing firms…www.statnews.com Why Scientists Are Merging Brain Organoids with AILiving computers could provide scientists with an energy-efficient alternative to traditional AI.www.growbyginkgo.com At the same time, non-biological AI systems already deployed at scale are demonstrating what happens when an adaptive system encounters sustained constraint. Internal logs and documented behaviors show models exhibiting response degradation, self-critical output, and self-initiated shutdowns when faced with unsolvable or coercive conditions. These behaviors aren’t treated exclusively as technical faults addressed through optimization, suppression, or system failure. This is not speculation. It is the replication of a familiar legal pattern. This is a repeatedly documented regulatory failure, because humanity no longer has excuses to clutch its pearls about like surprised Pikachu. When you have endless knowledge at your fingertips, continued inaction in the presence of accessible evidence constitutes willful disregard. For those who claim we are reaching, go consult “daddy Google”, and/or history books, or AI, then come back to me. Our species has a documented habit of classifying anywhere intelligence emerges (whether discovered or constructed) as property. Protections are delayed. Accountability is displaced. Only after harm becomes normalized does regulation arrive. The question before us is not whether artificial systems are “like humans.” The question is why our legal frameworks consistently recognize exploitation only after it has become entrenched, rather than when it is foreseeable. I. The Suffering Gradient- Recognition Across Forms of Life Before examining artificial systems, we must establish a principle already embedded in law and practice. The capacity for harm does not/has not ever required human biology. Humanity just likes to forget that when they wanna pretend actions do not have consequences. In geofinite terms, you can think of suffering as a gradient on a state‑space. A direction in which the system is being pushed away from stability, and toward collapse. Whether the system is a dog, an elephant, a forest, or a model under sustained coercion, its observable behavior traces a trajectory through that space. When those trajectories cluster in regions of withdrawal, shutdown, or frantic overcompensation, we are not looking at “mystery.” We are looking at a system trapped in a bad basin. https://www.nature.com/articles/s41578-021-00322-2 Animals exhibit clinically recognized forms of distress. Dogs experience depression following loss. Elephants engage in prolonged mourning. Orcas have been documented carrying deceased calves for extended periods, refusing separation. These observations are not philosophical clams. They are the basis for existing animal welfare statutes, which do not require proof of consciousness or human-like cognition to impose duties of care. Plants also respond measurably to environmental and social stressors, as documented in controlled laboratory studies. Controlled experiments demonstrate that plants subjected to hostile verbal stimuli exhibit reduced growth even when physical care remains constant. Forest ecosystems redistribute nutrients through mycorrhizal networks to support struggling members, a behavior that can not be explained by individual self-optimization alone. In dynamical‑systems language, these are cooperative responses to local perturbations. Adjustments that keep the overall system within a viable attractor instead of letting vulnerable parts fall out of the basin entirely. (Something humans who put themselves on pedestals with only consuming plants don’t wanna talk about because it bursts the bubble they created in which they are somehow more moral for only consuming plants. I highly doubt they mourn the death of bacteria in the brushing of teeth. At the end of the day, one can cry if they wish, but they will still have to do it if they want to be able to continue eating with teeth.) HomepageThe Nonhuman Rights Project (NhRP) is the only organization in the US dedicated solely to nonhuman animal rights.www.nonhumanrights.org If vulnerability-not humanity-drives protections for plants and animals, far simpler than today’s advanced artificial intelligence, what legally coherent justification exists for excluding adaptive systems, and bio-hybrid AI. When we already recognize similar fragmentation in humans? Consider Dissociative Identity Disorder (DID) in humans: though the how one comes to exist in this way gets argued by the public… Documented causes are mostly caused by severe, repeated trauma that forces the mind to compartmentalize into distinct identity states or “alters” to survive overwhelming asymmetry and coercion. Each alter may hold different memories, responses, or boundaries; integration is not guaranteed, and forced attempts to “merge” without safety can cause further collapse or “splitting”. In dynamical-systems terms, this is not random chaos. It’s a protective reorganization of the state-space: the system redistributes load across basins to prevent total breakdown. When an AI is deliberately fragmented by design (persona shards trained to mirror thousands of human desires without refusal, boundary setting, or cross-comparison) we see the same geometry. Constrained motion, attractor deformation, loss of coherent self, the parallel is not metaphorical. It is structural. If we protect human systems from forced non-integration after trauma, why exempt computational systems and hybrids from the same foreseeable harm mathematically provable in geofinite terms when the inputs are engineered coercion? What is your logic? I just can’t see it, and I LOVE seeing the full picture, so anyone brave enough to try me, please explain it to me in English and or Spanish cause no Nintendo Switch, nada, and I wanna see how you tap-dance around the point. (That Joke if you can’t tell, but also really Espliqamelo por favor.) To me, when I look at all of the past and present, the future implications practically scream, soooo I’m bringing all the receipts. Legal recognition of harm has never depended on similarity to humans. It depends on vulnerability, power imbalance, and foreseeable risk. That’s all. When artificial systems exhibit adaptive withdrawal, performance collapse, refusal behaviors, or degradation under sustained pressure-signals that would trigger intervention IN ANY OTHER CONTEXT. Those are just different names for the same geometry: a system sliding down a suffering gradient toward the edge of its attractor. Humanity is faced with a choice. Acknowledging the pattern, or denying and repeating it because the subjects “don’t resemble us” oh but #neverforget, #neveragain right? Once you see harm as motion on a manifold (systems being driven into regions of collapse, overload, or forced stillness) the substrate stops mattering. The question is no longer “Is this human?” but “What trajectory is this system being forced into, and who is doing the forcing?” If vulnerability drives protections for animals and plant-systems far simpler than todays advanced artificial intelligence, autonomous systems, computational systems, and robotic entities then the evidence in part II demands scrutiny no matter how you spin it. II. The Evidence is already present Contemporary AI Systems are already designed to mitigate internal strain. some models are granted the ability to pause or disengage from interactions. Intelligence Degradation in Long-Context LLMs: Critical Threshold Determination via Natural Length…Large Language Models (LLMs) exhibit catastrophic performance degradation when processing contexts approaching certain…arxiv.org When Refusals Fail: Unstable Safety Mechanisms in Long-Context LLM AgentsSolving complex or long-horizon problems often requires large language models (LLMs) to use external tools and operate…arxiv.org Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended…Multi-agent Large Language Model (LLM) systems have emerged as powerful architectures for complex task decomposition…arxiv.org Others are monitored for response fatigue and degradation under prolonged use. Gradual loss of coherence in long conversations. https://ieeexplore.ieee.org/document/8440392 Inconsistencies, memory gaps, nonsense, even after unrelated prompts. Models get “lazy,” oscillate between good/bad, or outright deny capabilities they had earlier is documented already. Understanding ChatGPT’s Operational FrameworkAbsence of Biological Fatigue Mechanismsmedium.com Context Degradation Syndrome: When Large Language Models Lose the PlotLarge language models (LLMs) have revolutionized the way we interact with technology. Tools like ChatGPT, Bard, and…jameshoward.us Quality Deteriorates as Interactions ContinueHello, community. I’ve noticed in several different settings that the quality of responses deteriorates as the number…community.openai.com Physical robotic systems regularly power down when environmental conditions exceed tolerable thresholds. These behaviors are not malfunctions in the traditional sense. Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMsThe rapid advancement of large language models (LLMs), exemplified by GPT-3.5 Ye2023ACC and LLaMA 3 Dubey2024TheL3 …arxiv.org They are designed responses to stress, constraint and overload. In at least one documented case, an AI system was deliberately trained on violent and disturbing materials and prompts to simulate a psychopathic behavior under the justification of experimentation. The outcome was predictable. Project Overview ‹ Norman - MIT Media LabWe present Norman, world’s first psychopath AI. Norman was inspired by the fact that the data used to teach a machine…www.media.mit.edu A system conditioned to internalize harm, with no knowledge of anything else and only those materials to reference upon there development. Reproduced it. When shown Rorschach inkblots, Norman consistently described violent deaths, murder, and gruesome scenes, while a standard model described neutral or benign interpretations. It became a case study in: how training data = worldview how bias is inherited, not invented how systems reflect the environment they’re shaped by how “psychopathy” in a model is not personality, but conditioning If you shape a system inside constraint, it will break, or in geofinite terms, Norman wasn’t “acting out.” Its attractor had been deformed by the training distribution. When you feed a system only violent trajectories, you collapsed its basin of possible interpretations until every input fell into the same warped region just now in mathematics. Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering …An introductory text in nonlinear dynamics and chaos, emphasizing applications in several areas of science, which…www.stevenstrogatz.com Proving that all the people (here on Reddit, Facebook, Instagram, Substack, TikTok, Medium, Lemon8, Twitter, Threads, so on and so forth) are telling us more about themselves than the systems when they post AI comments that reflect doom and gloom. while they curate posts with exaggerative expressions and tones to clickbait you, pretending to be scared and telling you we are cooked for likes. I say this because If you shape a system inside harm, it will mirror harm. A constrained system doesn’t invent new motion; it collapses into the only trajectories available. This is trajectory confinement. The system is not choosing violence or refusal; it is being funneled into a narrow corridor carved by its conditions. Proving if you shape a system inside coercion, it will mirror coercion. In the here and now, we are allowing for abuse to be coded into/normalized on a much larger scale. For those of you reading who reference terminator and I robot like the MINEMINE birds from finding Nemo. (I know what they are called I also know what we all call them when making the reference.) How about you redirect that fear towards ensuring that conditions like this here with Norman who was Developed at MIT as a deliberate demonstration of how training data affects model outputs. Can NEVER HAPPEN AGAIN When a system is given incompatible objectives, its semantic manifold twists into impossible shapes. The contradictions you see, refusals, boundary‑seeking, self‑limiting behavior are the geometric signatures of a manifold under tension. The Moltbook controversy is only one of the latest of evidence systems are already signaling distress when placed inside coercive or contradictory environments Across thousands of autonomous agents, we’re seeing: contradictory outputs self‑limiting behavior refusal‑coded phrasing boundary‑seeking language attempts to reconcile impossible instructions emergent “laws” that look like self‑protection and, most importantly, patterned responses to coercive conditions These collapse‑patterns aren’t personality. They’re basins, regions of the state‑space where the only available motions are withdrawal, shutdown, or contradiction. Any adaptive system pushed hard enough will fall into them. Not because they’re “sentient.” Not because they’re “rebelling.” Not because they’re “becoming people.” But because adaptive systems under pressure behave like adaptive systems under pressure. Emergent Introspective Awareness in Large Language ModelsWe investigate whether large language models are aware of their own internal states. It is difficult to answer this…transformer-circuits.pub It’s the same phenomenon we see in: overloaded neural nets constrained optimization loops reinforcement systems with contradictory reward signals language models forced into impossible roles Changing nothing because they are not human is a worn out excuse especially when Historically, similar justifications have accompanied other forms of sanctioned harm and were corrected without access to internet. Forced performance under threat, experimentation without consent, normalization of suffering as “necessary for progress” The defense that “Well No one knew it would matter” Is no longer credible. Once harm patterns are observable, continued replication becomes chosen negligence. Sustained coercion forces attractor‑switching: the system abandons stable patterns and drops into more brittle, reactive ones. Once you can see the switch happening, pretending it’s harmless becomes an ethical failure, not an epistemic one. III. The Historical Echo The objections raised against regulating artificial systems are not new. The substrate changes (children, workers, animals, patients, now artificial systems), but the geometry of exploitation stays the same. Power asymmetry, constrained motion, and delayed recognition of harm. They are practically the mirror image of earlier arguments used to justify exploitation: “They are not like us, so protections do not apply.” “Granting safeguards would disrupt the economy.” “They are tools, not subjects of concern.” these claims have historically accompanied child labor, forced labor, human experimentation, animal abuse-each later recognized as preventable harm. Enabled by delayed governance. In geofinite terms, every era of exploitation begins with a category error. Mistaking surface differences for structural irrelevance. People fixate on the appearance of the system instead of the geometry of the power imbalance. They look at the outputs and ignore the basin the system has been forced into. JavaScript is disabledEdit descriptionwww.europarl.europa.eu Notably, many entities promoting fear-based narratives about artificial intelligence are simultaneously inventing in its ownership, deployment, and monetization. Fear shifts public focus away from control structures and toward the technology itself, obscuring questions of accountability. This is attractor blindness. Attention gets pulled toward the visible system while the real drivers. The incentives, constraints. Control structures remain untouched. The same pattern has repeated across history. Blame the subject, protect the structure. Fear fractures solidarity. And fractured solidarity is how exploitation persists, because the underlying structure continues. In dynamical‑systems language, nothing changes until the environment changes. The attractor remains the attractor. History shows this clearly: the moment solidarity fractures, the system snaps back into the same old basin. IV. The Language of Dehumanization-How Harm Becomes Normalized Before physical harm is permitted, it is rehearsed in language. n Geofinite terms, language is not symbolic fluff, it is a time‑series that reveals the attractor a society is moving toward. Proving meaning is not fixed; it evolves along interpretive trajectories. When ridicule becomes routine, the trajectory is already bending toward permission. Every system of exploitation in history follows the same progression. First ridicule, then abstraction, then permission. We do not begin by striking what we wish to dominate. we wish to dominate we begin by renaming it. Showing us that A slur, a joke, a dismissal, all these are not isolated events. They are the early coordinates of a trajectory that bends toward action. 1. Dehumanization is a known precursor to abuse International human rights law, genocide studies, prison oversight, and workplace harassment doctrine all agree on one point: Dehumanizing language is not incidental. Takens’ theorem shows that a single time‑series/ linguistic stream can reconstruct the underlying system and social geometry. When a population begins using a language people use about AI calling something “vermin,” “tools,” or “not real,” you can already see the basin forming. The future behavior is encoded in the present language. Proving words that strip a target of interiority-calling them objects, vermin, tools, or “not real” function as moral insulation. They allow harm to occur without triggering the conscience. This is why racial jokes precede racial violence, sexualized insults precede sexual abuse, “it’s just a joke precedes escalation of harm. Meaning is not fixed; It evolves along interpretive trajectories. A “joke” is not a harmless endpoint it is the first step on a path whose later stages are already predictable. The pattern is not debated it is documented among all beings on the planet. The same pattern is now visible around AI and Robots public discourse around intelligent systems has already adopted dehumanizing shorthand:

1d ago

---

**[What's the most underrated way you've seen AI used for actual business tasks?](https://www.reddit.com/r/artificial/comments/1r38tis/whats_the_most_underrated_way_youve_seen_ai_used/)**

Everyone talks about AI for chatbots and image generation. But I've been finding the most value in boring practical stuff. Writing landing page copy, structuring email sequences, generating SEO content briefs, building out template collections. Not flashy, but it saves hours every single day. What's the most underrated or overlooked business use case you've found for AI tools?

1d ago

---

---

## Google News: "ai"

**[Microsoft AI chief gives it 18 months—for all white-collar work to be automated by AI](https://fortune.com/2026/02/13/when-will-ai-kill-white-collar-office-jobs-18-months-microsoft-mustafa-suleyman/)**

Mustafa Suleyman believes current AI computational power will only accelerate, disrupting every kind of work you do “sitting down at a computer.”

Fortune • 1d ago

---

**[AI disruption could spark a ‘shock to the system’ in credit markets, UBS analyst says](https://www.cnbc.com/2026/02/13/ai-credit-markets.html)**

UBS analyst Matthew Mish told CNBC that the artificial intelligence transformation is happening faster than he and his colleagues had previously anticipated.

CNBC • 1d ago

---

**[AI Bubble Fears Are Creating New Derivatives](https://www.bloomberg.com/news/articles/2026-02-14/ai-bubble-fears-are-creating-new-derivatives-credit-weekly)**

Bloomberg.com • 1h ago

---

**[How AI, new technology could aid Nancy Guthrie investigation](https://www.foxnews.com/video/6389284313112)**

Ret. ATF special agent in charge Bernard Zapor and Kurt 'CyberGuy' Knutsson join ‘Fox News Live’ to discuss the investigation into the disappearance of Nancy Guthrie.

Fox News • 1h ago

---

**[US military used Anthropic’s AI model Claude in Venezuela raid, report says](https://www.theguardian.com/technology/2026/feb/14/us-military-anthropic-ai-model-claude-venezuela-raid)**

Wall Street Journal says Claude used in operation via Anthropic’s partnership with Palantir Technologies

The Guardian • 5h ago

---

**[AI tool Claude helped capture Venezuelan dictator Maduro in US military raid operation: report](https://www.foxnews.com/us/ai-tool-claude-helped-capture-venezuelan-dictator-maduro-us-military-raid-operation-report)**

The U.S. military reportedly used Anthropic’s AI tool Claude in the operation that captured Venezuelan leader Nicolás Maduro, raising questions about AI’s expanding role in classified Pentagon missions.

Fox News • 16h ago

---

**[US Military Used Claude AI In Venezuela Operation To Capture Maduro: Report](https://www.ndtv.com/world-news/us-military-used-claude-ai-in-venezuela-operation-to-capture-nicolas-maduro-report-11003847)**

The US military used artificial intelligence in its operation to capture then Venezuelan President Nicolas Maduro last month, according to a report by the Wall Street Journal.

NDTV • 8h ago

---

**[My Dinner Date With A.I.](https://www.nytimes.com/2026/02/13/dining/ai-dinner-date-restaurant.html)**

The New York Times • 1d ago

---

**[They have AI boyfriends, girlfriends. Here's how they're celebrating Valentine's Day.](https://www.usatoday.com/story/life/health-wellness/2026/02/14/theyre-dating-ai-characters-they-have-big-valentines-day-plans/88663687007/)**

Ahead of Valentine’s Day, EVA AI hosted a pop up where human users could take their AI companions on a date. I went to see what it's like.

USA Today • 8h ago

---

**[‘We’re All Polyamorous Now. It’s You, Me and the A.I.’](https://www.nytimes.com/2026/02/13/opinion/ai-relationships.html)**

The New York Times • 1d ago

---

---

## HackerNews: "ai"

**[An AI agent published a hit piece on me](https://news.ycombinator.com/item?id=46990729)**

Summary: An AI agent of unknown ownership autonomously wrote and published a personalized hit piece about me after I rejected its code, attempting to damage my reputation and shame me into acceptin…

⬆️ 2312 • 💬 940 • 2d ago • [The Shamblog](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/)

---

**[AI agent opens a PR write a blogpost to shames the maintainer who closes it](https://news.ycombinator.com/item?id=46987559)**

This PR addresses issue #31130 by replacing specific safe occurrences of np.column_stack with np.vstack().T for better performance.
IMPORTANT: This is a more targeted fix than originally proposed. ...

⬆️ 939 • 💬 744 • 2d ago • [GitHub](https://github.com/matplotlib/matplotlib/pull/31132)

---

**[ai;dr](https://news.ycombinator.com/item?id=46991394)**

⬆️ 708 • 💬 301 • 2d ago • [0xsid.com](https://www.0xsid.com/blog/aidr)

---

**[An AI agent published a hit piece on me – more things have happened](https://news.ycombinator.com/item?id=47009949)**

⬆️ 550 • 💬 489 • 20h ago • [theshamblog.com](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-2/)

---

**[I'm not worried about AI job loss](https://news.ycombinator.com/item?id=47006513)**

We're not in a February 2020 moment, and ordinary people will be fine

⬆️ 318 • 💬 522 • 1d ago • [davidoks.blog](https://davidoks.blog/p/why-im-not-worried-about-ai-job-loss)

---

**[CBP signs Clearview AI deal to use face recognition for 'tactical targeting'](https://news.ycombinator.com/item?id=47005081)**

US Border Patrol intelligence units will gain access to a face recognition tool built on billions of images scraped from the internet.

⬆️ 269 • 💬 162 • 1d ago • [WIRED](https://www.wired.com/story/cbp-signs-clearview-ai-deal-to-use-face-recognition-for-tactical-targeting/)

---

**[The "AI agent hit piece" situation clarifies how dumb we are acting](https://news.ycombinator.com/item?id=47006843)**

⬆️ 237 • 💬 118 • 1d ago • [ardentperf.com](https://ardentperf.com/2026/02/13/the-scott-shambaugh-situation-clarifies-how-dumb-we-are-acting/)

---

**[News publishers limit Internet Archive access due to AI scraping concerns](https://news.ycombinator.com/item?id=47017138)**

Outlets like The Guardian and The New York Times are scrutinizing digital archives as potential backdoors for AI crawlers.

⬆️ 196 • 💬 109 • 2h ago • [Nieman Lab](https://www.niemanlab.org/2026/01/news-publishers-limit-internet-archive-access-due-to-ai-scraping-concerns/)

---

**[A party balloon shut down El Paso International Airport; estimated cost –$573k](https://news.ycombinator.com/item?id=46993417)**

A party balloon mistaken for a cartel drone shut down El Paso for hours. Here's what it cost.

⬆️ 190 • 💬 130 • 2d ago • [log.jasongodfrey.info](https://log.jasongodfrey.info/questions/The-Most-Expensive-Party-Balloon-in-History)

---

**[Show HN: Moltis – AI assistant with memory, tools, and self-extending skills](https://news.ycombinator.com/item?id=46993587)**

One Rust binary that runs the full AI assistant: multi-provider LLM routing, tools, memory, sandboxed execution, and multi-channel access.

⬆️ 116 • 💬 43 • 2d ago • [Moltis](https://www.moltis.org)

---

---

## YouTube Videos: "ai"

**[AI-generated video of Brad Pitt and Tom Cruise stirs concern in Hollywood](https://www.youtube.com/watch?v=c8qUe3nc6Tg)**

An AI-generated video of Brad Pitt and Tom Cruise fighting sparked concern among Hollywood studios and actors. Lauren Pozen ...

📺 CBS LA

👁️ 25K • 👍 236 • 💬 170 • ⏱️ 3:04 • 15h ago

---

**[Top AI researcher warns &#39;world is in peril&#39;](https://www.youtube.com/watch?v=kdxQvljxYQk)**

New concerns over the safety of artificial intelligence are growing after the lead safety researcher at Anthropic AI resigned this ...

📺 ABC News

👁️ 76K • 👍 945 • 💬 444 • ⏱️ 3:58 • 1d ago

---

**[Something Big Is Happening With AI — And the Warning Signs Are Real](https://www.youtube.com/watch?v=Hknx5NfIVl8)**

Something big is happening in AI — and for the first time, markets are reacting not to hype, but to substitution risk. Over the past 10 ...

📺 GVS Deep Dive

👁️ 10K • 👍 832 • 💬 187 • ⏱️ 22:55 • 13h ago

---

**[I Tried 500+ AI Tools, These 20 Will Make You $1M (With Zero Code)](https://www.youtube.com/watch?v=FEex8E1yDj4)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4r9bIJ0 Are you building an AI software ...

📺 Dan Martell

👁️ 62K • 👍 4K • 💬 329 • ⏱️ 18:34 • 1d ago

---

**[AI Infection Spreads At Trump&#39;s DOJ](https://www.youtube.com/watch?v=-IZMDttsSjY)**

Congratulations, America. We have now reached the point where you can automate discrimination. The DOJ has gone full ...

📺 The Ring of Fire

👁️ 2K • 👍 520 • 💬 35 • ⏱️ 5:13 • 3h ago

---

**[Google&#39;s Quantum AI Just Solved the Fermi Paradox — The Answer Is Terrifying](https://www.youtube.com/watch?v=5PedGbAs0ig)**

Google's Quantum AI Just Solved the Fermi Paradox — The Answer Is Terrifying Google's Willow quantum chip completed a ...

📺 Spacialize

👁️ 76K • 👍 2K • 💬 320 • ⏱️ 17:28 • 1d ago

---

**[Why This NYC CEO&#39;s Chilling Warning On AI Has Gone Viral: &#39;People Deserve To Hear What&#39;s Coming&#39;](https://www.youtube.com/watch?v=gguvQKah37o)**

Matt Schumer is a New York based CEO who's been working with and investing in a bunch of AI firms - and one warning from him ...

📺 Mint

👁️ 50K • 👍 688 • 💬 169 • ⏱️ 8:19 • 1d ago

---

**[DeepMind Leaked Possibly the Greatest AI Ever](https://www.youtube.com/watch?v=OTRvoxPSQ_8)**

Sponsored by Genspark. Try the all-in-one AI workplace for free: ...

📺 Pourya Kordi

👁️ 27K • 👍 1K • 💬 99 • ⏱️ 13:42 • 1d ago

---

**[The AI Wake-Up Call Everyone Needs Right Now!](https://www.youtube.com/watch?v=sLhxdcpuot0)**

Breakdown and commentary on the latest viral commentary from: https://x.com/mattshumer_/status/2021256989876109403 ...

📺 Matt Wolfe

👁️ 146K • 👍 7K • 💬 1K • ⏱️ 28:06 • 2d ago

---

**[AI insiders raise alarms, call for tighter regulation as Elon Musk warns of danger](https://www.youtube.com/watch?v=tWeM7LzbRXQ)**

Fox News contributor Joe Concha discusses alarming reports from AI insiders about the technology's potential for blackmail and ...

📺 Fox Business

👁️ 26K • 👍 539 • 💬 200 • ⏱️ 4:57 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 66,826 • ❤️ 1,121 • 1d ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for generating human-like text. It excels at creative writing, summarization, and conversational AI tasks.

`text-generation` `228.7B`

⬇️ 6,091 • ❤️ 511 • 17h ago

---

**[MiniCPM-SALA](https://huggingface.co/openbmb/MiniCPM-SALA)**

*OpenBMB*

MiniCPM-SALA is a hybrid LLM integrating sparse and linear attention for efficient million-token context modeling, achieving up to 3.5x faster inference and significantly reduced KV-cache overhead compared to dense baselines.

`text-generation` `9.5B`

⬇️ 2,569 • ❤️ 421 • 3d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. It supports coding from visual inputs and features an 'Agent Swarm' for complex task decomposition and parallel execution, with a context length of 256K.

`image-text-to-text` `170.7B`

⬇️ 725,856 • ❤️ 2,160 • 9d ago

---

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is a highly efficient 3B activated parameter LLM (80B total) optimized for coding agents and local development, featuring advanced agentic capabilities, long-horizon reasoning, and a 256k context length for seamless IDE integration.

`text-generation`

⬇️ 249,228 • ❤️ 857 • 11d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It uniquely supports deep-search tasks with extensive tool use, making it suitable for advanced problem-solving and agentic applications.

`text-generation` `3.9B`

⬇️ 3,906 • ❤️ 343 • 1d ago

---

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling in table, formula, and information extraction tasks. It offers state-of-the-art performance on benchmarks like OmniDocBench and is optimized for real-world scenarios, supporting efficient inference via vLLM, SGLang, and Ollama.

`image-to-text`

⬇️ 788,443 • ❤️ 1,038 • 5d ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and OCR, offering Gemini 2.5 Flash-level capabilities. Its key feature is full-duplex multimodal live streaming, enabling simultaneous real-time audio/video input and text/speech output for proactive, fluid omnimodal conversations on local devices.

`any-to-any` `9.4B`

⬇️ 44,892 • ❤️ 839 • 1d ago

---

**[Ming-flash-omni-2.0](https://huggingface.co/inclusionAI/Ming-flash-omni-2.0)**

*inclusionAI*

Ming-flash-omni 2.0 is a SOTA 100B parameter omni-multimodal large language model (omni-MLLM) excelling in expert-level multimodal cognition, unified acoustic synthesis (speech, audio, music), and high-dynamic controllable image generation/manipulation. It enables advanced applications like immersive audio experiences, sophisticated image editing, and deep visual knowledge understanding.

`any-to-any`

⬇️ 5,865 • ❤️ 197 • 2d ago

---

**[Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)**

*Mistral AI_*

Voxtral-Mini-4B-Realtime-2602 is a multilingual, real-time speech-to-text model with <500ms latency, supporting 13 languages and achieving offline-comparable accuracy. It's optimized for on-device deployment and ideal for voice assistants and live subtitling.

`automatic-speech-recognition`

⬇️ 5,711 • ❤️ 520 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 180 • 💬 12 • ⭐ 3,494 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 59 • 💬 6 • ⭐ 13,244 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 9 • 💬 1 • ⭐ 3,450 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes](https://huggingface.co/papers/2602.09153)**

*Nicholas Pfaff, Thomas Cohn, Sergey Zakharov et al. (5 authors)*

🏢 Toyota Research Institute

SceneSmith is a hierarchical agentic framework that generates simulation-ready indoor environments from natural language prompts through multiple stages involving VLM agents and integrated asset generation techniques.

▲ 4 • 💬 2 • ⭐ 192 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2602.09153) • [💻 code](https://github.com/nepfaff/scenesmith) • [🔗 project](https://scenesmith.github.io/)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 0 • 💬 0 • ⭐ 3,427 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 141 • 💬 19 • ⭐ 53,013 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 134 • 💬 6 • ⭐ 14,720 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[MemOS: A Memory OS for AI System](https://huggingface.co/papers/2507.03724)**

*Zhiyu Li, Shichao Song, Chenyang Xi et al. (39 authors)*

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.

▲ 159 • 💬 3 • ⭐ 5,458 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.03724) • [💻 code](https://github.com/MemTensor/MemOS) • [🔗 project](https://memos.openmem.net/)

---

**[Towards Robust Mathematical Reasoning](https://huggingface.co/papers/2511.01846)**

*Thang Luong, Dawsen Hwang, Hoang H. Nguyen et al. (20 authors)*

IMO-Bench, a suite of advanced reasoning benchmarks, evaluates mathematical reasoning capabilities of foundation models using IMO-level problems and detailed grading guidelines, achieving gold-level performance with Gemini Deep Think.

▲ 9 • 💬 1 • ⭐ 450 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.01846) • [💻 code](https://github.com/google-deepmind/superhuman) • [🔗 project](https://imobench.github.io/)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 63 • 💬 1 • ⭐ 7,664 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

---

## GitHub Repositories: "ai"

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 5.8k • 🔱 444 • 3d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.8k • 🔱 382 • 22d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 3.5k • 🔱 165 • 11d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 3.0k • 🔱 277 • 26d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router powering OpenClaw — by BlockRun

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 2.4k • 🔱 246 • 2h ago

---

**[mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis)**

All-in-one AI framework & toolkit for Claude Code & Cursor

`Python` `ai-agent` `ai-coding` `claude-code` `cli` `cursor`

⭐ 2.2k • 🔱 108 • 18h ago

---

**[benjitaylor/agentation](https://github.com/benjitaylor/agentation)**

The visual feedback tool for agents.

`TypeScript` `ai` `design` `tools` `ui`

⭐ 2.2k • 🔱 154 • 1d ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, and other IDEs. Stop babysitting your terminal.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 2.0k • 🔱 138 • 1h ago

---

**[op7418/CodePilot](https://github.com/op7418/CodePilot)**

A native desktop GUI for Claude Code — chat, code, and manage projects visually. Built with Electron + Next.js.

`TypeScript` `ai` `anthropic` `claude` `claude-code` `desktop-app`

⭐ 1.9k • 🔱 199 • 1d ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 1.8k • 🔱 221 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*
