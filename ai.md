---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-17T18:41:45.474857+00:00'
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

**Last Updated:** June 17, 2026 at 18:41 UTC  
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

**[Elon Musk's Grok Rained Bombs On Iran Even As Anthropic Pulled Out, Pentagon Reveals](https://www.reddit.com/r/artificial/comments/1u8atbd/elon_musks_grok_rained_bombs_on_iran_even_as/)**

Pentagon AI chief confirmed under oath that Grok replaced Claude inside Project Maven and enabled 2,000+ munitions strikes in 96 hours during Operation Epic Fury.

🔗 [News18](https://www.news18.com/world/elon-musks-grok-rained-bombs-on-iran-even-as-anthropic-pulled-out-pentagon-reveals-ws-l-10156416.html) • 4h ago

---

**[A 4b model is now beating 30b ones at web research and the reason is not size](https://www.reddit.com/r/artificial/comments/1u8bgrv/a_4b_model_is_now_beating_30b_ones_at_web/)**

A small thing from this month's model releases stuck with me more than the usual flagship leaderboard race, because it points at where the interesting progress actually is. A 4 billion parameter open model reportedly beat every open source model in the 30 billion class on a couple of hard web research benchmarks. Not matched, beat. A model you could run on a laptop outperforming ones roughly eight times its size on the specific task of going out, reading sources, and answering a multi step question. The reason that is interesting is the why. For the last couple of years the implied formula was straightforward, more parameters, more capability, and the leaderboard mostly cooperated. A result like this says the relationship is a lot looser than that for some skills. The claim from the people who built it is that research ability came from careful construction of the training data and from teaching the model to check and revise its own work, rather than from raw scale. In other words how you train a small model for a task can matter more than how big a generic model you throw at it. This particular one comes from a family, apodex, that is built around the idea of a system verifying its own answers before committing to them, and the small open versions seem to inherit that habit even though the headline flagship is a much larger closed model. Why this matters if you are not training models yourself. The expensive, capable research assistants have mostly lived behind apis you pay per query for. If a small model that runs on ordinary hardware can do a real chunk of that work, the cost and access picture changes for students, small teams, anyone in a place where the paid services are pricey or just unavailable. It also means the gap between what a big lab can do and what a hobbyist can run locally is narrower on some tasks than the flagship marketing suggests, which is healthy for the field. The caveat is the obvious one, a benchmark win is not the same as being reliable on your actual question, and the small model is not going to match the big hosted system on the genuinely hard stuff. But the direction is the part worth watching. If the lever for capability on a given task is data quality and training method rather than parameter count, a lot more of this becomes reproducible by people who are not sitting on a giant compute budget. That is a more democratic trajectory than the last two years pointed at, and it is showing up in things you can actually download now. EDIT: A few people asked for the model and sources, so here they are. Model card: https://huggingface.co/apodex/Apodex-1.0-4B-SFT Technical blog: https://www.apodex.com/blog/apodex-1.0 Evaluation harness: https://github.com/ApodexAI/AgentHarness

4h ago

---

**[AI made me more productive, but somehow more tired](https://www.reddit.com/r/artificial/comments/1u82hpd/ai_made_me_more_productive_but_somehow_more_tired/)**

Is anyone else feeling this? AI has made me faster at almost everything. Writing, research, planning, summarizing, learning, replying — all of it is quicker now. But instead of feeling like I have more free time, I feel like the standard just moved. If something used to take 3 hours and now takes 30 minutes, the result isn’t “great, I can rest.” It’s “great, now I can do 5 more things.” I get why everyone is excited about AI productivity, and I use these tools every day. But I also feel like they quietly raised the baseline for what a normal person is expected to output. Sometimes I miss when I didn’t know I could move this fast. Does anyone else feel like AI made work easier technically, but life harder psychologically?

12h ago

---

**[New survey: ~half of Americans don't recognize Sam Altman or Dario Amodei. Does name recognition shape how AI gets judged?](https://www.reddit.com/r/artificial/comments/1u8h2ie/new_survey_half_of_americans_dont_recognize_sam/)**

A national survey compared favorability and name recognition for 8 major tech executives, and the recognition gap is what stood out. The people most associated with building AI, Altman, Amodei, Huang, are unknown to a third to a half of the country, while opinions about tech as a whole keep getting measured through Musk and Zuckerberg, who most people know and view negatively. Tim Cook was the only one clearly above water. If most Americans can't name the people building AI, whose reputation is actually driving public opinion about it? Source: https://data.verasight.io/ai/many-americans-are-unfamiliar-with-sam-altman

59m ago

---

**[Apparently OpenAI's next voice model can listen and talk at the same time without freezing up](https://www.reddit.com/r/artificial/comments/1u8888x/apparently_openais_next_voice_model_can_listen/)**

Okay this is just floating around as a rumor right now but if true it's actually huge Next voice model is supposedly called GPT-Bidi-1, bidi for bidirectional, meaning it listens and talks at the same time instead of doing that thing where it just freezes the second you say "mm-hm" or try to jump in Can apparently adjust mid sentence too if you interrupt it which current voice mode absolutely cannot do If even half of this is true this fixes the most annoying thing about talking to chatgpt right now Anyone seen more on this...is this actually close or just early testing stuff

6h ago

---

**[Your company is probably spending more on coffee than AI](https://www.reddit.com/r/artificial/comments/1u7ta74/your_company_is_probably_spending_more_on_coffee/)**

19h ago

---

**[I coded the biologically possible network training algorithm by nobel prize winner - Jeff Hinton](https://www.reddit.com/r/artificial/comments/1u89mqc/i_coded_the_biologically_possible_network/)**

I went down the 'Papers by OG researchers' touching on biologically possible alternatives to backprop lol.

5h ago

---

**[If Anthropic opens Mythos to US citizens, wouldn't bypass mechanisms make it easy for non-US users to access too?](https://www.reddit.com/r/artificial/comments/1u8ilir/if_anthropic_opens_mythos_to_us_citizens_wouldnt/)**

Regional restrictions on digital services have often proven difficult to enforce completely, and inevitably Anthropic will release the model even if with regional restrictions and when it does so, I wonder how effective those measures would be in practice. Wouldn't it be easily accessible to restricted users too through various proxy mechanisms?

4m ago

---

**[What is the real cost of computing and token futures market](https://www.reddit.com/r/artificial/comments/1u8iiam/what_is_the_real_cost_of_computing_and_token/)**

Quick context: China is designing a futures market for AI tokens, with the Shanghai Futures Exchange in early stages of designing contracts for AI tokens here AI inference is becoming a real commodity cost, and nobody's hedged a commodity market that doesn't have a transparent, trusted spot price first. Oil futures didn't show up before oil pricing did. Same logic should apply here, but right now "the price of a token" is whatever each provider's pricing page says today, with no historical record, no standardization across providers. That gap gets more important as AI companies shift away from flat subscriptions toward usage-based/on-demand pricing. That's the model that exposes consumers and businesses directly to compute costs instead, which is great for transparency in theory, bad in practice if there's no independent benchmark to check prices against. A small group of researchers have been working on exactly that: an open, standardized index for tracking AI token prices over time, with the eventual goal of a real-time spot index and (longer term) the data infrastructure something like a futures market would actually need. Right now we're at the "define the standard" stage, basically: what the methodology should be. This is the part where outside feedback matters most, before assumptions get baked in. Research and current draft methodology: bellwethr.org We're trying to get the standard right with actual scrutiny from people who use these APIs and have opinions about where naive pricing comparisons go wrong. If you've got thoughts on methodology, edge cases we're missing, or just think the whole approach is flawed, that's exactly the discussion we want. We'll keep the discussion open and iterate publicly as feedback comes in, then move toward publishing the live index. If you want to follow along, there's an email signup on the site or I'll keep posting the progress here.

🔗 [bellwethr.org](http://bellwethr.org) • 7m ago

---

**[I found a secret API that gives $66/week of free GPT-5.5 & Claude Opus credits](https://www.reddit.com/r/artificial/comments/1u8i7k5/i_found_a_secret_api_that_gives_66week_of_free/)**

Hey developers, Found this tool called FreeModel.dev that gives free API access to GPT-5.5 and Claude Opus. Here's what you get: - $10 on signup (verify with Telegram) - $10 extra if you use a referral link - $66/week usage limit (~$10 per 5 hours) It's an OpenAI-compatible proxy, so you can use it with OpenCode, LangChain, basically any tool that supports OpenAI API. Link: freemodel.dev/invite/FRE-a4ce99da Full tutorial on Medium: https://medium.com/@mohaabdelkarim/i-found-a-secret-api-that-gives-you-66-week-of-free-gpt-5-5-claude-opus-credits-c0ad19558d96 Would be cool if anyone tried this and shared their experience!

18m ago

---

---

## Google News: "ai"

**['A signal of where power sits': Trump and world leaders joined by OpenAI, Anthropic, Google at G7](https://www.cnbc.com/2026/06/17/g7-trump-ai-tech-leaders-openai-anthropic-google.html)**

Frontier AI risks, infrastructure and sovereignty are all expected to be discussed at the world leaders' summit.

CNBC • 11h ago

---

**[AP Exclusive: Nvidia’s Jensen Huang says society needs ‘new social norms’ in the age of AI](https://apnews.com/article/nvidea-huang-artificial-intelligence-8334abcbc6ed8d3d7889b640ec6fa05b)**

Nvidia CEO Jensen Huang — whose work helped propel artificial intelligence — is stressing in an Associated Press interview that society has no choice but to change in the advent of AI.

AP News • 17h ago

---

**[Trump and AI CEOs discuss global AI rules](https://www.axios.com/2026/06/17/trump-ai-ceos-global-ai-rules)**

Axios • 1h ago

---

**[AI Health Startup Wants to Assist Half of Latin American Doctors](https://www.bloomberg.com/news/articles/2026-06-17/ai-health-startup-wants-to-assist-half-of-latin-american-doctors)**

Bloomberg.com • 55m ago

---

**[Jeff Bezos says AI will create more jobs at VivaTech Paris](https://www.bbc.com/news/articles/ceqdrw2yy3vo)**

The Amazon founder, who now has robotics and space travel companies, thinks AI will create a labour shortage.

BBC • 2h ago

---

**[Opinion | Dear A.I. Companies: The Doom Trolling Needs to Stop](https://www.nytimes.com/2026/06/17/opinion/ai-dangerous-openai-anthropic.html)**

The New York Times • 9h ago

---

**[College Grads Are Rejecting AI En Masse](https://www.motherjones.com/politics/2026/06/ai-commencement-student-graduation-speeches-booing-ai-mills-stanford-tech-elite/)**

The wave of booing aimed at AI-pilled commencement speakers signals a sea change in public opinion.

Mother Jones • 1h ago

---

**[Apple investors are tired of AI promises, want tangible progress](https://www.latimes.com/business/story/2026-06-17/apple-investors-are-tired-of-ai-promises-want-tangible-progress)**

Apple Inc. investors are losing patience with the company’s talk about becoming a more formidable presence in artificial intelligence and want to start seeing some results.

Los Angeles Times • 1h ago

---

**[Meet the world’s top AI-pilled economists](https://www.economist.com/finance-and-economics/2026/06/15/meet-the-worlds-top-ai-pilled-economists)**

The Economist • 1d ago

---

**[White House’s Anthropic move jolts Congress back into the AI debate](https://www.politico.com/news/2026/06/16/white-houses-anthropic-move-jolts-congress-back-into-the-ai-debate-00964614)**

Politico • 18h ago

---

---

## HackerNews: "ai"

**[Sixty percent of US consumers say 'AI' in brand messaging is a turnoff](https://news.ycombinator.com/item?id=48569278)**

Original research from 2,000 decision-makers and consumers on AI brand visibility, content trust, and what brands need to do as the web feels less human. 74% say the internet feels less human than it did 10 years ago.

⬆️ 840 • 💬 446 • 6h ago • [The Leading Enterprise Content Platform | WordPress VIP](https://wpvip.com/future-of-the-web-2026/)

---

**[Has AI already killed self-help nonfiction books?](https://news.ycombinator.com/item?id=48558489)**

⬆️ 385 • 💬 449 • 1d ago • [tim.blog](https://tim.blog/2026/06/12/has-ai-already-killed-nonfiction/)

---

**[My Homelab AI Dev Platform](https://news.ycombinator.com/item?id=48542433)**

Self-hosting OpenCode Web for GitOps style homelab changes.

⬆️ 361 • 💬 56 • 2d ago • [rsgm.dev](https://rsgm.dev/post/ai-dev-platform/)

---

**[Only 16 Percent of Americans Think AI Will Have a Positive Impact on Society](https://news.ycombinator.com/item?id=48573332)**

Although Wall Street loves AI, every day Americans are significantly less optimistic about the industry, a new report from Pew Research shows.

⬆️ 212 • 💬 193 • 1h ago • [TechCrunch](https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/)

---

**[AI demands more engineering discipline. Not less](https://news.ycombinator.com/item?id=48570948)**

⬆️ 209 • 💬 104 • 4h ago • [charitydotwtf.substack.com](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline)

---

**[The founder's playbook: Building an AI-native startup](https://news.ycombinator.com/item?id=48566832)**

We share how AI-native founders are using Claude at every stage of the startup journey, with practical exercises, frameworks, and prompts.

⬆️ 160 • 💬 132 • 11h ago • [Claude](https://claude.com/blog/the-founders-playbook)

---

**[AI is code – and can't be prompted into being smarter](https://news.ycombinator.com/item?id=48532178)**

From Java tests to Shai-Hulud, bots keep proving they'll swallow anything you feed them

⬆️ 158 • 💬 143 • 2d ago • [theregister](https://www.theregister.com/ai-and-ml/2026/06/14/ai-is-code-and-cant-be-prompted-into-being-smarter/5254141)

---

**[Microsoft turns to AWS as GitHub faces AI capacity crunch](https://news.ycombinator.com/item?id=48549918)**

Microsoft is adding AWS capacity for GitHub after AI-driven usage strained the developer platform, exposing Azure constraints and the infrastructure cost of agentic coding.

⬆️ 154 • 💬 75 • 1d ago • [RuntimeWire](https://runtimewire.com/article/microsoft-github-aws-ai-capacity-crunch)

---

**[Show HN: I wrote a C++ ray tracer from scratch without AI](https://news.ycombinator.com/item?id=48538833)**

C++ Path Tracer from scratch with zero third-party libraries. - themartiano/luz

⬆️ 154 • 💬 64 • 2d ago • [GitHub](https://github.com/themartiano/luz)

---

**[Can Europe train a frontier AI model on the compute it owns?](https://news.ycombinator.com/item?id=48541014)**

A sourced model and short report: can Europe train a sovereign frontier AI model on the public compute it already owns, while gigawatt datacenters wait years for grid power? - sammysltd/euromesh

⬆️ 142 • 💬 291 • 2d ago • [GitHub](https://github.com/sammysltd/euromesh)

---

---

## YouTube Videos: "ai"

**[THE AI Bubble JUST EXPOSED in LEAKED INFO...](https://www.youtube.com/watch?v=TCU2OER4ixQ)**

The AI boom may not be as profitable as Wall Street wants investors to believe. New leaked OpenAI financial disclosures reveal ...

📺 Wall Street Truthbombs

👁️ 5K • 👍 415 • 💬 67 • ⏱️ 9:13 • 4h ago

---

**[Maths is Cooked: AI&#39;s Latest Breakthrough -- And What&#39;s Next](https://www.youtube.com/watch?v=k5dZmMa0OIA)**

Take back your personal data with Incogni! Use code Sabine at the link below and get 60% off annual plans: ...

📺 Sabine Hossenfelder

👁️ 50K • 👍 4K • 💬 828 • ⏱️ 7:39 • 3h ago

---

**[How to Make Videos Like Chloe vs History With AI (Full Guide)](https://www.youtube.com/watch?v=OxyynOXX6mY)**

Create Your Own VIRAL History Videos with Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=robo21 In this video, I recreate the ...

📺 Roboverse

👁️ 6K • 💬 1 • ⏱️ 14:25 • 2h ago

---

**[The People Building AI Just Revealed Their End Goal](https://www.youtube.com/watch?v=RopkgBzHD8s)**

discord.gg/nickjones Source media: https://youtu.be/b1_7Pt0DJos?si=r1cZlHFuFNq6Nj8W ...

📺 Nick Jones

👁️ 15K • 👍 710 • 💬 143 • ⏱️ 27:00 • 21h ago

---

**[Google Just Revealed What Comes After AGI And It’s Shocking](https://www.youtube.com/watch?v=haB_od-xCWY)**

Google DeepMind just dropped a massive paper called From AGI to ASI, and the message is bigger than another AI release.

📺 AI Revolution

👁️ 75K • 👍 3K • 💬 367 • ⏱️ 13:33 • 1d ago

---

**[New #1 open-source AI model is here!](https://www.youtube.com/watch?v=6d__WOpZswY)**

GLM 5.2 review. New best open source AI model. #ai #aitools #llm #ainews #agi #singularity #gpt #deepseek Thanks to our ...

📺 AI Search

👁️ 160K • 👍 6K • 💬 735 • ⏱️ 29:57 • 15h ago

---

**[The AI Skills Nobody is Teaching (And Everyone Needs) | AI Expert Ethan Mollick](https://www.youtube.com/watch?v=9YMYVb1ASCg)**

Be honest: AI makes you a little nervous. Maybe you're afraid it'll take your job. Maybe you're overwhelmed by all the advice about ...

📺 Simon Sinek

👁️ 28K • 👍 1K • 💬 81 • ⏱️ 58:36 • 1d ago

---

**[They Looked Inside Claude’s AI&#39;s Mind. It Got Weird](https://www.youtube.com/watch?v=l72ufA-4SzE)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The paper is available here: ...

📺 Two Minute Papers

👁️ 60K • 👍 3K • 💬 191 • ⏱️ 6:57 • 1d ago

---

**[How To Create Long AI Anime With Consistent Characters](https://www.youtube.com/watch?v=qNCeIxja7Ws)**

How To Make Long AI Anime Videos (Full Workflow) Make your ai anime ...

📺 Skai Generated

👁️ 8K • ⏱️ 9:59 • 1d ago

---

**[AI Will Never Be The Same After This](https://www.youtube.com/watch?v=vHFIvXE7hcg)**

LIMITLESS HQ ⬇️ NEWSLETTER: https://limitlessft.substack.com/ FOLLOW ON X: https://x.com/LimitlessFT SPOTIFY: ...

📺 Limitless Podcast

👁️ 9K • 👍 268 • 💬 35 • ⏱️ 29:26 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 146,784 • ❤️ 1,403 • 19h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 666 • ❤️ 935 • 9h ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 42,198 • ❤️ 1,057 • 1d ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 172,727 • ❤️ 838 • 2d ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 460,173 • ❤️ 970 • 7d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 130,389 • ❤️ 2,133 • 5d ago

---

**[Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)**

*Prefeitura do Rio de Janeiro (City of Rio de Janeiro)*

Rio 3.5 Open 397B is a frontier-class, open-source image-text-to-text AI model post-trained from Qwen 3.5 397B. It excels in agentic coding, STEM, multilingual tasks, and multimodal reasoning, featuring a 1M context window and SwiReasoning for enhanced accuracy and efficiency.

`image-text-to-text` `403.4B`

⬇️ 189,986 • ❤️ 317 • 2d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 1,950 • ❤️ 294 • 15h ago

---

**[diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)**

*Unsloth AI*

DiffusionGemma-26B-A4B-it-GGUF is a 26B MoE multimodal generative model that produces text output from text, image, and video inputs using discrete diffusion. Optimized for speed and deployability, it leverages Gemma 4 architecture advancements for efficient token generation.

`image-text-to-text` `25.3B`

⬇️ 136,634 • ❤️ 295 • 5d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,876,624 • ❤️ 1,923 • 2mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 234 • 💬 4 • ⭐ 8,034 • 26d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 97 • 💬 4 • ⭐ 86,923 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 30 • 💬 1 • ⭐ 21,605 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[FastContext: Training Efficient Repository Explorer for Coding Agents](https://huggingface.co/papers/2606.14066)**

*Shaoqiu Zhang, Maoquan Wang, Yuling Shi et al. (8 authors)*

🏢 Microsoft

FastContext separates repository exploration from code solving in LLM agents using specialized exploration models that reduce token consumption and improve resolution rates.

▲ 81 • 💬 3 • ⭐ 455 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14066) • [💻 code](https://github.com/microsoft/fastcontext) • [🔗 project](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 42 • 💬 4 • ⭐ 30,589 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[JoyAI-VL-Interaction: Real-Time Vision-Language Interaction Intelligence](https://huggingface.co/papers/2606.14777)**

*Dingyu Yao, Junhao Zhou, Chenxu Yang et al. (15 authors)*

🏢 JD.com Open Source

A vision-language model operates continuously in real-time, making autonomous decisions about when to respond or delegate, enabling interactive systems that perceive and act upon environmental changes without user prompting.

▲ 171 • 💬 2 • ⭐ 256 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14777) • [💻 code](https://github.com/jd-opensource/JoyAI-VL-Interaction) • [🔗 project](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 18 • 💬 1 • ⭐ 82,697 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 80 • 💬 7 • ⭐ 77,481 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 167 • 💬 2 • ⭐ 67,853 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[DreamX-World 1.0: A General-Purpose Interactive World Model](https://huggingface.co/papers/2606.16993)**

*DreamX Team, Yancheng Bai, Rui Chen et al. (23 authors)*

🏢 AMAP-ML

DreamX-World 1.0 is a interactive text/image-to-video model that generates long-horizon content with camera control and scene persistence using specialized encoding, training techniques, and optimization methods.

▲ 94 • 💬 7 • ⭐ 372 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2606.16993) • [💻 code](https://github.com/AMAP-ML/DreamX-World) • [🔗 project](https://amap-ml.github.io/DreamX_World/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 72.9k • 🔱 9.3k • 8h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 30.6k • 🔱 1.4k • 16h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 9.6k • 🔱 860 • 3h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 4.4k • 🔱 387 • 2h ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.5k • 🔱 356 • 6h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 3.4k • 🔱 380 • 2m ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.2k • 🔱 392 • 8h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.1k • 🔱 191 • 9h ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.6k • 🔱 142 • 1d ago

---

**[study8677/awesome-architecture](https://github.com/study8677/awesome-architecture)**

🧭 Architecture-first system design: 26 bilingual tutorials, 25 architecture templates, and 6 end-to-end cases covering distributed systems, AI-native systems, RAG, coding Agents, and production trade-offs.

`Vue` `ai-agents` `ai-coding` `ai-native` `architecture-decision-records` `architecture-patterns`

⭐ 1.4k • 🔱 154 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
