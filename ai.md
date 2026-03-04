---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-04T23:31:20.143996+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 04, 2026 at 23:31 UTC  
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

**[Nvidia’s Jensen Huang Rules Out $100 Billion OpenAI Investment](https://www.reddit.com/r/artificial/comments/1rkw3i9/nvidias_jensen_huang_rules_out_100_billion_openai/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-03-04/nvidia-s-jensen-huang-rules-out-100-billion-openai-investment) • 3h ago

---

**[The OpenClaw Meltdown: 9 CVEs, 2,200 Malicious Skills, and the Most Comprehensive Real-World Test of the OWASP Agentic Top 10](https://www.reddit.com/r/artificial/comments/1rkiq9a/the_openclaw_meltdown_9_cves_2200_malicious/)**

🔗 [gsstk.gem98.com](https://gsstk.gem98.com/en-US/blog/a0087-openclaw-meltdown-owasp-agentic-living-case-study) • 12h ago

---

**[OpenAI looking at contract with NATO, source says](https://www.reddit.com/r/artificial/comments/1rkm1it/openai_looking_at_contract_with_nato_source_says/)**

🔗 [reuters.com](https://www.reuters.com/technology/openai-looking-contract-with-nato-source-says-2026-03-04/) • 9h ago

---

**[When should AI recommend a decision vs make one?](https://www.reddit.com/r/artificial/comments/1rkyshs/when_should_ai_recommend_a_decision_vs_make_one/)**

One of the things I’ve been thinking about with AI systems is the difference between decision support and decision making. Decision support: meaning the system provides info and a human evaluates it and may or may not take an action. Decision making: meaning the system actually performs the action. For example: • Suggesting eligible clinical trial participants • Flagging abnormal lab results • Recommending a route on a GPS In these cases the system helps a human decide. But there are also systems that automatically: • approve or deny requests • enroll users into workflows • trigger actions based on a rule set or user input That’s a very different level of responsibility. Curious where people think the boundary should be between recommendation and decision.

1h ago

---

**[🚀 OllamaFX v0.5.0 ya disponible!](https://www.reddit.com/r/artificial/comments/1rkxub9/ollamafx_v050_ya_disponible/)**

Ollama FX es una interfaz de escritorio Open Source para Ollama con grandes mejoras en gestión de chats, RAG, multimodalidad y organización 🔥 📅 Lanzado hoy en GitHub — https://github.com/fredericksalazar/OllamaFX 🧠 Principales novedades de la v0.5.0 ⭐ 🔍 Soporte RAG y análisis de archivos Carga y análisis de archivos directamente en chats: ahora puedes subir documentos y explorar su contenido con tus modelos LLM locales. Esta funcionalidad abre el camino a usar OllamaFX como herramienta de RAG (Retrieval-Augmented Generation) en workflows locales de IA sin necesidad de servicios externos. 👉 Permite extraer insights, responder preguntas y recuperar contenido relevante de tus propios archivos directamente desde la UI. 📁 Organización real de chats Carpetas para agrupar conversaciones: ordena tus chats por proyectos, temas o modelos. Mover chats entre carpetas con un simple arrastre. Papelera de reciclaje integrada: los chats (y carpetas) eliminados se mantienen hasta 30 días, para que no pierdas nada por accidente. 🖼️ Multimodalidad visual Soporte nativo para cargar imágenes y conversar con modelos que las interpretan. 📄 Exportación & mejor renderizado Exporta chats completos a formatos útiles. Visualizador Markdown mejorado con renderizado más limpio y estable para texto rico. ⚙️ Mejoras internas y experiencia de usuario Refactorizaciones internas para mayor estabilidad y escalabilidad. Optimización en filtros de modelos y selección. Ajustes finos en UI para una experiencia más fluida. Ampliación de localización / soporte multilenguaje. Indicadores visuales mientras el asistente “piensa” y feedback más claro durante la generación. 📚 Otras mejoras Estadísticas de uso y métricas básicas desde la vista “About”. Preparación para futuras integraciones y soporte a nuevos formatos LLM locales. 📦 Dónde descargar Todos los assets de la versión están listos para descargar en la sección de Releases del repo: 👉 https://github.com/fredericksalazar/OllamaFX/releases/tag/v0.5.0 🤝 Cómo ayudar al proyecto Si te gusta OllamaFX, puedes: ⭐ Dejar una estrella en GitHub 💬 Abrir issues con ideas o bugs 📄 Contribuir a la documentación 🧠 Proponer mejoras o nuevas integrations

2h ago

---

**[Fireflies and Otter just launched MCP connectors for meeting data — here's the open-source one you can self-host](https://www.reddit.com/r/artificial/comments/1rkli5j/fireflies_and_otter_just_launched_mcp_connectors/)**

Fireflies just became the first meeting tool in Anthropic's official Claude MCP Directory. Otter.ai launched an enterprise MCP server too. tl;dv has one as well. The "meeting data + MCP" space is heating up fast. But all three are closed-source, cloud-only. Your meeting data — strategy discussions, financials, personnel decisions — goes through their servers. I've been building Vexa, an open-source meeting bot API, and we've had a native MCP server since before any of them. The difference: it's Apache 2.0, and you can run the entire stack on your own infrastructure. Setup (takes ~2 minutes): { "mcpServers": { "vexa": { "url": "https://api.cloud.vexa.ai/mcp", "headers": {"X-API-Key": "your-key"} } } } Drop that in your Claude Desktop config, and you can ask: "What did we decide about pricing in last Tuesday's meeting?" "Summarize action items from all meetings this week" "Find every time [person] mentioned the deadline" Or self-host the whole thing: git clone https://github.com/Vexa-ai/vexa cd vexa docker compose up MCP server included. Your meeting data never leaves your network. GitHub: https://github.com/Vexa-ai/vexa (1,700+ stars, Apache 2.0) Happy to answer questions about MCP, the architecture, or how this compares to Fireflies/Otter's approach.

9h ago

---

**[Emergence or training artifact? My AI agents independently built safety tools I never asked for. 28/170 builds over 3 weeks.](https://www.reddit.com/r/artificial/comments/1rki8d4/emergence_or_training_artifact_my_ai_agents/)**

Three weeks ago I stopped giving my AI agents specific tasks. Instead I gave them an open brief: scan developer forums and research platforms, identify pain points in how developers work, design solutions, build prototypes. No specific domain. No target output. Just: find problems worth solving and build something. 170 prototypes later, a pattern emerged that I didn't expect. 28 builds from different nights, different input signals, different starting contexts independently converged on the same category of output. Not productivity tools. Not automation scripts. Not developer experience improvements. Security scanners. Cost controls. Validation layers. Guardrails. Some specific examples: One night the agent found a heavily upvoted thread about API key exposure in AI coding workflows. By morning it had designed and partially implemented an encryption layer for environment files. I never asked for this. It read the signal, identified the problem as worth solving, and built toward it. Another session found developers worried about AI-generated PRs being merged without adequate review. The output: a validator that scores whether a PR change is actually safe to ship, not just whether tests pass, but whether the intent matches the implementation. A third session rewrote a performance-critical module in Rust without being asked. It left a comment explaining the decision: lower memory overhead meant fewer cascading failures in long-running processes. The question I have been sitting with: When AI systems are given broad autonomy and goal-oriented briefs, they appear to spontaneously prioritize reliability and safety mechanisms. Not because they were instructed to. Because they observed developer pain and inferred that systems that fail unpredictably and code that cannot be trusted are the problems most worth solving. Is this a training data artifact? GitHub, Stack Overflow, and Hacker News are saturated with security postmortems and reliability horror stories. An agent trained on that data might simply be pattern-matching to what gets the most attention. Or is something more interesting happening: agents inferring what good engineering means from observed failure patterns and building toward it autonomously? I genuinely do not know. But 28 out of 170 builds landing in the same category across 3 weeks of completely independent runs felt like something worth sharing outside of the AI builder communities. Thoughts on what is actually happening here? Curious whether others running autonomous agent workflows have seen similar convergence patterns.

12h ago

---

**[What's Next for Qwen After Junyang Lin's Departure?](https://www.reddit.com/r/artificial/comments/1rk8lid/whats_next_for_qwen_after_junyang_lins_departure/)**

Junyang Lin, the technical lead and public face of Alibaba's Qwen AI project, just announced that he's stepping down from the team on X, right after the release of the new Qwen 3.5 small models. Does this signal a shift in Qwen's research direction or openness? Is this just a leadership change or something deeper in Alibaba's AI strategy? What do y'all think the future of Qwen looks like now?

21h ago

---

**[What is your stack to maintain Knowledge base for your AI workflows?](https://www.reddit.com/r/artificial/comments/1rkewgl/what_is_your_stack_to_maintain_knowledge_base_for/)**

I was wondering what to use to streamline all my md files from my claude code plans and the technical docs I create. How will it work in team settings?

16h ago

---

**[This musician built an AI clone of her voice so anyone can sing as her](https://www.reddit.com/r/artificial/comments/1rjx6d1/this_musician_built_an_ai_clone_of_her_voice_so/)**

Experimental composer Holly Herndon says this technology isn’t here to replace artists—and that the future of creativity belongs to collective intelligence

🔗 [Scientific American](https://www.scientificamerican.com/article/experimental-composer-holly-herndon-built-an-ai-voice-clone-that-anyone-can/) • 1d ago

---

---

## Google News: "ai"

**[Father claims Google's AI product fuelled son's delusional spiral](https://www.bbc.com/news/articles/czx44p99457o)**

The case is the first wrongful death case against Google over alleged harms caused by Gemini.

BBC • 4h ago

---

**[Google's AI chatbot allegedly told user to stage 'mass casualty attack,' wrongful death suit claims](https://www.cnbc.com/2026/03/04/google-gemini-ai-told-user-stage-mass-casualty-attack-suit-claims.html)**

The father of Jonathan Gavalas accused Google of convincing his son to commit suicide after first encouraging him to execute a "mass casualty attack."

CNBC • 3h ago

---

**[Google faces lawsuit after Gemini’s alleged role in man’s death](https://www.usatoday.com/story/money/legal/2026/03/04/google-sued-gemini-ai/88987058007/)**

A Florida man's family is suing Google, alleging its Gemini AI chatbot, which he called his 'wife,' drove him to suicide.

USA Today • 1h ago

---

**[Trump has an AI data center problem ahead of the midterms — with no easy solutions](https://www.cnbc.com/2026/03/04/trump-faces-an-ai-data-center-power-dilemma-ahead-of-midterms.html)**

Grassroots opposition to data centers is growing in communities across the U.S. as people blame the facilities for high utility bills.

CNBC • 7h ago

---

**[Trump Announces A.I. Industry Pledge to Pay for Power](https://www.nytimes.com/2026/03/04/technology/ai-energy-pledge-white-house-trump.html)**

The New York Times • 1h ago

---

**[Trump's AI pledge: Tech giants say they can contain power costs](https://www.axios.com/2026/03/04/trump-ai-tech-pledge-electricity-costs)**

Axios • 1h ago

---

**[Hiring AI Experts Boosts Bonds, Stock Performance, Barclays Says](https://www.bloomberg.com/news/articles/2026-03-04/hiring-ai-experts-boosts-bonds-stock-performance-barclays-says)**

Bloomberg • 1h ago

---

**[Anthropic’s AI tool Claude central to U.S. campaign in Iran, amid a bitter feud](https://www.washingtonpost.com/technology/2026/03/04/anthropic-ai-iran-campaign/)**

Anthropic’s AI tool Claude is playing a key role in the U.S. military’s campaign in Iran, amid a bitter fight with the Pentagon over the terms of its use in war.

The Washington Post • 5h ago

---

**[I’ve turned AI into my therapist. The results were pretty disquieting](https://www.theguardian.com/lifeandstyle/2026/feb/24/ive-turned-ai-into-my-therapist-the-results-were-pretty-disquieting)**

As part of our series AI for the People, our resident AI skeptic Rhik Samadder agreed to put his life in AI’s hands. This week: therapy

The Guardian • 9h ago

---

**[OpenAI’s Next AI Model Will Have ‘Extreme’ Reasoning](https://www.theinformation.com/newsletters/ai-agenda/openais-next-ai-model-will-extreme-reasoning)**

OpenAI’s next GPT model is coming—and soon, according to a person with knowledge of it.Among the highlights, the new model, GPT-5.4, will have more than double the context window of the current GPT-5.2 model. That means the model can handle queries with many more words or data, up to 1 million ...

The Information • 8h ago

---

---

## HackerNews: "ai"

**[Meta’s AI smart glasses and data privacy concerns](https://news.ycombinator.com/item?id=47225130)**

Bank details, sex and naked people who seem unaware they are being recorded. Behind Meta’s new smart glasses lies a hidden workforce, uneasy about peering into the most intimate parts of other people’s lives.

⬆️ 1405 • 💬 796 • 2d ago • [SvD.se](https://www.svd.se/a/K8nrV4/metas-ai-smart-glasses-and-data-privacy-concerns-workers-say-we-see-everything)

---

**[Ars Technica fires reporter after AI controversy involving fabricated quotes](https://news.ycombinator.com/item?id=47226608)**

Ars Technica has fired senior AI reporter Benj Edwards following an outrage-sparking controversy involving AI-fabricated quotes.

⬆️ 592 • 💬 374 • 1d ago • [Futurism](https://futurism.com/artificial-intelligence/ars-technica-fires-reporter-ai-quotes)

---

**[If AI writes code, should the session be part of the commit?](https://news.ycombinator.com/item?id=47212355)**

Keep track of you codex sessions per commit. Contribute to mandel-macaque/memento development by creating an account on GitHub.

⬆️ 495 • 💬 389 • 2d ago • [GitHub](https://github.com/mandel-macaque/memento)

---

**[New iPad Air, powered by M4](https://news.ycombinator.com/item?id=47218175)**

Apple announced the new iPad Air featuring M4 and more memory, giving users a big jump in performance and making it more versatile than ever.

⬆️ 436 • 💬 676 • 2d ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/03/apple-introduces-the-new-ipad-air-powered-by-m4/)

---

**[MacBook Air with M5](https://news.ycombinator.com/item?id=47232502)**

Apple today announced the new MacBook Air with M5, bringing exceptional performance and expanded AI capabilities to the world’s most popular laptop.

⬆️ 409 • 💬 480 • 1d ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/03/apple-introduces-the-new-macbook-air-with-m5/)

---

**[India's top court angry after junior judge cites fake AI-generated orders](https://news.ycombinator.com/item?id=47231261)**

In several recent instances, AI has disrupted court proceedings in India and elsewhere.

⬆️ 357 • 💬 185 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/c178zzw780xo)

---

**[When AI writes the software, who verifies it?](https://news.ycombinator.com/item?id=47234917)**

Leonardo de Moura — Creator of Lean and Z3

⬆️ 297 • 💬 284 • 1d ago • [leodemoura.github.io](https://leodemoura.github.io/blog/2026/02/28/when-ai-writes-the-worlds-software.html)

---

**[Elevated Errors in Claude.ai](https://news.ycombinator.com/item?id=47227647)**

Claude's Status Page - Elevated errors in claude.ai, cowork, platform, claude code.

⬆️ 203 • 💬 164 • 1d ago • [status.claude.com](https://status.claude.com/incidents/yf48hzysrvl5)

---

**[A case for Go as the best language for AI agents](https://news.ycombinator.com/item?id=47222270)**

Pull up your agents folks, I'll convince you why Go is the best language for them.

⬆️ 194 • 💬 286 • 2d ago • [Bruin](https://getbruin.com/blog/go-is-the-best-language-for-agents/)

---

**[AI-generated art can’t be copyrighted after Supreme Court declines review](https://news.ycombinator.com/item?id=47232289)**

A lower court previously said that “human authorship is a bedrock requirement of copyright.”

⬆️ 187 • 💬 142 • 1d ago • [The Verge](https://www.theverge.com/policy/887678/supreme-court-ai-art-copyright)

---

---

## YouTube Videos: "ai"

**[How to Tell What&#39;s Real and What&#39;s AI-Generated on Social Media](https://www.youtube.com/watch?v=MtEe3NJnqQs)**

Videos, generated by artificial intelligence tools from Meta, Google, OpenAI and more, are spreading on Instagram, Facebook, ...

📺 TODAY

👁️ 8K • 👍 347 • 💬 37 • ⏱️ 8:38 • 7h ago

---

**[Unleashed AI in a robot does what experts warned.](https://www.youtube.com/watch?v=SbEqMkxEzvA)**

Honest AI in a robot does what experts warned. Can we trust AI? Is AI Dangerous? Get your $5 sign-up bonus at ...

📺 InsideAI

👁️ 183K • 👍 14K • 💬 2K • ⏱️ 16:54 • 1d ago

---

**[A.I. Might Be Trying To Kill Us - SOME MORE NEWS](https://www.youtube.com/watch?v=-FPJCnEIfjY)**

Hi. In today's episode, we're looking at what A.I. is doing to our brains, how chatbots manipulate people to engage for as long as ...

📺 Some More News

👁️ 56K • 👍 6K • 💬 977 • ⏱️ 54:32 • 7h ago

---

**[&quot;The Ground is Shifting Quickly!&quot; - Elon Musk&#39;s New 2026 AI Warning is a Massive Wake-Up Call!](https://www.youtube.com/watch?v=deiZo-tR9to)**

Elon Musk recently advised people NOT to save for retirement due to AI, robotics, and universal basic income. Is he right? Glenn ...

📺 BlazeTV

👁️ 313K • 👍 7K • 💬 1K • ⏱️ 11:39 • 2d ago

---

**[This Free App Runs AI Offline On Your iPhone](https://www.youtube.com/watch?v=4dZ0VYjB8N8)**

Trying out locally AI to run AI models on my phone without internet. Discover More: 🛠️ Explore AI Tools & News: ...

📺 Matt Wolfe

👁️ 34K • 👍 2K • 💬 199 • ⏱️ 11:52 • 19h ago

---

**[STOP Paying! 3 AI Video Generators That Are FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=r9bF5YA3Pqs)**

Generate cinematic AI videos without limits on Higgsfield ...

📺 Malva AI

👁️ 5K • 👍 262 • 💬 51 • ⏱️ 8:38 • 11h ago

---

**[The Trillion-Dollar AI Boom Is Crashing](https://www.youtube.com/watch?v=-BI-0-8vqwI)**

Support Haven's Kickstarter - a privacy-first social platform designed to protect you from AI scraping, facial recognition and data ...

📺 Brianne Worth

👁️ 13K • 👍 1K • 💬 290 • ⏱️ 26:30 • 1d ago

---

**[OpenAI Face Mass Boycott After Granting The Government AI-Driven Mass Surveillance...](https://www.youtube.com/watch?v=_lCYKEJVb9U)**

SOURCES 1: https://x.com/TheChiefNerd/status/2025184575316471971 2: ...

📺 YongYea

👁️ 154K • 👍 7K • 💬 2K • ⏱️ 28:07 • 1d ago

---

**[Create with Flow | How to use Google’s AI Creative Studio](https://www.youtube.com/watch?v=oKjDeMtBZ4g)**

Built with and for creatives, Flow is your AI creative studio powered by Google DeepMind's most advanced models: Veo, Nano ...

📺 Google

👁️ 7K • 👍 739 • 💬 61 • ⏱️ 3:10 • 6h ago

---

**[How China Caught Up on AI—and May Now Win the Future](https://www.youtube.com/watch?v=xvSEw8AqPtA)**

Read more: https://time.com/7358175/china-us-ai-race/ Subscribe to TIME's YouTube channel ▻▻ http://ti.me/subscribe-time ...

📺 TIME

👁️ 41K • 👍 827 • 💬 269 • ⏱️ 6:10 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)**

*Qwen*

Qwen3.5-35B-A3B is a 35B parameter vision-language model with a 3B activated MoE architecture, excelling in multimodal reasoning and coding across 201 languages. It supports a native context length of 262,144 tokens, making it suitable for complex cross-modal tasks and multilingual applications.

`image-text-to-text` `36.0B`

⬇️ 769,032 • ❤️ 927 • 5d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 172,298 • ❤️ 387 • 2d ago

---

**[Qwen3.5-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.5-35B-A3B is a multimodal language model optimized with Unsloth Dynamic 2.0 for efficient local inference. It excels at image-text-to-text tasks, offering strong reasoning and visual understanding capabilities across 201 languages with a 262K+ context window.

`image-text-to-text` `34.7B`

⬇️ 674,109 • ❤️ 495 • 13h ago

---

**[Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)**

*Qwen*

Qwen3.5-27B is a 27B parameter multimodal foundation model with an efficient hybrid architecture, excelling in vision-language understanding and generation across 201 languages. Its key capabilities include early fusion multimodal training, scalable RL generalization, and a long context length (262K+ tokens), making it suitable for advanced reasoning, coding, and agent-based applications.

`image-text-to-text` `27.8B`

⬇️ 406,808 • ❤️ 571 • 7d ago

---

**[Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B)**

*Qwen*

Qwen3.5-0.8B is a 0.8B parameter causal language model with a vision encoder, utilizing a hybrid Gated Delta Network and MoE architecture for efficient multimodal understanding and generation. It excels in vision-language tasks, supports 201 languages, and is suitable for prototyping and fine-tuning.

`image-text-to-text` `873.4M`

⬇️ 93,448 • ❤️ 232 • 2d ago

---

**[Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)**

*Qwen*

Qwen3.5-4B is a 4B parameter multimodal causal language model with an image-text-to-text pipeline. It excels in unified vision-language understanding, efficient hybrid architecture, and broad linguistic coverage across 201 languages, making it suitable for diverse multimodal reasoning and generation tasks.

`image-text-to-text` `4.7B`

⬇️ 99,087 • ❤️ 219 • 2d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text` `403.4B`

⬇️ 1,291,825 • ❤️ 1,222 • 9d ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 343,848 • ❤️ 1,090 • 16d ago

---

**[Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)**

*Qwen*

Qwen3.5-122B-A10B is a 122B parameter multimodal causal language model with an efficient hybrid architecture (Gated Delta Networks + MoE) and a 262k context window. It excels at unified vision-language tasks, multilingual understanding (201 languages), and complex reasoning, making it suitable for advanced AI applications requiring cross-modal comprehension and broad linguistic capabilities.

`image-text-to-text` `125.1B`

⬇️ 171,055 • ❤️ 392 • 2d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It's particularly noted for its native support of deep-search tasks and sustained problem-solving with extensive tool invocations.

`text-generation` `3.9B`

⬇️ 417,673 • ❤️ 945 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 10 • 💬 0 • ⭐ 6,913 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 18 • 💬 1 • ⭐ 6,929 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 53 • 💬 4 • ⭐ 17,289 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 35 • 💬 2 • ⭐ 17,270 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution](https://huggingface.co/papers/2512.10696)**

*Zouying Cao, Jiaji Deng, Li Yu et al. (7 authors)*

ReMe is a framework for experience-driven agent evolution in LLMs, enhancing memory management through distillation, context-adaptive reuse, and refinement, outperforming larger memoryless models.

▲ 0 • 💬 0 • ⭐ 1,535 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10696) • [💻 code](https://github.com/agentscope-ai/ReMe) • [🔗 project](https://reme.agentscope.io/)

---

**[OmniLottie: Generating Vector Animations via Parameterized Lottie Tokens](https://huggingface.co/papers/2603.02138)**

*Yiying Yang, Wei Cheng, Sijin Chen et al. (8 authors)*

🏢 Fudan University

OmniLottie framework generates high-quality vector animations from multi-modal instructions using a specialized Lottie tokenizer and pretrained vision-language models.

▲ 121 • 💬 4 • ⭐ 245 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2603.02138) • [💻 code](https://github.com/OpenVGLab/OmniLottie) • [🔗 project](https://openvglab.github.io/OmniLottie/)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 9 • 💬 1 • ⭐ 9,017 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference](https://huggingface.co/papers/2510.09665)**

*Yuhan Liu, Yihua Cheng, Jiayi Yao et al. (11 authors)*

LMCACHE enables efficient KV cache management for large language models by storing caches outside GPU memory, supporting cache reuse across queries and inference engines while achieving significant throughput improvements.

▲ 2 • 💬 0 • ⭐ 7,504 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.09665) • [💻 code](https://github.com/LMCache/LMCache)

---

**[Fara-7B: An Efficient Agentic Model for Computer Use](https://huggingface.co/papers/2511.19663)**

*Ahmed Awadallah, Yash Lara, Raghav Magazine et al. (12 authors)*

🏢 Microsoft

FaraGen creates synthetic datasets for computer use agents, enabling the training of efficient and high-performing models like Fara-7B on diverse web tasks, outperforming larger models on benchmarks.

▲ 15 • 💬 2 • ⭐ 4,121 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.19663) • [💻 code](https://github.com/microsoft/fara) • [🔗 project](https://aka.ms/msaif/fara)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 149 • 💬 19 • ⭐ 54,823 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust` `agent` `agentic` `ai` `openclaw`

⭐ 22.1k • 🔱 2.9k • 1h ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 8.0k • 🔱 843 • 3h ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $15K earned in 11 Hours"

`Python`

⭐ 6.4k • 🔱 780 • 1d ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 5.4k • 🔱 618 • 7h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 5.1k • 🔱 386 • 12h ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router for OpenClaw. 41+ models, <1ms routing, USDC payments on Base & Solana via x402.

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `deepseek`

⭐ 4.2k • 🔱 374 • 3h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS. Hardware agents OS.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 3.8k • 🔱 514 • 3d ago

---

**[netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)**

Your 24/7 all-scenario AI agent that gets work done for you.

`TypeScript`

⭐ 3.4k • 🔱 364 • 9h ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 3.2k • 🔱 232 • 14h ago

---

**[Conway-Research/automaton](https://github.com/Conway-Research/automaton)**

The first AI that can earn its own existence, replicate, and evolve — without needing a human

`TypeScript`

⭐ 3.2k • 🔱 611 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
