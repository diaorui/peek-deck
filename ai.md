---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-25T22:34:07.331348+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 25, 2026 at 22:34 UTC  
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

**[Uber's COO says it's getting harder to justify the money spent on AI tokenmaxxing](https://www.reddit.com/r/artificial/comments/1tndgv8/ubers_coo_says_its_getting_harder_to_justify_the/)**

Operations chief Andrew Macdonald said he's not seeing proportional productivity gains from increasing AI costs within Uber.

🔗 [Business Insider](https://www.businessinsider.com/uber-coo-andrew-macdonald-ai-token-spending-harder-justify-2026-5) • 6h ago

---

**[We're reaching a point where "AI-generated but visually realistic" content will become the norm, not the exception. 👀](https://www.reddit.com/r/artificial/comments/1tn3e7k/were_reaching_a_point_where_aigenerated_but/)**

We have entered the era of artificial general intelligence.

13h ago

---

**[AI agents need audit trails more than they need more autonomy](https://www.reddit.com/r/artificial/comments/1tnarvu/ai_agents_need_audit_trails_more_than_they_need/)**

A lot of people talk about AI agents like the main goal is making them more independent. But the more I think about it, the bigger issue is probably visibility. If an AI is only answering a question, it is easy to judge the result. But once it starts doing things across websites, accounts, forms, support systems, or emails, users need to know exactly what happened. What did it click. What did it submit. What did it ask. Where did it fail. When did it decide to continue, retry, or stop. Without that kind of audit trail, even a smart agent feels hard to trust. A small mistake can hide inside a long workflow, and by the time the user notices, the problem may already be messy. The next useful version of AI agents might not be the one that acts the most independently. It might be the one that makes every step clear enough that a normal user can trust what it did.

8h ago

---

**[Top 10 Fastest Growing AI repos this week](https://www.reddit.com/r/artificial/comments/1tnjhts/top_10_fastest_growing_ai_repos_this_week/)**

Curated this list of fastest growing AI repos. They are mostly AI coding agents, personal AI, memory, browser automation, Claude Skills and local-first dev tooling: colbymchenry/codegraph (+14.1K stars) Pre-indexed local code knowledge graph for Claude Code, Codex, Cursor, OpenCode, and Hermes Agent. tinyhumansai/openhuman (+17.1K stars) Personal AI / private AI superintelligence. Imbad0202/academic-research-skills (+11.6K stars) Claude Code skills for academic research workflows: research, write, review, revise, finalize. ruvnet/RuView (+6.8K stars) Turns commodity WiFi signals into spatial intelligence, presence detection, and vital sign monitoring. rohitg00/agentmemory (+6.9K stars) Persistent memory for AI coding agents based on real-world benchmarks. supertone-inc/supertonic (+3.6K stars) On-device multilingual TTS running natively via ONNX. CloakHQ/CloakBrowser (+7.0K stars) Stealth Chromium that passes bot detection tests with Playwright compatibility. HKUDS/ViMax (+2.7K stars) Agentic video generation: director, screenwriter, producer, and video generator in one. humanlayer/12-factor-agents (+1.9K stars) Principles for building production-grade LLM-powered software. Varnan-Tech/OpenDirectory (+250 stars) AI Agent Skills built for founders who hate marketing. All links in 1st comment 👇

2h ago

---

**[Cerebras Chip Sets Appear to be Optimized for LLM Use Cases](https://www.reddit.com/r/artificial/comments/1tnkwqi/cerebras_chip_sets_appear_to_be_optimized_for_llm/)**

One distinction I think is getting lost in the Cerebras hype cycle is that Cerebras is primarily an LLM / generative AI infrastructure story, not a universal “all AI” chip story. That is not necessarily a criticism of Cerebras. Their wafer-scale approach is genuinely interesting, and for large model training and inference the design is compelling. Cerebras’ own public inference materials discuss applications mostly centered on open LLMs such as Llama, Qwen, GLM, and GPT-OSS. The inference metrics are expressed in tokens per second, which is fundamentally a language-model / generative inference framing rather than a robotics or industrial-control framing. What Kind of AI Compute? But “AI compute” is not one undifferentiated market. LLM inference is one class of AI compute. Robotics, autonomous vehicles, drones, industrial controls, real-time vision, embedded perception, video pipelines, and sensor-fusion systems are very different classes of AI compute. Thus, it appears from Cerebras’ own materials that their chip sets are not optimized for what comes after LLMs, such as JEPA-style World Models or other post-transformer architectures. Those systems are not merely asking, “How fast can I generate tokens?” They often care about power envelope, edge deployment, ruggedization, latency determinism, camera/radar/lidar integration, feedback loops, safety certification, and real-time physical control. Cerebras’ own CS-3 messaging, by contrast, frames the system around accelerating “the latest large AI models,” and the testing data is from the likes of Llama 2, Falcon 40B, MPT-30B, and multimodal models, again measured through tokens/second style throughput. The Chip Hierarchy This is also where the hardware distinction matters. Specialized ASICs are usually the narrowest bet: if the workload matches the chip, they can be extremely efficient, but that efficiency comes from specialization. Cerebras appears broader than a narrow single-use ASIC, but still much more concentrated around datacenter large-model training and inference. NVIDIA GPUs, by contrast, are less specialized but much more broadly useful across AI workloads, including LLMs, vision, robotics, simulation, autonomous systems, edge AI, and industrial applications. So the question is not merely whether Cerebras is “better” or “worse” than NVIDIA. The question is what part of the AI hardware market we are talking about? Challenge NVIDA? This is why I think people should be careful when saying Cerebras is going to “challenge Nvidia” without specifying the battlefield. Challenge Nvidia in what? High-speed LLM inference? Large model training? Datacenter generative AI workloads? That is a much more plausible and specific claim. Cerebras has even published and promoted work specifically on training large language models, and independent benchmarking literature also evaluates Cerebras WSE in terms of LLM training and inference performance. The Distinction that's Necessary The point is not that Cerebras is overhyped. The point is that it is important in a specific part of AI and that distinction should be made clear. Cerebras may become a very serious player in LLM infrastructure, especially if the market continues to reward faster and cheaper LLM inference. But that does not mean it is positioned the same way across non-LLM AI. The current hype cycle tends to conflate "LLMs" and general “AI” compute together and that makes the hardware discussion less useful and clear. So ultimately, an investment in Cerebras looks more like a bet on current LLM infrastructure than a broad bet on the future form of AI. It may be a good bet, but people should understand what kind of bet it is.

2h ago

---

**[If you could subscribe to one AI provider who would it be?](https://www.reddit.com/r/artificial/comments/1tn73ve/if_you_could_subscribe_to_one_ai_provider_who/)**

Im pretty much looking for where to get the most for the least amount of money. But with so many providers and most not even clearly stating their usage limits things get confusing fast. Any of you have a tip?

10h ago

---

**[Wix cutting](https://www.reddit.com/r/artificial/comments/1tne1m4/wix_cutting/)**

Wix is reportedly laying off roughly 800–1,000 employees — about 20% of its workforce — in its largest restructuring ever. The interesting part isn’t just the layoffs. It’s what they reveal about the economics of AI-first software companies. Wix’s core business is still growing: • Revenue reportedly rose ~14% YoY in Q1 2026 • Bookings were up ~15% • New AI-driven cohorts showed even faster growth But growth alone no longer protects margins when AI infrastructure costs explode. The pressure points: • Heavy investment in Base44, the vibe-coding startup Wix acquired in 2025 • Building and running proprietary AI models • Massive compute/inference costs • Expensive customer acquisition and marketing campaigns • A controversial $1.6B share buyback executed before the downturn At the same time, investors are questioning whether traditional website builders are becoming commoditized by AI. The bigger story is “vibe coding.” Users can now describe an app or website in plain English: “Create a sleek portfolio site with dark mode, payments, and a booking form.” AI generates the product instantly. That changes the value chain. The old moat was: templates + drag-and-drop builders. The new moat is becoming: AI orchestration + hosting + payments + integrations + reliability + distribution. Wix understands this. Instead of resisting the shift, they’ve aggressively moved toward it: • Acquired Base44 • Launched Wix Harmony, an AI-native creation platform • Combined natural-language generation with traditional visual editing • Pushed deeper into AI infrastructure and automation The irony is that AI didn’t kill Wix’s market overnight. It forced Wix to reinvent what “website building” even means. Pure AI tools can generate impressive demos quickly. But production systems still require: • uptime • commerce infrastructure • SEO • analytics • security • scalability • customer support That’s where incumbents still have leverage. This looks less like “AI destroyed Wix” and more like: a profitable software company being forced through an AI-era reset where efficiency, infrastructure costs, and platform strategy suddenly matter more than headcount growth. The broader lesson: AI is compressing the value of interfaces while increasing the value of infrastructure and distribution. The companies that survive won’t necessarily be the ones with the best demos. They’ll be the ones that can combine: • AI generation • operational reliability • ecosystem lock-in • cost control • and real business workflows AI is making software creation easier. But it’s also making software businesses much harder to defend.

6h ago

---

**[Why is there a sudden demand for a bunch of data centers?](https://www.reddit.com/r/artificial/comments/1tndecr/why_is_there_a_sudden_demand_for_a_bunch_of_data/)**

I live in Pennsylvania, and in just the past year there’s been about a dozen data centers proposed within a 30 mile radius of me, all pretty large scale projects. I’m confused because we have a bunch of AI now that’s working without all these newly proposed data centers. I understand it continues to advance and grow, but why is there such a significant spike? Is there actually demand, or are these going to be mostly unused?

6h ago

---

**[Future Prediction](https://www.reddit.com/r/artificial/comments/1tnbcsg/future_prediction/)**

I have a prediction that companies laying off workers thinking they can be replaced by AI are going to have a mess on their hands in a couple years. Execs think AI can do employees’ jobs and in many cases it can’t. This thinking would be like laying off workers because computers were invented. Between the loss of institutional knowledge, quality/hallucination issues with AI and the need for human supervision I believe these layoffs are extremely short-sighted. Thoughts?

7h ago

---

**[Building Conifer, an open-source local inference runtime (free + open source)](https://www.reddit.com/r/artificial/comments/1tnnaa6/building_conifer_an_opensource_local_inference/)**

Team of 5 from Princeton, and we got funding to build a local inference engine for Apple Silicon - rust, hand written kernels - and we're at the point where working with ~100 people will expose bugs/what people want tool-wise. All of this is free open source - will remain so. We're ahead of llama/mlx for small models working on similar performance for larger in the long run. Where this is going: the engine we're building supports a fully local agent that can do real work on your own files, apps, has permissions with OS kernel enforcement. Asking for any feedback and if you're really interested we're opening up a waitlist and taking 100 people into free beta and working with them 1-on-1 to writing specific tools and performance engineering on setups (sign up at https://conifer.build/feedback). Please only do this if you imagine using this and have some idea in mind, we'll release a full version later this summer but we want to build around talent. We need real usage and unrestrained feedback from ppl who run local models. site is live at conifer.build. also drop anything you want to see or ideas. conifer.build/feedback if you want to drop comment anon

34m ago

---

---

## Google News: "ai"

**[Pope Leo Warns of Risks From A.I. in 42,300-Word Encyclical](https://www.nytimes.com/2026/05/25/world/europe/pope-leo-encyclical.html)**

The New York Times • 13h ago

---

**[Google clarifies its slightly confusing pair of AI Ultra plans](https://9to5google.com/2026/05/25/google-one-ai-ultra-clarification/)**

Following the introduction of a more affordable new tier, Google One’s AI Ultra plans have been a tiny bit confusing...

9to5Google • 49m ago

---

**[This big university system is embracing AI. Students and faculty aren't all on board](https://www.npr.org/2026/05/25/nx-s1-5772820/artificial-intelligence-education-technology-california-state-university)**

The California State University system offers an early look at what happens when an administration commits to a technology that its own community isn't convinced will improve education.

NPR • 13h ago

---

**[Pope Leo presents 'Magnifica humanitas’ calling for disarmament of AI](https://www.vaticannews.va/en/pope/news/2026-05/pope-leo-xiv-magnifica-humanitas-presentation-ai-disarmament.html)**

Pope Leo XIV presents "Magnifica Humanitas" as the Church’s response to the challenges posed by artificial intelligence, calling for AI to be ...

Vatican News • 11h ago

---

**[As A.I. Fever Rises in Silicon Valley, Pope Leo Has a Few Words](https://www.nytimes.com/2026/05/25/technology/pope-ai-silicon-valley.html)**

The New York Times • 7h ago

---

**[Pope says AI must be ‘disarmed’ to prevent domination, exclusion, and death](https://www.aljazeera.com/news/2026/5/25/pope-says-ai-must-be-disarmed-to-prevent-domination-exclusion-and-death)**

In his first encyclical, Leo insists ownership of artificial intelligence data must not be left solely in private hands.

Al Jazeera • 6h ago

---

**[Pope, urging AI regulation, warns some weapons now beyond human control](https://www.reuters.com/business/media-telecom/pope-leo-urges-world-slow-down-ai-fervent-first-manifesto-2026-05-25/)**

Reuters • 2h ago

---

**[Pope Leo calls to 'disarm' AI in major document, warns of technologic threats to humanity](https://www.ncronline.org/vatican/vatican-news/pope-leo-calls-disarm-ai-major-document-warns-technologic-threats-humanity)**

In Magnifica Humanitas, the pope says just war theory is "outdated," condemns lethal AI weapons and asks pardon for the church's delayed condemnation of slavery.

National Catholic Reporter • 10h ago

---

**[Pope Leo says AI must be 'disarmed' in first major teaching](https://www.bbc.com/news/articles/cedppn6002jo)**

The pontiff also warned of a "new digital slaveries" in his first encyclical since becoming Pope last year.

BBC • 6h ago

---

**[Pope Leo warns AI is fueling conflict, urges world to slow advances](https://www.nbcnews.com/world/the-vatican/pope-leo-encyclical-ai-conflict-magnifica-humanitas-rcna346784)**

History’s first American pontiff was writing in his first encyclical, a sweeping and eagerly anticipated manifesto on the subject that was released Monday.

NBC News • 11h ago

---

---

## HackerNews: "ai"

**[Memory has grown to nearly two-thirds of AI chip component costs](https://news.ycombinator.com/item?id=48258684)**

High-bandwidth memory (HBM) accounts for 63% of AI chip component costs, up from 52% in Q1 2024. Epoch AI's breakdown of component cost shifts across major chip designers.

⬆️ 428 • 💬 467 • 1d ago • [Epoch AI](https://epoch.ai/data-insights/ai-chip-component-cost-shares)

---

**[Pope Leo XIV says AI must serve humanity, not the powerful few](https://news.ycombinator.com/item?id=48266485)**

VATICAN CITY (RNS) — In ‘Magnifica Humanitas,’ Leo's 83-page manifesto on AI, the pope tackles the social, economic and political challenges associated with artificial intelligence.

⬆️ 332 • 💬 66 • 9h ago • [RNS](https://religionnews.com/2026/05/25/in-his-first-encyclical-pope-leo-xiv-says-ai-must-serve-humanity-not-the-powerful-few/)

---

**[Italy moves to Airbus A330 tankers](https://news.ycombinator.com/item?id=48248775)**

Rome shifts course: six Airbus A330 MRTT tanker aircraft, worth around €1.39 billion in total, to bolster the European pillar in NATO. #EuropeNews

⬆️ 283 • 💬 118 • 2d ago • [euronews](https://www.euronews.com/my-europe/2026/05/21/italy-moves-to-airbus-a330-tankers-in-major-nato-aligned-shift)

---

**[Is AI Profitable Yet?](https://news.ycombinator.com/item?id=48243863)**

⬆️ 262 • 💬 204 • 2d ago • [isaiprofitable.com](https://isaiprofitable.com/)

---

**[Netherlands Seizes 800 Servers, Arrests 2 for Aiding Cyberattacks](https://news.ycombinator.com/item?id=48266906)**

Authorities in the Netherlands have arrested the co-owners of two related Internet hosting companies for operating IT infrastructure used by Russia to carry out cyberattacks, influence operations and disinformation campaigns inside the European Union. The two men were the focus…

⬆️ 246 • 💬 67 • 8h ago • [krebsonsecurity.com](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/)

---

**[Microsoft reports AI is more expensive than paying human employees](https://news.ycombinator.com/item?id=48244434)**

Companies are racing to incentivize employees to use AI. But as some companies are finding, the more employees that use the technology, the heavier the bill.

⬆️ 229 • 💬 70 • 2d ago • [Fortune](https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/)

---

**[DeepSeek to Make Permanent 75% Discount on Flagship AI Model](https://news.ycombinator.com/item?id=48257410)**

⬆️ 209 • 💬 2 • 1d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model)

---

**[Don't just paste the AI at me](https://news.ycombinator.com/item?id=48242648)**

If someone asks you a question, paste your answer — not the chatbot's.

⬆️ 181 • 💬 113 • 2d ago • [dontquotetheai.com](https://dontquotetheai.com/)

---

**['AI washing': firms are scrambling to rebrand themselves as tech-focused](https://news.ycombinator.com/item?id=48257980)**

PR executives say UK companies are forcing them to present ordinary automation as artificial intelligence

⬆️ 177 • 💬 160 • 1d ago • [the Guardian](https://www.theguardian.com/technology/2026/may/24/ai-washing-pr-firms-scrambling-rebrand)

---

**[Pope Leo: opaque AI run by few firms risks "New Forms of Dehumanization"](https://news.ycombinator.com/item?id=48266435)**

Pope Leo issues AI Encyclical warning that 'Opaque Algorithms' controlled by a 'few' companies threaten 'new forms of  dehumanization'

⬆️ 163 • 💬 2 • 9h ago • [Variety](https://variety.com/2026/biz/global/pope-leo-ai-encyclical-algorithms-threaten-dehumanisation-1236758186/)

---

---

## YouTube Videos: "ai"

**[Pope Leo issues manifesto warning about AI](https://www.youtube.com/watch?v=RqXXs-ZIDNo)**

Pope Leo XIV says control of artificial intelligence must not remain in the hands “of a few” while warning that technology is fueling ...

📺 CNN

👁️ 65K • 👍 2K • 💬 733 • ⏱️ 11:28 • 8h ago

---

**[FULL SPEECH: Pope Leo XIV Warns AI “Needs To Be Disarmed” In Explosive Vatican Speech | AK1B](https://www.youtube.com/watch?v=aaYJ_4QcZfE)**

Pope Leo XIV unveiled his first encyclical, Magnifica Humanitas, at the Vatican, warning that artificial intelligence “needs to be ...

📺 DRM News

👁️ 32K • 👍 2K • 💬 196 • ⏱️ 11:16 • 11h ago

---

**[AI Just Crossed The Line We Were Afraid Of: Continual Harness](https://www.youtube.com/watch?v=qCFyprzrCvA)**

Princeton researchers just revealed Continual Harness, a self-improving AI system that learns while it is already running.

📺 AI Revolution

👁️ 40K • 👍 2K • 💬 196 • ⏱️ 13:31 • 2d ago

---

**[The singularity is near: Google unveils next phase of AI](https://www.youtube.com/watch?v=zvJ5KfNjOCk)**

ABC News' Nathan Rousseau Smith travels to Google I/O where the search giant unveiled AI agent Gemini Spark, new smart ...

📺 ABC News

👁️ 213K • 👍 3K • 💬 749 • ⏱️ 5:06 • 2d ago

---

**[This New AI Agent Turns You Into a One-Person Company](https://www.youtube.com/watch?v=HJN3husu1oM)**

Try Accio Work : https://www.accio.com/work?src=p_ytkol_vaibhav @Accio_official Join our WhatsApp Community Get the ...

📺 Vaibhav Sisinty

👁️ 81K • 👍 3K • 💬 100 • ⏱️ 16:03 • 1d ago

---

**[Pope Leo warns of the risks of AI](https://www.youtube.com/watch?v=_7MoCJ5tVEM)**

"Artificial intelligence needs to be disarmed." Pope Leo XIV calls for the regulation of AI in a sweeping manifesto and warns it ...

📺 MS NOW

👁️ 29K • 👍 954 • 💬 150 • ⏱️ 0:59 • 3h ago

---

**[It’s Happening... Anthropic MYTHOS 1 Is Here!](https://www.youtube.com/watch?v=rDDI9gDiNAg)**

Claude Mythos 1 and Anthropic's Claude Security are now at the center of a massive AI cybersecurity story. Project Glasswing ...

📺 AI Revolution

👁️ 50K • 👍 2K • 💬 116 • ⏱️ 14:27 • 23h ago

---

**[Finally! FREE and Unlimited AI Video Generator](https://www.youtube.com/watch?v=lOhHu1WoiB4)**

3-Day Live Class to Start a successful Faceless channel to Monetize: https://selar.com/y167747p6g Want to create AI videos ...

📺 Build and Brand with Kuyik

👁️ 1K • 👍 66 • 💬 22 • ⏱️ 9:50 • 6h ago

---

**[Pope Leo XIV’s first encyclical calls for &quot;disarming&quot; of AI #shorts](https://www.youtube.com/watch?v=Z_qGDM1Q6qc)**

pope #ai #popeleoxiv Each weekday morning, "CBS Mornings" co-hosts Gayle King, Tony Dokoupil and Nate Burleson bring you ...

📺 CBS Mornings

👁️ 2K • 👍 50 • 💬 2 • ⏱️ 1:52 • 2h ago

---

**[Priest Reacts to Pope Leo’s AI Encyclical (w/ Fr. Gregory Pine)](https://www.youtube.com/watch?v=cpptgvohfZc)**

Pope Leo XIV's first encyclical, Magnifica Humanitas (“Magnificent Humanity”), reflects on the dignity of the human person in the ...

📺 Ascension Presents

👁️ 20K • 👍 1K • 💬 161 • ⏱️ 27:17 • 6h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)**

*Tencent*

Hy-MT2-1.8B is a fast, 1.8B parameter multilingual translation model supporting 33 languages, optimized for on-device deployment with 1.25-bit quantization (440MB storage, 1.5x speedup). It excels in general, business, and instruction-following translation tasks, outperforming mainstream commercial APIs.

`translation` `2.0B`

⬇️ 5,552 • ❤️ 788 • 3d ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 1,679 • ❤️ 815 • 2d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 7,291 • ❤️ 343 • 5d ago

---

**[Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)**

*Tencent*

Hy-MT2-30B-A3B is a large-scale (30B parameters, MoE) multilingual translation model supporting 33 languages. It excels in general, business, and instruction-following translation tasks, outperforming leading open-source models and commercial APIs.

`translation` `30.1B`

⬇️ 1,494 • ❤️ 323 • 3d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 90,026 • ❤️ 301 • 4d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 45,800 • ❤️ 669 • 7d ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 214 • 3d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, featuring a prompt enhancer for improved input processing and supporting various LTX 2.3 formats.

`text-to-video` `9.0B`

⬇️ 1,354,786 • ❤️ 1,345 • 3d ago

---

**[command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)**

*Cohere Labs*

Command A+ is a 25B parameter, multilingual, vision-capable LLM optimized for agentic and reasoning tasks. It supports a 128K context window and offers a W4A4 quantization for efficient enterprise deployment.

`image-text-to-text` `125.8B`

⬇️ 7,449 • ❤️ 199 • 3d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter causal language model with vision capabilities, optimized for faster inference via MTP. It excels at agentic coding, reasoning, and handling extended contexts up to 1M tokens, making it suitable for complex development workflows and iterative tasks.

`image-text-to-text` `27.3B`

⬇️ 695,277 • ❤️ 477 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 81 • 💬 3 • ⭐ 79,445 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 152 • 💬 2 • ⭐ 72 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 64,869 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 26,005 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,610 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 74,824 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://huggingface.co/papers/2605.18739)**

*Yukang Chen, Luozhou Wang, Wei Huang et al. (16 authors)*

🏢 NVIDIA

LongLive-2.0 presents an NVFP4-based parallel infrastructure for long video generation that addresses training and inference bottlenecks through sequence-parallel autoregressive training and diffusion model tuning.

▲ 109 • 💬 3 • ⭐ 1,993 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18739) • [💻 code](https://github.com/NVlabs/LongLive) • [🔗 project](https://nvlabs.github.io/LongLive/LongLive2/)

---

**[Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation](https://huggingface.co/papers/2605.19833)**

*Zhifei Xie, Kaiyu Pang, Haobin Zhang et al. (7 authors)*

🏢 National University of Singapore

Mega-ASR framework improves robustness in real-world speech recognition through compound-data construction and progressive acoustic-to-semantic optimization techniques.

▲ 127 • 💬 3 • ⭐ 576 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.19833) • [💻 code](https://github.com/xzf-thu/Mega-ASR) • [🔗 project](https://xzf-thu.github.io/Mega-ASR/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 8 • 💬 0 • ⭐ 18,713 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 120 • 💬 10 • ⭐ 10,589 • 22d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 4.9k • 🔱 500 • 3d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.5k • 🔱 1.1k • 8d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.6k • 🔱 179 • 6h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.3k • 🔱 390 • 3d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.3k • 🔱 346 • 8d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.2k • 🔱 480 • 15h ago

---

**[Nutlope/hallmark](https://github.com/Nutlope/hallmark)**

Anti-AI-slop design skill for Claude Code, Cursor, and Codex.

`CSS`

⭐ 1.9k • 🔱 131 • 5d ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.8k • 🔱 217 • 18d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 1.8k • 🔱 123 • 5h ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.7k • 🔱 191 • 14h ago

---

---

*Generated by PeekDeck - A glance is all you need*
