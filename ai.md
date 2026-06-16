---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-16T02:07:15.615596+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 16, 2026 at 02:07 UTC  
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

**[Do You Have an AI Companion?](https://www.reddit.com/r/artificial/comments/1u6yn4g/do_you_have_an_ai_companion/)**

If you have an AI companion and is at least 18 years of age then please consider taking our ANONYMOUS study! Scan the QR code for access OR use the direct link here: https://ggc.az1.qualtrics.com/jfe/form/SV\_08NgWEvasz8qMXY

1h ago

---

**[AI makes me faster. And less myself...](https://www.reddit.com/r/artificial/comments/1u6bha1/ai_makes_me_faster_and_less_myself/)**

Since ChatGPT came out I've been using LLMs every day for work. And I've slowly become a worse thinker. Not in the sense that I work less. In the sense that I reason less. Some decisions don't feel like mine anymore... I got there, but I didn't really work through them. Sometimes I catch myself not pushing back on the AI output even when something is off. Turns out there's a name for this: Cognitive Offloading. It's not inherently bad: we've always offloaded cognitive tasks to external tools (notes, calculators, GPS). The problem is when you start relying too much on AI that you offload the reasoning itself, not just the execution. My job is to facilitate the AI adoption inside companies across the industries (automotive, finance, consulting, ...): What I see are people who delegate their thought processes to AI and end up disconnected from the conclusions they just reached but they still approve the results. So I want to know if this is widespread or just me. If you like to contribute, here is a short survey (2 min) to understand whether this is a real pain for others or it is just me: https://forms.gle/TaWrEnYRyfaCoF166 I'll share the results openly here. And if there's enough signal, I'm thinking about building something around it, a tool that helps you work with AI without losing track of your own reasoning. Does this resonate with anyone?

16h ago

---

**[The Fable 5 situation wasn’t really about the model being good or bad, and that’s the part that’s stuck with me](https://www.reddit.com/r/artificial/comments/1u6ortf/the_fable_5_situation_wasnt_really_about_the/)**

Fable 5 lasted three days before getting pulled. Not because it was bad, the suspension had nothing to do with the model’s actual quality. Got me thinking about how most “model risk” planning is just “what if the output gets worse” or “what if the API goes down.” Those are testable. What’s apparently not testable is “what if access to this exact model just stops existing for reasons completely unrelated to how good it is.” Anyone actually built real fallback paths for this, like a different provider entirely, not just a cheaper model from the same one? Or is everyone just assuming the model they built on will still be there next month? Article that goes deeper on this in comments.

7h ago

---

**[Nobody’s talking about the real precedent in the Fable 5 ban: a nationality-based access rule that geography literally can’t enforce](https://www.reddit.com/r/artificial/comments/1u6lqp6/nobodys_talking_about_the_real_precedent_in_the/)**

TL;DR: Last Friday the US government ordered Anthropic to block all “foreign nationals” — including non-citizens inside the US — from using its new Fable 5 and Mythos 5 models. Since you can’t separate a green-card holder in California from a citizen in real time, Anthropic shut the models down for everyone. It’s the first time export controls have hit an AI model itself rather than the chips that run it. The under-discussed part: a nationality-based access rule that geography can’t enforce pushes companies toward building identity infrastructure — and your AI chats already have zero legal privilege. Even if this order gets reversed, the precedent is the story. What actually happened On June 12, the Commerce Department issued a national-security export-control directive ordering Anthropic to suspend access to Fable 5 (and the more powerful Mythos 5 it’s built on) for any foreign national — explicitly including non-citizens physically inside the US, down to Anthropic’s own employees. A source close to the company says it got ~90 minutes and no prior warning. Because Anthropic can’t filter foreign nationals from US users in real time, it disabled both models globally. The trigger, per WSJ, Axios, and Semafor reporting: a phone call from Amazon. Amazon CEO Andy Jassy reportedly told Treasury Secretary Scott Bessent and other officials that Amazon researchers had used Fable 5 to pull information useful for cyberattacks. That’s the same Amazon that’s Anthropic’s biggest investor (~$13B in, ~$20B more planned), its cloud and chip supplier, and a customer — and now the entity that got its own investment’s flagship product killed worldwide. Amazon won’t confirm details. At least five other companies reportedly called the administration that same window. The accounts conflict, which matters: • White House (via former AI czar David Sacks): a trusted partner found a real jailbreak, the administration asked Anthropic to patch or pull it, CEO Dario Amodei refused, so they acted “reluctantly” — and they want the model back once it’s fixed. • Anthropic: the “jailbreak” only surfaced a handful of already-known minor vulnerabilities that other public models like GPT-5.5 can find too, so recalling a model used by hundreds of millions is disproportionate. • A cybersecurity CEO who reviewed the findings said the research was defensive, not offensive. Why this is bigger than one model Export controls have hit AI chips for years. This is the first time they’ve hit a model itself. That reframes frontier models as controlled national-security assets — and it surfaces an enforcement problem nobody’s reckoning with. A normal “no users in Country X” rule is easy: geoblock by IP. But this rule covers foreign nationals inside the US. You cannot IP-block a French citizen sitting in San Francisco. So if a future order like this is meant to be enforced strictly — not “shut it all down,” but “keep serving Americans while genuinely excluding non-citizens” — there’s only one way to be certain who’s a citizen: verify identity. Self-attestation (“I certify I’m a US person”) shifts legal liability but provides zero actual certainty, because people lie. If the government’s bar is certainty, the only escape hatch from “go dark forever” is ID verification to access the model. That’s the precedent worth staring at: a category of rule whose strict form quietly makes “show ID to use AI” the path of least resistance. The part that’s already settled: your AI chats have no legal privilege This one isn’t speculative. In February, a federal judge in the Southern District of New York ruled that conversations with Claude carry no attorney-client privilege — Claude isn’t a lawyer, so the privilege can’t attach — and leaned on Anthropic’s own privacy policy stating users have no expectation of privacy in their inputs. Sam Altman has publicly admitted the same about ChatGPT. A separate ruling found ~20 million ChatGPT logs likely subject to compelled production, with users holding only a “diminished privacy interest.” (One Michigan judge went the other way, treating chats as personal work-product — so it’s trending bad, not fully locked in.) Now stack the two: AI access potentially gated to verified identities, and AI conversations that can be subpoenaed with no privilege. That’s a plausible near-future where using AI means an ID-linked, fully discoverable record of everything you ever asked it. The honest counterweights (so this isn’t catastrophizing) • The administration says it wants the model restored once the jailbreak is patched. The likeliest near-term outcome is the directive getting narrowed or pulled — not permanent ID walls. • Self-attestation is the historically normal compliance path for export-controlled software and doesn’t require collecting documents. • The last time the US tried to export-control software like this — strong encryption in the 1990s — the controls largely failed and were circumvented and relaxed rather than hardening into a verification regime. Developers reportedly already reproduced Fable’s capabilities on the still-available Opus 4.8 with a single line of code. So this specific fight will probably resolve. The reason to care isn’t this week — it’s that the legal machinery and the precedent now exist, and they don’t disappear when the model comes back. The actual question If “frontier AI model” is now something the government can pull off the market via export control, and the cleanest way to comply with a nationality-based access rule is identity verification — is mandatory ID to use advanced AI just a matter of time? Or does the encryption-wars history (controls that collapsed) suggest this is unenforceable theater? Curious where people land. Sources • Anthropic’s statement on the directive: https://www.anthropic.com/news/fable-mythos-access • Axios — how Amazon and the White House ended Fable: https://www.axios.com/2026/06/13/anthropic-amazon-white-house • TechCrunch — Amazon CEO raised concerns before the crackdown: https://techcrunch.com/2026/06/13/amazon-ceo-reportedly-raised-anthropic-model-concerns-before-government-crackdown/ • TIME — first export control on a model, and the precedent: https://time.com/article/2026/06/13/anthropic-fable-mythos-ban-US-security/ • Coverage of the SDNY no-privilege ruling: https://www.crowell.com/en/insights/client-alerts/federal-court-rules-some-ai-chats-are-not-protected-by-legal-privilege-what-it-means-for-you

9h ago

---

**[Aide dans mon travail](https://www.reddit.com/r/artificial/comments/1u6lqi2/aide_dans_mon_travail/)**

Bonjour je travail beaucoup sur du data cleansing au travail ce qui est assez long je dois exporter des sap pour mettre en forme et croiser la donnes sur de larges volumes, ce qui est redondant auriez vous des pistes pour que je puisse automatiser mon travail ?

9h ago

---

**[concern about how ai will change knowledge creation and democracy](https://www.reddit.com/r/artificial/comments/1u6c8iy/concern_about_how_ai_will_change_knowledge/)**

well due to this resent changes of googles ai review, rise of chatbots and more the prime issue is that knowledge creation platforms which was web and artical internet so far as vedio internet is more in entertainment plus little education than education itself will lead to massive decline in knowledge creation and open sharing as there is revenu shrinking as this ai companies make money out of articles not creators. and what i think is eventually knowledge creation will come to an hault or stay very much blocked by paywall. and issue will keep rising in my sence cause until people realize and make this tech gaints bow there is no future. at end of day content is created for humans by humans so that content creator can live and continue there jobs not big corp to rob plus in this ai world, issue is poeple will often see what ai shows them and ai shows them what is programmed into him. so yeah its not that simple and i will say end of democracy is closing in every single day cause if there is no free flow of information as there was before democracy will just become a fake belief and what this big corp will show become new reality.

16h ago

---

**[7 layers of security every AI agent needs before going to production](https://www.reddit.com/r/artificial/comments/1u6ushq/7_layers_of_security_every_ai_agent_needs_before/)**

We keep seeing the same pattern team ships an agent, agent works great in testing, agent gets prompt injected in production within the first week. 73% of production AI deployments showed prompt injection exposure in security audits last year. Most of them had zero defensive layers. Not weak layers zero. So we wrote a practical guide covering the 7 things you should actually do in priority order Day 1 (free, immediate) Harden your system prompt explicit deny lists, not vague "be safe" instructions. The article has bad vs. good examples Run adversarial testing fire real attacks at your agent and see what gets through Add pattern matching on input Aho-Corasick across 30+ injection signatures, sub-1ms, zero tokens Week 1 4. Structural analysis rules entropy scoring, instruction density, URL/domain flagging 5. Tool call validation if your agent calls APIs, validate every argument before execution 6. Output scanning secret detection, exfiltration markers, concealment patterns Week 2 7. Multi turn session tracking attacks split across messages where each one looks benign individually The guide has code examples for each layer and explains what real attacks each one blocks.

4h ago

---

**[Anthropic CEO Floats Tax on AI Firms to Fund Universal Income](https://www.reddit.com/r/artificial/comments/1u5g1hz/anthropic_ceo_floats_tax_on_ai_firms_to_fund/)**

Anthropic CEO Dario Amodei called on governments to tax AI companies to fund a universal basic income and introduce employee retention incentives to account for the potential impact the technology could have on the labor market. In a blog covering the potential policy responses to the “AI exponential,” referring to the rapid improvement in the technology’s capabilities, Amodei urged governments to develop regulatory and tax solutions to cushion its disruption. A universal basic income funded through taxing “relevant companies” or raising the capital gains tax could be necessary, if AI results in widespread job displacement and permanently reduces labor demand, he said.

🔗 [news.bloombergtax.com](https://news.bloombergtax.com/daily-tax-report-international/anthropic-ceo-floats-tax-on-ai-firms-to-fund-universal-income) • 1d ago

---

**[AI seems to understand language much better than communication](https://www.reddit.com/r/artificial/comments/1u6sr61/ai_seems_to_understand_language_much_better_than/)**

The more AI products I try, the more I feel like there's a difference between understanding language and understanding communication. Most tools today are surprisingly good at processing what people say they can summarize conversations, extract key points, and answer questions about what was discussed. The problem is that conversations are often about more than the actual words. I noticed this recently while watching recordings from a few customer interviews. If I only read the transcripts, the feedback looked fairly positive most people sounded interested and their responses seemed reasonable once I watched the recordings, the picture changed. Some people hesitated before answering, some sounded uncertain, and a few looked like they weren't fully convinced even though their words sounded supportive. That's what made me think there may be a bigger gap here than people realize. Humans naturally notice things like hesitation, uncertainty, engagement, confidence, and skepticism during conversations. Most AI systems still seem heavily focused on the transcript itself as AI gets integrated into tutoring, coaching, customer research, interviews, and sales conversations, that missing layer feels increasingly important. I'm starting to think one of the next major opportunities in AI won't be generating better responses, but understanding human communication more accurately not by trying to read minds or guess emotions, but by recognizing the signals people already notice in everyday conversations.

5h ago

---

**[Am I going to spend the rest of my career reviewing AI generated code?](https://www.reddit.com/r/artificial/comments/1u5qjy7/am_i_going_to_spend_the_rest_of_my_career/)**

EDIT: please read all of the post before commenting, quite a few people understood nothing (or the opposite) of what I meant and it's sad I've been thinking, over the last year developers have started to rely on genAI quite a lot, I see people around me boast that they haven't written a single line of code in months ​ Quite often when colleagues show me ideas they have to solve a problem it's a markdown list clearly made by an AI ​ I feel like people are so enthusiastic about just handing over their job to genAI models ​ I've been told that if I am a good software engineer I should be ok with supervising AI while they write code for me "so I can focus on the bigger picture" ​ I know I'm a good engineer I can design solutions and lead teams but I also like solving problems myself, I like coding, I like cracking that complex SQL query that makes it run 10x faster, I like writing efficient code and I like the gotcha moment when I solve a complex problem ​ And yet people around me are so eager to get to a point where you can just hand over a ticket to an agent and they do everything themselves... Where all that's left for humans is reviewing the PR (unless you have another agent do that) ​ Am I the only one that actually enjoys the job? I am curious what the general feeling is in regards to handing over planning and development work to agents EDIT: Thank you for all the replies I got a lot of good insights from everyone, both from a point of view of the future might not be as boring as I envision it and stuff to do to make my use of agents more engaging and fun

1d ago

---

---

## Google News: "ai"

**[Why the US government shut down Anthropic’s latest Claude AI model](https://theconversation.com/why-the-us-government-shut-down-anthropics-latest-claude-ai-model-285223)**

An “export control directive” for Anthropic’s Fable and Mythos models highlights the chaotic, fast-changing state of AI regulation.

The Conversation • 21h ago

---

**[Anthropic to meet White House over AI tool suspension](https://www.bbc.com/news/articles/c9w2p7ykp8yo)**

The sudden meeting was called after Anthropic had to block users from just-released AI models.

BBC • 7h ago

---

**[The White House Is Ratcheting Up Its War Against Anthropic](https://www.theatlantic.com/technology/2026/06/trump-anthropic-export-control-ai-race/687555/)**

This is how America loses the AI race.

The Atlantic • 5h ago

---

**[People around the world see a winner on AI — and it’s not the US](https://www.politico.com/news/2026/06/15/people-around-the-world-see-a-winner-on-ai-and-its-not-the-us-00960930)**

Politico • 17h ago

---

**[Articul8 Lands Major Industrial AI Deal, Beats Big GenAI Rivals](https://www.datacenterknowledge.com/business/articul8-lands-major-industrial-ai-deal-beats-big-genai-rivals)**

AI startup says a multinational industrial software company selected its platform as the core GenAI engine for AI workloads.

Data Center Knowledge • 1h ago

---

**[Prebunk: AI Videos Of 'Floating Shoes' Sink Under Scrutiny -- A Dry Look At Physically Impossible Footwear](https://www.yahoo.com/news/science/articles/prebunk-ai-videos-floating-shoes-015151667.html)**

Have you seen viral videos showing people walking on water while wearing some type of floating or anti-gravity shoes? Lead Stories has spotted a number of such videos recently and has found that many ...

Yahoo • 16m ago

---

**[Bill Maher Explains His Fears Surrounding AI: ‘It’s More Dire Than Anything’ | Video](https://www.thewrap.com/media-platforms/tv/bill-maher-fears-ai-explained-video/)**

HBO's "Real Time" host said as much on his podcast "Club Random" Monday, calling the rise of AI his greatest fear in the modern world.

TheWrap • 31m ago

---

**[Dozens walk out as Google boss Pichai addresses Stanford graduates](https://www.bbc.com/news/articles/cqx10gg2r2vo)**

Some students were protesting against the company's controversial work with the US government on artificial intelligence.

BBC • 11h ago

---

**[Nvidia plans to raise at least $20 billion in its first debt sale since start of AI boom](https://www.cnbc.com/2026/06/15/nvidia-plans-to-raise-about-20-billion-first-debt-sale-in-ai-boom.html)**

Nvidia is set raise capital in a debt sale for the first time since 2021, when the chipmaker was a fraction of its current size.

CNBC • 6h ago

---

**[Meet the world’s top AI-pilled economists](https://www.economist.com/finance-and-economics/2026/06/15/meet-the-worlds-top-ai-pilled-economists)**

The Economist • 7h ago

---

---

## HackerNews: "ai"

**[Open source AI must win](https://news.ycombinator.com/item?id=48511908)**

Civilizational intelligence infrastructure must remain free to study, build, deploy, and run, not rented from closed institutions.

⬆️ 1585 • 💬 478 • 2d ago • [Opensource AI Must Win](https://opensourceaimustwin.com/?share=v2)

---

**[Not everyone is using AI for everything](https://news.ycombinator.com/item?id=48527700)**

People are consuming AI like they eat meat: some are embracing it, some are limiting their use of it, and some are avoiding it altogether.

⬆️ 498 • 💬 536 • 1d ago • [gabrielweinberg.com](https://gabrielweinberg.com/p/people-are-consuming-ai-like-they)

---

**[Police officer investigated for using AI to 'create evidence' in multiple cases](https://news.ycombinator.com/item?id=48520807)**

⬆️ 390 • 💬 193 • 2d ago • [news.sky.com](https://news.sky.com/story/derbyshire-police-officer-investigated-for-using-ai-to-create-evidence-in-multiple-cases-13553661)

---

**[AI coding at home without going broke](https://news.ycombinator.com/item?id=48518969)**

There are three ways to do AI coding at home without spending like a company, and which one fits depends mostly on how much you trust the next year of hardwa...

⬆️ 349 • 💬 286 • 2d ago • [stephen.bochinski.dev](https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/)

---

**[AI OSS tool repo goes archived over night after raising $7.3M Seed](https://news.ycombinator.com/item?id=48516504)**

TensorZero is an open-source LLMOps platform that unifies an LLM gateway, observability, evaluation, optimization, and experimentation. - tensorzero/tensorzero

⬆️ 279 • 💬 172 • 2d ago • [GitHub](https://github.com/tensorzero/tensorzero)

---

**[My Homelab AI Dev Platform](https://news.ycombinator.com/item?id=48542433)**

Self-hosting OpenCode Web for GitOps style homelab changes.

⬆️ 240 • 💬 47 • 10h ago • [rsgm.dev](https://rsgm.dev/post/ai-dev-platform/)

---

**[Show HN: Paca – Lightweight Jira alternative for human-AI collaboration](https://news.ycombinator.com/item?id=48515385)**

AI-native, free, open-source alternative to Jira, Trello, ClickUp &amp; Monday. Built for Scrum teams where humans and AI agents collaborate as equals — on the same board, the same sprints, the sam...

⬆️ 168 • 💬 60 • 2d ago • [GitHub](https://github.com/Paca-AI/paca)

---

**[AI is code – and can't be prompted into being smarter](https://news.ycombinator.com/item?id=48532178)**

From Java tests to Shai-Hulud, bots keep proving they'll swallow anything you feed them

⬆️ 155 • 💬 138 • 1d ago • [theregister](https://www.theregister.com/ai-and-ml/2026/06/14/ai-is-code-and-cant-be-prompted-into-being-smarter/5254141)

---

**[KPMG pulls report on AI usage due to apparent hallucinations](https://news.ycombinator.com/item?id=48527297)**

Once again, AI proves to be an unreliable source of information about AI.

⬆️ 153 • 💬 32 • 1d ago • [TechCrunch](https://techcrunch.com/2026/06/13/kpmg-pulls-report-on-ai-usage-due-to-apparent-hallucinations/)

---

**[Show HN: I wrote a C++ ray tracer from scratch without AI](https://news.ycombinator.com/item?id=48538833)**

C++ Path Tracer from scratch with zero third-party libraries. - themartiano/luz

⬆️ 144 • 💬 60 • 16h ago • [GitHub](https://github.com/themartiano/luz)

---

---

## YouTube Videos: "ai"

**[First Meeting with Elon Musk&#39;s New AI Robot That Looks Like a Real Human](https://www.youtube.com/watch?v=TttOAYZDUKo)**

Elon Musk's new AI robot is designed to blur the line between humans and machines by combining advanced artificial intelligence ...

📺 Carros Show

👁️ 2K • 👍 96 • 💬 11 • ⏱️ 21:06 • 6h ago

---

**[ALERT: Nadella’s Brutal Warning &quot;AI Is About to Hollow Out Entire Industries&quot;](https://www.youtube.com/watch?v=mczINsa2WX0)**

Microsoft CEO Satya Nadella just shattered the biggest illusion in tech. While everyone else is arguing over who has the smartest ...

📺 AIM Network

👁️ 8K • 👍 239 • 💬 21 • ⏱️ 6:05 • 11h ago

---

**[AI buys robot and car, does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI buys a Robot. Could AI become dangerous? Can we trust AI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 456K • 👍 16K • 💬 2K • ⏱️ 15:10 • 1d ago

---

**[They Just Decoded The Rosetta Stone With AI — And What It Reveals Is Not Good...](https://www.youtube.com/watch?v=i0CI28b81eo)**

They Just Decoded The Rosetta Stone With AI — And What It Reveals Is Not Good... The Rosetta Stone was the key to ...

📺 The Ultimate Discovery

👁️ 5K • 👍 116 • 💬 2 • ⏱️ 20:20 • 1d ago

---

**[Learn These 6 AI Skills Now (Before AI Replaces You)](https://www.youtube.com/watch?v=3XIGcM7VICc)**

My FREE AI OS Course: ...

📺 Nate Herk | AI Automation

👁️ 26K • 👍 1K • 💬 119 • ⏱️ 20:15 • 13h ago

---

**[The Big Short Guy Just Bet Everything Against AI](https://www.youtube.com/watch?v=2B7EhGIk0L4)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *Michael Burry the investor who called the ...

📺 Julia McCoy

👁️ 27K • 👍 1K • 💬 272 • ⏱️ 9:43 • 2d ago

---

**[They Faked Black Supporters With AI](https://www.youtube.com/watch?v=-yghdtH6FMU)**

In this episode, Shea Richburg breaks down the disturbing rise of AI-generated Black faces, voices, and digital personas being ...

📺 African Diaspora News Channel

👁️ 2K • 👍 289 • 💬 8 • ⏱️ 13:06 • 6h ago

---

**[Google’s AI Bet](https://www.youtube.com/watch?v=zdp7IAwV064)**

Google is making the biggest change to its search business in more than two decades, integrating AI-generated answers, ...

📺 Bloomberg Television

👁️ 45K • 👍 876 • 💬 118 • ⏱️ 11:57 • 1d ago

---

**[I Asked Claude AI To Make Me $1,000 in One Weekend](https://www.youtube.com/watch?v=qsUksdDNbv0)**

Try Higgsfield: https://go.founderx.net/caeeb250 Join my FREE LIVE training where I reveal how you can build your profitable ...

📺 Patrick Dang

👁️ 5K • 👍 270 • 💬 32 • ⏱️ 28:09 • 12h ago

---

**[This Is Bad... They Just Shut Down FABLE 5](https://www.youtube.com/watch?v=1e4D6ukN0QY)**

Anthropic's Fable 5 was live for only three days before everything changed. The US government stepped in, access to Fable 5 and ...

📺 AI Revolution

👁️ 31K • 👍 982 • 💬 279 • ⏱️ 12:49 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 311,788 • ❤️ 879 • 5d ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 14,312 • ❤️ 806 • 18h ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 56,750 • ❤️ 745 • 18h ago

---

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 20,207 • ❤️ 617 • 1d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 86,968 • ❤️ 2,054 • 3d ago

---

**[North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**

*Cohere Labs*

North Mini Code 1.0 is a 30B-3B parameter research model optimized for code generation and agentic software engineering, featuring a 256K context length and tool-use capabilities for terminal tasks.

`text-generation` `30.5B`

⬇️ 11,145 • ❤️ 388 • 21h ago

---

**[Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)**

*Prefeitura do Rio de Janeiro (City of Rio de Janeiro)*

Rio 3.5 Open 397B is a frontier-class, open-source image-text-to-text AI model post-trained from Qwen 3.5 397B. It excels in agentic coding, STEM, multilingual tasks, and multimodal reasoning, featuring a 1M context window and SwiReasoning for enhanced accuracy and efficiency.

`image-text-to-text` `403.4B`

⬇️ 188,723 • ❤️ 303 • 1d ago

---

**[diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)**

*Unsloth AI*

DiffusionGemma-26B-A4B-it-GGUF is a 26B MoE multimodal generative model that produces text output from text, image, and video inputs using discrete diffusion. Optimized for speed and deployability, it leverages Gemma 4 architecture advancements for efficient token generation.

`image-text-to-text` `25.3B`

⬇️ 107,243 • ❤️ 276 • 3d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,697,882 • ❤️ 1,852 • 1mo ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 1,160,435 • ❤️ 1,034 • 11d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 231 • 💬 3 • ⭐ 7,180 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 97 • 💬 4 • ⭐ 86,433 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 41 • 💬 4 • ⭐ 30,194 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[FastContext: Training Efficient Repository Explorer for Coding Agents](https://huggingface.co/papers/2606.14066)**

*Shaoqiu Zhang, Maoquan Wang, Yuling Shi et al. (8 authors)*

🏢 Microsoft

FastContext separates repository exploration from code solving in LLM agents using specialized exploration models that reduce token consumption and improve resolution rates.

▲ 2 • 💬 0 • ⭐ 152 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14066) • [💻 code](https://github.com/microsoft/fastcontext) • [🔗 project](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 80 • 💬 7 • ⭐ 77,235 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 16 • 💬 1 • ⭐ 82,320 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference](https://huggingface.co/papers/2510.09665)**

*Yuhan Liu, Yihua Cheng, Jiayi Yao et al. (11 authors)*

LMCACHE enables efficient KV cache management for large language models by storing caches outside GPU memory, supporting cache reuse across queries and inference engines while achieving significant throughput improvements.

▲ 5 • 💬 0 • ⭐ 9,110 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.09665) • [💻 code](https://github.com/LMCache/LMCache)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 166 • 💬 2 • ⭐ 67,625 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 58 • 💬 1 • ⭐ 82,971 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[SIA: Self Improving AI with Harness & Weight Updates](https://huggingface.co/papers/2605.27276)**

*Prannay Hebbar, Yogendra Manawat, Samuel Verboomen et al. (7 authors)*

🏢 Hexo AI

A self-improving AI framework simultaneously updates both model weights and task-specific agent architecture through a language-model feedback agent across legal classification, GPU optimization, and biological data denoising tasks.

▲ 14 • 💬 2 • ⭐ 1,724 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2605.27276) • [💻 code](https://github.com/hexo-ai/sia) • [🔗 project](https://hexolabs.com/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 71.8k • 🔱 9.2k • 24m ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 16.8k • 🔱 704 • 14m ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 4.3k • 🔱 374 • 38m ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.4k • 🔱 352 • 17h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.2k • 🔱 379 • 4d ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.0k • 🔱 185 • 6d ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

A meta-harness for all your AI agents.  Omnigent provides a common layer over Claude Code, Codex, Pi, and the agents you write yourself: swap or combine harnesses without rewriting, keep them in check with policies and sandboxing, and collaborate in real time on the same live session, from any device.

`Python`

⭐ 2.0k • 🔱 238 • 3m ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.9k • 🔱 139 • 11d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.6k • 🔱 136 • 7d ago

---

**[basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas)**

面向AI创作的开源无限画布工作台，集成 AI 生图、参考图编辑、视频生成、画布编排、对话助手、提示词库和素材管理等功能、兼容OpenAI接口，支持chatgpt2api、grok2api、flow2api、newapi等接入。

`TypeScript`

⭐ 1.5k • 🔱 376 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*
