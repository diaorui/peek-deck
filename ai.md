---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-24T17:03:08.297621+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 24, 2026 at 17:03 UTC  
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

**[Multi-agent loop failures might be org-design failures, not prompt failures](https://www.reddit.com/r/artificial/comments/1tme23u/multiagent_loop_failures_might_be_orgdesign/)**

Repo: https://github.com/jeongmk522-netizen/agentlas\_org\_chart Almost every multi-agent setup I have shipped or tested eventually hits the same wall. Agents bouncing between each other, reviewers asking for one more polish pass forever, research workers spawning indefinite subtopics, tool calls spiraling until the recursion limit kicks in. The framework docs usually call these "loops" and offer a max-iteration knob. I started suspecting the knob is treating a symptom, and the real issue is closer to how the agents are organized to begin with. The pattern that kept reappearing: when agents are designed as peers (researcher talks to analyst, analyst talks to writer, writer hands back to reviewer), nobody clearly owns the outcome. Every agent can keep asking another agent for more work. The graph has stop conditions on paper, but no single agent has the authority to declare "this is done, stop the run." That authority is implicit at best and gets diluted across the peer network. The hypothesis I am testing is that loop failures are organization-design failures more than prompt failures. The fix is to treat the agent network as an org chart with explicit reporting lines, not a chat room of peers. One accountable mission owner. One owner per workstream. Finite delegation depth. A typed return contract per worker (status, evidence, output, blockers, next action). Manager-only authority to reopen or terminate. Memory lives at the authority layers, specialists get scoped context only. The layers I have been working with are roughly chair, strategy office, division manager, team lead, and specialist worker, with QA and policy as separate staff offices that can reject and escalate but cannot themselves spawn unbounded new work. The reviewer-recursion failure mode in particular gets killed when verifiers are structurally allowed one reject pass, then must escalate. Frameworks already have most of the primitives. CrewAI has a hierarchical process where a manager validates worker output. LangGraph has supervisors, subagents, and an explicit recursion limit. OpenAI Agents SDK has manager-style orchestration distinct from peer handoffs. AutoGen has GroupChatManager. Anthropic's published research system is orchestrator-worker. What I think is underused is treating the manager not as a moderator for an open group chat but as a formal reporting line with authority to terminate. Two things I am unsure about. First, hierarchy can become its own bottleneck. If every decision routes upward, the chair agent becomes a single point of latency and a single point of failure. Second, escalation-as-feature only works if the top of the org chart has real stop authority. If the chair just calls another LLM that calls more LLMs, the loop just moved one floor up.

2h ago

---

**["I'm retired. I showed my MS Paint paintings to AI for feedback. It accidentally invented an entire fake art movement. Google believes it's real."](https://www.reddit.com/r/artificial/comments/1tmb7c6/im_retired_i_showed_my_ms_paint_paintings_to_ai/)**

"I'm retired and started showing my MS Paint paintings to AI for criticism. The AI invented feuding critics, manifestos and a legal barrister to defend my work. Google now has a definition for my made up term. Here's what an accidental human/AI creative partnership looks like." Ralph Rumpelton https://zootsims1.wordpress.com/

4h ago

---

**[Vision-capable LLMs vs. OCR for long-document (including charts, images, tables, etc.) QA](https://www.reddit.com/r/artificial/comments/1tlzy43/visioncapable_llms_vs_ocr_for_longdocument/)**

I benchmarked vision-capable LLMs (the "just attach the PDF and let the model read it" pattern) against OCR-based pipelines on 30 long, image-heavy PDFs from MMLongBench-Doc (https://github.com/mayubo2333/MMLongBench-Doc). There were 171 questions in total, using Claude Sonnet 4.5 as the LLM. Post-retry results: Approach Accuracy $/query LlamaCloud premium + full-context 59.6% $0.1885 Azure premium + full-context 58.5% $0.2051 Azure basic + full-context 54.4% $0.1062 Agentic RAG 53.2% $0.0827 Native PDF (vision LLM) 52.0% $0.2552 LlamaCloud basic + full-context 50.9% $0.1049 Native PDF came 5th of 6 on accuracy and was the most expensive arm at $0.2552 per query. Two findings: Vision underperformed on chart-heavy and table-heavy pages, the territory that the "vision LLMs make OCR obsolete" claim most often points to. Premium OCR with layout extraction held up better there. The native-PDF arm had a 7% intrinsic failure rate (related to PDF file size) that survived retries. There were 27 first-pass failures, with 5 attempts of exponential backoff per failed query. Fifteen recovered, and 12 stayed permanently broken. These were concentrated in two specific PDFs that fail for predictable transport-layer reasons (the blog identifies them). OCR-based arms had a 0% intrinsic failure rate after retries. Caveats: 30 docs is a small sample. I ran McNemar's pairwise test to determine which gaps are real and which are within noise. Only 3 of 15 head-to-head gaps are statistically distinguishable at α = 0.05, so the order in the table is partly noise. The vision-versus-OCR finding survives the test. Full writeup: https://www.surfsense.com/blog/agentic-rag-vs-long-context-llms-benchmark

14h ago

---

**[Elon, stop trying to make Grok happen. New data suggests government workers don’t like Elon Musk’s chatbot. Does anybody?](https://www.reddit.com/r/artificial/comments/1tlp9gz/elon_stop_trying_to_make_grok_happen_new_data/)**

New data suggests government workers don’t like Elon Musk’s chatbot. Does anybody?

🔗 [The Verge](https://www.theverge.com/ai-artificial-intelligence/936219/elon-stop-trying-to-make-grok-happen) • 21h ago

---

**[Amnesty : US software company Palantir and other contractors were granted unlimited access to identifiable NHS England patient information](https://www.reddit.com/r/artificial/comments/1tlig93/amnesty_us_software_company_palantir_and_other/)**

1d ago

---

**[EdgeModel](https://www.reddit.com/r/artificial/comments/1tm92gy/edgemodel/)**

The idea: A platform where: Businesses can find specialized AI models (not general ChatGPT-style APIs) Developers can train and sell AI models optimized for specific business use cases Models are designed for edge deployment (low cost, offline, fast inference) Everything is focused on reducing AI API costs and improving performance for real business workflows Think: Instead of paying high API costs for generic AI businesses use smaller, optimized models tailored to their exact use case. (OCR, surveillance, retail analytics, automation, etc.) And developers earn money by: Selling trained models Offering optimized deployments Customizing models for businesses The problem I’m trying to solve: A lot of companies are: burning money on AI API calls struggling with latency and scaling costs unable to deploy AI models locally or efficiently relying on generic models that are not optimized for their workflows My question to you: Would businesses actually use something like this instead of just using OpenAI / APIs? If you are a developer, would you bother uploading/selling models like this? What would stop you from trusting or using a platform like this? Is this solving a real problem or does it sound unnecessary? Most importantly, would you personally sign up for something like this? I would much appreciate if I can get some honest feedback from you all! I’m not looking for validation, I want to know if this is actually needed in the market or just sounds good but won’t get real adoption. Appreciate any insights, especially from people who’ve built or used AI products in production.

6h ago

---

**[Exclusive: Departing Meta staffer posts biting anti-AI video internally amid mass layoffs](https://www.reddit.com/r/artificial/comments/1tlcscq/exclusive_departing_meta_staffer_posts_biting/)**

The tech giant made thousands of engineers train their AI replacements—then fired them.

🔗 [Mother Jones](https://www.motherjones.com/politics/2026/05/meta-video-ai-training-layoffs-video-exclusive-mci-bosworth-frenk/) • 1d ago

---

**[Who am I even supposed to trust when it comes to the future of AI?](https://www.reddit.com/r/artificial/comments/1tltq6b/who_am_i_even_supposed_to_trust_when_it_comes_to/)**

I am a PhD student (not in AI) and am usually alright when it comes to studying a topic I don't know much about. But it seems that because AI is so highly discussed nowadays, it's impossible to get a good gauge of what the rational scholarly consensus is regarding its and our future. I am constantly bombarded with people saying that at best most jobs are replaced and the future is a dystopia, and at worst AGI/ASI is achieved and we all are killed by a bioweapon or something. It honestly has me terrified, especially when I see a lot of figures in the AI sphere, including academics, seem to think that there are reasonably high "p(doom)"'s (what a horrifying concept that is). How am I supposed to parse all of this? Are there any actually level-headed people? Or are the people shouting about doom actually the level-headed ones? Compared to climate change, at least there are the IPCC reports which have laid out best guesses on what will happen. They're not perfect, but at least they exist.

18h ago

---

**[I built 10 gamified, interactive presentation decks to teach Agentic AI (Stop falling asleep reading whitepapers).](https://www.reddit.com/r/artificial/comments/1tmc38r/i_built_10_gamified_interactive_presentation/)**

Hey everyone, I've noticed a massive gap in how developers are trying to learn Agentic AI right now. There are hundreds of theoretical whitepapers and boring PowerPoint decks about ReAct loops, GraphRAG, and Semantic Routing. The problem is passive reading. You read a 20-page doc on multi-agent handoffs, close the tab, and immediately forget how the architecture actually works. So, I built a custom presentation engine directly into the AgentSwarms platform and just published 10 gamified, interactive slide decks. Here is how the learning loop works: Instead of just staring at static diagrams, the slides require you to interact with the concepts. You click to reveal logic paths, test your intuition on how an agent would route a specific prompt, and actively engage with the architecture. It uses active recall so the patterns actually stick in your brain before you ever touch a line of code. The decks cover everything from zero-to-production: The Basics: What a system prompt actually does, how RAG prevents hallucinations, and how tools give an LLM "hands." The Swarm: Building a 3-agent swarm, adding human-in-the-loop (HITL) approval gates, and deterministic routing logic. Production: Building multi-tenant RAG, cost-optimization, and shadow-mode LLM-as-a-Judge evals. It is completely free to read and play with the decks in the browser (no login or local setup required). I'd love for you to jump into one of the specialized deep-dive decks, click around, and let me know how this gamified learning loop feels compared to reading a standard Medium article! Link: agentswarms.fyi/learn

3h ago

---

**[Why We Build](https://www.reddit.com/r/artificial/comments/1tmgh0a/why_we_build/)**

One silver-lining to the dead internet we're living in, today, is that it's very quickly teaching us that we can't rely on our senses as much as we believe we can. It's not healthy to always live in skepticism, but it is necessary in a World where you don't know what's up or down anymore. That's why we need great minds to focus their attention on solving the problems associated with credible information sharing without it becoming some centralized playground designed to look like the free-flowing exchange of ideas. If we don't solve for that, then I guess we're heading into a future that a small handful of people want because elections or public opinion will no longer matter. One of the biggest focuses in AI should be in figuring out how to get it to provide deep credible knowledge in specific domains that can be best applied to the problems we're trying to solve. Sure, it can do this with enough fenagling, but what I really mean is having something easy for everyone to use like Perplexity or Gemini, only it doesn't simply find consensus information from the internet using all these black box methods that are owned by major corporations. Instead, it should use direct knowledge from domain experts who structure and cite their material and as users, we should be able to backtrack all of it, including the original author. And all of this should be achievable by simply engaging with a chatbot agent that can reliably go out and help me discover all of these things. Also, we shouldn't have to simply trust that the application works. We should be able to go in and see exactly how it's working. This way, the public can audit the systems we're relying on for grounding our worldviews. That, to me, is where we should be if we really want to break from the chains of propaganda and reclaim our genuine thoughts about how we ought to live. The alternative independent media space was co-opted long ago and now all of the feeds keep us in a state of perpetual dislocation from our friends, family, communities, new solutions, and better approximations to the truth. We exist in a walled-off digital pasture. But if regular people who are smart and capable enough decide to leverage this new technology, then we can break through the fencing and finally live in a world where discovery-based researching and learning can be easier than Google, which could eventually individuate society again, like how it was before, instead of keeping us clustered into specific groups based on our viewing preferences. That's why my brother and I got into this business. Yeah, sure, we also wanna make a buck so we can retire with dignity. That's true. But the drive has always stemmed from wanting to figure out a better way for people to share hidden insights and create things that are bigger than they thought they could handle. We have a long way to go, but we're making the first small steps, even if it isn't obvious, just yet. Bottom line, though? Humanity must figure out a way to help us master the means and methods of discovery-based knowledge acquisition, execution, and immediate distribution of information based on relevancy and needs from those who search instead of those who passively soak information in from the curated feeds. And all of this needs to be easy enough for a 12 year-old to do. If anyone else is working on this problem, we'd love to hear your thoughts, even if it's through a DM. We're living in the most exciting times, but with adventure, comes danger. So maybe, idk. Let's make it more fun and less hazardous, so that we can, at least, live long enough to re-tell this great story that we're all a part of.

49m ago

---

---

## Google News: "ai"

**[To A.I. Executives, We’re All Just ‘Meat Computers’](https://www.nytimes.com/2026/05/24/business/meat-computer-brain-artificial-intelligence.html)**

The New York Times • 8h ago

---

**[What to know about the AI models that are jolting Washington](https://www.politico.com/news/2026/05/24/anthropic-openai-mythos-what-to-know-00934668)**

Politico • 6h ago

---

**[Google CEO Sundar Pichai says booing graduates will shape AI's future — and live with its consequences](https://www.businessinsider.com/sundar-pichai-google-graduation-speech-stanford-ai-backlash-eric-schmidt)**

As commencement speakers face restless crowds of new graduates, Google CEO Sundar Pichai says he's ready for his turn at Stanford next month.

Business Insider • 35m ago

---

**[Humanoid robots work nonstop in package test](https://www.foxnews.com/tech/humanoid-robots-work-nonstop-package-test)**

Figure AI claims its three humanoid robots completed over 24 hours of continuous autonomous package sorting without any human control in a warehouse test.

Fox News • 32m ago

---

**[This Artificial Intelligence (AI) Stock Just Became Too Cheap to Ignore](https://finance.yahoo.com/markets/stocks/articles/artificial-intelligence-ai-stock-just-104000990.html)**

Microsoft stock hasn't received much love lately despite the company's solid fundamentals.

Yahoo Finance • 6h ago

---

**[The AI Stock I'm Buying for My Retirement Portfolio -- and Why It Has Nothing to Do With Hype](https://www.fool.com/investing/2026/05/24/the-ai-stock-im-buying-for-my-retirement-portfolio/)**

It's not easy to find companies you're confident in for the next 30 years, but this artificial intelligence (AI) stock fits the bill for me.

The Motley Fool • 7h ago

---

**[Berkshire Hathaway Rebalances Under Greg Abel With Bigger AI And Tech Bet](https://finance.yahoo.com/markets/stocks/articles/berkshire-hathaway-rebalances-under-greg-161316454.html)**

Greg Abel, now CEO of Berkshire Hathaway (NYSE:BRK.B), has overseen a major reshaping of the stock portfolio, including full exits from Amazon, Visa, Mastercard, and UnitedHealth. Berkshire has built a top 5 position in Alphabet and has sharply increased AI related holdings, which now account for more than a third of the portfolio’s value. These moves reflect the biggest shift in Berkshire’s capital allocation approach in decades, with a clearer tilt toward technology and AI focused...

Yahoo Finance • 49m ago

---

**[With AI now reading student names at graduation, not everyone is applauding](https://www.washingtonpost.com/education/2026/05/24/schools-turn-ai-graduation-ceremonies-drawing-mixed-success/)**

Officials say the tech can help ensure names are pronounced correctly and speed up ceremonies, but some parents and students are pushing back.

The Washington Post • 1h ago

---

**[Metro Detroit students gain access to new $5M AI, robotics learning hub](https://www.mlive.com/news/detroit/2026/05/metro-detroit-students-gain-access-to-new-5m-ai-robotics-learning-hub.html)**

MLive.com • 5h ago

---

**[Voices: AI is making my classmates and me lazy. Here’s how we fix it.](https://www.sltrib.com/opinion/commentary/2026/05/24/voices-ai-is-making-my-classmates/)**

“The only way to fight AI in schools is for the students to take accountability,” writes high school student Andrew Madsen in an op-ed. “I want students to give up using AI on assignments.”

The Salt Lake Tribune • 4h ago

---

---

## HackerNews: "ai"

**[Steve Wozniak cheered after telling students they have AI – actual intelligence](https://news.ycombinator.com/item?id=48233563)**

Apple cofounder Steve Wozniak's speech about AI at Grand Valley State University earlier this month got a laugh and applause from graduates.

⬆️ 643 • 💬 543 • 2d ago • [Business Insider](https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5)

---

**[AI has a multiplying effect on existing technical skills](https://news.ycombinator.com/item?id=48235526)**

Friendly articles and tutorials for front-end web developers. ❤️

⬆️ 337 • 💬 310 • 2d ago • [joshwcomeau.com](https://www.joshwcomeau.com/email/wham-launch-005-elephant-2-p/)

---

**[Italy moves to Airbus A330 tankers](https://news.ycombinator.com/item?id=48248775)**

Rome shifts course: six Airbus A330 MRTT tanker aircraft, worth around €1.39 billion in total, to bolster the European pillar in NATO. #EuropeNews

⬆️ 269 • 💬 106 • 1d ago • [euronews](https://www.euronews.com/my-europe/2026/05/21/italy-moves-to-airbus-a330-tankers-in-major-nato-aligned-shift)

---

**[Is AI Profitable Yet?](https://news.ycombinator.com/item?id=48243863)**

⬆️ 254 • 💬 197 • 1d ago • [isaiprofitable.com](https://isaiprofitable.com/)

---

**[Samsung chip workers will get an average $340k bonus as AI profits soar](https://news.ycombinator.com/item?id=48230892)**

The South Korean chipmaker struck a last-minute deal with its union to avert an 18-day strike, unlocking a $26.6 billion payout pool

⬆️ 251 • 💬 196 • 2d ago • [Quartz](https://qz.com/samsung-chip-workers-bonus-ai-profits-052126)

---

**[Microsoft reports AI is more expensive than paying human employees](https://news.ycombinator.com/item?id=48244434)**

Companies are racing to incentivize employees to use AI. But as some companies are finding, the more employees that use the technology, the heavier the bill.

⬆️ 227 • 💬 66 • 1d ago • [Fortune](https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/)

---

**[The Companies Cutting Headcount for AI Will Lose to the Ones Who Didn't](https://news.ycombinator.com/item?id=48234547)**

Organisations using AI to cut headcount are making a short-term trade with long-term consequences. The ones holding their teams together and investing in how those teams operate with AI are building something more durable.

⬆️ 202 • 💬 201 • 2d ago • [libertas.software](https://libertas.software/en/knowledge-hub/19/the-companies-cutting-headcount-for-ai-will-lose-to-the-ones-who-didnt)

---

**[Don't just paste the AI at me](https://news.ycombinator.com/item?id=48242648)**

If someone asks you a question, paste your answer — not the chatbot's.

⬆️ 180 • 💬 113 • 1d ago • [dontquotetheai.com](https://dontquotetheai.com/)

---

**[Models.dev: open-source database of AI model specs, pricing, and capabilities](https://news.ycombinator.com/item?id=48241172)**

An open-source database of AI models. Contribute to anomalyco/models.dev development by creating an account on GitHub.

⬆️ 156 • 💬 27 • 1d ago • [GitHub](https://github.com/anomalyco/models.dev)

---

**[1940 Air Terminal Museum Begins Liquidation](https://news.ycombinator.com/item?id=48238568)**

We own 3 full size, full motion simulators and they are available for purchase:  Southwest's first 737-200 simulator - donated by Southwest Beechcraft King Air 200 - donated by FlightSafety Hawker 700 - donated by FlightSafety  Each of these comes with all the associated computer cabinets that was u

⬆️ 130 • 💬 31 • 1d ago • [1940 Air Terminal Museum](https://www.1940airterminal.org/news/liquidation-of-simulators)

---

---

## YouTube Videos: "ai"

**[Zuckerberg Caught On SECRET RECORDING:Forcing Employees To Train Their AI Replacements! ](https://www.youtube.com/watch?v=uNrjuGENu44)**

Leaked audio from a Meta all-hands meeting reveals Mark Zuckerberg telling employees that the company is training AI models ...

📺 The Jimmy Dore Show

👁️ 113K • 👍 9K • 💬 2K • ⏱️ 15:52 • 21h ago

---

**[Figure 03 AI Robot Reveals Its UNFAIR Advantage… Humans Can’t Match It](https://www.youtube.com/watch?v=NPOqqDASRCA)**

A 22-year-old intern just beat a humanoid robot… but this might be the LAST time a human wins like this. In Figure AI's wild Man ...

📺 The AI Nexus

👁️ 5K • 👍 148 • 💬 26 • ⏱️ 18:21 • 15h ago

---

**[The singularity is near: Google unveils next phase of AI](https://www.youtube.com/watch?v=zvJ5KfNjOCk)**

ABC News' Nathan Rousseau Smith travels to Google I/O where the search giant unveiled AI agent Gemini Spark, new smart ...

📺 ABC News

👁️ 95K • 👍 2K • 💬 335 • ⏱️ 5:06 • 1d ago

---

**[How to Make AI Music Videos with Perfect Lip Sync](https://www.youtube.com/watch?v=7ajVhp8qM3U)**

Create Your Own Music Videos with Perfect Lip Sync on Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=isa15 In this video, ...

📺 Isa does AI

👁️ 6K • 💬 1 • ⏱️ 8:51 • 5h ago

---

**[AI Just Crossed The Line We Were Afraid Of: Continual Harness](https://www.youtube.com/watch?v=qCFyprzrCvA)**

Princeton researchers just revealed Continual Harness, a self-improving AI system that learns while it is already running.

📺 AI Revolution

👁️ 34K • 👍 2K • 💬 176 • ⏱️ 13:31 • 1d ago

---

**[I Found ALL Paid AI Video Tools in One Place — FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=hFnoAAd-pkQ)**

Try Higgsfield here and create cinematic AI videos with top models in one place → https://higgsfield.ai/s/general-malvaai-jupaTB ...

📺 Malva AI

👁️ 3K • 👍 237 • 💬 41 • ⏱️ 8:13 • 6h ago

---

**[Google’s AI endgame is here… everything you missed at I/O 2026](https://www.youtube.com/watch?v=9OQ5vaYbGV0)**

Try using Emergent's specialized agents in parallel to build any full-stack application ...

📺 Fireship

👁️ 662K • 👍 20K • 💬 1K • ⏱️ 5:44 • 2d ago

---

**[How to use Google OMNI 🤩 VERY EASY 🔥 New AI Video Model #ai #omni](https://www.youtube.com/watch?v=ikWmASLeCYU)**

Google just launched a brand-new AI video tool — and it could completely change the future of video editing. Link: ...

📺 Raj Photo Editing and Much More

👁️ 28K • 👍 2K • 💬 129 • ⏱️ 7:38 • 11h ago

---

**[Don&#39;t Buy AI Bath Bombs](https://www.youtube.com/watch?v=uocwJAi2y_U)**

Get your $10 sign-up bonus at http://privacy.com/pleasantgreen. You can use it on your first purchase! Privacy has a free plan with ...

📺 Pleasant Green

👁️ 441K • 👍 21K • 💬 2K • ⏱️ 10:02 • 1d ago

---

**[Microsoft Can’t Afford AI. Starbucks Can’t Trust It! #ai #anthropic #openai #claude #aibubble](https://www.youtube.com/watch?v=zzNyQxHWPnM)**

The Microsoft Anthropic situation is even weirder, microsoft hosts claude on azure, uses claude inside 365 copilot, has a $30 ...

📺 Mayankshah

👁️ 105K • 👍 4K • 💬 76 • ⏱️ 1:42 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 1,474 • ❤️ 740 • 1d ago

---

**[Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)**

*Tencent*

Hy-MT2-1.8B is a fast, 1.8B parameter multilingual translation model supporting 33 languages, optimized for on-device deployment with 1.25-bit quantization (440MB storage, 1.5x speedup). It excels in general, business, and instruction-following translation tasks, outperforming mainstream commercial APIs.

`translation` `2.0B`

⬇️ 4,534 • ❤️ 532 • 2d ago

---

**[Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)**

*Tencent*

Hy-MT2-30B-A3B is a large-scale (30B parameters, MoE) multilingual translation model supporting 33 languages. It excels in general, business, and instruction-following translation tasks, outperforming leading open-source models and commercial APIs.

`translation` `30.1B`

⬇️ 1,243 • ❤️ 303 • 2d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 43,119 • ❤️ 638 • 6d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 6,032 • ❤️ 291 • 4d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 84,346 • ❤️ 267 • 3d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, featuring a prompt enhancer for improved input processing and supporting various LTX 2.3 formats.

`text-to-video` `9.0B`

⬇️ 1,331,058 • ❤️ 1,318 • 2d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for on-device image and video understanding, offering strong foundation and multimodal capabilities with mixed visual token compression for flexible speed/accuracy trade-offs.

`image-text-to-text` `1.3B`

⬇️ 269,589 • ❤️ 917 • 5d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter causal language model with vision capabilities, optimized for faster inference via MTP. It excels at agentic coding, reasoning, and handling extended contexts up to 1M tokens, making it suitable for complex development workflows and iterative tasks.

`image-text-to-text` `27.3B`

⬇️ 660,321 • ❤️ 448 • 4d ago

---

**[command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)**

*Cohere Labs*

Command A+ is a 25B parameter, multilingual, vision-capable LLM optimized for agentic and reasoning tasks. It supports a 128K context window and offers a W4A4 quantization for efficient enterprise deployment.

`image-text-to-text` `125.8B`

⬇️ 5,627 • ❤️ 188 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 80 • 💬 3 • ⭐ 79,016 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://huggingface.co/papers/2605.18739)**

*Yukang Chen, Luozhou Wang, Wei Huang et al. (16 authors)*

🏢 NVIDIA

LongLive-2.0 presents an NVFP4-based parallel infrastructure for long video generation that addresses training and inference bottlenecks through sequence-parallel autoregressive training and diffusion model tuning.

▲ 108 • 💬 3 • ⭐ 1,935 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18739) • [💻 code](https://github.com/NVlabs/LongLive) • [🔗 project](https://nvlabs.github.io/LongLive/LongLive2/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 64,686 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,449 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://huggingface.co/papers/2605.18678)**

*Fengyi Fu, Mengqi Huang, Shaojin Wu et al. (13 authors)*

🏢 bytedance-research

Lance is a unified multimodal model that combines understanding, generation, and editing capabilities for images and videos through collaborative multi-task training and a dual-stream architecture.

▲ 72 • 💬 4 • ⭐ 818 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18678) • [💻 code](https://github.com/bytedance/Lance) • [🔗 project](https://lance-project.github.io/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 74,700 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation](https://huggingface.co/papers/2605.19833)**

*Zhifei Xie, Kaiyu Pang, Haobin Zhang et al. (7 authors)*

🏢 National University of Singapore

Mega-ASR framework improves robustness in real-world speech recognition through compound-data construction and progressive acoustic-to-semantic optimization techniques.

▲ 127 • 💬 3 • ⭐ 448 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.19833) • [💻 code](https://github.com/xzf-thu/Mega-ASR) • [🔗 project](https://xzf-thu.github.io/Mega-ASR/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 8 • 💬 0 • ⭐ 18,582 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 120 • 💬 10 • ⭐ 10,503 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 4 • 💬 1 • ⭐ 5,609 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 4.8k • 🔱 489 • 2d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.5k • 🔱 1.1k • 7d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.6k • 🔱 178 • 5h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.3k • 🔱 387 • 2d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.2k • 🔱 346 • 7d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.1k • 🔱 463 • 3d ago

---

**[Nutlope/hallmark](https://github.com/Nutlope/hallmark)**

Anti-AI-slop design skill for Claude Code, Cursor, and Codex.

`CSS`

⭐ 1.8k • 🔱 119 • 3d ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.8k • 🔱 213 • 17d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.7k • 🔱 184 • 3d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 1.7k • 🔱 117 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
