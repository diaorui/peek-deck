---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-01T20:16:08.748072+00:00'
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

**Last Updated:** November 01, 2026 at 20:16 UTC  
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

**[Trump’s achilles heel is turning his own voters against him](https://www.reddit.com/r/artificial/comments/1xl4wds/trumps_achilles_heel_is_turning_his_own_voters/)**

Lifelong Republicans are campaigning against the spread of data centres

🔗 [The i Paper](https://inews.co.uk/news/world/destroying-homes-trump-voters-turn-against-data-centres-4862641) • 5h ago

---

**[Like AI, we have had access to great computing power, all types of open and closed source softwares for decades. Still most people aren't even using Excel fully. AI is capable but most people won't use it as well for most use cases](https://www.reddit.com/r/artificial/comments/1xlah5b/like_ai_we_have_had_access_to_great_computing/)**

In this way AI is very overrated. 99% of even office users are basic excel users. We have had open source databases, rbdms, Hadoop and what not. Frankly most people don't even need AI

1h ago

---

**[Anthropic's Claude AI blocks video game cloning and reverse-engineering — sweeping new restrictions also hit legitimate developers and basic troubleshooting tasks](https://www.reddit.com/r/artificial/comments/1xkibsh/anthropics_claude_ai_blocks_video_game_cloning/)**

Many game developers are reporting Claude's refusal to work on their own projects.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked) • 1d ago

---

**[‘If it wasn’t for ChatGPT my brother would still be alive’: inside OpenAI’s safety unit](https://www.reddit.com/r/artificial/comments/1xkzv9y/if_it_wasnt_for_chatgpt_my_brother_would_still_be/)**

An Observer investigation reveals how OpenAI’s race for dominance has compromised user safety, with conversational AI linked to psychiatric crises and violence

🔗 [The Observer](https://observer.co.uk/news/technology/article/if-it-wasnt-for-chatgpt-my-brother-would-still-be-alive-inside-openais-safety-unit) • 9h ago

---

**[X/Twitter makes AI dev look effortless, but I keep burning tokens on unfinished projects. How are you actually shipping full apps?](https://www.reddit.com/r/artificial/comments/1xl815r/xtwitter_makes_ai_dev_look_effortless_but_i_keep/)**

Hey everyone, I need a real sanity-check on my workflow, because I feel like I'm being scammed. 😅 To get some contacts every single day on X, Insta, and TikTok, I see people posting demo videos of insanely cool, bespoke software, sleek data visualizations, and full-stack side projects they supposedly "built in 2 hours completely with AI." It makes me hyped and really optimistic for the future, and for tech as a whole. Howevr when I actually sit down to build anything beyond a MVP or lightweight component, I hit an invisible wall or something…. Ok if I had to break it down, I’ll first get honey potted, or stuck in the honeymoon phase. I’ll start building with Claude and/or Codex (depending on the project but at this point they’re pretty much the same). I’ll go through the steps of setting up the scaffold, initial architecture, and base feature set goes insanely fast. Then boom at some point I’ll hit a wall; or like a 80/20 trap, I’ll try pushing the project into a complete, polished, end-to-end product, but it never gets there. Then I end up in a token burn hell where I’m just burning through tokens, and context windows while the project completely stalls on the roadmap. I'm following standard prompt engineering practices, using system prompts, modular files, etc., but it feels like the model gets "tired" or bogged down once the codebase grows past a certain complexity. For the folks in here who are actually shipping full applications to production using LLMs: Is everyone on social media just showing off slick 30-second prototypes that are actually broken under the hood? What is your actual stack/workflow for pushing past that mid-project context degradation? Are you using spec-driven development (like custom system prompts, codebase indexing tools, or sub-agent architecture), or are you still dropping back into hand-coding the last 20%? Would appreciate any tips, workflow breakdowns, or brutal honesty. Cheers! Sidenote: if you guys have built any cool projects with AI, and are willing to share with me please feel free to :) I love stuff like that.

3h ago

---

**[DeepSeek open-sources a super-agent coding prototype: one Router, many Workers, minimal human attention](https://www.reddit.com/r/artificial/comments/1xlc9ye/deepseek_opensources_a_superagent_coding/)**

On October 31, the DeepSeek Harness team published a design essay, Exploring Super-agent Design: Towards a More Autonomous Agent System, alongside an MIT-licensed research prototype called dsh-superagent-prototype. The idea is not a new foundation model. It is orchestration around existing model-powered tools, built for one GitHub repository. A persistent Router session handles incoming conversations and dispatch decisions, but does not do the work itself. Each accepted work item gets its own Worker session and directory, so tasks run in parallel without sharing context. The prototype listens to GitHub events, and optionally to Feishu messages, and returns results in the original conversation, often as a pull request. A local web panel lists only the decisions that need a human. The stated philosophy is blunt: take as little human attention as possible, and give as much value as possible. The agent is supposed to confirm once, stay quiet while working, and speak again only with a result, a question, or a failure. It should act only when an allowed person asks, or when a team-written rule permits the work. For work it merely infers, the documented default is observe-only: record what it would do, do not execute it. DeepSeek's argument is that human attention, not model capability, is now the bottleneck. The team says a person can actively follow only 3 to 5 agent sessions at once. In its own simulated test, with about 300 messages and about 20 real work requests per run, the super-agent approach finished the slowest 5 percent of tasks in 15.7 minutes, versus 29.5 minutes for a single-session baseline. Treat those numbers as self-reported, not as an independent benchmark. The test used synthetic messages and simulated tools, real coding quality was not measured, and there is no verified comparison with Claude Code or Codex yet. DeepSeek is also unusually clear about the prototype limits: it is research code, not an official product and not production-ready, it may contain bugs, it differs from the internal system, and some essay ideas are future directions, not implemented features. The internal instance is reportedly already used for bug reproduction, code review, and Harness work, but that is the team's claim. Discussion: is a Router plus Workers the right split, or just parallel sessions with a nicer name? And where would you draw the line on proactive work? Would you let an agent open pull requests in your repository, and what permissions and team-written rules would you require before it touches anything? Sources: DeepSeek dsh-superagent-prototype on GitHub; reporting on October 31 by MarkTechPost (https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/) and Venture Atlas (https://www.ventureatlas.org/news/2026-10-31-deepseek-superagent).

37m ago

---

**[Dear Sam, My RAM Is None of Your Business.](https://www.reddit.com/r/artificial/comments/1xkmtyp/dear_sam_my_ram_is_none_of_your_business/)**

Well, the last time I looked, how much RAM we have in our personal computers was still a democratic decision, not a decree from Silicon Valley. Next, Sam Altman will be telling us what we're allowed to have for breakfast. Or perhaps that's the big announcement on next week's podcast. Honestly, whatever happened to simply minding your own business?

22h ago

---

**[Working on a research framework for intelligence beyond infrastructure and looking for honest feedback](https://www.reddit.com/r/artificial/comments/1xl59a7/working_on_a_research_framework_for_intelligence/)**

I have been working on a research project called Organic Intelligence Protocol, or OIP. The idea started with a question I kept coming back to. Are we evaluating intelligence fairly when access to infrastructure and resources can influence how capable a system appears to be? OIP is my attempt to explore that question through concepts such as infrastructure independence, grounded feedback, and adaptive moral logic. Over the past few months, I have been documenting the framework, reviewing its mathematical definitions, and auditing its use with four datasets from Bangladesh, Malawi, Uganda, and Ethiopia. The results have been more useful for identifying limitations than for making big claims. The audits did not establish enough evidence to authorize the constructs for further empirical evaluation. Some definitions still need clearer measurement rules, and a variable that looks relevant on paper cannot automatically be treated as a valid measurement. That has changed how I approach the project. Instead of forcing a score or trying to make the framework look complete,, I am keeping unresolved questions open and documenting what the available evidence can and cannot support. OIP is still research in progress. I am not claiming that it is validated or better than existing approaches. I would like to hear from people who have worked on AI evaluation, measurement theory, or empirical research. What would you want to see before taking a framework like this seriously? Where do you think the biggest methodological problems might be? Critical feedback is welcome. I would rather identify a fundamental problem now than build further work on an assumption that has not been tested.

5h ago

---

**[How's your grammar while prompting?](https://www.reddit.com/r/artificial/comments/1xl28yd/hows_your_grammar_while_prompting/)**

I feel like my grammar is awful whenever I write a prompt. It's as if I’ve forgotten everything I learned in school and just type away with terrible grammar, mixing up singular and plural, using the wrong articles, and so on. Am I the only one? Mind you, I'm trilingual, so that might be a factor.

7h ago

---

**[What's One Repetitive Task You Would Automate With AI?](https://www.reddit.com/r/artificial/comments/1xlcntu/whats_one_repetitive_task_you_would_automate_with/)**

I'm a web designer, and one of the most repetitive things in my business is finding new clients. So naturally, email outreach was one of the first things I wanted to automate. But not just regular cold email where you send the same template to thousands of businesses. I use Swokei to find businesses with websites, analyze them for issues with design, SEO, speed, and mobile optimization, and turn those findings into personalized, ready-to-send outreach emails. This way, I'm not just sending random offers. I'm reaching out with something relevant to each business while automating most of the research and writing process. It's made it much easier to keep outreach running consistently without spending hours researching prospects manually. What about you? What's one repetitive task you've automated with AI?

21m ago

---

---

## Google News: "ai"

**[Opinion | Could A.I. Be Conscious? It’s Definitely Possible.](https://www.nytimes.com/2026/11/01/opinion/ai-consciousness-ethics.html)**

The New York Times • 9h ago

---

**[Neoclouds: These firms you've never heard of are feeding fears the AI bubble could burst](https://www.bbc.com/news/articles/cje36degrgv5o)**

The amount of debt held by data centres is measured in the tens of billions of pounds.

BBC • 18h ago

---

**[Microsoft AI chief says AI is not conscious and we should keep it that way](https://www.businessinsider.com/mustafa-suleyman-microsoft-ai-consciousness-2026-11)**

Microsoft AI CEO Mustafa Suleyman said developers should only build AI models that "are not conscious and not deserving of rights."

Business Insider • 31m ago

---

**[AI stocks just lost $5 trillion — but history says the stock market's sweetest stretch starts now](https://finance.yahoo.com/markets/article/ai-stocks-just-lost-5-trillion--but-history-says-the-stock-markets-sweetest-stretch-starts-now-110000768.html)**

October selloffs, like the $5 trillion AI stock wipeout that hit the market, often lead into a sweet spot for traders.

Yahoo Finance • 9h ago

---

**[Why AI is boosting Meta's ad business while hurting Google search](https://www.cnbc.com/2026/11/01/ai-meta-ads-google-search.html)**

The gap between Meta's ad revenue growth and Google's search expansion was the widest it's been since 2021 in the latest quarter.

CNBC • 8h ago

---

**[The Smartest People in AI Believe This Is the World’s Most Important Chart](https://www.wsj.com/tech/ai/ai-anthropic-rsi-recursive-self-improvement-bff4e815)**

WSJ • 1d ago

---

**[‘Let’s take Alexa out into the garden and smash it with a shoe’: Charlie Brooker and Diane Morgan take aim at Hollywood, AI ... and each other](https://www.theguardian.com/tv-and-radio/2026/nov/01/philomena-cunk-on-cinema-charlie-brooker-diane-morgan-interview)**

As deadpan spoof documentarian Philomena Cunk returns with a new series on cinema, her creators discuss meeting J-Lo, their worst ever jobs – and why artificial intelligence is like mad cow disease

The Guardian • 10h ago

---

**[The Year Math Changed Forever](https://www.newyorker.com/magazine/2026/11/09/the-year-math-changed-forever)**

A.I. is solving problems that stumped the field of math for decades. Mathematicians look to Terence Tao for guidance on their altered world.

The New Yorker • 9h ago

---

**[Local mom-and-pops are embracing AI food slop, and residents are revolting](https://www.washingtonpost.com/dc-md-va/2026/11/01/local-mom-and-pops-are-embracing-ai-food-slop-residents-are-revolting/)**

Small businesses in D.C. are getting increasingly called out for using artificial intelligence. The owners have thoughts.

The Washington Post • 2h ago

---

**[South Korea exports nearly double in October on AI investment boom](https://www.reuters.com/world/asia-pacific/south-korea-exports-nearly-double-october-strongest-growth-since-1974-2026-11-01/)**

Reuters • 19h ago

---

---

## HackerNews: "ai"

**[AI isn't replacing SREs, it's deskilling them](https://news.ycombinator.com/item?id=50305693)**

When AI handles 95% of your incident response, do you get worse at handling the 5% that actually matters?

⬆️ 662 • 💬 482 • 2d ago • [newsletter.signoz.io](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling)

---

**[We ran AI agent swarms in Minecraft and Mindustry](https://news.ycombinator.com/item?id=50296486)**

Swarms of Claude and GPT agents in Minecraft and Mindustry.

⬆️ 416 • 💬 170 • 2d ago • [labs.ycombinator.com](https://labs.ycombinator.com/projects/games/index.html)

---

**[Cisco gives engineer unlimited AI tokens to rewrite legacy code](https://news.ycombinator.com/item?id=50304122)**

Meet Paddy, the 27-year-old Cisco’s president calls an “energizer bunny.” He’s been given unlimited AI tokens and told to “go nuts.”

⬆️ 311 • 💬 382 • 2d ago • [Fortune](https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/)

---

**[Proton's CEO Cancels AI 'Re-Interviews'](https://news.ycombinator.com/item?id=50307183)**

The move came after 404 Media published an investigation into how Proton CEO Andy Yen was aggressively pushing AI across Proton despite security concerns and the culture of fear he has created.

⬆️ 295 • 💬 254 • 2d ago • [404 Media](https://www.404media.co/protons-ceo-cancels-ai-re-interviews/)

---

**[US tech stocks see sharp falls over AI cost fears](https://news.ycombinator.com/item?id=50306008)**

Shares in Intel continue to fall while the tech-heavy Nasdaq opens at its lowest level in more than two months.

⬆️ 269 • 💬 299 • 2d ago • [BBC News](https://www.bbc.co.uk/news/articles/cvwy72e0n72yo)

---

**[The AI cost of JavaScript frameworks](https://news.ycombinator.com/item?id=50323088)**

One of my pet peeves with the web development community is that so many of the decisions we make are vibes-based. Frameworks are “blazing fast,” tools will…

⬆️ 248 • 💬 172 • 14h ago • [Read the Tea Leaves](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/)

---

**[Building an AI-native engineering org](https://news.ycombinator.com/item?id=50296730)**

Building an AI-native engineering org

⬆️ 188 • 💬 198 • 2d ago • [X (formerly Twitter)](https://twitter.com/sgondala2/status/2115832070274723875)

---

**[Leaking Secrets from Air-Gap Computers by Spelling Radio Signals from RAM (2024)](https://news.ycombinator.com/item?id=50322022)**

Air-gapped systems are physically separated from external networks, including the Internet. This isolation is achieved by keeping the air-gap computers disconnected from wired or wireless networks, preventing direct or remote communication with other devices or networks. Air-gap measures may be used in sensitive environments where security and isolation are critical to prevent private and confidential information leakage.
  In this paper, we present an attack allowing adversaries to leak information from air-gapped computers. We show that malware on a compromised computer can generate radio signals from memory buses (RAM). Using software-generated radio signals, malware can encode sensitive information such as files, images, keylogging, biometric information, and encryption keys. With software-defined radio (SDR) hardware, and a simple off-the-shelf antenna, an attacker can intercept transmitted raw radio signals from a distance. The signals can then be decoded and translated back into binary information. We discuss the design and implementation and present related work and evaluation results. This paper presents fast modification methods to leak data from air-gapped computers at 1000 bits per second. Finally, we propose countermeasures to mitigate this out-of-band air-gap threat.

⬆️ 166 • 💬 86 • 18h ago • [arXiv.org](https://arxiv.org/abs/2409.02292)

---

**[Ask HN: Are you tired too in this AI era?](https://news.ycombinator.com/item?id=50301479)**

⬆️ 149 • 💬 142 • 2d ago

---

**[AI agent swarms in Minecraft fail to build civilization, drown in bureaucracy](https://news.ycombinator.com/item?id=50325662)**

It is hoped game testing can provide insight into recent AI agent headlines, good and bad.

⬆️ 125 • 💬 60 • 6h ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-agent-swarms-unleashed-in-minecraft-to-build-a-thriving-civilization-50-agent-teams-fail-after-falling-into-paralyzing-bureaucracy)

---

---

## YouTube Videos: "ai"

**[Why Hasn’t The AI Bubble Burst (Yet)?](https://www.youtube.com/watch?v=7rtn4doHIuY)**

So... Why Isn't the AI Bubble Popping? In 2025, OpenAI lost about $1.60 for every $1 it earned just running its business. Yet Big ...

📺 MonkeyExplains

👁️ 286K • 👍 8K • 💬 1K • ⏱️ 13:57 • 6h ago

---

**[I Found An Uncensored AI That Runs on Your PHONE](https://www.youtube.com/watch?v=vbIw44T3yzU)**

In this video I show you how to setup and run a powerful and fast uncensored AI model directly on your iPhone or Android phone.

📺 Mark Gadala-Maria

👁️ 19K • 👍 591 • 💬 55 • ⏱️ 11:28 • 21h ago

---

**[AI&#39;s Own Lenders Just Exposed What It&#39;s Really Worth: Junk](https://www.youtube.com/watch?v=KWgAO7CEy-A)**

Thank you to Mint Mobile for partnering with us on this video! If you like your money, Mint Mobile is for you. Shop plans starting at ...

📺 Brendan Dell 

👁️ 73K • 👍 2K • 💬 509 • ⏱️ 25:02 • 1d ago

---

**[The AI Bubble Is Now A Debt Disaster](https://www.youtube.com/watch?v=ReX-AhNV1RQ)**

Amazon just spent more than $77 billion on AI and saw $42.4b in cash OUTFLOWS. Alphabet has now lost more than $500b in ...

📺 Eurodollar University

👁️ 144K • 👍 2K • 💬 345 • ⏱️ 18:55 • 21h ago

---

**[GPT and Claude Agents Just Started an AI Civilization War](https://www.youtube.com/watch?v=l1L9sezAcxc)**

OpenAI's GPT and Anthropic's Claude just went to war in a massive AI agent experiment, with GPT winning 12 of 16 battles.

📺 AI Revolution

👁️ 72K • 👍 1K • 💬 129 • ⏱️ 13:08 • 18h ago

---

**[Stock Market PANIC After AI Companies Report WORRYING Earnings](https://www.youtube.com/watch?v=upaSZ7QkgHo)**

Google lost roughly $500 billion in market value, and warning signs of an economic collapse are piling up as companies pour ...

📺 The Young Turks

👁️ 214K • 👍 3K • 💬 737 • ⏱️ 13:55 • 1d ago

---

**[Jensen Huang Just Named the Next Wave of AI](https://www.youtube.com/watch?v=oeq8PziWTeo)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *Jensen Huang says the chat window ...

📺 Julia McCoy

👁️ 188K • 👍 3K • 💬 276 • ⏱️ 11:48 • 2d ago

---

**[Half A Trillion Lost In A Day! Is AI Killing Google&#39;s Search Empire? | Firstpost Live](https://www.youtube.com/watch?v=eE8du73bC4M)**

Google is facing a massive AI dilemma. More than $500 billion has been wiped off the market value of its parent company, ...

📺 Firstpost

👁️ 475K • 👍 2K • 💬 307 • ⏱️ 6:26 • 2d ago

---

**[AI Getting Banned](https://www.youtube.com/watch?v=iciXQrtdro8)**

Writer: Brett Stelmaszek Editor: Catlin Stevenson Music by: @UFD-Music.

📺 UFD Tech

👁️ 207K • 👍 17K • 💬 1K • ⏱️ 0:49 • 6h ago

---

**[AI News Is Getting Absolutely RIDICULOUS](https://www.youtube.com/watch?v=UIYoKcIvSVo)**

0:00 Intro 0:57 Black October: the internet under attack 2:23 Banks find rogue AI agents in customer accounts 3:52 Sponsor: ...

📺 TheAIGRID

👁️ 51K • 👍 656 • 💬 63 • ⏱️ 30:27 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)**

*DeepSeek*

DeepSeek-V4.1-Flash-1017 is an image-text-to-text model that enhances reasoning, coding, and agentic tasks with reduced execution time and output length. It excels in benchmarks like HLE, Terminal-Bench, and ProgramBench, offering improved performance-cost efficiency for complex applications.

`image-text-to-text` `763.2B`

⬇️ 170,353 • ❤️ 4,247 • 15d ago

---

**[LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B)**

*Liquid AI*

LFM3-1.7B is a 1.73B parameter text model optimized for edge devices and local agents, featuring a 256K context window and multi-language support. It excels at agentic tasks, tool calling, and domain-specific fine-tuning, with low memory requirements (approx. 1GB at 4-bit precision).

`text-generation` `1.7B`

⬇️ 37,568 • ❤️ 679 • 4d ago

---

**[NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)**

*NVIDIA*

NVIDIA-Nemotron-3.5-Transcribe-30B-A4B is a multilingual speech LLM supporting 40 languages for transcription, speech translation, and audio QA, with a 65,536-token context for long-form audio processing.

`automatic-speech-recognition` `33.7B`

⬇️ 29,364 • ❤️ 583 • 2d ago

---

**[Nanbeige4.3-33B](https://huggingface.co/Nanbeige/Nanbeige4.3-33B)**

*Nanbeige LLM Lab*

Nanbeige4.3-33B is a 33B parameter text-generation model excelling in agentic coding and professional coworker tasks, outperforming comparable open models on benchmarks like Terminal-Bench and JobBench. It's designed for complex coding, professional collaboration, and serves as a teacher model for distilling agentic capabilities into smaller models.

`text-generation` `33.1B`

⬇️ 15,795 • ❤️ 965 • 4d ago

---

**[Mistral-Large-4-1T-A52B](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)**

*Mistral*

Mistral Large 4 is a 1T parameter, natively multimodal Mixture-of-Experts model supporting text and image inputs with a 1M context length. It excels in instruction following, reasoning, coding, and agentic workflows, with strong performance in cybersecurity, finance, and law, and state-of-the-art visual grounding.

`image-text-to-text`

⬇️ 4,576 • ❤️ 1,439 • 3d ago

---

**[Unlimited-OCR-2](https://huggingface.co/baidu/Unlimited-OCR-2)**

*BAIDU*

Unlimited-OCR-2 is a multilingual vision-language model for unlimited-horizon document parsing, achieving state-of-the-art performance on ultra-long documents by using Sparse Reference Sliding Window Attention (SR-SWA) to maintain constant computational complexity regardless of document length.

`image-text-to-text` `3.3B`

⬇️ 109,519 • ❤️ 511 • 3d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of image-to-video, text-to-video, and video-to-video generation, offering advanced control for creative applications.

`image-to-video`

⬇️ 2,431,846 • ❤️ 10,192 • 21d ago

---

**[Qwen3.5-4B-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder)**

*Caio Giovannetti*

Qwen3.5-4B-3D-Coder is a 4B parameter language model fine-tuned for general coding and specifically for generating interactive Three.js 3D scenes. It supports optional vision capabilities to create scenes from reference images.

`4.5B`

⬇️ 44,825 • ❤️ 466 • 2d ago

---

**[Pika-H3-Flex](https://huggingface.co/Pika-Labs/Pika-H3-Flex)**

*Pika-Labs*

Pika-H3-Flex is an image-to-video diffusion model that generates high-fidelity, temporally coherent videos from static images. It excels at precise camera motion control, maintaining subject consistency, and adapting to various artistic styles, making it ideal for creative video production and visual storytelling.

`image-to-video` `33.1B`

⬇️ 404 • ❤️ 303 • 2d ago

---

**[flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy)**

*Black Forest Labs*

FLUX 3 Image Klein is a 5.6B parameter model for ComfyUI enabling text-to-image generation and advanced image editing with multi-reference composition and bounding box control. It utilizes Qwen3-VL-4B-Instruct as its text encoder and supports features like text rendering within images.

`image-to-image`

⬇️ 970,633 • ❤️ 2,250 • 15d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 7 • 💬 2 • ⭐ 3,519 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 161 • 💬 6 • ⭐ 119,380 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 84 • 💬 4 • ⭐ 21,794 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 62 • 💬 4 • ⭐ 44,937 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 31 • 💬 9 • ⭐ 8,904 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 103 • 💬 7 • ⭐ 30,222 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[HairDeck: Animation-Ready Stylized Hair Cards from a Single Image](https://huggingface.co/papers/2610.40599)**

*Yuze He, Yixiang Wei, Wang Zhao et al. (6 authors)*

🏢 Tsinghua University

HairDeck generates stylized hair cards and spring-bone animations as unordered token sets using a diffusion transformer, improving accuracy and speed over prior methods.

▲ 23 • 💬 2 • ⭐ 563 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2610.40599) • [💻 code](https://github.com/hyz317/HairDeck) • [🔗 project](https://hyzcluster.github.io/HairDeck/)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 39 • 💬 2 • ⭐ 35,121 • 27mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 71 • 💬 4 • ⭐ 35,122 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 110 • 💬 2 • ⭐ 15,178 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 14.1k • 🔱 1.4k • 3d ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 5.6k • 🔱 501 • 14m ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 5.1k • 🔱 1.3k • 2h ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 4.7k • 🔱 230 • 3h ago

---

**[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)**

Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

`C` `ai-agent` `airplay` `automation` `computer-use` `esp32`

⭐ 4.2k • 🔱 561 • 4d ago

---

**[openfilm/openfilm](https://github.com/openfilm/openfilm)**

The open source AI video agent: turns any coding agent into a video agent, with an editor to change anything it makes.

`TypeScript` `ai-video` `claude-code` `codex` `coding-agents` `html`

⭐ 4.1k • 🔱 391 • 1d ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 3.7k • 🔱 675 • 1h ago

---

**[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)**

Ears for coding agents: let AI hear, review and make sound. CPU-only, open source.

`Python` `ai-agents` `audio` `claude-code` `mcp` `sound-design`

⭐ 3.4k • 🔱 215 • 9d ago

---

**[deeplethe/solid-glass](https://github.com/deeplethe/solid-glass)**

A design system for AI applications. Material, physical, tactile, technical.

`TypeScript` `agent-ui` `ai` `ai-agents` `chat-ui` `design-system`

⭐ 2.0k • 🔱 42 • 21h ago

---

**[zhuyansen/new-term-radar](https://github.com/zhuyansen/new-term-radar)**

Daily radar for new AI terms: names of new models, products and repos, caught on X, Hugging Face, GitHub and sitemaps before keyword tools list them.

`Python` `agent-skills` `ai` `aisa` `claude-code` `claude-skills`

⭐ 2.0k • 🔱 621 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
