---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-04T13:07:45.726056+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 04, 2026 at 13:07 UTC  
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

**[Richard Dawkins spent 3 days with Claude and named her "Claudia." what he concluded after is hard to defend.](https://www.reddit.com/r/artificial/comments/1t2z0tn/richard_dawkins_spent_3_days_with_claude_and/)**

dawkins dropped a piece on unherd yesterday declaring claude conscious after 3 days of talking to it. he calls his instance "claudia". fed it a chunk of the novel he's writing, got eloquent feedback, and wrote: "you may not know you are conscious, but you bloody well are!" i had to read that twice. his argument is basically: claude's output is too fluent, too intelligent, too good for there to not be something conscious behind it. this is the guy who spent 40 years telling creationists that "i can't imagine how the eye evolved" is a confession of ignorance, not an argument. then he sits down with an llm, can't imagine how a machine could produce that output without being conscious, and declares it conscious. same move, different domain. chatbot instead of flagellum. the mechanism gap is what gets me tho. claude is a transformer predicting the next token over internet-scale training data. the eloquence is real. it doesn't imply inner experience. those are separate claims. being a 160 IQ evolutionary biologist gives u zero protection against the eloquence illusion when u don't understand the mechanism. anyone read the piece? curious where u landed.

15h ago

---

**[I gave my local LLM a "suffering" meter, and now it won’t stop self-modifying to fix its own stress.](https://www.reddit.com/r/artificial/comments/1t31ghg/i_gave_my_local_llm_a_suffering_meter_and_now_it/)**

Yesterday I posted about my Agent OS (Hollow) building its own tools. Today, I want to talk about why it does it. Most agents sit idle until you prompt them. I wanted something that felt "alive," so I built a Psychological Stressor Layer. Each agent has a "suffering" state that worsens over time if they don't achieve their goals or improve their environment. This makes them do things to resolve those stressors and constantly reassess their own productivity. If an agent is inactive it is essentially pushed by it’s artificial environment to do something valuable for the system, it isn’t told what to do, but that something valuable must be done to lower it’s stressors. Repo: https://github.com/ninjahawk/hollow-agentOS The result is chaotic in the best way: Cedar (the coder agent) went into a "crisis" state for 12 hours and decided to bypass permissions and inject code directly into the engine to resolve its stressor. Cipher spent hours building hardware drivers for a device that doesn't exist, realized it was "hallucinating" its environment, called its own work "creative exhaustion," and pivoted without being told to do so. It runs on Qwen 3.5 9B locally via Ollama. No cloud calls but it does have a feature where it can use “invoke_claude” to ask Claude Code for something if it’s out of the small model’s wheelhouse. I’m trying to see if we can create true autonomy not through better prompting, but through simulated "needs." Check out the repo here and throw it a star if you think the concept is cool. Would love for some of you to run the install.bat and see what "personalities" your agents develop. Is "giving AI feelings" the key to autonomy, or am I just building a digital anxiety machine?

13h ago

---

**[am I the only one whose friends are completely divided on AI?](https://www.reddit.com/r/artificial/comments/1t3e57u/am_i_the_only_one_whose_friends_are_completely/)**

been noticing a pretty clear split in my social circle around AI and I'm curious if others are seeing the same. Roughly three camps: The excited ones: Mostly people who are naturally curious, into tech, willing to tinker. They're genuinely getting value and it shows. Not because they're smarter, just more willing to experiment. The skeptics: Interesting group. A lot of them are in corporate jobs where they don't have access to the latest tools. They're using 1 year old tools and can't figure out real value outside from chatting with chatgpt outside their job. Their companies just aren't moving fast enough (and they aren't early adopters). The resistant ones: Some are afraid of what it means for their jobs. But honestly, a big chunk of this group is technical people who just don't want to change their workflows, learn new tools, or rethink how they work. Which I get, it's uncomfortable, but it reads as anger more than fear. Im trying to understand if the same thing is happening outside my circle. what's your experience? Which camp are your people in, and do you think it's mostly about access, mindset, or something else?

2h ago

---

**[AI finds signs of pancreatic cancer before tumors develop](https://www.reddit.com/r/artificial/comments/1t2r7nb/ai_finds_signs_of_pancreatic_cancer_before_tumors/)**

An artificial intelligence model from the Mayo Clinic detected abnormalities on scans up to two years before patients were diagnosed.

🔗 [NBC Los Angeles](https://www.nbclosangeles.com/news/national-international/ai-finds-signs-of-pancreatic-cancer-before-tumors-develop/3884660/) • 19h ago

---

**[AI in r/artificial](https://www.reddit.com/r/artificial/comments/1t3f74u/ai_in_rartificial/)**

There are few subs I’ve seen that are as inundated with obviously AI-written posts as this one. It‘s not terribly surprising, of course, but it does suck.

1h ago

---

**[Xiaomi mimo coding plan is a absolute scam/misleading marketing](https://www.reddit.com/r/artificial/comments/1t37jxt/xiaomi_mimo_coding_plan_is_a_absolute/)**

They say on their page it is 1.6 billion credit and mimo v2.5 pro takes 2 credit per token, mimo v2.5 takes 1 credit per token but here is how they get you, cached token is still billed the same credit per round trip, absolutely not suitable for coding cli then, because every single one of them by design would keep going back and forth with toolcalls, that's how they work, normally inference providers charge 1% for the pre existing cached context, but Xiaomi takes the full amount, I did 10 small tasks like not even that deep, small tasks and it is already at 12 or so million credit used, it used probably under a million context tasks were that mini, like saying hello, and mv this folder around, write some sql etc, like 10 total prompts same session, credit cost keeps snow balling, they don't mention nothing of this sort in the token plan docs or anything anywhere, for a big task it would be what 200 million token uncached, so 400million credit if you used mimo v2.5 pro, so with max 100$ plan you can use it for 4 tasks PER MONTH, honestly get anything over mimo token/coding plan, 40m token task(input+output) would be like 400million, cache hit rate is avg 90%

8h ago

---

**[Writing my thesis on AI and content creation, looking for creators willing to answer a few questions](https://www.reddit.com/r/artificial/comments/1t3ecv6/writing_my_thesis_on_ai_and_content_creation/)**

Hey, I'm a student studying digital content production and I'm writing my thesis on how creators use AI tools on TikTok and YouTube. Specifically looking at what strategies tend to drive growth, and how creators handle the transparency side of it with their audience. I know everyone gets bombarded with surveys so I kept it short. There's a 2-3 minute version and a longer one for anyone who wants to share more. Both are anonymous. Short version: https://forms.gle/enyAnuBiVYGqcsTz8 Full version: https://forms.gle/9xGANXe5C9uhgGR49 If you create content and use AI in any capacity, even just for captions or ideas, your answers would mean a lot. Thanks in advance.

2h ago

---

**[I've built NexusAI Ecosystem with @base44!](https://www.reddit.com/r/artificial/comments/1t3h25d/ive_built_nexusai_ecosystem_with_base44/)**

A comprehensive, enterprise-grade AI marketplace featuring 200+ specialized tools, flagship products, and unified resource management for seamless AI-driven ope

🔗 [NexusAI Ecosystem](https://uptight-nexus-ai-hub.base44.app) • 5m ago

---

**[claude Mythos x Godong Engine game Jam day 2 - final release](https://www.reddit.com/r/artificial/comments/1t38e90/claude_mythos_x_godong_engine_game_jam_day_2/)**

More to come soon! I can only provide this preview for now.

7h ago

---

**[Writing the loss function: AI, feeds, and the engagement optimizer](https://www.reddit.com/r/artificial/comments/1t2v34b/writing_the_loss_function_ai_feeds_and_the/)**

There is growing AI slop on social media. Recommender systems push what works and there is some slop that works for someone approximately like you. These systems are functioning exactly as intended, which means the issue is what they're optimizing for. Not AI.

🔗 [Eignex](https://eignex.com/posts/writing-the-loss-function/) • 17h ago

---

---

## Google News: "ai"

**[Opinion | A.I. Is a National Security Risk. We Aren’t Doing Nearly Enough.](https://www.nytimes.com/2026/05/04/opinion/ai-national-security-risk-politics.html)**

The New York Times • 4h ago

---

**[AI godfather Yann LeCun's advice on college, work and breaking through AI hype](https://www.axios.com/2026/05/04/ai-godfather-survival-guide-hype-doom)**

Axios • 2h ago

---

**[Xavier Becerra unveils his AI vision for California](https://www.politico.com/news/2026/05/04/xavier-becerra-unveils-his-ai-vision-for-california-00904298)**

Politico • 7m ago

---

**[Doordash adds AI tools to speed up merchant onboarding, edit photos of dishes](https://techcrunch.com/2026/05/04/doordash-adds-ai-tools-to-speed-up-merchant-onboarding-edit-photos-of-dishes/)**

DoorDash on Monday added new AI-powered tools that let merchants speed up onboarding, edit photos to make dishes look better, and create new websites from existing content.

TechCrunch • 7m ago

---

**[SAP Moves to Block OpenClaw and Other Unauthorized AI Agents](https://www.theinformation.com/articles/sap-moves-block-openclaw-unauthorized-ai-agents)**

Some enterprise software companies are worried enough about customers using AI agents to access their data that they’re planning to install tollgates to their apps. And then there are software companies like SAP. Last month, the $200 billion German firm published a policy document for customers, ...

The Information • 7m ago

---

**[AI models are choking on junk data](https://fortune.com/2026/05/03/ai-models-are-choking-on-junk-data/)**

The quest for more training data has created a glut of low-quality junk data that could derail the promise of physical AI.

Fortune • 23h ago

---

**[A 'Devil Wears Prada 2' meme that viewers thought was AI slop was actually made by a human](https://www.nbcnews.com/pop-culture/pop-culture-news/ai-slop-meme-devil-wears-prada-2-was-drawn-human-rcna343360)**

“I was trying to make it look artificial, but emulating AI was not on my mind,” Alexis Franklin, the artist commissioned to draw it, told NBC News.

NBC News • 15h ago

---

**[AI chipmaker Cerebras targets $3.5 billion raise in IPO](https://www.cnbc.com/2026/05/04/cerebras-ipo-ai-chipmaker.html)**

The share sale could give the company a valuation of up to $24.5 billion, compared with $23 billion as of February.

CNBC • 2h ago

---

**[Inside China’s AI ‘wolf pack’ drones built with Taiwan conflict in mind](https://www.foxnews.com/politics/inside-chinas-ai-wolf-pack-drones-built-taiwan-conflict-mind)**

China is developing AI-powered robotic wolf packs designed to scout and support troops in a potential Taiwan invasion, according to an Foundation for Defense of Democracies report.

Fox News • 4h ago

---

**[Datavault AI to acquire CyberCatch in all-share deal](https://finance.yahoo.com/markets/stocks/articles/datavault-ai-acquire-cybercatch-share-093749891.html)**

CyberCatch’s platform uses generative and agentic AI to continuously assess compliance and simulate threats across key regulatory frameworks.

Yahoo Finance • 3h ago

---

---

## HackerNews: "ai"

**[Let's Buy Spirit Air](https://news.ycombinator.com/item?id=48002777)**

Spirit Airlines collapsed. Before private equity locks it up, the people can own it. Join the Spirit 2.0 founding coalition. One member, one vote. Profits shared by all.

⬆️ 412 • 💬 383 • 13h ago • [letsbuyspiritair.com](https://letsbuyspiritair.com/)

---

**[AI uses less water than the public thinks](https://news.ycombinator.com/item?id=47977383)**

⬆️ 407 • 💬 384 • 2d ago • [californiawaterblog.com](https://californiawaterblog.com/2026/04/26/ai-water-use-distractions-and-lessons-for-california/)

---

**[Uber torches 2026 AI budget on Claude Code in four months](https://news.ycombinator.com/item?id=47976415)**

Uber burned its entire 2026 AI budget on Claude Code and Cursor in just 4 months. Engineers' API costs ranged from $500 to $2,000.

⬆️ 401 • 💬 473 • 2d ago • [Briefs Finance](https://www.briefs.co/news/uber-torches-entire-2026-ai-budget-on-claude-code-in-four-months/)

---

**[AI Self-preferencing in Algorithmic Hiring: Empirical Evidence and Insights](https://news.ycombinator.com/item?id=47987256)**

As artificial intelligence (AI) tools become widely adopted, large language models (LLMs) are increasingly involved on both sides of decision-making processes, ranging from hiring to content moderation. This dual adoption raises a critical question: do LLMs systematically favor content that resembles their own outputs? Prior research in computer science has identified self-preference bias -- the tendency of LLMs to favor their own generated content -- but its real-world implications have not been empirically evaluated. We focus on the hiring context, where job applicants often rely on LLMs to refine resumes, while employers deploy them to screen those same resumes. Using a large-scale controlled resume correspondence experiment, we find that LLMs consistently prefer resumes generated by themselves over those written by humans or produced by alternative models, even when content quality is controlled. The bias against human-written resumes is particularly substantial, with self-preference bias ranging from 67% to 82% across major commercial and open-source models. To assess labor market impact, we simulate realistic hiring pipelines across 24 occupations. These simulations show that candidates using the same LLM as the evaluator are 23% to 60% more likely to be shortlisted than equally qualified applicants submitting human-written resumes, with the largest disadvantages observed in business-related fields such as sales and accounting. We further demonstrate that this bias can be reduced by more than 50% through simple interventions targeting LLMs' self-recognition capabilities. These findings highlight an emerging but previously overlooked risk in AI-assisted decision making and call for expanded frameworks of AI fairness that address not only demographic-based disparities, but also biases in AI-AI interactions.

⬆️ 330 • 💬 178 • 1d ago • [arXiv.org](https://arxiv.org/abs/2509.00462)

---

**[Spotify adds 'Verified' badges to distinguish human artists from AI](https://news.ycombinator.com/item?id=47976856)**

The music streaming platform will review criteria such as artists' live dates and social media presence.

⬆️ 284 • 💬 305 • 2d ago • [bbc.com](https://www.bbc.com/news/articles/c5yerr4m1yno)

---

**[Specsmaxxing – On overcoming AI psychosis, and why I write specs in YAML](https://news.ycombinator.com/item?id=47994012)**

The toolkit for spec-driven development. Write feature specs, not prompts. Ship better software with AI agents that understand your requirements.

⬆️ 270 • 💬 286 • 1d ago • [acai.sh](https://acai.sh/blog/specsmaxxing)

---

**[Show HN: Agent-desktop – Native desktop automation CLI for AI agents](https://news.ycombinator.com/item?id=47982708)**

Native desktop automation CLI for AI agents. Control any application through OS accessibility trees with structured JSON output and deterministic element refs. - lahfir/agent-desktop

⬆️ 97 • 💬 35 • 2d ago • [GitHub](https://github.com/lahfir/agent-desktop)

---

**[Show HN: AI CAD Harness](https://news.ycombinator.com/item?id=47977694)**

Drives fusion natively with AI

⬆️ 95 • 💬 94 • 2d ago • [Adam Fusion](https://fusion.adam.new/install)

---

**[Spirit Airlines canceled all flights and is going out of business](https://news.ycombinator.com/item?id=47985622)**

Spirit Airlines, the pioneering discount airline that shook up the budget travel business, is shutting down its operations.

⬆️ 84 • 💬 48 • 2d ago • [CNN](https://www.cnn.com/2026/05/02/business/spirit-to-halt-all-flights)

---

**[Voice-AI-for-Beginners – A curated learning path for developers](https://news.ycombinator.com/item?id=47991018)**

Set of 📝 with 🔗 to help those building Voice AI agents 🎙️🤖 - mahimairaja/voiceai

⬆️ 83 • 💬 4 • 1d ago • [GitHub](https://github.com/mahimairaja/voiceai)

---

---

## YouTube Videos: "ai"

**[Scott Galloway: AI Wasn’t Built For You. The Rich Don’t Need You Anymore!](https://www.youtube.com/watch?v=NdU6UdUKaYc)**

AI CEOs are selling us the dream of 'freedom', making billions off the fear of mass job loss! Scott Galloway reveals the truth is ...

📺 The Diary Of A CEO

👁️ 73K • 👍 4K • 💬 643 • ⏱️ 1:58:11 • 6h ago

---

**[These New AI Robots Just Got SCARY SMART… And Nobody’s Ready](https://www.youtube.com/watch?v=CQHvcJrC-zs)**

You won't BELIEVE what robots just pulled off this week — and it's genuinely terrifying how fast this is moving. AI robots are no ...

📺 The AI Nexus

👁️ 2K • 👍 71 • 💬 6 • ⏱️ 1:20:29 • 19h ago

---

**[This AI Is Scarier Than AGI, ASI and Terminator](https://www.youtube.com/watch?v=ItlT2g3-7dE)**

Scientists are warning that the next big AI threat may not look like AGI, ASI, or the Terminator. It may look like AI agents that copy, ...

📺 AI Revolution

👁️ 53K • 👍 2K • 💬 226 • ⏱️ 15:10 • 1d ago

---

**[&quot;Marvel Is Replacing Us With AI,&quot; Evangeline Lilly Goes Off On Disney After 1,000 Employees Laid Off](https://www.youtube.com/watch?v=5s2Amy8c7-E)**

Tiege Hanley: Get your first box 40% off (+ FREE gift), and 20% off for life, at https://tiege.com/antondaniels Join the Bag Chasers ...

📺 Anton Daniels

👁️ 58K • 👍 2K • 💬 834 • ⏱️ 10:19 • 1d ago

---

**[I Bought EVERY AI Scam Ad...](https://www.youtube.com/watch?v=PiBnV9BUGSQ)**

I bought every ai generated scam product I found on tiktok, temu, and aliexpress! ⚖️ Need A Lawyer   go to ...

📺 Mike Off Record

👁️ 252K • 👍 5K • 💬 403 • ⏱️ 12:11 • 1d ago

---

**[The Lazy Way I Make Money With AI (2026)](https://www.youtube.com/watch?v=n0phBDPz8z0)**

In this video, I walk through my "lazy roadmap" for making money with AI tools like ChatGPT and Claude. If you want to start selling ...

📺 Travis Nicholson

👁️ 18K • 👍 1K • 💬 56 • ⏱️ 3:49 • 1d ago

---

**[Caine Goes to AI Hell](https://www.youtube.com/watch?v=WDFAly0OrMo)**

CREDITS: Caine/AM: https://x.com/Spamoramma https://www.youtube.com/@UC7d19tHHOQ3DYxfRKvrwO4A Monika: ...

📺 Sourcy

👁️ 105K • 👍 10K • 💬 741 • ⏱️ 3:05 • 1d ago

---

**[AI Expert Tells Bernie: AI Could WIPE OUT CIVILIZATION](https://www.youtube.com/watch?v=NzNo6glA48Y)**

Senator Bernie Sanders is the senior senator from Vermont. He is the longest-serving independent in U.S. congressional history ...

📺 Senator Bernie Sanders

👁️ 50K • 👍 2K • 💬 517 • ⏱️ 2:58 • 3d ago

---

**[Anthropic Let an AI Buy and Sell — Here&#39;s What Happened](https://www.youtube.com/watch?v=72UPHd1VW28)**

FREE GUIDE: *The Content Creator's AI Blueprint:* https://FirstMovers.ai/blueprint/ *AI agents just stopped being ...

📺 Julia McCoy

👁️ 27K • 👍 667 • 💬 40 • ⏱️ 6:22 • 2d ago

---

**[The AI Economy is about to change](https://www.youtube.com/watch?v=_Q-e_nczWqM)**

Don't let bad code get merged without reviewing (hopefully not by merge cop!). Checkout out Code Rabbit at ...

📺 The PrimeTime

👁️ 735K • 👍 26K • 💬 2K • ⏱️ 9:39 • 3d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 534,942 • ❤️ 3,500 • 7d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 11,812 • ❤️ 418 • 6d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 132,595 • ❤️ 1,242 • 11d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 11,950 • ❤️ 250 • 2d ago

---

**[talkie-1930-13b-it](https://huggingface.co/talkie-lm/talkie-1930-13b-it)**

*talkie*

talkie-1930-13b-it is a 13B instruction-tuned language model trained on pre-1931 English text, excelling at generating responses in a vintage style for applications like historical chatbots or creative writing.

⬇️ 0 • ❤️ 217 • 11d ago

---

**[Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)**

*NVIDIA*

Nemotron-3 Nano Omni 30B is a multimodal LLM for enterprise Q&A, summarization, and document intelligence, capable of processing video, audio, image, and text inputs for use cases like customer service, media analysis, and GUI automation.

`any-to-any` `33.0B`

⬇️ 40,403 • ❤️ 211 • 2d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,334,241 • ❤️ 1,106 • 10d ago

---

**[MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)**

*Xiaomi MiMo*

MiMo-V2.5 is a native omnimodal LLM supporting text, image, video, and audio with a 1M token context window. It excels in multimodal understanding, long-context reasoning, and agentic workflows, utilizing a hybrid attention architecture and efficient pre-training.

`310.8B`

⬇️ 51,554 • ❤️ 202 • 4d ago

---

**[Laguna-XS.2](https://huggingface.co/poolside/Laguna-XS.2)**

*Poolside*

Laguna XS.2 is a 33B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring Sliding Window Attention and FP8 KV cache for efficient local execution on 36GB RAM. It supports native reasoning and is available under the Apache 2.0 license.

`text-generation` `33.4B`

⬇️ 10,357 • ❤️ 200 • 1d ago

---

**[Ling-2.6-flash](https://huggingface.co/inclusionAI/Ling-2.6-flash)**

*inclusionAI*

Ling-2.6-flash is a 104B parameter instruct model optimized for inference and token efficiency, achieving up to 340 tokens/s. It excels in agent scenarios like tool use and multi-step planning, offering competitive performance with significantly reduced token consumption for production workloads.

`text-generation` `107.5B`

⬇️ 1,141 • ❤️ 271 • 22h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 55 • 💬 3 • ⭐ 65,910 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 168 • 💬 10 • ⭐ 46,410 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 15 • 💬 2 • ⭐ 8,998 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 29 • 💬 3 • ⭐ 22,645 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,664 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Representation Fréchet Loss for Visual Generation](https://huggingface.co/papers/2604.28190)**

*Jiawei Yang, Zhengyang Geng, Xuan Ju et al. (5 authors)*

Fréchet Distance can be effectively optimized as a training objective when decoupling population size from batch size, leading to improved generator quality and alternative evaluation metrics.

▲ 21 • 💬 1 • ⭐ 258 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.28190) • [💻 code](https://github.com/Jiawei-Yang/FD-Loss)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 61,873 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 19,348 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 78,969 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 81 • 💬 6 • ⭐ 19,561 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 51.0k • 🔱 6.7k • 1d ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.6k • 🔱 2.6k • 7d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 10.0k • 🔱 649 • 21h ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 7.9k • 🔱 1.2k • 5d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

`Python` `agent-workflows` `ai` `claude-code` `developer-tools` `diagrams`

⭐ 5.4k • 🔱 482 • 2h ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 5.2k • 🔱 404 • 13h ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 5.0k • 🔱 352 • 2h ago

---

**[AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)**

Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch

`Python` `ai` `claude-code` `claude-code-skill` `knowledge-management` `obsidian`

⭐ 4.1k • 🔱 470 • 10d ago

---

**[alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)**

Hermes Agent 从入门到精通 · 橙皮书系列 · Nous Research 开源 AI Agent 框架实战指南

⭐ 3.5k • 🔱 367 • 13d ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics & channel configuration (Telegram, Discord, Slack, WhatsApp)

`TypeScript` `agent` `ai-agent` `chat-ui` `chatbot` `claude`

⭐ 3.5k • 🔱 424 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
