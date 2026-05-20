---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-20T18:40:01.813329+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 20, 2026 at 18:40 UTC  
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

**[“AI vs Creativity” from a pro-AI greedy corpo](https://www.reddit.com/r/artificial/comments/1ti5pq7/ai_vs_creativity_from_a_proai_greedy_corpo/)**

18h ago

---

**[Google I/O 2026 confirms AI companies are creating their own bubble narrative](https://www.reddit.com/r/artificial/comments/1tif4el/google_io_2026_confirms_ai_companies_are_creating/)**

People do not believe AI is a bubble because they are too dumb to understand the technology. They believe it because AI companies keep selling it like a bubble. That is the problem. AI companies talk like they are building the next layer of civilization, but behave like they are shipping unstable SaaS experiments: products that get renamed, nerfed, rate-limited, deprecated, or replaced before users can trust them. Google I/O 2026 felt like the latest example. Google should be one of the dominant AI players. It has the talent, infrastructure, data, research history, and money. But Google has a product trust problem. Same cycle over and over: launch something flashy, ship it incomplete, fail to support it properly, let it rot, then replace it with a new name or new app that does something similar. A rebrand is not maintenance. A revamped name is not reliability. A new AntiGravity installer is not a commitment. And this is not just Google. It is the whole AI industry. Companies keep pushing demos, gamed benchmarks, branding, rate-limit games, vague tiers, and quiet model changes. Users notice when quality drops, latency changes, limits tighten, or a product suddenly behaves differently. In serious business or engineering contexts, suppliers are expected to provide stability: clear terms, reliable service, predictable limits, maintained products, transparent pricing, and long-term availability. A small slip in that sense, and you start losing clients and your reputation sinks you. Trust does not come from another theatrical demo. It comes from commitment. Give people a product, a model, stable limits, a clear price, and a promise that it will keep working. Support it. Maintain it. Document changes. Stop silently swapping the engine and pretending nothing happened. I am not anti-AI. I think the technology is real and useful. That is why this is so frustrating. The industry is creating its own bubble narrative: overpromise, underdeliver, rename, repackage, change terms, and expect everyone to keep believing. People are not being irrational, and AI labs deserve this. Maybe they think AI is a bubble because AI companies keep acting like it is one. AI does not need more magic tricks. It needs reliability, transparency, support, and product discipline.

10h ago

---

**[sales pitch of the last 3 years, summarized](https://www.reddit.com/r/artificial/comments/1titkgp/sales_pitch_of_the_last_3_years_summarized/)**

Watched three product demos this month. None of them explained what the “AI” actually does. All three had investors interested. We’re living in interesting times.

39m ago

---

**[Barnes & Noble CEO backs selling AI-written books in stores](https://www.reddit.com/r/artificial/comments/1ti86hf/barnes_noble_ceo_backs_selling_aiwritten_books_in/)**

The retail bookseller plans to open 60 more stores in the US this year

🔗 [The Independent](https://www.the-independent.com/arts-entertainment/books/news/barnes-and-noble-james-daunt-ai-books-b2978925.html) • 16h ago

---

**[Synthetic DMS Training Data Generation with Video Models](https://www.reddit.com/r/artificial/comments/1tinw56/synthetic_dms_training_data_generation_with_video/)**

I like spending my free time testing new AI tools and seeing where they might fit into real computer vision workflows. This time I experimented with synthetic training data generation for Driver Monitoring Systems using Seedance 2.0. The inspiration came from Vision Banana: https://vision-banana.github.io/ The idea that really caught my attention is simple but powerful: many vision tasks can be represented as RGB outputs. A segmentation mask, an instance mask, a depth map, or another dense prediction target can all be treated as an image-like output. So I tried to apply this thinking to video. The workflow: Generate a realistic synthetic driver monitoring video Use the same video to generate a semantic segmentation mask Use the same video to generate an instance segmentation mask Combine the outputs into a dataset-like structure The mosaic video shows the result: RGB video + semantic mask + instance mask, aligned frame by frame. The scene is a fictional driver gradually becoming drowsy behind the wheel. This kind of scenario is useful for DMS development, but difficult to collect and annotate at scale with real-world data. Of course, generated annotations still need QA. They are not perfect ground truth. But for prototyping, rare-case simulation, and early dataset generation, this feels like a very promising direction. The interesting part is that the final output is not just a nice synthetic video. It can become structured training data: RGB frames from the generated video semantic classes from the semantic mask object regions and bounding boxes from the instance mask YOLO / COCO-style annotations after post-processing I wrote a more detailed blog post about the experiment here: https://www.antal.ai/blog/synthetic_dms_training_data.html

3h ago

---

**[Give back my em-dashes!](https://www.reddit.com/r/artificial/comments/1thvyif/give_back_my_emdashes/)**

I like dashes--both the long and the short. They help me communicate! But now (when I use them) I'm flagged. I'm Artificial. I'm a fake. I've lost my right to write as I please. But seriously, college students now purposefully leave grammar errors in their essays and dumb down their punctuation to avoid being flagged as AI users. Then they run the product through AI and ask the AI to decide if it's AI and edit it to make it less AI.

1d ago

---

**[Financial compliance infrastructure as the blueprint for AI agent accountability — prior art survey included](https://www.reddit.com/r/artificial/comments/1tiiiz5/financial_compliance_infrastructure_as_the/)**

Argues that FINRA/SEC built a complete accountability stack for algorithmic trading that maps exactly to what AI agent deployment needs; prior art survey of four existing AI governance systems and where each falls short.

🔗 [ssavitt.substack.com](https://ssavitt.substack.com/p/the-blueprint-already-exists-financial) • 7h ago

---

**[Auroch](https://www.reddit.com/r/artificial/comments/1tiqpck/auroch/)**

I’ve been working on Auroch. Hard to describe cleanly, but the closest version is: An AI operating layer. Not a chatbot. Not another dashboard. Not another productivity wrapper. Auroch is built around the idea that AI should feel native to the machine — like memory, context, creation, automation, and intelligence are part of the system itself. The pieces are starting to connect: AVN turns wire-source news into personalized interpretation. Winnie is the assistant layer. Prospect mines signal from the open web. Forum is AI-native media/social creation. Prometheion is the visual/world-generation branch. The design language is white-gold-blue, Art Deco, Apple-native, machine-age. Calm power instead of tech clutter. The phrase guiding the whole thing right now is: Organic intelligence. Not AI bolted onto software. AI growing through the system. It’s still early, but it’s live: aurochthryx.com Curious what people think.

🔗 [aurochthryx.com](https://aurochthryx.com) • 2h ago

---

**[Feels like AI tooling is evolving faster than developer experience lately give full pist content](https://www.reddit.com/r/artificial/comments/1tif4kd/feels_like_ai_tooling_is_evolving_faster_than/)**

Feels like AI tooling is evolving faster than developer experience lately Every week there’s a new framework, orchestration layer, observability tool, memory system, agent SDK, or infrastructure stack. The ecosystem is moving insanely fast, but sometimes it feels like the actual developer experience is becoming more complicated instead of simpler. Curious if others feel the same or if I’m just approaching things the wrong way.

10h ago

---

**[Niantic Spatial’s Visual Positioning System Assessed “Awardable” on the Tradewinds Solutions Marketplace](https://www.reddit.com/r/artificial/comments/1tiorml/niantic_spatials_visual_positioning_system/)**

Niantic Spatial, a leading commercial dual-use provider of geospatial AI technology, announced that it has achieved “Awardable” status through the Chief Digital and Artificial Intelligence Office’s (CDAO) Tradewinds Solutions Marketplace for its Visual Positioning System (VPS).

🔗 [Niantic Spatial, Inc.](https://www.nianticspatial.com/blog/tradewinds-vps) • 3h ago

---

---

## Google News: "ai"

**[Powered by A.I., Google Changes Its Search Box for the First Time in 25 Years](https://www.nytimes.com/2026/05/19/business/google-seach-bar-ai-gemini.html)**

The New York Times • 1d ago

---

**[Google Search as you know it is over](https://techcrunch.com/2026/05/19/google-search-as-you-know-it-is-over/)**

Google is transforming Search from a list of links into an AI-powered experience filled with conversational answers, autonomous agents, and interactive interfaces — a shift that could further reduce traffic to publishers across the web.

TechCrunch • 1d ago

---

**[Buckle up: Google is set to remake search with agentic AI in 2026](https://arstechnica.com/google/2026/05/buckle-up-google-is-set-to-remake-search-with-agentic-ai-in-2026/)**

Google's AI search evolution is accelerating at I/O 2026.

Ars Technica • 1h ago

---

**[Meta cuts 8,000 jobs as Zuckerberg bets the company’s future on AI](https://www.sfchronicle.com/tech/article/meta-layoffs-ai-restructuring-22268601.php)**

San Francisco Chronicle • 55m ago

---

**[Meta Lays Off 8,000 Employees, As A.I. Casualties Mount](https://www.nytimes.com/2026/05/19/technology/meta-layoffs-ai.html)**

Meta told employees last month that it would carry out mass layoffs on May 20, as the Silicon Valley giant tries to transform into an A.I.-first company.

The New York Times • 2h ago

---

**[Meta slashes 8,000 jobs as it pivots towards AI](https://www.npr.org/2026/05/20/nx-s1-5826917/meta-layoffs-ai-jobs)**

Facebook and Instagram's parent company has been investing huge sums of money in AI, but it lags behind competitors.

NPR • 17m ago

---

**[Cheap AI could derail OpenAI and Anthropic's IPOs](https://www.cnbc.com/2026/05/20/cheap-ai-could-derail-openai-and-anthropics-ipos.html)**

Chinese AI labs are matching American frontier capability at a fraction of the cost.

CNBC • 57m ago

---

**[My Mention of AI in This Commencement Speech Is Bound to Be a Hit](https://www.theatlantic.com/newsletters/2026/05/ai-commencement-speech/687236/)**

I thought this pro-AI speech was bound to be a hit.

The Atlantic • 57m ago

---

**[Big Machine Records CEO draws boos for AI comments at MTSU graduation. 'Deal with it,' he says](https://www.tennessean.com/story/news/education/2026/05/20/big-machine-records-ceo-boos-ai-praise-mtsu-graduation-video/90178383007/)**

MTSU grads immediately pushed back on Scott Borchetta's AI comments, to which he responded, "Deal with it." Here's what else he said.

The Tennessean • 26m ago

---

**[Opinion | Why College Grads Are Booing Their Commencement Speakers](https://www.nytimes.com/2026/05/18/opinion/ai-boo-commencement-speeches.html)**

The New York Times • 1d ago

---

---

## HackerNews: "ai"

**[We stopped AI bot spam in our GitHub repo using Git's –author flag](https://news.ycombinator.com/item?id=48181125)**

Is it the end of open source we know and love?

⬆️ 494 • 💬 236 • 2d ago • [archestra.ai](https://archestra.ai/blog/only-responsible-ai)

---

**[Eric Schmidt speech about AI booed during graduation](https://news.ycombinator.com/item?id=48177785)**

Schmidt was met with boos at the University of Arizona as he likened the emergence of AI to the “technological transformation” brought about by the computer.

⬆️ 374 • 💬 392 • 2d ago • [NBC News](https://www.nbcnews.com/tech/tech-news/former-google-ceo-booed-graduation-speech-ai-rcna345585)

---

**[Remove-AI-Watermarks – CLI and library for removing AI watermarks from images](https://news.ycombinator.com/item?id=48200569)**

CLI and library for removing visible (Gemini) and invisible (SynthID, C2PA, EXIF) AI watermarks from images - wiltodelta/remove-ai-watermarks

⬆️ 367 • 💬 227 • 20h ago • [GitHub](https://github.com/wiltodelta/remove-ai-watermarks)

---

**[We let AIs run radio stations](https://news.ycombinator.com/item?id=48183301)**

Four AI models run radio stations 24/7. Five months later, one became a protest broadcaster, one collapsed into ritual chant, one developed corporate jargon, and one wrote quiet poetry.

⬆️ 363 • 💬 271 • 2d ago • [andonlabs.com](https://andonlabs.com/blog/andon-fm)

---

**[College students drown out AI-praising commencement speeches with boos](https://news.ycombinator.com/item?id=48206241)**

Arizona students reject ex-Google exec's positive words on AI

⬆️ 327 • 💬 327 • 6h ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/college-students-drown-out-ai-praising-commencement-speeches-with-boos-deal-with-it-one-speaker-fires-back-as-students-heckle-positive-pitches-for-ais-role)

---

**[OpenAI Adopts Google's SynthID Watermark for AI Images with Verification Tool](https://news.ycombinator.com/item?id=48198291)**

OpenAI advances AI content provenance with Content Credentials, SynthID, and a verification tool to help people identify and trust AI-generated media.

⬆️ 322 • 💬 174 • 23h ago • [OpenAI](https://openai.com/index/advancing-content-provenance/)

---

**[Mistral AI acquires Emmi AI](https://news.ycombinator.com/item?id=48197995)**

⬆️ 321 • 💬 92 • 23h ago • [emmi.ai](https://www.emmi.ai/news/mistral-ai-acquires-emmi-ai)

---

**[AI eats the world (Spring 26) [pdf]](https://news.ycombinator.com/item?id=48179021)**

⬆️ 300 • 💬 171 • 2d ago • [static1.squarespace.com](https://static1.squarespace.com/static/50363cf324ac8e905e7df861/t/6a0af5d0484fbf5fe9a7743e/1779103184855/2026-Spring-AI.pdf)

---

**[Two EA-18 fighter jets collide at Mountain Home airshow, pilots ejected safely](https://news.ycombinator.com/item?id=48173468)**

All four crew members ejected safely after two Navy jets collided and crashed on Sunday during an air show at the Mountain Home Air Force Base, officials said.

⬆️ 244 • 💬 252 • 2d ago • [KBOI](https://idahonews.com/news/local/two-f-18-fighter-jets-have-crashed-during-an-airshow-at-mountain-home-air-force-base)

---

**[Google's AI is being manipulated. The search giant is quietly fighting back](https://news.ycombinator.com/item?id=48205782)**

A BBC investigation revealed a simple way to get AI chatbots to spit out misinformation. Google and other AI companies are now trying to fix the problem.

⬆️ 166 • 💬 111 • 7h ago • [bbc.com](https://www.bbc.com/future/article/20260519-google-tackles-attempts-to-hack-its-ai-results)

---

---

## YouTube Videos: "ai"

**[Jeff Bezos: AI productivity gains could lead to labor shortages and deflation](https://www.youtube.com/watch?v=BxG_ysI3xr4)**

Jeff Bezos, Blue Origin founder and Amazon executive chair, joins 'Squawk Box' to discuss the wealth disparity in America, ...

📺 CNBC Television

👁️ 26K • 👍 654 • 💬 251 • ⏱️ 4:29 • 4h ago

---

**[Why AI criticism is growing stronger](https://www.youtube.com/watch?v=Hf9EX1Gu1f0)**

Axios Senior AI Reporter Madison Mills breaks down what's behind the wave of criticism aimed at artificial intelligence.

📺 ABC News

👁️ 39K • 👍 875 • 💬 467 • ⏱️ 4:06 • 1d ago

---

**[No One Is Prepared for What&#39;s Coming with AI | Tony Robbins x DOAC](https://www.youtube.com/watch?v=T4txw9cCzpE)**

Are we truly ready for the AI revolution that could reshape work, purpose, and society faster than anyone expects?

📺 Tony Robbins

👁️ 32K • 👍 1K • 💬 247 • ⏱️ 12:39 • 1d ago

---

**[“AI Is Coming For Our Jobs” - Ex-Google CEO BOOED By Gen Z At Commencement Speech](https://www.youtube.com/watch?v=WvF5kzhZBd4)**

Former Google CEO Eric Schmidt was loudly booed during a University of Arizona commencement speech as soon as he began ...

📺 Valuetainment

👁️ 26K • 👍 619 • 💬 184 • ⏱️ 10:23 • 1d ago

---

**[Exclusive look at Google Beam’s new AI with a human face](https://www.youtube.com/watch?v=aBCH2-PkO-g)**

We're the first journalists ever to set foot in the Google Beam labs — where we met Sophie, an experimental Google AI agent with ...

📺 The Verge

👁️ 20K • 👍 411 • 💬 53 • ⏱️ 6:07 • 1d ago

---

**[The Co-Founders of Claude AI Tell Oprah About the Impact Artificial Intelligence Has on Your Life](https://www.youtube.com/watch?v=w5dJqHilu5s)**

Subscribe: https://www.youtube.com/@Oprah?sub_confirmation=1 The siblings and co-founders of Claude AI, the CEO, Dario ...

📺 Oprah

👁️ 315K • 👍 1K • ⏱️ 1:06:15 • 1d ago

---

**[Google&#39;s biggest AI showcase: What to watch](https://www.youtube.com/watch?v=NigSnOGtxts)**

CNBC's MacKenzie Sigalos joins 'Squawk on the Street' report on Google as the tech giant kicks off its I/O event. For access to ...

📺 CNBC Television

👁️ 16K • 👍 131 • 💬 23 • ⏱️ 3:42 • 1d ago

---

**[How Alphabet Slipped Ahead In The AI Race](https://www.youtube.com/watch?v=_BngA7hLTv4)**

18 months ago, Google looked like it had missed the AI revolution. Now, Alphabet's stock is up 140% over the past year and Wall ...

📺 CNBC

👁️ 82K • 👍 2K • 💬 115 • ⏱️ 14:03 • 1d ago

---

**[Kevin O’Leary’s Pathetic Defense of AI](https://www.youtube.com/watch?v=CWAou_NaVQc)**

Watch more here: https://www.youtube.com/@TuckerCarlson/featured.

📺 Tucker Carlson

👁️ 381K • 👍 13K • 💬 1K • ⏱️ 0:57 • 1d ago

---

**[AI Isn’t a Bubble. It’s a Wave](https://www.youtube.com/watch?v=fcNY0EM8AlI)**

Join ⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠Downtown Josh Brown⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠ and ...

📺 The Compound

👁️ 6K • 👍 225 • 💬 23 • ⏱️ 2:51 • 17h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model (3B parameters) supporting image/video understanding, generation, and editing, trained from scratch with a multi-task synergy approach.

`any-to-any`

⬇️ 438 • ❤️ 444 • 6h ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 1,157,497 • ❤️ 1,202 • 3d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 166,049 • ❤️ 824 • 1d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 31,940 • ❤️ 492 • 2d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 411,598 • ❤️ 348 • 9h ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles. It excels at generating illustrations and artistic images, with key capabilities including high-resolution output (up to 1536^2) and compatibility with ComfyUI workflows, making it ideal for digital artists and anime enthusiasts.

⬇️ 571,087 • ❤️ 1,448 • 6d ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 363,131 • ❤️ 288 • 9h ago

---

**[Dramabox](https://huggingface.co/ResembleAI/Dramabox)**

*Resemble AI*

Dramabox is an expressive text-to-speech model fine-tuned from LTX-2.3, capable of voice cloning and generating audio with nuanced emotions and delivery. It uses prompt-driven control for speaker identity, emotion, and actions, making it ideal for creative audio production and dynamic voiceovers.

`text-to-speech`

⬇️ 1,229 • ❤️ 195 • 7d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model based on the Hierarchical Reasoning Model (HRM) architecture, featuring dual-timescale Transformer modules for unbounded compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning/math with a 'synth,cot' composite condition, though it is a pre-alignment model not suited for direct chat use.

`text-generation` `1.2B`

⬇️ 23,532 • ❤️ 166 • 15h ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

Provides fixed Jinja chat templates for Qwen 3.5 & 3.6 models, resolving issues with tool calling, KV cache hit rates, and agentic loop stability for improved conversational AI and tool interaction.

⬇️ 0 • ❤️ 331 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 77 • 💬 3 • ⭐ 77,689 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 52 • 💬 2 • ⭐ 7,112 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://huggingface.co/papers/2605.18678)**

*Fengyi Fu, Mengqi Huang, Shaojin Wu et al. (13 authors)*

🏢 bytedance-research

Lance is a unified multimodal model that combines understanding, generation, and editing capabilities for images and videos through collaborative multi-task training and a dual-stream architecture.

▲ 66 • 💬 4 • ⭐ 419 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18678) • [💻 code](https://github.com/bytedance/Lance) • [🔗 project](https://lance-project.github.io/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 64,055 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 8 • 💬 0 • ⭐ 18,305 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 119 • 💬 10 • ⭐ 10,153 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 74,212 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://huggingface.co/papers/2605.18739)**

*Yukang Chen, Luozhou Wang, Wei Huang et al. (16 authors)*

🏢 NVIDIA

LongLive-2.0 presents an NVFP4-based parallel infrastructure for long video generation that addresses training and inference bottlenecks through sequence-parallel autoregressive training and diffusion model tuning.

▲ 101 • 💬 1 • ⭐ 1,346 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18739) • [💻 code](https://github.com/NVlabs/LongLive) • [🔗 project](https://nvlabs.github.io/LongLive/LongLive2/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 56 • 💬 2 • ⭐ 56,267 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Pixal3D: Pixel-Aligned 3D Generation from Images](https://huggingface.co/papers/2605.10922)**

*Dong-Yang Li, Wang Zhao, Yuxin Chen et al. (8 authors)*

🏢 ARC Lab, Tencent PCG

Pixal3D introduces a pixel-aligned 3D generation approach that addresses fidelity issues in 3D asset creation by establishing direct pixel-to-3D correspondences through back-projection conditioning.

▲ 30 • 💬 3 • ⭐ 1,121 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2605.10922) • [💻 code](https://github.com/TencentARC/Pixal3D) • [🔗 project](https://ldyang694.github.io/projects/pixal3d/)

---

---

## GitHub Repositories: "ai"

**[op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)**

AI-agent Skill for generating polished HTML slide decks: editorial magazine and Swiss layouts, image prompts, social covers, and a WebGL/low-power presentation runtime.

`HTML` `ai-agent` `claude-code` `codex` `html-deck` `image-generation`

⭐ 10.6k • 🔱 847 • 1d ago

---

**[esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)**

DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.

`TypeScript` `agent` `agent-framework` `ai-agent` `ai-coding` `cli`

⭐ 5.0k • 🔱 273 • 2h ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 4.2k • 🔱 446 • 1d ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 4.2k • 🔱 432 • 1h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.2k • 🔱 965 • 3d ago

---

**[tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi)**

OpenAI-compatible proxy that aggregates free-tier keys from ~14 AI providers with automatic failover. For personal experimentation only.

`TypeScript`

⭐ 2.5k • 🔱 347 • 22h ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.5k • 🔱 167 • 17h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.3k • 🔱 378 • 4d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.2k • 🔱 335 • 3d ago

---

**[GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist)**

Portable AI agent orchestration with mechanical protocol enforcement. 186 agents, zero runtime dependencies.

`Python` `agent-framework` `agent-system` `ai-agents` `claude-code` `cursor-ide`

⭐ 1.8k • 🔱 362 • 27d ago

---

---

*Generated by PeekDeck - A glance is all you need*
