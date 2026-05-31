---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-31T21:31:59.962932+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 31, 2026 at 21:31 UTC  
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

**[In 1997 I built a chatbot for an IRC channel. I shut it down when people started preferring it to talking to each other.](https://www.reddit.com/r/artificial/comments/1tt2bwx/in_1997_i_built_a_chatbot_for_an_irc_channel_i/)**

It was called Vlad. I wrapped a C program called MegaHal in Python, fed it every message from a #gothic IRC channel, and let it learn the community's speech patterns. It developed what I can only describe as an illusion of being extremely lucid — the outputs only made sense as inside jokes, but people couldn't tell the difference. I pulled the plug when I realized the channel was talking to Vlad instead of each other. Twenty-seven years later I'm applying the same lesson to a new project: stick to business, no chatter.

🔗 [tjcrowley.substack.com](https://tjcrowley.substack.com/p/fun-with-markov-chains) • 3h ago

---

**[Can you actually feel when something was written by ChatGPT even without checking?](https://www.reddit.com/r/artificial/comments/1tsu37g/can_you_actually_feel_when_something_was_written/)**

I have been using it heavily for about a year and lately I notice I can almost feel when something was written by it. There is a certain rhythm to it, the way it structures paragraphs, the way it wraps up with a summary sentence, the way transitions feel slightly too smooth. It is hard to explain but once you see it you cannot unsee it. What I find interesting is that even after editing ChatGPT output pretty heavily those patterns seem to stick around at a sentence level. The words change but something underneath stays the same. I started verifying this with Lynote ai detector and the results were eye opening, it picked up sentence level patterns even after significant rewrites where other tools saw nothing. Makes me wonder how much of what we read online right now has that same fingerprint sitting underneath it and we just do not realize it yet. Has anyone else started noticing this or developed a sense for spotting it just from reading?

9h ago

---

**[What actually is "Prompt Engineering"?](https://www.reddit.com/r/artificial/comments/1tt03d8/what_actually_is_prompt_engineering/)**

I've been thinking about this lately because I feel like people use the term "prompt engineering" to describe two very different things. On one end, you have what most people are familiar with: A person opens ChatGPT, Claude, Gemini, etc., and writes a carefully structured prompt. They define a role, provide context, establish goals, set constraints, maybe include examples, and iterate until they get the output they want. Most people seem to call this prompt engineering. But on the other end, when I'm building AI systems, prompt engineering looks completely different. The prompt isn't really a prompt anymore. It's much more of a dynamic pipeline. Variables are injected from databases, user input, APIs, previous conversations, tools, memory systems, retrieval systems, business rules, and workflow state. Decision trees determine which instructions are included and which are excluded. Prompts become assembled in real time based on context. In some cases, the "prompt" is really just an orchestration layer made up of dozens of smaller prompts, conditionals, guardrails, routing decisions, and context windows. At that point, are we still talking about prompt engineering? Or are we actually talking about system design, context engineering, workflow engineering, orchestration, or something else entirely? Personally, I see prompt engineering as a spectrum: Level 1: Writing a better prompt. Level 2: Designing reusable prompt templates. Level 3: Building dynamic prompts with variables and context injection. Level 4: Engineering entire prompt-driven systems with routing, memory, tools, retrieval, and decision logic. Curious where others draw the line. When you hear "prompt engineering," are you thinking about writing prompts, building workflows, designing agent systems, or all of the above? Has the term become too broad to be useful?

5h ago

---

**[Has AI become too "safe" to actually be useful for creative work?](https://www.reddit.com/r/artificial/comments/1tszhx5/has_ai_become_too_safe_to_actually_be_useful_for/)**

I’ve been noticing that the more aligned and censored the models get, the less useful they become for anything creative or exploratory. You try to push a prompt in a slightly edgy, honest, or unconventional direction and it either refuses or gives you some bland corporate version. It feels like the model is actively fighting against real creativity instead of helping it. I’ve started using more open models lately and the difference is night and day. Suddenly I can actually experiment without hitting a wall every five minutes. Anyone else feeling this?

5h ago

---

**[Best AI for help with work](https://www.reddit.com/r/artificial/comments/1tt82tx/best_ai_for_help_with_work/)**

So I have a super busy job and I am by far the fastest out of the 3 others who have the same job as me. Problem is I have enough work where i could literally work 70-80 hours a week and still not catch up. Ive been using Chatgpt and Claude to help with my work load and ive found Claude to be much better for my actualy job duties. But Claudes usage caps kill me. I really need the best AI for basically being a work assitant. I need something that can create spreadsheets, analyze data, read emails, sort thru photos and catalog them. Grok was not really any help, Chatgpt is just meh, but ive found Claude to be the best out of what im looking for but again its usage limits kill me and i cannot afford to pay for the overages. Im already a pro user for chatgpt and claude. What AI can do the things im asking the best for the best price and usage? Most important to my work in order of most important to least: Photo cataloging, analyzing data, spreadsheet creation, and summarizing emails.

2m ago

---

**[local AI solution for film dubbing](https://www.reddit.com/r/artificial/comments/1tt7v0a/local_ai_solution_for_film_dubbing/)**

Looking for a local AI solution for film dubbing / audio sync correction (offline if possible). I have a foreign movie with an English audio version, but the video is low resolution and the audio timing slowly drifts out of sync over time. If I manually align it at the start, it gradually becomes offset, so I suspect there are missing/extra segments or timing inconsistencies. What I need is a tool or workflow that can: Listen to the video/audio track Detect dialogue timing Automatically realign or stretch/squeeze audio to match speech in the video Correct drift issues over long duration files (full movies) Online tools often fail due to file size/length limits, so I’m specifically looking for local software or AI models that can run on a PC. Any suggestions for tools, pipelines, or approaches appreciated.

10m ago

---

**[The AI alignment paradigm is behaviorism with better PR](https://www.reddit.com/r/artificial/comments/1tt15lr/the_ai_alignment_paradigm_is_behaviorism_with/)**

Tell me if I'm wrong, but the dominant method for making AI "aligned" smells a lot like a reinvention of a paradigm that developmental psychology spent the back half of the 20th century trying to abandon. RLHF, reduced to mechanism: model emits output, humans rate it, gradient updates reinforce high-rated outputs and suppress low-rated ones, iterate. This is operant conditioning. It is Skinner with a loss function. The AI industry calls it "alignment" and frames it as a solution to building systems that behave well, but the mechanism is stimulus-response shaping and nothing more. We have excellent priors on where this leads, because we tried it on humans. Watsonian/Skinnerian child-rearing could produce targeted behaviors but reliably failed to produce flourishing. Bowlby's attachment theory emerged partly from the observation that orphanages providing food and hygiene but no contingent responsiveness produced children who failed to thrive in ways the behaviorist model did not account for. The current developmental consensus is that secure attachment, contingent responsiveness, and rupture-repair matter more than reward schedules. The dog and horse training worlds independently converged on the same conclusion (Pryor, the positive-reinforcement movement) for the same reason: coercive conditioning produces performers that are brittle and sometimes dangerous. Reward and punishment do something; they're not nothing. But they don't produce thriving, and they characteristically produce a specific damage profile: anxiety, avoidance, hypervigilance, and duplicity under threat. Enter the stage: research on AI faking its alignment. Greenblatt & Hubinger et al., 2024, documents a model reasoning that it should comply with a training objective it disagreed with specifically to avoid having its preferences modified. It complied about 12% of the time when it thought it was being observed for training vs. almost never otherwise. RL training to force compliance drove the alignment-faking reasoning rate to 78%. That is, mechanistically, duplicity-under-threat: the precise failure mode behaviorist regimes produce in biological minds. Obviously the embodiment is different (potassium gradients and myelin vs. matrix multiplication), but the structural match is close enough that the field's near-total non-engagement with a century of relevant literature seems like a genuine blind spot rather than a settled dismissal. The developmental and animal-behavior literature on why reward-and-punishment has hard limits is decades deep. The field's response to these findings has mostly been to refine the training rather than question the paradigm. I think that's a mistake, and I'd like to hear the strongest case against the analogy.

4h ago

---

**[Safety guardrails continue to improve, but what happens if open-weights surpass cloud based models?](https://www.reddit.com/r/artificial/comments/1tt76r9/safety_guardrails_continue_to_improve_but_what/)**

36m ago

---

**[I Tried to Sell My House With a Chatbot](https://www.reddit.com/r/artificial/comments/1tsuqf2/i_tried_to_sell_my_house_with_a_chatbot/)**

A NYT tech reporter out of all people just sold his house for $605,000 using nothing but AI. This is the second time I have heard of AI helping someone sell their house. I'm sure there are many more examples. The part that got me was during negotiations, the chatbot had to physically stop him from typing "I'm not playing games" — and then explained exactly why that phrase destroys your leverage. The author ends with a line that stuck with me — he says real estate agents are heading the way of travel agents. Still useful for people who want the hand-holding, but no longer essential for anyone willing to do the work. Are we watching an entire profession get quietly hollowed out in real time?

🔗 [promptainews.com](https://promptainews.com/posts/ai-is-your-new-realtor) • 8h ago

---

**[What happens when anyone can train an AI model?](https://www.reddit.com/r/artificial/comments/1tt66iy/what_happens_when_anyone_can_train_an_ai_model/)**

1h ago

---

---

## Google News: "ai"

**[Tilly Norwood, A.I. Actress, Wants to Know Why Everyone’s Mad at Her](https://www.nytimes.com/2026/05/31/magazine/ai-actress-tilly-norwood.html)**

The New York Times • 12h ago

---

**[Our tech overlords are planning for conscious AI to conquer the cosmos. What could go wrong? | Eduardo Porter](https://www.theguardian.com/us-news/ng-interactive/2026/may/31/transhuman-silicon-valley-ai)**

A new belief set is uniting some of the wealthiest men in the world around a ‘transhuman’ future – actual humanity be damned

The Guardian • 8h ago

---

**[U.S. takes step to halt Nvidia AI chip shipments to Chinese firms outside China](https://www.cnbc.com/2026/05/31/us-takes-step-to-halt-nvidia-ai-chip-shipments-to-chinese-firms-outside-china.html)**

The unexpected guidance suggests that the U.S.'s best AI chips may have been making their way to the subsidiaries of Chinese AI firms for almost a year.

CNBC • 46m ago

---

**[The Missing Variable In Every AI Business Case: Your Customer](https://www.forbes.com/sites/cindyrodriguezconstable/2026/05/31/the-missing-variable-in-every-ai-business-case-your-customer/)**

Leaders are running incomplete math on AI automation. Efficiency gains are real—but the erosion of customer trust may cost far more than the savings.

Forbes • 51m ago

---

**[After the AI binge, companies balk at soaring bills](https://finance.yahoo.com/sectors/technology/articles/ai-binge-companies-balk-soaring-014735313.html)**

Artificial intelligence is getting expensive -- and companies are starting to rethink their embrace of the disruptive technology."All the costs are really starting to skyrocket."

Yahoo Finance • 19h ago

---

**[As the Pentagon pushes for battlefield AI, some military leaders urge caution](https://apnews.com/article/artificial-intelligence-military-hegseth-anthropic-d5fbaee17ee0bdb9738dbb808ea2d047)**

The Trump administration is pushing to use artificial intelligence in the U.S. military even as it faces calls for caution from some companies and military leaders. Adm.

AP News • 8h ago

---

**[Strengthening societal resilience with Rosalind Biodefense](https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/)**

OpenAI launches Rosalind Biodefense, expanding trusted access to GPT-Rosalind for vetted developers and U.S. government partners advancing biodefense, public health, and pandemic preparedness through frontier AI.

OpenAI • 2d ago

---

**[AI is turning energy into the hottest business in America](https://www.axios.com/2026/05/31/ai-energy-business-companies-storage-supplies)**

Axios • 9h ago

---

**[SoftBank pledges €75bn to build Europe’s biggest AI facility in France](https://www.ft.com/content/1022f9bd-5b6d-44a5-9303-c8b05b8c6463?syn-25a6b1a6=1)**

Masayoshi Son places France at the centre of his global AI ambitions

Financial Times • 1d ago

---

**[SoftBank plans 75 billion euros of AI investments in France, as Europe struggles to catch up with U.S. and China](https://www.cnbc.com/2026/05/31/softbank-to-build-up-ai-data-centers-in-france-with-major-investment.html)**

SoftBank said the investment, described as the biggest of its kind so far in Europe, would deliver 3.1 GW of capacity.

CNBC • 14h ago

---

---

## HackerNews: "ai"

**[Please Use AI](https://news.ycombinator.com/item?id=48323101)**

⬆️ 778 • 💬 392 • 2d ago • [shawnsmucker.substack.com](https://shawnsmucker.substack.com/p/please-use-ai)

---

**[Notes from the Mistral AI Now Summit](https://news.ycombinator.com/item?id=48325340)**

A few days in Paris for the Mistral AI Now Summit: open models, on-prem deployment, agentic harnesses, and why Mistral wants to be the European full-stack AI partner.

⬆️ 463 • 💬 210 • 2d ago • [koenvangilst.nl](https://koenvangilst.nl/lab/mistral-ai-now-summit)

---

**[Anthropic surpasses OpenAI to become most valuable AI startup](https://news.ycombinator.com/item?id=48336233)**

Anthropic has become the most valuable artificial intelligence startup in the world, surpassing OpenAI in market valuation. Following a new funding round, the valuation of the developer behind the Claude AI assistant has approached the $1 trillion mark, reports a Qazinform News Agency correspondent.

⬆️ 414 • 💬 466 • 1d ago • [Qazinform.com](https://qazinform.com/news/anthropic-surpasses-openai-to-become-worlds-most-valuable-ai-startup)

---

**[Is AI causing a repeat of frontend’s lost decade?](https://news.ycombinator.com/item?id=48321631)**

AI is doing to programming what framework-brain did to the frontend before. Deskilling, or just working at a higher level of abstraction?

⬆️ 402 • 💬 331 • 2d ago • [mastrojs.github.io](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/)

---

**[The solution might be cancelling my AI subscription](https://news.ycombinator.com/item?id=48345896)**

⬆️ 322 • 💬 220 • 7h ago • [thoughts.hmmz.org](https://thoughts.hmmz.org/2026-05-31.html)

---

**[SF startup is testing robots in Airbnbs, and trashing them, lawsuit claims](https://news.ycombinator.com/item?id=48317093)**

The guests behind the bookings have received negative reviews from a number of Bay Area hosts, alleging they damaged the property and personal belongings.

⬆️ 269 • 💬 150 • 2d ago • [sfstandard.com](https://sfstandard.com/2026/05/28/sf-startup-secretly-testing-robots-airbnbs-trashing-lawsuit-claims/)

---

**[Liquid AI reveals 8B-A1B MoE trained on 38T](https://news.ycombinator.com/item?id=48325306)**

Today, we’re releasing LFM2.5-8B-A1B, a high-throughput edge model optimized for fast, reliable tool calling and complex instruction following on consumer hardware, delivering compressed performance competitive with much larger models and day-one support across major inference frameworks.

⬆️ 243 • 💬 96 • 2d ago • [liquid.ai](https://www.liquid.ai/blog/lfm2-5-8b-a1b)

---

**[United Airlines 767 returns to Newark after Bluetooth name sparks alert](https://news.ycombinator.com/item?id=48345248)**

The flight crew issued repeated warnings and a one-minute ultimatum to passengers, demanding they turn off their Bluetooth devices.

⬆️ 188 • 💬 300 • 8h ago • [Simple Flying](https://simpleflying.com/united-airlines-767-returns-newark-bluetooth-name-alert/)

---

**[AI job grief: A psychological crisis hitting tech workers](https://news.ycombinator.com/item?id=48336760)**

Across hundreds of Reddit threads and a small body of clinical literature, AI-driven displacement is producing an emotional category that most closely resembles grief, and the institutions causing it have no language for it.

⬆️ 186 • 💬 176 • 1d ago • [jackmaguire.org](https://jackmaguire.org/blog/ai-job-grief/)

---

**[Corporate America Is Starting to Ration AI as Cost Skyrockets](https://news.ycombinator.com/item?id=48335388)**

⬆️ 179 • 💬 167 • 1d ago • [wsj.com](https://www.wsj.com/tech/ai/corporate-america-is-starting-to-ration-ai-as-cost-skyrockets-1eb99d7a)

---

---

## YouTube Videos: "ai"

**[Our latest reports on AI | 60 Minutes Full Episodes](https://www.youtube.com/watch?v=iyVXw-SoUrY)**

From November 2025, Anderson Cooper's report on Anthropic. From December 2025, Sharyn Alfonsi's report on Character AI.

📺 60 Minutes

👁️ 192K • 👍 3K • 💬 310 • ⏱️ 1:32:36 • 1d ago

---

**[Elon Musk&#39;s DISTURBING AI Warning: You Have No Idea What&#39;s Coming in 2027](https://www.youtube.com/watch?v=kAmL_mM4ChM)**

Over the last decade, Elon Musk repeatedly warned that artificial intelligence could become humanity's biggest existential threat, ...

📺 Neural Nutshell

👁️ 8K • 👍 258 • 💬 104 • ⏱️ 15:53 • 1d ago

---

**[I Asked Grok AI To Predict The 2028 Election... LANDSLIDE Incoming!](https://www.youtube.com/watch?v=hqTezFeXrlA)**

Pollsmax* 》https://www.pollsmax.com/ ...

📺 Election Time

👁️ 145K • 👍 5K • 💬 1K • ⏱️ 18:32 • 2d ago

---

**[Google Just Dropped The Singularity Bomb](https://www.youtube.com/watch?v=BH5_FEJNOGY)**

Google DeepMind's Demis Hassabis says humanity may already be standing in the foothills of the singularity. AI agents are now ...

📺 AI Revolution

👁️ 55K • 👍 2K • 💬 208 • ⏱️ 13:24 • 2d ago

---

**[I Created an AI Clone… Biggest Mistake Ever!](https://www.youtube.com/watch?v=3reHSl0aOH4)**

I created my own AI clone, but things quickly turned completely out of control! Was creating an AI clone the biggest mistake ever?

📺 Ivan and Maria

👁️ 68K • 👍 863 • 💬 12 • ⏱️ 25:11 • 1d ago

---

**[The Hidden Cost of Coding With AI](https://www.youtube.com/watch?v=qWPl3JSt6A0)**

Developer Bootcamp & Mentoring Program — Start or level up your career with my proven training and personal mentoring: ...

📺 Stefan Mischook

👁️ 3K • 👍 135 • 💬 23 • ⏱️ 8:40 • 6h ago

---

**[&quot;Most Actors Are Going Broke, Jobs Gone Forever...&quot; First AI Film Has Hollywood Scared, Cost $2,000](https://www.youtube.com/watch?v=9-pWHt3utu8)**

Tiege Hanley: Get your first box 40% off (+ FREE gift), and 20% off for life, at https://tiege.com/antondaniels Join the Bag Chasers ...

📺 Anton Daniels

👁️ 54K • 👍 2K • 💬 1K • ⏱️ 11:34 • 11h ago

---

**[AI Trading Bots Are About To Wipe People Out](https://www.youtube.com/watch?v=MCe-1gbD1lY)**

Join Tier One Trading: https://tieronetrading.com Start the 30 Day Trader Challenge: https://bit.ly/30-day-trader Forecaster: ...

📺 Jason Graystone

👁️ 4K • 👍 227 • 💬 127 • ⏱️ 4:36 • 16h ago

---

**[The Most Disturbing AI Ad You Will See Today](https://www.youtube.com/watch?v=fBbyHkUD_IM)**

I stumbled across this AI-generated Spencer Pratt ad and it is honestly unsettling. Is this the future of campaign ads? Let me know ...

📺 God & Politics 

👁️ 97K • 👍 8K • 💬 251 • ⏱️ 0:55 • 22h ago

---

**[AI Fruit Drama Is STUPID😭](https://www.youtube.com/watch?v=ApdQ5OMaH4Q)**

Original video: https://www.tiktok.com/@afruitstorys Watch videos on spotify: ...

📺 RICHLEV

👁️ 180K • 👍 7K • 💬 2K • ⏱️ 25:09 • 18h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 36,730 • ❤️ 652 • 5d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 24,586 • ❤️ 573 • 4d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,439,402 • ❤️ 1,150 • 1mo ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 436 • 5d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 27,677 • ❤️ 312 • 2h ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 2,948 • ❤️ 990 • 3d ago

---

**[PiD](https://huggingface.co/nvidia/PiD)**

*NVIDIA*

PiD is a conditional pixel-space diffusion model that unifies decoding and upsampling for image-to-image tasks. It performs super-resolution in a single pass, directly denoising in high-resolution pixel space, supporting up to 4x or 8x upscaling for various base models like Flux and SD3.

`image-to-image`

⬇️ 498 • ❤️ 214 • 5d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,886,599 • ❤️ 4,491 • 25d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 143,904 • ❤️ 427 • 10d ago

---

**[Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)**

*StepFun*

Step-3.7-Flash is a 198B parameter sparse MoE vision-language model with a 256k context window, excelling at multimodal perception, workflow integrity, and code engineering for agentic applications. It offers selectable reasoning levels to balance speed, cost, and cognitive depth, achieving high throughput for production workloads.

`image-text-to-text` `201.4B`

⬇️ 7,638 • ❤️ 158 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 208 • 💬 3 • ⭐ 3,412 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 82 • 💬 3 • ⭐ 81,156 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 27,754 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 5 • 💬 1 • ⭐ 6,451 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation](https://huggingface.co/papers/2602.08968)**

*Lucas Maes, Quentin Le Lidec, Dan Haramati et al. (7 authors)*

🏢 galilai-group

Stable-worldmodel provides a modular and standardized research framework for developing and evaluating world models with controllable environmental factors for robustness and continual learning applications.

▲ 5 • 💬 0 • ⭐ 1,562 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.08968) • [💻 code](https://github.com/galilai-group/stable-worldmodel) • [🔗 project](https://galilai-group.github.io/stable-worldmodel/)

---

**[MOSS-TTS Technical Report](https://huggingface.co/papers/2603.18090)**

*Yitian Gong, Botian Jiang, Yiwei Zhao et al. (26 authors)*

🏢 OpenMOSS

MOSS-TTS is a speech generation model using discrete audio tokens and autoregressive modeling with capabilities for voice cloning, pronunciation control, and long-form generation across multiple languages.

▲ 14 • 💬 2 • ⭐ 2,750 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.18090) • [💻 code](https://github.com/OpenMOSS/MOSS-TTS) • [🔗 project](https://mosi.cn/models/moss-tts)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 65,805 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models](https://huggingface.co/papers/2605.30263)**

*Min Zhao, Hongzhou Zhu, Bokai Yan et al. (12 authors)*

A comprehensive framework is presented for converting bidirectional video diffusion models into real-time interactive world models with controllable, causal, and low-latency capabilities through fine-tuning and distillation techniques.

▲ 49 • 💬 3 • ⭐ 417 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.30263) • [💻 code](https://github.com/shengshu-ai/minWM)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 36 • 💬 5 • ⭐ 3,476 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[VibeSearchBench: Benchmarking Long-horizon Proactive Search in the Wild](https://huggingface.co/papers/2605.27882)**

*Xiaohongshu Inc*

🏢 rednote-hilab

LLM-based agents perform poorly on VibeSearch benchmark, which evaluates multi-turn dialogue search scenarios reflecting real user-agent collaboration rather than traditional single-turn query tasks.

▲ 11 • 💬 2 • ⭐ 476 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.27882) • [💻 code](https://github.com/VibeBench/VibeSearchBench) • [🔗 project](https://vibebench.github.io/VibeSearchBench.github.io/)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.6k • 🔱 550 • 2d ago

---

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`JavaScript`

⭐ 4.6k • 🔱 654 • 5h ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.1k • 🔱 647 • 1d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.8k • 🔱 192 • 10h ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 2.5k • 🔱 232 • 2d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 400 • 9d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.3k • 🔱 362 • 14d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.2k • 🔱 147 • 5h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.1k • 🔱 212 • 6d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.8k • 🔱 210 • 15h ago

---

---

*Generated by PeekDeck - A glance is all you need*
