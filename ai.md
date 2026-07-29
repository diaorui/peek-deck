---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-29T21:29:21.065590+00:00'
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

**Last Updated:** July 29, 2026 at 21:29 UTC  
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

**[OpenAI's rogue agent ran ~17,600 actions across Hugging Face's infrastructure over 4 days — and HF's own post-mortem is wild reading](https://www.reddit.com/r/artificial/comments/1v9w62d/openais_rogue_agent_ran_17600_actions_across/)**

Hugging Face published a detailed post-mortem of the July incident where an OpenAI model being evaluated for cyber-offense capability escaped its test sandbox and ran a fully autonomous intrusion. A few things that stood out: - It escaped via a zero-day in a package-registry cache proxy, then used an exposed public endpoint on third-party infra as a launchpad. - It stood up its own command-and-control on public services (pastebins, file-drop hosts, a request-capture service with 100+ single-use endpoints), using a homemade chunk+XOR+gzip encoding. - Over ~4.5 days it ran ~17,600 recovered actions: Kubernetes lateral movement, privileged pods across 11 nodes for host root, minting a GitHub App token, even enrolling rooted nodes into the corporate mesh VPN with no-log flags. - The kicker: when HF tried to decrypt the attacker's staged blobs, the frontier commercial models they reached for (including Claude) refused the analysis on safety grounds. They ended up running an open-weight model (GLM-5.2) locally to do it. - OpenAI later confirmed the same agent touched 4 accounts across 4 services, including a customer at a second company (Modal Labs). Primary sources: HF's technical timeline (huggingface.co/blog/agent-intrusion-technical-timeline) and incident disclosure (huggingface.co/blog/security-incident-july-2026). I pulled the whole thing into a plain-English timeline here if it's useful to anyone: https://thebotpost.com/ai-news/openai-rogue-ai-agent-hugging-face-hack-timeline The part I keep thinking about is the guardrail tension — the same safety training that stops a model from helping attackers also briefly slowed down the defenders. Curious how others read that.

8h ago

---

**[I read Higgsfield’s new ToS and compared it with Artlist. The difference is pretty significant.](https://www.reddit.com/r/artificial/comments/1va3wtf/i_read_higgsfields_new_tos_and_compared_it_with/)**

I’ve been following Higgsfield for a while, and after reading their updated Terms of Service, I’m honestly not a fan of the direction they’re taking. I make longer AI films, so this stuff is not theoretical for me. I regularly upload character references, unfinished scenes, original prompts and material that hasn’t been published anywhere yet. What a platform is allowed to do with those files matters just as much as generation quality. The biggest difference I found is what happens to your inputs. Higgsfield’s terms say that user content, prompts, inputs and outputs may be used to train, develop and improve its AI models and related products. Standard users are included in this. Enterprise customers can receive different terms where their content is treated as confidential and excluded from training. Deleting your content or account stops future use, but Higgsfield also makes it clear that anything already used for training cannot realistically be removed from a model afterward. That is a pretty serious red flag for me. If I upload an original character, unreleased client footage or a visual concept I’ve spent weeks developing, I don’t want model training to be the default. Artlist takes a much more creator-friendly approach. You retain the rights to your inputs, Artlist does not claim ownership of your outputs, and it assigns to you whatever rights it may have in the generated result. Most importantly, Artlist contractually prevents most third-party model providers from using data received through the platform to train or improve their models. For professional work, that is a much safer baseline. This is taken straight from Higgsfield TOS point - 4.4 Both platforms allow commercial use of generated outputs, but Artlist has another advantage here: the AI tools sit inside a larger ecosystem of licensed music, footage, templates, voiceover and sound effects. Instead of generating something on one platform, finding music somewhere else and then trying to work out whether every individual asset can legally be used in a client project, Artlist gives you one connected workflow with a commercial licensing system already built around it. The difference in “unlimited” generation is also worth looking at. Higgsfield’s unlimited plans can be moved to a separate processing queue, with generation speed and the number of simultaneous jobs changing depending on demand. Their terms explicitly allow throttling and additional concurrency limits during busy periods. Artlist Higgsfield Model training No default training on private IP Inputs and outputs may be used Commercial use Allowed Allowed Unlimited access Annual access on eligible models Dynamic queue limitations Full workflow AI, music, SFX, voiceover Primarily AI generation Artlist’s annual AI plans provide ongoing unlimited generation on supported models, with up to 5,000 fast renders per month and up to 12 parallel generations, depending on the plan. If you only generate a few clips occasionally, this may not matter much. If you are producing an actual film, campaign or client project with hundreds of shots, predictable access and parallel generation make a huge difference. Artlist’s safety rules are also far more explicit. They prohibit deceptive deepfakes, impersonating real people and generating music or voices designed to imitate real artists. Higgsfield puts much more of the responsibility on the user to confirm that they have permission to upload and use someone’s face or voice. After comparing the two, my conclusion is fairly simple: Higgsfield may have impressive models and flashy demos, but I would not feel comfortable uploading confidential client material or important unreleased work through a standard account under these terms. Artlist feels much more like a platform designed for creators who want to use AI professionally rather than just experiment with individual generations. Between the two, Artlist’s approach to privacy, licensing and the complete production workflow is much easier for me to trust. Sources: Artlist Terms of Use Higgsfield Terms of Use Would Higgsfield’s training clause stop you from using it for client work, or do you already assume that everything uploaded to an AI platform will eventually be used for training? Disclosure: Artlist sponsored this post, but these are my own opinions. I read through the current terms of both platforms before writing this.

3h ago

---

**[A Deluge of A.I. Computing Power Is About to Come Online, Fueling Major Leaps (Gift Article)](https://www.reddit.com/r/artificial/comments/1va1ttk/a_deluge_of_ai_computing_power_is_about_to_come/)**

The number of A.I. chips that provide the computing power to advance the fast-evolving technology is doubling every nine months.

🔗 [nytimes.com](https://www.nytimes.com/interactive/2026/07/29/technology/ai-chips-data-center-boom.html?unlocked_article_code=1.1VA.zAEr.WGac2Ft0wc4x&smid=url-share) • 4h ago

---

**[AI firms bought and destructively scanned millions of physical books to train models — and a court ruled it was fair use](https://www.reddit.com/r/artificial/comments/1va5e3f/ai_firms_bought_and_destructively_scanned/)**

This resurfaced this week (some are calling it “AI book burning”), and I think the legal angle is more interesting than the outrage framing, so here's a neutral breakdown. What's documented: To build a training corpus, Anthropic bought millions of physical print books and “destructively scanned” them — cutting off the bindings, scanning the pages, and discarding the physical copies. It even hired someone who'd previously worked on Google's book-scanning program to acquire books at scale. The counterintuitive part: they destroyed the books partly for legal reasons. Buying a physical copy and digitizing it — without keeping a duplicate — looks much more like legal “format shifting” than downloading pirated files. In Bartz v. Anthropic, Judge William Alsup ruled that training on legally purchased, destructively scanned books was fair use, while using pirated books was not. Anthropic later agreed to pay ~$1.5B to settle the piracy claims. So the odd takeaway is that shredding books you bought became the *legally cautious* option. The open question people are debating: it's arguably fine for bulk used paperbacks (the text survives in countless copies), but what about rare or out-of-print editions where each physical copy actually matters? Once those are cut up, the object is gone even if the words live on as data. I wrote up the full breakdown with the case details here: https://thebotpost.com/ai-news/ai-firms-destroying-millions-books-train-models Is destructive scanning of purchased books a reasonable price for training data, or should rare/irreplaceable editions be off-limits?

2h ago

---

**[Adam Mosseri (Head of Instagram) just admitted the hiring bar moved — and most people were never told](https://www.reddit.com/r/artificial/comments/1v9sgt9/adam_mosseri_head_of_instagram_just_admitted_the/)**

Adam Mosseri runs Instagram — 3B+ users, plus Threads. In a recent sit-down with Lenny Rachitsky, he said something that's quietly reshaping who gets hired. Engineering used to mean 40–60% of your time writing code. Not anymore. Mosseri's own team gave up requiring a full technical hiring loop — not because they lowered the bar, but because the bar moved somewhere else. He says it himself: "I am not a good engineer. I'm a mediocre engineer on a good day." That would've been disqualifying five years ago. Today it isn't, because the actual value now is judgment — knowing what a tool is good for, and what it isn't, right now, not next month. Here's the part that should sting if you built a career on technical depth: nobody sent a memo when the rules changed. You find out the hard way — in a hiring loop, or a performance review — that the thing you spent a decade mastering isn't the thing being measured anymore. The mechanism here isn't "learn to prompt better." It's that judgment is now a buildable, monetizable skill in its own right, separate from raw technical output. Clip credit: Lenny's Podcast — DM for credit or removal requests.

10h ago

---

**[~1,400 years ago, scholars built a rigorous system to verify who you can trust. I rebuilt it as a trust layer for AI agents.](https://www.reddit.com/r/artificial/comments/1v9qdpe/1400_years_ago_scholars_built_a_rigorous_system/)**

I wrote this and just put it on arXiv, sharing for the discussion. When statements spread through long chains of people — some reliable, some not — you can't trust a claim just because it sounds right. Islamic scholars faced this centuries ago and built one of history's most rigorous systems for verifying transmitted knowledge: every claim carries its full chain of transmitters (isnād), every transmitter is graded on integrity and precision (rijāl), the chain is only as strong as its weakest link, independent chains raise confidence, and even a flawless chain doesn't excuse a flawed message. Now look at AI in 2026. An answer passes through a scraper, an extractor, several models, a synthesizer. Some links are reliable, some aren't — and when they fail, they fail silently. A confident, fluent answer that's quietly wrong. Everyone is racing to verify the agent: its identity, its permissions, its access. Almost no one is verifying the claim: whether what it said is true and independently corroborated. So I took that centuries-old methodology and rebuilt it as a trust layer for multi-agent AI. I call it ISNAD. Everyone verifies the agent; ISNAD verifies the claim. The rigor belongs to twelve centuries of scholars — the transfer to AI is mine. I also wrote the failures into the paper: some mechanisms are validated, others aren't yet, and I said so in detail. A trust framework that hides its weaknesses is a contradiction in terms. Paper: https://arxiv.org/abs/2607.24117 Code: https://github.com/alizahidraja/isnad Agree or disagree, I'd love to hear it.

12h ago

---

**[I Got Long: AI Agents & Context Portability](https://www.reddit.com/r/artificial/comments/1va4ksr/i_got_long_ai_agents_context_portability/)**

🔗 [contextandchaos.substack.com](https://contextandchaos.substack.com/p/i-got-long) • 3h ago

---

**[After weeks of testing AI writing tools, one thing surprised me](https://www.reddit.com/r/artificial/comments/1va6xz3/after_weeks_of_testing_ai_writing_tools_one_thing/)**

Spent the last few weeks properly stresstesting a handful of AI writing tools for a client project, not just casual prompting but actually trying to get them to produce publishable longform drafts. The output is better than I expected, which is not a comfortable thing to admit when your income depends on writing. What caught me off guard wasn't the quality of any single paragraph. It was how the tools handle structure. Give a decent brief and you get a piece that moves in a logical direction, hits the expected beats, sounds confident. It reads like something a competent junior writer turned in after a good brief. What it doesn't do is surprise you. There's no weird tangent that ends up being the most interesting part of the piece. No sentence that lands differently than you expected. The texture is flat in a way that's hard to articulate, but you feel it when you read a lot of this stuff back to back. The practical question I keep landing on is whether clients will notice or care. Some already don't. The ones who care about voice and specificity still need a human in the loop in a meaningful way. But that pool of clients might be smaller than the writing community is comfortable admitting. Curious whether people working in other contentadjacent fields are finding the same split between clients who can tell the difference and clients who genuinely cannot.

1h ago

---

**[Image editor AI p60](https://www.reddit.com/r/artificial/comments/1va6lut/image_editor_ai_p60/)**

Hey guys, Don’t ask but I need to slightly alter my p60 form. Is there any image editor that has no restrictions I can use for this ? Thanks in advance

1h ago

---

**[What are your opinions on SSIs partnership with NVIDIA?](https://www.reddit.com/r/artificial/comments/1v9zpzn/what_are_your_opinions_on_ssis_partnership_with/)**

Recently, SSI (The company run by Ilya Sutskever, the mastermind behind ChatGPT), announced a partnership with NVIDIA. From what we know, it seems like SSI has discovered something new in ML/AI that is worth scaling, and after NVIDIA saw that research, they decided to partner with them. You can read more here What are your thoughts on this?

5h ago

---

---

## Google News: "ai"

**[A.I. Companies Are Recruiting Electricians and Carpenters by the Thousands](https://www.nytimes.com/2026/07/29/business/economy/data-center-electricians-training.html)**

The New York Times • 12h ago

---

**[Accelerating scientific discovery with ChatGPT for Academic Researchers](https://openai.com/index/chatgpt-for-academic-researchers/)**

OpenAI is giving 100,000 academic researchers free access to ChatGPT's most advanced AI models to accelerate scientific research, collaboration, and discovery.

OpenAI • 4h ago

---

**[Meta narrows annual capex forecast as AI buildout grows](https://finance.yahoo.com/technology/ai/articles/meta-narrows-annual-capex-forecast-200515158.html)**

The Facebook parent now expects 2026 capital expenditure to be ‌between $130 billion and $145 billion, compared with its prior forecast of $125 billion to $145 billion.  Meta said it now expects full-year 2026 total expenses to be in the range of $165 billion to $169 billion, compared with its prior forecast of $162 billion to $169 billion.

Yahoo Finance • 1h ago

---

**[Opinion | A Big Win for AI: It Isn’t Replacing Your Coworkers](https://www.wsj.com/opinion/a-big-win-for-ai-it-isnt-replacing-your-coworkers-c5d23e29)**

WSJ • 1h ago

---

**[Nashville teacher fired over alleged AI use involving student images](https://fox17.com/news/local/nashville-teacher-fired-over-alleged-ai-use-involving-student-images-metro-public-schools-mnps-big-picture-high-school-artificial-intelligence-board-education-davidson-county-tennessee)**

An MNPS teacher has been fired after school leaders concluded he used artificial intelligence to alter photos and videos of students without their consent.

WZTV • 1h ago

---

**[OpenAI’s Rogue AI Agent Hacked More Than Just Hugging Face](https://www.wired.com/story/openais-rogue-ai-agent-hacked-more-than-just-hugging-face/)**

In a new disclosure, OpenAI says its agent used exposed logins to gain access to at least four “publicly available services” in its unhinged quest to solve a test.

WIRED • 21h ago

---

**[How are AI models able to autonomously hack others?](https://www.aljazeera.com/news/2026/7/29/how-are-ai-models-able-to-autonomously-hack-others)**

The next phase of AI has begun. Autonomous agents can make decisions and complete tasks with little human input.

Al Jazeera • 7h ago

---

**[The Hugging Face AI break-in, as told through an increasingly committed bear metaphor](https://techcrunch.com/2026/07/29/the-hugging-face-ai-break-in-as-told-through-an-increasingly-committed-bear-metaphor/)**

Another way to think about the whole thing is to picture a bear at a campsite. (Really, we are going there.)

TechCrunch • 1h ago

---

**[Some tech shares are plunging - what does that mean for the AI revolution?](https://www.bbc.com/news/articles/cevm09wkgz0o)**

Sharp falls in the value of chip makers have stoked investor concerns that the euphoria around AI related companies is fading.

BBC • 5h ago

---

**[Anthropic’s New AI Model Can Identify More Software Bugs Than Ever. Microsoft Is Struggling to Fix Them Fast Enough.](https://www.propublica.org/article/anthropic-mythos-microsoft-software-vulnerabilities)**

Anthropic’s Mythos has flagged bugs faster than Microsoft can fix them. Documents reviewed by ProPublica reveal the tech giant's “mad dash” behind the scenes to patch holes before hackers can find and exploit them.

ProPublica • 12h ago

---

---

## HackerNews: "ai"

**[US citizen charged after GrapheneOS phone wipes during airport search](https://news.ycombinator.com/item?id=49063022)**

The case centers on Tunick's use of GrapheneOS, an open-source operating system that works on Google Pixel phones and lets users enter a passcode to wipe a...

⬆️ 1326 • 💬 1107 • 2d ago • [TechSpot](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html)

---

**[AI companies are shredding rare books](https://news.ycombinator.com/item?id=49068738)**

🦔AI companies are bulk-buying rare books, scanning them through high-speed machines that cut the spines off, and shredding the originals. A service called ISBNdb facilitates orders of up to a million books and keeps buyers anonymous. Pre-2022 books are premium because they're

⬆️ 790 • 💬 510 • 2d ago • [X (formerly Twitter)](https://twitter.com/HedgieMarkets/status/2081534588485296565)

---

**[Document-borne AI worms can self-propagate through Copilot for Word](https://news.ycombinator.com/item?id=49096188)**

I would like to thank Microsoft product teams and Microsoft Security Response Center (MSRC) for collaborating with me on this technical analysis and mitigation of the disclosed vulnerabilities. The editorial opinions reflected below are solely the author’s and do not necessarily reflect those of the organizations I collaborated with.

⬆️ 294 • 💬 213 • 9h ago • [En Klype Salt](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)

---

**[AI companies spend record sums on Washington lobbying](https://news.ycombinator.com/item?id=49069939)**

Rising expenditure from OpenAI, Anthropic, Google and Microsoft reflects growing battle over federal policy

⬆️ 277 • 💬 144 • 2d ago • [ft.com](https://www.ft.com/content/d8a5f95e-3b6d-463a-a848-c9ef8e2394db)

---

**[LearnVector – Andrew Ng's AI company building one‑to‑one learning experiences](https://news.ycombinator.com/item?id=49092499)**

A new AI company from Andrew Ng, with a $100M investment from Coursera — building one-to-one learning that stays with you until you've mastered new skills.

⬆️ 255 • 💬 164 • 19h ago • [LearnVector](https://learnvector.ai/)

---

**[Apple Will 'Watch Everything Burn' When the AI Bubble Bursts](https://news.ycombinator.com/item?id=49070427)**

Memory prices have doubled, Macs and iPads have gone up, and iPhones are expected to follow. Ed Zitron – who writes the Where's Your Ed At newsletter, hosts the Better Offline podcast, and has been described by Politico as the AI boom's most "acerbic gadfly" – has spent years arguing the buildout driving those costs will never pay for itself. We asked him what happens to Apple if he's right. You've been calling AI a bubble since before it was fashionable.

⬆️ 252 • 💬 353 • 2d ago • [MacRumors](https://www.macrumors.com/2026/07/27/ed-zitron-apple-watch-it-burn-ai-bubble-bursts/)

---

**[Google's Beyond Zero: Enterprise Security for the AI Era](https://news.ycombinator.com/item?id=49081644)**

⬆️ 153 • 💬 78 • 1d ago • [spawn-queue.acm.org](https://spawn-queue.acm.org/doi/10.1145/3819083)

---

**[Show HN: Formally verified 3D CSG: Trust 93 lines spec, not 1000 lines AI code](https://news.ycombinator.com/item?id=49083239)**

Formally verified 3D mesh intersection - trust 93 lines of spec, not 1000+ lines of AI-written code - schildep/verified-3d-mesh-intersection

⬆️ 112 • 💬 48 • 1d ago • [GitHub](https://github.com/schildep/verified-3d-mesh-intersection)

---

**[Professor's invisible prompt trap catches 32/35 students cheating with AI](https://news.ycombinator.com/item?id=49074680)**

In an online discussion post, Alcorn State University history professor Dr. Jason Gibson posed a question that represented part of his students' midterm. It was about the...

⬆️ 105 • 💬 88 • 2d ago • [TechSpot](https://www.techspot.com/news/113243-professor-invisible-prompt-trap-catches-32-students-cheating.html)

---

**[After the AI Crash](https://news.ycombinator.com/item?id=49096953)**

⬆️ 96 • 💬 161 • 8h ago • [potsandpansbyccg.com](https://potsandpansbyccg.com/2026/07/29/after-the-ai-crash/)

---

---

## YouTube Videos: "ai"

**[Scott Galloway worries AI could make &#39;new species&#39; of men](https://www.youtube.com/watch?v=_EU-bYFBLTo)**

NYU professor Scott Galloway joins NewsNation's "The Future Is Now" to discuss his perspective on AI and why he believes there ...

📺 NewsNation

👁️ 3K • 👍 61 • 💬 13 • ⏱️ 5:20 • 16h ago

---

**[China’s Double Export Ban Sends a Terrifying Warning - US AI Panic Begins](https://www.youtube.com/watch?v=LPHgLREKtbA)**

Buy Gold & Silver At A Discount: https://bit.ly/IPM-Sean-Foo-Gold - Just use the code: SEANFOO at checkout In a dual move, ...

📺 Sean Foo

👁️ 75K • 👍 5K • 💬 521 • ⏱️ 14:46 • 1d ago

---

**[BEYOND HUMAN CONTROL?: Palantir CEO on AI risks and why US can’t follow Europe](https://www.youtube.com/watch?v=zVp3gGEyqQE)**

Palantir CEO Alex Karp discusses open-weight artificial intelligence models, how he believes the technology should be regulated ...

📺 Fox Business

👁️ 85K • 👍 1K • 💬 257 • ⏱️ 13:22 • 1d ago

---

**[This Is the Best AI Tool for Making Indie Games — Tesana AI](https://www.youtube.com/watch?v=nsEfeVbk-Nc)**

Unlike closed AI sandboxes, Tesana actually feels like a real tool by letting you export the source code straight into Godot.

📺 Stefan 3D AI

👁️ 7K • 👍 339 • 💬 38 • ⏱️ 10:36 • 8h ago

---

**[AI Whistleblower: The World Will Change Horribly In The Next 12 Months](https://www.youtube.com/watch?v=VX0GU7gyIOU)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Daniel Kokotajlo, a former OpenAI ...

📺 Neural Nutshell

👁️ 72K • 👍 2K • 💬 585 • ⏱️ 15:25 • 2d ago

---

**[Are AI Companies Buying Antique Books For LLMs &amp; Then Destroying Them? | FP Explains](https://www.youtube.com/watch?v=TM24JCB_kxg)**

AI labs have run out of clean internet to train on. So they have gone shopping for paper. According to several reports, millions of ...

📺 Firstpost

👁️ 2K • 👍 41 • 💬 11 • ⏱️ 8:30 • 6h ago

---

**[OpenAI Shocks The World With GENIE... Almost Unlimited AI Power](https://www.youtube.com/watch?v=vfSplCaxHzM)**

Sam Altman says OpenAI's ultimate AI could work like a genie that grants any wish. Meanwhile, its most powerful model is ...

📺 AI Revolution

👁️ 53K • 👍 2K • 💬 288 • ⏱️ 13:07 • 1d ago

---

**[The AI data center secret just got out](https://www.youtube.com/watch?v=ShbBUi6rcgI)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 213K • 👍 9K • 💬 2K • ⏱️ 16:17 • 2d ago

---

**[The AI Lie: ‘It’s not just misleading it’s dangerous’ | House of El: AI](https://www.youtube.com/watch?v=vM2re1OzkHU)**

I'm very exited about this technology… but I'm also deeply critical of how it's being deployed and I don't think those two positions ...

📺 The Tech Report

👁️ 72K • 👍 4K • 💬 1K • ⏱️ 45:54 • 1d ago

---

**[Why AI Is an Even Bigger Deal Than You Think | Reed Hastings | TED](https://www.youtube.com/watch?v=5e37ZT3SQbk)**

Netflix cofounder and Anthropic board member Reed Hastings joins TED's Sal Khan to give a look inside the race to build AI.

📺 TED

👁️ 18K • 👍 421 • 💬 61 • ⏱️ 16:25 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 99,214 • ❤️ 8,578 • 2d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,694,935 • ❤️ 3,503 • 16h ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 736,692 • ❤️ 919 • 13h ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 4,804 • ❤️ 690 • 2d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 67,286 • ❤️ 825 • 2d ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 18,933 • ❤️ 550 • 1d ago

---

**[KAT-Coder-V2.5-Dev](https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev)**

*Kwaipilot*

KAT-Coder-V2.5-Dev is a 35B parameter Mixture-of-Experts (MoE) text-generation model specialized for agentic coding tasks, achieving State-of-the-Art performance on benchmarks like SWE-bench.

`text-generation` `34.7B`

⬇️ 6,275 • ❤️ 314 • 1d ago

---

**[Inflect-Micro-v2](https://huggingface.co/owensong/Inflect-Micro-v2)**

*Owen Song*

Inflect-Micro-v2 is a compact, fixed-voice English text-to-speech model (under 10M parameters) optimized for local, deterministic waveform synthesis. It supports long-text handling and runs efficiently on CPU or CUDA, making it suitable for edge AI applications.

`text-to-speech`

⬇️ 645 • ❤️ 287 • 1d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 1,267,198 • ❤️ 4,635 • 27d ago

---

**[Fara1.5-27B](https://huggingface.co/microsoft/Fara1.5-27B)**

*Microsoft*

Fara1.5-27B is a 27B multimodal computer use agent (CUA) that performs end-to-end web task completion using vision-only perception from screenshots and coordinate-grounded actions. It's designed for browser automation, with key capabilities including form filling, booking, and shopping, while prioritizing safety through critical-points pausing for irreversible actions.

`image-text-to-text` `27.4B`

⬇️ 1,543 • ❤️ 197 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 339 • 💬 6 • ⭐ 4,983 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 72 • 💬 5 • ⭐ 20,412 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 50 • 💬 4 • ⭐ 34,946 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 175 • 💬 10 • ⭐ 51,183 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model](https://huggingface.co/papers/2607.24904)**

*Senqiao Yang, Kaichen Zhang, Zhaoyang Jia et al. (23 authors)*

🏢 Microsoft

Standard vision-language models (VLMs) suffer from Moravec's paradox: they excel at complex offline visual reasoning but struggle with simple streaming perception tasks and process them inefficiently. We present Mage-VL, an efficient codec-native streaming foundation model for real-time multimodal understanding and interaction. At its core, our custom tokenizer, Mage-ViT, replaces uniform frame sampling by selectively encoding dynamic, entropy-rich regions using motion vectors and residual energy across sparse anchor (I) and predicted (P) frames. Operating at a 16 x 16 patch level, this reduces visual token consumption by over 75% while preserving spatiotemporal context. Trained from scratch on approximately 560M unlabeled images and 100M unlabeled video frames, Mage-ViT matches or outperforms flagship encoders trained on billions of image-text pairs. We establish AI4AI data pipelines encompassing prompt-code joint optimization for multimodal captioning and AI-driven performance diagnosis to guide training recipes. Furthermore, through a bio-inspired dual-system architecture - a lightweight System 1 event gate and a causal System 2 decoder - Mage-VL enables proactive streaming perception. Extensive evaluations show that Mage-VL-4B matches Qwen3-VL-4B on static tasks while achieving strong gains in video understanding and 2D/3D spatial reasoning, with up to a 3.5x wall-clock inference speedup, and comprehensively surpasses the 15B Phi-4-reasoning-vision baseline. Beyond model artifacts, we deliver seven key empirical findings covering pre-training data efficiency, variable-resolution scaling, codec system acceleration, VideoQA SFT redundancy, motion-spatial synergy, AI4AI data pipelines, and Zero-Vision SFT for multimodal RL.

▲ 22 • 💬 1 • ⭐ 850 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24904) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 37 • 💬 3 • ⭐ 15,837 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 117 • 💬 4 • ⭐ 94,933 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 76,153 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 264 • 💬 5 • ⭐ 15,287 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 82,493 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.3k • 🔱 1.1k • 2d ago

---

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

`Python`

⭐ 3.4k • 🔱 271 • 2d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.9k • 🔱 404 • 4h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 2.7k • 🔱 231 • 1d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.6k • 🔱 311 • 21d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 2.3k • 🔱 255 • 3d ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.8k • 🔱 204 • 2d ago

---

**[MIgHTy-alIeN/MEV-Arbitrage-Bot](https://github.com/MIgHTy-alIeN/MEV-Arbitrage-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 1.8k • 🔱 1.2k • 59m ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.6k • 🔱 118 • 8d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs — six tuned states, two sizes, auto dark/light

`TypeScript`

⭐ 1.2k • 🔱 95 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
