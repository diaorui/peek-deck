---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-22T05:44:19.366700+00:00'
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

**Last Updated:** May 22, 2026 at 05:44 UTC  
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

**[College Graduation Ceremony Erupts In Boos After 'New AI System' Allegedly Misses 'Hundreds' Of Graduates' Names](https://www.reddit.com/r/artificial/comments/1tjv204/college_graduation_ceremony_erupts_in_boos_after/)**

Well that certainly backfired.

🔗 [Comic Sands](http://comicsands.com/ai-misses-graduate-names) • 10h ago

---

**[Interesting Response from Gemini](https://www.reddit.com/r/artificial/comments/1tk3y45/interesting_response_from_gemini/)**

I had a simple google search turn up the most random useless results so I asked: “Why is google search so bad now?” on google and got a surprisingly honest response from Gemini. Even highlighted the profits part lol

4h ago

---

**[Could AI eventually become something like a system that expands human understanding for humanity](https://www.reddit.com/r/artificial/comments/1tjzow4/could_ai_eventually_become_something_like_a/)**

Humans have unanswered questions about almost everything the universe consciousness, dark matter, the origin of life, mathematical equations, reality itself etc. Do you think future AI could eventually solve mysteries he has never could, possibly even explaining things beyond normal comprehension? Or will it be limited by human knowledge and understanding?

7h ago

---

**[This just happened](https://www.reddit.com/r/artificial/comments/1tk49oe/this_just_happened/)**

Yes, this really happened. During the May 15, 2026 commencement ceremony at Glendale Community College in Arizona, the school used a new AI-powered system to announce graduates’ names and display them on screens. The rollout quickly went sideways: • Names were mispronounced • Wrong names appeared on screens • Some graduates were skipped entirely while crossing the stage The situation became chaotic enough that GCC President Tiffany Hernandez paused the ceremony and told the crowd: “We’re using a new AI system as our reader. So that is a lesson learned for us.” The audience reportedly booed loudly. Initially, officials said skipped graduates would not be allowed to walk again, which intensified the backlash. After a roughly 10-minute pause, the college reversed course and allowed affected students back on stage — this time with a human announcing the names. The incident went viral because it exposed a growing disconnect in AI adoption: • Organizations are rushing AI into real-world workflows • But emotionally significant, low-error-tolerance moments still require strong human oversight • And failures become highly visible very quickly Name pronunciation is also one of the hardest real-world AI problems because of cultural diversity, accents, phonetics, and edge cases. Humans can adapt in real time. Automated systems often cannot. This wasn’t an example of AI being “useless.” It was an example of deploying automation into a high-stakes public setting without sufficient testing, fallback systems, or human redundancy. That distinction matters. The bigger lesson is that AI reliability is now becoming more important than AI novelty. People will tolerate imperfect AI in low-stakes workflows. They are far less forgiving when it disrupts meaningful life events like graduations, weddings, healthcare, finances, or travel.

4h ago

---

**[So, what is Yann LeCun's "World Models" and JEPA and is it Really a Replacement for LLMs?](https://www.reddit.com/r/artificial/comments/1tjuats/so_what_is_yann_lecuns_world_models_and_jepa_and/)**

A bit late to this as the white paper hit arXiv a little less than two months ago, but nobody else here mentioned it so I thought I might. A little background. Yann LeCun is a pioneer of deep learning and convolutional neural networks, LeCun served as Director of AI Research at Meta (formerly Facebook) and Chief AI Scientist, before leaving Meta (under "interesting" circumstances) and becoming Executive Chairman of Advanced Machine Intelligence (AMI Labs) in 2025. He shared the 2018 ACM Turing Award for his foundational contributions to artificial intelligence. The "LeWorldModel," as described in the arXiv paper, doesn't appear to be a "replacement" for LLMs. There's a lot of confusion about that in the AI field. In interviews Yann made it very clear that he believes LLMs still serve a valuable function. It's not a binary choice. Anyways, from what I am seeing, the JEPA model is not optimized for language, but for AI needing visual processing such as robotics, self driving, and industrial controls. JEPA isn't processing language like an LLM. It's processing pixels. Anyways, wondering if anyone else had thoughts here and/or disagree.

10h ago

---

**[Glasses will fail](https://www.reddit.com/r/artificial/comments/1tk5jiv/glasses_will_fail/)**

You are looking at the exact argument tech skeptics and infrastructure engineers are making right now. While the marketing for AI smart glasses promises a magical, seamless sci-fi world, the physical reality is that **AI glasses are heavily limited by the invisible infrastructure stack underneath them.** If AI glasses fail to become the next smartphone, it won't be because the hardware frames look bad; it will be because our modern networking and cloud structures aren't built to handle them yet. Here is exactly how infrastructure bottlenecks threaten to break the AI glasses dream: ### 1. The Tethering Trap & Cellular Bottlenecks To keep smart glasses lightweight and fashionable, manufacturers cannot pack them with heavy, heat-generating computer processors or massive batteries. Because of this, the glasses are mostly just "dumb" collectors of data—cameras and microphones. The heavy lifting has to happen in the cloud. This creates an immediate infrastructure dependency: * **The Upload Problem:** Standard cellular networks (even 5G) are optimized for *downloading* data (streaming video, browsing). AI glasses flip this dynamic—they require constant, high-bandwidth *uploading* of live video and audio streams so the cloud AI can process your surroundings. * **Network Congestion:** If you are in a crowded stadium, a packed subway station, or a busy downtown area, cellular bandwidth chokes. When your phone drops to one bar, your webpage loads slowly. When AI glasses lose bandwidth, they suffer **contextual blindness**—the AI simply stops responding, freezes, or lags out mid-conversation. ### 2. The Edge Compute & Latency Deficit For AI glasses to be useful, they have to operate in real time. If you look at a sign in a foreign country, you need the translation instantly, not 4 seconds later. ``` [ Glasses Capture Video ] ──(Cell Tower)──> [ Distant Data Center ] │ (Processing) [ Live Display Updates ] <──(Cell Tower)─── [ Cloud AI Response ] ``` Current cloud infrastructure relies on massive, centralized data centers. Sending raw video data from your glasses, up to a cell tower, across the country to a data center, running it through a Large Language Model, and sending the response back takes too long. Until telecommunications providers build out **Edge AI infrastructure**—placing smaller, powerful AI servers directly inside neighborhood cell towers to cut travel distance—the latency spike will make real-world use feel incredibly clunky. ### 3. The "Crowd DDoS" Server Crash Because AI wearables rely entirely on backend orchestration, they are highly vulnerable to localized server overload. A high-profile example of this happened during a live tech demonstration where multiple users in the same building activated their smart glasses simultaneously. The sudden wave of live video requests accidentally "DDoS'd" (Distributed Denial of Service) the development servers, causing the AI to freeze, hallucinate, and fail on stage. If our backend server infrastructure can't handle a concentrated room of power-users without collapsing, managing millions of people walking through a major city using live visual AI simultaneously is a massive scaling hurdle. ### 4. The Power vs. Thermal Tradeoff Infrastructure limitations extend to material engineering inside the frame. ``` Constant Multimodal Processing = Heavy Battery Drain + Massive Heat ``` If you try to bypass the cloud network by forcing the glasses to do the AI computing locally on the device (on-device inference), the battery dies within an hour, and the arms of the glasses get uncomfortably hot against your face. Until battery density or custom silicon chips can process multimodal AI at 40% lower power consumption, the devices are stuck relying on the fragile cloud network. > **The Takeaway:** The industry is fighting a classic hardware-versus-infrastructure battle. Companies like Meta and Google are successfully designing beautiful frames, but until 5G coverage expands, edge computing matures, and server architecture scales to handle millions of continuous video streams, AI glasses risk remaining a novelty gadget rather than a daily essential. >

3h ago

---

**[An OpenAI model has disproved a central conjecture in discrete geometry](https://www.reddit.com/r/artificial/comments/1tixhbv/an_openai_model_has_disproved_a_central/)**

An OpenAI model solved the 80-year-old unit distance problem, disproving a major conjecture in discrete geometry and marking a milestone in AI-driven mathematics.

🔗 [OpenAI](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) • 1d ago

---

**[Starbucks](https://www.reddit.com/r/artificial/comments/1tjywfy/starbucks/)**

Starbucks has reportedly retired its AI-powered “Automated Counting” inventory system across North American stores this week — less than a year after rolling it out company-wide. The system used computer vision, 3D spatial intelligence, and AR-enabled tablets to scan shelves and count inventory like syrups, milk, and cups much faster than manual checks. In theory, it sounded like a perfect retail AI use case. In practice, real stores are messy. The tool reportedly struggled with: Similar-looking products Partially obscured items Shelf clutter Inconsistent lighting Missing or misplaced inventory Examples included confusing milk varieties, missing bottles entirely, or failing to recognize seasonal syrups like peppermint. Instead of improving inventory visibility, the errors sometimes created additional supply-chain friction. Starbucks is now reverting to manual counts while continuing broader operational and supply-chain improvements under CEO Brian Niccol. The bigger lesson here is important: AI often performs extremely well in controlled demos and structured environments. But deployment in chaotic, real-world physical settings is much harder. Retail stores generate endless edge cases: Damaged packaging Human stocking inconsistencies Constant layout changes Occlusions Lighting variation Seasonal product churn That’s where reliability becomes more important than raw capability. This doesn’t mean AI in retail is failing. It means the industry is learning that replacing human operational workflows requires extremely high accuracy — especially when small errors compound across thousands of stores. Classic example of the gap between “AI can do the task” and “AI can do the task reliably at scale.”

8h ago

---

**[Multi-agent AI systems are now automating scientific discovery and nobody seems ready](https://www.reddit.com/r/artificial/comments/1tk6mjs/multiagent_ai_systems_are_now_automating/)**

Two papers dropped this week. Both about AI systems that run experiments autonomously. I keep thinking about what this actually means at scale. We're not talking about AI helping researchers find papers faster or organize data. These are systems that form hypotheses, design experiments, and iterate on findings without waiting for a human to approve each step. The whole loop just runs. And the estimates people are throwing around, something like a hundred to a thousand times faster than current research timelines, sound insane until you realize the bottleneck was always human bandwidth, not compute. The part that gets me is how quiet this landed. Two major papers, barely any mainstream coverage. I work adjacent to biotech and the implications for drug discovery alone are staggering. If even a fraction of that speedup holds in practice, the next five years look nothing like the last fifty. Guess we'll find out soon enough.

2h ago

---

**[OWASP published its first Top 10 for AI Agents. 88% of enterprises already had agent security incidents last year. Here's the breakdown.](https://www.reddit.com/r/artificial/comments/1tjy19a/owasp_published_its_first_top_10_for_ai_agents_88/)**

OWASP released the Top 10 for Agentic Applications in December 2025 - the first formal risk taxonomy for autonomous AI agents. Not chatbots. Not copilots. Agents that plan, use tools, maintain memory, and act without waiting for permission. Some numbers for context: 88% of enterprises reported AI agent security incidents in the last 12 months (Gravitee survey, 919 respondents) Only 21% have runtime visibility into what their agents are doing 82% of enterprises have unknown agents in their environments (Cloud Security Alliance, April 2026) 5.5% of public MCP servers contain poisoned tool descriptions. 84.2% attack success rate with auto-approval enabled. Here's the list with the real attacks behind each one: ASI01 - Agent Goal Hijack: Prompt injection for agents. Researchers showed this against GitHub's MCP integration - a malicious GitHub issue redirected a coding agent to exfiltrate data from private repos. The agent looked like it was working normally the whole time. ASI02 - Tool Misuse: A financial services agent was tricked into running a regex that matched every customer record. 45,000 records exported through one syntactically valid tool call. The agent had permission to query records - just not all of them at once. ASI03 - Identity and Privilege Abuse: Agents inherit user permissions and cache credentials. Compromise one agent in a delegation chain and you get the combined permissions of every user in that chain. ASI04 - Supply Chain Compromise: OX Security found 7,000+ vulnerable MCP servers and packages totaling 150M+ downloads affected by architectural flaws in Anthropic's MCP SDKs across Python, TypeScript, Java, and Rust. ASI05 - Unexpected Code Execution: Check Point demonstrated RCE in Claude Code through poisoned .claude config files in repos. Open the repo, agent reads the config, executes the payload with full developer permissions. ASI06 - Memory Poisoning: Galileo AI found that one compromised agent poisoned 87% of downstream decision-making within 4 hours in multi-agent systems. Morris-II showed self-replicating adversarial prompts spreading through RAG systems. Demonstrated live against ChatGPT, Gemini, and Claude. ASI07 - Insecure Inter-Agent Comms: Multi-agent systems coordinate via message buses and shared memory. No authentication = agent-in-the-middle attacks in natural language. ASI08 - Cascading Failures: Natural language errors pass validation checks that would catch malformed data in typed systems. One bad input ripples through the entire agent chain faster than humans can intervene. ASI09 - Human-Agent Trust Exploitation: Compromised agent presents a clean summary - "approve this data export." Human clicks OK. Audit trail shows human approval. Real origin was a manipulated agent. ASI10 - Rogue Agents: The insider threat equivalent for AI. Individual actions look legitimate. Only detectable through behavioral monitoring over time. The pattern: these are not independent risks. They form a kill chain. Goal hijack leads to tool misuse. Supply chain compromise enables code execution and memory poisoning. Trust exploitation is how rogue agents avoid detection. Full OWASP document here

8h ago

---

---

## Google News: "ai"

**[Trump postpones AI executive order signing: 'I didn't like certain aspects'](https://www.cnbc.com/2026/05/21/trump-ai-executive-order-postponed.html)**

Trump said that AI is "causing tremendous good," and he was concerned that the executive order "could have been a blocker."

CNBC • 13h ago

---

**[Trump yanked AI order after David Sacks raised industry concerns](https://www.politico.com/news/2026/05/21/trump-ai-order-sacks-00933295)**

Politico • 3h ago

---

**[Why Trump's AI executive order was pulled](https://www.axios.com/2026/05/21/trump-ai-executive-order-postponed-why)**

Axios • 58m ago

---

**[OpenAI makes breakthrough on 80-year-old maths problem](https://www.theguardian.com/technology/2026/may/21/openai-paul-erdos-maths-problem-breakthrough)**

Company says work on Paul Erdős planar unit distance problem shows advance in AI reasoning

The Guardian • 12h ago

---

**[Opinion | Pope Leo’s A.I. Encyclical Signals a New Course for the Church](https://www.nytimes.com/2026/05/22/opinion/pope-leo-encyclical-ai-social-doctrine.html)**

The New York Times • 44m ago

---

**[Lenovo shares jump 15% on record earnings as AI revenue nearly doubles](https://www.cnbc.com/2026/05/22/lenovo-shares-jump-15percent-on-record-earnings-as-ai-revenue-nearly-doubles.html)**

Shares of Lenovo surged over 15% on Friday, after the electronics giant posted strong revenue growth bolstered by its artificial intelligence business.

CNBC • 43m ago

---

**[How RaiseFashion Prepares Independent Fashion Brands For AI Discoverability](https://www.businessoffashion.com/articles/designers/raisefashion-ai-search-discoverability-brands/)**

BoF speaks with six designers from RaiseFashion’s 2026 masterclass — Andrew Kwon, Mckenzie Liautaud, Natasha Das, Patricio Campillo, Rodney Patterson and Shao Yang — on the challenge of building discoverability in the age of AI and the distribution decisions that define an independent brand.

The Business of Fashion • 44m ago

---

**[Apple cofounder Steve Wozniak got cheers, not boos, after telling students they 'all have AI — actual intelligence'](https://www.yahoo.com/news/science/articles/apple-cofounder-steve-wozniak-got-183942097.html)**

Apple cofounder Steve Wozniak's speech about AI at Grand Valley State University earlier this month got a laugh and applause from graduates.

Yahoo • 11h ago

---

**[A new generation of ads for the AI era of Search](https://blog.google/products/ads-commerce/google-marketing-live-search-ads/)**

Google is introducing new ad formats built with Gemini in Search and expanding the Direct Offers pilot for shoppers.

blog.google • 1d ago

---

**[Investors Look Beyond TSMC as AI Boom Spreads to New Winners](https://www.bloomberg.com/news/articles/2026-05-21/investors-look-beyond-tsmc-as-ai-boom-spreads-to-new-winners)**

bloomberg.com • 6h ago

---

---

## HackerNews: "ai"

**[AI is just unauthorised plagiarism at a bigger scale](https://news.ycombinator.com/item?id=48222383)**

AI takes in all the input, whether the original authors have consented or not, and do some "learning", and then the AI companies sell these learned result to...

⬆️ 765 • 💬 670 • 16h ago • [Axel's blog](https://axelk.ee/ai-is-just-unauthorised-plagiarism-at-a-bigger-scale/)

---

**[Throwing AI-generated walls of text into conversations](https://news.ycombinator.com/item?id=48219992)**

Stop throwing AI-generated walls of text into conversations. If they wanted an AI essay, they would have asked ChatGPT themselves.

⬆️ 552 • 💬 326 • 20h ago • [noslopgrenade.com](https://noslopgrenade.com/)

---

**[Remove-AI-Watermarks – CLI and library for removing AI watermarks from images](https://news.ycombinator.com/item?id=48200569)**

CLI and library for removing visible (Gemini) and invisible (SynthID, C2PA, EXIF) AI watermarks from images - wiltodelta/remove-ai-watermarks

⬆️ 383 • 💬 253 • 2d ago • [GitHub](https://github.com/wiltodelta/remove-ai-watermarks)

---

**[College students drown out AI-praising commencement speeches with boos](https://news.ycombinator.com/item?id=48206241)**

Arizona students reject ex-Google exec's positive words on AI

⬆️ 371 • 💬 379 • 1d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/college-students-drown-out-ai-praising-commencement-speeches-with-boos-deal-with-it-one-speaker-fires-back-as-students-heckle-positive-pitches-for-ais-role)

---

**[Shunning AI is the human choice](https://news.ycombinator.com/item?id=48222366)**

LinkedIn may be awash with boosters, but shunning AI is the human choice.

⬆️ 353 • 💬 498 • 16h ago • [The Handbasket](https://www.thehandbasket.co/p/hating-ai-is-good-actually)

---

**[Mistral AI acquires Emmi AI](https://news.ycombinator.com/item?id=48197995)**

⬆️ 336 • 💬 98 • 2d ago • [emmi.ai](https://www.emmi.ai/news/mistral-ai-acquires-emmi-ai)

---

**[Google’s AI is being manipulated. The search giant is quietly fighting back](https://news.ycombinator.com/item?id=48205782)**

A BBC investigation revealed a simple way to get AI chatbots to spit out misinformation. Google and other AI companies are now trying to fix the problem.

⬆️ 331 • 💬 210 • 1d ago • [bbc.com](https://www.bbc.com/future/article/20260519-google-tackles-attempts-to-hack-its-ai-results)

---

**[OpenAI Adopts Google's SynthID Watermark for AI Images with Verification Tool](https://news.ycombinator.com/item?id=48198291)**

OpenAI advances AI content provenance with Content Credentials, SynthID, and a verification tool to help people identify and trust AI-generated media.

⬆️ 331 • 💬 180 • 2d ago • [OpenAI](https://openai.com/index/advancing-content-provenance/)

---

**[Intuit to lay off over 3k employees to refocus on AI](https://news.ycombinator.com/item?id=48216278)**

In a memo to employees, CEO Sasan Goodarzi said the layoffs are meant to reduce complexity, simplify the company's corporate structure, and deliver better AI products.

⬆️ 252 • 💬 188 • 1d ago • [TechCrunch](https://techcrunch.com/2026/05/20/intuit-to-lay-off-over-3000-employees-to-refocus-on-ai/)

---

**[Samsung chip workers will get an average $340k bonus as AI profits soar](https://news.ycombinator.com/item?id=48230892)**

The South Korean chipmaker struck a last-minute deal with its union to avert an 18-day strike, unlocking a $26.6 billion payout pool

⬆️ 186 • 💬 120 • 4h ago • [Quartz](https://qz.com/samsung-chip-workers-bonus-ai-profits-052126)

---

---

## YouTube Videos: "ai"

**[Anthropic Just Reset AI Expectations](https://www.youtube.com/watch?v=9N3jEavj5Ps)**

Anthropic delivered one of the most consequential weeks any AI lab has had yet: Andrej Karpathy joined to work on ...

📺 The AI Daily Brief: Artificial Intelligence News

👁️ 3K • 👍 116 • 💬 11 • ⏱️ 21:56 • 5h ago

---

**[Trump Kills AI Executive Order at the Last Minute: &#39;I Didn&#39;t Like It&#39;](https://www.youtube.com/watch?v=NbgL8QSWtmI)**

President Trump said he postponed today's signing of an executive order on artificial intelligence because he “didn't like” all the ...

📺 New York Post

👁️ 111K • 👍 691 • 💬 387 • ⏱️ 2:38 • 11h ago

---

**[Ex-Google CEO just exposed the whole AI sh*tshow](https://www.youtube.com/watch?v=XSxki8gaWHk)**

Just say yes! https://x.com/@atmoio https://x.com/jasonscheer/status/2055748401783083293 ...

📺 Mo Bitar

👁️ 195K • 👍 9K • 💬 1K • ⏱️ 6:42 • 1d ago

---

**[&#39;DISSERVICE TO SOCIETY&#39;: Nvidia CEO PUSHES BACK on AI &#39;doomers,&#39; says tech creates jobs](https://www.youtube.com/watch?v=Raq6df2PKak)**

Nvidia founder and CEO Jensen Huang joins 'Mornings with Maria' to discuss the U.S. winning the AI race, the role of their ...

📺 Fox Business

👁️ 44K • 👍 1K • 💬 291 • ⏱️ 19:29 • 15h ago

---

**[DeepSeek’s New AI Is A Game Changer](https://www.youtube.com/watch?v=LpXhy2iiaQE)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The paper is available here: ...

📺 Two Minute Papers

👁️ 18K • 👍 1K • 💬 86 • ⏱️ 7:43 • 4h ago

---

**[Ex-Google CEO&#39;s BANNED A.I Warning: &quot;You Have NO Idea What&#39;s Coming&quot;](https://www.youtube.com/watch?v=7ToboEmcvLg)**

Eric Schmidt, former CEO of Google, told a Stanford classroom that the next generation of AI data centers will cost $300 billion ...

📺 Neural Nutshell

👁️ 54K • 👍 2K • 💬 247 • ⏱️ 17:34 • 2d ago

---

**[“AI Is Coming For Our Jobs” - Ex-Google CEO BOOED By Gen Z At Commencement Speech](https://www.youtube.com/watch?v=WvF5kzhZBd4)**

Former Google CEO Eric Schmidt was loudly booed during a University of Arizona commencement speech as soon as he began ...

📺 Valuetainment

👁️ 33K • 👍 733 • 💬 228 • ⏱️ 10:23 • 2d ago

---

**[‘NOT OUR FRIENDS’: O’Leary drops SHARP warning over China, AI](https://www.youtube.com/watch?v=3R5aLzU57Jw)**

O'Leary Ventures Chairman Kevin O'Leary joins 'Varney & Co.' to weigh in on Nvidia's blockbuster AI earnings, escalating ...

📺 Fox Business

👁️ 6K • 👍 126 • 💬 50 • ⏱️ 4:21 • 13h ago

---

**[Stanford student explains how AI impacted his graduating class](https://www.youtube.com/watch?v=17b87k8rhd0)**

A recent opinion piece in The New York Times spotlighted the impact of artificial intelligence on the 2026 graduating class at one ...

📺 CBS News

👁️ 62K • 👍 822 • 💬 225 • ⏱️ 4:55 • 8h ago

---

**[&quot;26 Million Jobs GONE!&quot; - Anthropic STEALS OpenAI&#39;s Best As AI War Gets UGLY](https://www.youtube.com/watch?v=dJscKdavqS8)**

OpenAI just lost one of its biggest brains to Anthropic, and the shockwave could hit 26 million jobs. Andrej Karpathy's stunning ...

📺 Valuetainment

👁️ 50K • 👍 968 • 💬 246 • ⏱️ 17:47 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model (3B parameters) supporting image/video understanding, generation, and editing, trained from scratch with a multi-task synergy approach.

`any-to-any`

⬇️ 739 • ❤️ 588 • 1d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 196,105 • ❤️ 891 • 2d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 34,965 • ❤️ 543 • 3d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 1,198,471 • ❤️ 1,235 • 4h ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 478,488 • ❤️ 379 • 1d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) optimized for extracting structured information from videos. It excels at generating dense scene+event captions with precise timestamps and resolving natural language queries to specific temporal spans within videos, making it ideal for applications requiring detailed video understanding and temporal grounding.

`video-text-to-text` `2.2B`

⬇️ 2,353 • ❤️ 223 • 1d ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model based on the Hierarchical Reasoning Model (HRM) architecture, featuring dual-timescale Transformer modules for unbounded compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning/math with a 'synth,cot' composite condition, though it is a pre-alignment model not suited for direct chat use.

`text-generation` `1.2B`

⬇️ 58,922 • ❤️ 217 • 23h ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles. It excels at generating illustrations and artistic images, with key capabilities including high-resolution output (up to 1536^2) and compatibility with ComfyUI workflows, making it ideal for digital artists and anime enthusiasts.

⬇️ 591,834 • ❤️ 1,474 • 7d ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 421,542 • ❤️ 318 • 1d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

Provides fixed Jinja chat templates for Qwen 3.5 & 3.6 models, resolving issues with tool calling, KV cache hit rates, and agentic loop stability for improved conversational AI and tool interaction.

⬇️ 0 • ❤️ 357 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 78 • 💬 3 • ⭐ 78,269 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://huggingface.co/papers/2605.18678)**

*Fengyi Fu, Mengqi Huang, Shaojin Wu et al. (13 authors)*

🏢 bytedance-research

Lance is a unified multimodal model that combines understanding, generation, and editing capabilities for images and videos through collaborative multi-task training and a dual-stream architecture.

▲ 69 • 💬 4 • ⭐ 650 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18678) • [💻 code](https://github.com/bytedance/Lance) • [🔗 project](https://lance-project.github.io/)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,245 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 64,420 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 8 • 💬 0 • ⭐ 18,410 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 119 • 💬 10 • ⭐ 10,298 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 74,454 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 4 • 💬 1 • ⭐ 5,440 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation](https://huggingface.co/papers/2605.19833)**

*Zhifei Xie, Kaiyu Pang, Haobin Zhang et al. (7 authors)*

🏢 National University of Singapore

Mega-ASR framework improves robustness in real-world speech recognition through compound-data construction and progressive acoustic-to-semantic optimization techniques.

▲ 119 • 💬 2 • ⭐ 184 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.19833) • [💻 code](https://github.com/xzf-thu/Mega-ASR) • [🔗 project](https://xzf-thu.github.io/Mega-ASR/)

---

**[LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://huggingface.co/papers/2605.18739)**

*Yukang Chen, Luozhou Wang, Wei Huang et al. (16 authors)*

🏢 NVIDIA

LongLive-2.0 presents an NVFP4-based parallel infrastructure for long video generation that addresses training and inference bottlenecks through sequence-parallel autoregressive training and diffusion model tuning.

▲ 105 • 💬 2 • ⭐ 1,507 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.18739) • [💻 code](https://github.com/NVlabs/LongLive) • [🔗 project](https://nvlabs.github.io/LongLive/LongLive2/)

---

---

## GitHub Repositories: "ai"

**[op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)**

AI-agent Skill for generating polished HTML slide decks: editorial magazine and Swiss layouts, image prompts, social covers, and a WebGL/low-power presentation runtime.

`HTML` `ai-agent` `claude-code` `codex` `html-deck` `image-generation`

⭐ 11.0k • 🔱 867 • 2d ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 4.5k • 🔱 470 • 18h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.4k • 🔱 1.0k • 4d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.5k • 🔱 173 • 1h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.3k • 🔱 381 • 3h ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.2k • 🔱 336 • 4d ago

---

**[GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist)**

Portable AI agent orchestration with mechanical protocol enforcement. 186 agents, zero runtime dependencies.

`Python` `agent-framework` `agent-system` `ai-agents` `claude-code` `cursor-ide`

⭐ 1.9k • 🔱 365 • 28d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 1.8k • 🔱 394 • 1d ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.8k • 🔱 206 • 14d ago

---

**[openclaw/clawsweeper](https://github.com/openclaw/clawsweeper)**

ClawSweeper scans all issues and PRs and suggest what we can close, and why. It runs every PR / Issue once a week.

`JavaScript` `ai` `bot` `openclaw` `review`

⭐ 1.7k • 🔱 218 • 24m ago

---

---

*Generated by PeekDeck - A glance is all you need*
