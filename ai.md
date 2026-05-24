---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-24T07:36:50.361473+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 24, 2026 at 07:36 UTC  
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

**[Vision-capable LLMs vs. OCR for long-document (including charts, images, tables, etc.) QA](https://www.reddit.com/r/artificial/comments/1tlzy43/visioncapable_llms_vs_ocr_for_longdocument/)**

I benchmarked vision-capable LLMs (the "just attach the PDF and let the model read it" pattern) against OCR-based pipelines on 30 long, image-heavy PDFs from MMLongBench-Doc (https://github.com/mayubo2333/MMLongBench-Doc). There were 171 questions in total, using Claude Sonnet 4.5 as the LLM. Post-retry results: Approach Accuracy $/query LlamaCloud premium + full-context 59.6% $0.1885 Azure premium + full-context 58.5% $0.2051 Azure basic + full-context 54.4% $0.1062 Agentic RAG 53.2% $0.0827 Native PDF (vision LLM) 52.0% $0.2552 LlamaCloud basic + full-context 50.9% $0.1049 Native PDF came 5th of 6 on accuracy and was the most expensive arm at $0.2552 per query. Two findings: Vision underperformed on chart-heavy and table-heavy pages, the territory that the "vision LLMs make OCR obsolete" claim most often points to. Premium OCR with layout extraction held up better there. The native-PDF arm had a 7% intrinsic failure rate (related to PDF file size) that survived retries. There were 27 first-pass failures, with 5 attempts of exponential backoff per failed query. Fifteen recovered, and 12 stayed permanently broken. These were concentrated in two specific PDFs that fail for predictable transport-layer reasons (the blog identifies them). OCR-based arms had a 0% intrinsic failure rate after retries. Caveats: 30 docs is a small sample. I ran McNemar's pairwise test to determine which gaps are real and which are within noise. Only 3 of 15 head-to-head gaps are statistically distinguishable at α = 0.05, so the order in the table is partly noise. The vision-versus-OCR finding survives the test. Full writeup: https://www.surfsense.com/blog/agentic-rag-vs-long-context-llms-benchmark

4h ago

---

**[Amnesty : US software company Palantir and other contractors were granted unlimited access to identifiable NHS England patient information](https://www.reddit.com/r/artificial/comments/1tlig93/amnesty_us_software_company_palantir_and_other/)**

16h ago

---

**[Elon, stop trying to make Grok happen. New data suggests government workers don’t like Elon Musk’s chatbot. Does anybody?](https://www.reddit.com/r/artificial/comments/1tlp9gz/elon_stop_trying_to_make_grok_happen_new_data/)**

New data suggests government workers don’t like Elon Musk’s chatbot. Does anybody?

🔗 [The Verge](https://www.theverge.com/ai-artificial-intelligence/936219/elon-stop-trying-to-make-grok-happen) • 12h ago

---

**[Exclusive: Departing Meta staffer posts biting anti-AI video internally amid mass layoffs](https://www.reddit.com/r/artificial/comments/1tlcscq/exclusive_departing_meta_staffer_posts_biting/)**

The tech giant made thousands of engineers train their AI replacements—then fired them.

🔗 [Mother Jones](https://www.motherjones.com/politics/2026/05/meta-video-ai-training-layoffs-video-exclusive-mci-bosworth-frenk/) • 21h ago

---

**[I think AI training is way more accessible than people realize](https://www.reddit.com/r/artificial/comments/1tlpv9g/i_think_ai_training_is_way_more_accessible_than/)**

What i have felt from my posts cus its all about AI so :- now it feels like almost everyone just rents some GPUs, opens a bunch of AI tools, and tries to train an AI using another AI People even use AI to search for datasets for them without actually checking what’s inside the data. Then they throw random datasets straight into training and wonder why the results are terrible while burning money on compute. A lot of people just want quick answers from a model trained on random internet garbage instead of understanding the data first. The funniest part is when the AI helping them find datasets can’t even properly read or understand the full dataset itself because of token limits, access limits, or incomplete context, but people still trust it blindly and keep feeding everything into training. So instead of building something useful they just end up generating random nonsense because nobody actually looked at the quality of the data going in.

12h ago

---

**[Who am I even supposed to trust when it comes to the future of AI?](https://www.reddit.com/r/artificial/comments/1tltq6b/who_am_i_even_supposed_to_trust_when_it_comes_to/)**

I am a PhD student (not in AI) and am usually alright when it comes to studying a topic I don't know much about. But it seems that because AI is so highly discussed nowadays, it's impossible to get a good gauge of what the rational scholarly consensus is regarding its and our future. I am constantly bombarded with people saying that at best most jobs are replaced and the future is a dystopia, and at worst AGI/ASI is achieved and we all are killed by a bioweapon or something. It honestly has me terrified, especially when I see a lot of figures in the AI sphere, including academics, seem to think that there are reasonably high "p(doom)"'s (what a horrifying concept that is). How am I supposed to parse all of this? Are there any actually level-headed people? Or are the people shouting about doom actually the level-headed ones? Compared to climate change, at least there are the IPCC reports which have laid out best guesses on what will happen. They're not perfect, but at least they exist.

9h ago

---

**[Is There a Roadmap for Applied AI Engineering Without Going Deep Into Data Science?](https://www.reddit.com/r/artificial/comments/1tm3vba/is_there_a_roadmap_for_applied_ai_engineering/)**

Started my career as a C# developer, then moved into application design and architecture, followed by Azure, and now I’m mainly working in AWS and DevOps. I want to transition into becoming a Senior Applied AI Engineer. The kind of role I’m interested in is designing and architecting AI-enabled applications, working with LLMs, agentic workflows, AI integrations, orchestration, automation, and possibly MLOps. What I’m not really interested in is going deep into the maths, data titlescience, or traditional ML research side of things. Most roadmaps I’ve seen seem heavily focused on statistics, model training, and data science, which doesn’t feel aligned with the kind of AI engineering work I want to do. I’m more interested in: AI application architecture LLM integrations Agentic systems and workflows AI platforms and infrastructure RAG systems MLOps and deployment Cloud-native AI systems AI security, governance, and observability Given my background in software engineering, cloud, and DevOps, is there a roadmap specifically for Applied AI Engineering? Would love advice from people already working in this space, especially on: What skills actually matter What to ignore Good projects to build Certifications or courses worth doing Whether deep ML knowledge is really necessary for senior roles

1h ago

---

**[OpenAI is hiring a $445,000 researcher. Requirements? Be 'tasteful and strategic.'](https://www.reddit.com/r/artificial/comments/1tlh2gh/openai_is_hiring_a_445000_researcher_requirements/)**

OpenAI and Sam Altman aim to automate AI research. They are now hiring for a role to prepare the company for self-training AI.

🔗 [Business Insider](https://www.businessinsider.com/openai-safety-team-ai-self-improvement-challenge-job-2026-5) • 17h ago

---

**[ig nobody is talking about the real reason most AI agents fail in the real world](https://www.reddit.com/r/artificial/comments/1tm4aau/ig_nobody_is_talking_about_the_real_reason_most/)**

we spend a lot of time in this community talking about capabilities. context windows, reasoning benchmarks, multi-step tool use, how well a model can write code or pass a bar exam. i'm not dismissing any of that. capabilities matter. but when i look at AI products failing in production, the capability of the model is almost never the issue. ive been building and consulting on AI agents for about 18 months. the failure modes i see constantly are: users do not go where the agent lives. the agent has a beautiful web interface. the user visits it twice and stops. not because the agent was unhelpful. because opening a browser tab is a cognitive action that requires intention, and most of daily life does not create the right moment for that intention. humans do not change their behavior to accommodate useful tools. useful tools have to show up in the behavior humans already have. the agent is reactive when it needs to be proactive. the smartest human assistant you have ever had did not just answer questions. they showed up. they flagged things before you asked. they sent you the thing you did not know you needed. most AI agents are search bars with a personality. they wait. waiting is not intelligence in practice. intelligence in practice is noticing and acting. the agent has no memory of who you are. you tell it your preferences, your context, your situation, and then come back 3 days later and it knows nothing. this is not a model limitation. the model can remember if you feed it the right context. this is an architecture choice that most teams make wrong because they are thinking about sessions instead of relationships. the agents that are succeeding in production are not necessarily the ones with the best models. they are the ones that live in whatsapp and imessage and telegram where users already are. that proactively reach out when something relevant happens. that maintain coherent memory of the person across weeks and months of conversation. the tooling to build this way exists now. agno and langchain for orchestration, photon codes for the cross channel messaging surface, langfuse for traces and memory debugging, good persistence in postgres or supabase. the architecture is not magic. what is still rare is the mindset of treating the channel and the memory as primary constraints rather than afterthoughts. i think the gap between what AI agents can theoretically do and what they actually do for people in their daily lives is almost entirely a distribution and persistence problem, not a capability problem. we are solving for the wrong thing.

1h ago

---

**[Your AI agent is one tool call away from doing something you didn’t authorize. Here’s the fix.](https://www.reddit.com/r/artificial/comments/1tm37ut/your_ai_agent_is_one_tool_call_away_from_doing/)**

The attack doesn’t come from your users. It comes from your agent’s environment, the emails it reads, the webpages it visits, the documents it retrieves, the database rows it queries. Every piece of external content your agent processes is a potential instruction source. And your agent has no way to tell the difference between data it was sent to process and commands it should follow. This is not theoretical. It is happening in production systems right now. Once you give an agent tools, email access, browser access, API calls, memory writes, the stakes change completely. A poisoned document doesn’t just return bad text. It tells your agent what to do next. And your agent does it. We tested this. Arc Gate blocked 100% of agentic tool poisoning attacks across 54 scenarios from ETH Zurich’s AgentDojo benchmark. 99% on 200 blind test cases from University of Illinois InjecAgent. 0% false positives on legitimate workflows. Arc Sentry caught a USENIX 2025 multi-turn jailbreak at Turn 3. LLM Guard caught 0 out of 8 turns on the same attack. The difference is architecture. Text classifiers read what the prompt says. Arc Gate enforces where instructions are allowed to come from. Arc Sentry reads what the model’s internal state does, before generate() is even called. If your agent touches the real world, you need a runtime governance layer. Finance agent demo — no signup: https://web-production-6e47f.up.railway.app/finance-demo Arc Gate — hosted proxy, one URL change: https://github.com/9hannahnine-jpg/arc-gate — $29/month Arc Sentry — self-hosted models: https://github.com/9hannahnine-jpg/arc-sentry — pip install arc-sentry

2h ago

---

---

## Google News: "ai"

**[‘AI washing’: firms are scrambling to rebrand themselves as tech-focused](https://www.theguardian.com/technology/2026/may/24/ai-washing-pr-firms-scrambling-rebrand)**

PR executives say UK companies are forcing them to present ordinary automation as artificial intelligence

The Guardian • 1h ago

---

**[Venture Capitalist John Doerr Says AI Is the Biggest Tech ‘Tsunami’ Ever](https://www.wsj.com/tech/ai/john-doerr-ai-opinion-1d64ee60)**

WSJ • 16h ago

---

**[Nvidia Quietly Builds Major AI Portfolio Shaping Investor Risk And Optionality](https://finance.yahoo.com/markets/stocks/articles/nvidia-quietly-builds-major-ai-071112516.html)**

Nvidia (NasdaqGS:NVDA) has built one of Silicon Valley's largest private AI investment portfolios under CEO Jensen Huang. The company nearly doubled its private company holdings over the past year, according to its latest quarterly disclosure. Nvidia deployed record capital into emerging AI and technology ventures, including nearly US$18b into private ventures in a single quarter. As of 26 April, Nvidia reported more than US$42b in private company holdings linked to the broader AI...

Yahoo Finance • 25m ago

---

**[Overcoming Situational Depression Via Generative AI Including Tapping Into ChatGPT](https://www.forbes.com/sites/lanceeliot/2026/05/24/overcoming-situational-depression-via-generative-ai-including-tapping-into-chatgpt/)**

Situational depression arises when an event or circumstance triggers you into a bout of depression. AI can help to overcome this. An AI Insider scoop.

Forbes • 21m ago

---

**[I avoid AI tools because thinking is supposed to be hard. It’s what makes us human | Wendy Liu](https://www.theguardian.com/commentisfree/2026/may/24/ai-tools-thinking-human-hard-coding-writing-technology)**

As intelligence itself becomes privatised by big tech, allowing your intellectual faculties to wither in service of inane bots seems a dangerous move, says author Wendy Liu

The Guardian • 35m ago

---

**[Here's why people are booing college commencement speakers this year](https://www.usatoday.com/story/news/nation/2026/05/23/college-graduation-speakers-booed-ai/90232153007/)**

Multiple college graduations were marked by booing at featured speakers, who came to realize they had "struck a chord." What set the crowd off?

USA Today • 13h ago

---

**[‘F*** this guy’: Graduation speakers keep getting booed for talking about artificial intelligence](https://www.yahoo.com/news/politics/articles/f-guy-graduation-speakers-keep-125456074.html)**

Commencement speakers want new graduates to feel optimistic about artificial intelligence — instead students are booing. New grads tell Josh Marcus that their fury about doddering policymakers and loo...

Yahoo • 18h ago

---

**[Why College Students Are Booing AI](https://www.theatlantic.com/ideas/2026/05/ai-graduation-speeches-booing/687266/)**

The sound of a cosmic howl

The Atlantic • 20h ago

---

**[AI is changing the internet forever. Here’s how](https://www.cnn.com/2026/05/23/tech/ai-internet-search)**

Google is giving the search bar its biggest update in 25 years, another sign that AI is changing the way people use the internet and find information.

CNN • 22h ago

---

**[There’s Never Been a Better Time to Study Computer Science](https://www.theatlantic.com/technology/2026/05/computer-science-major-coding-ai/687279/)**

Even as AI progresses, coders aren’t doomed.

The Atlantic • 20h ago

---

---

## HackerNews: "ai"

**[AI is just unauthorised plagiarism at a bigger scale](https://news.ycombinator.com/item?id=48222383)**

AI takes in all the input, whether the original authors have consented or not, and do some "learning", and then the AI companies sell these learned result to...

⬆️ 816 • 💬 731 • 2d ago • [Axel's blog](https://axelk.ee/ai-is-just-unauthorised-plagiarism-at-a-bigger-scale/)

---

**[Throwing AI-generated walls of text into conversations](https://news.ycombinator.com/item?id=48219992)**

Stop throwing AI-generated walls of text into conversations. If they wanted an AI essay, they would have asked ChatGPT themselves.

⬆️ 699 • 💬 417 • 2d ago • [noslopgrenade.com](https://noslopgrenade.com/)

---

**[Steve Wozniak cheered after telling students they have AI – actual intelligence](https://news.ycombinator.com/item?id=48233563)**

Apple cofounder Steve Wozniak's speech about AI at Grand Valley State University earlier this month got a laugh and applause from graduates.

⬆️ 643 • 💬 540 • 1d ago • [Business Insider](https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5)

---

**[Shunning AI is the human choice](https://news.ycombinator.com/item?id=48222366)**

LinkedIn may be awash with boosters, but shunning AI is the human choice.

⬆️ 370 • 💬 538 • 2d ago • [The Handbasket](https://www.thehandbasket.co/p/hating-ai-is-good-actually)

---

**[AI has a multiplying effect on existing technical skills](https://news.ycombinator.com/item?id=48235526)**

Friendly articles and tutorials for front-end web developers. ❤️

⬆️ 332 • 💬 309 • 1d ago • [joshwcomeau.com](https://www.joshwcomeau.com/email/wham-launch-005-elephant-2-p/)

---

**[Italy moves to Airbus A330 tankers](https://news.ycombinator.com/item?id=48248775)**

Rome shifts course: six Airbus A330 MRTT tanker aircraft, worth around €1.39 billion in total, to bolster the European pillar in NATO. #EuropeNews

⬆️ 252 • 💬 99 • 15h ago • [euronews](https://www.euronews.com/my-europe/2026/05/21/italy-moves-to-airbus-a330-tankers-in-major-nato-aligned-shift)

---

**[Samsung chip workers will get an average $340k bonus as AI profits soar](https://news.ycombinator.com/item?id=48230892)**

The South Korean chipmaker struck a last-minute deal with its union to avert an 18-day strike, unlocking a $26.6 billion payout pool

⬆️ 251 • 💬 195 • 2d ago • [Quartz](https://qz.com/samsung-chip-workers-bonus-ai-profits-052126)

---

**[Is AI Profitable Yet?](https://news.ycombinator.com/item?id=48243863)**

⬆️ 250 • 💬 195 • 1d ago • [isaiprofitable.com](https://isaiprofitable.com/)

---

**[Microsoft reports AI is more expensive than paying human employees](https://news.ycombinator.com/item?id=48244434)**

Companies are racing to incentivize employees to use AI. But as some companies are finding, the more employees that use the technology, the heavier the bill.

⬆️ 223 • 💬 65 • 1d ago • [Fortune](https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/)

---

**[The Companies Cutting Headcount for AI Will Lose to the Ones Who Didn't](https://news.ycombinator.com/item?id=48234547)**

Organisations using AI to cut headcount are making a short-term trade with long-term consequences. The ones holding their teams together and investing in how those teams operate with AI are building something more durable.

⬆️ 202 • 💬 201 • 1d ago • [libertas.software](https://libertas.software/en/knowledge-hub/19/the-companies-cutting-headcount-for-ai-will-lose-to-the-ones-who-didnt)

---

---

## YouTube Videos: "ai"

**[Trump’s hilarious AI video trashing ‘unfunny hack’ Stephen Colbert sends the left into a meltdown](https://www.youtube.com/watch?v=GDwooMEwWgk)**

Sky News host James Morrow discusses late night TV host Stephen Colbert's final show. “Of course, we had Stephen Colbert, the ...

📺 Sky News Australia

👁️ 5K • 👍 564 • 💬 155 • ⏱️ 3:20 • 2h ago

---

**[The singularity is near: Google unveils next phase of AI](https://www.youtube.com/watch?v=zvJ5KfNjOCk)**

ABC News' Nathan Rousseau Smith travels to Google I/O where the search giant unveiled AI agent Gemini Spark, new smart ...

📺 ABC News

👁️ 80K • 👍 1K • 💬 260 • ⏱️ 5:06 • 1d ago

---

**[AI Just Crossed The Line We Were Afraid Of: Continual Harness](https://www.youtube.com/watch?v=qCFyprzrCvA)**

Princeton researchers just revealed Continual Harness, a self-improving AI system that learns while it is already running.

📺 AI Revolution

👁️ 32K • 👍 2K • 💬 170 • ⏱️ 13:31 • 1d ago

---

**[Zuckerberg Caught On SECRET RECORDING:Forcing Employees To Train Their AI Replacements! ](https://www.youtube.com/watch?v=uNrjuGENu44)**

Leaked audio from a Meta all-hands meeting reveals Mark Zuckerberg telling employees that the company is training AI models ...

📺 The Jimmy Dore Show

👁️ 84K • 👍 7K • 💬 2K • ⏱️ 15:52 • 12h ago

---

**[Google’s AI endgame is here… everything you missed at I/O 2026](https://www.youtube.com/watch?v=9OQ5vaYbGV0)**

Try using Emergent's specialized agents in parallel to build any full-stack application ...

📺 Fireship

👁️ 608K • 👍 19K • 💬 1K • ⏱️ 5:44 • 1d ago

---

**[Figure 03 AI Robot Reveals Its UNFAIR Advantage… Humans Can’t Match It](https://www.youtube.com/watch?v=NPOqqDASRCA)**

A 22-year-old intern just beat a humanoid robot… but this might be the LAST time a human wins like this. In Figure AI's wild Man ...

📺 The AI Nexus

👁️ 2K • 👍 92 • 💬 19 • ⏱️ 18:21 • 6h ago

---

**[Claude Mythos: The AI that can break the internet | DW News](https://www.youtube.com/watch?v=C3hAya6JjJ8)**

A new AI model, Claude Mythos, can uncover hidden vulnerabilities and chain exploits—raising global fears over cyberattacks, ...

📺 DW News

👁️ 16K • 👍 287 • 💬 51 • ⏱️ 3:45 • 1d ago

---

**[Joe Rogan accidentally exposed AI in four words](https://www.youtube.com/watch?v=waFl4uBfXRA)**

Token mania. I've been a user of Proton for almost a decade and I'm grateful to them for agreeing to sponsor this video. Proton ...

📺 Mo Bitar

👁️ 188K • 👍 11K • 💬 2K • ⏱️ 11:39 • 1d ago

---

**[The Odds: Are Americans concerned about AI replacing jobs?](https://www.youtube.com/watch?v=C4RPb3L5Ifo)**

CNN's Sara Sidner and chief data analyst Harry Enten examine the evolving landscape facing college graduates as they enter the ...

📺 CNN

👁️ 86K • 👍 615 • 💬 172 • ⏱️ 4:08 • 1d ago

---

**[Microsoft Can’t Afford AI. Starbucks Can’t Trust It! #ai #anthropic #openai #claude #aibubble](https://www.youtube.com/watch?v=zzNyQxHWPnM)**

The Microsoft Anthropic situation is even weirder, microsoft hosts claude on azure, uses claude inside 365 copilot, has a $30 ...

📺 Mayankshah

👁️ 73K • 👍 3K • 💬 63 • ⏱️ 1:42 • 17h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 1,227 • ❤️ 719 • 1d ago

---

**[Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)**

*Tencent*

Hy-MT2-1.8B is a fast, 1.8B parameter multilingual translation model supporting 33 languages, optimized for on-device deployment with 1.25-bit quantization (440MB storage, 1.5x speedup). It excels in general, business, and instruction-following translation tasks, outperforming mainstream commercial APIs.

`translation` `2.0B`

⬇️ 2,564 • ❤️ 479 • 2d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 40,368 • ❤️ 625 • 5d ago

---

**[Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)**

*Tencent*

Hy-MT2-30B-A3B is a large-scale (30B parameters, MoE) multilingual translation model supporting 33 languages. It excels in general, business, and instruction-following translation tasks, outperforming leading open-source models and commercial APIs.

`translation` `30.1B`

⬇️ 970 • ❤️ 296 • 2d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 5,283 • ❤️ 279 • 3d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 78,771 • ❤️ 262 • 3d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for on-device image and video understanding, offering strong foundation and multimodal capabilities with mixed visual token compression for flexible speed/accuracy trade-offs.

`image-text-to-text` `1.3B`

⬇️ 269,589 • ❤️ 916 • 4d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, featuring a prompt enhancer for improved input processing and supporting various LTX 2.3 formats.

`text-to-video` `9.0B`

⬇️ 1,286,075 • ❤️ 1,310 • 2d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter causal language model with vision capabilities, optimized for faster inference via MTP. It excels at agentic coding, reasoning, and handling extended contexts up to 1M tokens, making it suitable for complex development workflows and iterative tasks.

`image-text-to-text` `27.3B`

⬇️ 597,584 • ❤️ 443 • 3d ago

---

**[command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)**

*Cohere Labs*

Command A+ is a 25B parameter, multilingual, vision-capable LLM optimized for agentic and reasoning tasks. It supports a 128K context window and offers a W4A4 quantization for efficient enterprise deployment.

`image-text-to-text` `125.8B`

⬇️ 4,261 • ❤️ 187 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 80 • 💬 3 • ⭐ 79,016 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 64,631 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,400 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://huggingface.co/papers/2605.18678)**

*Fengyi Fu, Mengqi Huang, Shaojin Wu et al. (13 authors)*

🏢 bytedance-research

Lance is a unified multimodal model that combines understanding, generation, and editing capabilities for images and videos through collaborative multi-task training and a dual-stream architecture.

▲ 71 • 💬 4 • ⭐ 796 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18678) • [💻 code](https://github.com/bytedance/Lance) • [🔗 project](https://lance-project.github.io/)

---

**[LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://huggingface.co/papers/2605.18739)**

*Yukang Chen, Luozhou Wang, Wei Huang et al. (16 authors)*

🏢 NVIDIA

LongLive-2.0 presents an NVFP4-based parallel infrastructure for long video generation that addresses training and inference bottlenecks through sequence-parallel autoregressive training and diffusion model tuning.

▲ 108 • 💬 3 • ⭐ 1,818 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18739) • [💻 code](https://github.com/NVlabs/LongLive) • [🔗 project](https://nvlabs.github.io/LongLive/LongLive2/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 74,655 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation](https://huggingface.co/papers/2605.19833)**

*Zhifei Xie, Kaiyu Pang, Haobin Zhang et al. (7 authors)*

🏢 National University of Singapore

Mega-ASR framework improves robustness in real-world speech recognition through compound-data construction and progressive acoustic-to-semantic optimization techniques.

▲ 126 • 💬 3 • ⭐ 398 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.19833) • [💻 code](https://github.com/xzf-thu/Mega-ASR) • [🔗 project](https://xzf-thu.github.io/Mega-ASR/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 8 • 💬 0 • ⭐ 18,549 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 4 • 💬 1 • ⭐ 5,596 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 120 • 💬 10 • ⭐ 10,465 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 4.7k • 🔱 487 • 2d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.5k • 🔱 1.1k • 6d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.6k • 🔱 179 • 9m ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.3k • 🔱 386 • 2d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.2k • 🔱 344 • 6d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.0k • 🔱 445 • 3d ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.8k • 🔱 211 • 17d ago

---

**[Nutlope/hallmark](https://github.com/Nutlope/hallmark)**

Anti-AI-slop design skill for Claude Code, Cursor, and Codex.

`CSS`

⭐ 1.8k • 🔱 117 • 3d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.7k • 🔱 184 • 3d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 1.6k • 🔱 115 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
