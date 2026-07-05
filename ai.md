---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-05T16:34:23.346654+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 05, 2026 at 16:34 UTC  
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

**[Meta Paid Hundreds of Contractors to Pretend to Be Teenagers While Barraging Its Competitors’ AI With Disturbing Content](https://www.reddit.com/r/artificial/comments/1ungqh7/meta_paid_hundreds_of_contractors_to_pretend_to/)**

"Surely we are going to get in trouble for doing this?"

🔗 [Yahoo News](https://www.yahoo.com/news/us/articles/meta-paid-hundreds-contractors-pretend-130200038.html?.tsrc=daily_mail&segment_id=DY_VTO_50_Supernova&ncid=crm_19908-1475736-20260704-0--A&bt_ee=9gzHBYP4lPFkJ0sQWNTUaDg%2ByNx1IPgLBZidnverDFwSgBJNAY%2FSHqS9MjlzlxEm&bt_ts=1783187096830) • 21h ago

---

**[The Revenge of the Philosophy Majors. A.I. labs are hiring contrarian, chin-stroking, finger-steepling sages. Who’s underemployed now? (Gift Article)](https://www.reddit.com/r/artificial/comments/1uo3f4x/the_revenge_of_the_philosophy_majors_ai_labs_are/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/07/05/business/philosophy-majors-ai-jobs.html?unlocked_article_code=1.vVA.kh0d.yifPMBsgeixB&smid=url-share) • 2h ago

---

**[What should people learn today to stay relevant in an AI-driven future?](https://www.reddit.com/r/artificial/comments/1unzymd/what_should_people_learn_today_to_stay_relevant/)**

With AI advancing so quickly, I'm trying to understand how to prepare for the next 5–10 years. A few questions I'd love to hear your thoughts on: What skills should people focus on learning now to stay relevant alongside AI? Beyond prompting, what are the most valuable AI-related skills (automation, coding, workflows, AI agents, etc.)? Which jobs or industries are likely to benefit the most, and which are at the highest risk? Do you think AI will become expensive to use in the future? Will the best models and capabilities mostly be behind paid subscriptions? If you were starting from scratch today, what would your learning roadmap look like? I'm looking for practical advice from people who actively use AI in their work or projects. Thanks!

4h ago

---

**[What's one AI capability that you think is underrated because everyone is focused on AGI?](https://www.reddit.com/r/artificial/comments/1uo0tv5/whats_one_ai_capability_that_you_think_is/)**

It feels like most AI discussions revolve around AGI timelines or benchmark scores, but there are a lot of smaller capabilities improving rapidly (reasoning, memory, multimodal understanding, coding agents, robotics, speech, etc.) Which capability do you think is currently underrated and why? I'm more interested in practical applications over the next 3–5 years than distant predictions.

4h ago

---

**[Why I built a proactive context curator instead of a compactor — and what I got wrong for three months](https://www.reddit.com/r/artificial/comments/1uo5oty/why_i_built_a_proactive_context_curator_instead/)**

Two ways to handle a context window that's filling up. Reactive: wait until it's full, then compact everything. Proactive: be picky about what gets added every turn so noise never piles up in the first place. Most coding agents take the reactive path. I spent months building the proactive one, and I want to be honest about what actually worked and what didn't. What held up A decision your agent made on turn 3 is worth more tokens than tool output from turn 15 that's already resolved. Treat them the same and you get context rot. PRAANA's compiler splits working memory into active, soft, and hard tiers. It scores context units by information density, then uses BM25 plus semantic similarity (Transformers.js, running in-process) to decide what gets pulled back into the active window. What I got wrong — semantic recall was quietly broken for weeks I threw together a hash-based embedder early on as a placeholder. The problem was it was injecting noise into recall ranking. Memories came back in the wrong order, irrelevant items floated above relevant ones. The worst part: it looked plausible. No errors, just wrong answers. Took three weeks to even notice. I fixed it by switching to Transformers.js with keyword-only full-text search as the fallback. New rule: if there's no real semantic embedder available, you get keyword-only recall. No fake vectors, ever. The measurement gap For most of the project, I couldn't actually prove the context engine beat a plain transcript agent. "Feels better" doesn't count as evidence. A telemetry scorecard landed a few weeks ago — session-level signals like context pressure, memory recall percentage, skill load and decay, per-section token accounting. The A/B evaluation harness is next. Lesson learned: build the measurement before you build the thing you're trying to measure. The honesty problem in agent marketing PRAANA's memory stores and recalls with time decay. The reinforcement path — boosting confidence when a session succeeds — is wired up, but the signal that actually triggers it hasn't shipped yet. So I call it "stores and recalls" until that loop closes and I can show it working. A user who sees memory surface a stale belief at high confidence loses trust in the whole system. Publishing your limits before your benchmarks isn't just an ethics call — it's a product decision. The larger plan Four systems: Adaptive Context, Cognitive Memory, Background Consolidation, Intelligent Router. All domain-agnostic. Nothing in the system knows anything about code specifically. The coding agent is just the proving ground because outcomes are easy to measure: did the code work, how many turns did it take, did it avoid repeating the same mistake from last session. Phase 2 is extracting the runtime so other developers can build domain agents on top of it. I'm not touching that extraction until Phase 1 validates the architecture. That discipline has been the hardest part of the whole project. GitHub: amitkumardubey/praana — MIT, TypeScript, Bun.

39m ago

---

**[We are Focused on the Wrong Problems!](https://www.reddit.com/r/artificial/comments/1uo5oiq/we_are_focused_on_the_wrong_problems/)**

Most of the focus is on AI being bad rather than how major companies are deploying AI. My concern isn't that AI is becoming more powerful. I mean, that is a concern, of course, but since most of the implications are speculative, you can't exactly take any stance or action on that problem other than countries coming together and setting rules and policies for how they distribute and use frontier models and capabilities, especially in warfare. My largest concern is what corporations and governments will use AI for on their own citizens. The data center builds are not just about AI. They're about creating an infrastructure that allows for total brain capital capturing. In other words there are real plans in place for collecting as much data as possible on our individual brains and if they can accurately map all of that out, they can measure how much and the quality of cognitive output we're providing to the state, which means they can valuate our worth based on cognitive outputs. Furthermore, they can use environmental nudging and algorithmic management to modify and shape individual behavior, which means protesting or voicing any concerns becomes obsolete. Big picture: The social contract between government, citizen, and business is being radically re-shaped for a world where regular people have little to no leveraging power, which destroys the power of voice. This is why we shouldn't destroy AI. Rather, we should figure out ways to ween ourselves off of the dependency we have on major tech companies so that we can gain leveraging power back, again. The biggest mistake is taking the bribes like what Bernie Sanders and Ro Kana are suggesting. I have nothing against them or anything, but their proposal to have the federal government own stock in big tech companies is a disaster in the making. If that happens, forget about any manageable evolution towards a better future. You'll be fighting the federal government who will be working on behalf of major tech companies because to not do so, means their ability to fund themselves will go flat. This is a huge trap that we're walking into, which is why the AI community must look towards de-centralized open-source systems that can be locally hosted for deploying and using AI at scale. If we rely too much on a few major corporations, we'll have entered a techno-feudalistic system where powers greater than you will be able to do just about anything with impunity. We can't let that happen!

39m ago

---

**[Un modello 100% locale sul tuo smartphone!](https://www.reddit.com/r/artificial/comments/1uo4dyo/un_modello_100_locale_sul_tuo_smartphone/)**

Devo dirlo, sono diventato matto...questa volta pensavo di mollare sul serio, ma poi stamattina il miracolo. (almeno per me). Ho fatto fine tuning e scritto tools per due modelli: un Qwen 3 da 1.5B e un altro da 4B quantizzati all'estremo. Il 4B è per smartphone con almeno 12Gb di RAM, mentre il piccolo è per la fascia media (occupa appena 2,5 GB di RAM)...sto creando un LoRa in bilingua per aiutare il piccolo a usare al meglio i tools, e lo sto distillando da un 32B, quindi meglio di uno fatto con lo stesso. Il 4B se la cava anche senza LoRA, ma entro domattina il piccolo dovrebbe essere diplomato (il teacher 32B ha fatto un ottimo lavoro). Potete essere crudeli come sempre, l'importante è essere costruttivi...potete scaricare l'apk qui (il modello lavora anche offline!) https://nothumanallowed.com/local a breve anche il .exe per windows, dove con un buon pc funziona senza problemi (sul mio mac pro va una scheggia!)

1h ago

---

**[i automated my entire social media content production with cloud mcp. heres what actually changed](https://www.reddit.com/r/artificial/comments/1uo26nd/i_automated_my_entire_social_media_content/)**

i run a few accounts at decent volume and the content production was tough what was helpfyl was connecting the claude mcp from a social media management tool. a lot of them are rolling this out right now you connect the mcp once, and after that you just chat with it. you build the content plan out in plain conversation, it generates the posts with consistent branding and a human sounding voice, and you approve everything from one place the stuff most people get wrong when they try to automate is they lean on generic prompts and get generic output the audience can smell instantly. they dont lock a consistent visual style so the page looks like five different people run it. running it all through one connected system handles that by default.

3h ago

---

**[Survey: 63% of Americans are uncomfortable letting AI help them choose who to vote for, and 80% are worried AI bots are answering political surveys. Is the discomfort about AI, or about trust?](https://www.reddit.com/r/artificial/comments/1unmy3d/survey_63_of_americans_are_uncomfortable_letting/)**

Saw a national survey from March on how people feel about AI in politics, and two numbers stuck with me. 63% said they'd be uncomfortable using an AI chatbot to help decide who to vote for, even though plenty of people are fine using chatbots to fact-check or follow issues. 80% said they're worried that AI bots, not real people, are answering the surveys that feed into policy and business decisions. It reads less like fear of the tech and more like people drawing a hard line at AI touching the actual decision. Where do folks here think that line should be? Source: https://data.verasight.io/ai/adults-views-on-ai-in-elections

17h ago

---

**[This week in AI: GPT-5.6, Gemini 3.5 Flash, Claude Science, and a Qwen price war — inference cost is collapsing across every tier at once](https://www.reddit.com/r/artificial/comments/1un6v9c/this_week_in_ai_gpt56_gemini_35_flash_claude/)**

Lot dropped this week and there's a pretty clear through-line, so figured I'd pull it together. Model releases: - OpenAI launched GPT-5.6 (Sol/Terra/Luna). The bit worth noting isn't the flagship — it's Terra, reportedly matching GPT-5.5 quality at ~2x cheaper, with Luna aimed at the low-cost end. - Google shipped Gemini 3.5 Flash (beats 3.1 Pro on several benchmarks), plus Nano Banana 2 Lite (images ~$0.034/1K-res) and Gemini Omni Flash (video ~$0.10/sec via API). - xAI made Grok 3 GA and Grok 4.1 live for everyone. Grok 5 still hasn't shipped, which is its own story at this point. Vertical / enterprise: - Anthropic launched Claude Science for pharma and lab research. Separately, the US govt lifted the export restrictions on Fable 5 / Mythos 5 that it had imposed only weeks earlier. - Mistral shipped OCR 4 (on-prem, structure-aware extraction) and is reportedly raising ~€3B at ~€20B. Open source: - Ollama crossed 52M monthly downloads, added `ollama launch` (one command to run coding agents on local or cloud models), and is now compatible with the Anthropic Messages API. - Hugging Face: agents can train models via Hub skills now; Meta + HF also launched OpenEnv for agent environments. Funding: - Together AI raised $800M Series C (~$8.3B post). Crunchbase notes ~88% of 2026 AI funding went to US companies. My take as someone building on top of these APIs: The thing I keep noticing is that the price collapse is happening across every tier simultaneously, not just at the bottom. When the "balanced" model gets 2x cheaper each generation and the Flash tier beats last year's Pro, it gets really hard to build a business whose only edge is "we use the best model." That edge evaporates on someone else's release schedule. The stuff that looked durable this week was all workflow-and-data — Claude Science, Mistral's on-prem OCR, Alibaba's agent ecosystem. Would genuinely like to hear how others here are handling multi-provider abstraction, because a surprise price or availability change shouldn't be able to wreck your margins overnight. And the frozen-then-unfrozen Anthropic thing means model availability is now a supply-chain risk, not a hypothetical.

1d ago

---

---

## Google News: "ai"

**[Philosophers Are the Latest Hiring Target for AI Companies](https://www.nytimes.com/2026/07/05/business/philosophy-majors-ai-jobs.html)**

The New York Times • 3h ago

---

**[How Hollywood’s youngest filmmakers are exposing Gen Z’s real problem with AI](https://fortune.com/2026/07/05/why-doesnt-gen-z-trust-ai-box-office-youtube-directors-backrooms-obsession/)**

The generation most fluent in generative tools has least trust. A new class of box-office creators explains the contradiction and what brands need to hear.

Fortune • 5h ago

---

**[Rate hike readjustment and AI hardware momentum: What to watch this week](https://finance.yahoo.com/economy/article/rate-hike-readjustment-and-ai-hardware-momentum-what-to-watch-this-week-160059243.html)**

A quiet calendar ahead gives the market plenty of space to go off the beaten path this week as investors gear up for the beginning of earnings season.

Yahoo Finance • 33m ago

---

**[6 Critical Actions To Take To Advance Your Career In The Age Of AI](https://www.forbes.com/sites/williamarruda/2026/07/05/6-critical-actions-to-take-to-advance-your-career-in-the-age-of-ai/)**

Your greatest career advantage won't come from ignoring AI or becoming more like it. It will come from partnering with AI.

Forbes • 34m ago

---

**[Terrorists using AI ‘could cause next pandemic’](https://www.telegraph.co.uk/politics/2026/07/05/terrorists-using-ai-could-cause-next-pandemic/)**

Government plans curbs on sale of DNA as systems progress opens door to deadly biological weapons

The Telegraph • 34m ago

---

**[Macquarie says now is the 'best time' to buy Chinese AI chip stocks. This one's its favorite](https://www.cnbc.com/2026/07/05/macquarie-says-now-is-best-time-to-buy-chinese-ai-chip-stocks-heres-its-favorite.html)**

Macquarie began research coverage of five Chinese companies making chips for artificial intelligence applications.

CNBC • 3h ago

---

**[To unlock agentic AI’s promise for government, America must build reliability](https://thehill.com/opinion/technology/5950143-ai-reliability-national-security/)**

The Hill • 1h ago

---

**[Stop asking employees to adopt AI](https://www.fastcompany.com/91568873/stop-asking-employees-to-adopt-ai)**

Fast Company • 8h ago

---

**[This $35 AI-powered Mac app transcribes your voice three times faster than typing — last chance to save](https://mashable.com/tech/july-5-voibe-lifetime-subscription)**

Work smarter on your Mac with this AI voice assistant.

Mashable • 7h ago

---

**[Palo Alto Networks and Koi Security sued over alleged AI error in cyber threat report](https://www.calcalistech.com/ctechnews/article/bjkvcpvxzl)**

MeetingTV claims a flawed intelligence classification led to global blocking of its services.

CTech • 4h ago

---

---

## HackerNews: "ai"

**[The bottleneck might be the air in the room](https://news.ycombinator.com/item?id=48783117)**

You gather your most expensive people into a room to make your most important decisions. Then, somewhere in the second hour, the room quietly gets worse at making them. Not the people. The room.

⬆️ 797 • 💬 454 • 1d ago • [Mike Bowler](https://blog.mikebowler.ca/2026/07/03/co2-and-decision-making/)

---

**[Protect your right to run local AI](https://news.ycombinator.com/item?id=48768951)**

⬆️ 545 • 💬 196 • 2d ago • [righttointelligence.org](https://righttointelligence.org/)

---

**[Please stop the AI confidence theater](https://news.ycombinator.com/item?id=48774414)**

We don’t need an extra reason to be anxious

⬆️ 233 • 💬 256 • 2d ago • [elenaverna.com](https://www.elenaverna.com/p/please-stop-the-ai-confidence-theater)

---

**[The short leash AI coding method for beating Fable](https://news.ycombinator.com/item?id=48766026)**

⬆️ 195 • 💬 242 • 2d ago • [blog.okturtles.org](https://blog.okturtles.org/2026/07/short-leash-ai-method/)

---

**[AI has torched the market for junior programmers](https://news.ycombinator.com/item?id=48788361)**

Junior programmers are getting destroyed by AI — down 19%, while devs over 40 thrive. Meanwhile, millions of non-developers are shipping real software without the job title. The credential market collapsed; the activity exploded. The problem: nobody's building the next generation of senior engineers.

⬆️ 95 • 💬 182 • 20h ago • [seldo.com](https://seldo.com/posts/ai-has-torched-the-market-for-junior-programmers/)

---

**[Instead of banning AI, I made a classroom contract with my students](https://news.ycombinator.com/item?id=48775499)**

⬆️ 93 • 💬 90 • 2d ago • [science.org](https://www.science.org/content/article/instead-banning-ai-i-made-classroom-contract-my-students)

---

**[President pardons 9 for Clean Air violations for 'fixing their car'](https://news.ycombinator.com/item?id=48791091)**

⬆️ 82 • 💬 50 • 12h ago • [msn.com](https://www.msn.com/en-us/news/crime/trump-pardons-9-for-clean-air-violations-for-fixing-their-car/ar-AA27cSkT)

---

**[AI saves about 3% of your hours, and almost none of it reaches the money](https://news.ycombinator.com/item?id=48777257)**

The real ROI of AI for knowledge work: the task-level gains (Noy-Zhang, Brynjolfsson), the jagged frontier (BCG-Harvard), the 2.8% real-world time saving and no earnings effect (Humlum), 95% of enterprise pilots with no P&L return (MIT), and how to capture what is real.

⬆️ 77 • 💬 94 • 1d ago • [okaneland.com](https://okaneland.com/study/ai-productivity-roi-at-work/)

---

**[Weird Al Yankovic Pulled Out of AI Ad Deal: 'I Can't Be the Poster Boy for AI'](https://news.ycombinator.com/item?id=48764326)**

Weird Al Yankovic revealed he was offered “a nice pile of money” to appear in a commercial but backed out after realizing it would involve AI.

⬆️ 74 • 💬 46 • 2d ago • [Variety](https://variety.com/2026/biz/news/weird-al-yankovic-rejected-ai-commercial-money-offer-1236800794/)

---

**[Ask HN: Why are so many "AI evangelists" posting such insufferable content?](https://news.ycombinator.com/item?id=48765450)**

⬆️ 66 • 💬 36 • 2d ago

---

---

## YouTube Videos: "ai"

**[I Tried Google&#39;s FREE AI Video Generator](https://www.youtube.com/watch?v=uRNP0RFXVXs)**

Watch Next https://youtu.be/zKLT9p6XuWg?si=6jP-jUlgWsHzHK-y In this video, I test Google's free Omni Flash AI video model ...

📺 Thomas Creates

👁️ 5K • 💬 1 • ⏱️ 8:21 • 1h ago

---

**[Google Just UNLOCKED the Nano Banana of AI Video (Gemini Omni Deep Dive)](https://www.youtube.com/watch?v=7HhlSu3pPvU)**

Try Gemini Omni Flash over on Higgsfield AI https://higgsfield.ai/s/gemini-omni-flash-jackvsai-lbMYAV Google just unlocked ...

📺 Jack Vs. AI

👁️ 1K • 👍 179 • 💬 13 • ⏱️ 23:46 • 2h ago

---

**[Private Credit Just Burst The $25 Trillion AI Bubble](https://www.youtube.com/watch?v=ktLyXGRHNCk)**

The private credit bust is now starting to spread into AI and the AI buildout which up to now has been mostly financed by these ...

📺 Eurodollar University

👁️ 44K • 👍 2K • 💬 182 • ⏱️ 17:23 • 17h ago

---

**[China&#39;s Free AI Just Came For ChatGPT And Claude (+18 Updates)](https://www.youtube.com/watch?v=iT_yv_nEdIo)**

FREE GUIDES + FOLLOW ALONG Join free here: https://links.stayingahead.com/YT55 You can now merge ChatGPT and Claude ...

📺 Vaibhav Sisinty

👁️ 35K • 👍 1K • 💬 41 • ⏱️ 26:16 • 11h ago

---

**[China Just Dropped An Ultra-Bionic AI Human Replica Robot](https://www.youtube.com/watch?v=kjqWO8kFk7M)**

China just revealed the U-World U1, a full-size ultra-bionic humanoid robot built for mass production. But the real story is not just ...

📺 AI Revolution

👁️ 35K • 👍 1K • 💬 203 • ⏱️ 13:32 • 18h ago

---

**[I Tested AI&#39;s Morality 🤯](https://www.youtube.com/watch?v=JkLjf4pJi9w)**

📺 Zack D. Films

👁️ 1.3M • 👍 155K • 💬 4K • ⏱️ 0:55 • 4h ago

---

**[The AI Layoff Payback Has Begun](https://www.youtube.com/watch?v=QorWpn2O_sI)**

This video is sponsored by Lumo by Proton: a privacy-first AI assistant from the Swiss company behind Proton Mail. Whether ...

📺 House of El - AI

👁️ 178K • 👍 12K • 💬 2K • ⏱️ 27:19 • 1d ago

---

**[Flock&#39;s A.I.-enabled street cameras see backlash across the country](https://www.youtube.com/watch?v=5fbmWnJGCtc)**

Activists are speaking out against new, A.I.-enabled cameras being used by municipalities across the country. Critics argue the ...

📺 NBC News

👁️ 131K • 👍 2K • 💬 1K • ⏱️ 6:08 • 1d ago

---

**[Jackie DeAngelis: This is a &#39;MASSIVE GROIN PUNCH&#39; in US&#39; AI race against China](https://www.youtube.com/watch?v=EGAqQXVbqAc)**

'The Big Money Show' discusses China's AI advancements, highlighting the threat and implications to the United States' ...

📺 Fox Business

👁️ 74K • 👍 2K • 💬 447 • ⏱️ 15:20 • 1d ago

---

**[The world’s best AI is being locked down](https://www.youtube.com/watch?v=0Pz-jfyMPqs)**

A global power struggle is emerging over artificial intelligence, as governments and tech companies compete for control over the ...

📺 Sky News

👁️ 36K • 👍 567 • 💬 141 • ⏱️ 5:40 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,533,844 • ❤️ 1,524 • 6d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 220,379 • ❤️ 3,444 • 3d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,044,217 • ❤️ 1,734 • 2d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 394,164 • ❤️ 722 • 10d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 7,010 • ❤️ 272 • 2d ago

---

**[Qwen3.6-27B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-27B-NVFP4)**

*NVIDIA*

The Qwen3.6-27B-NVFP4 is an FP4 quantized version of Alibaba's Qwen3.6-27B LLM, optimized by NVIDIA for efficient inference on NVIDIA GPUs. It excels in text generation tasks and is suitable for AI agents, chatbots, and RAG systems.

`text-generation` `18.2B`

⬇️ 297,130 • ❤️ 268 • 5d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 355,871 • ❤️ 1,020 • 16d ago

---

**[tabfm-1.0.0-pytorch](https://huggingface.co/google/tabfm-1.0.0-pytorch)**

*Google*

TabFM 1.0.0 is a zero-shot PyTorch foundation model for tabular classification and regression, supporting mixed data types without fine-tuning by using in-context learning. It excels in tabular tasks by leveraging alternating row and column attention mechanisms, making it suitable for rapid prototyping and scenarios where dataset-specific training is infeasible.

`tabular-classification`

⬇️ 2,670 • ❤️ 218 • 1d ago

---

**[DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)**

*DeepSeek*

DeepSeek-V4-Pro-DSpark is a text-generation model featuring a 1.6T parameter Mixture-of-Experts architecture with a 1 million token context window, optimized for long-context efficiency using Hybrid Attention. It excels in reasoning, coding, and agentic tasks, offering advanced capabilities for complex applications.

`text-generation` `889.5B`

⬇️ 12,580 • ❤️ 381 • 1d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 352,002 • ❤️ 431 • 10d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 50 • 💬 5 • ⭐ 13,327 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 73,452 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 103 • 💬 4 • ⭐ 90,896 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 25 • 💬 2 • ⭐ 9,828 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 13 • 💬 2 • ⭐ 18,752 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,464 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 250 • 💬 4 • ⭐ 10,654 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 85,395 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 13 • 💬 1 • ⭐ 10,267 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[OmniFlatten: An End-to-end GPT Model for Seamless Voice Conversation](https://huggingface.co/papers/2410.17799)**

*Qinglin Zhang, Luyao Cheng, Chong Deng et al. (9 authors)*

A novel GPT-based model, OmniFlatten, enables real-time natural full-duplex spoken dialogue through a multi-stage post-training technique that integrates speech and text without altering the original model's architecture.

▲ 16 • 💬 1 • ⭐ 60,724 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.17799) • [💻 code](https://github.com/karpathy/nanogpt)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 74.5k • 🔱 3.9k • 3d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.5k • 🔱 1.1k • 54m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.3k • 🔱 827 • 3h ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 5.8k • 🔱 768 • 2h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.4k • 🔱 210 • 2d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.4k • 🔱 181 • 2d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.9k • 🔱 72 • 2d ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 88 • 22d ago

---

**[GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills)**

AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

`Python`

⭐ 1.4k • 🔱 130 • 28d ago

---

**[nolangz/pixel2motion](https://github.com/nolangz/pixel2motion)**

AI logo animation skill: turn raster logos into smooth SVG animation, animated HTML demos, GIF/video previews, and motion QA evidence.

`Python` `ai-design-tools` `animated-logo` `brand-motion` `claude-skill` `codex-skill`

⭐ 1.4k • 🔱 117 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
