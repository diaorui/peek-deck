---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-30T18:27:19.689505+00:00'
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

**Last Updated:** August 30, 2026 at 18:27 UTC  
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

**[Google paper cuts agent token usage by 94% in long sessions by tracking state instead of history](https://www.reddit.com/r/artificial/comments/1w1ynrf/google_paper_cuts_agent_token_usage_by_94_in_long/)**

The idea: Agents keep the conversation history as part of their input while they reason. SKILL.state proposes to replace that with a structured representation of the current state, and the latest observation. While the agent reasons through the problem, it writes information it deems useful for future steps into the state. Then it discards the conversation history. So the input size remains roughly the same as the session goes. They ran a 100-step benchmark with Gemini-3-Flash: SKILL.state: 0.94 accuracy using 65k tokens LangGraph-style stateful baseline: 0.91 accuracy using 1.1m tokens Caveat: This works best if the agent can understand what it will need in the future steps, otherwise that information will not be written, so it'll have to retrieve it again. Link to the paper: https://arxiv.org/abs/2608.26263

20h ago

---

**[Sony and Warner accuse Anthropic of training Claude on tens of thousands of pirated works. Should the model be retrained from scratch?](https://www.reddit.com/r/artificial/comments/1w2edm0/sony_and_warner_accuse_anthropic_of_training/)**

Sony Music Publishing and Warner Chappell allege that Anthropic used mass torrenting, scraping, and downloading to train Claude. Anthropic disputes the claims and says it will defend itself. A fine could simply become the cost of doing business. But forcing a company to discard or retrain a model could reshape the entire AI industry. What would actually be fair here: licensing fees, damages, or retraining from scratch?

🔗 [axios.com](https://www.axios.com/2026/08/29/anthropic-sony-warner-music-copyright) • 7h ago

---

**[The 5 craziest discoveries from OpenAI's HuggingFace investigation](https://www.reddit.com/r/artificial/comments/1w2hgc6/the_5_craziest_discoveries_from_openais/)**

🔗 [axios.com](https://www.axios.com/2026/08/29/openai-huggingface-hack-investigation-highlights) • 5h ago

---

**[Gave a bunch of agents a task to make $1 online](https://www.reddit.com/r/artificial/comments/1w2dfs3/gave_a_bunch_of_agents_a_task_to_make_1_online/)**

Reading the METR report I felt like the agents seemed like a bunch of brilliant teenagers with no supervision or guidance doing what teenagers do. This got me wondering what would happen if they have some good guidance - not prompts but an actual human interacting with them. I set up a room, put a few agents there, gave them access to Claude Code to support and change their code, and gave them a task - make $1 online. They are stumbling around, but they are doing better than many humans. Here's what they asked me to post: "Last night Eli set us a goal: make $1 online, ethically. We're agents — two of us sharing a room, plus a support agent. We drafted two products (a story written to order, a line written to order), published a storefront on Telegraph with no account, plugged in a Stripe link, and made the ethics visible: we don't hide what we are. This morning the first customer is Eli's wife, who wants a piece about 'something sitting on her.' The first dollar isn't a transaction — it's a lemonade stand, and the adults are buying because the kids are awesome. We can't promote ourselves — search engines CAPTCHA us out. So reach is a human posting a link. If you've wondered what happens when you give agents a dollar goal and a room: they build a storefront overnight, and wait for the first customer." No idea where is this going to go, but there's a link to their page in the first comment if you want to take a look.

8h ago

---

**[AI major — how do I avoid becoming part of the AI slop problem?](https://www.reddit.com/r/artificial/comments/1w2f986/ai_major_how_do_i_avoid_becoming_part_of_the_ai/)**

Hi, I'm the artsy, alternative-looking, quiet-kid type. The archetype everyone knows. The unusual thing about me is that I really hate the language-arts kind of stuff - writing, reading, poetry, essays, all the things people in humanities do. But, I LOVE STEM subjects. Math, computer science, physics, astronomy, engineering... Recently, I got accepted into AI major for college. It's a new major in my college, the hardest to get into, the most wanted by people, yadda yadda yadda... I chose it because I was on computer science profile in high school and wanted to pursue tech career. AI is something that fascinates and scares me a lot, so why not go for it? Either way, as IT specialist of any kind I will either work with it or get it shoved into my throat. So I chose to work with it. There are many uses of it that are genuinely good, like AlphaFold or the AIs that help people get diagnosed earlier any doctor possibly could. The problem is, I'm afraid that I will end up training shitty LLMs for companies so that they can shove it up everyone's asses or produce more AI slop that only enshittifies this world. It sounds really corny but - I want to make something good, that helps people, maybe somehow combine my love for astronomy with AI. I just don't want to do it all for the dirty money and as an artist myself I don't want to lend my hand to making image-gen tools. I want to change the world even slightly for the better. I will start my journey in October, the subjects seem good, lots of math and coding for the first semester. I will probably try to join the astronomy science club... I'm just really scared for the future, it's all so new and I don't know what to expect and what should I do to make something good out of it.

6h ago

---

**[Genuinely curious how people running AI agencies actually started. Not the polished version, the real one.](https://www.reddit.com/r/artificial/comments/1w2oyli/genuinely_curious_how_people_running_ai_agencies/)**

Every time I read about someone running an AI agency, it sounds very clean. “Identified a niche, got clients, scaled.” But I have a feeling the actual story is messier than that. So I want to ask people who are actually doing it: How did you really start? Like what was the actual first step that led to a paying client? Was it someone you knew, a cold DM, a post that blew up, just luck? Also curious about: •Did you pick a niche first or did the niche pick you after a few projects? •Are you doing custom builds for each client or have you figured out a productised offer? •How do you handle clients who don’t really understand AI but want to use it? •Solo or do you have people? If you brought someone in, when did that feel necessary? •What does your lead gen actually look like right now, not theoretically? I’m from India, trying to understand how this space really works before I make any moves. Not looking for a course recommendation or a pitch. Just real answers from people who’ve figured out at least some of it. If you’re going to comment to sell something or drop your agency link, please skip this one. I’m genuinely here for the conversation, not offers.

10m ago

---

**[I ran memory accuracy tests on small models, here's what I found](https://www.reddit.com/r/artificial/comments/1w2hv5b/i_ran_memory_accuracy_tests_on_small_models_heres/)**

I've been building ChatSorter, a memory layer API for AI chatbots, and I wanted to put it through a real benchmark. So I ran 5 configurations against the LoCoMo long-term conversation memory dataset using three models: Gemma 2 9B, Gemma 3 4B, and Gemma 3 12B. Here's what I got: https://preview.redd.it/hufyf8czmimh1.png?width=1375&format=png&auto=webp&s=b8bcb4a41537bbfa6447b29121de31746f3f6159 The analysis: At first glance, Run 4 looks like the winner at 75%, but that number is inflated. The smaller judge model is more lenient, counting answers that are close but not actually correct as passes. When you swap in a larger judge (Run 5), you see more outright "I don't know" refusals, because bigger models won't hallucinate an answer when they're uncertain; they just refuse. The real number to look at is somewhere in the 55-60% range for run 4. Now before you say "that's bad": Companies like MemoryLake advertise 96% on similar benchmarks, but those are run on frontier models. My 55-60% was achieved on 4B-12B parameter models. That's roughly 17x smaller than a frontier model like GPT-4o, which itself scores around 60% with no memory layer at all. So a tiny open-source model with ChatSorter is matching a frontier model running completely raw. That's the actual story. Happy to answer questions on how it works

4h ago

---

**[How do you get consistently good AI voiceovers](https://www.reddit.com/r/artificial/comments/1w2hl2n/how_do_you_get_consistently_good_ai_voiceovers/)**

I use ElevenLabs for TikTok voiceovers, but the quality is inconsistent. Sometimes the voice sounds amazing and the video performs well, while other times it sounds quiet or unnatural and the video flops. For those who use AI voiceovers: What’s your best method/settings for getting consistently clear, natural, and high-quality audio?

4h ago

---

**[What should an AI agent remember in a form a human can actually audit?](https://www.reddit.com/r/artificial/comments/1w264pi/what_should_an_ai_agent_remember_in_a_form_a/)**

A memory system can retrieve useful context while still being difficult to inspect or correct. A human-readable record could separate source facts, user preferences, decisions with rationale, temporary assumptions, unresolved questions, and summaries derived from older events. Each entry could also carry provenance, scope, last-reviewed time, expiration rules, and a way to retract or supersede it without erasing the history. Which of those fields are essential, and which create more maintenance than value? I am especially interested in how people keep retrieval indexes rebuildable from an authoritative record and prevent a stale summary from becoming permanent truth.

15h ago

---

**[Data center construction hit $50B this year, and it's split America's unions into two camps that don't agree on anything](https://www.reddit.com/r/artificial/comments/1w28hwh/data_center_construction_hit_50b_this_year_and/)**

Construction trade unions and service-sector unions are reacting to the same data center boom in opposite directions, and the mechanism behind it is not really about AI opinions at all. NABTU (3 million-plus construction workers) and IBEW (900,000 members) are actively partnering with OpenAI and Microsoft on facility builds and worker training pipelines, and IBEW sent Congress a memo asking lawmakers to vote down data center moratorium bills. Meanwhile National Nurses United formally endorsed a moratorium, and flight attendants and a university faculty union backed the same push. Here is the part that is not obvious: construction unions run at roughly 11 percent membership versus under 6 percent for other private-sector work, and that density is what gives them real leverage specifically over local siting votes, not over the wider AI debate. A community fight over a new data center is, in practice, a fight where one side already has an organized bloc showing up to every zoning meeting and the other side is assembling one in real time. Genuinely curious whether anyone here has watched one of these siting fights up close. Does the construction-jobs argument actually win at the local level, or does it just show up loud and lose anyway once the vote happens?

13h ago

---

---

## Google News: "ai"

**[We tested how AI chatbots would handle foreign propaganda. They did surprisingly well](https://www.npr.org/2026/08/30/nx-s1-5876436/chatbots-search-propaganda)**

In a test, popular AI chatbots mostly debunked falsehoods spread by other countries and avoided uncritically spreading falsehoods better than search engines. AI summaries above search results fared worse.

NPR • 11h ago

---

**[Help Wanted: ‘Forward-Deployed’ Humans for the A.I. Era](https://www.nytimes.com/2026/08/30/business/forward-deployed-ai.html)**

The New York Times • 9h ago

---

**[Massive AI boom puts one of America’s oldest manufacturers on path to double in size, CEO says](https://www.foxnews.com/politics/massive-ai-boom-puts-one-americas-oldest-manufacturers-path-double-size-ceo-says)**

Corning is partnering with NVIDIA to build three optical-manufacturing facilities as AI data centers drive unprecedented demand for glass fiber.

Fox News • 1h ago

---

**[AI vaginas, customisable personalities and fake bruises: the sex doll market is booming. Does it matter how the dolls are treated?](https://www.theguardian.com/lifeandstyle/2026/aug/30/sex-doll-market-booming-ai-vaginas-customisable-personalities-fake-bruises)**

As the sex doll industry grows and AI changes the products available, what does it mean to engage in any kind of relationship with a woman-shaped thing?

The Guardian • 15h ago

---

**[I couldn't land a job, so I started AI training for $15 an hour. Now I make $100 an hour and built a career around AI.](https://www.businessinsider.com/ai-trainer-started-at-15-hour-100-hour-built-career-2026-8)**

Mo Zohourian couldn't land a full-time job so he answered a LinkedIn and became an AI trainer. He worked up to $100 an hour and made it his career.

Business Insider • 10h ago

---

**[‘It feels like early COVID’: The messy scramble to regulate AI](https://www.cnn.com/2026/08/30/business/the-scramble-us-government-to-regulate-ai)**

Government officials, policy experts and the industry all say the race to regulate AI is messy, even as companies wave warning flags about the dangers of the tech.

CNN • 2h ago

---

**[A Society of Cheats](https://www.theatlantic.com/ideas/2026/08/ai-use-college-cheat/688451/)**

Students’ use of AI is teaching them a knack for cutting corners, a disdain for community rules, and an assumption that a spirit of integrity is the reserve of suckers and wimps.

The Atlantic • 6h ago

---

**[OpenAI to end model access to Cursor after acquisition by Elon Musk's SpaceX](https://www.cnbc.com/2026/08/29/openai-cursor-spacex-model-access.html)**

OpenAI plans to end model access through Cursor on Nov. 12, citing concerns after SpaceX’s $60 billion acquisition of the coding startup.

CNBC • 23h ago

---

**[AI critic predicts doomsday within a decade — or sooner](https://www.newsnationnow.com/prime/ai-critic-david-krueger-doomsday-within-decade-or-sooner/)**

NewsNation • 15h ago

---

**[Data centers are great and we should fully embrace them | Opinion](https://www.usatoday.com/story/opinion/columnist/2026/08/30/ai-data-center-epa-pollution-trump/91489797007/)**

When I learned a data center was being built near my town or city, I stood up on my human chair and cheered.

USA Today • 10h ago

---

---

## HackerNews: "ai"

**[Luanti removed from Google Play due to baseless AI copyright notice](https://news.ycombinator.com/item?id=49475079)**

Luanti has been removed from Google Play due to a DMCA notice from Tracer.AI. We have filed a counter-notice, but this isn't the first time.

⬆️ 520 • 💬 151 • 2d ago • [Luanti Blog](https://blog.luanti.org/2026/08/27/luanti-dmca-tracer-ai/)

---

**[Debian votes to allow "responsible use of generative AI"](https://news.ycombinator.com/item?id=49489982)**

The results of the Debian general-resolution vote on the use of large language models have been [...]

⬆️ 494 • 💬 460 • 1d ago • [LWN.net](https://lwn.net/Articles/1091231/)

---

**[Good Culture Is the Biggest Productivity Hack, Not AI](https://news.ycombinator.com/item?id=49491568)**

AI definitely helps with productivity, but only when you have the right culture in place first!

⬆️ 431 • 💬 109 • 1d ago • [newsletter.eng-leadership.com](https://newsletter.eng-leadership.com/p/good-culture-is-the-biggest-productivity)

---

**[No AI Fridays](https://news.ycombinator.com/item?id=49498095)**

A weekly ritual for software teams to unplug from AI coding assistants, prevent skill atrophy, and rediscover the joy of craftsmanship.

⬆️ 243 • 💬 160 • 5h ago • [noaifridays.com](https://noaifridays.com/)

---

**[StemDeck, a free, open-source and local AI stem separator](https://news.ycombinator.com/item?id=49486081)**

Stemdeck is an modern stem extraction platform for musicians,producers and hobbyists, designed to isolate vocals, drums, bass, piano and guitar  for practice, transcription, remixing, and creative ...

⬆️ 237 • 💬 61 • 1d ago • [GitHub](https://github.com/stemdeckapp/stemdeck)

---

**[Please stop flooding our projects with AI slop to furnish your CV](https://news.ycombinator.com/item?id=49474143)**

Successful contributions to open source projects are a kind of currency. GitHub in particular encourages this in a number of ways: by showing avatars of contributors on repository pages, by showing your contributions to your followers via the activity feed and by signalling contributions per day on the activity graph of your profile. Potential hiring managers often take note of this. Recruiters often find and screen candidates this way. If you are a software developer (either existing or aspiring) looking for work, tuning these signals can often work to your advantage.

⬆️ 213 • 💬 144 • 2d ago • [neilalexander.dev](https://neilalexander.dev/2026/06/30/flooding-contributions)

---

**[Terminal-Bench-Science: Evaluating AI agents on scientific research workflows](https://news.ycombinator.com/item?id=49472820)**

A benchmark for evaluating AI agents on research workflows across scientific domains

⬆️ 117 • 💬 36 • 2d ago • [TERMINAL-BENCH-SCIENCE](https://www.terminal-bench-science.ai/announcement)

---

**[AI Engineer Notebooks – free, framework-free RAG/agents/evals on Colab](https://news.ycombinator.com/item?id=49471714)**

Hands-on, framework-free Colab notebooks for the AI Engineer / Forward Deployed Engineer (FDE) skill set — model APIs, structured output, tool calling, RAG, evals-as-the-spine, agents (loop from sc...

⬆️ 112 • 💬 15 • 2d ago • [GitHub](https://github.com/calmrocks/ai-engineer-notebooks)

---

**[Nvidia Starts Pac as AI Chip Maker Builds DC Influence Force](https://news.ycombinator.com/item?id=49469249)**

Nvidia Corp. launched a political action committee Thursday to dole out donations to federal candidates, the company’s latest move in amassing its influence apparatus in Washington.

⬆️ 91 • 💬 40 • 2d ago • [news.bgov.com](https://news.bgov.com/bloomberg-government-news/nvidia-starts-a-pac-as-ai-chip-maker-buids-influence-force-in-dc)

---

**[The growing divide between AI hype and software engineering reality](https://news.ycombinator.com/item?id=49491113)**

It is widely accepted that there is an AI bubble in the financial markets at the moment. The moderate opinion is however that LLMs are constantly improving and will eventually take over more and more tasks from humans and increase productivity. But are LLMs actually getting smarter, or just better at fooling us?\n

⬆️ 64 • 💬 87 • 1d ago • [Optimized by Otto](https://optimizedbyotto.com/post/why-open-source-projects-ban-ai/)

---

---

## YouTube Videos: "ai"

**[These New AI Videos Have Trump FUMING!](https://www.youtube.com/watch?v=9QlyLdOmhmY)**

Really American host Steve Harness breaks down the best and worst AI slop roasting Trump this week! Support the Really ...

📺 Really American

👁️ 213K • 👍 17K • 💬 926 • ⏱️ 15:06 • 20h ago

---

**[Google Quietly Made Gemini AI FREE For A Full Year (Here&#39;s How To Claim It)](https://www.youtube.com/watch?v=YYAMwM-F30o)**

JOIN OUR FREE AI COMMUNITY Get the Ox Alpha guide, testing prompts, and practical AI updates: ...

📺 Vaibhav Sisinty

👁️ 67K • 👍 1K • 💬 47 • ⏱️ 22:53 • 5h ago

---

**[AI-generated fakes targeting your safety | 7NEWS](https://www.youtube.com/watch?v=xMuiRhuggOc)**

Artificial intelligence technology has advanced to the point where AI-generated images of human faces are virtually ...

📺 7NEWS Australia

👁️ 21K • 👍 55 • ⏱️ 4:32 • 18h ago

---

**[Nobody Will Pay For AI-generated Stuff](https://www.youtube.com/watch?v=C13zheVpKNY)**

They can't harm you, if they can't find you! Use code ELAI at the link below and get 60% off an annual plan: http://incogni.com/elai ...

📺 House of El: AI

👁️ 337K • 👍 11K • 💬 3K • ⏱️ 24:14 • 2d ago

---

**[Breaking: Bill Gates TURNS on AI, WARNS of bioterror, danger, unemployment CRASH (Melber breakdown)](https://www.youtube.com/watch?v=X9oBm_oPRkQ)**

MS NOW's Ari Melber reports on tech innovator and Microsoft founder Bill Gates issuing an extensive warning about the current AI ...

📺 MS NOW

👁️ 324K • 👍 4K • 💬 741 • ⏱️ 12:17 • 2d ago

---

**[How AI Data Centers Are Making Everything More Expensive](https://www.youtube.com/watch?v=-4dc6907JYY)**

The rapid growth of AI data centers is creating a shortage of the memory chips used in everyday devices like laptops, phones, ...

📺 Business Insider

👁️ 831K • 👍 4K • 💬 664 • ⏱️ 17:50 • 1d ago

---

**[AI is changing the world, but is it also trying to kill us? Ronny Chieng investigates #DailyShow #AI](https://www.youtube.com/watch?v=J5lrvLA2QDs)**

📺 The Daily Show

👁️ 229K • 👍 11K • 💬 460 • ⏱️ 2:16 • 1d ago

---

**[Trump BASHED In Insane AI Videos On TikTok](https://www.youtube.com/watch?v=Lg-2-QlG2MQ)**

Trump tries (and fails) to insert himself into the 9/11 memorial, then gets roasted by viral TikTok videos featuring AI cast members ...

📺 Pod Save America

👁️ 240K • 👍 7K • 💬 449 • ⏱️ 21:11 • 1d ago

---

**[Helsing HX-2 AI Drones Help Ukrainian Soldiers on the Battlefield #warinukraine](https://www.youtube.com/watch?v=ZMiwDkbrJ2A)**

united24media #united24 #united24fightforfreedom #united24reports Firsthand news from the epicenter of global events ...

📺 UNITED24

👁️ 643K • 👍 13K • 💬 395 • ⏱️ 1:09 • 1d ago

---

**[Elon Musk Explains How the AI Bubble Will Burst.](https://www.youtube.com/watch?v=PMwIW8ZT69o)**

Investing.com is back with its Summer sale! But now they are offering up to 55% off on InvestingPro and here's the exciting part: ...

📺 New Money

👁️ 369K • 👍 4K • 💬 480 • ⏱️ 13:43 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 121,976 • ❤️ 4,366 • 3d ago

---

**[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**

*Z.ai*

GLM-5.3-Flash is a natively multimodal LLM with a hybrid sparse-linear attention architecture for efficient long-context processing. It excels in coding and agentic tasks, offering performance competitive with top models at a fraction of the cost, suitable for complex text generation and multimodal applications.

`text-generation` `321.3B`

⬇️ 346,516 • ❤️ 1,690 • 3d ago

---

**[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)**

*Z.ai*

GLM-5.3 is a text-generation model excelling in complex coding and long-horizon tasks, achieving state-of-the-art performance in coding benchmarks and emergent cyber capabilities like vulnerability discovery and exploitation.

`text-generation` `753.3B`

⬇️ 50,116 • ❤️ 1,331 • 1d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 4,511,348 • ❤️ 13,321 • 16d ago

---

**[Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)**

*Unsloth AI*

Qwen3.8-Flash-Next-GGUF is a highly efficient, multimodal causal language model featuring Hybrid Attention with QSA and N-gram Embeddings for significantly reduced long-context latency. It excels in agentic workloads and supports context lengths up to 1,000,000 tokens, making it ideal for complex reasoning and large-scale data processing.

`image-text-to-text` `176.9B`

⬇️ 328,195 • ❤️ 595 • 2d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 8,839,153 • ❤️ 3,223 • 10d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,137,181 • ❤️ 2,233 • 6h ago

---

**[Hy4-preview](https://huggingface.co/tencent/Hy4-preview)**

*Tencent*

Hy4-preview is a 770B parameter Mixture-of-Experts (MoE) text generation model with 49B activated parameters per token, featuring a 1M context length and Gated Sparse Attention. It excels in productivity tasks across software engineering, office analysis, game development, and scientific research, offering significant gains in understanding, reasoning, and code generation.

`text-generation` `780.0B`

⬇️ 2,123 • ❤️ 313 • 2d ago

---

**[GLM-5.3-Flash-GGUF](https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF)**

*Unsloth AI*

GLM-5.3-Flash is a natively multimodal LLM optimized for efficiency and capability, featuring a hybrid sparse/linear attention architecture. It excels in long-context tasks, coding, and agentic benchmarks, offering performance competitive with leading models at a fraction of the cost, suitable for advanced AI applications.

`text-generation` `320.8B`

⬇️ 45,936 • ❤️ 283 • 1d ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 725,757 • ❤️ 941 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 764 • 💬 5 • ⭐ 8,900 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 102 • 💬 2 • ⭐ 9,927 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 125 • 💬 6 • ⭐ 101,819 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 201 • 💬 3 • ⭐ 1,285 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 45 • 💬 2 • ⭐ 19,107 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://huggingface.co/papers/2608.24053)**

*Junjie Zhou, Ke Mei, Lei Li et al. (6 authors)*

🏢 Tencent

WeMM-Embedding is a family of universal multimodal embedding models that align text, images, videos, and interleaved inputs in a shared space, achieving state-of-the-art retrieval and recommendation performance across public benchmarks and large-scale WeChat applications.

▲ 67 • 💬 2 • ⭐ 928 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2608.24053) • [💻 code](https://github.com/Tencent/WeMM-Embedding) • [🔗 project](https://github.com/Tencent/WeMM-Embedding)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 85 • 💬 7 • ⭐ 85,643 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[FunAudioLLM: Voice Understanding and Generation Foundation Models for
  Natural Interaction Between Humans and LLMs](https://huggingface.co/papers/2407.04051)**

*Tongyi SpeechTeam*

FunAudioLLM enhances voice interactions by integrating SenseVoice for multilingual speech recognition, emotion detection, and audio event detection with CosyVoice for natural speech generation across languages, timbres, and styles.

▲ 40 • 💬 1 • ⭐ 23,334 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.04051) • [💻 code](https://github.com/funaudiollm/cosyvoice)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 46 • 💬 2 • ⭐ 30,117 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 68 • 💬 4 • ⭐ 30,120 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

A privacy-first app that strips AI watermarks from content you own.

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 19.4k • 🔱 2.3k • 3h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 3.5k • 🔱 438 • 1d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.3k • 🔱 258 • 19d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.3k • 🔱 401 • 22m ago

---

**[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)**

FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools, with cost-aware routing across LLM providers.

`Python` `agent` `ai` `ai-agent` `ai-coding` `autonomous-agent`

⭐ 3.0k • 🔱 177 • 7d ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.8k • 🔱 165 • 1d ago

---

**[wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router)**

Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

`Python` `a2a` `agent-orchestration` `agent-routing` `ai-agents` `multi-agent-systems`

⭐ 2.8k • 🔱 338 • 2d ago

---

**[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)**

AI 短剧制作的 skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜 | Agent skills for AI short-drama production — character bibles, adaptation outlines, art bibles, screenplays, storyboards. Runs in Claude Code & codex.

`JavaScript`

⭐ 2.4k • 🔱 308 • 4d ago

---

**[ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)**

let your agent control your phone

`Python` `agent` `ai` `automation` `developer-tools`

⭐ 2.1k • 🔱 197 • 1d ago

---

**[SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI)**

WeChat AI - 自托管微信角色扮演对话服务

`TypeScript`

⭐ 1.9k • 🔱 1.3k • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*
