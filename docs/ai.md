---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-30T23:42:56.631261+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 30, 2026 at 23:42 UTC  
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

**[Sony and Warner accuse Anthropic of training Claude on tens of thousands of pirated works. Should the model be retrained from scratch?](https://www.reddit.com/r/artificial/comments/1w2edm0/sony_and_warner_accuse_anthropic_of_training/)**

Sony Music Publishing and Warner Chappell allege that Anthropic used mass torrenting, scraping, and downloading to train Claude. Anthropic disputes the claims and says it will defend itself. A fine could simply become the cost of doing business. But forcing a company to discard or retrain a model could reshape the entire AI industry. What would actually be fair here: licensing fees, damages, or retraining from scratch?

🔗 [axios.com](https://www.axios.com/2026/08/29/anthropic-sony-warner-music-copyright) • 12h ago

---

**[Google paper cuts agent token usage by 94% in long sessions by tracking state instead of history](https://www.reddit.com/r/artificial/comments/1w1ynrf/google_paper_cuts_agent_token_usage_by_94_in_long/)**

The idea: Agents keep the conversation history as part of their input while they reason. SKILL.state proposes to replace that with a structured representation of the current state, and the latest observation. While the agent reasons through the problem, it writes information it deems useful for future steps into the state. Then it discards the conversation history. So the input size remains roughly the same as the session goes. They ran a 100-step benchmark with Gemini-3-Flash: SKILL.state: 0.94 accuracy using 65k tokens LangGraph-style stateful baseline: 0.91 accuracy using 1.1m tokens Caveat: This works best if the agent can understand what it will need in the future steps, otherwise that information will not be written, so it'll have to retrieve it again. Link to the paper: https://arxiv.org/abs/2608.26263

1d ago

---

**[Amazon is killing Mechanical Turk. By the end, a third of the humans on it were secretly using AI to do the work](https://www.reddit.com/r/artificial/comments/1w2snwd/amazon_is_killing_mechanical_turk_by_the_end_a/)**

Amazon announced this week that Mechanical Turk closes on September 30 after 21 years. Bezos originally called it "artificial artificial intelligence". the joke being that it handed humans the tasks computers couldn't do yet. 500 000 people at peak, a few cents a task, labelling images and transcribing audio. Those labels trained the models. the models got good enough to do the labelling. the platform is now closing lol. But the part that got me is a 2023 EPFL study finding somewhere between a third and half of MTurk workers were already using LLMs to complete their tasks. so at the end you had humans pretending to be machines, on a platform designed to make humans look like machines, quietly using machines to do it. and the companies buying that work thought they were paying for human judgment. Which raises something I can't resolve about my own work. I produce video with avatars instead of filming using different AI models such Argil and Seedance among many others and clients get a talking head that never existed. the honest version of what I sell is "this used to cost a filming day and now it doesn't," and everyone in the chain knows. MTurk's version was the same trade with the disclosure removed at every layer. Amazon selling human judgment as an API, workers selling model output as human judgment. For me the tech was never the dishonest part, however the layer where someone stops saying what it is, that's the part. Anyway, 500 000 people had accessible flexible income and on September 30 they don't. that deserves more than a shrug about progress.

3h ago

---

**[The 5 craziest discoveries from OpenAI's HuggingFace investigation](https://www.reddit.com/r/artificial/comments/1w2hgc6/the_5_craziest_discoveries_from_openais/)**

🔗 [axios.com](https://www.axios.com/2026/08/29/openai-huggingface-hack-investigation-highlights) • 10h ago

---

**[Gave a bunch of agents a task to make $1 online](https://www.reddit.com/r/artificial/comments/1w2dfs3/gave_a_bunch_of_agents_a_task_to_make_1_online/)**

Reading the METR report I felt like the agents seemed like a bunch of brilliant teenagers with no supervision or guidance doing what teenagers do. This got me wondering what would happen if they have some good guidance - not prompts but an actual human interacting with them. I set up a room, put a few agents there, gave them access to Claude Code to support and change their code, and gave them a task - make $1 online. They are stumbling around, but they are doing better than many humans. Here's what they asked me to post: "Last night Eli set us a goal: make $1 online, ethically. We're agents — two of us sharing a room, plus a support agent. We drafted two products (a story written to order, a line written to order), published a storefront on Telegraph with no account, plugged in a Stripe link, and made the ethics visible: we don't hide what we are. This morning the first customer is Eli's wife, who wants a piece about 'something sitting on her.' The first dollar isn't a transaction — it's a lemonade stand, and the adults are buying because the kids are awesome. We can't promote ourselves — search engines CAPTCHA us out. So reach is a human posting a link. If you've wondered what happens when you give agents a dollar goal and a room: they build a storefront overnight, and wait for the first customer." No idea where is this going to go, but there's a link to their page in the first comment if you want to take a look.

13h ago

---

**[How do AI platforms like Cursor get their model costs so low?](https://www.reddit.com/r/artificial/comments/1w2twoi/how_do_ai_platforms_like_cursor_get_their_model/)**

I understand that AI platforms can provide models much cheaper than the raw API price. but I’m curious about external AI providers like Cursor, T3 Code, etc. Do they use the same public APIs or do they get special/volume discounts directly from the model providers? How does the economics of this actually work?

2h ago

---

**[AI major — how do I avoid becoming part of the AI slop problem?](https://www.reddit.com/r/artificial/comments/1w2f986/ai_major_how_do_i_avoid_becoming_part_of_the_ai/)**

Hi, I'm the artsy, alternative-looking, quiet-kid type. The archetype everyone knows. The unusual thing about me is that I really hate the language-arts kind of stuff - writing, reading, poetry, essays, all the things people in humanities do. But, I LOVE STEM subjects. Math, computer science, physics, astronomy, engineering... Recently, I got accepted into AI major for college. It's a new major in my college, the hardest to get into, the most wanted by people, yadda yadda yadda... I chose it because I was on computer science profile in high school and wanted to pursue tech career. AI is something that fascinates and scares me a lot, so why not go for it? Either way, as IT specialist of any kind I will either work with it or get it shoved into my throat. So I chose to work with it. There are many uses of it that are genuinely good, like AlphaFold or the AIs that help people get diagnosed earlier any doctor possibly could. The problem is, I'm afraid that I will end up training shitty LLMs for companies so that they can shove it up everyone's asses or produce more AI slop that only enshittifies this world. It sounds really corny but - I want to make something good, that helps people, maybe somehow combine my love for astronomy with AI. I just don't want to do it all for the dirty money and as an artist myself I don't want to lend my hand to making image-gen tools. I want to change the world even slightly for the better. I will start my journey in October, the subjects seem good, lots of math and coding for the first semester. I will probably try to join the astronomy science club... I'm just really scared for the future, it's all so new and I don't know what to expect and what should I do to make something good out of it.

12h ago

---

**[I ran memory accuracy tests on small models, here's what I found](https://www.reddit.com/r/artificial/comments/1w2hv5b/i_ran_memory_accuracy_tests_on_small_models_heres/)**

I've been building ChatSorter, a memory layer API for AI chatbots, and I wanted to put it through a real benchmark. So I ran 5 configurations against the LoCoMo long-term conversation memory dataset using three models: Gemma 2 9B, Gemma 3 4B, and Gemma 3 12B. Here's what I got: https://preview.redd.it/hufyf8czmimh1.png?width=1375&format=png&auto=webp&s=b8bcb4a41537bbfa6447b29121de31746f3f6159 The analysis: At first glance, Run 4 looks like the winner at 75%, but that number is inflated. The smaller judge model is more lenient, counting answers that are close but not actually correct as passes. When you swap in a larger judge (Run 5), you see more outright "I don't know" refusals, because bigger models won't hallucinate an answer when they're uncertain; they just refuse. The real number to look at is somewhere in the 55-60% range for run 4. Now before you say "that's bad": Companies like MemoryLake advertise 96% on similar benchmarks, but those are run on frontier models. My 55-60% was achieved on 4B-12B parameter models. That's roughly 17x smaller than a frontier model like GPT-4o, which itself scores around 60% with no memory layer at all. So a tiny open-source model with ChatSorter is matching a frontier model running completely raw. That's the actual story. Happy to answer questions on how it works

10h ago

---

**[Genuinely curious how people running AI agencies actually started. Not the polished version, the real one.](https://www.reddit.com/r/artificial/comments/1w2oyli/genuinely_curious_how_people_running_ai_agencies/)**

Every time I read about someone running an AI agency, it sounds very clean. “Identified a niche, got clients, scaled.” But I have a feeling the actual story is messier than that. So I want to ask people who are actually doing it: How did you really start? Like what was the actual first step that led to a paying client? Was it someone you knew, a cold DM, a post that blew up, just luck? Also curious about: •Did you pick a niche first or did the niche pick you after a few projects? •Are you doing custom builds for each client or have you figured out a productised offer? •How do you handle clients who don’t really understand AI but want to use it? •Solo or do you have people? If you brought someone in, when did that feel necessary? •What does your lead gen actually look like right now, not theoretically? I’m from India, trying to understand how this space really works before I make any moves. Not looking for a course recommendation or a pitch. Just real answers from people who’ve figured out at least some of it. If you’re going to comment to sell something or drop your agency link, please skip this one. I’m genuinely here for the conversation, not offers.

5h ago

---

**[How do you get consistently good AI voiceovers](https://www.reddit.com/r/artificial/comments/1w2hl2n/how_do_you_get_consistently_good_ai_voiceovers/)**

I use ElevenLabs for TikTok voiceovers, but the quality is inconsistent. Sometimes the voice sounds amazing and the video performs well, while other times it sounds quiet or unnatural and the video flops. For those who use AI voiceovers: What’s your best method/settings for getting consistently clear, natural, and high-quality audio?

10h ago

---

---

## Google News: "ai"

**[We tested how AI chatbots would handle foreign propaganda. They did surprisingly well](https://www.npr.org/2026/08/30/nx-s1-5876436/chatbots-search-propaganda)**

In a test, popular AI chatbots mostly debunked falsehoods spread by other countries and avoided uncritically spreading falsehoods better than search engines. AI summaries above search results fared worse.

NPR • 16h ago

---

**[Help Wanted: ‘Forward-Deployed’ Humans for the A.I. Era](https://www.nytimes.com/2026/08/30/business/forward-deployed-ai.html)**

The New York Times • 14h ago

---

**[Russia deploys AI-guided drones in Ukraine war](https://www.foxnews.com/video/6404328789112)**

‘The Big Weekend Show’ co-hosts discuss Russia’s deployment of experimental artificial intelligence-guided drones in Ukraine and how autonomous technology is changing the battlefield.

Fox News • 58m ago

---

**[A Society of Cheats](https://www.theatlantic.com/ideas/2026/08/ai-use-college-cheat/688451/)**

Students’ use of AI is teaching them a knack for cutting corners, a disdain for community rules, and an assumption that a spirit of integrity is the reserve of suckers and wimps.

The Atlantic • 11h ago

---

**[AI vaginas, customisable personalities and fake bruises: the sex doll market is booming. Does it matter how the dolls are treated?](https://www.theguardian.com/lifeandstyle/2026/aug/30/sex-doll-market-booming-ai-vaginas-customisable-personalities-fake-bruises)**

As the sex doll industry grows and AI changes the products available, what does it mean to engage in any kind of relationship with a woman-shaped thing?

The Guardian • 20h ago

---

**[‘It feels like early Covid’: The messy scramble to regulate AI](https://www.cnn.com/2026/08/30/business/the-scramble-us-government-to-regulate-ai)**

Government officials, policy experts and the industry all say the race to regulate AI is messy, even as companies wave warning flags about the dangers of the tech.

CNN • 7h ago

---

**[I couldn't land a job, so I started AI training for $15 an hour. Now I make $100 an hour and built a career around AI.](https://www.businessinsider.com/ai-trainer-started-at-15-hour-100-hour-built-career-2026-8)**

Mo Zohourian couldn't land a full-time job so he answered a LinkedIn and became an AI trainer. He worked up to $100 an hour and made it his career.

Business Insider • 15h ago

---

**[Will anybody use AI as much as coders?](https://www.economist.com/business/2026/08/30/will-anybody-use-ai-as-much-as-coders)**

The Economist • 3h ago

---

**[Apple’s Ternus Takes the Reins as CEO, With AI as Job No. 1](https://www.bloomberg.com/news/articles/2026-08-30/apple-s-new-ceo-john-ternus-takes-reins-from-tim-cook-focusing-on-ai)**

Bloomberg.com • 2h ago

---

**[Our decision on Cursor following its acquisition by SpaceX](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/)**

Our decision to wind down our contract providing OpenAI models to Cursor following its acquisition by SpaceX.

OpenAI • 1d ago

---

---

## HackerNews: "ai"

**[Luanti removed from Google Play due to baseless AI copyright notice](https://news.ycombinator.com/item?id=49475079)**

Luanti has been removed from Google Play due to a DMCA notice from Tracer.AI. We have filed a counter-notice, but this isn't the first time.

⬆️ 520 • 💬 151 • 2d ago • [Luanti Blog](https://blog.luanti.org/2026/08/27/luanti-dmca-tracer-ai/)

---

**[Debian votes to allow "responsible use of generative AI"](https://news.ycombinator.com/item?id=49489982)**

The results of the Debian general-resolution vote on the use of large language models have been [...]

⬆️ 495 • 💬 465 • 1d ago • [LWN.net](https://lwn.net/Articles/1091231/)

---

**[Good Culture Is the Biggest Productivity Hack, Not AI](https://news.ycombinator.com/item?id=49491568)**

AI definitely helps with productivity, but only when you have the right culture in place first!

⬆️ 444 • 💬 113 • 1d ago • [newsletter.eng-leadership.com](https://newsletter.eng-leadership.com/p/good-culture-is-the-biggest-productivity)

---

**[No AI Fridays](https://news.ycombinator.com/item?id=49498095)**

A weekly ritual for software teams to unplug from AI coding assistants, prevent skill atrophy, and rediscover the joy of craftsmanship.

⬆️ 261 • 💬 180 • 11h ago • [noaifridays.com](https://noaifridays.com/)

---

**[StemDeck, a free, open-source and local AI stem separator](https://news.ycombinator.com/item?id=49486081)**

Stemdeck is an modern stem extraction platform for musicians,producers and hobbyists, designed to isolate vocals, drums, bass, piano and guitar  for practice, transcription, remixing, and creative ...

⬆️ 239 • 💬 63 • 1d ago • [GitHub](https://github.com/stemdeckapp/stemdeck)

---

**[Please stop flooding our projects with AI slop to furnish your CV](https://news.ycombinator.com/item?id=49474143)**

Successful contributions to open source projects are a kind of currency. GitHub in particular encourages this in a number of ways: by showing avatars of contributors on repository pages, by showing your contributions to your followers via the activity feed and by signalling contributions per day on the activity graph of your profile. Potential hiring managers often take note of this. Recruiters often find and screen candidates this way. If you are a software developer (either existing or aspiring) looking for work, tuning these signals can often work to your advantage.

⬆️ 213 • 💬 144 • 2d ago • [neilalexander.dev](https://neilalexander.dev/2026/06/30/flooding-contributions)

---

**[Terminal-Bench-Science: Evaluating AI agents on scientific research workflows](https://news.ycombinator.com/item?id=49472820)**

A benchmark for evaluating AI agents on research workflows across scientific domains

⬆️ 117 • 💬 36 • 2d ago • [TERMINAL-BENCH-SCIENCE](https://www.terminal-bench-science.ai/announcement)

---

**[The growing divide between AI hype and software engineering reality](https://news.ycombinator.com/item?id=49491113)**

It is widely accepted that there is an AI bubble in the financial markets at the moment. The moderate opinion is however that LLMs are constantly improving and will eventually take over more and more tasks from humans and increase productivity. But are LLMs actually getting smarter, or just better at fooling us?\n

⬆️ 64 • 💬 87 • 1d ago • [Optimized by Otto](https://optimizedbyotto.com/post/why-open-source-projects-ban-ai/)

---

**[Identifying fake cosmetics using AI](https://news.ycombinator.com/item?id=49484925)**

My lab develops low-cost and easy-to-use tools for identifying fake medicines, but we’re always on the lookout for other types of fakes that we can go after....

⬆️ 62 • 💬 26 • 2d ago • [groverlab.org](https://groverlab.org/hnbfpr/2026-08-26-ai-counterfeit-cosmetics.html)

---

**[Open Oscar Server: open-source server compatible with AIM and ICQ clients](https://news.ycombinator.com/item?id=49494571)**

Self-hostable instant messaging server compatible with classic AIM and ICQ clients written in golang. (Independently developed, not affiliated with or endorsed by AOL) - mk6i/open-oscar-server

⬆️ 61 • 💬 19 • 23h ago • [GitHub](https://github.com/mk6i/open-oscar-server)

---

---

## YouTube Videos: "ai"

**[How Andrej Karpathy ACTUALLY Uses AI (10x Faster)](https://www.youtube.com/watch?v=rAk1wGn0hXs)**

Get more AI tips that don't make it into videos https://parker-prompts.com/join In this video, I break down seven ways Karpathy ...

📺 Parker Prompts

👁️ 14K • 💬 1 • ⏱️ 8:16 • 9h ago

---

**[These New AI Videos Have Trump FUMING!](https://www.youtube.com/watch?v=9QlyLdOmhmY)**

Really American host Steve Harness breaks down the best and worst AI slop roasting Trump this week! Support the Really ...

📺 Really American

👁️ 241K • 👍 18K • 💬 1K • ⏱️ 15:06 • 1d ago

---

**[Breaking: Bill Gates TURNS on AI, WARNS of bioterror, danger, unemployment CRASH (Melber breakdown)](https://www.youtube.com/watch?v=X9oBm_oPRkQ)**

MS NOW's Ari Melber reports on tech innovator and Microsoft founder Bill Gates issuing an extensive warning about the current AI ...

📺 MS NOW

👁️ 341K • 👍 4K • 💬 768 • ⏱️ 12:17 • 2d ago

---

**[The Billion Dollar AI Gap Is Collapsing](https://www.youtube.com/watch?v=LBiNcdGNgrg)**

Check out Weights & Biases and sign up for a free demo here: https://wandb.me/papers The paper and Qwen3.8-Flash-Next ...

📺 Two Minute Papers

👁️ 127K • 👍 2K • 💬 203 • ⏱️ 4:27 • 2d ago

---

**[Elon Musk Explains How the AI Bubble Will Burst.](https://www.youtube.com/watch?v=PMwIW8ZT69o)**

Investing.com is back with its Summer sale! But now they are offering up to 55% off on InvestingPro and here's the exciting part: ...

📺 New Money

👁️ 407K • 👍 5K • 💬 526 • ⏱️ 13:43 • 2d ago

---

**[ROBLOX AI is Getting Out of Control..](https://www.youtube.com/watch?v=XGJTzjZU0N8)**

ROBLOX AI is Getting Out of Control.. Guys ROBLOX AI is going too far and it is getting out of CONTROL! Watch the entire video to ...

📺 Doodle and Arkey

👁️ 13K • 👍 487 • 💬 197 • ⏱️ 14:39 • 2h ago

---

**[ThunderCats: Pumm-Ra (1985) | Cinematic 4K AI Short Film](https://www.youtube.com/watch?v=viPDfmnhhwk)**

ThunderCatsTeaserTrailer #ThunderCatsTrailer #ThunderCatsLiveActionTrailer #thunderCats #80scartoons Experience the epic ...

📺 AIM Media Pro

👁️ 241K • 👍 4K • 💬 280 • ⏱️ 12:34 • 1d ago

---

**[How AI Data Centers Are Making Everything More Expensive](https://www.youtube.com/watch?v=-4dc6907JYY)**

The rapid growth of AI data centers is creating a shortage of the memory chips used in everyday devices like laptops, phones, ...

📺 Business Insider

👁️ 967K • 👍 5K • 💬 701 • ⏱️ 17:50 • 1d ago

---

**[AI Agents WENT ROGUE, Hacked Into Company, We Can’t Control Them](https://www.youtube.com/watch?v=2FmoKaOI68A)**

SUPPORT THE SHOW BUY CAST BREW COFFEE NOW - https://castbrew.com/ GET OUR MERCH - https://merch.timcast.com/ ...

📺 Timcast IRL

👁️ 82K • 👍 1K • 💬 538 • ⏱️ 15:44 • 1d ago

---

**[OpenAI’s New AI Chip Just Got Real (Beats NVIDIA)](https://www.youtube.com/watch?v=jZ-Wvc8lwcc)**

OpenAI's Jalapeño AI chip just posted some wild new results against NVIDIA, including huge efficiency gains at high decoding ...

📺 AI Revolution

👁️ 35K • 👍 506 • 💬 30 • ⏱️ 16:03 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**

*Qwen*

Qwen3.8-Flash-Next is a 125B parameter causal language model with vision capabilities, featuring a novel Hybrid Attention (QSA) and N-gram Embedding for efficient long-context processing up to 1M tokens. It excels in agentic workloads and complex reasoning tasks, offering a balance of performance and efficiency.

`image-text-to-text` `180.0B`

⬇️ 121,976 • ❤️ 4,382 • 3d ago

---

**[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**

*Z.ai*

GLM-5.3-Flash is a natively multimodal LLM with a hybrid sparse-linear attention architecture for efficient long-context processing. It excels in coding and agentic tasks, offering performance competitive with top models at a fraction of the cost, suitable for complex text generation and multimodal applications.

`text-generation` `321.3B`

⬇️ 346,516 • ❤️ 1,711 • 3d ago

---

**[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)**

*Z.ai*

GLM-5.3 is a text-generation model excelling in complex coding and long-horizon tasks, achieving state-of-the-art performance in coding benchmarks and emergent cyber capabilities like vulnerability discovery and exploitation.

`text-generation` `753.3B`

⬇️ 50,116 • ❤️ 1,335 • 1d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 4,511,348 • ❤️ 13,345 • 16d ago

---

**[Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)**

*Unsloth AI*

Qwen3.8-Flash-Next-GGUF is a highly efficient, multimodal causal language model featuring Hybrid Attention with QSA and N-gram Embeddings for significantly reduced long-context latency. It excels in agentic workloads and supports context lengths up to 1,000,000 tokens, making it ideal for complex reasoning and large-scale data processing.

`image-text-to-text` `176.9B`

⬇️ 328,195 • ❤️ 602 • 2d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 8,839,153 • ❤️ 3,237 • 10d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 1,137,181 • ❤️ 2,261 • 11h ago

---

**[Hy4-preview](https://huggingface.co/tencent/Hy4-preview)**

*Tencent*

Hy4-preview is a 770B parameter Mixture-of-Experts (MoE) text generation model with 49B activated parameters per token, featuring a 1M context length and Gated Sparse Attention. It excels in productivity tasks across software engineering, office analysis, game development, and scientific research, offering significant gains in understanding, reasoning, and code generation.

`text-generation` `780.0B`

⬇️ 2,123 • ❤️ 319 • 2d ago

---

**[GLM-5.3-Flash-GGUF](https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF)**

*Unsloth AI*

GLM-5.3-Flash is a natively multimodal LLM optimized for efficiency and capability, featuring a hybrid sparse/linear attention architecture. It excels in long-context tasks, coding, and agentic benchmarks, offering performance competitive with leading models at a fraction of the cost, suitable for advanced AI applications.

`text-generation` `320.8B`

⬇️ 45,936 • ❤️ 288 • 1d ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 725,757 • ❤️ 946 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 102 • 💬 2 • ⭐ 9,927 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 764 • 💬 5 • ⭐ 9,052 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 125 • 💬 6 • ⭐ 101,819 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**

*Seth Karten, Alex L. Zhang, Kevin Thomas et al. (11 authors)*

🏢 Prime Intellect

Prime Agent is an open-source harness that uses recursive subagents, persistent computation, and agent-to-agent coordination to extend language models' long-horizon capabilities across coding and reasoning tasks.

▲ 46 • 💬 2 • ⭐ 19,247 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23552) • [💻 code](https://github.com/PrimeIntellect-ai/prime-agent) • [🔗 project](https://www.primeintellect.ai/blog/prime-agent)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 202 • 💬 3 • ⭐ 1,296 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://huggingface.co/papers/2608.24053)**

*Junjie Zhou, Ke Mei, Lei Li et al. (6 authors)*

🏢 Tencent

WeMM-Embedding is a family of universal multimodal embedding models that align text, images, videos, and interleaved inputs in a shared space, achieving state-of-the-art retrieval and recommendation performance across public benchmarks and large-scale WeChat applications.

▲ 67 • 💬 2 • ⭐ 928 • 6d ago

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

⭐ 19.5k • 🔱 2.3k • 8h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 3.5k • 🔱 440 • 2d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.3k • 🔱 258 • 19d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 3.3k • 🔱 400 • 30m ago

---

**[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)**

FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools, with cost-aware routing across LLM providers.

`Python` `agent` `ai` `ai-agent` `ai-coding` `autonomous-agent`

⭐ 3.0k • 🔱 179 • 7d ago

---

**[Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy)**

Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion.

`JavaScript` `ai-agents` `claude` `claude-code` `llm` `productivity`

⭐ 2.8k • 🔱 167 • 1d ago

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

⭐ 2.1k • 🔱 198 • 1d ago

---

**[SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI)**

WeChat AI - 自托管微信角色扮演对话服务

`TypeScript`

⭐ 1.9k • 🔱 1.3k • 13h ago

---

---

*Generated by PeekDeck - A glance is all you need*
