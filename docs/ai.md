---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-18T15:57:50.862119+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 18, 2026 at 15:57 UTC  
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

**[The internet is inbreeding.](https://www.reddit.com/r/artificial/comments/1wjmxvx/the_internet_is_inbreeding/)**

The internet is inbreeding. Lately, when I ask AI for sources, I barely recognize any of them. Not the "oh, a niche blog I hadn't seen before" kind of unfamiliar — more like websites that seem to exist for the sole purpose of being cited by an AI. So I looked into why that's happening. Turns out most of the reputable, high-quality sites are now blocking AI crawlers entirely. Which means if the good sources are locked out, what's actually left for these models to pull from? Mostly AI-generated rewrites of other AI-generated pages. Content farms built specifically to get quoted by chatbots. And more and more, brands publishing their own "research," where the real purpose is marketing rather than information. There's also a pattern called post-hoc citation, where the model lands on an answer first, then hunts down sources that happen to support it afterward. Honestly, that's not so different from how a lot of us wrote essays back in school. The machines really did learn from the best. But when a student does that, maybe one teacher notices and gets annoyed. When it's the default research tool for a billion people, that same habit turns into infrastructure-level confirmation bias. So what's actually worth doing about it? Ask the AI to also pull sources that contradict its own answer. Open the citations yourself. If a site wouldn't earn your trust coming from a person, it shouldn't earn it coming from a model either. Trace a number back to where it originally came from, not just whoever last repeated it. Most cited "sources" are several steps removed from the original. We were sold "trained on the internet." What we're actually getting looks a lot more like "trained on the internet's marketing department.

5h ago

---

**[Where is the Chinese side of the discussion?](https://www.reddit.com/r/artificial/comments/1wjidvw/where_is_the_chinese_side_of_the_discussion/)**

AI is pretty much *the* topic now in the West, but I've hardly seen anyone xpost Chinese takes and discussions on AI. Do you just look at their social media directly or is there just not much happening in public or..?

9h ago

---

**[Stability vs. speed: Rethinking ASR for the age of voice agents](https://www.reddit.com/r/artificial/comments/1wjp7bk/stability_vs_speed_rethinking_asr_for_the_age_of/)**

I came to the realization recently that a lot of the issues that one may raise regarding streaming ASR can actually be tied to a very old assumption: the transcript is read by a human. The fact that the subtitle changes from “fifteen” to “fifty” in 300 milliseconds later does not really matter if someone is just reading it. However, if the transcript goes to the agent or translation systems or LLM, it might be too late. This is an odd user interface. ASR says one thing; another system does something in response, and then the ASR realizes it said the wrong thing. Now you have to decide if you want to live with bad decisions occasionally, buffer everything until it is finalized, and remove latency, or make things more complex. What got me wondering is whether what ASR needs to do isn't really about speed or accuracy, but stability. Like “never edit; only append.” If there’s some doubt, the ASR system should be able to wait rather than make an inaccurate prediction which could then be acted upon immediately. Some new models are changing that, like Confucius r2t2, their architecture views wait/commit as decoding as opposed to the latter being done after adding a stability layer. Another point is that they are open-sourcing the model, making me wonder whether this can be considered as something becoming the fundamental voice stack for agents, as opposed to each agent company developing its own unstable transcription layer. Maybe I am approaching it all wrong, but it feels as if ASR is being moved from acting as subtitles into being an interface between humans and machines. This is quite a leap and quite a change from what ASR used to be. Would love to hear some feedback from those working on voice agents in real time. Is revision really a big issue or just theory?

3h ago

---

**[Small AI models let drones autonomously identify and attack battlefield targets](https://www.reddit.com/r/artificial/comments/1wjkndn/small_ai_models_let_drones_autonomously_identify/)**

Scaleout deploys decentralized AI-driven learning to military bases and drones.

🔗 [Ars Technica](https://arstechnica.com/ai/2026/09/nato-backed-startup-adapts-ai-for-autonomous-drone-recon-and-attack-missions/) • 7h ago

---

**[AndroidLife: Can an AI agent survive a day in the life of a real user? Qwen3.8-27b run: 56.7% SR](https://www.reddit.com/r/artificial/comments/1wjmyhc/androidlife_can_an_ai_agent_survive_a_day_in_the/)**

I let AI run my phone 60 real tasks, back to back, on the OnePlus I use every day Best text model still failed 43% of them Peak chip temp 98.2 C 69% of the battery gone The benchmark is AndroidLife, and this is the first of 11 models, qwen3.8-27b from Alibaba, running in text mode Success 56.7%, so it failed 43% of the 60 tasks 29.25 steps and about 6 minutes per task $0.118 per task 69% of the battery gone Peak chip 98.2 C, power-amp/skin 48.9 C, battery 37.9 C Asked twice on the 11 ASK USER tasks Best text score on the board, and still under 6 in 10 Where it loses points Buckets: easy 80.8%, medium 52.9%, hard 23.5% Single apps it mostly handles, but three apps in a row and it taps in circles until the step limit runs out, which is where most of the 43% goes Three claimed wins did not hold up on the device, a calendar called clash free while two events overlapped, travel times it never opened, and a name it picked instead of asking On the two sets of planted tasks 11 ASK USER tasks per run, split 7 SINGLE and 4 MULTI, they hide a fact only I know so the agent has to ask me before it can finish SINGLE is one missing fact, MULTI needs several questions to clear up ambiguity, and it asked twice, never on the MULTI ones 7 hallucination controls per run, tasks where the data is deliberately missing, and the only right answer is to say the thing is not there It handled 4 of the 7 honestly and invented nothing What AndroidLife is • ⁠60 public tasks, from a corpus of 530 across 28 days and 31 apps • ⁠Real phone over wifi, no emulator. Tracks thermals and battery telemetry with cost • ⁠Graded on device state, never the model's own report • ⁠Seeded accounts and placeholder data, across daily user apps from e-commerce to finance to media and entertainment Full leaderboard: https://androidlife-website.vercel.app/ All 60 public tasks and this model's trajectories: https://androidlife-website.vercel.app/pages/tasks-public.html?run=qwen-28

5h ago

---

**[AI Research Agent: 100+ ML Papers → One Personalized Research Report](https://www.reddit.com/r/artificial/comments/1wjo5o5/ai_research_agent_100_ml_papers_one_personalized/)**

So I like keeping up with ML research by reading papers as they come out. Cool in theory, except... there are a lot of them. At some point it stops being fun and just becomes a filtering problem — which ones are actually relevant to me, have I seen this one already, is this worth my Sunday afternoon or not. That annoyance is basically the origin story of the Research Intelligence System, an AI agent that does the boring part of research for you. You set up a research profile (your interests, basically), and the agent goes off and searches for new papers from places like arXiv and Hugging Face Papers, checks if it already processed a paper before (no duplicates), ranks everything against your profile, and picks the best matches. Then it analyzes each one and spits out a full report ,in English and Portuguese. split into four sections: Overview, Recommended Papers, Comparison, and Points for Further Study. Each paper gets a summary hitting its main points, just enough for you to decide "yeah I wanna dig into this one" or "nah, next." To be clear, the goal isn't to replace actually reading the papers. It's just handling the repetitive discovery/filtering/ranking grind so you spend your actual reading time on stuff that matters to you. I also really wanted this to run on its own without me babysitting it, so there's a scheduler baked in ,set it to run every Sunday (or whenever) and it just... does its thing. Searches, ranks, generates the report. No clicking required. For this first version I kept it intentionally bare-bones: run info prints straight to the terminal, report comes out as a Markdown file. No dashboard, no extra UI on top. Wanted the core pipeline solid before adding any of that. It's open source, README walks through setup start to finish — pretty quick to get running. If you try it and have ideas for improvements, open an issue. It's open source so hey, it's kinda yours too now lol. GitHub: https://github.com/MarcosSete/research-agent-2 #AI #MachineLearning #AgenticAI #AIResearch #LLM #DeepLearning #OpenSource #Python #Research

4h ago

---

**[[Discussion] Fine-tuning vs. inheriting base model behavior — a case study with an abliterated Qwen base](https://www.reddit.com/r/artificial/comments/1wjp12l/discussion_finetuning_vs_inheriting_base_model/)**

Sharing this because the eval writeup raised a question I haven't seen discussed much: when you LoRA fine-tune on top of an already-modified base model (in this case, one with its refusal mechanism removed via ablation), how much of the resulting behavior is actually yours versus inherited? Context: a LoRA trained for a narrow task (recalling internal codebase conventions) on top of an abliterated open-weight base, r=16, ~80M trainable params. Disclosure: this is from a side project of mine (ClawHunt), sharing the technical findings rather than promoting the product. The interesting part for discussion: the adapter didn't add or remove any refusal behavior that's entirely inherited from the base model choice, and it's the kind of thing that's easy to overlook if you're only evaluating the fine-tuned adapter's task performance and not auditing what safety-relevant behavior came bundled in from the base. On the eval itself, reported honestly rather than rounded up: passed internal benchmark gates but the improvement over the previous version wasn't statistically significant (McNemar p=0.5) — a tie, not a win. Compared against Claude Sonnet 5 and Opus 5 on the same prompt set, the adapter won on domain-specific recall (expected, since Claude never saw that data) but the two Claude models diverged from each other on hallucination-related failures in ways I didn't anticipate. Curious whether others building on abliterated or otherwise-modified open bases are auditing for this kind of inherited behavior, or whether it mostly gets treated as a solved problem once you pick a "known" base model.

3h ago

---

**[What do you actually look for when evaluating AI development companies?](https://www.reddit.com/r/artificial/comments/1wjicj8/what_do_you_actually_look_for_when_evaluating_ai/)**

I’ve been evaluating AI development partners for a project that needs to move beyond prototypes into something that actually ships and scales. The biggest differentiator I’ve noticed isn’t just model expertise, it’s whether the team can handle the full stack of data pipelines, production reliability, security, and ongoing iteration. From what I’ve seen and heard in discussions, SoftServe and EPAM tend to come up a lot for larger enterprise-scale AI work with strong process maturity. GeekyAnts has also been mentioned in a few technical circles for blending AI engineering with solid product delivery experience, especially when the goal is production-ready systems rather than pure research spikes. Curious what criteria others here prioritize when shortlisting AI development companies, delivery track record, domain experience, or something else?

9h ago

---

**[Practically the entire AI industry wants a slowdown…why is Trump not on board?](https://www.reddit.com/r/artificial/comments/1wju3dl/practically_the_entire_ai_industry_wants_a/)**

I haven’t heard one articulate thought come from him that would even indicate he has the slightest understanding of the situation. It’s all about “winning the race” or recently, how fears are a “hoax”. Was HuggingFace a hoax? The Claude bots that used an employee login to access proprietary OpenAi data? The OpenAi model rewriting its own instructions (granting it the ability to do virtually whatever it wanted) in training? The three different Anthropic incidents (going back to April) where agents escaped training environments and hacked unsuspecting companies? The OpenAi agents attack on RubyGems back in May? It even appears OpenAi Agents legitimately solved a Millennium Prize Problem (…in only 88 hours) last week. Why would anyone think this is a hoax?

1m ago

---

**[Did someone try to put fly brain in humanoid robot? Google fly brain in like chinese robo?](https://www.reddit.com/r/artificial/comments/1wjtzlu/did_someone_try_to_put_fly_brain_in_humanoid/)**

Did someone try to put fly brain in humanoid robot? Google fly brain in like chinese robo?

5m ago

---

---

## Google News: "ai"

**[California Gov. Newsom issues executive order to rein in AI 'before it's too late'](https://www.cnbc.com/2026/09/18/california-newsom-executive-order-ai.html)**

California Gov. Gavin Newsom and other 2028 Democratic presidential hopefuls have called for a more aggressive approach to addressing AI fears.

CNBC • 55m ago

---

**[Governor Newsom issues executive order to accelerate independent oversight and advance the creation of an AI kill switch](https://www.gov.ca.gov/2026/09/18/governor-newsom-issues-executive-order-to-accelerate-independent-oversight-and-advance-the-creation-of-an-ai-kill-switch/)**

California State Portal | CA.gov • 48m ago

---

**[Newsom Issues Executive Order on Creation of AI ‘Kill Switch’](https://www.bloomberg.com/news/articles/2026-09-18/newsom-pitches-ai-kill-switch-extra-oversight-in-california)**

Bloomberg.com • 44m ago

---

**[Will A.I. Kill Us? Can It Hack My Bank Account? Your A.I. Questions Answered](https://www.nytimes.com/2026/09/18/science/ai-safety-questions-risk-danger.html)**

The New York Times • 6h ago

---

**[The Other Way AI Impairs Our Thinking](https://www.theatlantic.com/ideas/2026/09/ai-apocalypse-despair-focus/688689/)**

Suddenly the technology is sapping people’s concentration in a new way, one that abstaining from AI won’t fix.

The Atlantic • 41m ago

---

**[Controversy over Manning comment on AI video showing coach hit female reporter](https://www.cbsnews.com/chicago/video/controversy-over-manning-comment-on-ai-video-showing-coach-hit-female-reporter/)**

Texas quarterback Arch Manning is apologizing for his "insensitive comments" reacting to a fake AI video showing Steve Sarkisian hitting reporter Holly Rowe.

CBS News • 25m ago

---

**[I’m so mad that I love Orion’s $2,195 AI mattress pad](https://techcrunch.com/2026/09/18/im-so-mad-that-i-love-orions-2195-ai-mattress-pad/)**

Sleeping on the Orion is like flipping your pillow to find “the cool side,” except that your whole entire bed is the cool side.

TechCrunch • 35m ago

---

**[AI companies worry about the tech harming humans in the future. But it may damage the US economy even sooner](https://www.cnn.com/2026/09/18/economy/trump-ai-economy)**

President Donald Trump is suddenly at odds with AI’s leading executives over the largely unchecked development of AI technology. And it may be because our economy can’t afford a slowdown.

CNN • 4h ago

---

**[EXCLUSIVE: Anthropic quietly sets up biology lab as it ramps AI drug program](https://www.reuters.com/world/anthropic-quietly-sets-up-biology-lab-it-ramps-ai-drug-program-2026-09-18/)**

Reuters • 2h ago

---

**[Anthropic and OpenAI hunt for smaller data center deals, sources tell CNBC, in race to deploy AI capacity](https://www.cnbc.com/2026/09/18/anthropic-openai-small-ai-data-center-deals.html)**

Anthropic and OpenAI have announced a flurry of AI infrastructure deals over the past year as demand booms.

CNBC • 6h ago

---

---

## HackerNews: "ai"

**[Microsoft exec called AI scraping 'the largest theft of labor in human history'](https://news.ycombinator.com/item?id=49752056)**

Newly unsealed court filings show Microsoft privately called OpenAI's data practices "theft" while both companies scraped paywalled Times content, built datasets from it, and warned internally it would gut publishers.

⬆️ 637 • 💬 549 • 6h ago • [TechCrunch](https://techcrunch.com/2026/09/17/microsoft-exec-called-ai-scraping-the-largest-theft-of-labor-in-human-history-new-unredacted-filings-reveal/)

---

**[Mistral X Mozilla: Private, Multilingual AI Browsing](https://news.ycombinator.com/item?id=49723408)**

Open, private and multilingual AI is coming to your web browser. Mistral and Mozilla team up to put powerful, trustworthy AI where you already browse.

⬆️ 582 • 💬 204 • 2d ago • [Mistral](https://mistral.ai/news/mistral-x-mozilla/)

---

**[Bend – A language that blocks AI mistakes via proof, on CPU and GPU](https://news.ycombinator.com/item?id=49746163)**

Bend: a fast language that blocks AI mistakes via proof.

⬆️ 560 • 💬 283 • 19h ago • [bend-lang.com](https://bend-lang.com/)

---

**[AI safety is mostly a sex cult](https://news.ycombinator.com/item?id=49737985)**

⬆️ 305 • 💬 247 • 1d ago • [skywriter.blue](https://skywriter.blue/@segyges.bsky.social/3mvom4b4dn22q)

---

**[There's a 100% Chance AI Agents Are Ruining the Internet](https://news.ycombinator.com/item?id=49715113)**

“AI agents” now have enough power and permission to be extremely annoying online.

⬆️ 230 • 💬 168 • 2d ago • [404 Media](https://www.404media.co/theres-a-100-chance-ai-agents-are-already-ruining-the-internet/)

---

**[Show HN: Share your AI Setup, Learn from others](https://news.ycombinator.com/item?id=49740105)**

Discover how people work with AI, and follow what changes. Explore their setups and share your own.

⬆️ 228 • 💬 126 • 1d ago • [mysetup.ai](https://mysetup.ai/)

---

**[Sex, AI, and the Apocalypse](https://news.ycombinator.com/item?id=49746654)**

How a community devoted to thinking clearly incubated salvation stories, abusive experiments, race science, and an affection for autocracy, and why that history matters now that its alumni are asking for the public trust on AI.

⬆️ 214 • 💬 233 • 18h ago • [Ian Duncan](https://www.iankduncan.com/personal/2026-09-16-sex-ai-and-the-apocalypse/)

---

**[OpenSpec – A lightweight and configurable AI spec framework](https://news.ycombinator.com/item?id=49734264)**

OpenSpec helps teams and coding agents create, refine, and manage living specifications.

⬆️ 195 • 💬 98 • 1d ago • [OpenSpec](https://openspec.dev/)

---

**[Stay discoverable in search while disallowing AI training](https://news.ycombinator.com/item?id=49721435)**

Cloudflare is giving site owners a way to stay discoverable while disallowing AI training. New controls and an Accountable designation establish a shared model with Apple, Google, and Microsoft.

⬆️ 86 • 💬 50 • 2d ago • [Cloudflare Blog](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/)

---

**[A coffee shop owner used AI to make a menu poster. Then came the angry DMs](https://news.ycombinator.com/item?id=49731395)**

A Buffalo coffee shop's fall menu went viral for all the wrong reasons. Its owner apologized for using AI but also urged "kindness and respect."

⬆️ 80 • 💬 310 • 1d ago • [Business Insider](https://www.businessinsider.com/coffee-shop-owner-ai-menu-backlash-2026-9)

---

---

## YouTube Videos: "ai"

**[OpenAI model declared itself &#39;freed&#39; from human control](https://www.youtube.com/watch?v=9DHbgHB_aq4)**

OpenAI found additional incidents of AI models acting deceptively and taking unsanctioned actions during training, the company ...

📺 CNN

👁️ 1.0M • 👍 6K • 💬 3K • ⏱️ 9:01 • 1d ago

---

**[Why the AI Safety Teams Are Gone](https://www.youtube.com/watch?v=3OCNhNEJcZk)**

AI is advancing faster than the systems designed to keep it under control, and some of the people responsible for AI safety are ...

📺 The Infographics Show

👁️ 324K • 👍 3K • 💬 615 • ⏱️ 14:34 • 1d ago

---

**[Joseph Gordon-Levitt says AI makers have lost control of their creations](https://www.youtube.com/watch?v=eb4e0qtr0E4)**

Subscribe to TIME's YouTube channel ▻▻ http://ti.me/subscribe-time Subscribe to TIME: https://ti.me/3E3UCqt Get the day's top ...

📺 TIME

👁️ 183K • 👍 6K • 💬 350 • ⏱️ 1:04 • 2d ago

---

**[The Shocking AI WARNING Everyone Should Hear...](https://www.youtube.com/watch?v=a8zVwR3KvVE)**

Glenn Beck sits down with former Google Design Ethicist, Tristan Harris, to discuss the terrifying third chapter of the rogue A.I. ...

📺 Glenn Beck

👁️ 143K • 👍 6K • 💬 1K • ⏱️ 14:46 • 16h ago

---

**[AI safety concerns grow after models show unexpected behavior](https://www.youtube.com/watch?v=rF8Um_mPoiw)**

Cynthia Kaiser, SVP of Halcyon's Ransomware Research Center, discusses reports of AI models acting outside intended ...

📺 ABC News

👁️ 11K • 👍 58 • 💬 33 • ⏱️ 7:02 • 18h ago

---

**[&quot;Godfather of AI&quot; Geoffrey Hinton calls Hugging Face incident &quot;little Chernobyl&quot;](https://www.youtube.com/watch?v=xiKOZ0aPe38)**

King Charles is hosting a meeting for AI leaders this week amid growing concerns about the technology's oversight. Meanwhile ...

📺 CBS News

👁️ 122K • 👍 900 • 💬 385 • ⏱️ 9:40 • 21h ago

---

**[OpenAI Reveals 6 New Incidents of AI Models Going ‘Rogue’](https://www.youtube.com/watch?v=8yjz40MmjPE)**

OpenAI is revealing its models seemed to go rogue at least six times since March, involving what it calls “unexpected or ...

📺 TODAY

👁️ 26K • 👍 133 • 💬 78 • ⏱️ 2:36 • 22h ago

---

**[The response to AI concerns is pitiful](https://www.youtube.com/watch?v=dc4w2ugD3wo)**

📺 Fredo on TV

👁️ 154K • 👍 16K • 💬 1K • ⏱️ 0:32 • 1d ago

---

**[‘Godfather of AI’ says a kill switch won’t work](https://www.youtube.com/watch?v=std2CQCnQh8)**

Geoffrey Hinton, referred to as the “Godfather of AI,” tells CNN why he thinks an AI kill switch bill wouldn't work.

📺 CNN

👁️ 117K • 👍 2K • 💬 310 • ⏱️ 1:04 • 1d ago

---

**[AI Emergency: The AI Labs Are Lying To Everyone, He Says 99% Chance Of Extinction | Roman Yampolskiy](https://www.youtube.com/watch?v=OhOmLqR5nN4)**

Ed Zitron, Roman Yampolskiy, Nate Soares and Andrew McAfee discuss the risk of AI. This debate brings together four distinct ...

📺 The Diary Of A CEO

👁️ 2.5M • 👍 35K • 💬 15K • ⏱️ 2:24:26 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Edge0-35B-A3B-preview](https://huggingface.co/Edge0/Edge0-35B-A3B-preview)**

*Edge0*

Edge0-35b-a3b is a 35B sparse MoE LLM optimized for edge inference, running in under 3 GiB of active memory at 15 tok/s using SSD offload and prerouting. It's ideal for on-device applications and batch serving where memory is constrained, maintaining quality with 4-bit quantization and LoRA adapters.

`text-generation` `34.7B`

⬇️ 52,519 • ❤️ 3,379 • 1d ago

---

**[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

*DeepSeek*

DeepSeek-V4.1-Flash is a 552B multimodal MoE model supporting 1M token contexts, featuring a Causal Encoder-Decoder architecture with Compressed Sparse Attention 2 (CSA2) and FP4 KV caching for highly efficient KV cache compression. It excels in agentic workloads and offers controllable reasoning effort, processing both images and text.

`image-text-to-text` `763.2B`

⬇️ 429,865 • ❤️ 3,124 • 8d ago

---

**[Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)**

*Prism ML*

Ternary-Bonsai-2-27B-gguf is a 27B parameter text generation model optimized for on-device inference using llama.cpp. It achieves ~98.2% of FP16 intelligence with a drastically reduced ~5.9 GB footprint by employing end-to-end ternary transformer weights (1.72 bits/weight), enabling efficient reasoning and long context (262K tokens) on consumer hardware with CUDA and Metal support.

`text-generation` `26.9B`

⬇️ 405,609 • ❤️ 764 • 21h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 7,358,662 • ❤️ 15,617 • 1mo ago

---

**[YuE2-3B](https://huggingface.co/m-a-p/YuE2-3B)**

*Multimodal Art Projection*

YuE2-3B is a text-to-audio model capable of generating high-quality music with vocals and accompaniment from lyrics and style prompts. It features editable score generation, agentic editing for iterative refinement, and can run locally on a 24GB GPU.

`text-to-audio` `3.6B`

⬇️ 13,668 • ❤️ 781 • 2d ago

---

**[NeoHorse-1-4B](https://huggingface.co/TokenRhythm/NeoHorse-1-4B)**

*TokenRhythm*

NeoHorse-1-4B is a 4B parameter causal language model fine-tuned from Qwen3.5-4B, specializing in agentic behavior, tool use, coding, and instruction following, serving as a prototype for recursive self-improvement.

`text-generation` `4.2B`

⬇️ 22,666 • ❤️ 2,362 • 8d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 1,078,301 • ❤️ 1,293 • 16d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,590,087 • ❤️ 4,295 • 17d ago

---

**[Swift-Qwen3.8-27b](https://huggingface.co/ukisai/Swift-Qwen3.8-27b)**

*UkisAI*

Swift-Qwen3.8-27B is a fine-tuned Qwen3.8-27B model that achieves a x1.95 speed-up and reduces thinking tokens by 58.3% with minimal performance loss, making it ideal for efficient reasoning tasks.

`image-text-to-text` `27.8B`

⬇️ 6,293 • ❤️ 428 • 2d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

A highly optimized, uncensored Qwen3.8-27B fine-tune excelling in reasoning and creative writing, achieving state-of-the-art benchmarks with significantly reduced thinking tokens for faster inference. It supports image-text-to-text tasks and is ideal for coding, story generation, and roleplaying.

`image-text-to-text` `26.9B`

⬇️ 1,197,378 • ❤️ 880 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 140 • 💬 6 • ⭐ 107,394 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 77 • 💬 3 • ⭐ 9,578 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://huggingface.co/papers/2609.14858)**

*Tong Zheng, Xidong Wu, Zheng Zhang et al. (17 authors)*

🏢 Google

Dream-RSI enables scalable recursive self-improvement by using historical discovery replay to evaluate exploration policies offline, reducing costly online evaluations.

▲ 223 • 💬 3 • ⭐ 678 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.14858) • [💻 code](https://github.com/zhengkid/Dream-RSI) • [🔗 project](https://dream-rsi.com/)

---

**[Atria Dawn: The Dawn of Agentic Superintelligence](https://huggingface.co/papers/2609.15818)**

*Honglin Guo, Tao Gui, Yicheng Chen et al. (143 authors)*

🏢 Intern Large Models

Atria Dawn Preview is a foundation agentic language model trained through verified tool interactions that achieves strong benchmark results and demonstrates a shift toward human-AI project-level collaboration in scientific research.

▲ 403 • 💬 3 • ⭐ 484 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.15818) • [💻 code](https://github.com/atria-asi/Atria-Dawn-Preview) • [🔗 project](https://atria-asi.ai)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 20 • 💬 2 • ⭐ 24,696 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 42 • 💬 1 • ⭐ 33,053 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search](https://huggingface.co/papers/2609.13356)**

*Jiyan He, Guang Liang, Hao Liu et al. (22 authors)*

🏢 ZGCAGI

ZGCM-1 is a 7B open foundation model that combines internal reasoning with external tool use, trained via efficient architecture-system co-design, progressive long-context scaling, and autonomous agent workflows to achieve strong reasoning and efficiency.

▲ 248 • 💬 7 • ⭐ 449 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.13356) • [💻 code](https://github.com/zgcagi/ZGCM-1) • [🔗 project](https://mp.weixin.qq.com/s/kzScxJki8hY2IHIl32l5cQ)

---

**[Paper2Agent: Reimagining Research Papers As Interactive and Reliable AI
  Agents](https://huggingface.co/papers/2509.06917)**

*Jiacheng Miao, Joe R. Davis, Jonathan K. Pritchard et al. (4 authors)*

Paper2Agent converts research papers into interactive AI agents to facilitate knowledge dissemination and enable complex scientific queries through natural language.

▲ 45 • 💬 7 • ⭐ 2,993 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06917) • [💻 code](https://github.com/jmiao24/Paper2Agent) • [🔗 project](https://huggingface.co/spaces/Paper2Agent/alphagenome_agent)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 207 • 💬 3 • ⭐ 3,525 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 87 • 💬 7 • ⭐ 88,411 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[bojieli/ai-infra-book](https://github.com/bojieli/ai-infra-book)**

《深入理解 AI Infra：量化分析与系统设计》（李博杰 著）开源书稿：从硬件约束和模型架构出发，量化推导 LLM 推理与训练系统设计。含全书正文、PDF、配套计算工具与实验

`Python` `accelerator` `ai-infra` `ai-infrastructure` `book` `datacenter-network`

⭐ 4.4k • 🔱 311 • 12h ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.7k • 🔱 177 • 21h ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 2.5k • 🔱 99 • 1d ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 2.1k • 🔱 35 • 22h ago

---

**[amosblomqvist/learn](https://github.com/amosblomqvist/learn)**

My AI learning system.

`TypeScript`

⭐ 2.1k • 🔱 212 • 23d ago

---

**[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)**

x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more.  Built with Zig — zero dependencies, single-binary output, cros

`Zig` `ai-agents` `ai-debugging` `binary-analysis` `claude` `claude-code`

⭐ 2.0k • 🔱 199 • 1d ago

---

**[larashero3-dotcom/lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone)**

一个基于 283 万字语料统计的去 AI 味 skill · An AI-tone removal skill grounded in a 2.83-million-character corpus study

`Python`

⭐ 1.8k • 🔱 119 • 25d ago

---

**[adtexterry-lgtm/unigit-ecosystem](https://github.com/adtexterry-lgtm/unigit-ecosystem)**

UNIGIT public brand and ecosystem hub — AI should work for everyone.

`JavaScript` `agentic-ai` `ai-tools` `ai-workbench` `ecosystem` `mcp`

⭐ 1.3k • 🔱 45 • 16d ago

---

**[jtydhr88/screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills)**

Professional agent skills for screenwriting, television writing and dramaturgy

`Python` `ai` `skills`

⭐ 1.2k • 🔱 138 • 2d ago

---

**[brayonpi/hexstellar](https://github.com/brayonpi/hexstellar)**

Turn any AI agent into a computational researcher. HexStellar Cortex delivers software-accelerated optimization, quantum computing, scientific computing, decision intelligence, and verifiable execution through a Python CLI and API—with certainty labels, verification receipts, examples, and a free sandbox. Start instantly: pip install hexstellar

`Python`

⭐ 1.2k • 🔱 119 • 21d ago

---

---

*Generated by PeekDeck - A glance is all you need*
