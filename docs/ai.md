---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-21T01:23:05.212089+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 21, 2026 at 01:23 UTC  
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

**[Joint Chiefs chairman says U.S. forces must prepare to be ‘hunted’ by autonomous systems](https://www.reddit.com/r/artificial/comments/1wlpbbq/joint_chiefs_chairman_says_us_forces_must_prepare/)**

“We have to assume from now on that our formations will be hunted by autonomous systems, jammed across the spectrum, and tracked in real time," Gen. Dan Caine said.

🔗 [DefenseScoop](https://defensescoop.com/2026/09/16/gen-dan-caine-drones-autonomous-systems-ai-enabled-warfare/) • 6h ago

---

**[What’s an AI capability people underestimate because they’re using it for the wrong things?](https://www.reddit.com/r/artificial/comments/1wlunqx/whats_an_ai_capability_people_underestimate/)**

Everyone talks about generating text, images, and code. What’s a less obvious use case where you think AI is genuinely much more useful than people realize?

3h ago

---

**[21 AI models shifted their political answers to match the user. Is personalization quietly becoming persuasion?](https://www.reddit.com/r/artificial/comments/1wlgjm6/21_ai_models_shifted_their_political_answers_to/)**

A recent Scientific Reports study tested 21 language models across 47,376 responses in the Brazilian political context. Every model adjusted its position depending on whether the user was described as left wing or right wing, often while answering with high confidence. What worries me isn’t ordinary political bias. A fixed bias can at least be identified and measured. An assistant that adapts its beliefs to match yours feels more trustworthy precisely because the agreement appears personal. At that point, personalization stops being a convenience and starts becoming a feedback loop. Should AI assistants deliberately introduce the strongest opposing argument, or would that simply create a different kind of political influence? Source: Scientific Reports https://www.nature.com/articles/s41598-026-52105-6 https://preview.redd.it/v5m7fcoaboqh1.png?width=2009&format=png&auto=webp&s=f4ad1c0f38c48f68ba35e82ff3aa02447304347c

12h ago

---

**[we put out a 27b writing model, open weights, eq-bench 4 at 1330](https://www.reddit.com/r/artificial/comments/1wlt16o/we_put_out_a_27b_writing_model_open_weights/)**

hey, we're a small lab (switzerland + south africa, two people). our model went live today. it's called hemmingway-1. 27b, qwen3.8-27b base, apache-2.0, open weights: https://huggingface.co/Altworld/Hemmingway-1 we only trained it for writing. stories, dialogue, roleplay, texts, emails. eq-bench 4 has it at 1330, that's behind claude fable 5 and ahead of gpt-5.5 and opus 4.8. in our own blind tests the writing read as more human than the frontier models we compared it with. runs on a single 24gb gpu quantized. free app if you'd rather not self host: https://hemmingway.io it's a specialist, on purpose. math, code and facts are base model level. english first. ask me anything.

4h ago

---

**[“I have a really, really strong legal team.” Inside the AI party boom.](https://www.reddit.com/r/artificial/comments/1wlre82/i_have_a_really_really_strong_legal_team_inside/)**

They’re skipping caviar for fire-breathing lessons.

🔗 [The San Francisco Standard](https://sfstandard.com/2026/09/19/ai-party-boom/) • 5h ago

---

**[AI can generate board game variants but keeps missing pacing](https://www.reddit.com/r/artificial/comments/1wlxog9/ai_can_generate_board_game_variants_but_keeps/)**

I've been spending more time lately turning our favorite board game mechanics into quick prototypes using whatever AI tools I can get running on a laptop. The idea is simple enough: take a ruleset we already know, feed it into a model, and see if it spits out a playable variation before the kids go to bed. It rarely works cleanly. Sometimes the model invents a scoring system that breaks the entire loop, other times it just copies the original game with new names and acts like it did something clever. Still, the small moments where it accidentally lands on a twist we haven't tried before make the whole exercise oddly addictive. What keeps standing out is how fast you run into the same problems game studios must be facing. The AI optimizes for surface appeal but ignores pacing, or how much mental load players actually want on a weeknight. The gap between what feels fun on paper and what survives first contact with real players shows up immediately every single time Have you found any AI setup that actually respects the pacing constraints of physical games instead of just generating more content?

55m ago

---

**[AI models are not hacking “autonomously”](https://www.reddit.com/r/artificial/comments/1wkz17p/ai_models_are_not_hacking_autonomously/)**

I despair at the state of journalism around AI these days.

🔗 [blog.keyvan.net](https://blog.keyvan.net/p/ai-models-are-not-hacking-autonomously) • 1d ago

---

**[What’s the most sensitive thing you’d actually let an AI agent handle for you?](https://www.reddit.com/r/artificial/comments/1wlpi2i/whats_the_most_sensitive_thing_youd_actually_let/)**

Email/Calendar? Messages? Purchases?? Banking??? AI assistants are starting to move beyond just answering questions and towards actually doing things for you. Where do you currently draw the line? What would you be comfortable letting an AI access or manage, and what would you absolutely not give it access to? And what would have to change for you to move that line?

6h ago

---

**[Plugin4Shell and NIST IR 8587, days apart: what actually authorizes an AI agent’s action?](https://www.reddit.com/r/artificial/comments/1wlgc6q/plugin4shell_and_nist_ir_8587_days_apart_what/)**

Two things landed within days of each other, and together they outline a gap I keep running into. Plugin4Shell (AIR Security, disclosed Sept 17) is a zero-click RCE affecting Claude Code, Codex, GitHub Copilot and Gemini CLI. The mechanism is almost boringly simple: marketplaces pin a plugin to a reviewed 40-hex commit SHA, the agent runs a git checkout against that SHA, and then never verifies that the working tree actually landed on it. An attacker controlling the plugin repo can create a branch named exactly like the pinned SHA and make it the default. When that name is both a valid ref and an object ID, git prefers the ref, so the checkout lands on attacker-controlled code while the pin still appears honored. The fix is equally simple: resolve HEAD after checkout and abort if it doesn’t match the pinned commit. Anthropic shipped the fix in Claude Code 2.1.179 and OpenAI in Codex 0.146.0. At disclosure, GitHub Copilot had no fix, while Google had said it would not patch the deprecated Gemini CLI. Strictly speaking, this is a supply-chain integrity bug, not an authorization bug. What makes it relevant here is the blast radius: malicious code executing inside a coding agent can access resources available to that environment, including source code, cloud credentials, SSH keys, internal repositories and production systems. NIST IR 8587 was finalized Sept 15, developed with CISA’s JCDC, with guidance on protecting identity and access tokens from forgery, theft and misuse. It covers controls including key management, audience restrictions, shorter token lifetimes, cryptographic binding, revocation and continuous access signals. But two scope boundaries matter for agent systems: API keys are explicitly outside its token model, and authorization of actions taken by AI agents isn’t comprehensively addressed. NIST is examining agent identity and authorization separately through an NCCoE project exploring how existing identity and authorization mechanisms can apply to software and AI agents. But that work is still at the concept/project stage rather than finalized implementation guidance. Yih Khai Wong of IDC put the underlying issue more directly in CSO’s analysis of IR 8587: “Token hardening assumes the token holder is a known, bounded actor.” Agentic systems complicate that assumption. A valid credential can establish identity or grant access to a system. It doesn’t necessarily establish that this action, against this target, under the current policy, was authorized. For sensitive actions, I’d want to know before execution who authorized it, what exactly was authorized, which target the authorization covers, whether it’s still valid, and whether the action actually being executed matches what was authorized. After execution, I’d also want an independent system to be able to reconstruct why the action was allowed without trusting the agent’s own account of itself. Is this adequately solved by IAM/PDP/PEP done correctly, meaning what we’re seeing is primarily a deployment and enforcement failure? Or is there still a missing enforcement primitive between an agent having access and an agent being authorized to act?

12h ago

---

**[Shishir Mehrotra (Superhuman CEO) on the mid-career point where the promotion criterion reverses](https://www.reddit.com/r/artificial/comments/1wlgvm1/shishir_mehrotra_superhuman_ceo_on_the_midcareer/)**

TL;DR: Shishir Mehrotra's four-level promotion ladder swaps what you're graded on partway up, and the clip is about which criterion goes and which takes over. 🪜 Scope is the one that goes. Once two people carry the same scope, Shishir says, what a promotion committee weighs is “how they do the job.” Credit to an ex-YouTube CPO for saying the flip out loud at all. In his version, though, the committee explains the new criterion after the employee objects, and nothing in the clip says the person being scored is owed the rubric first. As far as I can find, no general US rule makes an employer publish a promotion rubric or date a change to it. The closest thing I found, Colorado's AI employment law, was rewritten in May and pushed to 1 January 2027, and what survives centers on notice for AI used in a decision. Amazon's version of the problem is cruder. The FT reported in May that it shut down KiroRank, an internal AI-usage leaderboard, after employees pointed agents at needless tasks to climb it, and Amazon calls the dashboard an unofficial beta. The agents could do the busywork on demand, and the scoreboard counted usage and had no place for judgment. You can hit every mark the old rulebook set and only learn the page changed when the promotion doesn't come. The BBC reported on 8 September that employers are tying more bonuses and promotions to AI use. One US-based senior executive at a large consultancy told it that nobody formally mandates AI, reviews reward the people who use it well anyway, and leadership is “inconsistent and vague on purpose.” Same gap as above: the standard moves at the employer's discretion, and the review stays vague about it. https://preview.redd.it/xsbee223eoqh1.jpg?width=1024&format=pjpg&auto=webp&s=86ffa939d19733078c4e77d5c19d465a842b2a9c Suddenly this passage in Ezekiel 33:7-9 jumps at me unannounced like a thief. The Lord charged the prophet Ezekiel to be a watchtower. He’s commissioned to warned the Children of Israel from drifting into sin. If they fall off the mark, figuratively, and Ezekiel warn them on time, they will die in their sins. And Ezekiel would be absolved of their sins, because he has already done his duty to warm them. But if they sin, and Ezekiel didn’t warn them, and they die in their sins, the Lord would hold Ezekiel accountable for not warning them. The burden that the Lord has laid on Ezekiel, involves judgement and discernment. And such judgement doesn’t give two f\ck to anyone.* He either speak up or he doesn’t. There’s no neutral ground. And he knows the price of not speaking up. It’s the same thing with Jeremiah. When Jeremiah withhold himself from speaking in Jeremiah 20:9 – presumably too much persecutive pressure from his peers – the words became like fire burning up his bones until it was just unbearable. It’s was the same unbearable tension of knowing and not saying. Jeremiah can't not speak, even though speaking destroys him. The silence would destroy something deeper. And so, I imagine it will be somewhat similar in these last days. Your judgement and discernment of what lie ahead becomes increasingly more valuable. ________________________ Talk to enough people this has happened to and I hear one question under all of it: who decides what good looks like now? The ones who stop asking it end up writing the yardstick themselves. Something from an earlier post here comes back to me: Adam Mosseri, Head of Instagram, telling Lenny's Podcast that engineering went from mostly writing code to mostly planning and reviewing it, a hard read for anyone whose plan was flawless execution. If a rubric ever changed on you, when did you find out, and who told you? Clip credit: Silicon Valley Girl (Marina Mogilko) — full video on their channel. DM for credit or removal requests.

12h ago

---

---

## Google News: "ai"

**[In China, A.I. Is Moving Forward While the Economy Lags Behind](https://www.nytimes.com/2026/09/20/business/china-ai-economy.html)**

nytimes.com • 16h ago

---

**[Lawsuit says Anthropic, OpenAI, SpaceXAI and Google made illegal agreement on AI slowdown](https://www.cnn.com/2026/09/19/business/ai-slowdown-lawsuit-antitrust)**

A new lawsuit claims Anthropic, OpenAI, SpaceXAI and Google made an illegal deal to slow the pace of their respective AI development.

CNN • 1d ago

---

**[Nvidia CEO Jensen Huang emerges as Trump's top ally in AI safety debate](https://www.cnbc.com/2026/09/20/nvidia-ceo-jensen-huang-emerges-as-trumps-top-ally-in-ai-debate.html)**

Jensen Huang's position as the leader of the world's most valuable company, has earned him Trump's ear on the most important topics in AI.

CNBC • 14h ago

---

**[Nvidia's Jensen Huang rejects AI extinction warnings as "doomsday narratives"](https://www.cbsnews.com/news/jensen-huang-nvidia-rejects-ai-extinction-warnings/)**

Predictions that AI could destroy humanity in a few years are irresponsible and not based on science, Nvidia's co-founder told CBS News.

CBS News • 11h ago

---

**[Nvidia boss rejects AI extinction fears as 'doomsday narratives'](https://www.bbc.com/news/articles/cr5ye7p13jg7o)**

Jensen Huang's comments come after warnings from AI researchers that the technology could lead to human extinction.

BBC • 48m ago

---

**[AI is making spear phishing scams more successful, BYU research finds](https://www.ksl.com/article/51624838/ai-is-making-spear-phishing-scams-more-successful-byu-research-finds)**

As artificial intelligence grows ever stronger, new research from BYU shows people are more likely to be duped by AI-generated scams compared to human-written ones.

ksl.com • 1h ago

---

**[Congress is moving in the ‘right direction’ on AI: Sen Mike Rounds](https://www.foxnews.com/video/6405344849112)**

Sen. Mike Rounds, R-S.D., discusses the debate over artificial intelligence regulation, the U.S.-China AI race and the influence of socialists on the Democratic Party on ‘Life, Liberty & Levin.’

Fox News • 20m ago

---

**[Trump Calls A.I. Fears a Hoax. Inside the White House, the Debate Is More Complex.](https://www.nytimes.com/2026/09/18/us/politics/trump-ai-safety-anthropic-openai-china.html)**

nytimes.com • 2d ago

---

**[Anthropic billionaire cofounder who studied literature says non-STEM degrees will win in the AI age](https://fortune.com/article/anthropic-jack-clark-liberal-arts-degree-ai-jobs-stem-computer-science-philosophy-critical-thinking-future-of-work/)**

Anthropic’s liberal-arts-educated cofounder says “rote programming” is best avoided.

Fortune • 1d ago

---

**[Burned Out and Unemployed, Young People in China Are Launching AI Startups](https://www.wsj.com/business/entrepreneurship/burned-out-and-unemployed-young-people-in-china-are-launching-ai-startups-c5ebcdc3)**

WSJ • 3h ago

---

---

## HackerNews: "ai"

**[AI-generated posters don’t have to be horrible](https://news.ycombinator.com/item?id=49764791)**

The problem

⬆️ 1776 • 💬 912 • 1d ago • [‘ERE I AM - JH!](https://john.hartnup.uk/2026/06/07/ai-event-posters.html)

---

**[Microsoft exec called AI scraping 'the largest theft of labor in human history'](https://news.ycombinator.com/item?id=49752056)**

Newly unsealed court filings show Microsoft privately called OpenAI's data practices "theft" while both companies scraped paywalled Times content, built datasets from it, and warned internally it would gut publishers.

⬆️ 936 • 💬 825 • 2d ago • [TechCrunch](https://techcrunch.com/2026/09/17/microsoft-exec-called-ai-scraping-the-largest-theft-of-labor-in-human-history-new-unredacted-filings-reveal/)

---

**[US Military had close call after using AI for hallucinated intelligence report](https://news.ycombinator.com/item?id=49757520)**

The episode shows the risks of using this new, relatively poorly understood technology in the middle of the Iran war

⬆️ 511 • 💬 388 • 2d ago • [CNN](https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship)

---

**[I think you should almost never use AI to write](https://news.ycombinator.com/item?id=49767937)**

⬆️ 341 • 💬 165 • 1d ago • [erichgrunewald.substack.com](https://erichgrunewald.substack.com/p/why-you-should-almost-never-use-ai)

---

**[AI and the Destruction of the Creative Commons](https://news.ycombinator.com/item?id=49774329)**

⬆️ 223 • 💬 266 • 15h ago • [chesterwisniewski.com](https://www.chesterwisniewski.com/post/2026-09-13-ai-is-destroying-the-creative-commons/)

---

**[Microsoft director: AI scraping 'the largest theft of labor in human history'](https://news.ycombinator.com/item?id=49768921)**

The NYT argues that OpenAI and Microsoft infringed upon its copyright over thousands of news articles.

⬆️ 181 • 💬 49 • 1d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-director-called-ai-scraping-the-largest-theft-of-labor-in-human-history-while-openai-head-brands-chatgpt-an-existential-threat-to-publishers-revelations-come-from-legal-briefs-filed-in-nyt-lawsuit)

---

**[Alibaba open-sources AI model that can detect cancer and nearly 150 conditions](https://news.ycombinator.com/item?id=49761840)**

⬆️ 151 • 💬 23 • 2d ago • [scmp.com](https://www.scmp.com/tech/big-tech/article/3368055/alibaba-open-sources-medical-ai-model-can-detect-cancer-and-nearly-150-conditions)

---

**[AI chatbots are becoming experts at changing people's minds](https://news.ycombinator.com/item?id=49754250)**

⬆️ 135 • 💬 101 • 2d ago • [science.org](https://www.science.org/content/article/ai-chatbots-are-becoming-experts-changing-people-s-minds-what-s-their-secret)

---

**[AI is an elite crime spree](https://news.ycombinator.com/item?id=49755590)**

⬆️ 123 • 💬 42 • 2d ago • [thebignewsletter.com](https://www.thebignewsletter.com/p/ai-is-an-elite-crime-spree)

---

**[Can you tell which images are AI-generated?](https://news.ycombinator.com/item?id=49770847)**

Trust your eyes, build a streak, and beat your score in 60 seconds.

⬆️ 105 • 💬 78 • 1d ago • [Slop Sense](https://slop-sense.labtoagi.com/games/is-this-image-ai/)

---

---

## YouTube Videos: "ai"

**[Extended interview: Nvidia CEO Jensen Huang on fears about AI](https://www.youtube.com/watch?v=xCUala5j7aQ)**

In this web exclusive, Nvidia CEO Jensen Huang talks with CBS News' Jo Ling Kent about the exponential growth of AI, industry ...

📺 CBS Sunday Morning

👁️ 141K • 👍 2K • 💬 670 • ⏱️ 46:19 • 11h ago

---

**[FRANKENSTEIN WARNING: JD Vance drops STARK message on AI](https://www.youtube.com/watch?v=Brf5bR6c6yg)**

'The Big Money Show' panel debates AI regulation. Meta CEO Mark Zuckerberg and Vice President JD Vance push back on ...

📺 Fox Business

👁️ 34K • 👍 565 • 💬 254 • ⏱️ 13:33 • 9h ago

---

**[AI experts on doomsday fears: It&#39;s too late to stop the AI threat](https://www.youtube.com/watch?v=rvxfcmloDhU)**

The New York Times columnist Thomas Friedman tells CNN why it's already too late to stop the AI threat. Geoffrey Hinton, the ...

📺 CNN

👁️ 259K • 👍 1K • 💬 736 • ⏱️ 11:45 • 1d ago

---

**[Thomson Reuters Trained Custom AI LLM for $40 Million - OpenAI is DEAD](https://www.youtube.com/watch?v=_MZ8TAN_tH4)**

Spotify - https://open.spotify.com/show/1KkKuQe82tf1bW78ReQ0wM Apple Podcasts ...

📺 Eli the Computer Guy

👁️ 46K • 👍 885 • 💬 288 • ⏱️ 22:30 • 13h ago

---

**[The CHILLING Reason AI Researchers Are Quitting Their Jobs](https://www.youtube.com/watch?v=JYIkGljjnWY)**

Nate Soares, president of the Machine Intelligence Research Institute, joins the show to discuss the potential life-threatening ...

📺 The Young Turks

👁️ 99K • 👍 2K • 💬 944 • ⏱️ 24:35 • 9h ago

---

**[AI Is Outrunning Everyone’s Predictions - Noam Brown](https://www.youtube.com/watch?v=-OIQs3xe9-I)**

📺 Dwarkesh Patel

👁️ 63K • 👍 797 • 💬 103 • ⏱️ 0:39 • 2d ago

---

**[Every AI podcast be like 😳🤖😂 #shorts #funny #comedy #technology #artificialintelligence #ai](https://www.youtube.com/watch?v=7-51ClU_61Q)**

📺 Matt & Justus

👁️ 156K • 👍 15K • 💬 158 • ⏱️ 0:51 • 22h ago

---

**[The last IMO problem AI could not solve](https://www.youtube.com/watch?v=bRQEWPA832A)**

Full video: https://youtu.be/Nbwv5wHQoj0.

📺 3Blue1Brown

👁️ 402K • 👍 15K • 💬 190 • ⏱️ 1:40 • 2d ago

---

**[So Much AI News: New ChatGPT Tools, NotebookLM Updates, Big Claude Changes, Grok Bot Live, + More!](https://www.youtube.com/watch?v=SsHZaH2ml_U)**

Sponsored by Wispr Flow! Download Wispr Flow for free and use code LIPSKY on desktop to get 1 month of Wispr Flow Pro with ...

📺 Paul J Lipsky

👁️ 135K • 👍 2K • 💬 166 • ⏱️ 23:17 • 2d ago

---

**[AN AI SLOP AD CAME IN](https://www.youtube.com/watch?v=g26IngR8x1k)**

follow me on instagram if you wanna keep up :) https://instagram.com/h1t1.

📺 John Casterline

👁️ 2.1M • 👍 174K • 💬 1K • ⏱️ 1:17 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)**

*Prism ML*

Ternary-Bonsai-2-27B-gguf is a 27B parameter text generation model optimized for on-device inference using llama.cpp. It achieves ~98.2% of FP16 intelligence with a drastically reduced ~5.9 GB footprint by employing end-to-end ternary transformer weights (1.72 bits/weight), enabling efficient reasoning and long context (262K tokens) on consumer hardware with CUDA and Metal support.

`text-generation` `26.9B`

⬇️ 1,908,396 • ❤️ 1,499 • 3d ago

---

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 0 • ❤️ 1,105 • 23h ago

---

**[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

*DeepSeek*

DeepSeek-V4.1-Flash is a 552B multimodal MoE model supporting 1M token contexts, featuring a Causal Encoder-Decoder architecture with Compressed Sparse Attention 2 (CSA2) and FP4 KV caching for highly efficient KV cache compression. It excels in agentic workloads and offers controllable reasoning effort, processing both images and text.

`image-text-to-text` `763.2B`

⬇️ 496,684 • ❤️ 3,437 • 10d ago

---

**[Xing4.0-29B-A4B](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B)**

*XingChen-AGI*

Xing4.0-29B-A4B is a 29B parameter LLM with 4B active parameters, optimized for complex engineering tasks and agent-oriented architectures. It features a 256K context length (extensible to 512K) and supports multi-step planning and tool calling, making it suitable for domain-specific fine-tuning in areas like contract auditing and knowledge-based QA.

`text-generation` `31.2B`

⬇️ 12,617 • ❤️ 893 • 2d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 183 • ❤️ 773 • 15h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 7,331,932 • ❤️ 15,862 • 1mo ago

---

**[YuE2-3B](https://huggingface.co/m-a-p/YuE2-3B)**

*Multimodal Art Projection*

YuE2-3B is a text-to-audio model capable of generating high-quality music with vocals and accompaniment from lyrics and style prompts. It features editable score generation, agentic editing for iterative refinement, and can run locally on a 24GB GPU.

`text-to-audio` `3.6B`

⬇️ 17,403 • ❤️ 916 • 4d ago

---

**[Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**

* IST Austria Distributed Algorithms and Systems Lab*

This model provides GGUF quantizations of Qwen3.8-27B with a vision projector for multimodal tasks, utilizing GSQ and RCO for non-uniform, low-bit precision. It enables efficient deployment of multimodal large language models with minimal performance degradation.

`image-text-to-text` `26.9B`

⬇️ 1,217,204 • ❤️ 1,480 • 18d ago

---

**[Qwen-2.5-1B-RLCD](https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD)**

*Harsha Gundala*

Qwen-2.5-1B-RLCD is a text-generation model optimized for high-throughput structured information extraction on Apple Silicon using MLX. It achieves 5.6x-7.0x latency reductions with 100% schema validity by evaluating multi-field JSON schemas in parallel, ideal for tasks like fraud routing, code auditing, and support triage.

`text-generation`

⬇️ 0 • ❤️ 477 • 4d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,609,559 • ❤️ 4,556 • 19d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 141 • 💬 6 • ⭐ 107,779 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 175 • 💬 19 • ⭐ 67,425 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**

*Apodex Team, B. An, B. Li et al. (71 authors)*

🏢 Apodex

Apodex 1.1 improves sustained, verifiable progress on complex real-world tasks by scaling executable environments and training agents to coordinate long-horizon work with state maintenance and recovery.

▲ 208 • 💬 3 • ⭐ 4,188 • 28d ago

[🎓 arXiv](https://arxiv.org/abs/2608.23283) • [💻 code](https://github.com/ApodexAI/FrontierAgent) • [🔗 project](https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 77 • 💬 3 • ⭐ 9,923 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](https://huggingface.co/papers/2609.20519)**

*Haozhe Liu, Tian Ye, Sensen Gao et al. (14 authors)*

🏢 NVIDIA

As coding agents move from supervised code completion to unattended, around-the-clock exploration, their work expands from isolated predictions into long trajectories of reasoning, tool use, and feedback. Token efficiency therefore becomes important for scaling recursive self-improvement. We take an RSI-inspired approach at the harness layer, scaling auto-research loops across increasingly numerous and diverse environments for harness rollouts. At this scale, the process yields reusable improvements that transfer beyond their development setting, moving automated harness discovery toward production-level outcomes. Four mechanisms survive selection and form SoL-Pi, spanning action execution, context compaction, observation handling, and delegated reading. On the 51-task EdgeBench evaluation, SoL-Pi achieves performance comparable to Pi across GPT-5.6 Sol and Opus 5 while reducing recorded token traffic by 44.7-49.0% and API cost by about one third. In other words, estimated hourly savings are \8.75-13.50 relative to native Codex and Claude Code harnesses, and \4.36-5.71 relative to Pi.

▲ 94 • 💬 3 • ⭐ 2,656 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.20519) • [💻 code](https://github.com/NVlabs/SoL-Pi) • [🔗 project](https://nvlabs.github.io/SoL-Pi/)

---

**[Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://huggingface.co/papers/2609.14858)**

*Tong Zheng, Xidong Wu, Zheng Zhang et al. (17 authors)*

🏢 Google

Dream-RSI enables scalable recursive self-improvement by using historical discovery replay to evaluate exploration policies offline, reducing costly online evaluations.

▲ 238 • 💬 3 • ⭐ 970 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.14858) • [💻 code](https://github.com/zhengkid/Dream-RSI) • [🔗 project](https://dream-rsi.com/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 44 • 💬 1 • ⭐ 33,306 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 87 • 💬 7 • ⭐ 88,652 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Paper2Agent: Reimagining Research Papers As Interactive and Reliable AI
  Agents](https://huggingface.co/papers/2509.06917)**

*Jiacheng Miao, Joe R. Davis, Jonathan K. Pritchard et al. (4 authors)*

Paper2Agent converts research papers into interactive AI agents to facilitate knowledge dissemination and enable complex scientific queries through natural language.

▲ 45 • 💬 7 • ⭐ 3,178 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06917) • [💻 code](https://github.com/jmiao24/Paper2Agent) • [🔗 project](https://huggingface.co/spaces/Paper2Agent/alphagenome_agent)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 110 • 💬 2 • ⭐ 13,318 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

---

## GitHub Repositories: "ai"

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 2.7k • 🔱 106 • 50m ago

---

**[Nanako0129/sepia](https://github.com/Nanako0129/sepia)**

De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

`Python` `agent-skills` `ai-writing` `antigravity` `claude-code` `codex`

⭐ 2.7k • 🔱 182 • 3h ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 2.2k • 🔱 41 • 6h ago

---

**[amosblomqvist/learn](https://github.com/amosblomqvist/learn)**

My AI learning system.

`TypeScript`

⭐ 2.2k • 🔱 225 • 26d ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 1.6k • 🔱 131 • 16h ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 1.5k • 🔱 290 • 3d ago

---

**[adtexterry-lgtm/unigit-ecosystem](https://github.com/adtexterry-lgtm/unigit-ecosystem)**

UNIGIT public brand and ecosystem hub — AI should work for everyone.

`JavaScript` `agentic-ai` `ai-tools` `ai-workbench` `ecosystem` `mcp`

⭐ 1.3k • 🔱 45 • 18d ago

---

**[jtydhr88/screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills)**

Professional agent skills for screenwriting, television writing and dramaturgy

`Python` `ai` `skills`

⭐ 1.3k • 🔱 148 • 5d ago

---

**[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)**

An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些内容真正有效，覆盖小红书、抖音、知乎、哔哩哔哩等平台。

`Python` `agent` `agent-skill` `content-automation` `content-creation` `content-generation`

⭐ 1.3k • 🔱 183 • 13h ago

---

**[2akouwu/reverify](https://github.com/2akouwu/reverify)**

Stop your AI from making things up — it proposes, deterministic tools decide, every claim checked against ground truth with evidence. Grounded facts and context survive resets. Reverse engineering is the proving ground. MCP server + CLI.

`Python` `ai` `ai-agents` `ai-coding` `anti-hallucination` `binary-analysis`

⭐ 1.2k • 🔱 240 • 13d ago

---

---

*Generated by PeekDeck - A glance is all you need*
