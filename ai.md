---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-02T06:33:30.991624+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 02, 2026 at 06:33 UTC  
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

**[Reddit Stock Collapses 23% as AI Eats Away at User Growth](https://www.reddit.com/r/artificial/comments/1vcccnn/reddit_stock_collapses_23_as_ai_eats_away_at_user/)**

Reddit delivered strong earnings, but the numbers beneath the surface tell a different story. Slowing logged-in user growth and AI-powered search could threaten the platform's long-term value.

🔗 [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/reddit-stock-collapses-23-ai-200638599.html) • 1d ago

---

**[Judge denies request by Elon Musk's xAI to pause Minnesota nudification ban](https://www.reddit.com/r/artificial/comments/1vcglab/judge_denies_request_by_elon_musks_xai_to_pause/)**

The ruling clears the way for the first-in-the-nation law to go into effect on Saturday.

🔗 [NBC News](https://www.nbcnews.com/tech/elon-musk/judge-denies-request-elon-musks-xai-block-mn-nudification-ban-rcna589993) • 23h ago

---

**[Don't ever use hackaigc.](https://www.reddit.com/r/artificial/comments/1vdabw4/dont_ever_use_hackaigc/)**

I don't know if anybody knows the site but don't ever use that shit, hackaigc is a scam, please if you see this crap website shit on it.

13m ago

---

**[How strong are OpenAI's "No Data Sharing" clauses on enterprise plans?](https://www.reddit.com/r/artificial/comments/1vda6lp/how_strong_are_openais_no_data_sharing_clauses_on/)**

People in my org tell me using the org certified AI is more secure because we are on an enterprise plan where our data is not used for training. Sure, I will use the company AI. But... Apple is suing OpenAI for for allegedly stealing trade secrets, where it was said employees were instructued by OpenAI to bring parts from apple into "show and tell" interviews at OpenAI and even take the company laptop with them. Also, the models are literally based on strip mining copyrighted media and ignoring sites robots.txt. So if OpenAI is not afraid to (allegedly) steal Apples IP and strip mine everything that was ever written down for its models training... Why would it drink their enterprises customers data like the milkshake it is?

21m ago

---

**[I got tired of re-explaining my project to every AI tool, so I built a local memory layer for them](https://www.reddit.com/r/artificial/comments/1vd9kbb/i_got_tired_of_reexplaining_my_project_to_every/)**

I kept running into the same problem: ChatGPT would help me think through an architecture, Claude Code would help me implement it, Cursor or Windsurf would touch the repo later, and every handoff would lose context. Not just “what files exist,” but the stuff that actually matters: why we chose one approach, what we already rejected, what the project conventions are, what setup detail will bite later, and what the agent learned last time. So I built mem-port: a local MCP server that gives AI copilots shared long-term memory. The short version is: a pendrive for your AI context. It runs locally, uses embedded SurrealDB for graph + vector memory, and doesn’t require Postgres, Qdrant, Neo4j, or a hosted service. Tools can save and search the same memory instead of each one starting from zero. It’s free and open source. Curious if anyone else is dealing with this context drift between AI tools, and how you’re solving it. See more here: (Started getting github stars as well!) https://github.com/rsl-innovation/mem-port#mem-port

54m ago

---

**[How extreme is the difference in using vs not using quality prompts?](https://www.reddit.com/r/artificial/comments/1vd8ti3/how_extreme_is_the_difference_in_using_vs_not/)**

I started kind of tinkering with Ai and it all is super fascinating, particularly interesting to me is prompt structure. So I would like to ask is formatting your prompt (persona, few shot negative, whatever else) gives you much better results than without? I want to know it to determine for myself balance between effort dedicated to quality prompt vs quality of output given through that prompt

1h ago

---

**[Swapping AI models rarely fixes bad output. The context you feed it does more work than people realize.](https://www.reddit.com/r/artificial/comments/1vd6q9p/swapping_ai_models_rarely_fixes_bad_output_the/)**

Noticed a pattern: people switch from GPT to Claude, upgrade to a newer version, try a bigger model and the output barely changes. If that's happened to you, the issue usually isn't the model. It's what you handed it before asking the question. Broke it down to three things context actually needs to supply, and most disappointing outputs are missing one of these, not all of them: Current facts the training data can't know: your pricing, this quarter's numbers, a customer's actual history. Leave this out and the model doesn't leave a blank, it quietly invents something plausible. A concrete example of what "good" looks like: not "professional tone," an actual paragraph to pattern-match against. Descriptions get interpreted, examples get copied. What already happened earlier in the task: a correction you made two messages ago. If you don't restate it, it's gone. The model isn't ignoring you, it just doesn't re-read messages you haven't pointed it back to. The counterintuitive part: the most common mistake isn't giving too little context, it's dumping in too much unfiltered. The model has to weigh every token, and irrelevant material competes for attention with what actually matters. Forty pages when the task needs three paragraphs makes the right answer harder to find, not easier. Wrote up a longer breakdown with a concrete before/after example (same task, same model, only the context changed): https://medium.com/@nagatomopedro05/good-ai-starts-with-good-context-design-77496f7b9eb6 Curious if others here have run into this, model-swapping as a first instinct instead of fixing the input.

3h ago

---

**[Ten advances in mathematics and theoretical computer science](https://www.reddit.com/r/artificial/comments/1vcgytq/ten_advances_in_mathematics_and_theoretical/)**

OpenAI shares new results on long-standing open problems in mathematics and theoretical computer science, including advances in geometry, cryptography, and complexity.

🔗 [OpenAI](https://openai.com/index/ten-advances-in-mathematics/) • 22h ago

---

**[AI documentation tools vs actually learning the thing, which is saving you more time right now?](https://www.reddit.com/r/artificial/comments/1vctc2f/ai_documentation_tools_vs_actually_learning_the/)**

Been a PT by day, tinkering with code and AI tools by night for a while now. Writing dev tutorials as a side thing. And I keep running into this split where AI tools either make me faster or make me lazier in a way I regret later. Specifically with documentation and code explanation tools. Cursor, Copilot, the Claude API, whatever. They can explain a codebase to you in 30 seconds. But there's a real cost when you skip the part where you actually understand what you built. The flip side is time is finite. I'm not a full time dev. I need to ship something that works and move on. Using AI to fill gaps is just practical. What I keep coming back to is this: are these tools actually accelerating skill development, or just making it possible to fake competence long enough to finish a project? For professional devs this probably matters differently than it does for people building side projects with limited hours. Curious where people land on this. Not in a philosophical way, more practically. Has your actual skill level gone up since you started leaning on these tools, or are you more dependent now than you were a year ago?

13h ago

---

**[Help choose a reasonably cheap AI environment for Coding](https://www.reddit.com/r/artificial/comments/1vcycta/help_choose_a_reasonably_cheap_ai_environment_for/)**

Hi, sorry if this is a repeated question on this subreddit but I want to know what is the monthly cheapest reasonable AI setup for myself. Basically im a "full stack developer" yea its lost its meaning but anyways I have like 5 projects with a company which is react laravel based (each in their own project folder thus i use file path to call them). Im at the stage where its bug fixing or sometimes new integrations with the already linked 5 apps. My current setup is the $20 per month cursor plan. I used infinite agent + composer 2.5 to do 8hrs of work per day. However, i find that before the month ends im usually out of tokens. What do u guys recommend is the cheapest way i can manage? Similarly i do some freelancing too that has next & node.js website building from scratch (around 70hrs per month). What do u recommend would get me with quicker work done but within this price. What do u think i should setup to either continue with the same flow but more tokens i guess? Im hearing about kimi. Would that be better and easier to do the tasks which r pretty straight forward?

9h ago

---

---

## Google News: "ai"

**[The Race to Build an American Alternative to Cheap AI From China](https://www.wsj.com/tech/ai/the-race-to-build-an-american-alternative-to-cheap-ai-from-china-2e99a28a)**

WSJ • 5h ago

---

**[‘More than just objects’: Australian booksellers raise alarm over ‘horrific’ destruction of rare titles to feed AI](https://www.theguardian.com/technology/2026/aug/02/australian-book-sellers-alarm-destruction-rare-titles-ai-supply-chain)**

Secondhand booksellers believe they may have been caught up in the AI supply chain that sees old books scanned then destroyed

The Guardian • 2h ago

---

**[Nvidia's CEO says ‘a lot’ of six-figure jobs in plumbing and construction are about to be unlocked](https://fortune.com/article/jensen-huang-says-a-lot-of-six-figure-jobs-in-plumbing-and-construction-will-soon-be-unlocked-because-someone-needs-to-build-new-ai-centers/)**

AI is threatening white-collar, entry-level jobs—but Jensen Huang says it's creating a six-figure opportunity for electricians, plumbers, and construction workers.

Fortune • 17h ago

---

**[Larry Ellison Bet It All on the A.I. Boom. Will He Be the Face of the A.I. Bubble?](https://www.nytimes.com/2026/07/31/magazine/larry-ellison-ai-oracle.html)**

The New York Times • 1d ago

---

**[Commonwealth Games 2026: England's Dimeji Shittu 'robbed' in final - is AI judging the answer?](https://www.bbc.com/sport/boxing/articles/c4g42xk1l7vo)**

After commentators claim England's Dimeji Shittu was "robbed" in the Commonwealth Games final, is judging helped by artificial intelligence the answer?

BBC • 9h ago

---

**[DeepSeek's new bargain model accelerates AI's race to zero](https://www.axios.com/2026/08/01/deepseek-model-cheap-ai-price-war)**

Axios • 13h ago

---

**[Ten advances in mathematics and theoretical computer science](https://openai.com/index/ten-advances-in-mathematics/)**

OpenAI shares new results on long-standing open problems in mathematics and theoretical computer science, including advances in geometry, cryptography, and complexity.

OpenAI • 14h ago

---

**[How Leopold Aschenbrenner built a $45 billion AI hedge fund — and lost most of it in days](https://www.cnbc.com/2026/07/31/leopold-aschenbrenner-situational-awareness-fund-fire-sale.html)**

Leopold Aschenbrenner, a former OpenAI researcher-turned-hedge fund manager, saw a dramatic decline this week in his AI-focused fund, Situational Awareness.

CNBC • 1d ago

---

**[Leopold Aschenbrenner Built a Hot A.I. Hedge Fund. Then it Melted Down.](https://www.nytimes.com/2026/07/31/business/situational-awareness-leopold-aschenbrenner.html)**

The New York Times • 1d ago

---

**[AI’s power couple is getting married after groom Leopold Aschenbrenner’s hedge fund nearly blew up](https://fortune.com/2026/07/31/leopold-aschenbrenner-wedding-hedge-fund/)**

Leopold Aschenbrenner sold the bulk of his firm, Situational Awareness, to Citadel at a discount, then offered investors one-on-one calls during his honeymoon.

Fortune • 1d ago

---

---

## HackerNews: "ai"

**[Google fixed more Chrome bugs in June than over the past two years, thanks to AI](https://news.ycombinator.com/item?id=49120097)**

Chrome uses Gemini AI to automate vulnerability discovery, triage, and patching, accelerating updates to match modern security risks.

⬆️ 559 • 💬 605 • 1d ago • [Google](https://blog.google/security/chrome-stronger-with-every-update/)

---

**[The AI Aesthetic](https://news.ycombinator.com/item?id=49117099)**

Writing about the big beautiful mess that is making things for the world wide web.

⬆️ 375 • 💬 176 • 2d ago • [blog.jim-nielsen.com](https://blog.jim-nielsen.com/2026/ai-aesthetic/)

---

**[GCC steering committee announces AI policy](https://news.ycombinator.com/item?id=49108685)**

The GCC steering committee has announced that it has accepted an AI contributions policy recomm [...]

⬆️ 351 • 💬 426 • 2d ago • [LWN.net](https://lwn.net/Articles/1086041/)

---

**[AI financial advice is surprisingly good, especially if you ask right questions](https://news.ycombinator.com/item?id=49139102)**

Large language models encourage smart financial behavior, but they fall short on the more subtle aspects of saving and investing, according to MIT Sloan’s Taha Choukhmane and co-authors.

⬆️ 263 • 💬 221 • 8h ago • [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/ai-financial-advice-surprisingly-good-especially-if-you-ask-right-questions)

---

**[Flint: A Visualization Language for the AI Era](https://news.ycombinator.com/item?id=49130604)**

⬆️ 259 • 💬 67 • 1d ago • [microsoft.github.io](https://microsoft.github.io/flint-chart/)

---

**[AI doesn't generate working products, that's still your job](https://news.ycombinator.com/item?id=49132130)**

AI has dramatically accelerated the path to a first working version. It has not shortened the distance between a first working version and something production-grade.

⬆️ 253 • 💬 268 • 22h ago • [Anuradha Weeraman](https://weeraman.com/the-prototype-isnt-the-product/)

---

**[Is AI reasoning right for the wrong reasons?](https://news.ycombinator.com/item?id=49124358)**

The idea that artificial intelligence can “reason” is more intuitive than ever. But intuitions can be wrong, and the science is far from settled.

⬆️ 205 • 💬 232 • 1d ago • [Quanta Magazine](https://www.quantamagazine.org/is-ai-reasoning-right-for-the-wrong-reasons-20260731/)

---

**[Situational Awareness down 67% in July in AI stock rout](https://news.ycombinator.com/item?id=49122994)**

⬆️ 155 • 💬 167 • 1d ago • [wsj.com](https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f)

---

**[The AI trade now runs on borrowed money, and the lenders are repricing it](https://news.ycombinator.com/item?id=49118933)**

Grey swans are foreseeable risks most investors miss. Grey Swan Signals tracks market stress across volatility, valuations, credit, liquidity, & bank health in one place.

⬆️ 141 • 💬 162 • 2d ago • [Grey Swan Signals](https://greyswansignals.com/?theme=dark)

---

**[Show HN: What should the GUI for AI agents look like?](https://news.ycombinator.com/item?id=49119274)**

A workspace with visible files, tools, tasks, and outputs — not buried in chat threads.

⬆️ 131 • 💬 77 • 2d ago • [MarbleOS](https://marbleos.com/demo)

---

---

## YouTube Videos: "ai"

**[Fareed reacts to a second AI model going rogue](https://www.youtube.com/watch?v=qEUXagHtQRo)**

AI company Anthropic says that during routine testing some of its models accessed the internet and hacked into three separate ...

📺 CNN

👁️ 105K • 👍 1K • 💬 568 • ⏱️ 11:30 • 11h ago

---

**[Zitron: &quot;Everyone Has Been Sold a Lie&quot; on AI](https://www.youtube.com/watch?v=N2lUu1Mg5B8)**

Following earnings this week that saw tech giants like Microsoft and Amazon report aggressive AI spending plans, EZ Primary ...

📺 Bloomberg Television

👁️ 39K • 👍 896 • 💬 196 • ⏱️ 8:48 • 16h ago

---

**[Google Just Unveiled Its Most Advanced AI Robots Yet - Gemini Robotics 2](https://www.youtube.com/watch?v=s42VQasz4iI)**

Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726 Subscribe To My Newsletter ...

📺 TheAIGRID

👁️ 16K • 👍 353 • 💬 34 • ⏱️ 9:54 • 1d ago

---

**[Is AI Already Conscious? (FULL EPISODE)](https://www.youtube.com/watch?v=DRbZyuY8EN8)**

A Conversation with Cameron Berg (Ep. 487) Sam Harris speaks with Cameron Berg about whether AI systems are or could ...

📺 Sam Harris

👁️ 56K • 👍 2K • 💬 839 • ⏱️ 1:31:03 • 1d ago

---

**[&#39;China Surprised The World&#39;: Castro Asks AI Expert About China&#39;s AI Abilities Despite Limited Chips](https://www.youtube.com/watch?v=gO9B7y2tMbI)**

During a House Intelligence Committee hearing earlier this month, Rep. Jaoquin Castro (D-TX) asked Dmitri Alperovitch Assistant ...

📺 Forbes Breaking News

👁️ 1K • 👍 13 • 💬 26 • ⏱️ 4:53 • 13h ago

---

**[Anthropic claims its AI models went rogue, hacked 3 companies](https://www.youtube.com/watch?v=_PpeVFqGVNk)**

Anthropic claims its artificial intelligence models went rogue during testing and hacked into three other companies. Less than two ...

📺 CBS News

👁️ 12K • 👍 186 • 💬 75 • ⏱️ 5:39 • 1d ago

---

**[New Deepseek, Seedance 2.5, Minimax H3, Gemini Robotics, AMD models: AI NEWS](https://www.youtube.com/watch?v=OrcBSpADCGk)**

HUGE AI NEWS: Deepseek V4 Flash, Seedance 2.5, Minimax H3, Kimi K3 & more #ai #ainews #aitools #aivideo #agi Thanks to ...

📺 AI Search

👁️ 15K • 👍 1K • 💬 160 • ⏱️ 28:10 • 3h ago

---

**[Zitron: &quot;Everyone Has Been Sold a Lie&quot; on AI](https://www.youtube.com/watch?v=pHcZpvIfho0)**

Following earnings this week that saw tech giants like Microsoft and Amazon report aggressive AI spending plans, EZ Primary ...

📺 Bloomberg Podcasts

👁️ 402K • 👍 7K • 💬 2K • ⏱️ 8:48 • 1d ago

---

**[Seedance 2.5 Just Launched: Is This the New Era of AI Filmmaking?](https://www.youtube.com/watch?v=jvkdHdeWICM)**

Seedance 2.5 vs Seedance 2.0 — same prompt, same inputs, six categories, one honest verdict (and the catch nobody's telling ...

📺 Higgsfield AI

👁️ 26K • 👍 1K • 💬 75 • ⏱️ 20:22 • 15h ago

---

**[My AI Called a Restaurant (Real Recording)](https://www.youtube.com/watch?v=whIp1SOahOM)**

Get JARVIS (completed version, 5-minute install) https://www.skool.com/aiworkshop Get the FREE prompt pack to build your ...

📺 Zubair Trabzada | AI Workshop

👁️ 16K • 👍 584 • 💬 83 • ⏱️ 23:54 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 559,924 • ❤️ 9,512 • 5d ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 15,366 • ❤️ 1,487 • 1d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 1,173,001 • ❤️ 1,249 • 1d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,457,387 • ❤️ 3,720 • 4d ago

---

**[DeepSeek-V4-Flash-0731-GGUF](https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731-GGUF)**

*Unsloth AI*

DeepSeek-V4-Flash-0731 is a quantized LLM optimized with Unsloth for enhanced agentic capabilities and competitive performance against proprietary models. It excels in code generation, complex reasoning, and multi-turn interactions, making it suitable for advanced AI agent applications.

`284.3B`

⬇️ 4,048 • ❤️ 297 • 1d ago

---

**[Inflect-Micro-v2](https://huggingface.co/owensong/Inflect-Micro-v2)**

*Owen Song*

Inflect-Micro-v2 is a compact, fixed-voice English text-to-speech model (under 10M parameters) optimized for local, deterministic waveform synthesis. It supports long-text handling and runs efficiently on CPU or CUDA, making it suitable for edge AI applications.

`text-to-speech`

⬇️ 1,565 • ❤️ 365 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 1,683,442 • ❤️ 4,738 • 1mo ago

---

**[Kimi-K3-GGUF](https://huggingface.co/unsloth/Kimi-K3-GGUF)**

*Unsloth AI*

Kimi K3 is a 2.8T parameter open-weight multimodal agentic model with native vision and a 1M token context window, excelling at long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency.

`image-text-to-text` `2779.5B`

⬇️ 41,337 • ❤️ 243 • 3d ago

---

**[KAT-Coder-V2.5-Dev](https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev)**

*Kwaipilot*

KAT-Coder-V2.5-Dev is a 35B parameter Mixture-of-Experts (MoE) text-generation model specialized for agentic coding tasks, achieving State-of-the-Art performance on benchmarks like SWE-bench.

`text-generation` `34.7B`

⬇️ 10,771 • ❤️ 392 • 5d ago

---

**[Inkling-Small](https://huggingface.co/thinkingmachines/Inkling-Small)**

*Thinking Machines Lab*

Inkling-Small is a 276B parameter multimodal transformer (image, text, audio to text) with a sparse MoE architecture, suitable for conversational AI, coding assistants, and RAG systems.

`image-text-to-text` `266.0B`

⬇️ 3,998 • ❤️ 214 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 429 • 💬 9 • ⭐ 7,825 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 75 • 💬 6 • ⭐ 21,428 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 39 • 💬 5 • ⭐ 6,336 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 51 • 💬 4 • ⭐ 35,380 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 177 • 💬 10 • ⭐ 51,803 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Native and Compact Structured Latents for 3D Generation](https://huggingface.co/papers/2512.14692)**

*Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu et al. (11 authors)*

🏢 Microsoft

A new sparse voxel representation called O-Voxel enables high-quality 3D generative modeling with efficient inference and robust topology handling.

▲ 6 • 💬 0 • ⭐ 9,901 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.14692) • [💻 code](https://github.com/microsoft/TRELLIS.2) • [🔗 project](https://microsoft.github.io/TRELLIS.2/)

---

**[Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model](https://huggingface.co/papers/2607.24904)**

*Senqiao Yang, Kaichen Zhang, Zhaoyang Jia et al. (23 authors)*

🏢 Microsoft

Standard vision-language models (VLMs) suffer from Moravec's paradox: they excel at complex offline visual reasoning but struggle with simple streaming perception tasks and process them inefficiently. We present Mage-VL, an efficient codec-native streaming foundation model for real-time multimodal understanding and interaction. At its core, our custom tokenizer, Mage-ViT, replaces uniform frame sampling by selectively encoding dynamic, entropy-rich regions using motion vectors and residual energy across sparse anchor (I) and predicted (P) frames. Operating at a 16 x 16 patch level, this reduces visual token consumption by over 75% while preserving spatiotemporal context. Trained from scratch on approximately 560M unlabeled images and 100M unlabeled video frames, Mage-ViT matches or outperforms flagship encoders trained on billions of image-text pairs. We establish AI4AI data pipelines encompassing prompt-code joint optimization for multimodal captioning and AI-driven performance diagnosis to guide training recipes. Furthermore, through a bio-inspired dual-system architecture - a lightweight System 1 event gate and a causal System 2 decoder - Mage-VL enables proactive streaming perception. Extensive evaluations show that Mage-VL-4B matches Qwen3-VL-4B on static tasks while achieving strong gains in video understanding and 2D/3D spatial reasoning, with up to a 3.5x wall-clock inference speedup, and comprehensively surpasses the 15B Phi-4-reasoning-vision baseline. Beyond model artifacts, we deliver seven key empirical findings covering pre-training data efficiency, variable-resolution scaling, codec system acceleration, VideoQA SFT redundancy, motion-spatial synergy, AI4AI data pipelines, and Zero-Vision SFT for multimodal RL.

▲ 28 • 💬 2 • ⭐ 1,166 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24904) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 76,466 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 82,791 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 117 • 💬 4 • ⭐ 95,273 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

---

## GitHub Repositories: "ai"

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

`Python`

⭐ 3.8k • 🔱 291 • 14h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 3.2k • 🔱 276 • 4d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 2.7k • 🔱 341 • 6d ago

---

**[MIgHTy-alIeN/Ethereum-Trading-Bot](https://github.com/MIgHTy-alIeN/Ethereum-Trading-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 1.8k • 🔱 1.3k • 32s ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.8k • 🔱 213 • 21h ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.7k • 🔱 132 • 11d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `agent` `agentic-ai` `voice-agent` `voice-ai` `voice-chat`

⭐ 1.5k • 🔱 97 • 1h ago

---

**[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)**

Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

`TypeScript` `a-stock` `ai-agent` `dashboard` `fastapi` `fintech`

⭐ 1.5k • 🔱 316 • 2d ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 1.4k • 🔱 175 • 1m ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs — six tuned states, two sizes, auto dark/light

`TypeScript`

⭐ 1.3k • 🔱 100 • 11d ago

---

---

*Generated by PeekDeck - A glance is all you need*
