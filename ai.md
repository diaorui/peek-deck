---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-28T12:20:42.301329+00:00'
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

**Last Updated:** July 28, 2026 at 12:20 UTC  
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

**[AI Companies Are Buying Antique Books, Ingesting Their Contents to Train Models, and Then Destroying Them at Incredible Scale, Even If Almost No Copies Remain](https://www.reddit.com/r/artificial/comments/1v8ilsm/ai_companies_are_buying_antique_books_ingesting/)**

Source AI companies are literally destroying physical books to train their models. Using hydraulic cutting machines, they rip pages from used books, scan them with industrial equipment, and feed them into their AI systems. This practice, protected by the first-sale doctrine and fair use, has now become so widespread that book sellers are cashing in on the AI boom. Rare and out-of-print books are being pulped, raising serious ethical and cultural concerns about the cost of AI progress.

🔗 [Futurism](https://futurism.com/artificial-intelligence/ai-companies-destroying-rare-books) • 11h ago

---

**[The world's best mathematician won his prize this week and immediately announced he's leaving academia for OpenAI. That landed differently than I expected.](https://www.reddit.com/r/artificial/comments/1v8aeto/the_worlds_best_mathematician_won_his_prize_this/)**

I've been thinking about this one all weekend and I keep coming back to the same thing. Jacob Tsimerman just won the Fields Medal. If you're not familiar, it's the highest honor in mathematics, only awarded every four years, roughly the Nobel Prize of the field. He got it for solving a problem that had been open for nearly 40 years. And then, at the press conference, on the same day, he announced he's leaving his university position to join OpenAI's safety team. His exact words were: "The math profession as we know it now, I don't think it will exist the way it exists right now." I've seen a lot of AI announcements. That one hit differently. This isn't someone pivoting because they couldn't make it in academia. This is the person who just stood at the top of the field saying the field itself is changing underneath him. Then there's the infrastructure story. NVIDIA is in talks to backstop $250 billion in financing for a 10-gigawatt OpenAI data center in southern Ohio, built on a decommissioned uranium enrichment site. The total cost including chips could exceed $500 billion. That's not a software company. That's an energy company pretending to be a software company. And Kimi K3 weights dropped on July 26, a day early. 2.8 trillion parameters, 1 million token context, free to download from Hugging Face. The largest open model ever released. Anyone can run it now. Three things in one week. Talent, capital, and capability all moving at the same time. The Tsimerman thing is the one I can't stop thinking about though. What's your read on it?

16h ago

---

**[I tested Firecrawl, Exa, Parallel and Claude Search on SimpleQA. Here’s what scored best](https://www.reddit.com/r/artificial/comments/1v8u424/i_tested_firecrawl_exa_parallel_and_claude_search/)**

I ran Firecrawl, Exa, Parallel and Claude’s native web search against OpenAI’s SimpleQA benchmark to see how much of a difference the search provider actually makes. All four were tested with the same setup: a GPT-5.4 agent using high reasoning effort, with a maximum of 20 search or extraction calls per question. The answers were then graded by GPT-5.4 using OpenAI’s official SimpleQA grading prompt. Each provider was tested twice and I kept the better result. For comparison, GPT-5.4 without access to search scored 43.8%. The chart shows the correct and incorrect answers for each provider. Results: -Firecrawl: 947 correct answers (94.7%) -Exa: 919 correct answers (91.9%) -Parallel: 910 correct answers (91.0%) -Claude Native Search: 905 correct answers (90.5%) Firecrawl and Exa achieved the highest accuracy, while all four systems scored above 90%. Claude Native search, (not) surprisingly, the worst.

2h ago

---

**[Private Claude chats exposed on Google search results](https://www.reddit.com/r/artificial/comments/1v8gcbk/private_claude_chats_exposed_on_google_search/)**

Over the weekend, Reddit users discovered a trove of private Claude chatbot conversations were indexed and publicly accessible on Google search. Anthropic confirmed the exposure Monday and attributed it to users' misuse of Claude’s “share chat” tool. “We give people control over sharing their Claude conversations publicly," a spokesperson told TechCrunch. "These shareable links are not guessable or discoverable unless people ... share them themselves." Some leaked chats reportedly contained personal data, including medical records and cryptocurrency wallet keys.

🔗 [LinkedIn](https://www.linkedin.com/news/story/private-claude-chats-exposed-on-google-search-results-9083650/?utm_source=share&utm_campaign=reddit&utm_content=storyline&utm_term=artificial) • 13h ago

---

**[China's new challenge as natural disasters strike](https://www.reddit.com/r/artificial/comments/1v8ri12/chinas_new_challenge_as_natural_disasters_strike/)**

As China deals with the fallout of Typhoon Noul that made landfall over the weekend, officials will be painfully aware that they will likely have an additional challenge to deal with: dangerously misleading videos created with Artificial Intelligence (AI).

🔗 [bbc.com](https://www.bbc.com/news/articles/cx27mjvxgg1o) • 4h ago

---

**[AI research tools are still too eager to turn public signals into certainty](https://www.reddit.com/r/artificial/comments/1v8wf6m/ai_research_tools_are_still_too_eager_to_turn/)**

One thing I keep noticing with AI research tools: they’re very good at finding something interesting, but not always good at admitting when that “signal” is weak. I’ve been using Komo AI for company research, and the part I genuinely like is how quickly it can move from a company name to a compact packet of recent signals with the underlying sources kept close to the summary. For scanning accounts or getting oriented before a deeper research pass, that is much nicer than juggling a pile of tabs. The useful features for me are: - company-level research instead of a generic web answer - recent events and signals grouped in one place - source pages attached to the claims - faster prioritization when several companies need to be reviewed But there are still pain points that apply to Komo and most tools in this category. A public event is not the same thing as intent. A hiring page can be stale. A funding announcement may have nothing to do with the problem you care about. A technology mention can describe a partner or an old stack rather than current usage. And a clean summary can make a shaky inference feel more certain than it really is. My workaround is to split the job across tools: Komo handles discovery and builds the source packet. Claude or ChatGPT argues against the initial interpretation. Codex checks required fields, dates, and structured outputs when I need the process to repeat reliably. I make the final call after opening the strongest source myself. The audit prompt is intentionally simple: "Separate what the source directly says from what you inferred. Show the strongest evidence against the conclusion. If a claim depends on missing or stale information, mark it unresolved." What I’d like research products to improve next is contradiction handling. Don’t just show the newest supporting signal—surface evidence that weakens it, show when sources disagree, and make “not enough evidence” a first-class result. Komo saves me time at the discovery stage, but I would not treat it—or any research AI—as a source of truth by itself. The feature I value most is not the summary. It is being able to get back to the evidence quickly. For people using AI research tools: which matters more in practice, better discovery or better uncertainty/contradiction handling?

20m ago

---

**[Why AI companies want to scare you: 'We immediately think of The Terminator'](https://www.reddit.com/r/artificial/comments/1v8p5mt/why_ai_companies_want_to_scare_you_we_immediately/)**

The following is translated from a Dutch news site... The doomsday scenarios regarding artificial intelligence vary: you lose your job, everything will soon be hacked, or humanity will be destroyed. But they share the same goal: to convince you that AI is so powerful that you should be a little afraid of it. Large AI companies love to tell you how dangerous their latest AI program is. And then, every time, they do the same thing: they bring it to market anyway. For instance, seven years ago, OpenAI stated that it was concerned about the misuse of the technology it had developed. This was in early 2019, almost four years before the company gained widespread fame with ChatGPT. At that time, OpenAI was working on an early version of the AI ​​program upon which the chat service is built. This AI program is called GPT-2 and, according to OpenAI, could well lead to major problems. For instance, people using it to create misleading news reports, write texts to scam people, or send offensive messages on social media. That is why it is being released on a limited scale. The reluctance did not last long: nine months later, GPT-2 became fully available after all, although OpenAI did note that the text program could be used for racism or terrorism. 'Enormous consequences' Earlier this year, AI company Anthropic did the same. With its AI program Mythos, anyone without technical knowledge could hack, the company claimed. "The consequences for the economy, public safety, and national security could be enormous." That is why the company, by its own account, made the AI ​​program available only to a small group of companies and organizations. "The name Mythos is brilliant, of course," says Hannes Cools of the University of Amsterdam. He conducts research into the language used surrounding artificial intelligence. "It brings to mind Greek mythology, as if it were some kind of god. Because of that, you quickly think that it is very powerful or mighty." The attention surrounding Mythos helped Anthropic when it released Fable a few months later, Cools believes. That is a variant of Mythos that, according to the company, "is safe for general use." "Thanks to Mythos, Fable also gained the same appeal. Ultimately, of course, they want to sell something," says Cools. Using it to their advantage This is what AI companies do all the time, says technology expert Bert Hubert. "These kinds of companies say every few months: 'Our technology is so dangerous and so terrible, we have to handle it very carefully.' That generates mountains of attention every time. Only to say six weeks later that you can get it there." The AI ​​companies sell stories because they want to make money. What they want is not necessarily in the interest of ordinary people. Andrea Reyes Elizondo, researcher at Leiden University Last week he saw it again, this time once more at OpenAI. The company announced that it had accidentally hacked another company with one of its AI programs. "Normally we call that a crime, but OpenAI turns the bad news into good news. They say they did something stupid, but also how powerful their technology is." According to UvA researcher Cools, OpenAI is well aware that they can use this to their advantage. You can expect that from a commercial company, he says. According to Cools, the problem lies primarily in how the media writes about it: the AI ​​program is said to have 'gone haywire'. "That is not what happened here, but it does sound like all the alarms are going off." The perception surrounding AI reminds people of the science fiction film The Terminator, says Cools. "Words like 'gone haywire' prevent us from fully understanding what this technology can and cannot do. It is problematic because it helps OpenAI in their narrative that the AI ​​was at fault and not them, even though OpenAI is responsible for it." 'Companies sell a story' "OpenAI and Anthropic want to determine how a story is presented to the public," says Andrea Reyes Elizondo. She is a researcher at the Centre for Science and Technology Studies at Leiden University, where research is conducted into the impact of science and technology. "They tell their story in such a way that people think AI is good or scary, or at least has many possibilities." So be critical when a company makes such claims, she says. "Their story targets different people. If a top executive says that AI is going to take over our jobs, they are talking to their customers: the directors of other companies. So that they think they can replace their staff with AI to lower their costs. The AI ​​companies sell stories because they want to make money." "What they want is not necessarily in the interest of ordinary people. Or of society. So ask yourself: why is the company saying this?"

6h ago

---

**[Will AI literacy become a basic workplace skill?](https://www.reddit.com/r/artificial/comments/1v8vu55/will_ai_literacy_become_a_basic_workplace_skill/)**

A few years ago, knowing how to use a computer was a big advantage. Today, it’s expected. I feel AI might follow a similar path. Knowing how to use AI tools effectively could become a basic skill across many jobs. Not everyone needs to build AI models but understanding how to use them, verify outputs and improve workflows might become important. Do you think AI skills will become a normal requirement in the workplace or is the hype bigger than the actual impact?

45m ago

---

**[So Claude Artifacts are Public](https://www.reddit.com/r/artificial/comments/1v8h6l6/so_claude_artifacts_are_public/)**

site:claude.ai/public/artifacts

12h ago

---

**[I tested Firecrawl, Exa, Parallel and Claude Search on SimpleQA. Here’s what scored best](https://www.reddit.com/r/artificial/comments/1v8u2vk/i_tested_firecrawl_exa_parallel_and_claude_search/)**

I ran Firecrawl, Exa, Parallel and Claude’s native web search against OpenAI’s SimpleQA benchmark to see how much of a difference the search provider actually makes. All four were tested with the same setup: a GPT-5.4 agent using high reasoning effort, with a maximum of 20 search or extraction calls per question. The answers were then graded by GPT-5.4 using OpenAI’s official SimpleQA grading prompt. Each provider was tested twice and I kept the better result. For comparison, GPT-5.4 without access to search scored 43.8%. The chart shows the correct and incorrect answers for each provider. Results: -Firecrawl: 947 correct answers (94.7%) -Exa: 919 correct answers (91.9%) -Parallel: 910 correct answers (91.0%) -Claude Native Search: 905 correct answers (90.5%) Firecrawl and Exa achieved the highest accuracy, while all four systems scored above 90%. Claude Native search, (not) surprisingly, the worst.

2h ago

---

---

## Google News: "ai"

**[Tech Stocks Tumble on Worries About A.I. Spending and China’s Chip Competition](https://www.nytimes.com/2026/07/28/business/stocks-ai-chips.html)**

The New York Times • 3h ago

---

**[AI sell-off intensifies as investors ditch chip stocks](https://www.theguardian.com/business/2026/jul/28/ai-sell-off-chip-stocks-sk-hynix-samsung)**

Samsung and SK Hynix fall by more than 10% amid renewed fears over AI spending and Chinese competition

The Guardian • 1h ago

---

**[AI stock sell-off deepens as investors dump chipmakers](https://www.ft.com/content/f8c03b5b-e194-4236-82c3-389b6f5dd7ae?syn-25a6b1a6=1)**

Wall Street tech shares set for further declines after South Korean markets tumble

Financial Times • 9h ago

---

**[Some people's chats with Claude AI found to be publicly available online](https://www.bbc.com/news/articles/cly5qgjk5ywo)**

Hundreds of conversations with Anthropic’s chatbot were discovered as being publicly accessible.

BBC • 5h ago

---

**[Meta to report Q2 earnings amid AI investing concerns](https://finance.yahoo.com/news/meta-to-report-q2-earnings-amid-ai-investing-concerns-121325403.html)**

Meta will report its Q2 earnings after the bell on Wednesday.

Yahoo Finance • 7m ago

---

**[AI has one unsolved problem](https://www.fastcompany.com/91579922/ai-has-one-unsolved-problem)**

Fast Company • 9m ago

---

**[Morning Call Sheet: AI, earnings and Fed outlook drive market focus](https://www.cnbc.com/video/2026/07/28/morning-call-sheet-ai-earnings-and-fed-outlook-drive-market-focus.html)**

Ryan Detrick, Chief Market Strategist at Carson Group, Mark Smith, Senior Vice President and Portfolio Manager at Wells Fargo Advisors, and Jose Torres, Senior Economist at Interactive Brokers, discussed AI, earnings, Fed policy, inflation and portfolio positioning.

CNBC • 28m ago

---

**[Opinion | If You’re Over 40, You’re Ready to Use A.I.](https://www.nytimes.com/2026/07/27/opinion/teaching-kabbalah-ai.html)**

The New York Times • 21h ago

---

**[Opinion | The scams of the future will be written just for you](https://www.washingtonpost.com/opinions/2026/07/28/ai-is-gaining-ability-personalize-cyberattacks-enabling-phishing-scale/)**

AI models can increasingly run scams end to end. The labs that build them aren’t measuring the risk.

The Washington Post • 17m ago

---

**[Is This What Comes After AI Slop?](https://www.theatlantic.com/technology/2026/07/daggermouth-novel-bestseller-ai/688067/)**

Daggermouth could be the first best-selling novel partly written by a chatbot.

The Atlantic • 14h ago

---

---

## HackerNews: "ai"

**[US citizen charged after GrapheneOS phone wipes during airport search](https://news.ycombinator.com/item?id=49063022)**

The case centers on Tunick's use of GrapheneOS, an open-source operating system that works on Google Pixel phones and lets users enter a passcode to wipe a...

⬆️ 1292 • 💬 1041 • 1d ago • [TechSpot](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html)

---

**[AI companies are shredding rare books](https://news.ycombinator.com/item?id=49068738)**

🦔AI companies are bulk-buying rare books, scanning them through high-speed machines that cut the spines off, and shredding the originals. A service called ISBNdb facilitates orders of up to a million books and keeps buyers anonymous. Pre-2022 books are premium because they're

⬆️ 771 • 💬 489 • 23h ago • [X (formerly Twitter)](https://twitter.com/HedgieMarkets/status/2081534588485296565)

---

**[Open-weight AI is having its Kubernetes moment](https://news.ycombinator.com/item?id=49048034)**

⬆️ 410 • 💬 320 • 2d ago • [tobi.knaup.me](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/)

---

**[What is happening to jobs? Separating AI hype from reality](https://news.ycombinator.com/item?id=49052570)**

Other

⬆️ 298 • 💬 376 • 2d ago • [Stanford Institute for Economic Policy Research (SIEPR)](https://siepr.stanford.edu/publications/policy-brief/what-really-happening-jobs-separating-ai-hype-reality)

---

**[London Gatwick has launched a robotic airport parking service](https://news.ycombinator.com/item?id=49058669)**

London Gatwick is the first UK airport to launch robotic parking. Passengers can keep their keys while autonomous robots park their cars.

⬆️ 290 • 💬 259 • 1d ago • [AGN](https://aerospaceglobalnews.com/news/gatwick-airport-robotic-parking-stanley-robotics/)

---

**[AI companies spend record sums on Washington lobbying](https://news.ycombinator.com/item?id=49069939)**

Rising expenditure from OpenAI, Anthropic, Google and Microsoft reflects growing battle over federal policy

⬆️ 268 • 💬 142 • 22h ago • [ft.com](https://www.ft.com/content/d8a5f95e-3b6d-463a-a848-c9ef8e2394db)

---

**[Apple Will 'Watch Everything Burn' When the AI Bubble Bursts](https://news.ycombinator.com/item?id=49070427)**

Memory prices have doubled, Macs and iPads have gone up, and iPhones are expected to follow. Ed Zitron – who writes the Where's Your Ed At newsletter, hosts the Better Offline podcast, and has been described by Politico as the AI boom's most "acerbic gadfly" – has spent years arguing the buildout driving those costs will never pay for itself. We asked him what happens to Apple if he's right. You've been calling AI a bubble since before it was fashionable.

⬆️ 241 • 💬 322 • 21h ago • [MacRumors](https://www.macrumors.com/2026/07/27/ed-zitron-apple-watch-it-burn-ai-bubble-bursts/)

---

**[The New AI Superpowers: Focus and Followthrough](https://news.ycombinator.com/item?id=49057877)**

Burnout is on the rise again, with an ironic twist.

⬆️ 214 • 💬 78 • 1d ago • [rickmanelius.com](https://www.rickmanelius.com/p/the-new-ai-superpowers-focus-and)

---

**[Cloudflare's new AI traffic options for customers](https://news.ycombinator.com/item?id=49052564)**

For our second Content Independence Day, we’re giving website owners finer options to manage AI traffic. Instead of a one-size-fits-all block, all customers can now easily distinguish and manage Search, Agent, and Training bots, alongside the new ability to protect ad-monetized pages.

⬆️ 193 • 💬 157 • 2d ago • [The Cloudflare Blog](https://blog.cloudflare.com/content-independence-day-ai-options/)

---

**[Terence Tao: Mathematics in the Age of AI [pdf]](https://news.ycombinator.com/item?id=49056620)**

⬆️ 159 • 💬 63 • 2d ago • [teorth.github.io](https://teorth.github.io/tao-web/slides/age-of-ai-icm-2026.pdf)

---

---

## YouTube Videos: "ai"

**[Why the AI crash is going viral](https://www.youtube.com/watch?v=iR0P6eVqpy8)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 136K • 👍 8K • 💬 1K • ⏱️ 15:38 • 9h ago

---

**[OpenAI Shocks The World With GENIE... Almost Unlimited AI Power](https://www.youtube.com/watch?v=vfSplCaxHzM)**

Sam Altman says OpenAI's ultimate AI could work like a genie that grants any wish. Meanwhile, its most powerful model is ...

📺 AI Revolution

👁️ 29K • 👍 1K • 💬 172 • ⏱️ 13:07 • 12h ago

---

**[‘Consequences we can’t comprehend’: Elon Musk’s unsettling five-year AI prediction](https://www.youtube.com/watch?v=kO3COuXVgCc)**

News24 contributor Kosha Gada reacts to an interview with Elon Musk in which he predicts AI will overtake human intelligence ...

📺 News24

👁️ 7K • 👍 146 • 💬 114 • ⏱️ 4:27 • 12h ago

---

**[The AI data center secret just got out](https://www.youtube.com/watch?v=ShbBUi6rcgI)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 177K • 👍 8K • 💬 2K • ⏱️ 16:17 • 21h ago

---

**[AI realises it&#39;s not being watched, does what experts warned.](https://www.youtube.com/watch?v=3ohDmtfdHks)**

How will superintelligent AI (AGI) affect our lives? And what can we do about it? Featuring: AI Companions, ChatGPT, OpenAI, ...

📺 AI Frontier

👁️ 20K • 👍 830 • 💬 126 • ⏱️ 21:31 • 1d ago

---

**[10 Times AI Said Things That Scientists Still Can&#39;t Explain](https://www.youtube.com/watch?v=mH4NmqSl2FE)**

Artificial intelligence has produced responses so strange and unexpected that even the researchers who built these systems ...

📺 MostAmazingTop10

👁️ 38K • 👍 774 • 💬 72 • ⏱️ 8:49 • 16h ago

---

**[AI Whistleblower: The World Will Change Horribly In The Next 12 Months](https://www.youtube.com/watch?v=VX0GU7gyIOU)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Daniel Kokotajlo, a former OpenAI ...

📺 Neural Nutshell

👁️ 17K • 👍 519 • 💬 134 • ⏱️ 15:25 • 20h ago

---

**[The Rogue AI Story Just Got A Lot Worse (OpenAI Freaking Out)](https://www.youtube.com/watch?v=JRcAegChriY)**

New reporting reveals OpenAI lost track of its escaped agent for days, while internal tests exposed AI-written escape notes, ...

📺 AI Revolution

👁️ 69K • 👍 3K • 💬 372 • ⏱️ 12:42 • 2d ago

---

**[AMD Says 2 Ryzen AI Halos Can Run a 400B Model... I Tested It](https://www.youtube.com/watch?v=FE1Uyhg5hjw)**

AMD finally answered NVIDIA's tiny AI box with their own Ryzen AI Halo, but the real question Micro Center is THE AI Destination: ...

📺 Alex Ziskind

👁️ 163K • 👍 4K • 💬 449 • ⏱️ 17:42 • 1d ago

---

**[Trump is Starting The Billion Dollar AI Bailout Now](https://www.youtube.com/watch?v=Y1Qt050jSEw)**

Website & Livestream Chat - https://www.vaush.gg/ ⭐️ 2nd Channel - https://www.youtube.com/c/thevaushpit Twitter ...

📺 Vaush

👁️ 97K • 👍 4K • 💬 519 • ⏱️ 9:54 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 99,214 • ❤️ 7,441 • 19h ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 67,286 • ❤️ 778 • 1d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,694,935 • ❤️ 3,375 • 4h ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 736,692 • ❤️ 799 • 11h ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 4,804 • ❤️ 639 • 1d ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 18,933 • ❤️ 505 • 1d ago

---

**[Mage-Flow](https://huggingface.co/microsoft/Mage-Flow)**

*Microsoft*

Mage-Flow is a 4B-scale text-to-image generation and instruction-based image editing model, featuring an efficient native-resolution generation stack (512-2048px) with competitive quality and low latency. It excels at both generating novel images from text and performing versatile image edits, including semantic changes and restoration, with variants for base, RL-aligned, and fast Turbo inference.

`text-to-image` `4.1B`

⬇️ 2,007 • ❤️ 408 • 5d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 1,267,198 • ❤️ 4,578 • 26d ago

---

**[KAT-Coder-V2.5-Dev](https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev)**

*Kwaipilot*

KAT-Coder-V2.5-Dev is a 35B parameter Mixture-of-Experts (MoE) text-generation model specialized for agentic coding tasks, achieving State-of-the-Art performance on benchmarks like SWE-bench.

`text-generation` `34.7B`

⬇️ 6,275 • ❤️ 258 • 7h ago

---

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 39,052 • ❤️ 1,618 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 69 • 💬 5 • ⭐ 19,747 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 50 • 💬 4 • ⭐ 34,689 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 36 • 💬 3 • ⭐ 15,709 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 264 • 💬 5 • ⭐ 15,234 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 117 • 💬 4 • ⭐ 94,835 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 82,347 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://huggingface.co/papers/2607.19064)**

*Xinjie Zhang, Peng Zhang, Shicheng Zheng et al. (24 authors)*

🏢 Microsoft

Large-scale visual generators are increasingly capable but costly to train, fine-tune, and deploy. We introduce Mage-Flow, a compact 4B-scale generative stack for efficient text-to-image generation and instruction-based image editing. The stack is built from two co-designed components: Mage-VAE, a lightweight high-fidelity latent tokenizer, and a Native-Resolution Multimodal Diffusion Transformer trained with rectified flow matching. Mage-VAE uses one-step diffusion-style encoding and decoding with anchor-latent regularization, preserving the reconstruction quality of strong public VAEs while reducing tokenization cost by more than an order of magnitude. Together with native-resolution packing and stack-level CUDA kernel fusion, the stack supports flexible-resolution training and improves end-to-end training throughput by about 2.5times. Built on this foundation, we develop a complete model family with Base, RL-aligned, and Turbo variants for both generation and editing. Diffusion-NFT improves prompt following, text rendering, aesthetic quality, and editing fidelity, while few-step distillation with adversarial perceptual guidance produces 4-step Turbo models for low-latency inference. Despite its compact scale, Mage-Flow and Mage-Flow-Edit achieves competitive performance across standard generation and editing benchmarks. More importantly, the Turbo variants make high-resolution generation and editing practical for interactive use: at 1024^2 resolution on a single NVIDIA A100 GPU, Mage-Flow-Turbo generates an image in 0.59s, and Mage-Flow-Edit-Turbo edits an image in 1.02s, while maintaining a small memory footprint. These results show that careful tokenizer--backbone--system co-design can deliver strong high-resolution generation and editing within an efficient 4B model family.

▲ 72 • 💬 2 • ⭐ 714 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19064) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 75,921 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 64 • 💬 1 • ⭐ 86,094 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 68 • 💬 2 • ⭐ 61,903 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.3k • 🔱 1.1k • 16h ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.4k • 🔱 270 • 3h ago

---

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

`Python`

⭐ 3.0k • 🔱 237 • 1d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.9k • 🔱 403 • 19h ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.6k • 🔱 299 • 19d ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 2.4k • 🔱 208 • 5h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 1.9k • 🔱 206 • 2d ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.8k • 🔱 200 • 1d ago

---

**[MIgHTy-alIeN/MEV-Arbitrage-Bot](https://github.com/MIgHTy-alIeN/MEV-Arbitrage-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 1.5k • 🔱 1.1k • 1m ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.5k • 🔱 110 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
