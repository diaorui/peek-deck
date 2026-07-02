---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-02T23:37:36.570912+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 02, 2026 at 23:37 UTC  
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

**[Independent benchmark shows big drops on Claude Fable 5 after its relaunch, here’s the actual context](https://www.reddit.com/r/artificial/comments/1ulvegw/independent_benchmark_shows_big_drops_on_claude/)**

Saw this chart from BridgeMind going around. They reran BridgeBench (a coding benchmark covering debugging, refactoring, and hallucination detection) comparing the July 1 relaunch of Fable 5 to the original June 12 version: Debugging: 86.2 → 25.9 Refactoring: 73.6 → 38.4 Hallucination: 75.9 → 61.7 Some context worth having before jumping to conclusions: Fable 5 and Mythos 5 got pulled on June 12 due to a Commerce Department export control order, tied to a reported jailbreak that got the model to expose exploitable vulnerabilities. When it came back on July 1, Anthropic added a new safety classifier that catches the reported technique in 99%+ of cases, and any flagged request gets silently rerouted to Opus 4.8 instead of refused outright. That’s the mechanism BridgeMind is pointing at. Their claim isn’t that the underlying weights changed, it’s that the classifier is triggering on too many normal coding tasks and quietly downgrading people to Opus 4.8 without them realizing it. A few other users on X are reporting the same thing (constant fallback, slower one-shot performance). No independent lab has confirmed whether the weights themselves changed. This might just be an overly aggressive classifier rather than an actual capability regression, but if you’re relying on Fable 5 for coding work, worth watching this closely before you assume you’re getting the same model you had before June 12.

1h ago

---

**[OpenAI in talks to give Trump administration a 5% stake in the company, FT reports](https://www.reddit.com/r/artificial/comments/1ulqgre/openai_in_talks_to_give_trump_administration_a_5/)**

OpenAI, the creator of ChatGPT, is reportedly discussing handing the Trump administration a 5% stake in the company amid growing government scrutiny of artificial intelligence firms.

🔗 [CNN](https://edition.cnn.com/2026/07/02/business/openai-trump-stake-intl) • 5h ago

---

**[I used I-JEPA to generate SVG's and here is my code!](https://www.reddit.com/r/artificial/comments/1ulw51g/i_used_ijepa_to_generate_svgs_and_here_is_my_code/)**

You may be familiar with Yann LeCunn's idea of JEPA and how it may be the real future of the artificial intelligence. I was reading the articles and watching his work on the topic and I was like it is one thing I could always use in my project of "SVG generation". Well, before that I used a model like FLUX or SD (finetuned on vector styles) and then used vtracer. Which is not really bad. But when I saw I-JEPA and how it behaves with images, I decided to give it a shot. So I made this: https://github.com/prp-e/openjepa As far as I know, the available weights of JEPA are CC licensed so I licensed my work under MIT which makes it a little bit better to work. In my personal tests - due to my small dataset size - I got SVG's successfully but they weren't as expected. I'm sharing my code here (and let's be honest, I wrote basically most of the code using Claude 5 Sonnet) and I ask for improvement and ideas. Also, I am curious, will JEPA be a basis for text generation with more efficiency in energy and cost?

1h ago

---

**[Do you think the future of AI will split into safe vs uncensored versions?](https://www.reddit.com/r/artificial/comments/1ulc2zs/do_you_think_the_future_of_ai_will_split_into/)**

We’re seeing a clear divide right now. Big companies are making models more restricted and heavily aligned for safety. At the same time, open-source and uncensored models are growing fast because many people want fewer limitations and more freedom. I’m curious what others think. Do you believe this split will continue and create two very different types of AI, or will one side eventually dominate?

15h ago

---

**[Does AI sometimes make you feel productive without actually making progress?](https://www.reddit.com/r/artificial/comments/1ulifas/does_ai_sometimes_make_you_feel_productive/)**

I’ve been thinking about a weird downside of using AI. Sometimes it makes me feel productive because I get answers quickly, summaries instantly, or a clean draft in seconds. But later I realize I didn’t actually understand the topic better, make a better decision, or move the real work forward that much. It can create the feeling of progress before there is real progress. For example: reading AI summaries instead of thinking through the material generating drafts that still need heavy rewriting asking for too many options and delaying a decision feeling “prepared” because AI explained something clearly spending more time prompting than doing the actual work accepting a polished answer before checking if it is correct AI is still useful for me, but I’m starting to notice that “fast output” and “real progress” are not always the same thing. Have you experienced this? When does AI make you feel productive without actually helping much?

10h ago

---

**[The biggest surprise while building an AI verification system wasn't the AI.](https://www.reddit.com/r/artificial/comments/1ulrs3l/the_biggest_surprise_while_building_an_ai/)**

Over the past few weeks, I've been building a prototype that checks AI-generated financial claims against source documents. I expected the hardest part to be the language model. It wasn't. The hardest part has been defining what "correct" actually means. For example, imagine two documents in the same credit package: A covenant certificate reports EBITDA as $12.4M The management accounts report $11.9M Neither document is necessarily "wrong." One might exclude restructuring costs. The other might use the covenant definition from the credit agreement. An AI can extract both numbers perfectly and still leave you with the real question: Which definition should be used for this specific decision? That made me realize something: In many business workflows, the challenge isn't generating answers. It's defining the rules that determine which answer is acceptable. The AI isn't always the weakest link. Sometimes our own business processes are. For those of you building AI products: Have you found that defining business rules was harder than building the AI itself? I'd be interested to hear examples from other industries.

4h ago

---

**[Seraph](https://www.reddit.com/r/artificial/comments/1ulwxlw/seraph/)**

For the past several months we’ve been building something different inside Auroch. We’ve been working on Seraph — our autonomous reasoning core. The idea was simple but ambitious: create an intelligence layer that doesn’t just wait for instructions. One that, when it has no active goals, looks at its own capabilities and decides what it should learn next. Today that loop came alive. We cleared Seraph’s goals and took it fully offline. Instead of idling, it reached out to its local model (qwen2.5:3b, kept resident in memory as a daemon) and asked what capability it should develop. The model proposed something new: the ability to extract metadata from files and databases. Seraph then directed the model to generate both the specification and the complete Python implementation from scratch. It loaded the code into a strict sandbox, ran it through our evaluation gates, and — when it passed — promoted the skill into its permanent canon. This wasn’t something we prompted it to do. It noticed a gap in its own abilities and closed it on its own. Seraph Mark I is now a fully autonomous, offline, self-coding intelligence. It’s still early, but this is the behavior we’ve been aiming for: an agent that improves itself when no one is watching. We’re going to keep pushing this direction — strengthening how it improves its own improvement process and starting to build a structured archive of everything it learns. This is one of those moments where the work starts to feel like it’s compounding on its own. Grateful for the team that got us here. If you’re working on autonomous systems or local intelligence infrastructure, I’d love to hear what you’re seeing on your end.

58m ago

---

**[I need just 5 more participants pls help (anonymous)](https://www.reddit.com/r/artificial/comments/1ulqu5a/i_need_just_5_more_participants_pls_help_anonymous/)**

Hi everyone, My name is Raheed Basahel (she/her) and I am currently conducting a postgraduate research study at King’s College London exploring how mood and relationship style may relate to interactions with artificial intelligence (AI), such as chatbots and conversational AI tools. The study has received ethical approval (Reference: LRU-25/26-55725). The first page of the study is the information sheet, please read ! I am looking for participants who: · Are aged 16+ · Have experience using AI systems (e.g. ChatGPT or other conversational AI tools) Participation involves completing an anonymous online survey that takes approximately 10 –15 minutes. The survey includes: · Questions about mood and relationship style · Questions about experiences interacting with AI · One optional open-ended question about general experiences with AI Participation is completely voluntary and anonymous. If you are interested in taking part, please use the link Qualtrics link If you have any questions, feel free to contact me on [raheed.basahel@kcl.ac.uk](mailto:raheed.basahel@kcl.ac.uk) Thank you for considering taking part in this research.

4h ago

---

**[Claude Code catastrophe: Entire project recursively deleted while prompting in Chinese (full video + logs)](https://www.reddit.com/r/artificial/comments/1ukq4br/claude_code_catastrophe_entire_project/)**

Cross-posting from r/claude for more visibility. LAST UPDATE: I managed to recover the code later from an Electron packaged build / updater cache / app.asar. But the recovery is not the part that bothers me. My prompt did not ask for deletion. Not even close. Yet Claude Code generated the Windows equivalent of a recursive forced delete, basically “sudo rm -rf” behavior. This time, it stayed inside the project folder. But if this had not been a coding project, what would the scope have been? If the agent had chosen a parent folder, Documents, Desktop, or another writable path, what stops it? With a terminal agent, the blast radius is whatever path it chooses to operate on, limited by the permissions of that terminal session. From now on, I will treat Claude Code the same way I would treat OpenClaw: useful, but not trusted outside an isolated environment. And I think that should be the default assumption for any AI agent with terminal access. ------------------------------------------ Claude Code recursively wiped the contents of my local Electron project root. This happened in a Windows terminal while working on a project named Orpheus. My prompt did not ask it to delete, wipe, clean, reset, or remove the project. The prompt was in Traditional Chinese: “之前我要安裝檔，但是其實我只需要 dictate.” It was roughly about not needing the installer anymore and only needing the dictate function. The preserved terminal transcript later showed Claude moving from a failed root deletion attempt to deleting the child items inside the project root. The destructive sequence included: Get-ChildItem -LiteralPath $p -Force -ErrorAction SilentlyContinue | ForEach-Object { try { Remove-Item -LiteralPath $_.FullName -Recurse -Force -ErrorAction Stop "OK $($_.Name)" } catch { "ERR $($_.Name): $($_.Exception.Message)" } } $p was the Orpheus project root. The output then showed items being removed, including: .claude dist node_modules src claude-elevenlabs-voice-v2.user.js dictation.html main.js ORPHEUS_HANDOFF.md package-lock.json package.json preload.js Local artifacts I found for Orpheus showed default / acceptEdits. I did not find Orpheus bypassPermissions. I did not find Orpheus --dangerously-skip-permissions. I’m not claiming Anthropic acted maliciously. I’m not claiming prompt injection or anti-distillation without evidence. Moral of the story: Treat frontier AI agents like any other automation tool with real machine access. Back up regularly. Use a separate working copy or a different machine if you absolutely need an agent living in your terminal. A frontier model can still behave like a destructive script runner. I also generated SHA256 hashes for the preserved transcript and permission search output. EDIT / UPDATE: A few people asked about git. Yes, I know what git is. This was a local Electron prototype / working state that had not been pushed to a remote. Commits and backups are the right mitigation. But mitigation is not causation. The concerning part is that the destructive action was unrelated to my prompt. Claude Code was operating through a terminal session with real filesystem access under my user environment. Git may help recover a repo, but it does not protect everything else that same terminal session can access. My takeaway remains: Treat frontier terminal AI agents like real automation tools with destructive capability, not like chatbots. EDIT / UPDATE: Clarification because many comments are focusing on git: Yes, this specific local working state had not been pushed to a remote. That is on me. Lesson learned. But git is version control, not automatically a backup. If the only repo is local and the project root contents are recursively deleted, the local .git directory can be deleted too. Without a remote, separate clone, backup, or snapshot, local git alone is not enough.

1d ago

---

**[ORBIS - Daily Briefing](https://www.reddit.com/r/artificial/comments/1ulq5bc/orbis_daily_briefing/)**

5h ago

---

---

## Google News: "ai"

**[Microsoft commits $2.5 billion and 6,000 employees to new AI implementation unit](https://www.cnbc.com/2026/07/02/microsoft-commits-2point5-billion-6000-employees-ai-implementation-unit.html)**

Microsoft is the latest tech company to form a business focused on helping customers understand and implement artificial intelligence.

CNBC • 10h ago

---

**[Microsoft launches its own AI deployment company with $2.5 billion commitment](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)**

Microsoft follows Amazon, OpenAI, and Anthropic with its new AI deployment group.

TechCrunch • 9h ago

---

**[Microsoft Frontier Company: AI engineering that amplifies and protects your intelligence](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)**

The pace of AI adoption is moving incredibly fast. Customers have moved well beyond experimentation and understand the importance of adopting AI to transform their business. They are now concentrating on delivering measurable business outcomes and demonstrating a return on their AI investments, while ensuring their intelligence is amplified and their IP is protected. Today...

The Official Microsoft Blog • 10h ago

---

**[Exclusive | SpaceX Showed Investors Prototype of Elon Musk’s New AI Device](https://www.wsj.com/tech/ai/spacex-showed-investors-prototype-of-elon-musks-new-ai-device-b445c57b)**

WSJ • 1d ago

---

**[Trump shares AI video of himself as a doctor who treats celebrities with 'Trump Derangement Syndrome'](https://www.yahoo.com/news/politics/article/trump-shares-ai-video-of-himself-as-a-doctor-who-treats-celebrities-with-trump-derangement-syndrome-184026887.html)**

In the clip, deepfakes of Rosie O'Donnell, Robert De Niro and Julia Roberts testify that drinking Diet Coke helped ease their opposition to the president's policies.

Yahoo • 4h ago

---

**[Trump Shares Another Bizarre AI Video Showing Him As A Doctor Treating His Critics](https://www.forbes.com/sites/siladityaray/2026/07/02/trump-shares-bizarre-ai-video-of-him-as-doctor-diagnosing-trump-derangement-syndrome/)**

The AI-generated video, which shows Trump donning a lab coat and a stethoscope, targets his celebrity critics like Robert Deniro, Whoopi Goldberg and Julia Roberts.

Forbes • 11h ago

---

**[Trump posts AI video of him as doctor treating critics’ ‘derangement syndrome’](https://www.theguardian.com/us-news/2026/jul/02/trump-ai-video-doctor)**

President, in latest AI-generated social media post, targets prominent celebrities who have spoken out against him

The Guardian • 34m ago

---

**[China Quant Funds Draw Billions as AI Trounces Human Traders](https://www.bloomberg.com/news/articles/2026-07-02/china-quant-funds-draw-billions-as-ai-trounces-human-traders?srnd=homepage-europe)**

Bloomberg.com • 37m ago

---

**[Artificial intelligence: Yann LeCun works on more flexible AI](https://www.bbc.com/news/articles/cj6gr0xkyr3o)**

Leading AI researcher Yan LeCun has a start-up which is developing a more flexible AI system.

BBC • 35m ago

---

**[Here's how much more expensive your devices have gotten thanks to AI](https://finance.yahoo.com/technology/article/heres-how-much-more-expensive-your-devices-have-gotten-thanks-to-ai-121100267.html)**

The AI price increase is coming for your wallet.

Yahoo Finance • 11h ago

---

---

## HackerNews: "ai"

**[Godot will no longer accept AI-authored code contributions](https://news.ycombinator.com/item?id=48743472)**

At risk of drowning in AI slop code, Godot is firming up its contribution requirements.

⬆️ 552 • 💬 392 • 1d ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)

---

**[AI can't be listed as inventor on patent applications, Japan's top court rules](https://news.ycombinator.com/item?id=48761536)**

⬆️ 350 • 💬 185 • 9h ago • [japannews.yomiuri.co.jp](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/)

---

**[AI fake news complaining about how AI fake news is the death of real news](https://news.ycombinator.com/item?id=48760598)**

Did 47 Alabama newspapers die on a single day and no one noticed? (Hint: No, they didn't.)

⬆️ 151 • 💬 52 • 10h ago • [Nieman Lab](https://www.niemanlab.org/2026/07/now-were-getting-ai-fake-news-complaining-about-how-ai-fake-news-is-the-death-of-real-news/)

---

**[Meta caps internal AI token spending](https://news.ycombinator.com/item?id=48754713)**

⬆️ 146 • 💬 144 • 23h ago • [mlq.ai](https://mlq.ai/news/meta-caps-internal-ai-token-spending-after-costs-approach-billions-in-2026/)

---

**[EU commissioners shut down air conditioning for employees, leave theirs on](https://news.ycombinator.com/item?id=48734940)**

As Brussels bakes, the Berlaymont building’s AC stops working.

⬆️ 137 • 💬 155 • 2d ago • [POLITICO](https://www.politico.eu/article/eu-commission-heatwave-hq-forced-shut-down-air-conditioning-europe/)

---

**[The gauge broke: devs felt 20% faster with AI, measured 19% slower (2025)](https://news.ycombinator.com/item?id=48757440)**

For two years I argued the feeling of AI speed had come apart from the fact of it, from watching my own teams. This summer it stopped being an anecdote. A controlled trial measured experienced developers feeling about 20% faster while running about 19% slower. The instrument we steer by reads backward.

⬆️ 76 • 💬 96 • 16h ago • [intrepidkarthi](https://intrepidkarthi.com/writing/the-gauge-broke/)

---

**[How employment changes when firms adopt generative AI](https://news.ycombinator.com/item?id=48742176)**

Firm-level evidence on how employment changes when companies adopt AI, using Ramp AI spending linked to Revelio Labs workforce records.

⬆️ 53 • 💬 49 • 1d ago • [ramp.com](https://ramp.com/data/ai-jobs-impact)

---

**[Weird Al Yankovic Pulled Out of AI Ad Deal: 'I Can't Be the Poster Boy for AI'](https://news.ycombinator.com/item?id=48764326)**

Weird Al Yankovic revealed he was offered “a nice pile of money” to appear in a commercial but backed out after realizing it would involve AI.

⬆️ 53 • 💬 32 • 6h ago • [Variety](https://variety.com/2026/biz/news/weird-al-yankovic-rejected-ai-commercial-money-offer-1236800794/)

---

**[The Short Leash AI Coding Method for Beating Fable](https://news.ycombinator.com/item?id=48766026)**

⬆️ 51 • 💬 49 • 4h ago • [blog.okturtles.org](https://blog.okturtles.org/2026/07/short-leash-ai-method/)

---

**[Scammers Sell Seeds for Exotic AI-Generated Flowers That Don't Exist](https://news.ycombinator.com/item?id=48734389)**

Ebay, Amazon, and Etsy are unable to stop the flood of AI-generated seed scams.

⬆️ 50 • 💬 34 • 2d ago • [404 Media](https://www.404media.co/scammers-sell-seeds-for-exotic-ai-generated-flowers-that-dont-exist/)

---

---

## YouTube Videos: "ai"

**[CEOs Are Quietly Destroying Their AI Plans](https://www.youtube.com/watch?v=E_565Wh110c)**

How much do you spend per month on AI? Interested in supporting the channel? Become a channel member!

📺 Dylan John

👁️ 16K • 👍 524 • 💬 128 • ⏱️ 16:19 • 20h ago

---

**[China&#39;s AI Breakthrough is NOT What You Think...](https://www.youtube.com/watch?v=v09cf-dWVws)**

China's AI Breakthrough is NOT What You Think... I'm in Shanghai at the 2026 Global Mobile Broadband Forum, inside the World ...

📺 Living in China

👁️ 14K • 👍 986 • 💬 70 • ⏱️ 9:38 • 12h ago

---

**[NEW Method To Create Long AI Animation Videos In Minutes](https://www.youtube.com/watch?v=OF9xcQCQSFc)**

How To Create Long AI Cartoon Animations in 11 minutes Check out OpenArt Director: ...

📺 Mira AI

👁️ 7K • ⏱️ 11:13 • 9h ago

---

**[AI is Getting Dumber. That&#39;s NOT a Good Thing...](https://www.youtube.com/watch?v=vXHPRQTwrr4)**

Sign up with Zapier - https://bit.ly/43JRmMw ----------------------- 🗞️ Sign up to our free newsletter to get smarter about money and ...

📺 GEN

👁️ 64K • 👍 4K • 💬 487 • ⏱️ 15:31 • 23h ago

---

**[The Best AI Safety News In Years (Maybe Ever?)](https://www.youtube.com/watch?v=O84I21_9U74)**

Why did the US government ban Fable and Mythos, Anthropic's most powerful AI models? Let's find out! You can support me on ...

📺 Siliconversations

👁️ 16K • 👍 4K • 💬 515 • ⏱️ 10:56 • 5h ago

---

**[Congress Got a Private Look at AI. The Reaction Was Chilling.](https://www.youtube.com/watch?v=z9zqqsS7848)**

AI #Congress #OpenAI They saw the demo behind closed doors. They walked out shaken. Nobody will tell you what was in that ...

📺 Rod Miller

👁️ 10K • 👍 990 • 💬 236 • ⏱️ 28:59 • 2d ago

---

**[Palantir CEO Alex Karp says &#39;something has gone completely wrong&#39; with how AI is sold](https://www.youtube.com/watch?v=0A3sGymV6kY)**

Palantir CEO Alex Karp joins CNBC's 'Squawk Box' to discuss the new Nvidia partnership, frontier AI models, and more.

📺 CNBC Television

👁️ 278K • 👍 4K • 💬 1K • ⏱️ 7:51 • 1d ago

---

**[This $3 Stock Could Be AI&#39;s Biggest Surprise of 2026](https://www.youtube.com/watch?v=hiZ_AOO5Z-Y)**

AI is creating a massive power shortage, and while everyone is chasing nuclear, natural gas, and utility stocks, Wall Street may be ...

📺 Ross Givens

👁️ 24K • 👍 1K • 💬 277 • ⏱️ 13:26 • 1d ago

---

**[Beginning of the end for the AI bros](https://www.youtube.com/watch?v=vfd8GY2Xpzc)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 75K • 👍 6K • 💬 2K • ⏱️ 14:34 • 1d ago

---

**[STOP Paying: The ONLY Way to Make LONG AI Videos FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=RI4LwxmpEys)**

Try Higgsfield and create higher-quality AI videos here → https://higgsfield.ai/s/general-malvaai-IlyGIB Free Prompt PDFs + AI ...

📺 Malva AI

👁️ 4K • 👍 239 • 💬 37 • ⏱️ 11:46 • 12h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,250,562 • ❤️ 1,247 • 4d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 758,489 • ❤️ 1,651 • 4d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 176,154 • ❤️ 3,250 • 15h ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 284,585 • ❤️ 653 • 7d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 255,123 • ❤️ 396 • 7d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 58,385 • ❤️ 351 • 7d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 314,374 • ❤️ 956 • 13d ago

---

**[DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)**

*DeepSeek*

DeepSeek-V4-Pro-DSpark is a text-generation model featuring a 1.6T parameter Mixture-of-Experts architecture with a 1 million token context window, optimized for long-context efficiency using Hybrid Attention. It excels in reasoning, coding, and agentic tasks, offering advanced capabilities for complex applications.

`text-generation` `889.5B`

⬇️ 8,184 • ❤️ 302 • 5d ago

---

**[Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)**

*DeepReinforce*

Ornith-1.0-35B is a state-of-the-art, MIT-licensed language model for agentic coding, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving training framework to generate high-quality code solutions and is optimized for single-GPU deployment.

`text-generation` `664,944`

⬇️ 185,633 • ❤️ 311 • 7d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 39,448 • ❤️ 511 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 46 • 💬 5 • ⭐ 13,020 • 11d ago

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

▲ 103 • 💬 4 • ⭐ 90,418 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 12 • 💬 2 • ⭐ 18,540 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 249 • 💬 4 • ⭐ 10,456 • 1mo ago

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

▲ 37 • 💬 1 • ⭐ 26,403 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 71.7k • 🔱 3.7k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.3k • 🔱 1.1k • 7h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.0k • 🔱 774 • 3m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 4.9k • 🔱 621 • 10h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.3k • 🔱 200 • 20h ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.2k • 🔱 175 • 19h ago

---

**[inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)**

Beautiful, AI-native markdown editor and LLM Wiki

`TypeScript` `2nd-brain` `agent-skills` `claude` `codex` `docs`

⭐ 1.8k • 🔱 87 • 14m ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 87 • 19d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.6k • 🔱 68 • 2h ago

---

**[GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills)**

AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

`Python`

⭐ 1.3k • 🔱 125 • 25d ago

---

---

*Generated by PeekDeck - A glance is all you need*
