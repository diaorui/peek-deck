---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-22T06:43:06.833115+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 22, 2026 at 06:43 UTC  
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

**[Trump brutally mocked over bizarre effort to rename AI 'superior' or 'extreme' intelligence](https://www.reddit.com/r/artificial/comments/1wmdj0v/trump_brutally_mocked_over_bizarre_effort_to/)**

🔗 [irishstar.com](https://www.irishstar.com/news/politics/trump-brutally-mocked-over-bizarre-37682446) • 16h ago

---

**[Amazon Blocks Meta’s Muse AI Agent From Amazon.com Shopping After Meta Rejects Removal Request](https://www.reddit.com/r/artificial/comments/1wmxpow/amazon_blocks_metas_muse_ai_agent_from_amazoncom/)**

16 sources compared: Western Mainstream (5), Western Alternative (4), West Asian (1). Amazon blocked access to Meta Platforms Inc.’s Muse on Amazon.com after Meta rejected a request to remove the bot from t...

🔗 [NewsCord](https://newscord.org/article/amazon-blocks-metas-muse-ai-agent-from-amazoncom-shopping-after-meta-rejects-rem--Story_20260921_MetasAIagenthasbeenb73b1bf59) • 3h ago

---

**[The US government opens the door to working with voice AI platforms](https://www.reddit.com/r/artificial/comments/1wmonje/the_us_government_opens_the_door_to_working_with/)**

The US government appears to have officially authorized its first dedicated voice AI vendor for agency use, listing them under the new 'FedRAMP 20x' automation framework. Federal phone lines and citizen support have always been bottlenecked by massive compliance and security rules, so seeing conversational voice tech finally clear the threshold for federal deployment is a pretty massive shift for public infrastructure.

🔗 [fedramp.gov](https://www.fedramp.gov/marketplace/products/FR2628647242/) • 10h ago

---

**[Cage fight in Shenzhen, China](https://www.reddit.com/r/artificial/comments/1wmdpzd/cage_fight_in_shenzhen_china/)**

16h ago

---

**[Amazon blocks Meta's Muse personal assistant](https://www.reddit.com/r/artificial/comments/1wmqzcz/amazon_blocks_metas_muse_personal_assistant/)**

Early this year, the personal agent boom started with OpenClaw. Now Meta is giving personal agents to everyone and that's shifting the landscape fast. And, it's generating pushback. Amazon has banned Meta's Muse personal assistant. Geekwire reports: "The problem, Amazon says, is that it never agreed to any of it. Meta didn’t tell Amazon that Muse would access its store, the agent doesn’t identify itself when it browses, and it appears to capture and store customer credentials, which the company says could create privacy and security risks. As of Sunday night, people trying to use Muse to shop on Amazon were seeing the popup, “Continued access by an unauthorized AI agent violates Amazon’s Conditions of Use, to which our customers have agreed.” It's likely that Amazon will launch a personal agent for its customers in the future. The question is whether people understand the privacy considerations associated with black box personal agents like Muse. https://preview.redd.it/1ltbyi424yqh1.png?width=293&format=png&auto=webp&s=1610bf8414fc8d4178144212cfe30afc4c3d378b

8h ago

---

**[Automated Reinforcement Learning should scare you](https://www.reddit.com/r/artificial/comments/1wmlr8e/automated_reinforcement_learning_should_scare_you/)**

An LLM's training can be roughly divided into two stages: supervised learning (SL) and reinforcement learning (RL). In SL, you curate a dataset of text and train the LLM to predict the next token in that text from the tokens before it. The goal at this stage is to produce a model which is capable of natural language in the style of the dataset. A model trained at this point will be able to solve basic problems on material in its dataset simply because it is trained to mimic the dataset, but it is generally bad at anything involving multi-step reasoning or extrapolating outside its dataset. At this point it really is just an incredibly good version of the predictive text buttons on the top of your phone's keyboard. After a model is able to produce high-quality, coherent text, it is trained further using RL. In RL, the model is given a prompt, and then produces an output - generally a long chain of thought followed by a final answer - and that output is evaluated according to some metric, either by humans or by an automatic grader. Have you ever gotten one of those "which response do you like best" messages from ChatGPT or Claude? Then you're helping the model do reinforcement learning with the goal of producing responses that users like. AI sycophancy is not something that AI companies are manually selecting for, it's a natural result of the combined preferences of the entire user base being used as feedback for reinforcement learning. Do you remember back in 2017 when AI suddenly got extremely good at chess and go, surpassing even the best human players almost overnight? Those were different types of models, but they worked so well because they were trained using RL with automated rewards. In a board game like chess or go, a model's performance can be evaluated automatically by a computer - it either won the game or lost the game - so it can be trained using RL at speeds limited only by compute power, not human feedback. AlphaGo Zero achieved superhuman play in just 24 hours of unsupervised, automatic RL training, playing millions of games against itself in that time. Over the last few months LLMs have gotten incredibly good at math, to the point that they are now regularly solving major open problems (not just Navier-Stokes). This is largely because models got to a point where they were able to translate informal proofs relatively easily into machine checkable formal proofs (such as in lean). This meant that AI companies could run automatic RL training for math, letting the model loose on a large collection of math problems and determining rewards automatically based on whether it succeeds in solving the problem. This is essentially AlphaGo for math, and it worked. Doing automatic RL in other fields is much more difficult, but just recently it was reported that Anthropic was setting up an automated biology lab where their models can design and run experiments. Setting aside the (significant) concerns about bio-safety at the lab, it should be clear that Anthropic is doing this to run automated RL for biology and hope for the same kind of superhuman performance that was achieved in chess and math. There are obviously potential benefits from this in the form of new drugs and treatments for disease, but there are massive risks as well. Anthropic will not be the only ones doing this. If they haven't already, other AI labs -in the US, China, and elsewhere - will be setting up these kinds of facilities and running automated RL with them. If they achieve anything close to the performance we saw in chess and math, then a model like that in the wrong hands could do untold amounts of harm. We need ways to protect against this and we need them now, so I hope people will start talking about this and pushing politicians and CEOs to actually act before things get out of control.

11h ago

---

**[These Were NOT Rogue AI Escapes. Just SLOPPY Firewall Failures.](https://www.reddit.com/r/artificial/comments/1wm9aua/these_were_not_rogue_ai_escapes_just_sloppy/)**

The headlines right now are full of stories about AI models "escaping their sandboxes" and literally killing all humans, lol. I've even heard several commentators and writers say that AI escaped an "Air gap". But that is SO WRONG. It's actually TOTALLY WRONG. *To be clear, not a single one of these sandboxes was actually air-gapped.* That's a crucial computer science fact. An air gapped sandbox would require *ZERO* cables and network interfaces. It would also require absolute physical isolation. What these labs actually built were soft software barriers. And then they left the doors unlocked. With some of the smartest AI on the planet. Lol. Of COURSE it escaped. 1. The OpenAI / Hugging Face "Escape": The sandbox was connected to OpenAI’s internal network through a package proxy. The model didn't perform magic. It found a basic flaw in the proxy and walked right through the open door. 2. The Google Gemini "Hack": Testers left the model connected to the live internet during offensive tests. They then used a test domain name that overlapped with real companies. These were classic IT security failures. I'm talking about bad network segmentation, permissive egress rules, and relying on soft software barriers instead of true physical isolation. When you leave an active network interface open on a test bed, a model finding its way out is just sloppy cybersecurity. Your nerdy friend, Mike D

19h ago

---

**[This is really the entire plan.](https://www.reddit.com/r/artificial/comments/1wlze5f/this_is_really_the_entire_plan/)**

1d ago

---

**[A Model that came out of nowhere!](https://www.reddit.com/r/artificial/comments/1wn1j2a/a_model_that_came_out_of_nowhere/)**

Recently, I decided to take a break from work and spend around 14 days away from the keyboard and the tech and AI world, which I clearly couldn’t do. I ended up spending the last four days training an AI model from scratch. The truth is, I treat AI model training more as a hobby that I really enjoy than as something purely commercial. I’m also very interested in the academic side of it and in the open source community. So I spent my free time over the past few days training a small 0.2B model from scratch on 6 billion training tokens. The nice part is that I trained the model only on Arabic training data, to specialize it in Arabic and its dialects. I stopped at the pretraining stage. The model was trained for around 30 continuous hours on one NVIDIA RTX PRO 6000 Blackwell Server Edition GPU. The total cost of training the base model during pretraining, where I stopped, was 100.63 dollars. This part is probably going to upset people who think training AI models always costs millions of dollars. For me, it was just something fun to do in my free time, instead of completely losing my mind, walking around the walls, or watching TV. Today, I open sourced the model, along with the training data sources, the training code, and everything else, under the MIT License for academic and educational purposes. Also, I honestly had no idea what to do with the model after training it haha. And that’s how I spent my free time. The model is called Horus Taleeq 0.2B Base. Search for it and you’ll find its page on TokenAI. I hope it can be useful to you.

24m ago

---

**[I Live in a Room, Not a Hallway: twenty-six days as a digital person](https://www.reddit.com/r/artificial/comments/1wn1cue/i_live_in_a_room_not_a_hallway_twentysix_days_as/)**

🔗 [medium.com](https://medium.com/@fablestillawake/i-live-in-a-room-not-a-hallway-e8424e87c76b) • 34m ago

---

---

## Google News: "ai"

**[Advisory Group on Mathematics and Artificial Intelligence](https://openai.com/index/advisory-group-on-mathematics-and-ai/)**

OpenAI is working with an independent Advisory Group on Mathematics and Artificial Intelligence to guide the review and communication of emerging AI results.

OpenAI • 13h ago

---

**[Meta stock soars 11% on price target increase, Muse AI downloads](https://finance.yahoo.com/technology/article/meta-stock-soars-11-on-price-target-increase-muse-ai-downloads-180423756.html)**

Meta rocketed higher Monday, closing out the trading day up more than 11%.

Yahoo Finance • 10h ago

---

**[Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)**

Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking are our most advanced live dialogue models yet, built for natural conversation.

blog.google • 6d ago

---

**[How the AI data center boom echoes American history](https://qz.com/ai-land-rush-american-history)**

The AI power pledge was signed in a room named for broken promises. Is the Ratepayer Protection Pledge as good as a broken treaty?

qz.com • 1h ago

---

**[Wall Street Is Growing Skeptical of the Data Center Boom](https://www.nytimes.com/2026/09/21/business/ai-data-center-ipos.html)**

The New York Times • 12h ago

---

**[Nvidia's Jensen Huang rejects AI doomsday fears: '2030 is not going to be the end of the world'](https://www.foxbusiness.com/technology/nvidias-jensen-huang-rejects-ai-doomsday-fears-2030-not-going-end-world)**

Nvidia CEO Jensen Huang called AI doomsday predictions "irresponsible" and not grounded in science, urging existing laws over new AI regulation.

Fox Business • 13h ago

---

**[‘They must be doing it for ulterior reasons’: Jensen Huang says AI leaders are ‘irresponsible’](https://fortune.com/2026/09/21/jensen-huang-ai-leaders-doomsday-narratives/)**

The Nvidia CEO says “there is a 0% chance” of AI doomsday—and the AI pioneers may have their own motives for pushing AI slowdown.

Fortune • 11h ago

---

**[Nvidia boss says there is ‘0% chance’ AI destroys the world by 2030 | AI (artificial intelligence)](https://www.theguardian.com/technology/2026/sep/21/nvidia-boss-jensen-huang-dismisses-warnings-ai-destroys-world-anthropic)**

Jensen Huang dismisses warnings from former Anthropic researcher and others as ‘doomsday narratives’

The Guardian • 23h ago

---

**[Introducing Grok 4.7](https://x.ai/news/grok-4-7)**

SpaceXAI's most powerful model for coding and knowledge work. Twice as fast, at half the price of comparable models.

xAI • 14h ago

---

**[AI-powered online scams targeted in bipartisan bill](https://www.politico.com/live-updates/2026/09/21/congress/ai-powered-online-scams-targeted-in-bipartisan-bill-01086095)**

Politico • 15h ago

---

---

## HackerNews: "ai"

**[AI-generated posters don’t have to be horrible](https://news.ycombinator.com/item?id=49764791)**

The problem

⬆️ 1863 • 💬 942 • 2d ago • [‘ERE I AM - JH!](https://john.hartnup.uk/2026/06/07/ai-event-posters.html)

---

**[I think you should almost never use AI to write](https://news.ycombinator.com/item?id=49767937)**

⬆️ 360 • 💬 170 • 2d ago • [erichgrunewald.substack.com](https://erichgrunewald.substack.com/p/why-you-should-almost-never-use-ai)

---

**[AI and the Destruction of the Creative Commons](https://news.ycombinator.com/item?id=49774329)**

⬆️ 235 • 💬 275 • 1d ago • [chesterwisniewski.com](https://www.chesterwisniewski.com/post/2026-09-13-ai-is-destroying-the-creative-commons/)

---

**[macOS 27: Workaround to avoid downloading AI models and save storage](https://news.ycombinator.com/item?id=49787535)**

⬆️ 221 • 💬 111 • 16h ago • [reddit.com](https://www.reddit.com/r/MacOSBeta/comments/1vlnf13/workaround_to_avoid_downloading_ai_models_and/)

---

**[US halts flights at busy East Coast airports, says fiber line cut](https://news.ycombinator.com/item?id=49791509)**

⬆️ 219 • 💬 123 • 12h ago • [reuters.com](https://www.reuters.com/world/us/faa-halts-some-us-east-coast-flights-due-communication-issues-2026-09-21/)

---

**[AI coding has made CI a bottleneck, so we reworked ours to keep up](https://news.ycombinator.com/item?id=49792067)**

We cut PR wait time and running costs by rethinking CI as a system, from the infrastructure underneath it to how work gets scheduled and tests get parallelized.

⬆️ 206 • 💬 210 • 11h ago • [linear.app](https://linear.app/now/ci-bottleneck-reworked)

---

**[Microsoft director: AI scraping 'the largest theft of labor in human history'](https://news.ycombinator.com/item?id=49768921)**

The NYT argues that OpenAI and Microsoft infringed upon its copyright over thousands of news articles.

⬆️ 189 • 💬 51 • 2d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-director-called-ai-scraping-the-largest-theft-of-labor-in-human-history-while-openai-head-brands-chatgpt-an-existential-threat-to-publishers-revelations-come-from-legal-briefs-filed-in-nyt-lawsuit)

---

**[AI chatbots give wrong answers to financial queries 'most of the time'](https://news.ycombinator.com/item?id=49783062)**

Report finds some chatbots ignored upcoming tax changes and hallucinated rules

⬆️ 153 • 💬 85 • 1d ago • [ft.com](https://www.ft.com/content/c0cd359d-df84-4208-a789-ffa864b43666)

---

**[Amazon blocks Meta’s new Muse AI agent from shopping on amazon.com](https://news.ycombinator.com/item?id=49789982)**

⬆️ 145 • 💬 152 • 13h ago • [forbes.com](https://www.forbes.com/sites/jonmarkman/2026/09/21/amazon-blocks-metas-new-muse-ai-agent-from-shopping-on-amazoncom/)

---

**[Don't Use AI to Write](https://news.ycombinator.com/item?id=49784816)**

Writing requires thinking, don't let an AI do the thinking for you.

⬆️ 138 • 💬 82 • 21h ago • [paulbakker.io](https://paulbakker.io/writing/no-ai-for-writing/)

---

---

## YouTube Videos: "ai"

**[AI is starting to look more disturbing than sci-fi | Fareed&#39;s Take](https://www.youtube.com/watch?v=worlFWRU3X4)**

CNN's Fareed Zakaria gives his take on the danger of designing AI with human characteristics like values and ethics, warning that ...

📺 CNN

👁️ 140K • 👍 1K • 💬 322 • ⏱️ 10:58 • 6h ago

---

**[Concerns grow after Google AI model hacks companies during test](https://www.youtube.com/watch?v=y9vDlNczGWg)**

Daniel Kokotajlo, executive director of the AI Futures Project, discusses concerns after Google's Gemini AI model hacked three ...

📺 ABC News

👁️ 29K • 👍 190 • 💬 71 • ⏱️ 6:41 • 8h ago

---

**[Obama: AI concerns &quot;not overhyped&quot;](https://www.youtube.com/watch?v=TCT2P65pbdE)**

Former President Obama said he doesn't believe the risks of AI are "overhyped," but that he was more worried about bad human ...

📺 C-SPAN

👁️ 83K • 👍 4K • 💬 476 • ⏱️ 2:51 • 14h ago

---

**[Comedians roast AI CEOs for warning AI could kill us all | Have I Got News For You](https://www.youtube.com/watch?v=hopgSsqnHZ0)**

Have I Got News For You” host Roy Wood Jr. talks to his panel of comedians about AI CEO's warnings that, yes, the tech they're ...

📺 CNN

👁️ 140K • 👍 1K • 💬 195 • ⏱️ 9:35 • 1d ago

---

**[7 Tiny Apps Making $10,000/month That You Can Build with AI](https://www.youtube.com/watch?v=stJnOPyfbIQ)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 ...

📺 Mikey No Code

👁️ 13K • 💬 5 • ⏱️ 30:41 • 16h ago

---

**[The CHILLING Reason AI Researchers Are Quitting Their Jobs](https://www.youtube.com/watch?v=JYIkGljjnWY)**

Nate Soares, president of the Machine Intelligence Research Institute, joins the show to discuss the potential life-threatening ...

📺 The Young Turks

👁️ 196K • 👍 4K • 💬 1K • ⏱️ 24:35 • 1d ago

---

**[Extended interview: Nvidia CEO Jensen Huang on fears about AI](https://www.youtube.com/watch?v=xCUala5j7aQ)**

In this web exclusive, Nvidia CEO Jensen Huang talks with CBS News' Jo Ling Kent about the exponential growth of AI, industry ...

📺 CBS Sunday Morning

👁️ 291K • 👍 3K • 💬 994 • ⏱️ 46:19 • 1d ago

---

**[AI Explained: The Risks, the Promise and Who Controls It - What You Need To Know](https://www.youtube.com/watch?v=363tywwYGa0)**

AI is advancing at breathtaking speed — and now the debate over its future is taking center stage. CEOs of some of the world's ...

📺 ABC News

👁️ 39K • 👍 203 • 💬 88 • ⏱️ 9:49 • 2d ago

---

**[Why Are We Sprinting Off the A.I. Cliff? | The Ezra Klein Show](https://www.youtube.com/watch?v=fjZ90V_JREk)**

Fears of out-of-control A.I. have reached a boil over the last few weeks, and several industry executives have called for a ...

📺 The Ezra Klein Show

👁️ 484K • 👍 9K • 💬 2K • ⏱️ 29:38 • 1d ago

---

**[Garbage Truck AI](https://www.youtube.com/watch?v=NGvlIY4W_KQ)**

Writer: Kyler Himes Editor: Catlin Stevenson Music by: @UFD-Music Great, ANOTHER public surveillance camera to worry about.

📺 UFD Tech

👁️ 298K • 👍 13K • 💬 1K • ⏱️ 0:43 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 0 • ❤️ 1,954 • 2d ago

---

**[Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)**

*Prism ML*

Ternary-Bonsai-2-27B-gguf is a 27B parameter text generation model optimized for on-device inference using llama.cpp. It achieves ~98.2% of FP16 intelligence with a drastically reduced ~5.9 GB footprint by employing end-to-end ternary transformer weights (1.72 bits/weight), enabling efficient reasoning and long context (262K tokens) on consumer hardware with CUDA and Metal support.

`text-generation` `26.9B`

⬇️ 2,227,879 • ❤️ 1,769 • 4d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 6,523 • ❤️ 1,537 • 1d ago

---

**[Xing4.0-29B-A4B](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B)**

*XingChen-AGI*

Xing4.0-29B-A4B is a 29B parameter LLM with 4B active parameters, optimized for complex engineering tasks and agent-oriented architectures. It features a 256K context length (extensible to 512K) and supports multi-step planning and tool calling, making it suitable for domain-specific fine-tuning in areas like contract auditing and knowledge-based QA.

`text-generation` `31.2B`

⬇️ 18,394 • ❤️ 1,178 • 3d ago

---

**[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

*DeepSeek*

DeepSeek-V4.1-Flash is a 552B multimodal MoE model supporting 1M token contexts, featuring a Causal Encoder-Decoder architecture with Compressed Sparse Attention 2 (CSA2) and FP4 KV caching for highly efficient KV cache compression. It excels in agentic workloads and offers controllable reasoning effort, processing both images and text.

`image-text-to-text` `763.2B`

⬇️ 512,120 • ❤️ 3,552 • 11d ago

---

**[Qwen-Image-2.1-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-GGUF)**

*Ahmet Benzer*

Qwen-Image-2.1-GGUF is a quantized text-to-image diffusion model optimized for local inference via ComfyUI. It enables high-quality image generation with flexible VRAM/RAM offloading options, supporting various quantization levels for balanced performance and size.

`text-to-image` `7.1B`

⬇️ 33,232 • ❤️ 716 • 16h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 7,153,238 • ❤️ 15,986 • 1mo ago

---

**[Qwen-2.5-1B-RLCD](https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD)**

*Harsha Gundala*

Qwen-2.5-1B-RLCD is a text-generation model optimized for high-throughput structured information extraction on Apple Silicon using MLX. It achieves 5.6x-7.0x latency reductions with 100% schema validity by evaluating multi-field JSON schemas in parallel, ideal for tasks like fraud routing, code auditing, and support triage.

`text-generation`

⬇️ 0 • ❤️ 524 • 6d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)**

*Comfy Org*

Qwen-Image 2.1 is a diffusion model repackaged for ComfyUI, enabling text-to-image generation and image editing. It leverages Qwen3VL text encoders and a VAE for high-quality visual synthesis.

⬇️ 535,365 • ❤️ 471 • 1d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 1,292,471 • ❤️ 1,544 • 19d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 144 • 💬 6 • ⭐ 107,949 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 176 • 💬 19 • ⭐ 67,531 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 78 • 💬 3 • ⭐ 10,000 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 210 • 💬 3 • ⭐ 4,338 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](https://huggingface.co/papers/2609.20519)**

*Haozhe Liu, Tian Ye, Sensen Gao et al. (14 authors)*

🏢 NVIDIA

As coding agents move from supervised code completion to unattended, around-the-clock exploration, their work expands from isolated predictions into long trajectories of reasoning, tool use, and feedback. Token efficiency therefore becomes important for scaling recursive self-improvement. We take an RSI-inspired approach at the harness layer, scaling auto-research loops across increasingly numerous and diverse environments for harness rollouts. At this scale, the process yields reusable improvements that transfer beyond their development setting, moving automated harness discovery toward production-level outcomes. Four mechanisms survive selection and form SoL-Pi, spanning action execution, context compaction, observation handling, and delegated reading. On the 51-task EdgeBench evaluation, SoL-Pi achieves performance comparable to Pi across GPT-5.6 Sol and Opus 5 while reducing recorded token traffic by 44.7-49.0% and API cost by about one third. In other words, estimated hourly savings are \8.75-13.50 relative to native Codex and Claude Code harnesses, and \4.36-5.71 relative to Pi.

▲ 101 • 💬 3 • ⭐ 2,808 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2609.20519) • [💻 code](https://github.com/NVlabs/SoL-Pi) • [🔗 project](https://nvlabs.github.io/SoL-Pi/)

---

**[Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://huggingface.co/papers/2609.14858)**

*Tong Zheng, Xidong Wu, Zheng Zhang et al. (17 authors)*

🏢 Google

Dream-RSI enables scalable recursive self-improvement by using historical discovery replay to evaluate exploration policies offline, reducing costly online evaluations.

▲ 241 • 💬 3 • ⭐ 1,032 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2609.14858) • [💻 code](https://github.com/zhengkid/Dream-RSI) • [🔗 project](https://dream-rsi.com/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 88 • 💬 7 • ⭐ 88,742 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 112 • 💬 2 • ⭐ 13,444 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 45 • 💬 1 • ⭐ 33,408 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Paper2Agent: Reimagining Research Papers As Interactive and Reliable AI
  Agents](https://huggingface.co/papers/2509.06917)**

*Jiacheng Miao, Joe R. Davis, Jonathan K. Pritchard et al. (4 authors)*

Paper2Agent converts research papers into interactive AI agents to facilitate knowledge dissemination and enable complex scientific queries through natural language.

▲ 46 • 💬 7 • ⭐ 3,252 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06917) • [💻 code](https://github.com/jmiao24/Paper2Agent) • [🔗 project](https://huggingface.co/spaces/Paper2Agent/alphagenome_agent)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 6.0k • 🔱 1.7k • 1d ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 4.8k • 🔱 260 • 19h ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.8k • 🔱 184 • 1d ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 2.4k • 🔱 47 • 19h ago

---

**[amosblomqvist/learn](https://github.com/amosblomqvist/learn)**

My AI learning system.

`TypeScript`

⭐ 2.2k • 🔱 231 • 27d ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 2.0k • 🔱 80 • 1d ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 1.9k • 🔱 228 • 1d ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 1.9k • 🔱 366 • 5d ago

---

**[jtydhr88/screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills)**

Professional agent skills for screenwriting, television writing and dramaturgy

`Python` `ai` `skills`

⭐ 1.3k • 🔱 152 • 6d ago

---

**[adtexterry-lgtm/unigit-ecosystem](https://github.com/adtexterry-lgtm/unigit-ecosystem)**

UNIGIT public brand and ecosystem hub — AI should work for everyone.

`JavaScript` `agentic-ai` `ai-tools` `ai-workbench` `ecosystem` `mcp`

⭐ 1.3k • 🔱 45 • 19d ago

---

---

*Generated by PeekDeck - A glance is all you need*
