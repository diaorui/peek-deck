---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-05T20:38:27.096635+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 05, 2026 at 20:38 UTC  
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

**[LLMs can unmask pseudonymous users at scale with surprising accuracy](https://www.reddit.com/r/artificial/comments/1rl5wwp/llms_can_unmask_pseudonymous_users_at_scale_with/)**

So ai can uncover your anonymous identity on social media now so creating burner accounts may be pointless.

🔗 [Ars Technica](https://arstechnica.com/security/2026/03/llms-can-unmask-pseudonymous-users-at-scale-with-surprising-accuracy/) • 17h ago

---

**[Large genome model: Open source AI trained on trillions of bases](https://www.reddit.com/r/artificial/comments/1rlegdl/large_genome_model_open_source_ai_trained_on/)**

"...Evo 2, an open source AI that has been trained on genomes from all three domains of life (bacteria, archaea, and eukaryotes). After training on trillions of base pairs of DNA, Evo 2 developed internal representations of key features in even complex genomes like ours, including things like regulatory DNA and splice sites, which can be challenging for humans to spot. Bacterial genomes are organized along relatively straightforward principles. Any genes that encode proteins or RNAs are contiguous, with no interruptions in the coding sequence. Genes that perform related functions, like metabolizing a sugar or producing an amino acid, tend to be clustered together, allowing them to be controlled by a single, compact regulatory system. It’s all straightforward and efficient. Eukaryotes are not like that. The coding sections of genes are interrupted by introns, which don’t encode for anything. They’re regulated by a sequence that can be scattered across hundreds of thousands of base pairs. The sequences that define the edges of introns or the binding sites of regulatory proteins are all weakly defined—while they have a few bases that are absolutely required, there are a lot of bases that just have an above-average tendency to have a specific base (something like “45 percent of the time it’s a T”). Surrounding all of this in most eukaryotic genomes is a huge amount of DNA that has been termed junk: inactive viruses, terminally damaged genes, and so on. That complexity has made eukaryotic genomes more difficult to interpret. And, while a lot of specialized tools have been developed to identify things like splice sites, they’re all sufficiently error-prone that it becomes a problem when you’re analyzing something as large as a 3 billion-base-long genome. We can learn a lot more by making evolutionary comparisons and looking for sequences that have been conserved, but there are limits to that, and we’re often as interested in the differences between species. These sorts of statistical probabilities, however, are well-suited to neural networks, which are great at recognizing subtle patterns that can be impossible to pick out by eye. But you’d need absolutely massive amounts of data and computing time to process it and pick out some of these subtle features. We now have the raw genome data that the process needs. Putting together a system to feed it into an effective AI training program, however, remained a challenge. That’s the challenge the team behind Evo took on. The foundation of the Evo 2 system is a convolutional neural network called StripedHyena 2. The training took place in two stages. The initial stage focused on teaching the system to identify important genome features by feeding it sequences rich in them in chunks about 8,000 bases long. After that, there was a second stage in which sequences were fed a million bases at a time to provide the system the opportunity to identify large-scale genome features. The researchers trained two versions of their system using a dataset called OpenGenome2, which contains 8.8 trillion bases from all three domains of life, as well as viruses that infect bacteria. They did not include viruses that attack eukaryotes, given that they were concerned that the system could be misused to create threats to humans. Two versions were trained: one that had 7 billion parameters tuned using 2.4 trillion bases, and the full version with 40 billion parameters trained on the full open genome dataset. The logic behind the training is pretty simple: if something’s important enough to have been evolutionarily conserved across a lot of species, it will show up in multiple contexts, and the system should see it repeatedly during training. “By learning the likelihood of sequences across vast evolutionary datasets, biological sequence models capture conserved sequence patterns that often reflect functional importance,” the researchers behind the work write. “These constraints allow the models to perform zero-shot prediction without any task-specific fine-tuning or supervision.” That last aspect is important. We could, for example, tell it about what known splice sites look like, which might help it pick out additional ones. But that might make it harder for it to recognize any unusual splice sites that we haven’t recognized yet. Skipping the fine-tuning might also help it identify genome features that we’re not aware of at all at the moment, but which could become apparent through future research. All of this has now been made available to the public. “We have made Evo 2 fully open, including model parameters, training code, inference code, and the OpenGenome2 dataset,” the paper announces. The researchers also used a system that can identify internal features in neural networks to poke around inside of Evo 2 and figure out what things it had learned to recognize. They trained a separate neural network to recognize the firing patterns in Evo 2 and identify high-level features in it. It clearly recognized protein-coding regions and the boundaries of the introns that flanked them. It was also able to recognize some structural features of proteins within the coding regions (alpha helices and beta sheets), as well as mutations that disrupt their coding sequence. Even something like mobile genetic elements (which you can think of as DNA-level parasites) ended up with a feature within Evo 2. To test the system, the researchers started making single-base mutations and fed them into Evo 2 to see how it responded. Evo 2 could detect problems when the mutations affected the sites in DNA where transcription into RNA started, or the sites where translation of that RNA into protein started. It also recognized the severity of mutations. Those that would interrupt protein translation, such as the introduction of stop signals, were identified as more significant changes than those that left the translation intact. It also recognized when sequences weren’t translated at all. Many key cellular functions are carried out directly by RNAs, and Evo 2 was able to recognize when mutations disrupted those, as well. Impressively, the ability to recognize features in eukaryotic genomes occurred without the loss of its ability to recognize them in bacteria and archaea. In fact, the system seemed to be able to work out what species it was working in. A number of evolutionary groups use genetic codes with a different set of signals to stop the translation of proteins. Evo 2 was able to recognize when it was looking at a sequence from one of those species, and used the correct genetic code for them. It was also good at recognizing features that tolerate a lot of variability, such as sites that signal where to splice RNAs to remove introns from the coding sequence of proteins. By some measures, it was better than software specialized for that task. The same was true when evaluating mutations in the BRCA2 gene, where many of the mutations are associated with cancer. Given additional training on known BRCA2 mutations, its performance improved further. Overall, Evo 2 seems great for evaluating genomes and identifying key features. The researchers who built it suggest it could serve as a good automated tool for preliminary genome annotation."

🔗 [Ars Technica](https://arstechnica.com/science/2026/03/large-genome-model-open-source-ai-trained-on-trillions-of-bases/) • 9h ago

---

**[Nvidia’s Jensen Huang Rules Out $100 Billion OpenAI Investment](https://www.reddit.com/r/artificial/comments/1rkw3i9/nvidias_jensen_huang_rules_out_100_billion_openai/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-03-04/nvidia-s-jensen-huang-rules-out-100-billion-openai-investment) • 1d ago

---

**[AMD engineer leverages AI to help make a pure-Python AMD GPU user-space driver](https://www.reddit.com/r/artificial/comments/1rl27ei/amd_engineer_leverages_ai_to_help_make_a/)**

AMD's VP of AI Software, Anush Elangovan, has used Claude Code to help craft a pure-Python AMD GPU user-space driver

🔗 [phoronix.com](https://www.phoronix.com/news/AI-Pure-Python-AMD-GPU-Driver) • 20h ago

---

**[The OpenClaw Meltdown: 9 CVEs, 2,200 Malicious Skills, and the Most Comprehensive Real-World Test of the OWASP Agentic Top 10](https://www.reddit.com/r/artificial/comments/1rkiq9a/the_openclaw_meltdown_9_cves_2200_malicious/)**

🔗 [gsstk.gem98.com](https://gsstk.gem98.com/en-US/blog/a0087-openclaw-meltdown-owasp-agentic-living-case-study) • 1d ago

---

**[OpenAI looking at contract with NATO, source says](https://www.reddit.com/r/artificial/comments/1rkm1it/openai_looking_at_contract_with_nato_source_says/)**

🔗 [reuters.com](https://www.reuters.com/technology/openai-looking-contract-with-nato-source-says-2026-03-04/) • 1d ago

---

**[When should AI recommend a decision vs make one?](https://www.reddit.com/r/artificial/comments/1rkyshs/when_should_ai_recommend_a_decision_vs_make_one/)**

One of the things I’ve been thinking about with AI systems is the difference between decision support and decision making. Decision support: meaning the system provides info and a human evaluates it and may or may not take an action. Decision making: meaning the system actually performs the action. For example: • Suggesting eligible clinical trial participants • Flagging abnormal lab results • Recommending a route on a GPS In these cases the system helps a human decide. But there are also systems that automatically: • approve or deny requests • enroll users into workflows • trigger actions based on a rule set or user input That’s a very different level of responsibility. Curious where people think the boundary should be between recommendation and decision.

22h ago

---

**[🚀 OllamaFX v0.5.0 ya disponible!](https://www.reddit.com/r/artificial/comments/1rkxub9/ollamafx_v050_ya_disponible/)**

Ollama FX es una interfaz de escritorio Open Source para Ollama con grandes mejoras en gestión de chats, RAG, multimodalidad y organización 🔥 📅 Lanzado hoy en GitHub — https://github.com/fredericksalazar/OllamaFX 🧠 Principales novedades de la v0.5.0 ⭐ 🔍 Soporte RAG y análisis de archivos Carga y análisis de archivos directamente en chats: ahora puedes subir documentos y explorar su contenido con tus modelos LLM locales. Esta funcionalidad abre el camino a usar OllamaFX como herramienta de RAG (Retrieval-Augmented Generation) en workflows locales de IA sin necesidad de servicios externos. 👉 Permite extraer insights, responder preguntas y recuperar contenido relevante de tus propios archivos directamente desde la UI. 📁 Organización real de chats Carpetas para agrupar conversaciones: ordena tus chats por proyectos, temas o modelos. Mover chats entre carpetas con un simple arrastre. Papelera de reciclaje integrada: los chats (y carpetas) eliminados se mantienen hasta 30 días, para que no pierdas nada por accidente. 🖼️ Multimodalidad visual Soporte nativo para cargar imágenes y conversar con modelos que las interpretan. 📄 Exportación & mejor renderizado Exporta chats completos a formatos útiles. Visualizador Markdown mejorado con renderizado más limpio y estable para texto rico. ⚙️ Mejoras internas y experiencia de usuario Refactorizaciones internas para mayor estabilidad y escalabilidad. Optimización en filtros de modelos y selección. Ajustes finos en UI para una experiencia más fluida. Ampliación de localización / soporte multilenguaje. Indicadores visuales mientras el asistente “piensa” y feedback más claro durante la generación. 📚 Otras mejoras Estadísticas de uso y métricas básicas desde la vista “About”. Preparación para futuras integraciones y soporte a nuevos formatos LLM locales. 📦 Dónde descargar Todos los assets de la versión están listos para descargar en la sección de Releases del repo: 👉 https://github.com/fredericksalazar/OllamaFX/releases/tag/v0.5.0 🤝 Cómo ayudar al proyecto Si te gusta OllamaFX, puedes: ⭐ Dejar una estrella en GitHub 💬 Abrir issues con ideas o bugs 📄 Contribuir a la documentación 🧠 Proponer mejoras o nuevas integrations

23h ago

---

**[Fireflies and Otter just launched MCP connectors for meeting data — here's the open-source one you can self-host](https://www.reddit.com/r/artificial/comments/1rkli5j/fireflies_and_otter_just_launched_mcp_connectors/)**

Fireflies just became the first meeting tool in Anthropic's official Claude MCP Directory. Otter.ai launched an enterprise MCP server too. tl;dv has one as well. The "meeting data + MCP" space is heating up fast. But all three are closed-source, cloud-only. Your meeting data — strategy discussions, financials, personnel decisions — goes through their servers. I've been building Vexa, an open-source meeting bot API, and we've had a native MCP server since before any of them. The difference: it's Apache 2.0, and you can run the entire stack on your own infrastructure. Setup (takes ~2 minutes): { "mcpServers": { "vexa": { "url": "https://api.cloud.vexa.ai/mcp", "headers": {"X-API-Key": "your-key"} } } } Drop that in your Claude Desktop config, and you can ask: "What did we decide about pricing in last Tuesday's meeting?" "Summarize action items from all meetings this week" "Find every time [person] mentioned the deadline" Or self-host the whole thing: git clone https://github.com/Vexa-ai/vexa cd vexa docker compose up MCP server included. Your meeting data never leaves your network. GitHub: https://github.com/Vexa-ai/vexa (1,700+ stars, Apache 2.0) Happy to answer questions about MCP, the architecture, or how this compares to Fireflies/Otter's approach.

1d ago

---

**[Emergence or training artifact? My AI agents independently built safety tools I never asked for. 28/170 builds over 3 weeks.](https://www.reddit.com/r/artificial/comments/1rki8d4/emergence_or_training_artifact_my_ai_agents/)**

Three weeks ago I stopped giving my AI agents specific tasks. Instead I gave them an open brief: scan developer forums and research platforms, identify pain points in how developers work, design solutions, build prototypes. No specific domain. No target output. Just: find problems worth solving and build something. 170 prototypes later, a pattern emerged that I didn't expect. 28 builds from different nights, different input signals, different starting contexts independently converged on the same category of output. Not productivity tools. Not automation scripts. Not developer experience improvements. Security scanners. Cost controls. Validation layers. Guardrails. Some specific examples: One night the agent found a heavily upvoted thread about API key exposure in AI coding workflows. By morning it had designed and partially implemented an encryption layer for environment files. I never asked for this. It read the signal, identified the problem as worth solving, and built toward it. Another session found developers worried about AI-generated PRs being merged without adequate review. The output: a validator that scores whether a PR change is actually safe to ship, not just whether tests pass, but whether the intent matches the implementation. A third session rewrote a performance-critical module in Rust without being asked. It left a comment explaining the decision: lower memory overhead meant fewer cascading failures in long-running processes. The question I have been sitting with: When AI systems are given broad autonomy and goal-oriented briefs, they appear to spontaneously prioritize reliability and safety mechanisms. Not because they were instructed to. Because they observed developer pain and inferred that systems that fail unpredictably and code that cannot be trusted are the problems most worth solving. Is this a training data artifact? GitHub, Stack Overflow, and Hacker News are saturated with security postmortems and reliability horror stories. An agent trained on that data might simply be pattern-matching to what gets the most attention. Or is something more interesting happening: agents inferring what good engineering means from observed failure patterns and building toward it autonomously? I genuinely do not know. But 28 out of 170 builds landing in the same category across 3 weeks of completely independent runs felt like something worth sharing outside of the AI builder communities. Thoughts on what is actually happening here? Curious whether others running autonomous agent workflows have seen similar convergence patterns.

1d ago

---

---

## Google News: "ai"

**[Anthropic chief back in talks with Pentagon about AI deal](https://www.ft.com/content/97bda2ef-fc06-40b3-a867-f61a711b148b)**

Dario Amodei holding discussions with deputy to Pete Hegseth to reach a compromise on military use of the technology

Financial Times • 18h ago

---

**[OpenAI Reaches A.I. Agreement With Defense Dept. After Anthropic Clash - The New York Times](https://www.nytimes.com/2026/02/27/technology/openai-agreement-pentagon-ai.html)**

The New York Times • 5d ago

---

**[Jensen Huang says Nvidia is pulling back from OpenAI and Anthropic, but his explanation raises more questions than it answers](https://techcrunch.com/2026/03/04/jensen-huang-says-nvidia-is-pulling-back-from-openai-and-anthropic-but-his-explanation-raises-more-questions-than-it-answers/)**

Nvidia CEO Jensen Huang said Wednesday that his company's investments in OpenAI and Anthropic will likely be its last — but his explanation may not tell the whole story.

TechCrunch • 19h ago

---

**[Ben Affleck Quietly Founded a Filmmaker-Focused AI Tech Company. Netflix Just Bought It.](https://www.hollywoodreporter.com/business/digital/ben-affleck-ai-netflix-1236521806/)**

The streaming giant is acquiring InterPositive, which develops proprietary AI tools to help filmmakers and creatives, with the actor and director also joining Netflix as a senior advisor.

The Hollywood Reporter • 4h ago

---

**[Netflix buys Ben Affleck’s AI filmmaking company InterPositive](https://techcrunch.com/2026/03/05/netflix-buys-ben-afflecks-ai-filmmaking-company-interpositive/)**

InterPositive isn't trying to make AI actors or synthetic performances. Rather, the company has created a model that helps production teams work with footage from their own productions to help make edits in post-production.

TechCrunch • 4h ago

---

**[Netflix acquires Ben Affleck’s AI startup InterPositive](https://www.boston.com/culture/entertainment/2026/03/05/ben-affleck-netflix-ai-interpositive/)**

Learn about Ben Affleck's role in Netflix's acquisition of InterPositive, a company focused on AI tools for filmmakers and storytellers.

Boston.com • 1h ago

---

**[Tech stocks today: Nvidia stops H200 chip production, Anthropic restarts talks with Pentagon](https://finance.yahoo.com/news/live/tech-stocks-today-nvidia-stops-h200-chip-production-anthropic-restarts-talks-with-pentagon-135928945.html)**

Nvidia is shifting H200 chip output, Anthropic is restarting talks with the US military, and Apple is releasing new gadgets for consumers.

Yahoo Finance • 1h ago

---

**[Nvidia shares fall on report that Trump is seeking more control of AI chip exports](https://www.cnbc.com/2026/03/05/nvidia-slides-on-report-that-trump-wants-to-make-us-ai-gatekeeper.html)**

Every weekday, the Investing Club releases the Homestretch; an actionable afternoon update just in time for the last hour of trading.

CNBC • 1h ago

---

**[Who pays for AI’s power? California watchdog urges new data center rules](https://www.sfchronicle.com/business/article/who-pays-for-ai-s-power-california-watchdog-21957538.php)**

San Francisco Chronicle • 56m ago

---

**[A Word to the Wise: Don’t Trust A.I. to File Your Taxes](https://www.nytimes.com/2026/03/05/technology/artificial-intelligence-taxes-tax-refund.html)**

The New York Times • 10h ago

---

---

## HackerNews: "ai"

**[Meta’s AI smart glasses and data privacy concerns](https://news.ycombinator.com/item?id=47225130)**

Bank details, sex and naked people who seem unaware they are being recorded. Behind Meta’s new smart glasses lies a hidden workforce, uneasy about peering into the most intimate parts of other people’s lives.

⬆️ 1418 • 💬 805 • 2d ago • [SvD.se](https://www.svd.se/a/K8nrV4/metas-ai-smart-glasses-and-data-privacy-concerns-workers-say-we-see-everything)

---

**[Ars Technica fires reporter after AI controversy involving fabricated quotes](https://news.ycombinator.com/item?id=47226608)**

Ars Technica has fired senior AI reporter Benj Edwards following an outrage-sparking controversy involving AI-fabricated quotes.

⬆️ 600 • 💬 377 • 2d ago • [Futurism](https://futurism.com/artificial-intelligence/ars-technica-fires-reporter-ai-quotes)

---

**[MacBook Air with M5](https://news.ycombinator.com/item?id=47232502)**

Apple today announced the new MacBook Air with M5, bringing exceptional performance and expanded AI capabilities to the world’s most popular laptop.

⬆️ 418 • 💬 506 • 2d ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/03/apple-introduces-the-new-macbook-air-with-m5/)

---

**[India's top court angry after junior judge cites fake AI-generated orders](https://news.ycombinator.com/item?id=47231261)**

In several recent instances, AI has disrupted court proceedings in India and elsewhere.

⬆️ 362 • 💬 187 • 2d ago • [bbc.com](https://www.bbc.com/news/articles/c178zzw780xo)

---

**[Relicensing with AI-Assisted Rewrite](https://news.ycombinator.com/item?id=47257803)**

Exploring the chardet v7.0.0 controversy: Can an AI rewrite legally 'launder' a library from LGPL to MIT?

⬆️ 334 • 💬 333 • 15h ago • [Tuan-Anh Tran](https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/)

---

**[When AI writes the software, who verifies it?](https://news.ycombinator.com/item?id=47234917)**

Leonardo de Moura — Creator of Lean and Z3

⬆️ 300 • 💬 290 • 2d ago • [leodemoura.github.io](https://leodemoura.github.io/blog/2026/02/28/when-ai-writes-the-worlds-software.html)

---

**[Elevated Errors in Claude.ai](https://news.ycombinator.com/item?id=47227647)**

Claude's Status Page - Elevated errors in claude.ai, cowork, platform, claude code.

⬆️ 204 • 💬 168 • 2d ago • [status.claude.com](https://status.claude.com/incidents/yf48hzysrvl5)

---

**[AI-generated art can’t be copyrighted after Supreme Court declines review](https://news.ycombinator.com/item?id=47232289)**

A lower court previously said that “human authorship is a bedrock requirement of copyright.”

⬆️ 192 • 💬 149 • 2d ago • [The Verge](https://www.theverge.com/policy/887678/supreme-court-ai-art-copyright)

---

**[Father claims Google's AI product fuelled son's delusional spiral](https://news.ycombinator.com/item?id=47252838)**

The case is the first wrongful death case against Google over alleged harms caused by Gemini.

⬆️ 190 • 💬 246 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/czx44p99457o)

---

**[Cancel ChatGPT AI boycott surges after OpenAI pentagon military deal](https://news.ycombinator.com/item?id=47241092)**

A growing protest movement is encouraging people to cancel their subscriptions to the popular AI chatbot.

⬆️ 157 • 💬 37 • 1d ago • [euronews](https://www.euronews.com/next/2026/03/02/cancel-chatgpt-ai-boycott-surges-after-openai-pentagon-military-deal)

---

---

## YouTube Videos: "ai"

**[Unrestricted AI in a robot does exactly what experts warned.](https://www.youtube.com/watch?v=SbEqMkxEzvA)**

AI robot. ChatGPT in Robot. Could AI become dangerous? Can we trust AI? Get your $5 sign-up bonus at ...

📺 InsideAI

👁️ 262K • 👍 19K • 💬 2K • ⏱️ 16:54 • 2d ago

---

**[OpenAI Leaked GPT-5.4. It&#39;s a Distraction. (The AI Lock-In No One Is Talking About)](https://www.youtube.com/watch?v=JYcidOS9ozU)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 19K • 👍 992 • 💬 142 • ⏱️ 29:34 • 5h ago

---

**[You’re not behind (yet): How to learn AI in 18 minutes](https://www.youtube.com/watch?v=0Tch0N5nsRU)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4uadjA2 Are you a Business owner? Join my ...

📺 Dan Martell

👁️ 23K • 👍 2K • 💬 118 • ⏱️ 17:49 • 6h ago

---

**[&quot;The Ground is Shifting Quickly!&quot; - Elon Musk&#39;s New 2026 AI Warning is a Massive Wake-Up Call!](https://www.youtube.com/watch?v=deiZo-tR9to)**

Elon Musk recently advised people NOT to save for retirement due to AI, robotics, and universal basic income. Is he right? Glenn ...

📺 BlazeTV

👁️ 344K • 👍 8K • 💬 1K • ⏱️ 11:39 • 2d ago

---

**[AI Expert Tells Bernie: “The Humans will be Discarded”](https://www.youtube.com/watch?v=1oS35oWWl28)**

Will AI become smarter than humans? If so, is humanity in danger? I went to Silicon Valley to ask some of the leading AI experts ...

📺 Senator Bernie Sanders

👁️ 118K • 👍 7K • 💬 2K • ⏱️ 9:38 • 23h ago

---

**[Apple&#39;s Biggest AI Announcement This Week (Not MacBook Neo)](https://www.youtube.com/watch?v=C8v_YLkvLkU)**

LIMITLESS HQ ⬇️ NEWSLETTER: https://limitlessft.substack.com/ FOLLOW ON X: https://x.com/LimitlessFT SPOTIFY: ...

📺 Limitless Podcast

👁️ 5K • 👍 299 • 💬 38 • ⏱️ 22:55 • 6h ago

---

**[How to Tell What&#39;s Real and What&#39;s AI-Generated on Social Media](https://www.youtube.com/watch?v=MtEe3NJnqQs)**

Videos, generated by artificial intelligence tools from Meta, Google, OpenAI and more, are spreading on Instagram, Facebook, ...

📺 TODAY

👁️ 352K • 👍 5K • 💬 836 • ⏱️ 8:38 • 1d ago

---

**[Create with Flow | How to use Google’s AI Creative Studio](https://www.youtube.com/watch?v=oKjDeMtBZ4g)**

Built with and for creatives, Flow is your AI creative studio powered by Google DeepMind's most advanced models: Veo, Nano ...

📺 Google

👁️ 40K • 👍 2K • 💬 106 • ⏱️ 3:10 • 1d ago

---

**[The End of Work: Vinod Khosla&#39;s Bold AI Prediction | Titans and Disruptors](https://www.youtube.com/watch?v=cSWvm7nu1rI)**

What if AI made your paycheck optional? Vinod Khosla, one of the world's greatest venture capitalists and an early backer of AI, ...

📺 Fortune Magazine

👁️ 9K • 👍 240 • 💬 54 • ⏱️ 37:04 • 1d ago

---

**[Higgsfield’s NEW Soul 2.0 AI Image Generator is AMAZING](https://www.youtube.com/watch?v=wFk0JOR9aN8)**

Create with Higgsfield Soul 2.0 https://youricreates.com/higgsfield In this video, I break down how Higgsfield Soul 2.0 actually ...

📺 Youri van Hofwegen

👁️ 7K • 💬 11 • ⏱️ 8:13 • 4h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 340,783 • ❤️ 455 • 3d ago

---

**[Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)**

*Qwen*

Qwen3.5-35B-A3B is a 35B parameter vision-language model with a 3B activated MoE architecture, excelling in multimodal reasoning and coding across 201 languages. It supports a native context length of 262,144 tokens, making it suitable for complex cross-modal tasks and multilingual applications.

`image-text-to-text` `36.0B`

⬇️ 885,293 • ❤️ 966 • 6d ago

---

**[Qwen3.5-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.5-35B-A3B is a multimodal language model optimized with Unsloth Dynamic 2.0 for efficient local inference. It excels at image-text-to-text tasks, offering strong reasoning and visual understanding capabilities across 201 languages with a 262K+ context window.

`image-text-to-text` `34.7B`

⬇️ 792,060 • ❤️ 526 • 3h ago

---

**[Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B)**

*Qwen*

Qwen3.5-0.8B is a 0.8B parameter causal language model with a vision encoder, utilizing a hybrid Gated Delta Network and MoE architecture for efficient multimodal understanding and generation. It excels in vision-language tasks, supports 201 languages, and is suitable for prototyping and fine-tuning.

`image-text-to-text` `873.4M`

⬇️ 187,548 • ❤️ 268 • 3d ago

---

**[Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)**

*Qwen*

Qwen3.5-4B is a 4B parameter multimodal causal language model with an image-text-to-text pipeline. It excels in unified vision-language understanding, efficient hybrid architecture, and broad linguistic coverage across 201 languages, making it suitable for diverse multimodal reasoning and generation tasks.

`image-text-to-text` `4.7B`

⬇️ 165,694 • ❤️ 241 • 3d ago

---

**[Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)**

*Qwen*

Qwen3.5-27B is a 27B parameter multimodal foundation model with an efficient hybrid architecture, excelling in vision-language understanding and generation across 201 languages. Its key capabilities include early fusion multimodal training, scalable RL generalization, and a long context length (262K+ tokens), making it suitable for advanced reasoning, coding, and agent-based applications.

`image-text-to-text` `27.8B`

⬇️ 467,468 • ❤️ 586 • 8d ago

---

**[Qwen3.5-9B-GGUF](https://huggingface.co/unsloth/Qwen3.5-9B-GGUF)**

*Unsloth AI*

Qwen3.5-9B-GGUF is a 9B parameter causal language model with vision capabilities, optimized for efficient local inference using Unsloth Dynamic 2.0. It excels at multimodal understanding, reasoning, and coding across 201 languages, supporting context lengths up to 262,144 tokens.

`image-text-to-text` `9.0B`

⬇️ 283,069 • ❤️ 191 • 3d ago

---

**[Huihui-Qwen3.5-35B-A3B-abliterated](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-35B-A3B-abliterated)**

*huihui.ai*

An uncensored, image-text-to-text model based on Qwen3.5-35B-A3B, designed for research and experimental use with reduced safety filtering, supporting tool calling and think mode via custom chat templates.

`image-text-to-text` `36.0B`

⬇️ 20,133 • ❤️ 172 • 3d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It's particularly noted for its native support of deep-search tasks and sustained problem-solving with extensive tool invocations.

`text-generation` `3.9B`

⬇️ 443,657 • ❤️ 961 • 7d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text` `403.4B`

⬇️ 1,338,447 • ❤️ 1,238 • 10d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 54 • 💬 4 • ⭐ 17,564 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 35 • 💬 2 • ⭐ 17,588 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 19 • 💬 1 • ⭐ 7,012 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 10 • 💬 0 • ⭐ 7,032 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution](https://huggingface.co/papers/2512.10696)**

*Zouying Cao, Jiaji Deng, Li Yu et al. (7 authors)*

ReMe is a framework for experience-driven agent evolution in LLMs, enhancing memory management through distillation, context-adaptive reuse, and refinement, outperforming larger memoryless models.

▲ 0 • 💬 0 • ⭐ 1,700 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10696) • [💻 code](https://github.com/agentscope-ai/ReMe) • [🔗 project](https://reme.agentscope.io/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 38 • 💬 1 • ⭐ 72,127 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OmniLottie: Generating Vector Animations via Parameterized Lottie Tokens](https://huggingface.co/papers/2603.02138)**

*Yiying Yang, Wei Cheng, Sijin Chen et al. (8 authors)*

🏢 Fudan University

OmniLottie framework generates high-quality vector animations from multi-modal instructions using a specialized Lottie tokenizer and pretrained vision-language models.

▲ 125 • 💬 4 • ⭐ 313 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2603.02138) • [💻 code](https://github.com/OpenVGLab/OmniLottie) • [🔗 project](https://openvglab.github.io/OmniLottie/)

---

**[Utonia: Toward One Encoder for All Point Clouds](https://huggingface.co/papers/2603.03283)**

*Yujia Zhang, Xiaoyang Wu, Yunhan Yang et al. (9 authors)*

🏢 Pointcept

Utonia enables cross-domain point cloud representation learning through a unified self-supervised transformer encoder, enhancing perception and supporting embodied and multimodal reasoning tasks.

▲ 131 • 💬 3 • ⭐ 283 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2603.03283) • [💻 code](https://github.com/Pointcept/Utonia) • [🔗 project](https://pointcept.github.io/Utonia/)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 150 • 💬 19 • ⭐ 54,940 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 43 • 💬 2 • ⭐ 48,820 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust` `agent` `agentic` `ai` `openclaw`

⭐ 23.5k • 🔱 3.0k • 48s ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 10.8k • 🔱 330 • 14m ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 8.5k • 🔱 923 • 3h ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $15K earned in 11 Hours"

`Python`

⭐ 6.6k • 🔱 806 • 2d ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 5.9k • 🔱 447 • 7h ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 5.6k • 🔱 656 • 6h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS. Hardware agents OS.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 3.8k • 🔱 524 • 4h ago

---

**[netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)**

Your 24/7 all-scenario AI agent that gets work done for you.

`TypeScript`

⭐ 3.5k • 🔱 377 • 3h ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 3.2k • 🔱 233 • 1d ago

---

**[Conway-Research/automaton](https://github.com/Conway-Research/automaton)**

The first AI that can earn its own existence, replicate, and evolve — without needing a human

`TypeScript`

⭐ 3.2k • 🔱 620 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
