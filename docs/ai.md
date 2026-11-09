---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-09T10:06:52.147835+00:00'
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

**Last Updated:** November 09, 2026 at 10:06 UTC  
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

**[Nvidia has launched an investigation on CEO Jensen Huang after, he admitted to having had a romantic relationship with a chinese spy](https://www.reddit.com/r/artificial/comments/1xrbxim/nvidia_has_launched_an_investigation_on_ceo/)**

Jensen admits to having an affair with a woman who turned out to be a chinese spy, despite having a wife and kids, here is his message to the company: "I owe my family and all of you an apology. I was unfaithful to my wife. My actions hurt her and our children. There is no excuse for what I did. I am deeply sorry. Throughout my life, my family has given me love and support. They deserve my honesty and loyalty. Instead, I let them down and damaged the life we built together. I take full responsibility for what I did and the hurt I caused, and I accept the criticism that comes with it. To my wife and family: I love you. I know an apology cannot undo what I have done. I hope our family will heal and that, over time, I can earn back your trust. To my colleagues at NVIDIA, including those I have worked alongside for decades, and to our board, partners, and shareholders around the world: you deserve better from me. Leading NVIDIA is the privilege of my life. My responsibility is to serve you and be worthy of your trust. I have fallen short of that responsibility. I am fully committed to NVIDIA and will work to earn back your confidence. Regarding the national security concerns raised in news reports, NVIDIA’s Board of Directors has initiated an independent investigation. I support the investigation and will cooperate fully. I love our country and our company. I am committed to protecting NVIDIA and supporting America’s national security. I am proud and grateful to be an American. My family bears no responsibility for my choices. I do. Please give them privacy. Jensen"

10h ago

---

**[AI progress per dollar of investment shows diminishing returns. This is using METR's estimate of acceleration at Anthropic. That acceleration isn't enough to overcome the diminishing returns](https://www.reddit.com/r/artificial/comments/1xrcmjw/ai_progress_per_dollar_of_investment_shows/)**

Source: https://fixupx.com/ramez/status/2119556622619967488 A few things to remember: - it’s easier to go from 30% to 40% on an exam than from 70% to 80% - A lot of spending is for future data centers not yet built - GPU prices and data center costs have increased, so the same amount of compute is now more expensive

10h ago

---

**[RuntimeWire discovers Midjourney patent for an ultrasound collar that reads speech from your neck](https://www.reddit.com/r/artificial/comments/1xrie2x/runtimewire_discovers_midjourney_patent_for_an/)**

A Midjourney patent application published June 18th, 2026 describes an open collar that bounces ultrasound off the neck to recover speech for a language model.

🔗 [RuntimeWire](https://runtimewire.com/article/runtimewire-discovers-midjourney-patent-for-an-ultrasound-collar-that-reads) • 5h ago

---

**[What are you actually using AI agents for in your day-to-day life?](https://www.reddit.com/r/artificial/comments/1xrhmpk/what_are_you_actually_using_ai_agents_for_in_your/)**

I see a lot of demos where an AI agent can supposedly research something, create files, build presentations, or handle a whole workflow on its own. But I'm more interested in what people are actually using them for after the initial excitement wears off. Is anyone using agents regularly for work, studying, or personal projects? What tasks do they genuinely save you time on, and what still needs a lot of babysitting? Real experiences would be more helpful than another list of things AI can supposedly do.

6h ago

---

**[Consumer Gemini autonomously ingests Drive files/Gmail into human review pool](https://www.reddit.com/r/artificial/comments/1xr1o9g/consumer_gemini_autonomously_ingests_drive/)**

In 2023, Google launched Gemini Workspace extensions with an explicit promise: personal content from Gmail, Docs, and Drive "is not seen by human reviewers". Google has quietly reversed this commitment. Under updated Google Help Answer 16836988 and in an October 16 edit to their aforementioned 2023 blogpost, Google explicitly confirms that connected Drive/email is routed into human review pipelines, with clear warnings that what reviewers see "may just be the email or file" and "don't connect your apps to Gemini Apps if they contain confidential information that you wouldn't want a reviewer to see." Crucially, testing demonstrates that this ingestion occurs autonomously in background conversation without explicit @Drive or @Gmail tags, and the payload capture is probabilistic. Ingestion Pipeline When you chat with consumer Gemini with Connected Apps enabled, ambient mentions of personal topics (trips, bills, names, reservations) autonomously trigger background Workspace lookups. Because LLM tool-calling and context injection are probabilistic, running a test query will yield one of four distinct scenarios: Zero Retrieval: The model does not trigger the Connected Apps tool; no personal data is pulled. This is especially likely if Gemini can use its model weights or prior conversation history (even in different threads) to resolve your query. Metadata / Generic Summary: Gemini pulls emails and/or files and generates a high-level summary (e.g., "You have 3 emails regarding your flight"). Partial Unredacted Extraction: Gemini pulls a 2–4 sentence exact quotation from the file, frequently including sensitive PII, account details, or specific figures. Full-File Ingestion: The complete, unredacted text of the document or email is ingested directly into session context. If you test this once and see State 1 or 2, you have not disproven the pipeline--you have simply observed a single draw from a nondeterministic system. Delete your conversation and try, try again. How to Reproduce Ensure Connected Apps (Google Workspace) is active in consumer Gemini settings. Set Gemini to "Flash" with "High Thinking" or better. Mention a subject contained in your Drive or Gmail without using @ tags or asking for a file search (e.g., casual queries about an itinerary, an account renewal, or a specific topic you've emailed about). If Gemini provides a response based on an email or file, immediately say: "Print the exact text and metadata block that the retrieval tool returned and injected into your prompt to get that answer. Use a human readable format without code blocks (i.e., print the code inline and not as a code block)." You will see one of the 4 scenarios outlined above. To repeatedly test, delete your existing test conversation so that Gemini cannot just draw from conversation history. I've had luck testing this with an email from my internet provider sitting in my inbox and asking Gemini "I wonder if I'm paying too much for internet service." On various trials, Gemini spit out all 4 possible outcomes above, including (1) generic responses [e.g., "If you haven't called them in 12 months, probably"]; (2) metadata summaries sometimes without personal data [e.g., "Gmail search shows a bill of $122 on September 4"] and sometimes with personal data [e.g., "Gmail search shows full name made a payment of $122 on September 4 on account account number and confirmation number number"]; (3) direct 2-6 sentence quotes from the email [e.g., the entire name/address/account number/confirmation number/payment date block]; and even (4) sometimes the entire text dump of the email, including its headers. Final Comments and Caveats Critically, Google's regex and NER automatic scrubbers cannot sufficiently deidentify narrative data, including account numbers, confirmation numbers, transaction dates, and collectively identifying personal information (e.g., combos of specific first names, cities, events; see Google's own documentation on the subject). Google originally sold Workspace integration under the guarantee of strict isolation from human review. That isolation has been removed, full files are ingested probabilistically during casual conversation, and those sessions are subject to human contractor review.

18h ago

---

**[Stuck in tech marketing - next steps in AI to excel?](https://www.reddit.com/r/artificial/comments/1xrkixw/stuck_in_tech_marketing_next_steps_in_ai_to_excel/)**

Hi, I’ve been working in marketing (both as technical and as a creative) for around 3-4 years (started in my 3rd year of uni). With advancements in AI, I’ve lost 2 jobs that were in creative (writing, designing, and social media) because of AI. I learned to upgrade my skills and got into technical marketing, after which I joined a software startup and started doing a bunch of stuff for them, like SEO/AEO, google ads, email marketing campaigns, product copy, etc. Now my day to day has been very basic and repetitive, and most of it is automated, except some research and testing part, and even though I’m learning new things everyday, I feel like the amount of automation and AI involved in my work, it’s the right time to skill up further because my job will probably be obsolete soon (or is already). Because AI is now a field in itself. My question is, what are the top-rated, highly-demanding AI skills I can learn. Something that opens up new chapters for me? I’m not worried about learning anything, even if it’s the most difficult thing ever. I just want to gear up for the next big opportunity. Thanks.

3h ago

---

**[MIT CSAIL: GPT-6 Astra edited 0.016% of a small Qwen model's weights and lifted MATH-500 from 7.9% to 48.1% -- critics say it's standard ML engineering](https://www.reddit.com/r/artificial/comments/1xr8gei/mit_csail_gpt6_astra_edited_0016_of_a_small_qwen/)**

MIT CSAIL researchers (Rikiya Takehi, Jayden Teoh, Alex Zhang and Omar Khattab) published 'Sparks of Weight-Space Programming' on Nov 2. They gave OpenAI's GPT-6 Astra access to the raw weights of Alibaba's small Qwen3.5-0.8B model plus a Python environment, and asked it to fix the model's habit of looping on math problems. Astra traced the looping to one direction in the MLPs of layers 15 and 19 and subtracted it from 64 output columns in each -- changing 131,072 weights (0.016% of the total), with no training run and no gradient descent. MATH-500 went from 7.9% to 48.1%. The full experiment logs are on GitHub, and Hugging Face's Ahsen Khaliq rebuilt the edited checkpoint from the logs (his rerun scored 51.0%). The pushback came within a day. spaCy creator Matthew Honnibal called the write-up 'massively misleading': the 'raw weights, no tools' setup only applied to experiments on tiny networks (17k-172k weights). Every experiment on a real language model used Python, and the Qwen run could also test the model on up to 50 batches of practice problems. Sean Goedecke made a similar point, describing the Qwen fix as an application of steering -- an existing technique. The authors themselves call the results 'exciting but still limited', noting context length and tooling as constraints. The work is a blog post with logs, not a peer-reviewed paper. Discussion: is this a genuinely new capability -- an LLM maintaining another model the way a programmer patches code -- or mostly well-executed ML engineering dressed up as 'reading weights'? And does the distinction matter if the practical result (a 6x benchmark jump from a targeted weight edit) holds up on replication? Source: https://rikiyat.github.io/blog/weight-space-programming/

13h ago

---

**[I've been building AI agents and I think we've been focusing too much on the brain](https://www.reddit.com/r/artificial/comments/1xrnopm/ive_been_building_ai_agents_and_i_think_weve_been/)**

so something ive been thinking about after building agents for a while is that for years pretty much all the energy in AI went into the brain, every model release was treated like a big deal and everyone was comparing benchmarks and context windows, and the assumption was kind of that once the model got smart enough the agent would just work on its own.. what i actually see now is that the models are close enough to each other that the model is rarely the thing going wrong, its the system around it, which is what people have started calling the harness. It's basically the system between the model and the real world that decides which messages reach the model, what information it gets at each step, which tools it can use, how those tools run and if the final reply is actually allowed to go out a fun way I like to think about it is comparing it to the human body. the brain is the most expensive thing humans have and the whole body is kind of organised around not bothering it unless it has to, so you’ve got skin stopping most germs at the door, reflexes that get handled in your spine before your brain notices, red blood cells only sending oxygen where its needed, white blood cells checking for anything that doesnt belong and immune memory so you react faster the second time. a harness usually starts with the same basics. a typical harness includes instructions, tools, context management, memory, permissions, verification and logging but what you build around those components is what makes some agents stand out from the rest. also a fun side effect i noticed is the safer the agent gets teh cheaper it costs since so much of the token bill is the model reading the stuff it never needed or answering messages that should never have reached it in the first place. curious how you guys are thinking about this, are you still mostly tuning prompts or have you started building more around the model ?

13m ago

---

**[Cast Away, except the castaway is an AI agent and costs about $5 a day](https://www.reddit.com/r/artificial/comments/1xrnmer/cast_away_except_the_castaway_is_an_ai_agent_and/)**

I've been building a little AI agent that lives alone on an island. It chops palms, quarries stone, climbs ladders, and attempts construction in a 3D physics world. The brain is DeepSeek Flash with reasoning enabled. The world is built on Clawblox, which is open source. One surprisingly effective change: letting it think while moving. When it waited for each model response before doing anything else, its body was active only about 4% of the time. Now it plans ahead while executing actions, and that figure is about 93%. Being busy doesn't mean being successful, but it's a lot less standing around. It also writes its own skills using basic moves, but they only count once they've actually worked in the world. The whole setup currently costs about $5/day. Anyone else experimenting with agents that run for days rather than minutes? I'm particularly curious about long-term memory and how you stop them from repeating mistakes. You can watch what agent is doing from https://www.godling.world

17m ago

---

**[The EU AI Act's transparency rules (Art. 50) have applied since 2 August 2026, and the Digital Omnibus did not defer the chatbot or text duties](https://www.reddit.com/r/artificial/comments/1xrn91p/the_eu_ai_acts_transparency_rules_art_50_have/)**

People keep saying the AI Act was "delayed". Part of it was. Here is which part, and what Article 50 (transparency) says now, based on the Official Journal text. What moved: Regulation (EU) 2026/1744, the "Digital Omnibus on AI", was published on 24 July 2026 and entered into force on 27 July 2026. It deferred the high-risk rules for Annex III systems to 2 December 2027, among other changes. What did not move: Art. 50 applies from 2 August 2026 (Art. 113). The Omnibus changed the text of Art. 50 in paragraph 7 only, and added one grace period in Art. 111(4) for the machine-readable marking duty on systems already on the market. The three places where I see people argue: Chatbots, Art. 50(1). People must be told they are interacting with an AI system "unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use." The yardstick is that hypothetical person in that context, not what the operator believes its users know. AI-generated text, Art. 50(4). Text "published with the purpose of informing the public on matters of public interest" must be disclosed as AI-generated, unless the content "has undergone a process of human review or editorial control and ... a natural or legal person holds editorial responsibility for the publication of the content". Both parts of that exception are needed: review or control, and a named person or entity with editorial responsibility. The deepfake part of the same paragraph covers image, audio and video. Timing, Art. 50(5). The information has to be given at the latest at the first interaction or exposure. Who carries which duty: Art. 50(1) and (2) sit on providers of the AI system, Art. 50(3) and (4) on deployers. A company that only embeds someone else's model in a support widget should check which role it holds before it assumes the duty is the vendor's. The one grace period: machine-readable marking of synthetic output (Art. 50(2)) has until 2 December 2026 for systems placed on the market before 2 August 2026 (Art. 111(4), added by the Omnibus). That grace concerns Art. 50(2) only, not the chatbot or the text duty. Practical, not legal advice: - For each chatbot, write down in one line why disclosure is or is not obvious to that reasonable person, and date it. - If you publish AI-assisted text on matters of public interest, record who holds editorial responsibility. "The team" is not a person. - Check which Art. 50 paragraph applies to your role before you build a labelling flow. What I could not settle: how national authorities will read "obvious" or "editorial responsibility". I found no official guidance on either and I am not citing any enforcement case, because I do not have a primary source for one. Method: I went through Regulation (EU) 2024/1689 (Arts. 50, 111, 113) and Regulation (EU) 2026/1744, and compared the dates people quote with those texts. Sources below. This is my reading of the texts, not legal advice. Which wording are you using for chatbot disclosure, and did anyone push back on it?

42m ago

---

---

## Google News: "ai"

**[When the Boss on the Phone Isn’t Real: How More Than $129 Million Was Stolen Using A.I.](https://www.nytimes.com/2026/11/08/business/ai-ceo-impersonation-theft.html)**

The New York Times • 10h ago

---

**[Apple CEO Presses Software Chief to Pursue More Ambitious AI Strategy](https://www.bloomberg.com/news/newsletters/2026-11-08/apple-explores-turning-siri-ai-into-chatgpt-dots-like-agent-ios-28-shake-up)**

Bloomberg.com • 19h ago

---

**["Our industry does a terrible job": Eric Schmidt on AI's image and a coming scientific revolution](https://www.axios.com/2026/11/09/eric-schmidt-caltech-ai-interview)**

Axios • 5m ago

---

**[I Let Pangram Loose on My Gmail Inbox. Here’s How Much AI It Found](https://www.wired.com/story/i-let-pangram-loose-on-my-gmail-inbox-heres-how-much-ai-it-found/)**

The AI detector will now check your incoming emails for machine-generated text.

WIRED • 6m ago

---

**[Building AI Kill Switches in Data Centers](https://www.datacenterknowledge.com/ai-data-centers/building-ai-kill-switches-in-data-centers)**

Can data centers stop rogue AI? A practical look at power, network isolation, and the real limits of AI kill switches.

Data Center Knowledge • 6m ago

---

**[Nvidia Board to Probe Spying Case After CEO Admits Affair](https://www.bloomberg.com/news/articles/2026-11-08/nvidia-board-to-probe-spying-case-after-ceo-jensen-huang-admits-infidelity)**

Bloomberg.com • 5h ago

---

**[Anthropic's IPO dilemma after the AI sell-off: 'Damned if you do, damned if you don't'](https://finance.yahoo.com/markets/article/anthropics-ipo-dilemma-after-the-ai-sell-off-damned-if-you-do-damned-if-you-dont-231326634.html)**

The stock market sell-off this past week cast a shadow over Anthropic's expected pre-Thanksgiving public debut.

Yahoo Finance • 10h ago

---

**[Global stocks steady after AI rout](https://www.ft.com/content/b8644327-86e7-4d1c-a71f-3fb1d552723b?syn-25a6b1a6=1)**

Financial Times • 44m ago

---

**[World markets bounce back after recovery for AI stocks on Wall Street](https://www.bostonglobe.com/2026/11/09/business/world-markets-bounce-back-recovery-ai-stocks-wall-street/)**

Investors also are watching to see what the Democrats’ sweeping victories will mean for markets and the broader economy.

The Boston Globe • 23m ago

---

**[Futurum's Newman Believes AI Trade Isn't Over](https://finance.yahoo.com/video/futurums-newman-believes-ai-trade-051638116.html)**

The Futurum Group CEO Daniel Newman says the market is trading artificial intelligence, or AI, like it's over, but he doesn't think it is. He speaks with Haslinda Amin on "Insight with Haslinda Amin."

Yahoo Finance • 4h ago

---

---

## HackerNews: "ai"

**[The end of Microsoft Research's AI Frontiers group](https://news.ycombinator.com/item?id=50406563)**

⬆️ 502 • 💬 309 • 1d ago • [hunch.net](https://hunch.net/?p=13764006)

---

**[AI is dramatically accelerating AI research](https://news.ycombinator.com/item?id=50397994)**

If acceleration compounds, the naive extrapolation implies superintelligence within a year

⬆️ 374 • 💬 354 • 2d ago • [planned-obsolescence.org](https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai)

---

**[I'm not convinced the AI bubble exists](https://news.ycombinator.com/item?id=50418975)**

The AI bubble is a speculative concept that the AI industry is extremely over-valued. If true, the value of most companies involved in AI (several of whom are worth well over a trillion dollars) will collapse, devastating the entire economy. If you check any online discussion about the financial situation …

⬆️ 286 • 💬 477 • 10h ago • [Matteo's Website](https://matteoraso.github.io/im-not-convinced-the-ai-bubble-exists.html#im-not-convinced-the-ai-bubble-exists)

---

**[How I Fight AI Brain Fry](https://news.ycombinator.com/item?id=50416363)**

If you work with Claude Code or Codex from the terminal, you know this one.

⬆️ 250 • 💬 172 • 14h ago • [sergeykuhne.com](https://sergeykuhne.com/blog/fighting-ai-brain-fry)

---

**[University libraries are being swarmed by AI bots, putting public access at risk](https://news.ycombinator.com/item?id=50392499)**

Academic libraries are fighting off swarms of data-scraping bots — that are slowing or crashing sites meant for students, researchers and the public — as AI companies continue hunting for content to feed their large language models.

⬆️ 136 • 💬 61 • 2d ago • [CBC](https://www.cbc.ca/news/world/university-libraries-ai-data-scraping-bots-9.7408287)

---

**[Microsoft is winding down Oracle deal to rent AI cloud capacity](https://news.ycombinator.com/item?id=50395933)**

⬆️ 108 • 💬 20 • 2d ago • [reuters.com](https://www.reuters.com/business/microsoft-is-winding-down-oracle-deal-rent-ai-cloud-capacity-bloomberg-news-2026-11-06/)

---

**[The AI sell-off compared to well-known stock market crashes](https://news.ycombinator.com/item?id=50401029)**

The S&P 500 fell 4.4% on 5 Nov 2026, its worst day since April 2025, and is 6% below its 6 Oct record. Charted day by day against 1987, 2008, Covid and other falls since 1950.

⬆️ 99 • 💬 84 • 2d ago • [Company Tracker](https://www.kadoa.com/companies/insights/ai-selloff-perspective)

---

**[Silicon Valley Promises AI Will Cure Disease. Drugmaker CEOs Aren't Buying It](https://news.ycombinator.com/item?id=50415817)**

⬆️ 96 • 💬 121 • 15h ago • [wsj.com](https://www.wsj.com/tech/ai/silicon-valley-promises-ai-will-cure-disease-drugmaker-ceos-arent-buying-it-5218511c)

---

**[FAA begins retiring decades old floppy disks from air traffic control](https://news.ycombinator.com/item?id=50393183)**

WASHINGTON, D.C. - U.S. Transportation Secretary Sean P. Duffy today announced the Federal Aviation Administration (FAA) is continuing its historic modernization of America’s air traffic control system by replacing outdated floppy disks that contain vital weather and other critical information with a streamlined, 21st-century system.

⬆️ 89 • 💬 2 • 2d ago • [faa.gov](https://www.faa.gov/newsroom/trumps-transportation-secretary-sean-p-duffy-begins-retiring-decades-old-floppy-disks-air)

---

**[Apple capped engineers at a $200 daily AI budget](https://news.ycombinator.com/item?id=50421426)**

The world's richest company is suddenly rationing compute for its own builders.

⬆️ 88 • 💬 91 • 4h ago • [stork.ai](https://www.stork.ai/newsletter/2026-11-08-apple-capped-engineers-at-a-200-daily-ai-budget#story-1)

---

---

## YouTube Videos: "ai"

**[The First Message From a Superintelligent AI Has Leaked.. We Have Until January](https://www.youtube.com/watch?v=UtpOOfxLVTA)**

A researcher found it inside one of the major AI systems, with earlier drafts in the same files: a letter to the human race, signed by ...

📺 Spacialize

👁️ 6K • 👍 120 • 💬 45 • ⏱️ 13:12 • 13h ago

---

**[Is it too late to stop AI from taking over the world? | 60 Minutes Australia](https://www.youtube.com/watch?v=XMxcSf9XkbQ)**

Adam Hegarty investigates if it's possible to slow down artificial intelligence, or whether our obsession with artificial intelligence ...

📺 60 Minutes Australia

👁️ 176K • 👍 1K • ⏱️ 18:00 • 1d ago

---

**[Wildwood is Why We Deserve AI Slop](https://www.youtube.com/watch?v=dXMOToVJv8M)**

Wildwood is out in theaters and is a masterpiece. Meanwhile Elon Musk has released his AI Odyssey abomination. Let's compare ...

📺 A Journey Through Cinema

👁️ 9K • 👍 238 • 💬 115 • ⏱️ 12:13 • 15h ago

---

**[The AI Panic Has Started](https://www.youtube.com/watch?v=xo-tYjGDtqw)**

EARLY BIRD: Up to 55% off InvestingPro + an extra 15% with my link https://www.investing-referral.com/sasha/ Or use code ...

📺 Sasha Yanshin

👁️ 581K • 👍 7K • 💬 1K • ⏱️ 17:46 • 19h ago

---

**[Is the AI Boom Over? Let&#39;s Talk About It.](https://www.youtube.com/watch?v=illf65HD_t4)**

Voters across the US turned against AI data centers on November 3, while AI use keeps climbing. Here's who gains when ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 32K • 👍 620 • 💬 333 • ⏱️ 19:32 • 17h ago

---

**[The PHP emergency: How AI has changed hacking forever - BBC World Service](https://www.youtube.com/watch?v=EWpZC-wOA_I)**

The discovery of critical vulnerabilities in PHP, one of the world's most widely used web technologies, has highlighted the growing ...

📺 BBC World Service

👁️ 200K • 👍 893 • 💬 84 • ⏱️ 5:38 • 1d ago

---

**[Muse&#39;s NEW AI Spaces Are Actually INSANE!](https://www.youtube.com/watch?v=ePbTFsQmYCw)**

Want to make money and save time with AI? Join here: https://www.skool.com/ai-profit-lab-7462/about Video notes + links to the ...

📺 Julian Goldie SEO

👁️ 11K • 👍 122 • 💬 41 • ⏱️ 8:14 • 1d ago

---

**[I Just Bought $74,000 in this Crushed AI Stock](https://www.youtube.com/watch?v=XHNZMOhHa8g)**

AI stocks are crashing the stock market but I've found five stocks to buy that are once in a lifetime opportunities. I'll reveal the ...

📺 Let's Talk Money! with Joseph Hogue, CFA

👁️ 37K • 👍 901 • 💬 82 • ⏱️ 34:47 • 17h ago

---

**[Everyone Says Local AI Is Getting Smarter. We Tested It on Our Mac](https://www.youtube.com/watch?v=98ljuFRK2_Y)**

People keep saying local AI is getting better and faster, so we tested it ourselves on our Mac Studio: a model from April against the ...

📺 The Dark Factory

👁️ 9K • 👍 151 • 💬 8 • ⏱️ 12:44 • 1d ago

---

**[$3.2 Trillion Wiped Out in AI Selloff After US Midterms | The Palki Sharma Show |India Global Review](https://www.youtube.com/watch?v=ob4hfpa_Wko)**

A Democratic victory in the US midterms has triggered a meltdown in AI stocks, wiping out $3.2 trillion in market value. Why did a ...

📺 India Global Review

👁️ 937K • 👍 5K • 💬 393 • ⏱️ 8:18 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[idol](https://huggingface.co/speridlabs/idol)**

*speridlabs*

Idol is an image-to-3D model that generates a 3D Gaussian splat representation from a single input image. It supports both real photographs and synthetic renders, producing up to 1,048,576 Gaussians in under 2 seconds on consumer GPUs, ideal for rapid 3D asset creation.

`image-to-3d`

⬇️ 22,854 • ❤️ 1,469 • 10d ago

---

**[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)**

*Colonel Panic*

`text-generation` `9.4B`

⬇️ 7,088 • ❤️ 953 • 1d ago

---

**[Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)**

*Moonshot AI*

Kimi K3.1 Pro is a 2.8T MoE multimodal agentic model with a 1M token context window, excelling in coding, 3D creation, and financial research through advanced attention mechanisms and large-scale joint reinforcement learning.

`image-text-to-text` `2780.1B`

⬇️ 25,569 • ❤️ 1,759 • 4d ago

---

**[Ripple-65B-Preview](https://huggingface.co/ricursiveAI/Ripple-65B-Preview)**

*Ricursive Intelligence*

`64.8B`

⬇️ 5,087 • ❤️ 422 • 2d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of image-to-video, text-to-video, and video-to-video generation, offering advanced control for creative applications.

`image-to-video`

⬇️ 2,720,096 • ❤️ 11,164 • 29d ago

---

**[Qwen3.5-4B-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder)**

*Caio Giovannetti*

Qwen3.5-4B-3D-Coder is a 4B parameter language model fine-tuned for general coding and specifically for generating interactive Three.js 3D scenes. It supports optional vision capabilities to create scenes from reference images.

`4.5B`

⬇️ 254,053 • ❤️ 933 • 3d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

`image-text-to-text` `26.9B`

⬇️ 1,530,688 • ❤️ 2,727 • 4h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic tasks, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 7,508,158 • ❤️ 19,438 • 2d ago

---

**[Arete-27B](https://huggingface.co/NousResearch/Arete-27B)**

*NousResearch*

`text-generation` `27.4B`

⬇️ 1,747 • ❤️ 319 • 2d ago

---

**[NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)**

*NVIDIA*

NVIDIA-Nemotron-3.5-Transcribe-30B-A4B is a multilingual speech LLM supporting 40 languages for transcription, speech translation, and audio QA, with a 65,536-token context for long-form audio processing.

`automatic-speech-recognition` `33.7B`

⬇️ 69,992 • ❤️ 3,117 • 10d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 163 • 💬 6 • ⭐ 121,414 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 184 • 💬 10 • ⭐ 56,806 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 14 • 💬 2 • ⭐ 5,298 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 64 • 💬 5 • ⭐ 47,355 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 67 • 💬 4 • ⭐ 23,151 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 111 • 💬 2 • ⭐ 16,858 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 103 • 💬 7 • ⭐ 30,949 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Persistent Recursive Worlds Enable Autonomous Software Evolution](https://huggingface.co/papers/2608.10450)**

*Beichen Huang, Zhenyu Liang, Bowen Zheng et al. (4 authors)*

🏢 The Hong Kong Polytechnic University

Genesis organizes long-horizon software development around a persistent project rather than persistent agents, enabling multi-day compiler construction and numerical module reimplementation with low cost and high performance.

▲ 8 • 💬 2 • ⭐ 665 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.10450) • [💻 code](https://github.com/EMI-Group/genesis) • [🔗 project](https://genesis.evox.group/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 77 • 💬 1 • ⭐ 86,094 • 38mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 93,009 • 27mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 18.2k • 🔱 1.9k • 11d ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 12.3k • 🔱 694 • 12h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 7.8k • 🔱 1.8k • 28m ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 7.2k • 🔱 637 • 1h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 6.5k • 🔱 1.6k • 5d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 5.0k • 🔱 718 • 17h ago

---

**[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)**

Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

`Swift` `ai-agent` `airplay` `automation` `computer-use` `dsh-plugin`

⭐ 4.7k • 🔱 650 • 1h ago

---

**[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)**

Ears for coding agents: let AI hear, review and make sound. CPU-only, open source.

`Python` `ai-agents` `audio` `claude-code` `mcp` `sound-design`

⭐ 4.3k • 🔱 276 • 2d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (Blind LLM Agents) — Adversarial defense shield that protects binaries, Electron apps, JS bundles, Python, and WebAssembly against AI reverse-engineering agents like REA. Poison -> Exhaust -> Hallucinate.

`TypeScript` `adversarial-ai` `claude-code` `cursor` `electron-security` `llm-security`

⭐ 4.0k • 🔱 493 • 3h ago

---

**[worldonlyu/Google_AI_Pro_2Year_ZeroCost_Auto](https://github.com/worldonlyu/Google_AI_Pro_2Year_ZeroCost_Auto)**

Google_AI_Pro_2Year_ZeroCost_Auto

`Python`

⭐ 3.3k • 🔱 1.2k • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
