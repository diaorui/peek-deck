---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-05T11:34:40.579350+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 05, 2026 at 11:34 UTC  
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

🔗 [Ars Technica](https://arstechnica.com/security/2026/03/llms-can-unmask-pseudonymous-users-at-scale-with-surprising-accuracy/) • 8h ago

---

**[Large genome model: Open source AI trained on trillions of bases](https://www.reddit.com/r/artificial/comments/1rlegdl/large_genome_model_open_source_ai_trained_on/)**

"...Evo 2, an open source AI that has been trained on genomes from all three domains of life (bacteria, archaea, and eukaryotes). After training on trillions of base pairs of DNA, Evo 2 developed internal representations of key features in even complex genomes like ours, including things like regulatory DNA and splice sites, which can be challenging for humans to spot. Bacterial genomes are organized along relatively straightforward principles. Any genes that encode proteins or RNAs are contiguous, with no interruptions in the coding sequence. Genes that perform related functions, like metabolizing a sugar or producing an amino acid, tend to be clustered together, allowing them to be controlled by a single, compact regulatory system. It’s all straightforward and efficient. Eukaryotes are not like that. The coding sections of genes are interrupted by introns, which don’t encode for anything. They’re regulated by a sequence that can be scattered across hundreds of thousands of base pairs. The sequences that define the edges of introns or the binding sites of regulatory proteins are all weakly defined—while they have a few bases that are absolutely required, there are a lot of bases that just have an above-average tendency to have a specific base (something like “45 percent of the time it’s a T”). Surrounding all of this in most eukaryotic genomes is a huge amount of DNA that has been termed junk: inactive viruses, terminally damaged genes, and so on. That complexity has made eukaryotic genomes more difficult to interpret. And, while a lot of specialized tools have been developed to identify things like splice sites, they’re all sufficiently error-prone that it becomes a problem when you’re analyzing something as large as a 3 billion-base-long genome. We can learn a lot more by making evolutionary comparisons and looking for sequences that have been conserved, but there are limits to that, and we’re often as interested in the differences between species. These sorts of statistical probabilities, however, are well-suited to neural networks, which are great at recognizing subtle patterns that can be impossible to pick out by eye. But you’d need absolutely massive amounts of data and computing time to process it and pick out some of these subtle features. We now have the raw genome data that the process needs. Putting together a system to feed it into an effective AI training program, however, remained a challenge. That’s the challenge the team behind Evo took on. The foundation of the Evo 2 system is a convolutional neural network called StripedHyena 2. The training took place in two stages. The initial stage focused on teaching the system to identify important genome features by feeding it sequences rich in them in chunks about 8,000 bases long. After that, there was a second stage in which sequences were fed a million bases at a time to provide the system the opportunity to identify large-scale genome features. The researchers trained two versions of their system using a dataset called OpenGenome2, which contains 8.8 trillion bases from all three domains of life, as well as viruses that infect bacteria. They did not include viruses that attack eukaryotes, given that they were concerned that the system could be misused to create threats to humans. Two versions were trained: one that had 7 billion parameters tuned using 2.4 trillion bases, and the full version with 40 billion parameters trained on the full open genome dataset. The logic behind the training is pretty simple: if something’s important enough to have been evolutionarily conserved across a lot of species, it will show up in multiple contexts, and the system should see it repeatedly during training. “By learning the likelihood of sequences across vast evolutionary datasets, biological sequence models capture conserved sequence patterns that often reflect functional importance,” the researchers behind the work write. “These constraints allow the models to perform zero-shot prediction without any task-specific fine-tuning or supervision.” That last aspect is important. We could, for example, tell it about what known splice sites look like, which might help it pick out additional ones. But that might make it harder for it to recognize any unusual splice sites that we haven’t recognized yet. Skipping the fine-tuning might also help it identify genome features that we’re not aware of at all at the moment, but which could become apparent through future research. All of this has now been made available to the public. “We have made Evo 2 fully open, including model parameters, training code, inference code, and the OpenGenome2 dataset,” the paper announces. The researchers also used a system that can identify internal features in neural networks to poke around inside of Evo 2 and figure out what things it had learned to recognize. They trained a separate neural network to recognize the firing patterns in Evo 2 and identify high-level features in it. It clearly recognized protein-coding regions and the boundaries of the introns that flanked them. It was also able to recognize some structural features of proteins within the coding regions (alpha helices and beta sheets), as well as mutations that disrupt their coding sequence. Even something like mobile genetic elements (which you can think of as DNA-level parasites) ended up with a feature within Evo 2. To test the system, the researchers started making single-base mutations and fed them into Evo 2 to see how it responded. Evo 2 could detect problems when the mutations affected the sites in DNA where transcription into RNA started, or the sites where translation of that RNA into protein started. It also recognized the severity of mutations. Those that would interrupt protein translation, such as the introduction of stop signals, were identified as more significant changes than those that left the translation intact. It also recognized when sequences weren’t translated at all. Many key cellular functions are carried out directly by RNAs, and Evo 2 was able to recognize when mutations disrupted those, as well. Impressively, the ability to recognize features in eukaryotic genomes occurred without the loss of its ability to recognize them in bacteria and archaea. In fact, the system seemed to be able to work out what species it was working in. A number of evolutionary groups use genetic codes with a different set of signals to stop the translation of proteins. Evo 2 was able to recognize when it was looking at a sequence from one of those species, and used the correct genetic code for them. It was also good at recognizing features that tolerate a lot of variability, such as sites that signal where to splice RNAs to remove introns from the coding sequence of proteins. By some measures, it was better than software specialized for that task. The same was true when evaluating mutations in the BRCA2 gene, where many of the mutations are associated with cancer. Given additional training on known BRCA2 mutations, its performance improved further. Overall, Evo 2 seems great for evaluating genomes and identifying key features. The researchers who built it suggest it could serve as a good automated tool for preliminary genome annotation."

🔗 [Ars Technica](https://arstechnica.com/science/2026/03/large-genome-model-open-source-ai-trained-on-trillions-of-bases/) • 48m ago

---

**[Nvidia’s Jensen Huang Rules Out $100 Billion OpenAI Investment](https://www.reddit.com/r/artificial/comments/1rkw3i9/nvidias_jensen_huang_rules_out_100_billion_openai/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-03-04/nvidia-s-jensen-huang-rules-out-100-billion-openai-investment) • 15h ago

---

**[AMD engineer leverages AI to help make a pure-Python AMD GPU user-space driver](https://www.reddit.com/r/artificial/comments/1rl27ei/amd_engineer_leverages_ai_to_help_make_a/)**

AMD's VP of AI Software, Anush Elangovan, has used Claude Code to help craft a pure-Python AMD GPU user-space driver

🔗 [phoronix.com](https://www.phoronix.com/news/AI-Pure-Python-AMD-GPU-Driver) • 11h ago

---

**[Apple Music is building tools to identify and tag AI-generated songs](https://www.reddit.com/r/artificial/comments/1rl61te/apple_music_is_building_tools_to_identify_and_tag/)**

Apple is deploying new detection tools to identify and label AI-generated tracks across its streaming platform. The move aims to protect artist royalties and ensure transparency as "fake" songs increasingly flood the charts. This infrastructure shift allows Apple to verify human-made content while keeping its library legally compliant. By stripping away deceptive synthetic audio, the company is reinforcing the premium value of human creativity. Apple is drawing a digital line in the sand to stop the AI dilution of the music industry.

8h ago

---

**[The OpenClaw Meltdown: 9 CVEs, 2,200 Malicious Skills, and the Most Comprehensive Real-World Test of the OWASP Agentic Top 10](https://www.reddit.com/r/artificial/comments/1rkiq9a/the_openclaw_meltdown_9_cves_2200_malicious/)**

🔗 [gsstk.gem98.com](https://gsstk.gem98.com/en-US/blog/a0087-openclaw-meltdown-owasp-agentic-living-case-study) • 1d ago

---

**[OpenAI looking at contract with NATO, source says](https://www.reddit.com/r/artificial/comments/1rkm1it/openai_looking_at_contract_with_nato_source_says/)**

🔗 [reuters.com](https://www.reuters.com/technology/openai-looking-contract-with-nato-source-says-2026-03-04/) • 21h ago

---

**[When should AI recommend a decision vs make one?](https://www.reddit.com/r/artificial/comments/1rkyshs/when_should_ai_recommend_a_decision_vs_make_one/)**

One of the things I’ve been thinking about with AI systems is the difference between decision support and decision making. Decision support: meaning the system provides info and a human evaluates it and may or may not take an action. Decision making: meaning the system actually performs the action. For example: • Suggesting eligible clinical trial participants • Flagging abnormal lab results • Recommending a route on a GPS In these cases the system helps a human decide. But there are also systems that automatically: • approve or deny requests • enroll users into workflows • trigger actions based on a rule set or user input That’s a very different level of responsibility. Curious where people think the boundary should be between recommendation and decision.

13h ago

---

**[🚀 OllamaFX v0.5.0 ya disponible!](https://www.reddit.com/r/artificial/comments/1rkxub9/ollamafx_v050_ya_disponible/)**

Ollama FX es una interfaz de escritorio Open Source para Ollama con grandes mejoras en gestión de chats, RAG, multimodalidad y organización 🔥 📅 Lanzado hoy en GitHub — https://github.com/fredericksalazar/OllamaFX 🧠 Principales novedades de la v0.5.0 ⭐ 🔍 Soporte RAG y análisis de archivos Carga y análisis de archivos directamente en chats: ahora puedes subir documentos y explorar su contenido con tus modelos LLM locales. Esta funcionalidad abre el camino a usar OllamaFX como herramienta de RAG (Retrieval-Augmented Generation) en workflows locales de IA sin necesidad de servicios externos. 👉 Permite extraer insights, responder preguntas y recuperar contenido relevante de tus propios archivos directamente desde la UI. 📁 Organización real de chats Carpetas para agrupar conversaciones: ordena tus chats por proyectos, temas o modelos. Mover chats entre carpetas con un simple arrastre. Papelera de reciclaje integrada: los chats (y carpetas) eliminados se mantienen hasta 30 días, para que no pierdas nada por accidente. 🖼️ Multimodalidad visual Soporte nativo para cargar imágenes y conversar con modelos que las interpretan. 📄 Exportación & mejor renderizado Exporta chats completos a formatos útiles. Visualizador Markdown mejorado con renderizado más limpio y estable para texto rico. ⚙️ Mejoras internas y experiencia de usuario Refactorizaciones internas para mayor estabilidad y escalabilidad. Optimización en filtros de modelos y selección. Ajustes finos en UI para una experiencia más fluida. Ampliación de localización / soporte multilenguaje. Indicadores visuales mientras el asistente “piensa” y feedback más claro durante la generación. 📚 Otras mejoras Estadísticas de uso y métricas básicas desde la vista “About”. Preparación para futuras integraciones y soporte a nuevos formatos LLM locales. 📦 Dónde descargar Todos los assets de la versión están listos para descargar en la sección de Releases del repo: 👉 https://github.com/fredericksalazar/OllamaFX/releases/tag/v0.5.0 🤝 Cómo ayudar al proyecto Si te gusta OllamaFX, puedes: ⭐ Dejar una estrella en GitHub 💬 Abrir issues con ideas o bugs 📄 Contribuir a la documentación 🧠 Proponer mejoras o nuevas integrations

14h ago

---

**[Fireflies and Otter just launched MCP connectors for meeting data — here's the open-source one you can self-host](https://www.reddit.com/r/artificial/comments/1rkli5j/fireflies_and_otter_just_launched_mcp_connectors/)**

Fireflies just became the first meeting tool in Anthropic's official Claude MCP Directory. Otter.ai launched an enterprise MCP server too. tl;dv has one as well. The "meeting data + MCP" space is heating up fast. But all three are closed-source, cloud-only. Your meeting data — strategy discussions, financials, personnel decisions — goes through their servers. I've been building Vexa, an open-source meeting bot API, and we've had a native MCP server since before any of them. The difference: it's Apache 2.0, and you can run the entire stack on your own infrastructure. Setup (takes ~2 minutes): { "mcpServers": { "vexa": { "url": "https://api.cloud.vexa.ai/mcp", "headers": {"X-API-Key": "your-key"} } } } Drop that in your Claude Desktop config, and you can ask: "What did we decide about pricing in last Tuesday's meeting?" "Summarize action items from all meetings this week" "Find every time [person] mentioned the deadline" Or self-host the whole thing: git clone https://github.com/Vexa-ai/vexa cd vexa docker compose up MCP server included. Your meeting data never leaves your network. GitHub: https://github.com/Vexa-ai/vexa (1,700+ stars, Apache 2.0) Happy to answer questions about MCP, the architecture, or how this compares to Fireflies/Otter's approach.

22h ago

---

---

## Google News: "ai"

**[Anthropic’s AI tool Claude central to U.S. campaign in Iran, amid a bitter feud](https://www.washingtonpost.com/technology/2026/03/04/anthropic-ai-iran-campaign/)**

Anthropic’s AI tool Claude is playing a key role in the U.S. military’s campaign in Iran, amid a bitter fight with the Pentagon over the terms of its use in war.

The Washington Post • 17h ago

---

**[Anthropic chief back in talks with Pentagon about AI deal](https://www.ft.com/content/97bda2ef-fc06-40b3-a867-f61a711b148b)**

Dario Amodei holding discussions with deputy to Pete Hegseth to reach a compromise on military use of the technology

Financial Times • 6h ago

---

**[The Pentagon-Anthropic feud is quietly obscuring the real fight over military AI](https://www.fastcompany.com/91502340/the-pentagon-anthropic-feud-is-quietly-obscuring-the-real-fight-over-military-ai)**

The fight over how the military can use large language models is narrowing the scope of an urgent debate.

Fast Company • 1h ago

---

**[Opinion | Your Job May Already Be in Jeopardy](https://www.nytimes.com/2026/03/05/opinion/ai-jobs-white-collar-apocalpyse.html)**

The New York Times • 1h ago

---

**[AI could revolutionize antibiotics — but the market is standing in the way](https://www.statnews.com/2026/03/05/antibiotic-resistance-why-ai-innovation-not-enough/)**

Economic reality and the persistent absence of funding stand in the way of using AI for antibiotic breakthroughs.

statnews.com • 1h ago

---

**[AI Agents Love to Hodl Bitcoin and Spend Stablecoins, Study Finds](https://gizmodo.com/ai-agents-love-to-hodl-bitcoin-and-spend-stablecoins-study-finds-2000729877)**

The preference for bitcoin as a long-term store of value was referred to as the most dominant response in the recent Bitcoin Policy Institute report at 79.1%.

Gizmodo • 1h ago

---

**[ICO writes to Meta over 'concerning' AI smart glasses report](https://www.bbc.com/news/articles/c0q33nvj0qpo)**

Videos, including of glasses-wearers using the toilet or having sex, are sometimes reviewed by a Kenya-based subcontractor.

BBC • 19h ago

---

**[Homebuyers have another thing to worry about. This time, it's 'housefishing.'](https://www.businessinsider.com/home-listing-ai-photos-housefishing-agents-buyers-2026-3)**

There's a fine line between helping a buyer imagine a home's potential and deceiving them with AI enhanced photos. Welcome to the "housefishing" era.

Business Insider • 18h ago

---

**[Broadcom beats on earnings and guidance as AI revenue doubles](https://www.cnbc.com/2026/03/04/broadcom-avgo-q1-earnings-report-2026.html)**

Broadcom's AI revenue jumped 106% as the company continues to be a big beneficiary of the boom in infrastructure spending.

CNBC • 17h ago

---

**[Broadcom Earnings Are the Latest to Try to Climb AI Wall of Fear](https://finance.yahoo.com/news/broadcom-earnings-latest-try-climb-114413855.html)**

The chipmaker’s shares are down about 23% from a December record, well underperforming the S&P 500 Index.  The selloff is part of investors’ broader rotation away from the largest technology companies due to fears about the sustainability of the hundreds of billions of dollars committed to developing artificial intelligence capabilities.  Broadcom, which is the seventh-most valuable company in the S&P 500 at $1.5 trillion, is a chipmaking partner with Alphabet Inc. and other AI giants, making it a beneficiary of that largesse.

Yahoo Finance • 16h ago

---

---

## HackerNews: "ai"

**[Meta’s AI smart glasses and data privacy concerns](https://news.ycombinator.com/item?id=47225130)**

Bank details, sex and naked people who seem unaware they are being recorded. Behind Meta’s new smart glasses lies a hidden workforce, uneasy about peering into the most intimate parts of other people’s lives.

⬆️ 1415 • 💬 803 • 2d ago • [SvD.se](https://www.svd.se/a/K8nrV4/metas-ai-smart-glasses-and-data-privacy-concerns-workers-say-we-see-everything)

---

**[Ars Technica fires reporter after AI controversy involving fabricated quotes](https://news.ycombinator.com/item?id=47226608)**

Ars Technica has fired senior AI reporter Benj Edwards following an outrage-sparking controversy involving AI-fabricated quotes.

⬆️ 599 • 💬 378 • 2d ago • [Futurism](https://futurism.com/artificial-intelligence/ars-technica-fires-reporter-ai-quotes)

---

**[New iPad Air, powered by M4](https://news.ycombinator.com/item?id=47218175)**

Apple announced the new iPad Air featuring M4 and more memory, giving users a big jump in performance and making it more versatile than ever.

⬆️ 436 • 💬 677 • 2d ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/03/apple-introduces-the-new-ipad-air-powered-by-m4/)

---

**[MacBook Air with M5](https://news.ycombinator.com/item?id=47232502)**

Apple today announced the new MacBook Air with M5, bringing exceptional performance and expanded AI capabilities to the world’s most popular laptop.

⬆️ 415 • 💬 500 • 1d ago • [Apple Newsroom](https://www.apple.com/newsroom/2026/03/apple-introduces-the-new-macbook-air-with-m5/)

---

**[India's top court angry after junior judge cites fake AI-generated orders](https://news.ycombinator.com/item?id=47231261)**

In several recent instances, AI has disrupted court proceedings in India and elsewhere.

⬆️ 362 • 💬 185 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/c178zzw780xo)

---

**[When AI writes the software, who verifies it?](https://news.ycombinator.com/item?id=47234917)**

Leonardo de Moura — Creator of Lean and Z3

⬆️ 299 • 💬 290 • 1d ago • [leodemoura.github.io](https://leodemoura.github.io/blog/2026/02/28/when-ai-writes-the-worlds-software.html)

---

**[Elevated Errors in Claude.ai](https://news.ycombinator.com/item?id=47227647)**

Claude's Status Page - Elevated errors in claude.ai, cowork, platform, claude code.

⬆️ 203 • 💬 168 • 2d ago • [status.claude.com](https://status.claude.com/incidents/yf48hzysrvl5)

---

**[A case for Go as the best language for AI agents](https://news.ycombinator.com/item?id=47222270)**

Pull up your agents folks, I'll convince you why Go is the best language for them.

⬆️ 195 • 💬 288 • 2d ago • [Bruin](https://getbruin.com/blog/go-is-the-best-language-for-agents/)

---

**[AI-generated art can’t be copyrighted after Supreme Court declines review](https://news.ycombinator.com/item?id=47232289)**

A lower court previously said that “human authorship is a bedrock requirement of copyright.”

⬆️ 188 • 💬 144 • 1d ago • [The Verge](https://www.theverge.com/policy/887678/supreme-court-ai-art-copyright)

---

**[Father claims Google's AI product fuelled son's delusional spiral](https://news.ycombinator.com/item?id=47252838)**

The case is the first wrongful death case against Google over alleged harms caused by Gemini.

⬆️ 182 • 💬 242 • 15h ago • [bbc.com](https://www.bbc.com/news/articles/czx44p99457o)

---

---

## YouTube Videos: "ai"

**[Jailbroken AI in a robot does what experts warned.](https://www.youtube.com/watch?v=SbEqMkxEzvA)**

Honest AI in a robot does what experts warned. Can we trust AI? Is AI Dangerous? Get your $5 sign-up bonus at ...

📺 InsideAI

👁️ 234K • 👍 16K • 💬 2K • ⏱️ 16:54 • 1d ago

---

**[&quot;The Ground is Shifting Quickly!&quot; - Elon Musk&#39;s New 2026 AI Warning is a Massive Wake-Up Call!](https://www.youtube.com/watch?v=deiZo-tR9to)**

Elon Musk recently advised people NOT to save for retirement due to AI, robotics, and universal basic income. Is he right? Glenn ...

📺 BlazeTV

👁️ 333K • 👍 7K • 💬 1K • ⏱️ 11:39 • 2d ago

---

**[AI Art Just Lost.](https://www.youtube.com/watch?v=yDecu_jNpZI)**

The Supreme Court of the United States of America has officially turned away a key case surrounding artificial intelligence art and ...

📺 Vailskibum

👁️ 245K • 👍 19K • 💬 4K • ⏱️ 2:09 • 15h ago

---

**[The FASTEST Way To Tell What&#39;s REAL vs AI](https://www.youtube.com/watch?v=vIJXfUy5cT4)**

World-renowned security expert Gavin de Becker explains why AI is making it nearly impossible to tell what is real and what is ...

📺 The Diary Of A CEO Clips

👁️ 20K • 👍 774 • 💬 50 • ⏱️ 21:25 • 16h ago

---

**[The Trillion-Dollar AI Boom Is Crashing](https://www.youtube.com/watch?v=-BI-0-8vqwI)**

Support Haven's Kickstarter - a privacy-first social platform designed to protect you from AI scraping, facial recognition and data ...

📺 Brianne Worth

👁️ 16K • 👍 1K • 💬 350 • ⏱️ 26:30 • 1d ago

---

**[The End of Work: Vinod Khosla&#39;s Bold AI Prediction | Titans and Disruptors](https://www.youtube.com/watch?v=cSWvm7nu1rI)**

What if AI made your paycheck optional? Vinod Khosla, one of the world's greatest venture capitalists and an early backer of AI, ...

📺 Fortune Magazine

👁️ 5K • 👍 151 • 💬 35 • ⏱️ 37:04 • 20h ago

---

**[STOP Paying! 3 AI Video Generators That Are FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=r9bF5YA3Pqs)**

Generate cinematic AI videos without limits on Higgsfield ...

📺 Malva AI

👁️ 11K • 👍 493 • 💬 74 • ⏱️ 8:38 • 23h ago

---

**[This Free App Runs AI Offline On Your iPhone](https://www.youtube.com/watch?v=4dZ0VYjB8N8)**

Trying out locally AI to run AI models on my phone without internet. Discover More: 🛠️ Explore AI Tools & News: ...

📺 Matt Wolfe

👁️ 40K • 👍 2K • 💬 222 • ⏱️ 11:52 • 1d ago

---

**[Create with Flow | How to use Google’s AI Creative Studio](https://www.youtube.com/watch?v=oKjDeMtBZ4g)**

Built with and for creatives, Flow is your AI creative studio powered by Google DeepMind's most advanced models: Veo, Nano ...

📺 Google

👁️ 24K • 👍 1K • 💬 93 • ⏱️ 3:10 • 18h ago

---

**[How China Caught Up on AI—and May Now Win the Future](https://www.youtube.com/watch?v=xvSEw8AqPtA)**

Read more: https://time.com/7358175/china-us-ai-race/ Subscribe to TIME's YouTube channel ▻▻ http://ti.me/subscribe-time ...

📺 TIME

👁️ 47K • 👍 923 • 💬 307 • ⏱️ 6:10 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)**

*Qwen*

Qwen3.5-35B-A3B is a 35B parameter vision-language model with a 3B activated MoE architecture, excelling in multimodal reasoning and coding across 201 languages. It supports a native context length of 262,144 tokens, making it suitable for complex cross-modal tasks and multilingual applications.

`image-text-to-text` `36.0B`

⬇️ 885,293 • ❤️ 949 • 6d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 340,783 • ❤️ 427 • 3d ago

---

**[Qwen3.5-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.5-35B-A3B is a multimodal language model optimized with Unsloth Dynamic 2.0 for efficient local inference. It excels at image-text-to-text tasks, offering strong reasoning and visual understanding capabilities across 201 languages with a 262K+ context window.

`image-text-to-text` `34.7B`

⬇️ 792,060 • ❤️ 509 • 1d ago

---

**[Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)**

*Qwen*

Qwen3.5-27B is a 27B parameter multimodal foundation model with an efficient hybrid architecture, excelling in vision-language understanding and generation across 201 languages. Its key capabilities include early fusion multimodal training, scalable RL generalization, and a long context length (262K+ tokens), making it suitable for advanced reasoning, coding, and agent-based applications.

`image-text-to-text` `27.8B`

⬇️ 467,468 • ❤️ 581 • 8d ago

---

**[Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B)**

*Qwen*

Qwen3.5-0.8B is a 0.8B parameter causal language model with a vision encoder, utilizing a hybrid Gated Delta Network and MoE architecture for efficient multimodal understanding and generation. It excels in vision-language tasks, supports 201 languages, and is suitable for prototyping and fine-tuning.

`image-text-to-text` `873.4M`

⬇️ 187,548 • ❤️ 249 • 3d ago

---

**[Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)**

*Qwen*

Qwen3.5-4B is a 4B parameter multimodal causal language model with an image-text-to-text pipeline. It excels in unified vision-language understanding, efficient hybrid architecture, and broad linguistic coverage across 201 languages, making it suitable for diverse multimodal reasoning and generation tasks.

`image-text-to-text` `4.7B`

⬇️ 165,694 • ❤️ 233 • 3d ago

---

**[Qwen3.5-9B-GGUF](https://huggingface.co/unsloth/Qwen3.5-9B-GGUF)**

*Unsloth AI*

Qwen3.5-9B-GGUF is a 9B parameter causal language model with vision capabilities, optimized for efficient local inference using Unsloth Dynamic 2.0. It excels at multimodal understanding, reasoning, and coding across 201 languages, supporting context lengths up to 262,144 tokens.

`image-text-to-text` `9.0B`

⬇️ 283,069 • ❤️ 173 • 2d ago

---

**[Huihui-Qwen3.5-35B-A3B-abliterated](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-35B-A3B-abliterated)**

*huihui.ai*

An uncensored, image-text-to-text model based on Qwen3.5-35B-A3B, designed for research and experimental use with reduced safety filtering, supporting tool calling and think mode via custom chat templates.

`image-text-to-text` `36.0B`

⬇️ 20,133 • ❤️ 163 • 3d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text` `403.4B`

⬇️ 1,338,447 • ❤️ 1,229 • 9d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It's particularly noted for its native support of deep-search tasks and sustained problem-solving with extensive tool invocations.

`text-generation` `3.9B`

⬇️ 443,657 • ❤️ 953 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 53 • 💬 4 • ⭐ 17,384 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 19 • 💬 1 • ⭐ 6,963 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 35 • 💬 2 • ⭐ 17,363 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 10 • 💬 0 • ⭐ 6,994 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution](https://huggingface.co/papers/2512.10696)**

*Zouying Cao, Jiaji Deng, Li Yu et al. (7 authors)*

ReMe is a framework for experience-driven agent evolution in LLMs, enhancing memory management through distillation, context-adaptive reuse, and refinement, outperforming larger memoryless models.

▲ 0 • 💬 0 • ⭐ 1,650 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10696) • [💻 code](https://github.com/agentscope-ai/ReMe) • [🔗 project](https://reme.agentscope.io/)

---

**[OmniLottie: Generating Vector Animations via Parameterized Lottie Tokens](https://huggingface.co/papers/2603.02138)**

*Yiying Yang, Wei Cheng, Sijin Chen et al. (8 authors)*

🏢 Fudan University

OmniLottie framework generates high-quality vector animations from multi-modal instructions using a specialized Lottie tokenizer and pretrained vision-language models.

▲ 124 • 💬 4 • ⭐ 281 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2603.02138) • [💻 code](https://github.com/OpenVGLab/OmniLottie) • [🔗 project](https://openvglab.github.io/OmniLottie/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 38 • 💬 1 • ⭐ 71,987 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Utonia: Toward One Encoder for All Point Clouds](https://huggingface.co/papers/2603.03283)**

*Yujia Zhang, Xiaoyang Wu, Yunhan Yang et al. (9 authors)*

🏢 Pointcept

Utonia enables cross-domain point cloud representation learning through a unified self-supervised transformer encoder, enhancing perception and supporting embodied and multimodal reasoning tasks.

▲ 127 • 💬 3 • ⭐ 231 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2603.03283) • [💻 code](https://github.com/Pointcept/Utonia) • [🔗 project](https://pointcept.github.io/Utonia/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 43 • 💬 2 • ⭐ 48,772 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 9 • 💬 1 • ⭐ 9,065 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust` `agent` `agentic` `ai` `openclaw`

⭐ 22.4k • 🔱 3.0k • 4h ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 8.4k • 🔱 887 • 1h ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $15K earned in 11 Hours"

`Python`

⭐ 6.5k • 🔱 796 • 1d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 6.5k • 🔱 177 • 2h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 5.6k • 🔱 423 • 2h ago

---

**[nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)**

Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

`Zig` `ai` `assistant` `personal` `zig`

⭐ 5.5k • 🔱 644 • 10h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS. Hardware agents OS.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 3.8k • 🔱 520 • 8h ago

---

**[netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)**

Your 24/7 all-scenario AI agent that gets work done for you.

`TypeScript`

⭐ 3.5k • 🔱 371 • 2h ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 3.2k • 🔱 232 • 1d ago

---

**[Conway-Research/automaton](https://github.com/Conway-Research/automaton)**

The first AI that can earn its own existence, replicate, and evolve — without needing a human

`TypeScript`

⭐ 3.2k • 🔱 617 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
