---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-27T13:44:33.953884+00:00'
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

**Last Updated:** June 27, 2026 at 13:44 UTC  
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

**[So now scraping data without permission is bad for AI training all of sudden?](https://www.reddit.com/r/artificial/comments/1ugwccs/so_now_scraping_data_without_permission_is_bad/)**

Oh .... the irony!

6h ago

---

**[I have it on good authority that Google are going to be hit with export controls soon.](https://www.reddit.com/r/artificial/comments/1uh2fc5/i_have_it_on_good_authority_that_google_are_going/)**

33m ago

---

**[What "AI Layoffs" Tell Us About the Companies Claiming Them](https://www.reddit.com/r/artificial/comments/1ugysid/what_ai_layoffs_tell_us_about_the_companies/)**

What all the "AI Layoffs" are telling us is that companies would rather compete by being cheaper than by being better. There are really two main competitive pathways for businesses: Do the same thing as your competition, but for a lower cost. Do something better than your competition at a reasonable cost. No one who has experience using AI for anything should say they feel comfortable letting it run free without any human supervision, but many businesses now are doing just that...and oftentimes it's apparent they are using AI tools with no oversight (just look at my LinkedIn DMs). So, it seems that the value equation for most of these businesses weighs more heavily for cost-cutting than on the "lesser" expense of AI, resulting in costly miscalculations. If anything, it seems more logical to keep your employees and EMPOWER/AUGMENT THEM with AI tools than to reduce headcount and try to completely replace an employee with an AI tool.

3h ago

---

**[Google keeps losing top ai researchers, the moat was never the weights](https://www.reddit.com/r/artificial/comments/1ugbwol/google_keeps_losing_top_ai_researchers_the_moat/)**

Shazeer to openai, then John Jumper (the alphaFold nobel guy) to anthropic, plus Adler and Pritzler out the same door within a week. Every time one of these drops the framing is google is bleeding. I think people are reading it backwards. If the people who actually trained the thing can leave and instantly matter at a competitor, the weights were never the asset. The judgment about how to steer a model, what to eval it on, where it breaks, that stuff lives in heads not in checkpoints. Hardware you can buy. That you cannot. What it means for the rest of us is simpler than the talent drama. If capability is going to keep walking between labs every few months, betting your whole stack on one provider's model is a bet on that lab keeping its people, which is the one thing you cannot control. I stopped caring which lab is quote winning this quarter. The move is keeping the model layer swappable so a shakeup at one place does not strand the work. Mine runs through verdent with byok but honestly any setup that lets you reroute works, the point is not the tool, it is not being married to one model.

21h ago

---

**[Same memory, different model. Why do local 8B models use memory worse?](https://www.reddit.com/r/artificial/comments/1uh1xbs/same_memory_different_model_why_do_local_8b/)**

I’ve been building FERNme, an open-source, brain-inspired memory engine for AI agents. While testing, I noticed something interesting. With the same FERNme memory, graph, and retrieval pipeline, a stronger API reasoning model performed very well in my initial tests, while a lightweight local 8B model occasionally made mistakes. The memory itself didn’t change, only the reasoning model did. This made me think memory and reasoning are separate problems. Human memory also isn’t useful just because something is stored. We use context and reasoning to decide which memories matter in a situation. FERNme exposes signals like strength, salience, uncertainty, provenance, age, contradictions, and related memories. But the model still has to interpret those signals correctly. So I’m now experimenting with an agent layer on top of FERNme to help smaller local models retrieve and reason over memory more effectively, while keeping the memory engine model-agnostic. For people building local AI agents: have you seen similar behavior? Would you focus on improving the memory engine itself, adding an agent layer over retrieval, or using more structured prompting / deterministic steps to help smaller models interpret memory better?

56m ago

---

**[Anyone else feel like a ghost in the machine? The bizarre isolation of AI training.](https://www.reddit.com/r/artificial/comments/1uh1swn/anyone_else_feel_like_a_ghost_in_the_machine_the/)**

I have been working in the AI training and data annotation space for a while now, and it is easily one of the strangest industries I have ever been a part of. On one hand, the perks are real. The flexibility is unmatched, you can work in your sweatpants, and sometimes you get genuinely fascinating prompts that actually challenge your brain, whether you are grading complex code, checking historical facts, or analyzing legal logic. But on the other hand, the complete and total isolation is starting to get pretty bizarre. We are helping build the future of technology, yet we do it in total silos. If you have ever been in an official platform Slack or forum, you know the vibe. You are constantly walking on eggshells. You cannot openly ask about sudden dry spells, you cannot critique confusing or contradictory guidelines without worrying about a random shadowban, and the second a project ends, you are instantly booted from the channel. Any temporary "coworkers" you had just vanish overnight. It feels like the platforms go out of their way to keep us from actually talking to one another without a moderator watching over our shoulders. It is a weird mix of having total freedom but zero community. I am curious what everyone else’s experience has been like lately. What are your personal pros and cons of the gig right now? How do you deal with the isolation, or do you actually prefer the ghost lifestyle? Also, out of pure curiosity, how do you even explain what you do for a living to your friends and family without their eyes glazing over?

1h ago

---

**[at what point do logs and dashboards stop being enough for llm costs?](https://www.reddit.com/r/artificial/comments/1uh0hu2/at_what_point_do_logs_and_dashboards_stop_being/)**

Hello everyone, currently digging into workflow-layer economics and trying to figure out how people track unexpected runtime spikes at scale. At an early stage simple margin buffers are fine because volume is bounded. But once you move past basic apps, factors like failed loops, retries, and context window inflation create a ton of cost variance that is hard to forecast or map to clean client billing. For those running agent or voice workflows in production, or working on complex ai products what do you currently use to understand costs and failures at the individual workflow level? More importantly, what's something you still can't easily answer with your current setup? Like why did a specific workflow suddenly cost 2x more, or which exact customer trigger is driving the increase? Are you guys just manually digging through raw api logs to catch leakage like infinite loops, or has it not become a big enough issue for your teams yet? Curious to hear how other teams handle the infrastructure discipline here.

2h ago

---

**[GNOME AI assistant adds image generation support](https://www.reddit.com/r/artificial/comments/1ugzpi1/gnome_ai_assistant_adds_image_generation_support/)**

In development over the past three years has been Newelle as a GNOME-aligned AI virtual assistant

🔗 [phoronix.com](https://www.phoronix.com/news/GNOME-Newelle-Image-Gen) • 2h ago

---

**[Anthropic just published data showing 35% of their users expect AI to do MOST of their work within 12 months. We’re not having an honest conversation about what this actually means.](https://www.reddit.com/r/artificial/comments/1ugaq5b/anthropic_just_published_data_showing_35_of_their/)**

Anthropic dropped their June 2026 Economic Index today and buried inside the survey data is something that should be making headlines: Over a third of respondents (9,700 actual Claude users, linked to real usage data) believe AI will be capable of handling most or nearly all of their work tasks within the next year. Not “some tasks.” Not “help me write emails.” MOST of their work. And here’s the part nobody wants to talk about: the people who delegate the most to AI are the MOST optimistic about their job prospects. Meanwhile entry-level workers are the ones most worried about displacement. Senior devs and managers? Thriving. Junior colleagues? Everyone in the survey is more worried about them than themselves. The data also shows AI autonomy is measurably higher on Claude Code than on regular chat, across 26 out of 31 output types. A blog post that takes 13 rounds of back-and-forth on Claude.ai? Claude Code does it in a single prompt. So here’s the uncomfortable question nobody wants to ask: Are we witnessing the largest skill-premium compression in history, where the gap between a senior person using AI and a junior person using AI collapses the value of experience? Or is this actually fine and we’re all just catastrophizing? Because Anthropic’s own framing spins this as “augmentation not displacement” while simultaneously showing that 38% of people who think they’ll lose their job attribute that directly to AI. Make it make sense. Full report: https://www.anthropic.com/research/economic-index-june-2026-report

21h ago

---

**[do you think ai will add more jobs than it will cut over the long run?](https://www.reddit.com/r/artificial/comments/1ugki2w/do_you_think_ai_will_add_more_jobs_than_it_will/)**

if so, what would these jobs look like?

15h ago

---

---

## Google News: "ai"

**[US government allows Anthropic limited release of AI model that sparked cybersecurity concerns](https://www.cnn.com/2026/06/26/tech/anthropic-mythos-release)**

The US government has allowed Anthropic to release its powerful Mythos AI model to select companies and organizations, revising license requirements after ordering an export block earlier this month in the wake of national security fears.

CNN • 13h ago

---

**[AI glasses are aiding cheating in exams. Test-obsessed Asia is ground zero](https://www.cnn.com/2026/06/26/asia/ai-glasses-cheating-exams-intl-hnk)**

For as long as there have been tests in schools, students have found ways to cheat, whether its peeking over a classmate’s shoulder or scribbling notes on a palm or crib sheet.

CNN • 12h ago

---

**[The AI backlash is only getting started](https://www.economist.com/leaders/2026/06/25/the-ai-backlash-is-only-getting-started)**

The Economist • 2d ago

---

**[Advertisers Are Good at Getting Human Attention. Can They Stand Out to A.I.?](https://www.nytimes.com/2026/06/27/business/dealbook/ai-visibility.html)**

The New York Times • 1h ago

---

**[AI’s Energy Crunch Has Investors Searching for Next IPO Winners](https://www.bloomberg.com/news/articles/2026-06-27/wall-street-bets-billions-on-power-firms-as-ai-boom-drives-ipo-rush)**

Bloomberg.com • 44m ago

---

**[Exclusive / Threats to US payment rails helped trigger Bessent’s AI worries](https://www.semafor.com/article/06/26/2026/bessent-engaged-on-ai-following-warnings-about-fed-payment-rails)**

Advanced models have heightened banks’ fears of an outage that would hamstring their ability to send money.

Semafor • 20h ago

---

**[Oracle stock has worst week since 2001 dot-com bust as AI financing concerns escalate](https://www.cnbc.com/2026/06/26/oracle-stock-ends-worst-week-since-2001-as-investors-dwell-on-finances.html)**

Oracle's surging spending, negative free cash flow and $130 billion debt pile are weighing on the stock.

CNBC • 17h ago

---

**[AI stocks melt down again. What’s going on?](https://www.cnn.com/2026/06/26/investing/tech-stocks-nasdaq-kospi)**

Tech stock traders can be an impatient bunch. But lately, they’ve grown seriously ticked off about the high price they’ve paid to get into the AI game without the profit boost they were expecting.

CNN • 1d ago

---

**[AI turbocharged the stock market. Now it’s firing up the economy.](https://www.marketwatch.com/story/ai-turbocharged-the-stock-market-now-its-firing-up-the-economy-193d2eb1)**

MarketWatch • 44m ago

---

**[Mark Cuban lays out a strategy for AI companies and data centers to win the PR battle. Hint: It's not hiring celebrity spokespeople.](https://finance.yahoo.com/technology/ai/article/mark-cuban-lays-out-a-strategy-for-ai-companies-and-data-centers-to-win-the-pr-battle-hint-its-not-hiring-celebrity-spokespeople-090000827.html)**

Billionaire Mark Cuban has ideas for how the companies behind massive data centers can win public support.

Yahoo Finance • 1d ago

---

---

## HackerNews: "ai"

**[Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://news.ycombinator.com/item?id=48664814)**

⬆️ 796 • 💬 1297 • 2d ago • [reuters.com](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)

---

**[Ford AI hiccups push carmaker to rehire ‘gray beard’ inspectors](https://news.ycombinator.com/item?id=48674446)**

⬆️ 600 • 💬 321 • 1d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-06-25/ford-has-been-rehiring-quality-inspectors-after-ai-fell-short)

---

**[U.S. allows Anthropic to release Mythos AI to ‘trusted’ US organizations](https://news.ycombinator.com/item?id=48692995)**

The move comes the same day as a new OpenAI model sees a limited release.

⬆️ 486 • 💬 634 • 14h ago • [semafor.com](https://www.semafor.com/article/06/27/2026/us-releases-powerful-anthropic-model-mythos-to-some-us-companies)

---

**[RubyLLM: A Ruby framework for all major AI providers](https://news.ycombinator.com/item?id=48660711)**

A single, beautiful Ruby framework for all major AI providers. Easily build chatbots, AI agents, RAG applications, content generators, and every AI workflow you can think of.

⬆️ 445 • 💬 82 • 2d ago • [RubyLLM](https://rubyllm.com/)

---

**[Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion](https://news.ycombinator.com/item?id=48675435)**

Beautiful, AI-native markdown editor and LLM Wiki. Contribute to inkeep/open-knowledge development by creating an account on GitHub.

⬆️ 370 • 💬 170 • 1d ago • [GitHub](https://github.com/inkeep/open-knowledge)

---

**[What happened after 2k people tried to hack my AI assistant](https://news.ycombinator.com/item?id=48681687)**

⬆️ 365 • 💬 160 • 1d ago • [fernandoi.cl](https://www.fernandoi.cl/posts/hackmyclaw/)

---

**[Apple to skip high-end M6 Mac chips in favor of AI-focused M7 line](https://news.ycombinator.com/item?id=48676795)**

⬆️ 310 • 💬 368 • 1d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-06-25/apple-to-skip-high-end-m6-mac-chips-to-launch-m7-pro-m7-max-m7-ultra-instead?embedded-checkout=true)

---

**[For most of the world, open-source AI is the only way forward](https://news.ycombinator.com/item?id=48660839)**

Proprietary AI is both too expensive and too centralized in control for most countries and companies to rely upon.

⬆️ 234 • 💬 144 • 2d ago • [Techstrong.ai](https://techstrong.ai/articles/for-most-of-the-world-open-source-ai-is-the-only-way-forward/)

---

**[AI children's books, body horror edition](https://news.ycombinator.com/item?id=48681250)**

⬆️ 207 • 💬 77 • 1d ago • [lcamtuf.substack.com](https://lcamtuf.substack.com/p/ai-childrens-books-body-horror-edition)

---

**[Political bias in AI: Where the AI models stand](https://news.ycombinator.com/item?id=48672779)**

Political bias in AI measures where every major AI model stands on charged political and ethical questions: run many times, no web search, plotted with error...

⬆️ 174 • 💬 304 • 2d ago • [Trakkr](https://trakkr.ai/bias)

---

---

## YouTube Videos: "ai"

**[People Are Finally Waking Up About AI - And They’re Sick of It](https://www.youtube.com/watch?v=BDfTt2yUu4E)**

Subscribe to My New Clips Channel https://www.youtube.com/@MichaelBordenaroClips ======= Need a Real Estate Agent You ...

📺 Michael Bordenaro

👁️ 37K • 👍 3K • 💬 825 • ⏱️ 26:21 • 17h ago

---

**[Why South Korea’s AI Stock Mania Is a Warning to the World](https://www.youtube.com/watch?v=jJrEnv1IDvg)**

South Korea's stock market has surged about 200% year-on-year, powered by retail investors chasing an artificial ...

📺 Bloomberg Originals

👁️ 271K • 👍 4K • 💬 453 • ⏱️ 9:20 • 1d ago

---

**[AI News: The New Model That&#39;s As Good As Fable](https://www.youtube.com/watch?v=zMVZvgCOr40)**

Stop losing money on separate AI subscriptions. Get ChatGPT, Claude, Gemini, and 200+ models in one place for one price with ...

📺 Matt Wolfe

👁️ 57K • 👍 2K • 💬 161 • ⏱️ 20:01 • 20h ago

---

**[Z.ai Chinese AI Comparable to OpenAI and Anthropic - China Tech Beating USA Sanctions](https://www.youtube.com/watch?v=B2N5DC6qkI0)**

Spotify - https://open.spotify.com/show/1KkKuQe82tf1bW78ReQ0wM Apple Podcasts ...

📺 Eli the Computer Guy

👁️ 11K • 👍 542 • 💬 151 • ⏱️ 15:15 • 13h ago

---

**[This AI Brain Will Make You So Smart It’s Almost Unfair](https://www.youtube.com/watch?v=b4d32pBa3UY)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4amP5uh Are you building an AI software ...

📺 Dan Martell

👁️ 78K • 👍 3K • 💬 149 • ⏱️ 12:02 • 2d ago

---

**[Ancient scrolls unread for 2,000 years revealed with AI](https://www.youtube.com/watch?v=hcTnaI_djHQ)**

Researchers used AI and “virtual unwrapping” to reveal never-before-seen texts inside charred Roman scrolls buried by Mount ...

📺 NBC News

👁️ 264K • 👍 5K • 💬 652 • ⏱️ 3:00 • 1d ago

---

**[The AI Water Use Problem](https://www.youtube.com/watch?v=wx7ToT0G0qo)**

Go to https://ground.news/kylehill to get 40% off unlimited access to the news tool I actually trust. It helps you cut through the noise ...

📺 Kyle Hill

👁️ 257K • 👍 25K • 💬 4K • ⏱️ 21:59 • 1d ago

---

**[The AI Future No One Wants to Talk About](https://www.youtube.com/watch?v=zWQe2Fn--Eg)**

Go to https://ground.news/sabine to get 40% off the Vantage plan and see through sensationalized reporting. Stay fully informed ...

📺 Sabine Hossenfelder

👁️ 305K • 👍 18K • 💬 4K • ⏱️ 12:14 • 2d ago

---

**[Why the AI Era Will End Sooner Than You Think](https://www.youtube.com/watch?v=dtFu7baviTQ)**

Everyone keeps talking about the AI era like it's just beginning. But I think the public AI boom may end much sooner than people ...

📺 Coding with Dee

👁️ 14K • 👍 1K • 💬 179 • ⏱️ 7:31 • 19h ago

---

**[AI News: NotebookLM Update; Gemini Study Notebooks; Claude Design 2.0; and ChatGPT Is Now Better!!](https://www.youtube.com/watch?v=JfxLTPAjGgg)**

Try Lovart Today: https://www.lovart.ai/?sourceId=902604 Every week I bring you the latest AI news. This week I show you some ...

📺 Paul J Lipsky

👁️ 27K • 👍 1K • 💬 60 • ⏱️ 17:03 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 212,760 • ❤️ 1,102 • 3d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 98,994 • ❤️ 2,640 • 4d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 712,627 • ❤️ 639 • 4h ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 206,828 • ❤️ 709 • 8d ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 536,130 • ❤️ 2,417 • 8d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 30,298 • ❤️ 465 • 2d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 18,872 • ❤️ 342 • 2d ago

---

**[Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)**

*KREA*

Krea-2-Turbo is a text-to-image diffusion model capable of generating diverse artistic styles, including halftone, pixelated, impressionist, thermal imaging, and black and white photography. It is primarily used for creative image generation and artistic exploration.

`text-to-image`

⬇️ 17,445 • ❤️ 304 • 3d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 20,266 • ❤️ 273 • 1d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 57,521 • ❤️ 737 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 37 • 💬 4 • ⭐ 10,664 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 173 • 💬 2 • ⭐ 70,494 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 89,024 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 25,689 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 8 • 💬 1 • ⭐ 9,308 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 60 • 💬 1 • ⭐ 84,521 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 247 • 💬 4 • ⭐ 9,441 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 23 • 💬 1 • ⭐ 84,033 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Qwen-AgentWorld: Language World Models for General Agents](https://huggingface.co/papers/2606.24597)**

*Yuxin Zuo, Zikai Xiao, Li Sheng et al. (33 authors)*

🏢 Qwen

Language-based world models enable agentic environment simulation across multiple domains and enhance general agent performance through scalable simulation and improved downstream task performance.

▲ 132 • 💬 4 • ⭐ 573 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.24597) • [💻 code](https://github.com/QwenLM/Qwen-AgentWorld)

---

**[GLM-5: from Vibe Coding to Agentic Engineering](https://huggingface.co/papers/2602.15763)**

*GLM-5 Team, Aohan Zeng, Xin Lv et al. (186 authors)*

GLM-5 advances foundation models with DSA for cost reduction, asynchronous reinforcement learning for improved alignment, and enhanced coding capabilities for real-world software engineering.

▲ 187 • 💬 6 • ⭐ 5,570 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.15763) • [💻 code](https://github.com/zai-org/GLM-5)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 78.4k • 🔱 10.2k • 2m ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 61.1k • 🔱 3.1k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 10.9k • 🔱 1.0k • 2h ago

---

**[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG)**

The end of web parsing. The beginning of scalable pixel-native search.

`Python` `agent` `ai` `memory` `multimodal` `rag`

⭐ 5.5k • 🔱 429 • 32m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 5.1k • 🔱 624 • 16m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 3.0k • 🔱 402 • 6h ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.1k • 🔱 145 • 4d ago

---

**[Forward-Future/loop-library](https://github.com/Forward-Future/loop-library)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 1.7k • 🔱 153 • 15h ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.7k • 🔱 150 • 1d ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 86 • 14d ago

---

---

*Generated by PeekDeck - A glance is all you need*
