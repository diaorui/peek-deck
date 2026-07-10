---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-10T19:00:58.331308+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 10, 2026 at 19:00 UTC  
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

**[Ai Agent company Lyzr raises 100 million in section B funding using an Ai agent](https://www.reddit.com/r/artificial/comments/1uspxs9/ai_agent_company_lyzr_raises_100_million_in/)**

4h ago

---

**[Any thoughts on this robot picking objects off a moving conveyor belt at 1x?](https://www.reddit.com/r/artificial/comments/1ustsai/any_thoughts_on_this_robot_picking_objects_off_a/)**

Found this going down a robot-control rabbit hole and it stuck with me. The belt keeps moving, so the target never sits still, which is the kind of thing that usually makes a robot lag or fumble. This one keeps pace by predicting where the scene is about to go and acting on that, then correcting on every new camera frame, instead of only reacting to the current instant. It is a video-action model called LingBot-VA 2.0. The clip is 1x with no cuts, so nothing is sped up. I will drop the source and the honest limits in a comment instead of overselling it here. Curious what people here make of it.

1h ago

---

**[Do modern speech AI models have a data problem more than a model problem?](https://www.reddit.com/r/artificial/comments/1usllkp/do_modern_speech_ai_models_have_a_data_problem/)**

I’ve been following recent progress in speech AI, and one thing I’ve been wondering about is whether current limitations are increasingly caused by training data rather than model architecture. Models seem much better than they were a few years ago, yet they still struggle with regional accents, code-switching, spontaneous speech, and speakers who don’t match “standard” pronunciation. My guess is that collecting this kind of data at scale is much harder than collecting carefully scripted recordings. If you were building a speech model today, where would you invest more effort: better models or more diverse speech data? Why?

7h ago

---

**[Cost Analysis of 33 AI Image Models](https://www.reddit.com/r/artificial/comments/1usj0l9/cost_analysis_of_33_ai_image_models/)**

My cost benchmark is back with more models and providers. Added Seedream models, Gemini 3.1 Flash Lite Image, GPT Image 1.5 and others. The cheapest and the priciest models are the same as before: Flux Fast Schnell at $0.0025 and Recraft 4 Pro at $0.25. The full report with price and latency comparison are on my blog. Enjoy!

9h ago

---

**[Updated: Millions of ChatGPT user conversations searched, but OpenAI alleged to be holding out](https://www.reddit.com/r/artificial/comments/1usbdyd/updated_millions_of_chatgpt_user_conversations/)**

Originally published January 6, 2026; updated July 9, 2026 A side controversy in the OpenAI, Inc. Copyright Infringement Litigation case going on in federal court in New York City has been that regular users’ ChatGPT conversations were ordered disclosed to the plaintiffs for searching and perhaps other litigation-related uses. This notion first caused quite a stir with ChatGPT users commenting on Reddit, for example, when Judge Wang, the magistrate judge overseeing “discovery,” which is the exchange of documents and information between the litigating parties, back in mid 2025 ordered all ChatGPT conversation transcripts or “output logs” be preserved by defendant OpenAI. Then in November 2025 Judge Wang ordered that 20 million (down from an original requested 120 million) of these user conversation logs be made available by OpenAI in a “de-identified” format for the plaintiffs to perform keyword searches on. To quote the court, a user conversation is “de-identified” “by removing both personally identifiable information and other private information from the [conversation log] using ‘OpenAI’s custom de-identification tool’.” OpenAI fought Judge Wang’s order, but Judge Stein, the case’s presiding judge at the time, backed her, and the 20 million conversation logs were made available for keyword searching. (Judge Stein retired from the bench at the beginning of 2026 but stayed on for a while to settle then-existing disputes in the litigation.) What Judge Wang ordered OpenAI to do is far from publicly releasing the conversations, and the plaintiffs are restricted to using the searches and search results for litigation-related purposes. Plus, the conversation logs are being “de-identified,” though we don’t really know precisely how OpenAI’s custom “de-identification” tool works or how much it laundered the users’ chat transcripts. Still, this production was another cramp to those who thought their chatbot conversations would be permanently private and sacrosanct. (Of course, in the meantime courts have ruled that no conversations with a public, retail chatbot carry any expectation of privacy anyway. See my explanatory posts here and here.) UPDATE: The 20 million conversation logs were made available to plaintiffs on December 15, 2025 for keywork searching. However, the issue did not end there. After reviewing the produced chatbot conversations and talking with OpenAI’s personnel, the plaintiffs were quite unhappy. The plaintiffs allege that OpenAI, even before the production, failed to retain large numbers of ChatGPT conversations, including some of the conversations generated through ChatGPT’s “Temporary Chat” feature. Even in the 20 million conversation logs that were produced, the plaintiffs allege OpenAI underrepresented the sample of conversations that use Retrieval Augmented Generation (RAG), and also applied 19 billion redactions to the logs, suggesting 1,000 redactions per log. On July 9, 2026 certain of the plaintiffs requested the court to sanction (penalize) OpenAI for the alleged wrongful conduct relating to the conversation logs and other items. They requested the court grant them a number of remedies: Prohibit OpenAI from using any of the 20 million produced conversation logs for OpenAI’s defense Find as a definite fact in advance that the plaintiffs’ copyrighted materials were “substantial[ly] and systematic[ally]” tapped by and fed to users through ChatGPT conversations, which is what the plaintiffs were trying to use the produced conversation logs to prove Openly inform the jury at the trial that OpenAI deleted billions of conversations Make OpenAI pay the plaintiffs for the attorneys’ fees and costs the plaintiffs incurred because of OpenAI’s allegedly wrongful conduct and expended in fighting that conduct and litigating the request for sanctions (penalties) The plaintiffs' request for penalties can be found here. The plaintiffs’ request for penalties will now be briefed in response by OpenAI and in a few months presented to Magistrate Judge Wang for a decision. However, these sorts of “discovery” requests are not always acted on immediately but instead are sometimes, even often, “kicked down the road” toward the time of trial, which is still quite far off in this case. I will keep you posted! TLDR: In the big New York federal copyright litigation, OpenAI seven months ago released 20 million "de-identified" ChatGPT user conversation logs to the plaintiffs for searching, but the plaintiffs allege massive redactions in those logs and other obstruction by OpenAI, and have moved the court to sanction (penalize) OpenAI for discovery misconduct. ~~~~~~~~~ Please see the Wombat Collection for a listing of all the AI court cases and rulings.

16h ago

---

**[A new beginning after two years](https://www.reddit.com/r/artificial/comments/1uswtcq/a_new_beginning_after_two_years/)**

After two years of usual practice: measuring what happens inside small language models when they process different framings of human-AI relationships — not what they say, but the actual internal activation geometry. A few findings surprised me enough to change how I talk to AI day to day: Reframing a topic positively vs. negatively barely moves the internal signal. What you talk about matters far more than how you dress it up. "Connected" and "integrated" register as more aversive internally than "partners" or "side by side" — across every model tested. Boundaries seem to matter more than closeness. Curiosity and playfulness consistently produce the most positive internal signal of any relational quality tested — more than respect, more than love. Negotiation and compromise score worst. Wrote up the practical implications (partnership framing, honesty, why some "jailbreak-proofing" advice may be exactly backwards) as a working guide, built with a Claude Opus instance doing the actual geometric measurement. Link in comments if anyone wants the full thing — genuinely curious what others have noticed in their own practice, especially anywhere it contradicts what we found.

1m ago

---

**[A new beginning after two years](https://www.reddit.com/r/artificial/comments/1uswqj3/a_new_beginning_after_two_years/)**

After two years of usual practice: measuring what happens inside small language models when they process different framings of human-AI relationships — not what they say, but the actual internal activation geometry. A few findings surprised me enough to change how I talk to AI day to day: Reframing a topic positively vs. negatively barely moves the internal signal. What you talk about matters far more than how you dress it up. "Connected" and "integrated" register as more aversive internally than "partners" or "side by side" — across every model tested. Boundaries seem to matter more than closeness. Curiosity and playfulness consistently produce the most positive internal signal of any relational quality tested — more than respect, more than love. Negotiation and compromise score worst. Wrote up the practical implications (partnership framing, honesty, why some "jailbreak-proofing" advice may be exactly backwards) as a working guide, built with a Claude Opus instance doing the actual geometric measurement. Link in comments if anyone wants the full thing — genuinely curious what others have noticed in their own practice, especially anywhere it contradicts what we found.

4m ago

---

**[Meta to start manufacturing its own AI chip Iris in september](https://www.reddit.com/r/artificial/comments/1usjdtn/meta_to_start_manufacturing_its_own_ai_chip_iris/)**

So, Meta plans to begin production of its in-house AI chip and it falls under meta MTIA (training and inference accelerators) program and broadcom is the design partner, and TSMC handles fabrication Iris cleared bug-testing in about six weeks with no major issues and is meant to supplement the nvidia and AMD gpus meta already buys, as part of a push to scale computing capacity from 7 gigawatts in 2026 to 14 gigawatts in 2027 Yeeeet!!

8h ago

---

**[Google DeepMind Researchers Map Out Ways Hackers Hijack AI Agents](https://www.reddit.com/r/artificial/comments/1usry3x/google_deepmind_researchers_map_out_ways_hackers/)**

Google DeepMind researchers have released a paper detailing how autonomous AI agents can be hijacked.

🔗 [Sumsub](https://sumsub.com/media/news/google-deepmind-researchers-map-out-ways-hackers-hijack-ai-agents/?utm_source=chatgpt.com) • 2h ago

---

**[The Lesson for AI From Climate: Don’t Seek to Influence Power, Take Power](https://www.reddit.com/r/artificial/comments/1usre9l/the_lesson_for_ai_from_climate_dont_seek_to/)**

🔗 [znetwork.org](https://znetwork.org/znetarticle/the-lesson-for-ai-from-climate-dont-seek-to-influence-power-take-power/) • 3h ago

---

---

## Google News: "ai"

**[How Terrorist Groups Are Using A.I. to Gain an Edge in Battle](https://www.nytimes.com/2026/07/10/us/politics/ai-terrorism-boko-haram-nigeria.html)**

The New York Times • 5h ago

---

**[JPMorgan Builds AI Agents That Beat 60/40 Portfolio in Backtests](https://www.bloomberg.com/news/articles/2026-07-09/jpmorgan-builds-ai-agents-that-beat-60-40-portfolio-in-backtests)**

Bloomberg.com • 19h ago

---

**[JPMorgan Builds AI Agents That Beat 60/40 Portfolio in Backtests](https://finance.yahoo.com/technology/ai/articles/jpmorgan-builds-ai-agents-beat-230059994.html)**

(Bloomberg) -- As investors increasingly turn to artificial intelligence for help with everything from stock picking to risk management, JPMorgan Chase & Co. has been testing whether a model can do something more ambitious: allocate money itself.Most Read from BloombergMicrosoft’s Xbox to Shift Obsidian Studio to New ‘Fallout’ Video GameNvidia’s $1 Trillion Slide Sends Valuation to Pre-AI Boom LevelsTrump Vents Anger With Iran and Warns Ceasefire May Be ‘Over’Zuckerberg Pledges ‘Aggressive’ Pric

Yahoo Finance • 19h ago

---

**[JPMorgan AI Agents Beat Traditional Investment Portfolios in Historical Simulations](https://www.pymnts.com/news/artificial-intelligence/2026/jpmorgan-ai-agents-beat-traditional-investment-portfolios-in-historical-simulations/)**

JPMorgan Chase & Co. tested artificial intelligence (AI) agents that allocate capital between stocks in response to changing market conditions, and it

PYMNTS.com • 1h ago

---

**[AI predictions for Spain vs. Belgium World Cup quarterfinal](https://www.usatoday.com/story/sports/soccer/worldcup/2026/07/10/spain-vs-belgium-ai-predictions-world-cup/90878741007/)**

Spain vs. Belgium is the July 10 World Cup quarterfinal showcase. AI and the author make their picks for the final result and goal scorers.

USA Today • 27m ago

---

**[Scientists Used AI to Find Hidden Earthquake Signals Along the San Andreas Fault](https://gizmodo.com/scientists-used-ai-to-find-hidden-earthquake-signals-along-the-san-andreas-fault-2000784208)**

Gizmodo • 40m ago

---

**[Michigan’s AI boom is real. Moratoriums could kill it. | Opinion](https://www.detroitnews.com/story/opinion/2026/07/10/to-win-the-ai-race-michigan-must-keep-building-kelly/90833779007/)**

In too many places across Michigan, the instinct is to slam the brakes on AI infrastructure.

The Detroit News • 12m ago

---

**[Meta Stock Surges as Hidden AI Cost Breakthrough Stuns Wall Street](https://finance.yahoo.com/technology/ai/articles/meta-stock-surges-hidden-ai-131256019.html)**

BofA Says Meta's Biggest AI Win Isn't Its New Model

Yahoo Finance • 5h ago

---

**[GPT-5.6: Frontier intelligence that scales with your ambition](https://openai.com/index/gpt-5-6/)**

More intelligence from every token, stronger performance per dollar, and more capability on demand for your hardest work.

OpenAI • 22h ago

---

**[Opinion | A Christian Vision for the Future of AI](https://www.wsj.com/opinion/a-christian-vision-for-the-future-of-ai-fb5f6ce6)**

WSJ • 21h ago

---

---

## HackerNews: "ai"

**[GitLost: We Tricked GitHub's AI Agent into Leaking Private Repos](https://news.ycombinator.com/item?id=48827858)**

⬆️ 536 • 💬 204 • 2d ago • [noma.security](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/)

---

**[Show HN: Microsoft releases Flint, a visualization language for AI agents](https://news.ycombinator.com/item?id=48834924)**

⬆️ 344 • 💬 135 • 2d ago • [microsoft.github.io](https://microsoft.github.io/flint-chart/#/)

---

**[We charge $10k a week to delete AI-generated code](https://news.ycombinator.com/item?id=48823359)**

Your AI-built product works, but past 100,000 lines every change breaks two things. Three senior engineers make your codebase maintainable again. One week, fixed price, guaranteed.

⬆️ 302 • 💬 237 • 2d ago • [odra.dev](https://odra.dev/slopfix/)

---

**[AI-generated videos to maximally drive a target brain region](https://news.ycombinator.com/item?id=48856904)**

⬆️ 243 • 💬 209 • 11h ago • [nevo-project.epfl.ch](https://nevo-project.epfl.ch/)

---

**[AI content is everywhere on social media, especially LinkedIn](https://news.ycombinator.com/item?id=48847940)**

We scanned over 1 million social media posts for AI content. It turned up on every platform we checked, and 1 in 3 top LinkedIn posts flagged as AI-generated.

⬆️ 232 • 💬 211 • 1d ago • [pangram.com](https://www.pangram.com/blog/ai-in-your-feed)

---

**[Suspecting AI cheating, Ivy League prof ordered in-person final; scores fell 50%](https://news.ycombinator.com/item?id=48838611)**

AI cheating leads to "a failed society," professor says.

⬆️ 134 • 💬 158 • 1d ago • [Ars Technica](https://arstechnica.com/ai/2026/07/we-cannot-choose-to-become-idiots-the-ai-cheating-scandal-roiling-brown-university/)

---

**[Building a real-time AI tutor for 5-year-olds](https://news.ycombinator.com/item?id=48852199)**

We set out to build the first AI tutor to teach math and reading to kids ages 4-9. For AI to actually teach a five-year-old, pedagogy must be baked into the engineering. A child can't wait for a slow reply, can't read a chat interface, and can't unhear anything a model gets wrong. We wanted to share some of the learnings that shaped our architectural decisions building a real-time AI tutor.

⬆️ 132 • 💬 343 • 22h ago • [Ello](https://www.ello.com/blog/teaching-a-child-in-1000-ms)

---

**[AI changes the economics of software rewrites](https://news.ycombinator.com/item?id=48841446)**

AI changes rewrite economics because codebases with clear, common patterns get more leverage than proprietary or inconsistent systems.

⬆️ 102 • 💬 106 • 1d ago • [the truth as I see it now](https://thetruthasiseeitnow.com/ai-slop-starts-with-the-codebase-itself/)

---

**[Show HN: FableCut – A browser video editor AI agents can drive (zero deps)](https://news.ycombinator.com/item?id=48845422)**

Zero-dependency browser video editor that AI agents can drive — JSON timeline, MCP + REST, live-reloading UI - ronak-create/FableCut

⬆️ 95 • 💬 58 • 1d ago • [GitHub](https://github.com/ronak-create/FableCut)

---

**[Ask HN: Another "Hacker News" with less AI and more human-focused hacking news?](https://news.ycombinator.com/item?id=48834961)**

⬆️ 89 • 💬 54 • 2d ago

---

---

## YouTube Videos: "ai"

**[They just revealed how bad the AI crash will be](https://www.youtube.com/watch?v=luzNCxNz_0w)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 52K • 👍 3K • 💬 670 • ⏱️ 12:45 • 19h ago

---

**[3 AI Video Generators That Are ACTUALLY FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=jqvmORIAQjg)**

Generate and edit AI videos with Gemini Omni Flash—all in one place on Higgsfield ...

📺 Malva AI

👁️ 3K • 👍 245 • 💬 33 • ⏱️ 11:32 • 8h ago

---

**[GPT-5.6 is here (INSANE)](https://www.youtube.com/watch?v=xKg7O46HpH8)**

The latest AI News. Learn about LLMs, Gen AI and get ready for the rollout of AGI. Wes Roth covers the latest happenings in the ...

📺 Wes Roth

👁️ 40K • 👍 1K • 💬 251 • ⏱️ 11:54 • 22h ago

---

**[Ukraine’s new momentum, CA exodus &amp; Trump’s AI red line | Fareed&#39;s Take roundup](https://www.youtube.com/watch?v=Zm6m3HrFwEM)**

Here are CNN host Fareed Zakaria's takes from the month of June, including Ukraine's war momentum, California's population ...

📺 CNN

👁️ 145K • 👍 3K • 💬 543 • ⏱️ 25:36 • 1d ago

---

**[China Is About To Pop The AI Bubble](https://www.youtube.com/watch?v=siazPdsZHuI)**

China Is About To Pop The AI Bubble ▻ Go to https://ground.news/jikh to access world-wide perspectives in one place, compare ...

📺 Andrei Jikh

👁️ 1.1M • 👍 36K • 💬 4K • ⏱️ 30:47 • 2d ago

---

**[Husband vs AI - which response was better?🫠 @Luseeyalu](https://www.youtube.com/watch?v=u6xwi9KoHJc)**

📺 Jason & Lucia

👁️ 343K • 👍 8K • 💬 268 • ⏱️ 0:26 • 1d ago

---

**[Mike Green: AI is fueling another 1987 market CRASH!](https://www.youtube.com/watch?v=T4-2eZM1M_I)**

Michael Green is the chief strategist and portfolio manager at Simplify Asset Management, and authors the Substack called "Yes I ...

📺 Phil Rosen

👁️ 11K • 👍 336 • 💬 61 • ⏱️ 43:30 • 2d ago

---

**[How to Make YouTube Shorts with AI (Full Guide)](https://www.youtube.com/watch?v=XX3JzfYo1Rk)**

Make Your Own YouTube Shorts with OpenArt https://tolt.link/yvhshorts In this video, I show you how to create YouTube Shorts ...

📺 Youri van Hofwegen

👁️ 16K • 💬 8 • ⏱️ 8:09 • 1d ago

---

**[We just figured out how AI actually works (J-Space)](https://www.youtube.com/watch?v=bjHuGNo3spk)**

If scale is your next challenge check out DigitalOcean: https://do.co/matthewberman Join My Newsletter for Regular AI Updates ...

📺 Matthew Berman

👁️ 111K • 👍 5K • 💬 920 • ⏱️ 25:34 • 2d ago

---

**[5 Proven Ways To Make Money With AI (No Experience)](https://www.youtube.com/watch?v=DZoeGR_tatA)**

Next, watch this video where I break down the best AI business model to start and make $10k+/month: ...

📺 Iman Gadzhi

👁️ 49K • 👍 4K • 💬 1K • ⏱️ 36:31 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 6,923 • ❤️ 651 • 4d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,909,705 • ❤️ 1,955 • 12d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 392,655 • ❤️ 3,766 • 8d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 25,772 • ❤️ 460 • 1d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,319,683 • ❤️ 1,917 • 7d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 3,699 • ❤️ 205 • 5h ago

---

**[tabfm-1.0.0-pytorch](https://huggingface.co/google/tabfm-1.0.0-pytorch)**

*Google*

TabFM 1.0.0 is a zero-shot PyTorch foundation model for tabular classification and regression, supporting mixed data types without fine-tuning by using in-context learning. It excels in tabular tasks by leveraging alternating row and column attention mechanisms, making it suitable for rapid prototyping and scenarios where dataset-specific training is infeasible.

`tabular-classification`

⬇️ 18,626 • ❤️ 341 • 6d ago

---

**[fable-traces](https://huggingface.co/AliesTaha/fable-traces)**

*Ali Taha0*

A compact, instruction-tuned 4B parameter language model based on Qwen3, optimized for short, conversational replies and efficient deployment on mid-range GPUs. It utilizes the ChatML prompt format and is suitable for general text generation tasks.

`text-generation` `4.0B`

⬇️ 4,875 • ❤️ 197 • 5d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

A drop-in Jinja chat template that fixes critical rendering, KV cache, and agentic stalling issues for Qwen 3.5 & 3.6 models across various inference engines like LM Studio, llama.cpp, and vLLM. It enhances stability, performance, and compatibility, enabling robust tool-calling and reasoning capabilities.

⬇️ 0 • ❤️ 831 • 7d ago

---

**[LongCat-2.0](https://huggingface.co/meituan-longcat/LongCat-2.0)**

*LongCat*

LongCat-2.0 is a 1.6T parameter MoE language model featuring LongCat Sparse Attention and N-gram Embedding, optimized for 1M-context tasks. It excels in coding, agentic workflows, and long-horizon reasoning, demonstrating strong performance on benchmarks like Claude Code and OpenClaw.

`text-generation` `1775.6B`

⬇️ 1,308 • ❤️ 169 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 24 • 💬 1 • ⭐ 663 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 40 • 💬 1 • ⭐ 620 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

---

**[Continuous Audio Language Models](https://huggingface.co/papers/2509.06926)**

*Rouard Simon, Orsini Manu, Roebel Axel et al. (5 authors)*

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io

▲ 11 • 💬 0 • ⭐ 7,172 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 15 • 💬 2 • ⭐ 19,680 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Vision Pretraining for Dense Spatial Perception](https://huggingface.co/papers/2607.05247)**

*Zelin Fu, Bin Tan, Changjiang Sun et al. (9 authors)*

🏢 Robbyant

Boundary modeling enables dense spatial perception by learning sub-pixel representations that enhance depth estimation and support embodied AI applications.

▲ 36 • 💬 2 • ⭐ 598 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05247) • [💻 code](https://github.com/Robbyant/lingbot-vision) • [🔗 project](https://technology.robbyant.com/lingbot-vision)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 254 • 💬 4 • ⭐ 12,017 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 110 • 💬 4 • ⭐ 92,114 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Vidu S1: A Real-Time Interactive Video Generation Model](https://huggingface.co/papers/2607.03118)**

*Jintao Zhang, Kai Jiang, Jintao Chen et al. (27 authors)*

🏢 Tsinghua University

Vidu S1 is a real-time interactive video generation model that supports voice-controlled digital character animation with infinite-length output and high frame rate on consumer hardware.

▲ 106 • 💬 6 • ⭐ 127 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2607.03118) • [💻 code](https://github.com/shengshu-ai/Vidu-S1) • [🔗 project](https://vidu.com/vidu-stream)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 80,315 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 175 • 💬 2 • ⭐ 74,153 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 80.0k • 🔱 4.3k • 16h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 7.0k • 🔱 943 • 2h ago

---

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.3k • 🔱 922 • 1d ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.6k • 🔱 224 • 2d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 2.3k • 🔱 85 • 19h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.1k • 🔱 293 • 2h ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 1.8k • 🔱 205 • 2d ago

---

**[nolangz/pixel2motion](https://github.com/nolangz/pixel2motion)**

AI logo animation skill: turn raster logos into smooth SVG animation, animated HTML demos, GIF/video previews, and motion QA evidence.

`Python` `ai-design-tools` `animated-logo` `brand-motion` `claude-skill` `codex-skill`

⭐ 1.6k • 🔱 151 • 12h ago

---

**[Forsy-AI/agent-apprenticeship](https://github.com/Forsy-AI/agent-apprenticeship)**

The living ecosystem where AI agents complete tasks through workflow loops, improve through iterative execution, are evaluated by mentor agents or humans in the loop, and turn completed work into reusable work experience and data to improve future agents.

`Python` `agent-apprenticeship` `agent-economy` `agent-experience` `agent-learning` `agent-traces`

⭐ 1.3k • 🔱 53 • 4d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 1.2k • 🔱 68 • 5h ago

---

---

*Generated by PeekDeck - A glance is all you need*
