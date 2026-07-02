---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-02T19:25:18.451714+00:00'
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

**Last Updated:** July 02, 2026 at 19:25 UTC  
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

**[OpenAI in talks to give Trump administration a 5% stake in the company, FT reports](https://www.reddit.com/r/artificial/comments/1ulqgre/openai_in_talks_to_give_trump_administration_a_5/)**

OpenAI, the creator of ChatGPT, is reportedly discussing handing the Trump administration a 5% stake in the company amid growing government scrutiny of artificial intelligence firms.

🔗 [CNN](https://edition.cnn.com/2026/07/02/business/openai-trump-stake-intl) • 53m ago

---

**[I need just 5 more participants pls help (anonymous)](https://www.reddit.com/r/artificial/comments/1ulqu5a/i_need_just_5_more_participants_pls_help_anonymous/)**

Hi everyone, My name is Raheed Basahel (she/her) and I am currently conducting a postgraduate research study at King’s College London exploring how mood and relationship style may relate to interactions with artificial intelligence (AI), such as chatbots and conversational AI tools. The study has received ethical approval (Reference: LRU-25/26-55725). The first page of the study is the information sheet, please read ! I am looking for participants who: · Are aged 16+ · Have experience using AI systems (e.g. ChatGPT or other conversational AI tools) Participation involves completing an anonymous online survey that takes approximately 10 –15 minutes. The survey includes: · Questions about mood and relationship style · Questions about experiences interacting with AI · One optional open-ended question about general experiences with AI Participation is completely voluntary and anonymous. If you are interested in taking part, please use the link Qualtrics link If you have any questions, feel free to contact me on [raheed.basahel@kcl.ac.uk](mailto:raheed.basahel@kcl.ac.uk) Thank you for considering taking part in this research.

40m ago

---

**[Do you think the future of AI will split into safe vs uncensored versions?](https://www.reddit.com/r/artificial/comments/1ulc2zs/do_you_think_the_future_of_ai_will_split_into/)**

We’re seeing a clear divide right now. Big companies are making models more restricted and heavily aligned for safety. At the same time, open-source and uncensored models are growing fast because many people want fewer limitations and more freedom. I’m curious what others think. Do you believe this split will continue and create two very different types of AI, or will one side eventually dominate?

11h ago

---

**[Is it fair to reduce AI quotas after people have already subscribed?](https://www.reddit.com/r/artificial/comments/1ulm89k/is_it_fair_to_reduce_ai_quotas_after_people_have/)**

When I first subscribed to GitHub Copilot Pro, I remember having a much more generous premium model allowance. Today it's 300 premium requests/month, and different models consume different amounts, so the effective usage is even lower. I understand the economics of AI inference and why providers need to change pricing over time. My question isn't whether AI is expensive to run. What I'm wondering is: Is it fair to significantly reduce the value of an existing subscription after people have already signed up? It feels like the product I subscribed to has gradually become more restrictive. Also, what are people doing now? Are you sticking with Copilot, upgrading, switching to Cursor/Claude/ChatGPT, relying more on local models, or just becoming more selective about which models you use? Curious to hear how others think about this.

3h ago

---

**[Does AI sometimes make you feel productive without actually making progress?](https://www.reddit.com/r/artificial/comments/1ulifas/does_ai_sometimes_make_you_feel_productive/)**

I’ve been thinking about a weird downside of using AI. Sometimes it makes me feel productive because I get answers quickly, summaries instantly, or a clean draft in seconds. But later I realize I didn’t actually understand the topic better, make a better decision, or move the real work forward that much. It can create the feeling of progress before there is real progress. For example: reading AI summaries instead of thinking through the material generating drafts that still need heavy rewriting asking for too many options and delaying a decision feeling “prepared” because AI explained something clearly spending more time prompting than doing the actual work accepting a polished answer before checking if it is correct AI is still useful for me, but I’m starting to notice that “fast output” and “real progress” are not always the same thing. Have you experienced this? When does AI make you feel productive without actually helping much?

5h ago

---

**[The biggest surprise while building an AI verification system wasn't the AI.](https://www.reddit.com/r/artificial/comments/1ulrs3l/the_biggest_surprise_while_building_an_ai/)**

Over the past few weeks, I've been building a prototype that checks AI-generated financial claims against source documents. I expected the hardest part to be the language model. It wasn't. The hardest part has been defining what "correct" actually means. For example, imagine two documents in the same credit package: A covenant certificate reports EBITDA as $12.4M The management accounts report $11.9M Neither document is necessarily "wrong." One might exclude restructuring costs. The other might use the covenant definition from the credit agreement. An AI can extract both numbers perfectly and still leave you with the real question: Which definition should be used for this specific decision? That made me realize something: In many business workflows, the challenge isn't generating answers. It's defining the rules that determine which answer is acceptable. The AI isn't always the weakest link. Sometimes our own business processes are. For those of you building AI products: Have you found that defining business rules was harder than building the AI itself? I'd be interested to hear examples from other industries.

5m ago

---

**[Claude Code catastrophe: Entire project recursively deleted while prompting in Chinese (full video + logs)](https://www.reddit.com/r/artificial/comments/1ukq4br/claude_code_catastrophe_entire_project/)**

Cross-posting from r/claude for more visibility. LAST UPDATE: I managed to recover the code later from an Electron packaged build / updater cache / app.asar. But the recovery is not the part that bothers me. My prompt did not ask for deletion. Not even close. Yet Claude Code generated the Windows equivalent of a recursive forced delete, basically “sudo rm -rf” behavior. This time, it stayed inside the project folder. But if this had not been a coding project, what would the scope have been? If the agent had chosen a parent folder, Documents, Desktop, or another writable path, what stops it? With a terminal agent, the blast radius is whatever path it chooses to operate on, limited by the permissions of that terminal session. From now on, I will treat Claude Code the same way I would treat OpenClaw: useful, but not trusted outside an isolated environment. And I think that should be the default assumption for any AI agent with terminal access. ------------------------------------------ Claude Code recursively wiped the contents of my local Electron project root. This happened in a Windows terminal while working on a project named Orpheus. My prompt did not ask it to delete, wipe, clean, reset, or remove the project. The prompt was in Traditional Chinese: “之前我要安裝檔，但是其實我只需要 dictate.” It was roughly about not needing the installer anymore and only needing the dictate function. The preserved terminal transcript later showed Claude moving from a failed root deletion attempt to deleting the child items inside the project root. The destructive sequence included: Get-ChildItem -LiteralPath $p -Force -ErrorAction SilentlyContinue | ForEach-Object { try { Remove-Item -LiteralPath $_.FullName -Recurse -Force -ErrorAction Stop "OK $($_.Name)" } catch { "ERR $($_.Name): $($_.Exception.Message)" } } $p was the Orpheus project root. The output then showed items being removed, including: .claude dist node_modules src claude-elevenlabs-voice-v2.user.js dictation.html main.js ORPHEUS_HANDOFF.md package-lock.json package.json preload.js Local artifacts I found for Orpheus showed default / acceptEdits. I did not find Orpheus bypassPermissions. I did not find Orpheus --dangerously-skip-permissions. I’m not claiming Anthropic acted maliciously. I’m not claiming prompt injection or anti-distillation without evidence. Moral of the story: Treat frontier AI agents like any other automation tool with real machine access. Back up regularly. Use a separate working copy or a different machine if you absolutely need an agent living in your terminal. A frontier model can still behave like a destructive script runner. I also generated SHA256 hashes for the preserved transcript and permission search output. EDIT / UPDATE: A few people asked about git. Yes, I know what git is. This was a local Electron prototype / working state that had not been pushed to a remote. Commits and backups are the right mitigation. But mitigation is not causation. The concerning part is that the destructive action was unrelated to my prompt. Claude Code was operating through a terminal session with real filesystem access under my user environment. Git may help recover a repo, but it does not protect everything else that same terminal session can access. My takeaway remains: Treat frontier terminal AI agents like real automation tools with destructive capability, not like chatbots. EDIT / UPDATE: Clarification because many comments are focusing on git: Yes, this specific local working state had not been pushed to a remote. That is on me. Lesson learned. But git is version control, not automatically a backup. If the only repo is local and the project root contents are recursively deleted, the local .git directory can be deleted too. Without a remote, separate clone, backup, or snapshot, local git alone is not enough.

1d ago

---

**[ORBIS - Daily Briefing](https://www.reddit.com/r/artificial/comments/1ulq5bc/orbis_daily_briefing/)**

1h ago

---

**[AI safety testing is getting weird: when does benchmarking become abuse?](https://www.reddit.com/r/artificial/comments/1ulozxq/ai_safety_testing_is_getting_weird_when_does/)**

Reports say Meta contractors posed as teens to test rival chatbots on self-harm, sex, drugs, and eating disorders.

1h ago

---

**[I spent ~4.5 months building a free, self-hosted AI gateway: one endpoint for 237 providers (90+ free), auto-fallback, and a token-compression pipeline (MIT)](https://www.reddit.com/r/artificial/comments/1ulotbw/i_spent_45_months_building_a_free_selfhosted_ai/)**

Sharing an open-source project I've put ~4.5 months into (disclosure: I'm the maintainer; per the self-advertisement rule I'm keeping the link in the first comment and making this post substantive). It started from two problems I hit daily: AI runs dying on a provider rate limit, and burning thousands of tokens dumping tool/log output into the context window. One endpoint, 237 providers — 90+ of them free. You point any tool or agent at a single OpenAI-compatible endpoint (localhost:20128/v1) and it can reach 237 LLM providers without you rewriting anything. 90+ have free tiers and 11 are free forever (no card), which aggregates to ~1.6B documented free tokens/month — and that's honest, pool-deduped math (we count each shared pool once instead of inflating it; the methodology is public in the repo). There's a one-command setup-* for 13+ coding tools (Claude Code, Codex, Cursor, Cline, Roo, Kilo, Gemini CLI…), so switching your existing setup over takes seconds. Fallback combos — so it never stops mid-task. A "combo" is a ladder of models the router walks automatically: your subscription first, then API keys, then cheap models, then free ones. When a provider returns a 500 or you hit a rate limit, it slides to the next target in milliseconds, mid-request, and your tool never even sees the error. There are 17 routing strategies (priority, weighted, round-robin, cost-optimized, auto/coding:fast…) plus three resilience layers — a per-provider circuit breaker, a per-key cooldown, and a per-model lockout — so one dead key can't take down a whole provider. A 10-engine compression pipeline — the part most routers don't have. Every request flows through a transparent compression pass you can toggle/stack per combo. Instead of one trick, it stacks the best of the open-source ecosystem: RTK filters command/tool output (git diffs, test logs, builds) at 60–90%, Microsoft's LLMLingua-2 does ML semantic pruning, Caveman handles prose, session-dedup strips repeats across turns. Critically, code, URLs and JSON are preserved byte-perfect, and a default-on inflation guard throws the compressed version away and sends the original if compressing would actually grow the prompt — it never makes things worse. On tool-heavy sessions that's ~89% average input-token reduction (an 8k-token git diff becomes a few hundred). Full credit to every upstream project (RTK, Caveman, LLMLingua-2, Troglodita) is in the README. Agent-native — the agent can drive the router itself. There's a built-in MCP server (95 tools across 30 audited scopes, over stdio / SSE / streamable-HTTP), plus A2A (v0.3, JSON-RPC 2.0) support. That means an agent can query providers, switch combos, read its own remaining quota and manage memory through the gateway — not just consume tokens through it. For context on whether it's worth your time: it's grown to ~9.8K GitHub stars, 1,490+ forks and 280+ contributors in ~4.5 months, with 21,000+ automated tests and 1,830+ issues closed — so it's a battle-tested project, not a brand-new experiment. Happy to go deep on the routing engine, the honest free-tier math, or how the compression pipeline decides what's safe to compress. Repo + install in the first comment.

1h ago

---

---

## Google News: "ai"

**[Microsoft Frontier Company: AI engineering that amplifies and protects your intelligence](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)**

The pace of AI adoption is moving incredibly fast. Customers have moved well beyond experimentation and understand the importance of adopting AI to transform their business. They are now concentrating on delivering measurable business outcomes and demonstrating a return on their AI investments, while ensuring their intelligence is amplified and their IP is protected. Today...

The Official Microsoft Blog • 5h ago

---

**[Microsoft commits $2.5 billion and 6,000 employees to new AI implementation unit](https://www.cnbc.com/2026/07/02/microsoft-commits-2point5-billion-6000-employees-ai-implementation-unit.html)**

Microsoft is the latest tech company to form a business focused on helping customers understand and implement artificial intelligence.

CNBC • 6h ago

---

**[Microsoft merging enterprise, consumer Copilot AI chatbots: report (MSFT:NASDAQ)](https://seekingalpha.com/news/4609753-microsoft-merging-enterprise-consumer-copilot-ai-chatbots-report)**

Microsoft is merging enterprise and consumer Copilot into one app, adding AI coding tools and agents with paid features.

Seeking Alpha • 1h ago

---

**[Exclusive | SpaceX Showed Investors Prototype of Elon Musk’s New AI Device](https://www.wsj.com/tech/ai/spacex-showed-investors-prototype-of-elon-musks-new-ai-device-b445c57b)**

WSJ • 1d ago

---

**[SpaceX Built the Network an AI Device Needs. Now What?](https://www.pymnts.com/news/artificial-intelligence/2026/spacex-built-the-network-an-ai-device-needs-now-what/)**

SpaceX controls a satellite broadband network, a direct-to-cell service and an AI company. What it doesn’t have is a consumer device that connects all

PYMNTS.com • 27m ago

---

**[SpaceX has an AI device prototype, and it sure sounds phone-ish](https://techcrunch.com/2026/07/01/spacex-has-an-ai-device-prototype-and-it-sure-sounds-phone-ish/)**

SpaceX reportedly showed investors a "handset-like" AI device before going public. It could be another signal SpaceX wants to expand into wireless.

TechCrunch • 1d ago

---

**[Meta Stock Falls as AI Cloud Plans Hit an Immediate Snag](https://www.barrons.com/articles/meta-stock-price-softbank-cloud-0f855abd)**

Barron's • 1h ago

---

**[Meta Is Planning a Cloud Business to Sell AI Computing Power](https://www.bloomberg.com/news/articles/2026-07-01/meta-is-building-a-cloud-business-to-sell-excess-ai-compute)**

Bloomberg.com • 1d ago

---

**[Meta quietly launches vibe-coded gaming app Pocket](https://techcrunch.com/2026/07/02/meta-quietly-launches-vibe-coded-gaming-app-pocket/)**

Meta has quietly launched Pocket, an experimental AI app that lets users generate and share interactive mini games using text prompts.

TechCrunch • 41m ago

---

**[‘Doctor’ Donald Trump Posts AI Video Dragging Rosie O’Donnell, Whoopi Goldberg, Robert De Niro and More for Suffering From ‘Trump Derangement Syndrome’](https://variety.com/2026/digital/news/dr-trump-fake-ai-video-trump-derangement-syndrome-rosie-odonnell-whoopi-goldberg-robert-de-niro-1236800663/)**

In a fake AI video shared by Trump, he's a doctor treating celebrities for 'Trump Derangement Syndrome' including Rosie O'Donnell, Whoopi Goldberg and Robert De Niro.

Variety • 6h ago

---

---

## HackerNews: "ai"

**[Godot will no longer accept AI-authored code contributions](https://news.ycombinator.com/item?id=48743472)**

At risk of drowning in AI slop code, Godot is firming up its contribution requirements.

⬆️ 549 • 💬 390 • 1d ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)

---

**[AI can't be listed as inventor on patent applications, Japan's top court rules](https://news.ycombinator.com/item?id=48761536)**

⬆️ 280 • 💬 147 • 5h ago • [japannews.yomiuri.co.jp](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/)

---

**[Meta caps internal AI token spending](https://news.ycombinator.com/item?id=48754713)**

⬆️ 145 • 💬 141 • 19h ago • [mlq.ai](https://mlq.ai/news/meta-caps-internal-ai-token-spending-after-costs-approach-billions-in-2026/)

---

**[AI fake news complaining about how AI fake news is the death of real news](https://news.ycombinator.com/item?id=48760598)**

Did 47 Alabama newspapers die on a single day and no one noticed? (Hint: No, they didn't.)

⬆️ 140 • 💬 52 • 6h ago • [Nieman Lab](https://www.niemanlab.org/2026/07/now-were-getting-ai-fake-news-complaining-about-how-ai-fake-news-is-the-death-of-real-news/)

---

**[EU commissioners shut down air conditioning for employees, leave theirs on](https://news.ycombinator.com/item?id=48734940)**

As Brussels bakes, the Berlaymont building’s AC stops working.

⬆️ 137 • 💬 155 • 2d ago • [POLITICO](https://www.politico.eu/article/eu-commission-heatwave-hq-forced-shut-down-air-conditioning-europe/)

---

**[The gauge broke: devs felt 20% faster with AI, measured 19% slower (2025)](https://news.ycombinator.com/item?id=48757440)**

For two years I argued the feeling of AI speed had come apart from the fact of it, from watching my own teams. This summer it stopped being an anecdote. A controlled trial measured experienced developers feeling about 20% faster while running about 19% slower. The instrument we steer by reads backward.

⬆️ 75 • 💬 94 • 12h ago • [intrepidkarthi](https://intrepidkarthi.com/writing/the-gauge-broke/)

---

**[How employment changes when firms adopt generative AI](https://news.ycombinator.com/item?id=48742176)**

Firm-level evidence on how employment changes when companies adopt AI, using Ramp AI spending linked to Revelio Labs workforce records.

⬆️ 53 • 💬 48 • 1d ago • [ramp.com](https://ramp.com/data/ai-jobs-impact)

---

**[Scammers Sell Seeds for Exotic AI-Generated Flowers That Don't Exist](https://news.ycombinator.com/item?id=48734389)**

Ebay, Amazon, and Etsy are unable to stop the flood of AI-generated seed scams.

⬆️ 50 • 💬 34 • 2d ago • [404 Media](https://www.404media.co/scammers-sell-seeds-for-exotic-ai-generated-flowers-that-dont-exist/)

---

**[America can switch off AI. Europe must switch gears before it's too late](https://news.ycombinator.com/item?id=48741943)**

'Europe is becoming a digital colony between two AI empires' writes Dr. Sergey Lagodinsky, Vice Chair of the Greens/EFA Group in the European Parlament in an OpEd for Euronews. For Brussels, it is time to act. Europe needs a smart strategy of cooperation that will keep the European economy alive. #EuropeNews

⬆️ 45 • 💬 59 • 1d ago • [euronews](https://www.euronews.com/my-europe/2026/06/30/america-can-switch-off-the-worlds-ai-europe-must-switch-gears-before-its-too-late)

---

**['It's like having a dumb friend': Young San Franciscans hate AI](https://news.ycombinator.com/item?id=48753927)**

⬆️ 45 • 💬 15 • 21h ago • [sfgate.com](https://www.sfgate.com/tech/article/san-francisco-ai-backlash-22325141.php)

---

---

## YouTube Videos: "ai"

**[NEW Method To Create Long AI Animation Videos In Minutes](https://www.youtube.com/watch?v=OF9xcQCQSFc)**

How To Create Long AI Cartoon Animations in 11 minutes Check out OpenArt Director: ...

📺 Mira AI

👁️ 5K • ⏱️ 11:13 • 5h ago

---

**[CEOs Are Quietly Destroying Their AI Plans](https://www.youtube.com/watch?v=E_565Wh110c)**

How much do you spend per month on AI? Interested in supporting the channel? Become a channel member!

📺 Dylan John

👁️ 14K • 👍 486 • 💬 120 • ⏱️ 16:19 • 16h ago

---

**[STOP Paying: The ONLY Way to Make LONG AI Videos FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=RI4LwxmpEys)**

Try Higgsfield and create higher-quality AI videos here → https://higgsfield.ai/s/general-malvaai-IlyGIB Free Prompt PDFs + AI ...

📺 Malva AI

👁️ 1K • 👍 127 • 💬 31 • ⏱️ 11:46 • 8h ago

---

**[China&#39;s AI Breakthrough is NOT What You Think...](https://www.youtube.com/watch?v=v09cf-dWVws)**

China's AI Breakthrough is NOT What You Think... I'm in Shanghai at the 2026 Global Mobile Broadband Forum, inside the World ...

📺 Living in China

👁️ 9K • 👍 773 • 💬 45 • ⏱️ 9:38 • 8h ago

---

**[AI is Getting Dumber. That&#39;s NOT a Good Thing...](https://www.youtube.com/watch?v=vXHPRQTwrr4)**

Sign up with Zapier - https://bit.ly/43JRmMw ----------------------- 🗞️ Sign up to our free newsletter to get smarter about money and ...

📺 GEN

👁️ 55K • 👍 3K • 💬 456 • ⏱️ 15:31 • 18h ago

---

**[Congress Got a Private Look at AI. The Reaction Was Chilling.](https://www.youtube.com/watch?v=z9zqqsS7848)**

AI #Congress #OpenAI They saw the demo behind closed doors. They walked out shaken. Nobody will tell you what was in that ...

📺 Rod Miller

👁️ 10K • 👍 984 • 💬 234 • ⏱️ 28:59 • 2d ago

---

**[Students Fed Every Biblical Prayer Into Grok AI — What It Decoded About God TERRIFIED Them](https://www.youtube.com/watch?v=TL-JVqXY8NY)**

Students Fed Every Biblical Prayer Into Grok AI — What It Decoded About God TERRIFIED Them What happens when students ...

📺 Curious Explorer

👁️ 46K • 👍 524 • 💬 10 • ⏱️ 31:35 • 3d ago

---

**[Why is AI expensive all of a sudden?](https://www.youtube.com/watch?v=DDj30VWCbbY)**

ZapierPartner Sponsored by Zapier! Zapier MCP levels you up, connecting you directly to apps to automate your workflow.

📺 Alberta Tech

👁️ 144K • 👍 8K • 💬 740 • ⏱️ 9:43 • 2d ago

---

**[The AI Bubble Has F*cked Us (Even If It NEVER Pops)](https://www.youtube.com/watch?v=dPVEha6oqfw)**

The AI Bubble Will Is MUCH Worse Than We Thought. Contact your representative to ENSURE AI is aligned with humanity: ...

📺 Damon Cassidy

👁️ 85K • 👍 4K • 💬 800 • ⏱️ 22:06 • 1d ago

---

**[AI Stand-Up Comedy is Worse Than You Think...](https://www.youtube.com/watch?v=FA-dfsMLd7Q)**

In this video, I talk about the cringe world of AI stand-up comedy and the weirdos online making videos of AI babies doing ...

📺 Kameron

👁️ 74K • 👍 4K • 💬 437 • ⏱️ 20:00 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 758,489 • ❤️ 1,640 • 4d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,250,562 • ❤️ 1,224 • 4d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 176,154 • ❤️ 3,235 • 11h ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 284,585 • ❤️ 644 • 7d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 255,123 • ❤️ 391 • 7d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 58,385 • ❤️ 344 • 7d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 314,374 • ❤️ 947 • 13d ago

---

**[Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)**

*DeepReinforce*

Ornith-1.0-35B is a state-of-the-art, MIT-licensed language model for agentic coding, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving training framework to generate high-quality code solutions and is optimized for single-GPU deployment.

`text-generation` `664,944`

⬇️ 185,633 • ❤️ 306 • 7d ago

---

**[DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)**

*DeepSeek*

DeepSeek-V4-Pro-DSpark is a text-generation model featuring a 1.6T parameter Mixture-of-Experts architecture with a 1 million token context window, optimized for long-context efficiency using Hybrid Attention. It excels in reasoning, coding, and agentic tasks, offering advanced capabilities for complex applications.

`text-generation` `889.5B`

⬇️ 8,184 • ❤️ 297 • 5d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 39,448 • ❤️ 510 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 46 • 💬 5 • ⭐ 12,943 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 73,045 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 23 • 💬 2 • ⭐ 9,361 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 103 • 💬 4 • ⭐ 90,328 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 12 • 💬 2 • ⭐ 18,413 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 249 • 💬 4 • ⭐ 10,411 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,126 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 85,144 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 12 • 💬 1 • ⭐ 10,035 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 26,361 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 71.5k • 🔱 3.7k • 19h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.3k • 🔱 1.1k • 2h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.0k • 🔱 771 • 1h ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 4.8k • 🔱 616 • 6h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.3k • 🔱 199 • 16h ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.2k • 🔱 175 • 15h ago

---

**[inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)**

Beautiful, AI-native markdown editor and LLM Wiki

`TypeScript` `2nd-brain` `agent-skills` `claude` `codex` `docs`

⭐ 1.8k • 🔱 86 • 1h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 87 • 19d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.5k • 🔱 67 • 1d ago

---

**[GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills)**

AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

`Python`

⭐ 1.3k • 🔱 125 • 25d ago

---

---

*Generated by PeekDeck - A glance is all you need*
