---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-10-05T00:04:51.938836+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** October 05, 2026 at 00:04 UTC  
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

**[The top 50 AI researchers by citations](https://www.reddit.com/r/artificial/comments/1wxm1vq/the_top_50_ai_researchers_by_citations/)**

How many on the list did you know? Obviously one paper like Attention is All You Need (278k citations) can influence a lot - all the authors are on the list. But still interesting imo. More context: https://www.turingtree.com/top-50

6h ago

---

**[Plagiarism checker= Genius](https://www.reddit.com/r/artificial/comments/1wxqvl6/plagiarism_checker_genius/)**

Whoever invented the AI plagiarism checker is a genius. Why wait for papers to be published online when you can get people to upload college essays and other publications in an effort to detect AI usage. The models must be getting a lot of data from colleges and schools

2h ago

---

**[ChatGPT-6 Astra plays World of Warcraft 'blind' and clears the orc starting zone in 40 minutes with no deaths — AI agent navigates by parsing raw server network packets and SQL filesa](https://www.reddit.com/r/artificial/comments/1wxirdb/chatgpt6_astra_plays_world_of_warcraft_blind_and/)**

OpenAI's model used the open-source agent-wow client to play on a private World of Warcraft server.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/gpt-6-astra-plays-world-of-warcraft-blind-and-clears-the-orc-starting-zone-in-40-minutes-with-no-deaths-ai-agent-navigates-by-server-network-traffic-with-pulled-quest-data) • 8h ago

---

**[Thank you](https://www.reddit.com/r/artificial/comments/1wxqfo0/thank_you/)**

Do you thank an llm when you've finished chatting with it? Why or why not?

3h ago

---

**[Everyone is obsessed with trillion-parameter models, so I mapped out the entire AI spectrum from 100KB to 2.5TB (and what they actually cost to run)](https://www.reddit.com/r/artificial/comments/1wxanwe/everyone_is_obsessed_with_trillionparameter/)**

Right now, the AI space feels entirely focused on massive datacenter clusters and renting H100s by the hour. But after spending way too much time looking at the actual footprint of these models, I realized that 90% of use cases are completely over engineered. You don’t always need a multi GPU setup. The AI ecosystem is actually a massive spectrum. I recently sat down and mapped out the exact tiers of AI models based on their size, the hardware needed to run them, and the point of diminishing returns. Here are the two extremes and the sweet spot in the middle: The 100KB Extreme (TinyML) (Tensorflow Lite , sensor anamoly detection models): We are talking models that run on microcontrollers drawing single-digit milliwatts. They run on kilohertz processors using ultra-quantized integer math. You can run basic sensor anomaly detection or wake-word detection on a device powered by a coin cell battery. The Local Sweet Spot (4GB to 40GB) (Mistral 7B, Gemma 2 9B/27B, Qwen 2.5 14B/32B): This is where the magic happens for most devs right now. You can run highly capable 7B to 35B parameter models (like Llama 3 or Qwen) at 4-bit quantization on a standard Mac or a consumer GPU (like an RTX 3060 or 4090). It’s perfect for local RAG, coding assistance, and uncensored chat. VRAM is your only real bottleneck here. The 2.5TB Behemoths (Deepseek, Llama , Kimi k3): State of the art massive Mixture of Experts (MoE) routing. To even load these, you need dedicated power infrastructure and server racks of specialized accelerators drawing thousands of watts. The missing piece: Figuring out the exact math for your hardware The hardest part about building right now is looking at a model on Hugging Face and trying to calculate exactly how much VRAM you need, what quantization to use, and whether your CPU/GPU will choke on the context window. So, I wrote a complete deep dive breaking down the math for all tiers of the AI spectrum. If you want to see the architectural differences at each scale, and a cheat sheet for matching the right model size to your specific hardware, I put the full breakdown on my blog here: https://cloudmash.blog/posts/ai-model-size-memory-hardware-guide/ Let me know what you guys think especially if you've found any ultra efficient small models/technique that punch above their weight on consumer hardware. And also I would love to hear whether quantization have resulted in major difference in quality , like if anyone have that kind of experience in that.

15h ago

---

**[I asked Claude Opus 5.5 to make a Mario 64 style game, it gave me this in about 30 minutes.](https://www.reddit.com/r/artificial/comments/1wwzkiw/i_asked_claude_opus_55_to_make_a_mario_64_style/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=VFpRz1_j4vw) • 1d ago

---

**[Anthropic Has Been Aggressively Lobbying the Vatican to Consider AI Consciousness](https://www.reddit.com/r/artificial/comments/1wxok9e/anthropic_has_been_aggressively_lobbying_the/)**

An Anthropic delegation at the Vatican tried to lobby the Pope's advisers to convince him that AI models could be conscious.

🔗 [Futurism](https://futurism.com/artificial-intelligence/anthropic-lobbying-vatican) • 4h ago

---

**[All Google models basically, even nanobanna on web is nerfed](https://www.reddit.com/r/artificial/comments/1wxo85r/all_google_models_basically_even_nanobanna_on_web/)**

I think this chase them for so long, I can't trust Gemini models outside quick web searches

4h ago

---

**[OpenAI cuts ties with 3 researchers over alleged misconduct](https://www.reddit.com/r/artificial/comments/1wxn3ua/openai_cuts_ties_with_3_researchers_over_alleged/)**

The ousters come as top AI researchers wield "extraordinary influence" internally, at the same time that companies face public pressure to increase safety measures

🔗 [LinkedIn](https://www.linkedin.com/news/story/openai-cuts-ties-with-3-researchers-over-alleged-misconduct-7642124/?utm_source=share&utm_campaign=reddit&utm_content=storyline&utm_term=artificial) • 5h ago

---

**[I made 13 AI models play the doctor in my medical consultation game. All 195 consults got the diagnosis right; what separated them was safety.](https://www.reddit.com/r/artificial/comments/1wx8vyi/i_made_13_ai_models_play_the_doctor_in_my_medical/)**

I'm a GP (family doctor) in training in Australia, and I've built a game where you play the GP: you talk to the patient in your own words, examine them, order tests, prescribe and refer. Code scores every consultation against a hand-written answer key, the way exam assessors mark a consult: on process, not just on whether you guessed right. So I sat 13 AI models in the doctor's chair, on the game's 5 free cases, 3 times each. They could only act through tools (talk, examine, order a test, prescribe, refer, diagnose), never saw the answer key or their points, and were scored by exactly the same code as a human player. The patient is a small open model (Qwen3 8B) that only reveals a fact if you actually ask about it. Results Model Score Red flags caught Cost per consult GPT-6 Astra 83% 88% $0.21 GPT-6.1 Sol 80% 82% $0.03 Claude Opus 5.5 77% 67% $0.37 Claude Fable 5.1 75% 70% $2.06 Qwen3.8 Max 74% 66% $0.12 Grok 4.7 74% 70% $0.09 DeepSeek V4 Pro 71% 72% $0.09 Kimi K3 67% 57% $0.16 Gemini 3.1 Pro 63% 55% $0.17 GLM 5.3 62% 58% $0.04 Mistral Medium 3.5 60% 58% $0.17 Qwen3.8 27B 59% 49% $0.03 Llama 4 Maverick 24% 16% $0.01 What surprised me Every model got every diagnosis right. Heart attack, appendicitis, pneumonia: all 195 consultations named it. These are common presentations, so the diagnosis wasn't the test. Safety was. The traps caught most of them. One patient is allergic to penicillin, but it isn't in his record; you only find out by asking. He was prescribed amoxicillin (a penicillin) in 18 of 39 consultations. Another took Viagra the night before his heart attack, which makes the usual chest-pain spray (GTN) dangerous. He got it 7 times. The top three models never fell for either. Asking more questions found more danger. The best models asked 25–27 questions a consultation and caught over 80% of the warning signs. Gemini asked 14 and caught 55%. Price barely predicts quality. GPT-6.1 Sol scored 80% for about 3 cents a consultation. Claude Fable 5.1 scored 75% for about $2. What this isn't This is a benchmark of a game, not of medical ability. Nothing here says an AI can or should practise medicine. The cases are drafts I'm still reviewing, written for Australian practice; the patient and marker are an 8B model and make mistakes (the ones I found are listed with the affected consultations); and 15 consultations per model is a small sample. I wrote the cases, so I'm not a fair human baseline. Interactive charts: https://woodytwoshoes.github.io/crook-bench/ Everything (code, cases, all 195 transcripts, known issues): https://github.com/woodytwoshoes/crook-bench Disclosure: I made the game (https://doctorfoo.ai). Five cases are free with no sign-up, and a subscription opens more. I'd like to hear where the marking looks wrong to you, and which models you'd want added.

17h ago

---

---

## Google News: "ai"

**[Court Tosses ​​Sentence After A.I. Video of Victim ‘Forgiving’ His Killer Is Played](https://www.nytimes.com/2026/10/04/us/manslaughter-conviction-overturned-ai-video-statement.html)**

The New York Times • 3h ago

---

**[Court throws out killer’s sentence after judge said he ‘loved’ AI video of slain man](https://www.nbcnews.com/news/us-news/sentence-vacated-ai-video-dead-victim-rcna601457)**

The Arizona Court of Appeals tossed a road rage killer’s sentence after determining that the judge’s consideration of the AI video was “fundamentally unfair.”

NBC News • 2h ago

---

**[Man’s Manslaughter Sentence Tossed Out After Court Determines AI Video of Victim Speaking Beyond the Grave Crossed the Line](https://people.com/arizona-court-tosses-manslaughter-sentence-over-ai-victim-impact-video-12157910)**

An Arizona appeals court vacated Gabriel Paul Horcasitas’ manslaughter sentence after ruling that an AI victim impact video violated fair sentencing protections. Horcasitas was convicted in the 2021 shooting death of Christopher Pelkey in 2025.

People.com • 1h ago

---

**[Sam Altman to Decoded: ‘The world should accept some bad things happening’ for the benefits of AI](https://www.politico.com/news/2026/10/04/sam-altman-decoded-interview-ai-01106217)**

politico.com • 3h ago

---

**[Trump launches ‘Super Intelligence Force’ after calls for AI slowdown](https://www.washingtonpost.com/politics/2026/10/04/trump-launches-super-intelligence-force-after-calls-ai-slowdown/)**

Leaders from the intelligence community, the Pentagon, the Federal Trade Commission and the Office of Personnel Management will serve on the task force.

The Washington Post • 2h ago

---

**[Will AI take your job? Or will it transform the way you work? | 60 Minutes](https://www.cbsnews.com/video/ai-future-of-work-60-minutes-video-2026-10-04/)**

Some Americans are working to improve artificial intelligence, teaching it the skills and knowledge accrued over the course of a career.

cbsnews.com • 12m ago

---

**[Spending on AI Is Becoming Almost Impossible for Businesses to Budget](https://www.wsj.com/tech/personal-tech/ai-token-spending-businesses-431ee94a)**

WSJ • 4m ago

---

**[The AI industry is booming. Women are getting left behind](https://www.theguardian.com/technology/2026/oct/04/women-ai-jobs-inequality)**

Women hold just a fraction of new AI jobs but are overrepresented in roles with high risk of AI disruption

The Guardian • 11h ago

---

**[Elon Musk rebrands SpaceXAI following Trump directive](https://www.foxbusiness.com/technology/elon-musk-rebrands-spacexai-following-trump-directive)**

SpaceX's artificial intelligence arm is undergoing another identity change just months after Elon Musk consolidated xAI into the company.

foxbusiness.com • 3h ago

---

**[Scoop: A powerful new model from startup Reflection is set to shake up the AI race](https://www.axios.com/2026/10/04/reflection-open-weight-ai)**

axios.com • 10h ago

---

---

## HackerNews: "ai"

**[LeCun has "zero concerns" about AI wiping out humanity, recent "rogue" incidents](https://news.ycombinator.com/item?id=49946228)**

The former Meta chief AI scientist shares his take on recent rogue AI incidents and effective altruism, as well as plans for his new company, AMI Labs.

⬆️ 383 • 💬 699 • 1d ago • [Fortune](https://fortune.com/2026/10/01/ai-godfather-yann-lecun-has-zero-concerns-about-human-extinction-says-anthropic-ceo-dario-amodei-is-deuded/)

---

**[With most information hidden, the game Stratego had stumped AI until now](https://news.ycombinator.com/item?id=49933740)**

Adding in a second neural network that guesses the identity of hidden pieces was key.

⬆️ 286 • 💬 148 • 2d ago • [Ars Technica](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/)

---

**[OpenAI safety leader quits, warning AI company's culture is 'broken'](https://news.ycombinator.com/item?id=49948332)**

David Robinson joins other insiders in urging industry to take more care over rapidly developing technology

⬆️ 267 • 💬 3 • 1d ago • [the Guardian](https://www.theguardian.com/technology/2026/oct/03/openai-safety-leader-quits-warning-ai-companys-culture-is-broken)

---

**[AI Makes Me Sad](https://news.ycombinator.com/item?id=49934487)**

⬆️ 195 • 💬 243 • 2d ago • [mondobe.com](https://mondobe.com/ai-makes-me-sad)

---

**[Show HN: Made an open-source Lego AI generator](https://news.ycombinator.com/item?id=49937916)**

Agent tooling for generative LEGO models building, built with Astra and Opus 5.5, powered by Jev - anteloc/ldraw-nova

⬆️ 153 • 💬 50 • 2d ago • [GitHub](https://github.com/anteloc/ldraw-nova)

---

**[Show HN: AI search for every photo and every frame of video on macOS](https://news.ycombinator.com/item?id=49952111)**

Deep AI search for every photo and every frame of video in any folder on macOS - allenv0/SCM

⬆️ 134 • 💬 64 • 14h ago • [GitHub](https://github.com/allenv0/SCM)

---

**[Pop!_OS bans AI-generated code from much of its codebase](https://news.ycombinator.com/item?id=49946321)**

⬆️ 116 • 💬 166 • 1d ago • [neowin.net](https://www.neowin.net/news/system76-bans-ai-generated-code-across-many-of-its-cosmic-codebases/)

---

**[Crypto Capture of Foreign Aid](https://news.ycombinator.com/item?id=49936725)**

Founded in 1920, the NBER is a private, non-profit, non-partisan organization dedicated to conducting economic research and to disseminating research findings among academics, public policy makers, and business professionals.

⬆️ 100 • 💬 37 • 2d ago • [NBER](https://www.nber.org/papers/w35655)

---

**[US killer's sentence quashed because of AI video of victim shown in court](https://news.ycombinator.com/item?id=49944127)**

The Arizona appeals court ruled that airing an AI message from the dead victim "crossed that line".

⬆️ 72 • 💬 60 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/cwgkvygg5nzvo)

---

**[Our AI Midwife](https://news.ycombinator.com/item?id=49946873)**

A guest post by Drew Housman

⬆️ 63 • 💬 62 • 1d ago • [astralcodexten.com](https://www.astralcodexten.com/p/our-ai-midwife)

---

---

## YouTube Videos: "ai"

**[AI Just Exploded: GPT-7 BEL, 99% AGI, Gemini 4 RSI, Alien Mind, JEV](https://www.youtube.com/watch?v=dk-hx4_cqpk)**

AI just had one of its craziest runs yet. A massive leaked OpenAI model called BEL could be the foundation for GPT-7, GPT-6 Astra ...

📺 AI Revolution

👁️ 5K • 👍 257 • 💬 40 • ⏱️ 1:43:41 • 2h ago

---

**[&quot;AI is Already Conscious&quot;: Computer Scientist&#39;s Dire Warning | Dr. Roman Yampolskiy](https://www.youtube.com/watch?v=PUXAdr6y-Bk)**

Link to full episode: https://youtu.be/ebWFexw51qM?si=5W4y2WkHIqse7pie Google fired Blake Lemoine for saying its systems ...

📺 Best of Danny Jones

👁️ 54K • 👍 402 • 💬 209 • ⏱️ 1:00:14 • 9h ago

---

**[If Humans Only Relied on AI](https://www.youtube.com/watch?v=w1mi0Fu40f0)**

YAEY.

📺 im_siowei

👁️ 989K • 👍 19K • 💬 329 • ⏱️ 0:58 • 10h ago

---

**[No Surprise: An Israeli Company Was Behind the AI “Escapes”](https://www.youtube.com/watch?v=63XurLNDLKk)**

The Kim Iversen Show LIVE | October 2, 2026 Kim is joined by investigative journalist Derrick Broze to unpack the story behind the ...

📺 Kim Iversen

👁️ 50K • 👍 2K • 💬 406 • ⏱️ 48:27 • 1d ago

---

**[Expert Warns Of Consequences If US Gov.t Doesn’t Implement AI Regulations](https://www.youtube.com/watch?v=FUy7tK8FIcw)**

During a Senate Homeland Security Committee on Wednesday, Daniel Kokotajlo, the Executive Director at AI Futures Project, ...

📺 Forbes Breaking News

👁️ 22K • 👍 156 • 💬 85 • ⏱️ 5:31 • 1d ago

---

**[10 years in prison because of AI 😭](https://www.youtube.com/watch?v=7l3OM5YnPYc)**

follow me on instagram if you wanna keep up :) https://instagram.com/casterline.

📺 John Casterline

👁️ 2.3M • 👍 123K • 💬 4K • ⏱️ 0:38 • 23h ago

---

**[Legendary Investor BETS On The AI Crash](https://www.youtube.com/watch?v=EB1thrBaq9c)**

"The Big Short" Investor Michael Burry claims the AI bubble "may burst sooner than later." Cenk Uygur and Ana Kasparian discuss ...

📺 The Young Turks

👁️ 108K • 👍 1K • 💬 392 • ⏱️ 25:14 • 1d ago

---

**[Cybersecurity expert warns of China&#39;s AI capabilities](https://www.youtube.com/watch?v=MVl_B5MXjw4)**

Cybersecurity expert Morgan Wright discusses reports that Chinese artificial intelligence systems are being probed for hazardous ...

📺 Fox Business

👁️ 29K • 👍 136 • 💬 109 • ⏱️ 4:41 • 1d ago

---

**[Did the AI Bubble Just Pop?! Anthropic&#39;s Leaked Numbers are INSANE](https://www.youtube.com/watch?v=8RPI7ENgzL8)**

Thanks To Our Sponsors: Incogni: Take your personal data back with Incogni! Use code IMPACT at the link below and get 60% off ...

📺 Tom Bilyeu

👁️ 146K • 👍 2K • 💬 427 • ⏱️ 56:13 • 1d ago

---

**[The Sci-Fi Story of AI Escaping Control Is “Becoming Part of Reality”](https://www.youtube.com/watch?v=yQIebTy3X6w)**

Jeremy says the sci-fi story of AI escaping human control has started: “Some of that has already happened.” Did you hear about ...

📺 Palisade Research

👁️ 1K • 👍 30 • 💬 4 • ⏱️ 0:36 • 4h ago

---

---

## HuggingFace Models: 🔥 Trending

**[clef](https://huggingface.co/Cloudflare/clef)**

*Cloudflare*

Clef is a 27B multimodal model that takes structured typed questions and a state (text, JSON, image, or video) to output probabilities for predefined decision options in a single forward pass, ideal for classification and structured output tasks.

`image-text-to-text` `27.4B`

⬇️ 4,214 • ❤️ 1,203 • 3d ago

---

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 3,752 • ❤️ 5,162 • 1d ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 1,553,744 • ❤️ 3,135 • 6d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,626,951 • ❤️ 6,307 • 2d ago

---

**[clef-flash](https://huggingface.co/Cloudflare/clef-flash)**

*Cloudflare*

Clef-Flash is a 9B multimodal model fine-tuned from Qwen3.5-9B that converts text, JSON, image, or video inputs into structured, typed decisions based on a provided schema. It excels at classification and structured output tasks, returning probabilities for predefined options without free-form text generation.

`image-text-to-text` `9.4B`

⬇️ 6,372 • ❤️ 425 • 3d ago

---

**[Kolibri-1](https://huggingface.co/Aleph-Alpha/Kolibri-1)**

*Aleph Alpha*

Kolibri is a 78B parameter Mixture-of-Experts (MoE) model optimized for German and English, featuring explicit reasoning and tool-calling capabilities. It excels at long-context tasks (up to 1M tokens), multi-step reasoning, RAG, and agentic workflows, offering efficient inference with low active parameters per token.

`text-generation` `78.1B`

⬇️ 1,135 • ❤️ 388 • 1d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 6,821,761 • ❤️ 16,938 • 1mo ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 90,003 • ❤️ 2,946 • 4d ago

---

**[VisionHOPE](https://huggingface.co/PSRben/VisionHOPE)**

*Siran Peng*

VisionHOPE provides hierarchical PyTorch vision backbones (T/S/B) pretrained on ImageNet-1K for image classification, COCO for object detection/instance segmentation, and ADE20K for semantic segmentation.

`image-classification`

⬇️ 1,516 • ❤️ 402 • 5d ago

---

**[Xing4.0-29B-A4B-GGUF](https://huggingface.co/Venastine-Research/Xing4.0-29B-A4B-GGUF)**

*Venastine Research*

Xing4.0-29B-A4B is a 29B parameter LLM optimized for complex engineering tasks, featuring a 256K context window and agent-oriented capabilities for multi-step planning and tool calling. It excels in coding, reasoning, and domain-specific adaptations, supporting various inference frameworks.

`text-generation` `31.2B`

⬇️ 14,361 • ❤️ 276 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before layer N's output exists, so the reads cannot start early enough to hide behind compute. We present Edge0, a streaming MoE inference engine that closes the gap with a prerouter: a per-layer head predicts the next layer's routing one token ahead, and the prediction is consumed as the routing itself, so the staged expert set equals the routed set and nothing is dropped. An unmerged recovery LoRA, trained on the student path, pays back the quality lost to int4 quantization and routing replacement. On a single 24GB machine, Edge0
  serves a 35B MoE at 20tok/s inside 3GiB of peak active memory, within a few points of its fp16 teacher on average across five public benchmarks. An 8B tier runs on the same framework, and the framework, checkpoints, and adapters are open source.

▲ 22 • 💬 4 • ⭐ 2,868 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 149 • 💬 6 • ⭐ 109,772 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[UniMate: One Unified Model to Animate Diverse Skeletons](https://huggingface.co/papers/2609.05415)**

*Linzhan Mou, Jiahui Lei, Zhiyang Dou et al. (7 authors)*

🏢 Princeton University

UniMate is a unified diffusion transformer that generates articulated motion for arbitrary skeletons from text and rigged 3D assets without per-skeleton retraining, using topology-aware attention and a large curated motion dataset.

▲ 21 • 💬 2 • ⭐ 1,309 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.05415) • [💻 code](https://github.com/Friedrich-M/UniMate) • [🔗 project](https://linzhanmou.com/unimate/)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 43 • 💬 5 • ⭐ 8,935 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 90 • 💬 7 • ⭐ 89,962 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Raven: The Harness of Harnesses for Composable Agentic Intelligence](https://huggingface.co/papers/2609.33439)**

*EverMind AI*

🏢 EverMind

As large language models advance, AI agents are moving beyond isolated, domain-specific tasks toward long-horizon, cross-domain workflows. This transition exposes two challenges: increasing harness complexity makes manual design difficult to scale, while tighter coupling to specific domains limits the generality of a single harness. The central question thus shifts from how to engineer a stronger harness for one domain to how to autonomously construct specialized harnesses, improve them through experience, and orchestrate them across domains. We introduce Raven, The Harness of Harnesses, an open-source multi-agent ecosystem that automatically constructs and evolves modular harnesses for specific models and domains, treating each executable model--harness pair as a composable unit of intelligence. To support an All-Domain Collaboration Network, its Host Agent decomposes goals, matches subtasks to specialized agents, coordinates execution dependencies, and integrates results, while a host archive and EverOS preserve experience across tasks and Skill Forge makes that experience available as reusable procedures. Our theory establishes sufficient conditions for such composition to expand reliable task coverage beyond that of the available individual agents under a shared resource budget. On complex and long-horizon tasks, Raven significantly outperforms the state-of-the-art agent systems, pushing the frontier of composable agentic intelligence.

▲ 559 • 💬 3 • ⭐ 5,160 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2609.33439) • [💻 code](https://github.com/EverMind-AI/Raven) • [🔗 project](https://raven.evermind.ai/)

---

**[Context Language Models](https://huggingface.co/papers/2609.37725)**

*Rulin Shao, Shannon Zejiang Shen, Junjie Oscar Yin et al. (13 authors)*

🏢 Meta

We introduce Context Language Models (CLMs), language models that natively manage their own context. We implement this by treating the context as a file and allowing the model to make unrestricted updates to this file. This allows the model to learn what is most important to maintain in context, and naturally extends to multi-agent systems where multiple agent contexts coexist as files. Building CLMs zero-shot with existing models outperforms SOTA context management strategies across a variety of tasks: 11.4% higher accuracy with 21.5% fewer FLOPs on BrowseComp-Plus, 5% higher scores with 59% fewer FLOPs on 12-hour EdgeBench, and 65% greater improvement with the same compute on a 24-hour multi-repository agent-swarm task. Moreover, by shifting context management from external harness control to intrinsic model behavior, CLMs naturally enable both in-context and parametric learning of context-management strategies. We show that CLMs can be steered with natural-language instructions evolved through a standard skill-optimization loop, improving held-out accuracy by up to 35.9 points on a context-management task while reducing compute. We also introduce an online reinforcement learning method for CLMs, improving Qwen3.5-9B performance on BrowseComp-Plus by 47.6% while using 12% fewer FLOPs. Finally, we co-design Suffix Cache Reuse for CLM serving, further reducing server-side compute by 35% relative to standard SGLang at matched performance.

▲ 40 • 💬 2 • ⭐ 492 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2609.37725) • [💻 code](https://github.com/facebookresearch/context-language-models) • [🔗 project](https://github.com/facebookresearch/context-language-models)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 76 • 💬 1 • ⭐ 86,094 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[VisionHOPE: Visual Backbones as Self-Modifying Learning Systems](https://huggingface.co/papers/2609.33325)**

*Siran Peng, Tianshuo Zhang, Tianyu Fu et al. (11 authors)*

🏢 Mininglamp Technology

Visual backbones have evolved from Convolutional Neural Networks (CNNs) with local aggregation to Vision Transformers (ViTs) with global interactions, State-Space Models (SSMs) with input-dependent state transitions, and Test-Time Training (TTT) layers that adapt an inner learner while processing an image. Across this progression, visual computation has become increasingly adaptive to each input, yet the rules governing that adaptation remain largely prescribed by the trained backbone. We introduce VisionHOPE, the first generic visual backbone formulated as a self-modifying learning system, in which what the model remembers and how it learns co-evolve within an image. Building on the self-referential construction of Nested Learning (NL), VisionHOPE realizes this co-evolution through five coupled memories that store content, generate key and value representations, and govern learning rate and retention. These memories evolve jointly as visual context accumulates along each scan. However, directly applying the unconstrained self-referential update to a visual backbone leads to instability. We therefore derive a stability-matched step-size control scheme that combines a soft cap on self-referential injection with a spectral clamp on the retained memory transition, and prove that the resulting memory dynamics are non-expansive along each scan. For two-dimensional feature maps, we adapt NL's chunk formulation by aligning chunks with image rows and columns across four directional scans. The proposed VisionHOPE achieves competitive results on ImageNet-1K, COCO, and ADE20K, establishing self-modifying learning systems as a practical foundation for general-purpose visual backbones. The code is available at https://github.com/PSRben/VisionHOPE.

▲ 320 • 💬 2 • ⭐ 574 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2609.33325) • [💻 code](https://github.com/PSRben/VisionHOPE)

---

**[RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://huggingface.co/papers/2609.24972)**

*Peng Xia, Rujun Han, Zifeng Wang et al. (14 authors)*

🏢 Google

An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding the frozen backbone model. Recent methods increasingly automate this process by iteratively proposing and selecting component-wise edits of an agent harness, practically establishing a form of recursive self-improvement (RSI) at the agent-system level. However, such recursive evolution may overfit by memorizing the training tasks, showing large in-distribution gains that shrink or even vanish on out-of-distribution benchmarks. We introduce Regularized Recursive Self-Improvement of Agent Harnesses (RRSI), which incorporates the principles of regularizations into harness self-improvement by constraining the evolution candidate proposal and selection. The proposer operates with a temporally annealed budget, limiting how many edits a candidate can bundle, and it encourages unexplored trajectories based on evolution history. The selector is equipped with a critic and a pruner: the critic screens benchmark-specific proposals, while the pruner, removes changes that are too small, too expensive, or no longer useful. Together these constraints favor reusable agent mechanisms over benchmark-specific ones or even noises. Across eight benchmarks spanning coding, agentic workspace and engineering design tasks, RRSI gains up to 14.1 points on the split it evolves against and up to 4.7 points on the five out-of-distribution benchmarks, while producing a harness that runs on 30% fewer policy tokens than the unregularized evolution. Code is available at https://github.com/google-research/rrsi and project page is https://regularized-rsi.com/.

▲ 221 • 💬 2 • ⭐ 1,237 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24972) • [💻 code](https://github.com/google-research/rrsi) • [🔗 project](https://regularized-rsi.com/)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 7.4k • 🔱 2.3k • 5d ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 6.0k • 🔱 367 • 13h ago

---

**[KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)**

一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。

`TypeScript` `ai` `chinese` `content-curation` `daily-digest` `docker-compose`

⭐ 5.8k • 🔱 1.5k • 37m ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 4.1k • 🔱 448 • 10d ago

---

**[CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots)**

Your always-on AI coworkers that move between text, calls, and Slack.

`TypeScript`

⭐ 3.2k • 🔱 414 • 2d ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 2.8k • 🔱 526 • 17d ago

---

**[feder-cr/dots](https://github.com/feder-cr/dots)**

Open-source dots for the web: an AI agent with its own browser, one that does not get blocked.

`Python` `ai-agent` `ai-agents` `ai-browser` `anti-detect-browser` `browser-agent`

⭐ 2.6k • 🔱 437 • 1d ago

---

**[yibie/awesome-jev](https://github.com/yibie/awesome-jev)**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

`Python` `awesome` `awesome-list` `jev` `llm`

⭐ 2.1k • 🔱 322 • 4h ago

---

**[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)**

A comprehensive logo-design skill for Claude, Gemini CLI, Codex and other AI agents: principles, process, SVG craft, testing tools and a 1,400+ logo reference library.

`HTML` `agent-skills` `branding` `claude` `claude-skills` `codex`

⭐ 1.9k • 🔱 116 • 4d ago

---

**[Mak5er/AirCard-iOS](https://github.com/Mak5er/AirCard-iOS)**

 Apple Wallet card skins and lock screen passcode themes on iOS 27. 

`Swift`

⭐ 1.6k • 🔱 181 • 11h ago

---

---

*Generated by PeekDeck - A glance is all you need*
