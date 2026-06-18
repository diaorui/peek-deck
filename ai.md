---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-18T09:54:07.066861+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 18, 2026 at 09:54 UTC  
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

**[Anthropic CEO Dario Amodei goes completely candid on why he left OpenAI: "When you feel that you can't trust someone when you see disturbing patterns of behavior, dishonesty, that makes it very hard to continue."](https://www.reddit.com/r/artificial/comments/1u8zigf/anthropic_ceo_dario_amodei_goes_completely_candid/)**

In a recent candid interview Anthropic CEO Dario Amodei did not hold back regarding his departure from OpenAI. He cited a fundamental breakdown of trust and "disturbing patterns of behavior" and "dishonesty" as the primary reasons it became impossible to stay. Considering the massive wave of high-profile safety researcher departures from OpenAI over the last year or two, Amodei’s comments add a lot of retroactive context to the cultural shift that happened right around the time ChatGPT was being spun up. What do you think? Does this align with everything we've seen play out with Sam Altman and the board over the past couple of years?

2h ago

---

**[Elon Musk's Grok Rained Bombs On Iran Even As Anthropic Pulled Out, Pentagon Reveals](https://www.reddit.com/r/artificial/comments/1u8atbd/elon_musks_grok_rained_bombs_on_iran_even_as/)**

Pentagon AI chief confirmed under oath that Grok replaced Claude inside Project Maven and enabled 2,000+ munitions strikes in 96 hours during Operation Epic Fury.

🔗 [News18](https://www.news18.com/world/elon-musks-grok-rained-bombs-on-iran-even-as-anthropic-pulled-out-pentagon-reveals-ws-l-10156416.html) • 20h ago

---

**[OpenAI's Losses Swelled to $38.5B in 2025 Despite $13B Revenue Surge](https://www.reddit.com/r/artificial/comments/1u916c5/openais_losses_swelled_to_385b_in_2025_despite/)**

Leaked financial documents show OpenAI generated $13.07 billion in revenue in 2025 but posted a staggering $38.5 billion net loss amid soaring AI spending.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/openai-38-5-billion-loss-13-billion-revenue-2025/) • 50m ago

---

**[Copilot vulnerability could expose emails and 2FA codes](https://www.reddit.com/r/artificial/comments/1u8wxqd/copilot_vulnerability_could_expose_emails_and_2fa/)**

This sneaky attack tricks Microsoft's AI assistant to hand over your data.

🔗 [Mashable](https://mashable.com/tech/searchleak-microsoft-copilot-ai-assistant-vulnerability-report) • 4h ago

---

**[A 4b model is now beating 30b ones at web research and the reason is not size](https://www.reddit.com/r/artificial/comments/1u8bgrv/a_4b_model_is_now_beating_30b_ones_at_web/)**

A small thing from this month's model releases stuck with me more than the usual flagship leaderboard race, because it points at where the interesting progress actually is. A 4 billion parameter open model reportedly beat every open source model in the 30 billion class on a couple of hard web research benchmarks. Not matched, beat. A model you could run on a laptop outperforming ones roughly eight times its size on the specific task of going out, reading sources, and answering a multi step question. The reason that is interesting is the why. For the last couple of years the implied formula was straightforward, more parameters, more capability, and the leaderboard mostly cooperated. A result like this says the relationship is a lot looser than that for some skills. The claim from the people who built it is that research ability came from careful construction of the training data and from teaching the model to check and revise its own work, rather than from raw scale. In other words how you train a small model for a task can matter more than how big a generic model you throw at it. This particular one comes from a family, apodex, that is built around the idea of a system verifying its own answers before committing to them, and the small open versions seem to inherit that habit even though the headline flagship is a much larger closed model. Why this matters if you are not training models yourself. The expensive, capable research assistants have mostly lived behind apis you pay per query for. If a small model that runs on ordinary hardware can do a real chunk of that work, the cost and access picture changes for students, small teams, anyone in a place where the paid services are pricey or just unavailable. It also means the gap between what a big lab can do and what a hobbyist can run locally is narrower on some tasks than the flagship marketing suggests, which is healthy for the field. The caveat is the obvious one, a benchmark win is not the same as being reliable on your actual question, and the small model is not going to match the big hosted system on the genuinely hard stuff. But the direction is the part worth watching. If the lever for capability on a given task is data quality and training method rather than parameter count, a lot more of this becomes reproducible by people who are not sitting on a giant compute budget. That is a more democratic trajectory than the last two years pointed at, and it is showing up in things you can actually download now. EDIT: A few people asked for the model and sources, so here they are. Model card: https://huggingface.co/apodex/Apodex-1.0-4B-SFT Technical blog: https://www.apodex.com/blog/apodex-1.0 Evaluation harness: https://github.com/ApodexAI/AgentHarness

19h ago

---

**[Building independent LLM drift detection - sharing the methodology, looking for feedback on the approach](https://www.reddit.com/r/artificial/comments/1u91u9d/building_independent_llm_drift_detection_sharing/)**

Disclosed upfront: I run [Tickerr dot ai], an independent external monitor for AI APIs. Today it tracks latency, TTFT, uptime, and error rates across major models. I’m trying to validate a more specific idea before building too much. Basic transport health is not the hard part. If Claude/OpenAI/Gemini gets slow, times out, or throws 5xx errors, most teams can catch that with APM, logs, Sentry, Langfuse, Helicone, Datadog, etc. The harder failure mode seems to be silent model behavior drift when API returns 200, latency is normal, no exception is thrown, output looks plausible, but JSON adherence, tool-calling, refusal behavior, reasoning quality, or instruction-following has quietly degraded. This gets worse with agentic systems. In a normal chat, drift may produce a bad answer but in an agentic workflow, the model can silently choose the wrong tool, stop early, mark a task as complete, or take a bad action while everything still looks successful at the API level. The system is running and confidently doing worse work. User complaints are still the primary detection mechanism currently for these. VIGIL (arXiv 2605.08747) found 65 to 88 percent of false-success reports happened at literally zero task progress. DeployBench (2606.05238) found most failures were the system stopping against a softer bar it set for itself and returning clean. Plausible-in-isolation is the failure mode itself, not a sign you are safe, which is why a single model's output never alerts on its own. That's what I'm thinking to build - an external drift detection probe on top LLM APIs, that stays out of your system and does continuous checks every hour, to find out these silent degradations, and sends proactive alerts. Rough idea: External canary suite: run private fixed prompts on a schedule against major models. Track schema adherence, instruction-following, refusal/over-refusal, output length, tool-call format, and simple deterministic correctness checks. Drift baseline: Do not judge a single output in isolation. Track whether today’s behavior has materially shifted versus that model’s own baseline. Cross-model comparison: For some task types, compare model behavior against peer models. Not to say which model is “right”, but to detect abnormal divergence. Example: “Sonnet and Gemini usually disagree 12% of the time on this task type; today disagreement is 28%.” Optional bring your own prompts: A paid tier where you provide some critical prompts from your own workload. Tickerr runs them on a schedule and alerts if behavior drifts from your baseline. Prompts would remain private and would not be public benchmark prompts. What I’m trying to learn: Is this technically sound enough to be useful, or are there are other failure modes that I am missing / are more valuable ? Which alerts would you actually care about? JSON/schema adherence drift tool-call format drift refusal/over-refusal drift output length drift cross-model disagreement spike bring-your-own-prompt regression alerts Would you pay for this, or would you just build it yourself? If you would pay, what pricing feels realistic? $19/month $99/month $299+/month for team/Slack/webhook/BYO prompts Brutal feedback welcome. If this is not a real pain, I’d rather know now, or which direction you feel makes more sense to take this.

9m ago

---

**[Anyone in research](https://www.reddit.com/r/artificial/comments/1u8ztub/anyone_in_research/)**

if there's anyone here who is research area of AI like currently working in research for ai please drop a comment here i actually need some guidance and if you're are okay we can talk in dm as well. TL/DR: I'm a student learning ml so need some guidance

2h ago

---

**[Anyone else's coding agent just sit there for 30 minutes?](https://www.reddit.com/r/artificial/comments/1u8uvlk/anyone_elses_coding_agent_just_sit_there_for_30/)**

Watched a coding agent spend 30 minutes "thinking" on what should've been a 10-minute task — barely touched any tokens, just… sat there. Not the first time I've seen it. How common is this for everyone else? When your AI coding agent stalls like that, what's usually the cause in your setup — context bloat, a tool call hanging, waiting on a confirmation, something else? And do you just kill + restart, or have you found a way to keep it moving? Trying to figure out if it's a me-problem or an everyone-problem.

6h ago

---

**[Do you think most people are using AI more as a tool or as a replacement for thinking?](https://www.reddit.com/r/artificial/comments/1u8iyrv/do_you_think_most_people_are_using_ai_more_as_a/)**

I’ve noticed that some people use AI just to speed things up or get quick answers, while others seem to rely on it more and more for ideas, writing, decisions, and problem-solving. It made me wonder where most people actually stand. Do you think AI is mostly being used as a helpful tool, or has it started replacing a lot of people’s own thinking and creativity?

15h ago

---

**[Best AI for cartoon image generation](https://www.reddit.com/r/artificial/comments/1u8qlwu/best_ai_for_cartoon_image_generation/)**

Ok so, I have been telling my kids a bedtime story over the past couple of weeks. I tried using the free version of chatgpt and gemini but they are very inconsistent with the characters and eventually runs out of time. I think I'd eventually want to turn the photos into a book for my kids. What would be the best AI option to help me create these story board style photos? I am willing to pay a small amount but nothing crazy.

10h ago

---

---

## Google News: "ai"

**[Allbirds continues AI pivot with name change and CEO hire, sending stock soaring](https://www.cnbc.com/2026/06/17/allbirds-bird-ai-smartbird-ceo.html)**

Allbirds became NewBird AI in April and said it would trade shoes for AI compute infrastructure.

CNBC • 18h ago

---

**[AI will lead to labour shortages, Bezos says in optimistic talk](https://www.reuters.com/business/world-at-work/ai-will-lead-labour-shortages-jeff-bezos-says-vivatech-2026-06-17/)**

Reuters • 17h ago

---

**[Trump's shadow AI policy](https://www.axios.com/2026/06/18/trump-shadow-ai-policy)**

Axios • 36m ago

---

**[How A.I. Apps Teach Students How to Cheat](https://www.nytimes.com/2026/06/18/us/ai-apps-students-cheat.html)**

The New York Times • 53m ago

---

**[Why do AI models struggle with online hate speech detection?](https://www.aljazeera.com/news/2026/6/18/why-do-ai-models-struggle-with-online-hate-speech-detection)**

As the UN marks International Day for Countering Hate Speech, Al Jazeera examines how AI handles it - and falls short.

Al Jazeera • 1h ago

---

**[Apple boss Tim Cook says prices to rise due to memory chip costs](https://www.bbc.com/news/articles/c3wyxvqdx1zo)**

The firm's outgoing boss Tim Cook did not say when prices will rise or which products will be affected.

BBC • 2h ago

---

**[A Rock Band Went Viral. Then AI Scammers Moved In](https://time.com/article/2026/06/17/ai-scam-music-sons-legion/)**

Scammers are using AI tools to impersonate the band Sons of Legion and scam their fans. Could your favorite band be next?

Time Magazine • 14h ago

---

**[State Farm’s AI Plan for Sales Agents Sparks Uproar. ‘A Real Slap in the Face.’](https://www.wsj.com/finance/state-farms-ai-plan-for-sales-agents-sparks-uproar-a-real-slap-in-the-face-6453e2cb)**

WSJ • 1d ago

---

**[AI Is Taking Over Hospitals](https://www.theatlantic.com/health/2026/06/ai-healthcare-uber-moment/687567/)**

This is health care’s Uber moment.

The Atlantic • 22h ago

---

**[Anthropic opens Seoul office and announces new partnerships across the Korean AI ecosystem](https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem)**

Anthropic opens Seoul and announces new partnerships across the Korean AI ecosystem—with the enterprises, startups, and researchers behind some of the most ambitious deployments of Claude.

Anthropic • 18h ago

---

---

## HackerNews: "ai"

**[Sixty percent of US consumers say 'AI' in brand messaging is a turnoff](https://news.ycombinator.com/item?id=48569278)**

Original research from 2,000 decision-makers and consumers on AI brand visibility, content trust, and what brands need to do as the web feels less human. 74% say the internet feels less human than it did 10 years ago.

⬆️ 1042 • 💬 550 • 21h ago • [The Leading Enterprise Content Platform | WordPress VIP](https://wpvip.com/future-of-the-web-2026/)

---

**[Has AI already killed self-help nonfiction books?](https://news.ycombinator.com/item?id=48558489)**

⬆️ 401 • 💬 472 • 1d ago • [tim.blog](https://tim.blog/2026/06/12/has-ai-already-killed-nonfiction/)

---

**[AI demands more engineering discipline. Not less](https://news.ycombinator.com/item?id=48570948)**

⬆️ 381 • 💬 189 • 19h ago • [charitydotwtf.substack.com](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline)

---

**[Only 16 Percent of Americans Think AI Will Have a Positive Impact on Society](https://news.ycombinator.com/item?id=48573332)**

Although Wall Street loves AI, every day Americans are significantly less optimistic about the industry, a new report from Pew Research shows.

⬆️ 380 • 💬 458 • 16h ago • [TechCrunch](https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/)

---

**[My Homelab AI Dev Platform](https://news.ycombinator.com/item?id=48542433)**

Self-hosting OpenCode Web for GitOps style homelab changes.

⬆️ 364 • 💬 56 • 2d ago • [rsgm.dev](https://rsgm.dev/post/ai-dev-platform/)

---

**[The founder's playbook: Building an AI-native startup](https://news.ycombinator.com/item?id=48566832)**

We share how AI-native founders are using Claude at every stage of the startup journey, with practical exercises, frameworks, and prompts.

⬆️ 230 • 💬 160 • 1d ago • [Claude](https://claude.com/blog/the-founders-playbook)

---

**[Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)**

CADAM is the open source text-to-CAD web application - Adam-CAD/CADAM

⬆️ 183 • 💬 86 • 17h ago • [GitHub](https://github.com/Adam-CAD/CADAM)

---

**[Microsoft turns to AWS as GitHub faces AI capacity crunch](https://news.ycombinator.com/item?id=48549918)**

Microsoft is adding AWS capacity for GitHub after AI-driven usage strained the developer platform, exposing Azure constraints and the infrastructure cost of agentic coding.

⬆️ 154 • 💬 75 • 2d ago • [RuntimeWire](https://runtimewire.com/article/microsoft-github-aws-ai-capacity-crunch)

---

**[Can Europe train a frontier AI model on the compute it owns?](https://news.ycombinator.com/item?id=48541014)**

A sourced model and short report: can Europe train a sovereign frontier AI model on the public compute it already owns, while gigawatt datacenters wait years for grid power? - sammysltd/euromesh

⬆️ 142 • 💬 293 • 2d ago • [GitHub](https://github.com/sammysltd/euromesh)

---

**[The Competitive Moat That AI Can't Replicate](https://news.ycombinator.com/item?id=48573435)**

Portfolio and personal blog of Chris Hillman.

⬆️ 136 • 💬 114 • 16h ago • [ghostinthedata.info](https://ghostinthedata.info/posts/2026/2026-06-13-human-connection-moat/)

---

---

## YouTube Videos: "ai"

**[The US Government Just Killed The Most Powerful AI Ever Made](https://www.youtube.com/watch?v=7vz6T6TNIzo)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *The most powerful AI ever released to the ...

📺 Julia McCoy

👁️ 11K • 👍 607 • 💬 87 • ⏱️ 10:09 • 7h ago

---

**[Jeff Bezos Makes Shocking AI Prediction and the Future of Jobs](https://www.youtube.com/watch?v=qI1tLQF-_9A)**

Speaking at the VivaTech conference in Paris on June 17, the Jeff Bezos pushed back on fears that artificial intelligence will ...

📺 New York Post

👁️ 6K • 👍 129 • 💬 38 • ⏱️ 5:28 • 10h ago

---

**[9 AI Agent Trends To Get Ahead of 99% of People](https://www.youtube.com/watch?v=vhyna9ur6Gc)**

Become Agent Native: 9 Inevitable AI Agent Trends (Skills, Super Apps, Automations, Computer Control, and Cost) Learn ...

📺 Riley Brown

👁️ 7K • 👍 358 • 💬 25 • ⏱️ 33:39 • 7h ago

---

**[We Might Actually Need to Stop AI](https://www.youtube.com/watch?v=CvA8-aScqio)**

My FREE AI OS Course: ...

📺 Nate Herk | AI Automation

👁️ 34K • 👍 962 • 💬 264 • ⏱️ 12:28 • 1d ago

---

**[I Tried PewDiePie’s Odysseus AI So You Don’t Have To (Its FREE)](https://www.youtube.com/watch?v=_7BHqZayPOc)**

Try Recraft V4.1 now and experience an image generation model with exceptional visual taste : https://go.recraft.ai/MattWolfe ...

📺 Matt Wolfe

👁️ 25K • 👍 876 • 💬 104 • ⏱️ 31:47 • 17h ago

---

**[Maths is Cooked: AI&#39;s Latest Breakthrough -- And What&#39;s Next](https://www.youtube.com/watch?v=k5dZmMa0OIA)**

Take back your personal data with Incogni! Use code Sabine at the link below and get 60% off annual plans: ...

📺 Sabine Hossenfelder

👁️ 194K • 👍 10K • 💬 2K • ⏱️ 7:39 • 18h ago

---

**[China’s New AI Is 6X More Efficient Than Claude](https://www.youtube.com/watch?v=gKBazze-8qU)**

China just dropped two new open-weight coding models, Kimi K2.7 Code and GLM-5.2, and the timing could not be more ...

📺 AI Revolution

👁️ 18K • 👍 603 • 💬 48 • ⏱️ 16:01 • 10h ago

---

**[The People Building AI Just Revealed Their End Goal](https://www.youtube.com/watch?v=RopkgBzHD8s)**

discord.gg/nickjones Source media: https://youtu.be/b1_7Pt0DJos?si=r1cZlHFuFNq6Nj8W ...

📺 Nick Jones

👁️ 21K • 👍 914 • 💬 179 • ⏱️ 27:00 • 1d ago

---

**[AI Will Never Be The Same After This](https://www.youtube.com/watch?v=vHFIvXE7hcg)**

LIMITLESS HQ ⬇️ NEWSLETTER: https://limitlessft.substack.com/ FOLLOW ON X: https://x.com/LimitlessFT SPOTIFY: ...

📺 Limitless Podcast

👁️ 10K • 👍 278 • 💬 44 • ⏱️ 29:26 • 1d ago

---

**[New #1 open-source AI model is here!](https://www.youtube.com/watch?v=6d__WOpZswY)**

GLM 5.2 review. New best open source AI model. #ai #aitools #llm #ainews #agi #singularity #gpt #deepseek Thanks to our ...

📺 AI Search

👁️ 239K • 👍 8K • 💬 922 • ⏱️ 29:57 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 146,784 • ❤️ 1,567 • 7h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 666 • ❤️ 1,155 • 1d ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 42,198 • ❤️ 1,077 • 2d ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 172,727 • ❤️ 859 • 3d ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 460,173 • ❤️ 986 • 7d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 1,950 • ❤️ 347 • 1d ago

---

**[Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)**

*Prefeitura do Rio de Janeiro (City of Rio de Janeiro)*

Rio 3.5 Open 397B is a frontier-class, open-source image-text-to-text AI model post-trained from Qwen 3.5 397B. It excels in agentic coding, STEM, multilingual tasks, and multimodal reasoning, featuring a 1M context window and SwiReasoning for enhanced accuracy and efficiency.

`image-text-to-text` `403.4B`

⬇️ 189,986 • ❤️ 321 • 3d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 183,093 • ❤️ 2,142 • 5d ago

---

**[Qwopus3.6-27B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF)**

*Jackrong*

Qwopus-3.6-27B-Coder is a 27B parameter multimodal model fine-tuned for agentic coding and tool-use reasoning. It excels at repository-level code generation, debugging, and structured tool orchestration, leveraging trace inversion and native long-context support for complex developer workflows.

`image-text-to-text` `460.7M`

⬇️ 99,909 • ❤️ 241 • 3d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 3,420,052 • ❤️ 1,947 • 2mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 236 • 💬 4 • ⭐ 8,135 • 27d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 30 • 💬 1 • ⭐ 21,939 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 99 • 💬 4 • ⭐ 87,024 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 18 • 💬 1 • ⭐ 82,886 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 42 • 💬 4 • ⭐ 30,608 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[FastContext: Training Efficient Repository Explorer for Coding Agents](https://huggingface.co/papers/2606.14066)**

*Shaoqiu Zhang, Maoquan Wang, Yuling Shi et al. (8 authors)*

🏢 Microsoft

FastContext separates repository exploration from code solving in LLM agents using specialized exploration models that reduce token consumption and improve resolution rates.

▲ 81 • 💬 3 • ⭐ 542 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14066) • [💻 code](https://github.com/microsoft/fastcontext) • [🔗 project](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)

---

**[JoyAI-VL-Interaction: Real-Time Vision-Language Interaction Intelligence](https://huggingface.co/papers/2606.14777)**

*Dingyu Yao, Junhao Zhou, Chenxu Yang et al. (15 authors)*

🏢 JD.com Open Source

A vision-language model operates continuously in real-time, making autonomous decisions about when to respond or delegate, enabling interactive systems that perceive and act upon environmental changes without user prompting.

▲ 181 • 💬 2 • ⭐ 266 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14777) • [💻 code](https://github.com/jd-opensource/JoyAI-VL-Interaction) • [🔗 project](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 80 • 💬 7 • ⭐ 77,606 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 167 • 💬 2 • ⭐ 67,963 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[VibeThinker-3B: Exploring the Frontier of Verifiable Reasoning in Small Language Models](https://huggingface.co/papers/2606.16140)**

*Sen Xu, Shixi Liu, Wei Wang et al. (9 authors)*

🏢 WeiboAI

VibeThinker-3B demonstrates that compact models can achieve state-of-the-art performance on verifiable reasoning tasks through specialized training techniques, challenging conventional scaling assumptions.

▲ 90 • 💬 1 • ⭐ 903 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.16140) • [💻 code](https://github.com/WeiboAI/VibeThinker) • [🔗 project](https://github.com/WeiboAI/VibeThinker)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 73.3k • 🔱 9.4k • 1h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 33.9k • 🔱 1.5k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 9.7k • 🔱 878 • 6m ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 4.4k • 🔱 391 • 4h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 3.7k • 🔱 410 • 1m ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.5k • 🔱 360 • 3h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.3k • 🔱 395 • 23h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.1k • 🔱 192 • 1d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.6k • 🔱 143 • 2d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.5k • 🔱 113 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
