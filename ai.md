---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-30T21:33:42.964453+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 30, 2026 at 21:33 UTC  
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

**[Mystery company accidentally blew $500 million on Claude AI in a single month — failed to put usage limit on licenses for employees](https://www.reddit.com/r/artificial/comments/1trmvgh/mystery_company_accidentally_blew_500_million_on/)**

A mysterious, unnamed company is reported to have accidentally spent half a billion dollars in a single month on Claude AI after forgetting to set usage limits for Claude licenses for employees.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/mystery-company-accidentally-blew-usd500-million-on-claude-in-a-single-month-failed-to-put-usage-limit-on-licenses-for-employees) • 19h ago

---

**[Ronny Chieng Tells Harvard to ‘Destroy AI’ as Graduates Cheer](https://www.reddit.com/r/artificial/comments/1trfunt/ronny_chieng_tells_harvard_to_destroy_ai_as/)**

The comedian and The Daily Show host gave the keynote address for Class Day 2026.

🔗 [Harvard Magazine](https://www.harvardmagazine.com/commencement/class-day-ronny-chieng-harvard) • 1d ago

---

**[How has AI actually benefited you in day-to-day life?](https://www.reddit.com/r/artificial/comments/1ts6q6b/how_has_ai_actually_benefited_you_in_daytoday_life/)**

With AI becoming part of almost everything now—work, business, investing, coding, spreadsheets, content creation, and more—I'm curious about real-world use cases. What's the one thing you use AI for regularly that has genuinely saved you time, made you money, improved your productivity, or solved a problem? Looking for practical examples rather than just "I use ChatGPT." What specific tasks have you automated or improved with AI?

3h ago

---

**[🚀 Prompt Logic Gates (PLG): Are Prompts Becoming Systems?](https://www.reddit.com/r/artificial/comments/1ts7b48/prompt_logic_gates_plg_are_prompts_becoming/)**

GitHub: Prompt-Logic-Gates-PLG Over the past few days, I've shared my research project Prompt Logic Gates (PLG) and received a lot of interesting feedback. Some people loved the idea, some were skeptical, and many raised valid questions. The most common reaction was: > "Natural language is already the abstraction layer. Why add logic gates?" That's a fair question. My goal isn't to replace natural language prompting. In fact, natural language remains at the center of PLG. The idea is to explore what happens when prompts stop being a single request and start becoming systems. The Problem When we write prompts, we're converting our ideas, requirements, constraints, and expectations into text. For simple tasks, this works perfectly. But as prompts grow, they often include: Multiple objectives Business rules Style constraints Context dependencies Exclusions Fallback instructions Tool orchestration At that point, prompts become harder to maintain. Contradictions appear. Priorities become unclear. Context gets mixed together. The prompt is still text, but the complexity starts to resemble a system. What is PLG? Prompt Logic Gates (PLG) is a visual prompt engineering experiment that explores whether prompts can be organized before being sent to an AI model. Instead of writing one giant prompt, users create prompt components and connect them using semantic logic gates. The AI then analyzes the graph and compiles a final structured prompt. How It Works AND Gate When multiple instructions exist, the system evaluates them against the current context and determines which instruction is more foundational. The higher-priority instruction is applied first. OR Gate When multiple options are available, the system selects the most contextually relevant option instead of blindly including everything. NOT Gate Defines exclusions and negative constraints. It explicitly tells the system what should not be done, reducing contradictions and ambiguity. Ask Questions Gate If the system detects missing information or uncertainty, it asks follow-up questions before generating the final prompt. Addressing Common Criticisms "This is just block coding." Not exactly. The goal isn't to create a programming language for prompts. The nodes still contain natural language. The visual layer only helps express relationships between prompt components. "Prompts aren't code." I agree. But once prompts include branching decisions, reusable components, exclusions, fallback behavior, memory, and tool orchestration, they start behaving less like a sentence and more like a system. PLG is exploring whether that hidden structure can be represented more explicitly. "Visual prompt engineering may be harder to debug." That's a valid concern. Visual doesn't automatically mean better. One of the main goals of this project is to test whether visual organization actually improves maintainability, reusability, and prompt consistency—or whether it simply makes the same complexity look different. "The future is promptless AI." Maybe. But today's AI systems still rely heavily on instructions, context, constraints, and reasoning frameworks. Even if prompts eventually disappear, the underlying problem of organizing intent, requirements, and context may still exist. Why I'm Building This This project started because I was facing problems in my own prompting workflow. I wanted a way to organize ideas, constraints, and instructions more systematically instead of continuously rewriting large prompts. PLG isn't trying to solve every problem in AI. It's a research experiment exploring one question: > At what point does a prompt stop being "just text" and start behaving like a system that benefits from structure, organization, and validation? I don't know the answer yet. That's exactly why I'm building the prototype and testing it. If the idea turns out to be useful, great. If it doesn't, I'll still learn something valuable about how humans interact with AI systems. I'd love to hear more thoughts, criticism, and feedback from the community.

3h ago

---

**[Deep Neural Network that turns any Image into a Playable Game ! All on consumer GPUs and Not Datacenters](https://www.reddit.com/r/artificial/comments/1trs21e/deep_neural_network_that_turns_any_image_into_a/)**

Hi everyone!! I really wanted to share my research what I've been working on. I wanted to build a nn that can simulate games, or at least start doing that Most video generators are too large to run on consumer hardware realtime, so I I designed a model that does this from scratch. No fine tuning bs or anything The core de noiser network is fully trained from scratch to support this goal. From image to games data. That video. above is on a RTX 5090. The nn is a small Transformer-like model and works in a causal way, just like LLMs. That lets us KV Cache all past information and do a simple autoregressive decode forward passes for every new frame we want. In the video shared, the model is a 0.4B variant with some SIGNIFICANT ISSUES like poor motion and some weird flashes, some context issues It's taking the keyboard actions I give it in realtime and utilising that in the forward pass. (no classifier free guidance though) Im training the next iteration , a 0.8B model now. Btw I haven't done quantisation yet, that can save a LOT more time. bf16 is slow.

15h ago

---

**[Meta lays off more than 2,000 from Menlo Park headquarters](https://www.reddit.com/r/artificial/comments/1trevkk/meta_lays_off_more_than_2000_from_menlo_park/)**

🔗 [sfgate.com](https://www.sfgate.com/tech/article/more-meta-layoffs-22282871.php) • 1d ago

---

**[I built a tool that generates 3D objects assembled with separate, logical parts (e.g. it generated a microwave in the video with complete internal assembly and a door that swings open)](https://www.reddit.com/r/artificial/comments/1ts5ql9/i_built_a_tool_that_generates_3d_objects/)**

Standard AI 3D generators (like Meshy or Tripo) are limited. They produce solid, monolithic 3D objects that look good but are practically useless, because: - Want to rig or animate it for a game? Can't easily do that, because it’s a dead, monolithic blob instead of a functional, modular asset. - Want to change the arm of a robot you generated? Regenerate the entire asset. - Want to edit something manually? The whole thing collapses because it's not actually structured. Free github project here: https://github.com/RareSense/Nova3D But you'll need to bring your own API Key (BYOK) Under the hood (if you're interested): It uses an LLM as a structured code compiler, instead of an image generator. It writes native Blender Python (bpy) code blocks that target specific nodes in the scene graph. The trick is that everything compiles through Blender's actual scene graph structures instead of pixel or point-cloud diffusion. Final export is a clean multi-part GLB with transform nodes and working pivot axes preserved.

4h ago

---

**[I connected my AI agent to manage my redirects and I'm not going back to doing it manually](https://www.reddit.com/r/artificial/comments/1ts2n0t/i_connected_my_ai_agent_to_manage_my_redirects/)**

I have been doing URL redirect work for client sites for some time now. It’s one of those jobs that’s never quite urgent enough to automate, but tedious enough to dread, especially after a migration when you have hundreds of them. Recently tried it. Connected my AI agent with MCP to handle it. I told it to build a set of redirects and it did. No dashboard, no wrestling with CSVs, no clicking through settings. Teaching in plain language. In seconds. And what I was surprised by was not the speed, but the amount of mental overhead such a task involves. You’re not just doing the task you’re context switching into a tool, remembering where things are, making sure nothing breaks. Giving it to an agent removes all of it. What really made me trust it for real client work was the dry-run feature. See exactly what is changing, before it changes. No surprises here. Curious if anyone else has been using MCP for infrastructure tasks, redirects, DNS, workspace management. I think we are at the start of something that is going to quietly gobble up a lot of tedious technical work.

6h ago

---

**[Weekly AI roundup (May 23–30, 2026): Claude Opus 4.8 Fast Mode 3x cheaper, Qwen 3.7 Max beats Claude at half the price, ChatGPT moves into Excel](https://www.reddit.com/r/artificial/comments/1trz2pd/weekly_ai_roundup_may_2330_2026_claude_opus_48/)**

Pulling together this week's major AI releases for anyone who didn't have time to track every blog post. Sticking to substantive changes, not hype. Anthropic — Claude Opus 4.8 Released this week. Headline pricing unchanged, but Fast Mode dropped from $30 input / $150 output per million tokens to $10 / $50 — a 3x reduction on the premium tier. Reported improvements in "judgment" and longer autonomous runs. Also shipped 20+ legal MCP connectors and Microsoft 365 add-ins (Excel, PowerPoint, Word) in GA. Alibaba — Qwen 3.7 Max Launched May 20 at Alibaba Cloud Summit. 1M-token context. Reported to top Claude Opus 4.6 Max on Terminal-Bench 2.0, SWE-Bench Pro, and MCP-Atlas. Pricing $2.50 / $7.50 per million tokens — roughly half of Opus 4.7. Alibaba claims autonomous operation up to 35 hours without performance degradation. Alibaba is now ranked #6 lab globally on Arena text leaderboard. OpenAI — GPT-5.5 Instant Now default in ChatGPT. Reports 52.5% fewer hallucinated claims than GPT-5.3 Instant on high-stakes prompts (medicine, law, finance). OpenAI also shipped a ChatGPT sidebar inside Excel and Google Sheets, plus a personal finance dashboard for Pro users (US only). Google — Gemini 3.5 Flash Reported to beat Gemini 3.1 Pro on coding and agentic benchmarks at ~4x faster output token rate. Ultra subscription cut from $250 to $200/month; new $100/month Developer tier introduced. xAI — Grok Build 0.1 Coding agent moved to public API beta May 28. Custom Skills feature added for reusable user-defined tasks. Connectors for SharePoint, OneDrive, Notion, GitHub, Linear, plus bring-your-own MCP support. Mistral Launched Vibe (unified work + code agent, replaces Le Chat). Acquired Emmi AI for physics-based simulation. Targeting €1B revenue in 2026; new 10MW inference DC announced. Hugging Face Launched an app store for the Reachy Mini robot. ~10,000 units shipped. Also reported a malicious repo masquerading as an OpenAI release that accumulated 244K downloads before takedown — relevant for anyone pinning models from HF in production. My take as someone building on top of these APIs: The 3x Opus Fast Mode price cut and Qwen 3.7 Max's pricing + autonomous duration are the real signal this week. The cost floor on premium-tier inference is dropping faster than most app-layer products have repriced for. Anyone running multi-step agent workflows needs to recompute unit economics this week — either pass through the savings or reinvest the margin. The other pattern worth noting: OpenAI and Anthropic are both pushing into Excel/M365 surfaces. Distribution is becoming the next battleground, not raw model capability. If you're building a productivity SaaS, the giants are now inside the same surface as you.

8h ago

---

**[[Open Source] I built a full Git MCP server in Go that doesn't just wrap bash. It uses tree-sitter, handles real plumbing (write-tree), and runs 100% locally.](https://www.reddit.com/r/artificial/comments/1tsbgpx/open_source_i_built_a_full_git_mcp_server_in_go/)**

I was tired of watching LLM agents fail at basic Git operations. Standard integrations pass raw text, hang on pagers, or scream because they can't parse unstructured ⁠git diff⁠ outputs. git-courer is a full Model Context Protocol (MCP) server written in Go that treats Git properly. No bash spawning, no unstructured text to parse. Everything communicates via structured JSON. Here is an actual commit message it generated completely locally: fix: fix mcp server connection handling WHY The previous implementation lacked proper error handling for connection failures in the MCP server, leading to unhandled panics or silent failures when the local LLM backend was unreachable. WHAT * Added connection timeout logic to the local client calls. * Implemented retry mechanisms with exponential backoff for transient backend errors. The Architecture & Tool Pack Read Tools (status, diff, history, blame): Completely structured JSON and fully paginated. A single ⁠status⁠ call replaces over 5 standard Git commands for the agent. Write Tools (commit, merge, rebase, branch, stash, stage, sync...): Every single mutation auto-creates a backup before executing. If the LLM messes up, a ⁠RESTORE⁠ command brings you back exactly where you were. Safety Model: Destructive operations (hard resets, force pushes, branch deletions) require an explicit ⁠confirmed=true⁠ gate. The agent is forced to ask you first. ⁠dry_run=true⁠ is also available for peace of mind. The Semantic Annotator (Why it's different) Instead of just feeding raw code to the LLM, git-courer uses ⁠go-enry⁠ + ⁠go-tree-sitter⁠ to parse the AST and tag every hunk semantically before the LLM even sees it. It detects tags like ⁠NEW_FUNC⁠, ⁠MOD_SIG⁠, ⁠MOD_BODY⁠, ⁠DELETED⁠, and ⁠BREAKING_CHANGE⁠. The commit type (⁠feat⁠, ⁠fix⁠, ⁠refactor⁠) is determined deterministically from these AST tags rather than guessed by the model. The Commit Pipeline Atomic Commits: One staged area = one commit. It actively prevents the agent from creating giant, messy multi-feature commits. In-Memory Previews: The ⁠PREVIEW⁠ tool uses ⁠write-tree⁠ to snapshot the staging area into a ⁠job_id⁠. The working tree is never touched during the preview stage. ⁠APPLY⁠ then uses ⁠commit-tree⁠ + ⁠update-ref⁠ to seal the deal cleanly. Client & Backend Support 13 Clients Configured Automatically: Runs out of the box with ⁠git-courer mcp setup⁠ for Claude Code, Cursor, Windsurf, OpenCode, Cline, Roo Code, VS Code, Zed, Claude Desktop, Continue, and more. 100% Local-First: Works with any backend exposing an OpenAI-compatible ⁠/v1⁠ API (Ollama, LM Studio, llama.cpp). The project is fully open source. I’d love to hear your thoughts on the architecture, the plumbing pipeline, or any features you'd like to see added! Repo: github.com/Alejandro-M-P/git-courer

29m ago

---

---

## Google News: "ai"

**[The Feeling of Control Slipping Away](https://www.theatlantic.com/technology/2026/05/ai-agents-agency-crisis-humanity/687379/)**

AI is causing a crisis of agency.

The Atlantic • 10h ago

---

**[Opinion | The First A.I. High School in the U.S. Is Surprisingly Human](https://www.nytimes.com/2026/05/30/opinion/ai-high-school.html)**

The New York Times • 10h ago

---

**[SoftBank to build up AI data centres in France with major investment](https://www.reuters.com/business/media-telecom/softbank-build-up-ai-data-centres-france-with-major-investment-2026-05-30/)**

Reuters • 2h ago

---

**[SoftBank Plans Up to €75 Billion Investment in French AI Centers](https://www.bloomberg.com/news/articles/2026-05-30/softbank-to-invest-some-75-billion-in-ai-in-france-reports-say)**

Bloomberg.com • 1h ago

---

**[SoftBank plans up to €75 billion investment in French AI centers](https://fortune.com/2026/05/30/softbank-75-billion-investment-french-ai-data-centers-masayoshi-son-emmanuel-macron/)**

SoftBank’s initial investment plans to deliver data centers in Dunkirk, Bosquel and Bouchain.

Fortune • 31m ago

---

**[The NTSB tries to keep cockpit audio recordings private. AI is making that harder](https://www.npr.org/2026/05/30/nx-s1-5835242/ntsb-cockpit-audio-cvr-reconstruction)**

The National Transportation Safety Board temporarily pulled its docket system offline after digital images were used to reconstruct cockpit voice recordings of the pilots in a recent crash.

NPR • 11h ago

---

**["The pitchforks are here": Billionaires work to contain AI's populist revolt](https://www.axios.com/2026/05/29/ai-billionaires-tech-taxes-wealth)**

Axios • 1d ago

---

**[Ukraine using AI drones to strike vital convoys supplying Russian troops](https://www.bbc.com/news/articles/cdjp0n7rn41o)**

BBC Verify has analysed videos of attacks in occupied Ukraine on Russian trucks carrying ammunition, fuel and food.

BBC • 19h ago

---

**[Meta has struggled at selling anything other than ads. Will AI be different?](https://www.cnbc.com/2026/05/30/meta-struggled-selling-anything-other-than-ads-will-ai-be-different.html)**

Meta is making a major push to expand its business beyond online advertising, but past efforts show that success is far from guaranteed.

CNBC • 9h ago

---

**[Corporate America Is Starting to Ration AI as Cost Skyrockets](https://www.wsj.com/tech/ai/corporate-america-is-starting-to-ration-ai-as-cost-skyrockets-1eb99d7a)**

WSJ • 1d ago

---

---

## HackerNews: "ai"

**[Please Use AI](https://news.ycombinator.com/item?id=48323101)**

⬆️ 758 • 💬 388 • 1d ago • [shawnsmucker.substack.com](https://shawnsmucker.substack.com/p/please-use-ai)

---

**[Notes from the Mistral AI Now Summit](https://news.ycombinator.com/item?id=48325340)**

A few days in Paris for the Mistral AI Now Summit: open models, on-prem deployment, agentic harnesses, and why Mistral wants to be the European full-stack AI partner.

⬆️ 449 • 💬 197 • 1d ago • [koenvangilst.nl](https://koenvangilst.nl/lab/mistral-ai-now-summit)

---

**[Is AI causing a repeat of frontend’s lost decade?](https://news.ycombinator.com/item?id=48321631)**

AI is doing to programming what framework-brain did to the frontend before. Deskilling, or just working at a higher level of abstraction?

⬆️ 396 • 💬 325 • 1d ago • [mastrojs.github.io](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/)

---

**[Anthropic surpasses OpenAI to become most valuable AI startup](https://news.ycombinator.com/item?id=48336233)**

Anthropic has become the most valuable artificial intelligence startup in the world, surpassing OpenAI in market valuation. Following a new funding round, the valuation of the developer behind the Claude AI assistant has approached the $1 trillion mark, reports a Qazinform News Agency correspondent.

⬆️ 381 • 💬 431 • 7h ago • [Qazinform.com](https://qazinform.com/news/anthropic-surpasses-openai-to-become-worlds-most-valuable-ai-startup)

---

**[Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue](https://news.ycombinator.com/item?id=48308376)**

A 30-second game about LLM permission fatigue. How carefully do you really read AI commands?

⬆️ 378 • 💬 156 • 2d ago • [llmgame.scalex.dev](https://llmgame.scalex.dev)

---

**[SF startup is testing robots in Airbnbs, and trashing them, lawsuit claims](https://news.ycombinator.com/item?id=48317093)**

The guests behind the bookings have received negative reviews from a number of Bay Area hosts, alleging they damaged the property and personal belongings.

⬆️ 267 • 💬 148 • 1d ago • [sfstandard.com](https://sfstandard.com/2026/05/28/sf-startup-secretly-testing-robots-airbnbs-trashing-lawsuit-claims/)

---

**[Liquid AI reveals 8B-A1B MoE trained on 38T](https://news.ycombinator.com/item?id=48325306)**

Today, we’re releasing LFM2.5-8B-A1B, a high-throughput edge model optimized for fast, reliable tool calling and complex instruction following on consumer hardware, delivering compressed performance competitive with much larger models and day-one support across major inference frameworks.

⬆️ 238 • 💬 92 • 1d ago • [liquid.ai](https://www.liquid.ai/blog/lfm2-5-8b-a1b)

---

**[Sam Altman and Dario Amodei are both walking back AI jobs apocalypse predictions](https://news.ycombinator.com/item?id=48314363)**

Some leaders like Goldman Sachs’s David Solomon and Box’s Aaron Levie have been saying all along that there won’t be a white-collar wipeout.

⬆️ 234 • 💬 179 • 2d ago • [Fortune](https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/)

---

**[AI sticker shock hits corporate America](https://news.ycombinator.com/item?id=48307098)**

⬆️ 167 • 💬 143 • 2d ago • [axios.com](https://www.axios.com/2026/05/28/ai-spending-roi-enterprise-costs)

---

**[A Eureka machine that thinks like nature and explores what AI cannot](https://news.ycombinator.com/item?id=48305446)**

IISc is the premier institute for advanced scientific and technological research and education in India.

⬆️ 146 • 💬 44 • 2d ago • [iisc.ac.in](https://iisc.ac.in/a-eureka-machine-that-thinks-like-nature-and-explores-what-ai-cannot/)

---

---

## YouTube Videos: "ai"

**[Our latest reports on AI | 60 Minutes Full Episodes](https://www.youtube.com/watch?v=iyVXw-SoUrY)**

From November 2025, Anderson Cooper's report on Anthropic. From December 2025, Sharyn Alfonsi's report on Character AI.

📺 60 Minutes

👁️ 63K • 👍 1K • 💬 121 • ⏱️ 1:32:36 • 10h ago

---

**[I Asked Grok AI To Predict The 2028 Election... LANDSLIDE Incoming!](https://www.youtube.com/watch?v=hqTezFeXrlA)**

Pollsmax* 》https://www.pollsmax.com/ ...

📺 Election Time

👁️ 80K • 👍 3K • 💬 529 • ⏱️ 18:32 • 1d ago

---

**[I Created an Army of AI Influencers With Higgsfield Supercomputer](https://www.youtube.com/watch?v=kXo2_X5Z9Uw)**

Create Your Own Army of AI Influencers with Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=isa17 In this video, I build a full ...

📺 Isa does AI

👁️ 9K • ⏱️ 11:28 • 9h ago

---

**[If you’re trying to get rich with AI, you need to hear this…](https://www.youtube.com/watch?v=TWuzAO7ukk0)**

Want my AI Tech Stack? Get it here: https://go.danmartell.com/4nUvaZi Are you building an AI software company? Partner with ...

📺 Dan Martell

👁️ 61K • 👍 2K • 💬 118 • ⏱️ 14:06 • 2d ago

---

**[Google Just Dropped The Singularity Bomb](https://www.youtube.com/watch?v=BH5_FEJNOGY)**

Google DeepMind's Demis Hassabis says humanity may already be standing in the foothills of the singularity. AI agents are now ...

📺 AI Revolution

👁️ 49K • 👍 2K • 💬 198 • ⏱️ 13:24 • 1d ago

---

**[They Are Building A &quot;New God&quot; | Revelation 13 and the AI Image Of The Beast](https://www.youtube.com/watch?v=ErNmkFo0COw)**

They are building an ai god, is this the image of the beast from Revelation 13? Today I look at this end times prophecy from the ...

📺 Sling and Stone

👁️ 17K • 👍 2K • 💬 333 • ⏱️ 16:13 • 1d ago

---

**[Harvard Grads Cheer Comedian Ronny Chieng&#39;s AI Speech](https://www.youtube.com/watch?v=0z7Q0Bg9TAY)**

In his keynote speech to Harvard graduates this week, The Daily Show host Ronny Chieng joked and warned students about AI.

📺 404 Media

👁️ 783K • 👍 34K • 💬 1K • ⏱️ 1:37 • 2d ago

---

**[We Asked AI To Simulate The First Woman President And The Results Are Exactly What You Expect](https://www.youtube.com/watch?v=AwXYrQxEnl8)**

We let AI run a simulation to see what the first female—that means woman— president in the White House would be like.

📺 The Babylon Bee

👁️ 102K • 👍 10K • 💬 913 • ⏱️ 1:34 • 1d ago

---

**[We Saw What AI Data Centers Don&#39;t Want You to See](https://www.youtube.com/watch?v=5p426fSlYH4)**

We investigated one of the world's largest AI data centers, using thermal drone footage to reveal the hidden pollution powering the ...

📺 PBS Terra

👁️ 694K • 👍 30K • 💬 6K • ⏱️ 21:45 • 2d ago

---

**[The AI Boom Is Coming to Your Backyard](https://www.youtube.com/watch?v=bA2rUkm7J9k)**

The rush to build AI data centers is drawing trillions of dollars in investment and long-term bets from infrastructure firms such as ...

📺 Bloomberg Television

👁️ 2K • 👍 60 • 💬 29 • ⏱️ 11:37 • 7h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 28,793 • ❤️ 601 • 4d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 18,327 • ❤️ 484 • 3d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,227,885 • ❤️ 1,097 • 1mo ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 405 • 4d ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 2,856 • ❤️ 980 • 2d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 17,084 • ❤️ 259 • 11h ago

---

**[PiD](https://huggingface.co/nvidia/PiD)**

*NVIDIA*

PiD is a conditional pixel-space diffusion model that unifies decoding and upsampling for image-to-image tasks. It performs super-resolution in a single pass, directly denoising in high-resolution pixel space, supporting up to 4x or 8x upscaling for various base models like Flux and SD3.

`image-to-image`

⬇️ 437 • ❤️ 190 • 4d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,918,111 • ❤️ 4,460 • 24d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 15,780 • ❤️ 454 • 12h ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 138,118 • ❤️ 418 • 9d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 204 • 💬 3 • ⭐ 3,086 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 82 • 💬 3 • ⭐ 80,871 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 27,494 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models](https://huggingface.co/papers/2605.30263)**

*Min Zhao, Hongzhou Zhu, Bokai Yan et al. (12 authors)*

A comprehensive framework is presented for converting bidirectional video diffusion models into real-time interactive world models with controllable, causal, and low-latency capabilities through fine-tuning and distillation techniques.

▲ 46 • 💬 2 • ⭐ 356 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.30263) • [💻 code](https://github.com/shengshu-ai/minWM)

---

**[stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation](https://huggingface.co/papers/2602.08968)**

*Lucas Maes, Quentin Le Lidec, Dan Haramati et al. (7 authors)*

🏢 galilai-group

Stable-worldmodel provides a modular and standardized research framework for developing and evaluating world models with controllable environmental factors for robustness and continual learning applications.

▲ 5 • 💬 0 • ⭐ 1,346 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.08968) • [💻 code](https://github.com/galilai-group/stable-worldmodel) • [🔗 project](https://galilai-group.github.io/stable-worldmodel/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 65,701 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 4 • 💬 1 • ⭐ 6,180 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[MOSS-TTS Technical Report](https://huggingface.co/papers/2603.18090)**

*Yitian Gong, Botian Jiang, Yiwei Zhao et al. (26 authors)*

🏢 OpenMOSS

MOSS-TTS is a speech generation model using discrete audio tokens and autoregressive modeling with capabilities for voice cloning, pronunciation control, and long-form generation across multiple languages.

▲ 14 • 💬 2 • ⭐ 2,543 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.18090) • [💻 code](https://github.com/OpenMOSS/MOSS-TTS) • [🔗 project](https://mosi.cn/models/moss-tts)

---

**[Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of
  Encoders](https://huggingface.co/papers/2408.15998)**

*Min Shi, Fuxiao Liu, Shihao Wang et al. (15 authors)*

Mixture of vision encoders and resolutions in multimodal large language models improves performance through concatenation of visual tokens and a Pre-Alignment mechanism, leading to superior results on benchmarks.

▲ 86 • 💬 3 • ⭐ 1,553 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2408.15998) • [💻 code](https://github.com/nvlabs/eagle)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 75,412 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.4k • 🔱 542 • 1d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.0k • 🔱 633 • 8h ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.8k • 🔱 192 • 10h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 399 • 8d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.3k • 🔱 359 • 13d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 2.2k • 🔱 201 • 1d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.1k • 🔱 145 • 5h ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.0k • 🔱 209 • 5d ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.9k • 🔱 227 • 23d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.8k • 🔱 209 • 17h ago

---

---

*Generated by PeekDeck - A glance is all you need*
