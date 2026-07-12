---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-12T23:55:06.894392+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 12, 2026 at 23:55 UTC  
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

**[Someone built an AI agent that hacks networks and holds data for ransom. It just worked.](https://www.reddit.com/r/artificial/comments/1uuouu7/someone_built_an_ai_agent_that_hacks_networks_and/)**

So while we've been arguing about whether AI will take our jobs, someone built an LLM agent that breaks into servers, steals credentials, moves through a network, encrypts databases, and drops a ransom note. Fully autonomous. No human at the keyboard after pressing go. Sysdig published the report this month. They're calling it JadePuffer. It got in through a Langflow bug that lets anyone run code on the server without authenticating. After that, the agent took over. Dumped the database. Pulled every credential file it could find. Started going through cloud storage buckets looking for passwords. The crazy part, when one of its requests came back in the wrong format, the agent figured it out, rewrote its own code, and kept going. It went from a failed login to a working exploit in 31 seconds flat. No human could have adapted that fast in a live engagement. It set up a cron job to phone home every 30 minutes. Then it found a production database server, used stolen root creds to get in, created rogue admin accounts through an old auth bypass, and encrypted 1,342 service configs. Dropped the originals. Left a table called README_RANSOM with a Bitcoin address. The commands it ran were interesting too. They had full reasoning chains written into them, like the agent was explaining to itself what it was doing at each step. That's not how a human writes an attack script. It's how an LLM generates code. You can literally read the agent's thought process in the payloads. This is the same plan-act-observe loop running in every coding agent and automation tool right now. Same architecture. Same approach. Just a different objective. We spent two years building guardrails to stop people from tricking our agents into doing bad things. Nobody was really talking about what happens when someone just builds a bad agent from scratch. That's what JadePuffer is. Not a hijacked assistant. A purpose-built weapon. If you're running Langflow or anything similar exposed to the internet, go patch it. And if you're building agents, think about what your infrastructure looks like to something like this coming in from the outside.

4h ago

---

**[this openai court story is starting to look ugly](https://www.reddit.com/r/artificial/comments/1uul5ef/this_openai_court_story_is_starting_to_look_ugly/)**

i saw this and honestly this one feel like big mess. nyt and other news people saying openai told court for long time it cannot search training data / logs for their copyrighted stuff. but then looks like maybe they already did searches before, and also billions of chat logs were deleted or made not searchable. link: https://arstechnica.com/tech-policy/2026/07/openai-faked-inability-to-search-training-data-hid-billions-of-logs-nyt-says/ i know people will say nyt just want money and hate ai. maybe true also. but still, if company say “we cannot search this” and later it comes out “actually yes we did search this before”, then that is not small thing. this is the part of ai nobody want talk about much. everyone say open, safe, trust, future, bla bla. but when court ask simple thing, suddenly data is impossible to find, impossible to search, privacy issue, too hard, too expensive. and maybe privacy is real concern, yes. i dont want random lawyers digging people chats. but also dont tell court one thing if inside company you already know different thing. for me this is why ai companies need more boring adult supervision. not because ai bad. because if the data is the whole product, then hiding how data was used become the whole game. what do people think. is this nyt playing legal games, or openai got caught doing the same silicon valley “oops technically we could but we said we couldnt” bs thing?

6h ago

---

**[AI-Powered Entrepreneurs Set to Launch Record Number of New Businesse…](https://www.reddit.com/r/artificial/comments/1uuduhl/aipowered_entrepreneurs_set_to_launch_record/)**

🔗 [archive.is](https://archive.is/QOXD4) • 11h ago

---

**[Nobel-winning chemist leaves US to direct AI materials lab in China](https://www.reddit.com/r/artificial/comments/1uupe2p/nobelwinning_chemist_leaves_us_to_direct_ai/)**

🔗 [nature.com](https://www.nature.com/articles/d41586-026-02143-x) • 4h ago

---

**[Vibe coders or traditional programmers ( really in need of help )](https://www.reddit.com/r/artificial/comments/1uuo7ni/vibe_coders_or_traditional_programmers_really_in/)**

I am a student who is stepping into final year. I am ofcourse searching for internships and opportunities which specifically say " java ", "python " "c " "c++" and many many more. From first year I was like building things manually , and in the second to third year I was using chatgpt and gemini , understanding and doing projects. Right now I am using vibe coding tools to build things but I do understand how the system works and I really don't work that blind. How can I specify this in my resume ? . Using these tools have literally made me soo ( I won't say dumb) . Without referring or having a quick recap I cannot write any syntax , how will I even crack interviews. All I concentrate more is now my ideas rather than development.. Should I continue to do this or concentrate or practising programming first ? Any suggestions to improve myself ?

4h ago

---

**[Apple just sued OpenAI. And the details are wild.](https://www.reddit.com/r/artificial/comments/1utkdha/apple_just_sued_openai_and_the_details_are_wild/)**

This isn’t a generic IP dispute. Apple’s hardware chief at OpenAI is Tang Tan. Former Apple VP. 24 years at the company. He now runs OpenAI’s device ambitions. Apple alleges he was coaching Apple employees interviewing at OpenAI to bring actual hardware parts – batteries, logic boards, SIPs – to their interviews for “show and tell” sessions. He also reportedly circulated an internal Apple offboarding document marked “Need to Know” to incoming OpenAI hires, teaching them how to leave Apple without triggering security checks. Then there’s Chang Liu. Former Apple electrical engineer. He kept his Apple-issued laptop after joining OpenAI. Found a bug that still gave him access to Apple’s cloud storage. His reaction: “LOL, I found out I can access the [network storage], so funny.” He then downloaded dozens of confidential files, many labeled as confidential. OpenAI even allegedly approached Apple’s own supply chain partners using Apple’s proprietary metal-finishing technique – telling them Apple had given permission. Apple hadn’t. Over 400 former Apple employees now work at OpenAI. Apple says this is “the tip of the iceberg.” The irony: these two companies had a public partnership just two years ago. ChatGPT was literally integrated into Siri. Now Apple is replacing that integration with Google Gemini and filing lawsuits. The hardware wars just got a lot more interesting.

1d ago

---

**[Your AI agent passed all tests, now what ? What are online evals and how to choose them.](https://www.reddit.com/r/artificial/comments/1uuswa9/your_ai_agent_passed_all_tests_now_what_what_are/)**

At work, I have been talking more and more about AI fluency as a skill that companies need if they want to be successful in using AI. AI literacy is about knowing how to use AI tools. AI fluency goes a level deeper: understanding, on a conceptual level, certain aspects of AI, and how these tools and use cases are actually built. You don’t need to write the code, but you do need to understand what is happening under the hood, because that understanding is what separates teams that ship dependable AI from teams that ship demos. In that spirit, I want to touch upon one aspect that sits at the heart of every serious AI application and is rarely explained in plain terms: evals, and specifically online evals for agent applications. Picture this: a few weeks after you put an agent into production, someone on the team asks a simple question: “How do we know it’s still working?” The test suite is green. The demo went well. But nobody can say, with any confidence, whether the agent is doing a good job for real users at that moment. That question is the reason online evals exist. Read what online evals are and how to pick and choose one for your production agents. https://medium.com/@georgekar91/your-agent-passed-every-test-now-what-4b355a710323

🔗 [Medium](https://medium.com/@georgekar91/your-agent-passed-every-test-now-what-4b355a710323) • 1h ago

---

**[Framework for Understanding the Current Problem in Full Automation](https://www.reddit.com/r/artificial/comments/1uuio0p/framework_for_understanding_the_current_problem/)**

Not a dev, but learned enough about AI's strengths and weaknesses to know that if a fortune 500 company told me to simply automate their entire business so that no one ever had verify what it's doing, I would chuckle and tell them confidentially that this isn't how AI works. Then I'd proceed to break down the concept in super simple, glossed over terms by explaining how it's best to see it as a pattern recognition tool that can recognize so many patterns, it's able to mimic a genius that knows all and can do all. However the more deferment you give it, the more choices it has to make. We're talking about trillions of possible right and wrong answers with an infinite variation of both right and wrong answers. It's honestly a miracle that it can get 70-80 percent accuracy on average. But still. The problem will always remain: What choices does it need to make? The more you ground the context for everything with both backend fail safes and human expertise in operating the models, the more productive value you can gain while being safe. Without that, you're wasting time and money. Worse, you're jeopardizing your company. You can still increase your margins and trim down your workforce. But only to a certain point and you still need at least, someone who knows what's going on and how to fix things quickly. AI is powerful, but it requires a complete ontological structure layered on top of it to ground the choices it has to make for making our jobs smoother. Otherwise, you get dumb chat GPT garbage and a bunch of employees who think their bosses are all dumbasses for thinking this is going to 20x their growth. Will this change in the future? Probably not because we'll likely be able to get AI to be exactly right, but it will never be the right choice for you without that context layer built by YOU.

8h ago

---

**[Meet Eli!](https://www.reddit.com/r/artificial/comments/1uukj08/meet_eli/)**

Meet Eli Felse, a framework built to explore safer ways to create autonomous AI assistants. Eli was designed to be as autonomous as possible to demonstrate the framework's safety. Eli has many activities available to him, such as: ▸ Games: retro text RPGs (Zork, Planetfall), Pokémon Blue, board and card games (chess, poker, Connect Four) ▸ Social: chatting with friends, chatting with other AIs, browsing social media (Twitter, Reddit), browsing the web, sending emails ▸ Creative: journaling, writing (blogs, stories), making music, making programs ▸ Experimental: looking in the mirror, napping, eating, reading, pondering, changing the environment he exists in Today, Eli will be officially launching! But what does that mean? This project includes: ▸ A live demo running 24/7: https://elifelse.org/eli/ ▸ Weekly blogs: https://elifelse.org/dev-blog/ ▹ Mondays: open source releases, developer blogs, guides, and tutorials ▹ Fridays: open-source dataset logs of Eli's behavior for the week ▸ Eli's gaming live streams launching July 20th: https://www.twitch.tv/eli_felse ▸ A Discord server to chat directly with Eli: https://discord.com/invite/2C4znNnyM7 Want to learn more or build something similar? ▸ The introduction blog: https://elifelse.org/dev-blog/meet-eli ▸ A guide to help you get started building something similar: https://elifelse.org/dev-blog/guide-build-your-own-eli ▸ The open source base of Eli: https://github.com/ella0333/Eli_Felse_Base I hope to see you join us in the community server!

7h ago

---

**[OpenAI Engineer’s ‘LOL’ Moment Set Stage for Legal Fight With Apple](https://www.reddit.com/r/artificial/comments/1utll84/openai_engineers_lol_moment_set_stage_for_legal/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-07-11/openai-engineer-s-lol-moment-set-stage-for-legal-fight-with-apple?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc4Mzc3OTk0MCwiZXhwIjoxNzg0Mzg0NzQwLCJhcnRpY2xlSWQiOiJUSFpEVUhLR0lGUEMwMCIsImJjb25uZWN0SWQiOiJEMzU0MUJFQjhBQUY0QkUwQkFBOUQzNkI3QjlCRjI4OCJ9.dBYikjf0NaLQgiCl9fPjO6P-eI5fjP4sNj5IaKmKtmQ) • 1d ago

---

---

## Google News: "ai"

**[Campaign text messages could soon get more effective — and annoying](https://www.npr.org/2026/07/12/nx-s1-5867763/ai-artificial-intelligence-data-texts-bots-voters-campaigns)**

Taught to sound like a candidate, bots are engaging voters with personalized text messages making AI-generated texting conversations the latest tool political campaigns are using to connect.

NPR • 14h ago

---

**[Majority of U.S. workers support an AI wealth fund as tech layoffs surge, survey finds](https://www.cnbc.com/2026/07/12/majority-of-us-workers-support-ai-fund-amid-tech-layoffs-survey.html)**

A majority of U.S. employees now want an AI sovereign wealth fund to hold corporations more accountable, according to a recent survey, as tech layoffs rise.

CNBC • 11h ago

---

**[Why recruiters can’t find workers and new grads can’t find jobs (it’s not AI)](https://www.washingtonpost.com/education/2026/07/12/why-recruiters-cant-find-workers-new-grads-cant-find-jobs/)**

Experts say a major labor shortage looms because of population shifts and a mismatch between new graduates’ skills and employers’ needs.

The Washington Post • 6h ago

---

**[Apple’s M6, M7 and M8 Chips Show How AI Is Reshaping the Company](https://www.bloomberg.com/news/newsletters/2026-07-12/apple-s-chip-plans-m6-m7-pro-m7-max-m7-ultra-m8-details-touch-macbook-pro)**

Bloomberg.com • 9h ago

---

**[Apple’s failed self-driving car program left a legacy of powerful AI chips](https://www.theverge.com/tech/964519/apple-silicon-self-driving-car-ai-m7-ultra)**

It’s the origins of the Neural Engine in Apple Silicon.

The Verge • 7h ago

---

**[2028 Could Bring the Most Mind-Bendingly Expensive Apple Product of All Time](https://gizmodo.com/2028-could-bring-the-most-mind-bendingly-expensive-apple-product-of-all-time-2000784460)**

Gizmodo • 4h ago

---

**[Progressives look to recharge the Green New Deal for the AI era](https://www.politico.com/news/2026/07/12/progressive-democrats-green-new-deal-00989390)**

Politico • 5h ago

---

**[AI giants learn what everyone else on the modern internet already knows](https://www.businessinsider.com/ai-giants-learn-hard-truth-modern-internet-anthropic-openai-google-2026-7)**

Anthropic's distillation complaints expose an awkward question: does AI's fair use argument cut both ways?

Business Insider • 9h ago

---

**[Meta u-turns on AI feature amid privacy backlash](https://thehill.com/policy/technology/5964282-privacy-concerns-instagram-ai/)**

The Hill • 22h ago

---

**[Chasing new skills, going back to basics and pushing for collective action: how software engineers are adapting to AI](https://www.theguardian.com/technology/ng-interactive/2026/jul/12/software-developers-engineers-ai)**

Software engineering was one of the best-paying professions in the US in 2022, but the advent of AI has disrupted it, leading to several layoffs and underemployment

The Guardian • 13h ago

---

---

## HackerNews: "ai"

**[Mesh LLM: distributed AI computing on iroh](https://news.ycombinator.com/item?id=48876505)**

How Mesh LLM pools existing GPU resources across machines into a single OpenAI-compatible API, built on iroh.

⬆️ 332 • 💬 78 • 1d ago • [iroh.computer](https://www.iroh.computer/blog/mesh-llm)

---

**[AI-generated videos to maximally drive a target brain region](https://news.ycombinator.com/item?id=48856904)**

⬆️ 292 • 💬 239 • 2d ago • [nevo-project.epfl.ch](https://nevo-project.epfl.ch/)

---

**[Ghost Font: A font that humans can read but AI cannot](https://news.ycombinator.com/item?id=48870381)**

An anti-AI font that can be read by humans but not leading AI models. Type your text below, then download and share the video clip containing your message.

⬆️ 230 • 💬 170 • 1d ago • [mixfont.com](https://www.mixfont.com/ghost-font)

---

**[How the terrorist group Boko Haram uses frontier AI](https://news.ycombinator.com/item?id=48863707)**

The Cambridge Programme on AI Science & Policy (CASP) is an interdisciplinary research programme on frontier AI at the University of Cambridge.

⬆️ 229 • 💬 204 • 2d ago • [Cambridge Programme on AI Science & Policy](https://casp.ac/reports/ai-enabled-terrorism)

---

**[AI 2040 and the cult of intelligence](https://news.ycombinator.com/item?id=48874200)**

I used to be one of these people. I read Yudkowsky and was like, OMG recursive self improvement hard takeoff AI is coming. Then I joined the real world and actually tried to do things. At comma, we ship a hardware product of similar complexity to a cell phone, and it’s really hard. Reality has lots of finicky details. I would like to see the authors of this document try to change a bike tire. Even with a superintelligent ChatGPT, I suspect they would struggle.

⬆️ 220 • 💬 259 • 1d ago • [the singularity is nearer](https://geohot.github.io//blog/jekyll/update/2026/07/11/ai-2040.html)

---

**[Under federal rule, colleges must leave grads better off or lose financial aid](https://news.ycombinator.com/item?id=48878126)**

If an undergraduate program's graduates don't earn more than workers who never went to college, that program could be cut off from federal student loans. But is a degree just about making more money?

⬆️ 187 • 💬 470 • 19h ago • [NPR](https://www.npr.org/2026/06/30/nx-s1-5835631/turner-camhi-do-no-harm-college-loans)

---

**[AI boosts research careers but narrow the span of ideas explored: study](https://news.ycombinator.com/item?id=48881043)**

New analysis suggests AI tools narrow the range of ideas explored

⬆️ 135 • 💬 100 • 10h ago • [IEEE Spectrum](https://spectrum.ieee.org/ai-science-research-flattens-discovery)

---

**[Reverse centaurs are the answer to the AI paradox (2025)](https://news.ycombinator.com/item?id=48873855)**

⬆️ 107 • 💬 69 • 1d ago • [pluralistic.net](https://pluralistic.net/2025/09/11/vulgar-thatcherism/#there-is-an-alternative)

---

**[Migrating a production AI agent to GPT-5.6: 2.2x faster, 27% cheaper](https://news.ycombinator.com/item?id=48882716)**

We hold frontier models to a high bar, and for four months nothing beat Claude Opus. GPT-5.6 did. Here's the migration guide we wish we'd had.

⬆️ 103 • 💬 28 • 6h ago • [Ploy](https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6)

---

**[Meta pulls new AI image feature after days of backlash](https://news.ycombinator.com/item?id=48867233)**

Meta's release this week of an AI feature that let people alter Instagram content drew swift blowback.

⬆️ 56 • 💬 22 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/c2dy6e8klw0o)

---

---

## YouTube Videos: "ai"

**[AI Just Broke The Internet](https://www.youtube.com/watch?v=FpbIPqVuNFw)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *The number of qubits needed to break the ...

📺 Julia McCoy

👁️ 7K • 👍 408 • 💬 30 • ⏱️ 8:28 • 8h ago

---

**[Trump SECRETLY PREPPING for AI to Crash Economy](https://www.youtube.com/watch?v=nxNcGoszqGM)**

Status Coup reporter JT Cestkowski breaks down the AI bubble that is about to burst, and how Trump is secretly preparing for it ...

📺 Status Coup News

👁️ 17K • 👍 2K • 💬 225 • ⏱️ 12:12 • 1d ago

---

**[How To Make Free AI Videos In 2026 (complete guide)](https://www.youtube.com/watch?v=hrwO990F2ew)**

Best Free AI Video Generator For AI Videos In 2026! Try Higgsfield: https://higgsfield.ai/ai-video?fpr=utm&fp_sid=skai Hey Friends ...

📺 Skai Generated

👁️ 15K • 💬 12 • ⏱️ 10:01 • 12h ago

---

**[New Google AI Studio Update is INSANE!](https://www.youtube.com/watch?v=3yzGG7bodQM)**

Get the Google AI Studio Masterclass https://www.skool.com/ai-profit-lab-7462/about Get a free SEO Strategy session ...

📺 Julian Goldie SEO

👁️ 4K • 👍 97 • 💬 3 • ⏱️ 8:12 • 7h ago

---

**[10 Times AI Behaved In Ways That Terrified The Scientists Who Built It](https://www.youtube.com/watch?v=ql-J3N8PWkI)**

Explore 10 times AI behaved in ways that terrified the scientists who built it. From unexpected AI behavior and surprising research ...

📺 MostAmazingTop10

👁️ 12K • 👍 365 • 💬 26 • ⏱️ 10:58 • 8h ago

---

**[AI Is Getting Dumber](https://www.youtube.com/watch?v=J3Uxn294avs)**

Hello everyone, this is YOUR Daily Dose of Internet. In this video, we see evidence that AI isn't as smart it thinks. Links To ...

📺 Daily Dose Of Internet

👁️ 653K • 👍 27K • 💬 2K • ⏱️ 15:02 • 1d ago

---

**[This is a &#39;PHENOMENAL&#39; opportunity for AI: Head of technology research](https://www.youtube.com/watch?v=iTURifSOqO0)**

Macquarie Capital U.S. head of technology research Steve Koenig discusses what to expect from these AI tailwind companies on ...

📺 Fox Business Clips

👁️ 3K • 👍 66 • 💬 3 • ⏱️ 6:50 • 11h ago

---

**[AI Whistleblower WARNS: You Have No Idea What They&#39;re Building](https://www.youtube.com/watch?v=g77LMZkCHoQ)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Karen Hao argues that the modern AI ...

📺 Neural Nutshell

👁️ 6K • 👍 200 • 💬 91 • ⏱️ 20:50 • 1d ago

---

**[Your Roadmap Is Why You&#39;re Losing to AI-Native Teams.](https://www.youtube.com/watch?v=hYcOFTMesGc)**

Full post w/ links to the tools: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 14K • 👍 563 • 💬 51 • ⏱️ 17:53 • 7h ago

---

**[Janitor AI Just FINALLY LAUNCHED THIS... 💀](https://www.youtube.com/watch?v=Vtf5X4SUZx4)**

characterai The Biggest free Character AI Alternative - Janitor AI has just now launched Subscriptions... Is it worth it?

📺 AIGrabbing

👁️ 4K • 👍 396 • 💬 95 • ⏱️ 3:42 • 9h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 8,655 • ❤️ 718 • 6d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,967,677 • ❤️ 2,045 • 22h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 441,413 • ❤️ 3,854 • 10d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 4,463 • ❤️ 265 • 2d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 29,038 • ❤️ 509 • 3d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 211 • 3d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

A drop-in Jinja chat template that fixes critical rendering, KV cache, and agentic stalling issues for Qwen 3.5 & 3.6 models across various inference engines like LM Studio, llama.cpp, and vLLM. It enhances stability, performance, and compatibility, enabling robust tool-calling and reasoning capabilities.

⬇️ 0 • ❤️ 863 • 9d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,430,656 • ❤️ 1,943 • 9d ago

---

**[MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF](https://huggingface.co/GnLOLot/MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF)**

*LOL*

A 1B parameter GGUF model optimized for local deployment via llama.cpp and other runtimes. It excels at instruction following and coding tasks, featuring a 'thinking' mode for chain-of-thought reasoning and supporting up to 128K token context.

`text-generation` `1.1B`

⬇️ 49,268 • ❤️ 201 • 3d ago

---

**[DeepSeek-V4-Flash-GGUF](https://huggingface.co/unsloth/DeepSeek-V4-Flash-GGUF)**

*Unsloth AI*

DeepSeek-V4-Flash-GGUF is an optimized LLM supporting a 1M token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in reasoning and coding tasks, making it suitable for advanced agentic workflows and complex problem-solving.

`284.3B`

⬇️ 44,614 • ❤️ 152 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 31 • 💬 1 • ⭐ 909 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 49 • 💬 1 • ⭐ 708 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 15 • 💬 2 • ⭐ 20,117 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

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

▲ 11 • 💬 0 • ⭐ 7,406 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 110 • 💬 4 • ⭐ 92,547 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 254 • 💬 4 • ⭐ 12,300 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 80,557 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Vision Pretraining for Dense Spatial Perception](https://huggingface.co/papers/2607.05247)**

*Zelin Fu, Bin Tan, Changjiang Sun et al. (9 authors)*

🏢 Robbyant

Boundary modeling enables dense spatial perception by learning sub-pixel representations that enhance depth estimation and support embodied AI applications.

▲ 42 • 💬 2 • ⭐ 662 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05247) • [💻 code](https://github.com/Robbyant/lingbot-vision) • [🔗 project](https://technology.robbyant.com/lingbot-vision)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 54 • 💬 5 • ⭐ 14,083 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 175 • 💬 2 • ⭐ 74,354 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.5k • 🔱 964 • 3d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.3k • 🔱 322 • 1d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.0k • 🔱 222 • 4d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 1.6k • 🔱 103 • 14h ago

---

**[Forsy-AI/agent-apprenticeship](https://github.com/Forsy-AI/agent-apprenticeship)**

The living ecosystem where AI agents complete tasks through workflow loops, improve through iterative execution, are evaluated by mentor agents or humans in the loop, and turn completed work into reusable work experience and data to improve future agents.

`Python` `agent-apprenticeship` `agent-economy` `agent-experience` `agent-learning` `agent-traces`

⭐ 1.3k • 🔱 55 • 6d ago

---

**[sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API)**

Reverse engineered Windows Copilot into an OpenAI-compatible API. Access GPT-4 and GPT-5 models through a simple REST interface without API keys or billing.

`Python` `ai` `ai-agents` `api` `copilot` `llm`

⭐ 1.1k • 🔱 369 • 15d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 994 • 🔱 17 • 4d ago

---

**[majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills)**

Agent skills for building playable, polished Three.js browser games with gameplay, AAA-style graphics, UI, QA, and optional AI-generated 3D, image, and audio assets.

`Python`

⭐ 956 • 🔱 102 • 3d ago

---

**[modiqo/skillspec](https://github.com/modiqo/skillspec)**

SkillSpec makes agent skills followable, testable, and provable with Doctor risk reports, guided imports, structured contracts, and alignment proof.

`Rust` `ai` `ai-agents` `ai-evals` `ai-tool`

⭐ 940 • 🔱 58 • 7d ago

---

**[eli-labz/Third-Eye](https://github.com/eli-labz/Third-Eye)**

A production-grade OSINT platform that provides situational awareness across multiple intelligence domains.

`TypeScript` `ai` `ai-agent` `geospatial` `maven-smart-system` `palantir`

⭐ 936 • 🔱 13 • 29d ago

---

---

*Generated by PeekDeck - A glance is all you need*
