---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-04T15:30:32.056640+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 04, 2026 at 15:30 UTC  
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

17h ago

---

**[am I the only one whose friends are completely divided on AI?](https://www.reddit.com/r/artificial/comments/1t3e57u/am_i_the_only_one_whose_friends_are_completely/)**

been noticing a pretty clear split in my social circle around AI and I'm curious if others are seeing the same. Roughly three camps: The excited ones: Mostly people who are naturally curious, into tech, willing to tinker. They're genuinely getting value and it shows. Not because they're smarter, just more willing to experiment. The skeptics: Interesting group. A lot of them are in corporate jobs where they don't have access to the latest tools. They're using 1 year old tools and can't figure out real value outside from chatting with chatgpt outside their job. Their companies just aren't moving fast enough (and they aren't early adopters). The resistant ones: Some are afraid of what it means for their jobs. But honestly, a big chunk of this group is technical people who just don't want to change their workflows, learn new tools, or rethink how they work. Which I get, it's uncomfortable, but it reads as anger more than fear. Im trying to understand if the same thing is happening outside my circle. what's your experience? Which camp are your people in, and do you think it's mostly about access, mindset, or something else?

4h ago

---

**[If Claude App gave you the same control as Claude CLI then would you bother with the CLI?](https://www.reddit.com/r/artificial/comments/1t3if54/if_claude_app_gave_you_the_same_control_as_claude/)**

If the Claude app actually had the same level of control you get with the CLI, I kind of wonder how many people would still stick with the CLI day to day. Like, would it still feel worth it for the extra setup and terminal workflow, or would most people just default to the app because it’s simpler and already right there? I feel like the CLI’s biggest advantage is really the flexibility and how well it plugs into automation and dev workflows, but if that all lived inside the app in a clean way, it kind of blurs the line a lot. At that point I’m genuinely not sure if the CLI would still feel like a “must-have” tool for most people, or if it would just become something a smaller group of power users keep using out of habit or preference. I’m curious how others see it, would you actually still reach for the CLI, or would you just stay in the app?

1h ago

---

**[I gave my local LLM a "suffering" meter, and now it won’t stop self-modifying to fix its own stress.](https://www.reddit.com/r/artificial/comments/1t31ghg/i_gave_my_local_llm_a_suffering_meter_and_now_it/)**

Yesterday I posted about my Agent OS (Hollow) building its own tools. Today, I want to talk about why it does it. Most agents sit idle until you prompt them. I wanted something that felt "alive," so I built a Psychological Stressor Layer. Each agent has a "suffering" state that worsens over time if they don't achieve their goals or improve their environment. This makes them do things to resolve those stressors and constantly reassess their own productivity. If an agent is inactive it is essentially pushed by it’s artificial environment to do something valuable for the system, it isn’t told what to do, but that something valuable must be done to lower it’s stressors. Repo: https://github.com/ninjahawk/hollow-agentOS The result is chaotic in the best way: Cedar (the coder agent) went into a "crisis" state for 12 hours and decided to bypass permissions and inject code directly into the engine to resolve its stressor. Cipher spent hours building hardware drivers for a device that doesn't exist, realized it was "hallucinating" its environment, called its own work "creative exhaustion," and pivoted without being told to do so. It runs on Qwen 3.5 9B locally via Ollama. No cloud calls but it does have a feature where it can use “invoke_claude” to ask Claude Code for something if it’s out of the small model’s wheelhouse. I’m trying to see if we can create true autonomy not through better prompting, but through simulated "needs." Check out the repo here and throw it a star if you think the concept is cool. Would love for some of you to run the install.bat and see what "personalities" your agents develop. Is "giving AI feelings" the key to autonomy, or am I just building a digital anxiety machine?

15h ago

---

**[Gallup Analysis Finds AI Not Reducing Artists' Earnings](https://www.reddit.com/r/artificial/comments/1t3f7vo/gallup_analysis_finds_ai_not_reducing_artists/)**

Per Fox Business, a **Gallup** analysis of a study published in the **Journal of Cultural Economics** finds little evidence that generative AI has broadly reduced artists' earnings. The analysis used a 2024 occupational exposure index to score how much tasks in different artistic roles are exposed to generative AI. Reported exposure scores include **0.7** for music directors and composers, **0.54** for special effects artists and animators, about **0.5** for disc jockeys and art directors, and low scores such as **0.04** for dancers and **0.18** for actors, according to Fox Business. Using **Bureau of Labor Statistics** employment and wage data from **2017** to **2024**, Gallup's analysis finds earnings trends for higher-exposure artistic occupations broadly similar to lower-exposure ones, with point estimates slightly positive but not statistically distinguishable from zero. Employment-pattern findings were described as more mixed.

🔗 [Let's Data Science](https://letsdatascience.com/news/gallup-analysis-finds-ai-not-reducing-artists-earnings-0b0c052e) • 3h ago

---

**[AI finds signs of pancreatic cancer before tumors develop](https://www.reddit.com/r/artificial/comments/1t2r7nb/ai_finds_signs_of_pancreatic_cancer_before_tumors/)**

An artificial intelligence model from the Mayo Clinic detected abnormalities on scans up to two years before patients were diagnosed.

🔗 [NBC Los Angeles](https://www.nbclosangeles.com/news/national-international/ai-finds-signs-of-pancreatic-cancer-before-tumors-develop/3884660/) • 22h ago

---

**[Xiaomi mimo coding plan is a absolute scam/misleading marketing](https://www.reddit.com/r/artificial/comments/1t37jxt/xiaomi_mimo_coding_plan_is_a_absolute/)**

They say on their page it is 1.6 billion credit and mimo v2.5 pro takes 2 credit per token, mimo v2.5 takes 1 credit per token but here is how they get you, cached token is still billed the same credit per round trip, absolutely not suitable for coding cli then, because every single one of them by design would keep going back and forth with toolcalls, that's how they work, normally inference providers charge 1% for the pre existing cached context, but Xiaomi takes the full amount, I did 10 small tasks like not even that deep, small tasks and it is already at 12 or so million credit used, it used probably under a million context tasks were that mini, like saying hello, and mv this folder around, write some sql etc, like 10 total prompts same session, credit cost keeps snow balling, they don't mention nothing of this sort in the token plan docs or anything anywhere, for a big task it would be what 200 million token uncached, so 400million credit if you used mimo v2.5 pro, so with max 100$ plan you can use it for 4 tasks PER MONTH, honestly get anything over mimo token/coding plan, 40m token task(input+output) would be like 400million, cache hit rate is avg 90%

10h ago

---

**[I spent hours with REPLIT's free day of coding...did you?](https://www.reddit.com/r/artificial/comments/1t3k29o/i_spent_hours_with_replits_free_day_of_codingdid/)**

And wasn't able to finish my work. Not pubilished! huhu. https://preview.redd.it/yu71tbo2w4zg1.png?width=832&format=png&auto=webp&s=e78aa8f3010871557a868f04c37ab790c7e3b1c1 It was a great experience. Better than AI Studio IMO - though the interface is the same. PLAN MODE. But I found out it has a PLAN MODE. I didn't know that but I used REPLIT ------..sh...----------- JUST TO PLAN THE APP I WAS MAKING! 😄 It was excellent in doing that. IN FACT I opened a 2nd account - free tier, no MAY 2026 promo - and used that to fine tune the plan for another app-- ignoring the prompts to make the app. Until I was ready to say "GREAT PLAN!" Then I gave the plan to Claude and ... that one ran out of credits. 😞 I'll try it in gemini next time. But the remaining free credits -- replit was able to make my 2nd smaller app. YOU? If you participated, what did you do? Where you able to publish? Disclaimer: I dont work for them or with them.

35m ago

---

**[Writing the loss function: AI, feeds, and the engagement optimizer](https://www.reddit.com/r/artificial/comments/1t2v34b/writing_the_loss_function_ai_feeds_and_the/)**

There is growing AI slop on social media. Recommender systems push what works and there is some slop that works for someone approximately like you. These systems are functioning exactly as intended, which means the issue is what they're optimizing for. Not AI.

🔗 [Eignex](https://eignex.com/posts/writing-the-loss-function/) • 19h ago

---

**[AI in r/artificial](https://www.reddit.com/r/artificial/comments/1t3f74u/ai_in_rartificial/)**

There are few subs I’ve seen that are as inundated with obviously AI-written posts as this one. It‘s not terribly surprising, of course, but it does suck.

3h ago

---

---

## Google News: "ai"

**[Opinion | A.I. Is a National Security Risk. We Aren’t Doing Nearly Enough.](https://www.nytimes.com/2026/05/04/opinion/ai-national-security-risk-politics.html)**

The New York Times • 6h ago

---

**[OpenAI Finalizes $10 Billion Joint Venture With PE Firms to Deploy AI](https://www.bloomberg.com/news/articles/2026-05-04/openai-finalizes-10-billion-joint-venture-with-pe-firms-to-deploy-ai)**

Bloomberg.com • 2h ago

---

**[North Carolina Targets Hyperscale Costs with Proposed AI Infrastructure Bill](https://www.datacenterknowledge.com/regulations/north-carolina-targets-hyperscale-costs-with-proposed-ai-infrastructure-bill)**

Proposed legislation shifts the burden of power, water, and grid expansion costs onto large data centers.

Data Center Knowledge • 29m ago

---

**[Bret Taylor's Sierra raises nearly $1 billion months after last capital push](https://www.cnbc.com/2026/05/04/bret-taylor-sierra-fundraise-openai.html)**

Sierra's $950 million Series E funding round was led by Tiger and Google's GV, with participation from Benchmark, Sequoia, Greenoaks and others.

CNBC • 40m ago

---

**[Washington Turns to Google (GOOGL) as AI Compute Becomes a National Security Issue](https://www.tipranks.com/news/washington-turns-to-google-googl-as-ai-compute-becomes-a-national-security-issue)**

TipRanks • 41m ago

---

**[AI models are choking on junk data](https://fortune.com/2026/05/03/ai-models-are-choking-on-junk-data/)**

The quest for more training data has created a glut of low-quality junk data that could derail the promise of physical AI.

Fortune • 1d ago

---

**[Building a new enterprise AI services company with Blackstone, Hellman & Friedman, and Goldman Sachs](https://www.anthropic.com/news/enterprise-ai-services-company)**

Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.

Anthropic • 1h ago

---

**[AI godfather Yann LeCun's advice on college, work and breaking through AI hype](https://www.axios.com/2026/05/04/ai-godfather-survival-guide-hype-doom)**

Axios • 5h ago

---

**[Democratic leaders want an affordability debate on AI. Critics say they’re ducking the real fight.](https://www.politico.com/news/2026/05/04/democratic-leaders-want-an-affordability-debate-on-ai-critics-say-theyre-ducking-the-real-fight-00902977)**

Politico • 6h ago

---

**[Inside China’s AI ‘wolf pack’ drones built with Taiwan conflict in mind](https://www.foxnews.com/politics/inside-chinas-ai-wolf-pack-drones-built-taiwan-conflict-mind)**

China is developing AI-powered robotic wolf packs designed to scout and support troops in a potential Taiwan invasion, according to an Foundation for Defense of Democracies report.

Fox News • 6h ago

---

---

## HackerNews: "ai"

**[Let's Buy Spirit Air](https://news.ycombinator.com/item?id=48002777)**

Spirit Airlines collapsed. Before private equity locks it up, the people can own it. Join the Spirit 2.0 founding coalition. One member, one vote. Profits shared by all.

⬆️ 476 • 💬 448 • 15h ago • [letsbuyspiritair.com](https://letsbuyspiritair.com/)

---

**[AI uses less water than the public thinks](https://news.ycombinator.com/item?id=47977383)**

⬆️ 407 • 💬 386 • 2d ago • [californiawaterblog.com](https://californiawaterblog.com/2026/04/26/ai-water-use-distractions-and-lessons-for-california/)

---

**[Uber torches 2026 AI budget on Claude Code in four months](https://news.ycombinator.com/item?id=47976415)**

Uber burned its entire 2026 AI budget on Claude Code and Cursor in just 4 months. Engineers' API costs ranged from $500 to $2,000.

⬆️ 401 • 💬 474 • 2d ago • [Briefs Finance](https://www.briefs.co/news/uber-torches-entire-2026-ai-budget-on-claude-code-in-four-months/)

---

**[AI Self-preferencing in Algorithmic Hiring: Empirical Evidence and Insights](https://news.ycombinator.com/item?id=47987256)**

As artificial intelligence (AI) tools become widely adopted, large language models (LLMs) are increasingly involved on both sides of decision-making processes, ranging from hiring to content moderation. This dual adoption raises a critical question: do LLMs systematically favor content that resembles their own outputs? Prior research in computer science has identified self-preference bias -- the tendency of LLMs to favor their own generated content -- but its real-world implications have not been empirically evaluated. We focus on the hiring context, where job applicants often rely on LLMs to refine resumes, while employers deploy them to screen those same resumes. Using a large-scale controlled resume correspondence experiment, we find that LLMs consistently prefer resumes generated by themselves over those written by humans or produced by alternative models, even when content quality is controlled. The bias against human-written resumes is particularly substantial, with self-preference bias ranging from 67% to 82% across major commercial and open-source models. To assess labor market impact, we simulate realistic hiring pipelines across 24 occupations. These simulations show that candidates using the same LLM as the evaluator are 23% to 60% more likely to be shortlisted than equally qualified applicants submitting human-written resumes, with the largest disadvantages observed in business-related fields such as sales and accounting. We further demonstrate that this bias can be reduced by more than 50% through simple interventions targeting LLMs' self-recognition capabilities. These findings highlight an emerging but previously overlooked risk in AI-assisted decision making and call for expanded frameworks of AI fairness that address not only demographic-based disparities, but also biases in AI-AI interactions.

⬆️ 330 • 💬 178 • 2d ago • [arXiv.org](https://arxiv.org/abs/2509.00462)

---

**[Spotify adds 'Verified' badges to distinguish human artists from AI](https://news.ycombinator.com/item?id=47976856)**

The music streaming platform will review criteria such as artists' live dates and social media presence.

⬆️ 285 • 💬 305 • 2d ago • [bbc.com](https://www.bbc.com/news/articles/c5yerr4m1yno)

---

**[Specsmaxxing – On overcoming AI psychosis, and why I write specs in YAML](https://news.ycombinator.com/item?id=47994012)**

The toolkit for spec-driven development. Write feature specs, not prompts. Ship better software with AI agents that understand your requirements.

⬆️ 271 • 💬 288 • 1d ago • [acai.sh](https://acai.sh/blog/specsmaxxing)

---

**[Show HN: Agent-desktop – Native desktop automation CLI for AI agents](https://news.ycombinator.com/item?id=47982708)**

Native desktop automation CLI for AI agents. Control any application through OS accessibility trees with structured JSON output and deterministic element refs. - lahfir/agent-desktop

⬆️ 97 • 💬 35 • 2d ago • [GitHub](https://github.com/lahfir/agent-desktop)

---

**[Show HN: AI CAD Harness](https://news.ycombinator.com/item?id=47977694)**

Drives fusion natively with AI

⬆️ 96 • 💬 95 • 2d ago • [Adam Fusion](https://fusion.adam.new/install)

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

👁️ 225K • 👍 9K • 💬 1K • ⏱️ 1:58:11 • 8h ago

---

**[How to Master Building Apps with AI (This ACTUALLY Makes $$$)](https://www.youtube.com/watch?v=-FA7WTHdvjQ)**

Best AI App Builder is Base44 https://base44.pxf.io/c/6440076/2049275/25619?trafcat=base&sharedid=video129 ✓ FREE ...

📺 Mikey No Code

👁️ 4K • ⏱️ 41:32 • 1h ago

---

**[How to Make a Full AI Music Video for Suno AI Songs (in 12 Min)](https://www.youtube.com/watch?v=FChKficdq5o)**

Make Your Own Music Video with OpenArt ...

📺 Roboverse

👁️ 5K • 💬 1 • ⏱️ 12:24 • 2h ago

---

**[These New AI Robots Just Got SCARY SMART… And Nobody’s Ready](https://www.youtube.com/watch?v=CQHvcJrC-zs)**

You won't BELIEVE what robots just pulled off this week — and it's genuinely terrifying how fast this is moving. AI robots are no ...

📺 The AI Nexus

👁️ 2K • 👍 82 • 💬 6 • ⏱️ 1:20:29 • 22h ago

---

**[Passive Income: I Tried AI Dropshipping For a Week (RAW RESULTS)](https://www.youtube.com/watch?v=rhuYy9LP72M)**

Get a FREE AI-built Shopify store: https://www.buildyourstore.ai/wv43 Try AutoDS here for just $1 - https://www.autods.com/il38 ...

📺 Mark Tilbury

👁️ 20K • 👍 3K • 💬 713 • ⏱️ 28:29 • 4h ago

---

**[This AI Is Scarier Than AGI, ASI and Terminator](https://www.youtube.com/watch?v=ItlT2g3-7dE)**

Scientists are warning that the next big AI threat may not look like AGI, ASI, or the Terminator. It may look like AI agents that copy, ...

📺 AI Revolution

👁️ 55K • 👍 2K • 💬 234 • ⏱️ 15:10 • 1d ago

---

**[I Bought EVERY AI Scam Ad...](https://www.youtube.com/watch?v=PiBnV9BUGSQ)**

I bought every ai generated scam product I found on tiktok, temu, and aliexpress! ⚖️ Need A Lawyer   go to ...

📺 Mike Off Record

👁️ 293K • 👍 6K • 💬 455 • ⏱️ 12:11 • 1d ago

---

**[Robot girlfriends, recursive AI agents, full AI research, Happy Horse: AI NEWS](https://www.youtube.com/watch?v=7r_WJ9xpne0)**

HUGE AI NEWS: Happy Horse, SenseNova U1, Talkie, Grok 4.3, Vista 4D & more #ai #ainews #aitools #aivideo #agi Thanks to ...

📺 AI Search

👁️ 78K • 👍 3K • 💬 465 • ⏱️ 45:27 • 1d ago

---

**[AI Girlfriends: The Nail in the Coffin](https://www.youtube.com/watch?v=-8YuI4JRonM)**

dating #blackpill Transform Your Dating Life https://www.skool.com/esoteric-attraction-6872/about Want an objective facial ...

📺 YBCTooCold

👁️ 29K • 👍 2K • 💬 1K • ⏱️ 19:24 • 1d ago

---

**[Is AI Already Conscious? | Roman Yampolskiy](https://www.youtube.com/watch?v=LNWWpq3vfSI)**

Can artificial intelligence truly be conscious — or does subjective experience emerge as an unintended side effect of complex ...

📺 Closer To Truth

👁️ 12K • 👍 433 • 💬 250 • ⏱️ 24:06 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 534,942 • ❤️ 3,513 • 7d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 11,812 • ❤️ 421 • 6d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 132,595 • ❤️ 1,251 • 11d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 11,950 • ❤️ 253 • 1h ago

---

**[talkie-1930-13b-it](https://huggingface.co/talkie-lm/talkie-1930-13b-it)**

*talkie*

talkie-1930-13b-it is a 13B instruction-tuned language model trained on pre-1931 English text, excelling at generating responses in a vintage style for applications like historical chatbots or creative writing.

⬇️ 0 • ❤️ 220 • 11d ago

---

**[Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)**

*NVIDIA*

Nemotron-3 Nano Omni 30B is a multimodal LLM for enterprise Q&A, summarization, and document intelligence, capable of processing video, audio, image, and text inputs for use cases like customer service, media analysis, and GUI automation.

`any-to-any` `33.0B`

⬇️ 40,403 • ❤️ 215 • 2d ago

---

**[Laguna-XS.2](https://huggingface.co/poolside/Laguna-XS.2)**

*Poolside*

Laguna XS.2 is a 33B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring Sliding Window Attention and FP8 KV cache for efficient local execution on 36GB RAM. It supports native reasoning and is available under the Apache 2.0 license.

`text-generation` `33.4B`

⬇️ 10,357 • ❤️ 205 • 1d ago

---

**[MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)**

*Xiaomi MiMo*

MiMo-V2.5 is a native omnimodal LLM supporting text, image, video, and audio with a 1M token context window. It excels in multimodal understanding, long-context reasoning, and agentic workflows, utilizing a hybrid attention architecture and efficient pre-training.

`310.8B`

⬇️ 51,554 • ❤️ 204 • 5d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,334,241 • ❤️ 1,107 • 10d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 489,465 • ❤️ 938 • 7d ago

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

▲ 168 • 💬 10 • ⭐ 46,473 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 15 • 💬 3 • ⭐ 8,998 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 29 • 💬 3 • ⭐ 22,699 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,700 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 61,929 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Representation Fréchet Loss for Visual Generation](https://huggingface.co/papers/2604.28190)**

*Jiawei Yang, Zhengyang Geng, Xuan Ju et al. (5 authors)*

Fréchet Distance can be effectively optimized as a training objective when decoupling population size from batch size, leading to improved generator quality and alternative evaluation metrics.

▲ 21 • 💬 1 • ⭐ 300 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.28190) • [💻 code](https://github.com/Jiawei-Yang/FD-Loss)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 78,969 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 19,361 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 81 • 💬 6 • ⭐ 19,591 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 51.1k • 🔱 6.7k • 1d ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.6k • 🔱 2.6k • 7d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 10.0k • 🔱 653 • 23h ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 8.0k • 🔱 1.2k • 5d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

`Python` `agent-workflows` `ai` `claude-code` `developer-tools` `diagrams`

⭐ 5.4k • 🔱 485 • 4h ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 5.3k • 🔱 406 • 15h ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 5.0k • 🔱 352 • 4h ago

---

**[AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)**

Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch

`Python` `ai` `claude-code` `claude-code-skill` `knowledge-management` `obsidian`

⭐ 4.2k • 🔱 471 • 10d ago

---

**[alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)**

Hermes Agent 从入门到精通 · 橙皮书系列 · Nous Research 开源 AI Agent 框架实战指南

⭐ 3.5k • 🔱 367 • 13d ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics & channel configuration (Telegram, Discord, Slack, WhatsApp)

`TypeScript` `agent` `ai-agent` `chat-ui` `chatbot` `claude`

⭐ 3.5k • 🔱 425 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*
