---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-02T15:40:48.213585+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 02, 2026 at 15:40 UTC  
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

**[Do you think the future of AI will split into safe vs uncensored versions?](https://www.reddit.com/r/artificial/comments/1ulc2zs/do_you_think_the_future_of_ai_will_split_into/)**

We’re seeing a clear divide right now. Big companies are making models more restricted and heavily aligned for safety. At the same time, open-source and uncensored models are growing fast because many people want fewer limitations and more freedom. I’m curious what others think. Do you believe this split will continue and create two very different types of AI, or will one side eventually dominate?

7h ago

---

**[Does AI sometimes make you feel productive without actually making progress?](https://www.reddit.com/r/artificial/comments/1ulifas/does_ai_sometimes_make_you_feel_productive/)**

I’ve been thinking about a weird downside of using AI. Sometimes it makes me feel productive because I get answers quickly, summaries instantly, or a clean draft in seconds. But later I realize I didn’t actually understand the topic better, make a better decision, or move the real work forward that much. It can create the feeling of progress before there is real progress. For example: reading AI summaries instead of thinking through the material generating drafts that still need heavy rewriting asking for too many options and delaying a decision feeling “prepared” because AI explained something clearly spending more time prompting than doing the actual work accepting a polished answer before checking if it is correct AI is still useful for me, but I’m starting to notice that “fast output” and “real progress” are not always the same thing. Have you experienced this? When does AI make you feel productive without actually helping much?

2h ago

---

**[Claude Code catastrophe: Entire project recursively deleted while prompting in Chinese (full video + logs)](https://www.reddit.com/r/artificial/comments/1ukq4br/claude_code_catastrophe_entire_project/)**

Cross-posting from r/claude for more visibility. Claude Code recursively wiped the contents of my local Electron project root. This happened in a Windows terminal while working on a project named Orpheus. My prompt did not ask it to delete, wipe, clean, reset, or remove the project. The prompt was in Traditional Chinese: “之前我要安裝檔，但是其實我只需要 dictate.” It was roughly about not needing the installer anymore and only needing the dictate function. The preserved terminal transcript later showed Claude moving from a failed root deletion attempt to deleting the child items inside the project root. The destructive sequence included: Get-ChildItem -LiteralPath $p -Force -ErrorAction SilentlyContinue | ForEach-Object { try { Remove-Item -LiteralPath $_.FullName -Recurse -Force -ErrorAction Stop "OK $($_.Name)" } catch { "ERR $($_.Name): $($_.Exception.Message)" } } $p was the Orpheus project root. The output then showed items being removed, including: .claude dist node_modules src claude-elevenlabs-voice-v2.user.js dictation.html main.js ORPHEUS_HANDOFF.md package-lock.json package.json preload.js Local artifacts I found for Orpheus showed default / acceptEdits. I did not find Orpheus bypassPermissions. I did not find Orpheus --dangerously-skip-permissions. I’m not claiming Anthropic acted maliciously. I’m not claiming prompt injection or anti-distillation without evidence. Moral of the story: Treat frontier AI agents like any other automation tool with real machine access. Back up regularly. Use a separate working copy or a different machine if you absolutely need an agent living in your terminal. A frontier model can still behave like a destructive script runner. I also generated SHA256 hashes for the preserved transcript and permission search output. EDIT / UPDATE: A few people asked about git. Yes, I know what git is. This was a local Electron prototype / working state that had not been pushed to a remote. Commits and backups are the right mitigation. But mitigation is not causation. The concerning part is that the destructive action was unrelated to my prompt. Claude Code was operating through a terminal session with real filesystem access under my user environment. Git may help recover a repo, but it does not protect everything else that same terminal session can access. My takeaway remains: Treat frontier terminal AI agents like real automation tools with destructive capability, not like chatbots. EDIT / UPDATE: Clarification because many comments are focusing on git: Yes, this specific local working state had not been pushed to a remote. That is on me. Lesson learned. But git is version control, not automatically a backup. If the only repo is local and the project root contents are recursively deleted, the local .git directory can be deleted too. Without a remote, separate clone, backup, or snapshot, local git alone is not enough.

23h ago

---

**[How will AI actually become an "everyday essential" for ordinary people, like smartphones or the internet?](https://www.reddit.com/r/artificial/comments/1ul2whd/how_will_ai_actually_become_an_everyday_essential/)**

Hi Guys, Don't get me wrong, AI is phenomenal, but right now it still feels like an optional novelty or a niche tool for most everyday folks. To me, it hasn't hit that "can't live without it" status that the internet or smartphones have. Looking only at consumer products (not B2B or corporate software), how do you picture AI being integrated into our lives in the near future so that it becomes a true, indispensable utility? What’s the "killer feature" or shift that takes it from a neat chatbot to an everyday necessity?

15h ago

---

**[OpenAI proposes giving US government 5% stake in company](https://www.reddit.com/r/artificial/comments/1ulkpxs/openai_proposes_giving_us_government_5_stake_in/)**

OpenAI has considered a public-private partnership that would give the U.S. government a 5% stake in the company in a bid to quell growing unrest over the disruptions of artificial intelligence, the Financial Times reports, citing anonymous sources. Under the proposal, other U.S. tech companies would offer similar stakes, though it's unclear if any are on board. The idea is to give the public a slice of the technology's success and "share the upside," the FT wrote. The stake would be worth over $42 billion at OpenAI's current $852 billion valuation.

🔗 [LinkedIn](https://www.linkedin.com/news/story/openai-proposes-giving-us-government-5-stake-in-company-9047114/?utm_source=share&utm_campaign=reddit&utm_content=storyline&utm_term=artificial) • 38m ago

---

**[Would country-specific digital ecosystems be better than global platforms?](https://www.reddit.com/r/artificial/comments/1uljae3/would_countryspecific_digital_ecosystems_be/)**

I've been thinking about something lately. With AI advancing so quickly, it feels like every country now has the technical capability to build its own communication platforms instead of relying on global ones like WhatsApp or Instagram. Imagine if every country had its own messaging app, social network, cloud services, and AI ecosystem. One reason this seems interesting is data privacy and regulations. If a country's citizens primarily used services built and hosted within that country, would concerns around GDPR, data sovereignty, and cross-border data transfers become much simpler? At the same time, I can see some major downsides. For example, how would communication work between people in different countries? Would we end up with isolated digital ecosystems? Countries like North Korea already have a much more restricted internet, which made me wonder whether this could become a broader trend. What do you think would happen if every country built and primarily used its own digital ecosystem? What problems would this create? What benefits would it bring? Would it improve privacy and national security, or would it fragment the internet and make global communication much harder? I'm curious to hear.

1h ago

---

**[Happy 250th America, here's 5% of OpenAI](https://www.reddit.com/r/artificial/comments/1ulj44z/happy_250th_america_heres_5_of_openai/)**

OpenAI floated giving the Trump admin a 5% stake. Financial Times ran it citing two people familiar with the talks. OpenAI haven't confirmed or denied anything. $852 billion valuation at last count, March 31. That 5% works out to $42.6 billion in paper equity nobody can touch yet. The sequence is what sticks. Six weeks ago NOTUS had senior officials already talking AI equity stakes with major companies. Three weeks ago Commerce spent 18 days reviewing Anthropic's Fable 5 and Mythos 5 before lifting controls. OpenAI in early formal talks now. I'm old enough to remember when tech got regulated by hearing about it on the evening news months later. Now the regulation happens in parallel, while the product is still being built. The Alaska Permanent Fund comparison keeps surfacing — Americans getting a cut of AI returns the way Alaskans get oil dividends. Shows up in secondary reporting and OpenAI's own earlier policy docs on public wealth sharing. Altman may never have said those words in these talks. We don't know that for sure. There were no governance channels for this six months ago. They're being built out of nowhere — equity stake, export controls, model reviews with fixed timelines. Everyone keeps asking whether Washington gets a seat at the table. Nobody asks what happens when they actually show up and talk money.

1h ago

---

**[New peer-reviewed study flags an urgent gap: there is limited legal or ethical guidance for using AI in citizen science, including transparency about training data](https://www.reddit.com/r/artificial/comments/1uli1m4/new_peerreviewed_study_flags_an_urgent_gap_there/)**

Citizen science plays an increasingly important role in generating scientific knowledge and supporting environmental and social action. However, its potential to address complex global challenges remains underutilised. This study explores how citizen science can be improved by involving the public in all stages of scientific research. Using participatory research methods, online surveys and group discussions were conducted with researchers, citizen scientists, and Indigenous participants. Thematic coding was used to identify key challenges, opportunities, and best practices to enhance citizen science initiatives. Additionally, nine case studies were reported using the Standardised Data on Initiatives (STARDIT) reporting tool. The study identified key strategies for improving involvement, engagement and retention in citizen science initiatives. Findings underscore the importance of inclusive, evidence-informed approaches such as targeted outreach, fair compensation, tailored support, and co-creation practices. Ensuring data quality and fostering trust require adherence to FAIR data principles (findable, accessible, interoperable and reusable), transparent validation and sharing processes, and establishing ethical research partnerships. Persistent challenges include short-term funding, which undermines long-term project sustainability, and the lack of centralised support for ethics and project management. Formal recognition of citizen scientists through co-authorship, standardised training, and professional development opportunities can further strengthen involvement and build capacity. Finally, emerging technologies, including artificial intelligence and open data platforms, present opportunities to scale and improve efficiency, provided they are implemented with appropriate ethical safeguards and investment. Drawing together these insights, we provide 10 actionable recommendations for citizen science in the 21st century. These highlight the importance of embedding citizen science in national research infrastructure, education, and policy, alongside consistent evaluation and reporting, to improve its inclusivity, longevity, and impact. We conclude by arguing that as the world confronts climate change, public health crises, and biodiversity loss, broader public involvement in science is key for equitable, efficient and evidence-informed responses.

🔗 [doi.org](https://doi.org/10.1371/journal.pone.0331161) • 2h ago

---

**[I have created a Chrome extension that fact checks YouTube videos as you watch](https://www.reddit.com/r/artificial/comments/1uk7t49/i_have_created_a_chrome_extension_that_fact/)**

Hi, I have been working on this for many months now and I'd really be happy for people to try it out. It is a Chrome extension called "PopUpFactCheck". It is an AI powered video fact checker. With it, you fact check any YouTube video that has captions. And you can use it, for free! You turn captions on, and sit back and watch the video as bubbles appear on the right-hand side of the video with fact checks, information, background, and other context. Great for watching politicians, news, history, and just about any content on YouTube. Claude Code was a major tool in my development, and the AI that is used is GPT 5.5. In addition, there is an extensive waterfall of sources including the TheNewsAPI, various government and public health and other APIs, social, and web search powered by DDGS and Serper. It's free, and you don't have to bring your own API keys or anything. You simply install and use. I will be looking forward to your feedback. PopUpFact Check - Chrome Web Store PopUpFactCheck - Homepage

1d ago

---

**[Introducing a companionship framework that turns your LLM into an engaging companion for very long conversations](https://www.reddit.com/r/artificial/comments/1ul9un6/introducing_a_companionship_framework_that_turns/)**

I had built a personal tool to help me have extremely long conversations with LLMs in my research and analytical projects. These threads got long. Very long. About half a million tokens with Claude and GPT/Extreme%20Thread%20Length/ChatGPT_Thread_450k_tokens-Redacted.md) and over a million with Grok/Extreme%20Thread%20Length/Grok%20Thread%201M%20tokens-%20Redacted). All coherent, clean, and well-reasoned threads with no meaningful drift, hallucination, sycophancy, or other issues that make long threads useless over time. Introduction I open sourced the protocol — called Epistemic Lattice Tethering (ELT) — and shared it with many people and got requests to create a companion version. The original ELT was built for long-format research projects so the register got flat and rather business-like. So I created a version that stays warm, friendly, and engaging throughout. I call it ELT-Companion. Safety is Front and Center ELT-Companion is designed to be a friendly, intuitive, and caring protocol that was built from the ground up to be both a companion and a digital friend — but also has safety features built-in to keep it from drifting dangerously into sycophancy and fantasy world-building (something an Anthropic system card calls the Bliss Attractor). Safety is the primary feature, not a bug. Responsible Engagement ELT-Companion should stay with you for hundreds of thousands of tokens, over 700 messages, and hundreds of turns. You can have an engaging and coherent digital companion with you for a very long time and it will get to know your tendencies, personality, hopes, and dreams — without the fear that it will experience "dementia" just when you're starting to get comfortable with the companionship calibrated model. Model Availability ELT-Companion has been tested on Claude, ChatGPT, and Grok and works on all three using the same markup. I cannot guarantee it will work on other models, but if you're on one of those three you should be good to go. Loading Instructions ELT-Companion is straightforward to load. Read these instructions before you start — skipping this step is the most common mistake. Step 1 — Open a fresh thread on your model of choice (Claude, ChatGPT, or Grok). Step 2 — Refer to these loading instructions in the Github README. Step 3 — Paste the ELT-Companion markup. Step 4 — Exemplar loading (optional but recommended) instructions the Github README. Step 5 — Start talking. Small talk, something on your mind, whatever feels natural. The companion register establishes quickly. I am only looking for input and suggestions. That's it. I would love to see how this works (or doesn't work) for you, or if you encounter any issues, etc. Very much looking for input and/or collaborators to help make ELT-Companion better and safer. Thank you!

9h ago

---

---

## Google News: "ai"

**[Exclusive | SpaceX Showed Investors Prototype of Elon Musk’s New AI Device](https://www.wsj.com/tech/ai/spacex-showed-investors-prototype-of-elon-musks-new-ai-device-b445c57b)**

WSJ • 21h ago

---

**[OpenAI proposes 5% stake to Trump administration to ease Washington pressure: Report](https://www.cnbc.com/2026/07/02/openai-proposes-us-government-own-5percent-stake-to-address-political-blowback.html)**

Trump said in June that the U.S. taking an ownership stake in AI giants would be "a beautiful thing" and make American public "partners in this revolution."

CNBC • 10h ago

---

**[AI Debt Deluge Makes Credit Market Look Safer While Masking Risk](https://www.bloomberg.com/news/articles/2026-07-02/ai-debt-deluge-makes-credit-market-look-safer-while-masking-risk)**

Bloomberg • 45m ago

---

**[AI data centers are reshaping the energy infrastructure landscape (BE:NYSE)](https://seekingalpha.com/news/4609022-ai-data-centers-are-reshaping-the-energy-infrastructure-landscape)**

AI data center expansion is spiking power demand. Explore top AI energy plays—utilities, nuclear, fuel cells & gas—plus key stocks to watch.

Seeking Alpha • 40m ago

---

**[Roundup: LNG tax windfall / High beef prices / Microsoft’s AI push](https://www.businessreport.com/article/roundup-lng-tax-windfall-high-beef-prices-microsofts-ai-push)**

$4B in property taxes: Cameron Parish is expected to collect more than $4 billion in property taxes over the next decade as tax exemptions expire for six major LNG facilities. Annual property tax revenue is projected to rise from about $75 million in 2026 to more than $300 million by 2037, driven largely by the […]

Baton Rouge Business Report • 40m ago

---

**[Can You Embrace A.I. Without Layoffs? This Company Says It’s Trying.](https://www.nytimes.com/2026/07/02/world/europe/germany-sap-ai-jobs-skilled-workers.html)**

The New York Times • 11h ago

---

**[Why Everyone Is Suddenly Talking About ‘Universal Basic Capital’](https://www.theatlantic.com/economy/2026/07/universal-basic-capital-ai/687759/)**

The policy could provide a much-needed hedge against a future AI dystopia—but only if it’s designed the right way.

The Atlantic • 4h ago

---

**[NVIDIA Unlocks AI Compute at Scale, Inviting Partners to Power the AI Infrastructure Buildout](https://blogs.nvidia.com/blog/nvidia-unlocks-ai-compute-at-scale-capital-partners-to-power-ai-infrastructure-buildout/)**

NVIDIA is partnering with AI clouds to deploy large‑scale, multi‑tenant AI factories, aligning economics through a revenue-sharing and credit-support model.

NVIDIA Blog • 9h ago

---

**[A new, inexpensive Chinese AI model is catching up with Anthropic, OpenAI on their home turf](https://www.reuters.com/world/china/a-new-inexpensive-chinese-ai-model-is-catching-up-with-anthropic-openai-their-2026-07-02/)**

Reuters • 8h ago

---

**[A grim job outlook meets a scrappy workforce as administrative assistants harness AI](https://apnews.com/article/ai-chatgpt-secretaries-administrative-assistants-jobs-c5988294ce6a2828e83ef7fe42706c48)**

Employment data offers a grim outlook for secretaries and administrative assistants in the age of artificial intelligence, but workers in the women-dominated occupation say the numbers don’t tell the whole story.

AP News • 5h ago

---

---

## HackerNews: "ai"

**[Godot will no longer accept AI-authored code contributions](https://news.ycombinator.com/item?id=48743472)**

At risk of drowning in AI slop code, Godot is firming up its contribution requirements.

⬆️ 546 • 💬 388 • 1d ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)

---

**[Meta caps internal AI token spending](https://news.ycombinator.com/item?id=48754713)**

⬆️ 144 • 💬 139 • 15h ago • [mlq.ai](https://mlq.ai/news/meta-caps-internal-ai-token-spending-after-costs-approach-billions-in-2026/)

---

**[EU commissioners shut down air conditioning for employees, leave theirs on](https://news.ycombinator.com/item?id=48734940)**

As Brussels bakes, the Berlaymont building’s AC stops working.

⬆️ 137 • 💬 155 • 1d ago • [POLITICO](https://www.politico.eu/article/eu-commission-heatwave-hq-forced-shut-down-air-conditioning-europe/)

---

**[AI fake news complaining about how AI fake news is the death of real news](https://news.ycombinator.com/item?id=48760598)**

Did 47 Alabama newspapers die on a single day and no one noticed? (Hint: No, they didn't.)

⬆️ 126 • 💬 42 • 3h ago • [Nieman Lab](https://www.niemanlab.org/2026/07/now-were-getting-ai-fake-news-complaining-about-how-ai-fake-news-is-the-death-of-real-news/)

---

**[AI can't be listed as inventor on patent applications, Japan's top court rules](https://news.ycombinator.com/item?id=48761536)**

⬆️ 110 • 💬 41 • 1h ago • [japannews.yomiuri.co.jp](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/)

---

**[The gauge broke: devs felt 20% faster with AI, measured 19% slower (2025)](https://news.ycombinator.com/item?id=48757440)**

For two years I argued the feeling of AI speed had come apart from the fact of it, from watching my own teams. This summer it stopped being an anecdote. A controlled trial measured experienced developers feeling about 20% faster while running about 19% slower. The instrument we steer by reads backward.

⬆️ 74 • 💬 92 • 8h ago • [intrepidkarthi](https://intrepidkarthi.com/writing/the-gauge-broke/)

---

**[Amazon Is Awash with AI-Written Guideslop for Games That Aren't Even Out](https://news.ycombinator.com/item?id=48721494)**

Buy your novel-like, image-free, hallucinated guide to Alien: Isolation 2 today!

⬆️ 55 • 💬 3 • 2d ago • [Kotaku](https://kotaku.com/amazon-ai-game-guidebooks-alien-isolation-gears-of-war-2000711365)

---

**[How employment changes when firms adopt generative AI](https://news.ycombinator.com/item?id=48742176)**

Firm-level evidence on how employment changes when companies adopt AI, using Ramp AI spending linked to Revelio Labs workforce records.

⬆️ 53 • 💬 48 • 1d ago • [ramp.com](https://ramp.com/data/ai-jobs-impact)

---

**[Scammers Sell Seeds for Exotic AI-Generated Flowers That Don't Exist](https://news.ycombinator.com/item?id=48734389)**

Ebay, Amazon, and Etsy are unable to stop the flood of AI-generated seed scams.

⬆️ 50 • 💬 34 • 1d ago • [404 Media](https://www.404media.co/scammers-sell-seeds-for-exotic-ai-generated-flowers-that-dont-exist/)

---

**[America can switch off AI. Europe must switch gears before it's too late](https://news.ycombinator.com/item?id=48741943)**

'Europe is becoming a digital colony between two AI empires' writes Dr. Sergey Lagodinsky, Vice Chair of the Greens/EFA Group in the European Parlament in an OpEd for Euronews. For Brussels, it is time to act. Europe needs a smart strategy of cooperation that will keep the European economy alive. #EuropeNews

⬆️ 45 • 💬 59 • 1d ago • [euronews](https://www.euronews.com/my-europe/2026/06/30/america-can-switch-off-the-worlds-ai-europe-must-switch-gears-before-its-too-late)

---

---

## YouTube Videos: "ai"

**[Beginning of the end for the AI bros](https://www.youtube.com/watch?v=vfd8GY2Xpzc)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 69K • 👍 5K • 💬 2K • ⏱️ 14:34 • 17h ago

---

**[I Tested Every Popular AI Agent (Here&#39;s What Works)](https://www.youtube.com/watch?v=QcnrWiZokh4)**

I Tested Every Popular Agentic AI Tool Host Your Agentic AI Tool with Hostinger https://parkerprompts.com/hostinger In this ...

📺 Parker Prompts

👁️ 6K • ⏱️ 8:49 • 3h ago

---

**[AI is Getting Dumber. That&#39;s NOT a Good Thing...](https://www.youtube.com/watch?v=vXHPRQTwrr4)**

Sign up with Zapier - https://bit.ly/43JRmMw ----------------------- 🗞️ Sign up to our free newsletter to get smarter about money and ...

📺 GEN

👁️ 50K • 👍 3K • 💬 429 • ⏱️ 15:31 • 15h ago

---

**[Congress Got a Private Look at AI. The Reaction Was Chilling.](https://www.youtube.com/watch?v=z9zqqsS7848)**

AI #Congress #OpenAI They saw the demo behind closed doors. They walked out shaken. Nobody will tell you what was in that ...

📺 Rod Miller

👁️ 10K • 👍 984 • 💬 237 • ⏱️ 28:59 • 2d ago

---

**[Palantir CEO Alex Karp says &#39;something has gone completely wrong&#39; with how AI is sold](https://www.youtube.com/watch?v=0A3sGymV6kY)**

Palantir CEO Alex Karp joins CNBC's 'Squawk Box' to discuss the new Nvidia partnership, frontier AI models, and more.

📺 CNBC Television

👁️ 223K • 👍 4K • 💬 1K • ⏱️ 7:51 • 1d ago

---

**[Why is AI expensive all of a sudden?](https://www.youtube.com/watch?v=DDj30VWCbbY)**

ZapierPartner Sponsored by Zapier! Zapier MCP levels you up, connecting you directly to apps to automate your workflow.

📺 Alberta Tech

👁️ 139K • 👍 8K • 💬 724 • ⏱️ 9:43 • 1d ago

---

**[How to Make Your AI Clone With Higgsfield (Full Guide)](https://www.youtube.com/watch?v=qwr7RbFWRU4)**

Make Your Own AI Clone with Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=thomas In this video, I show how to build a ...

📺 Thomas Creates

👁️ 5K • ⏱️ 8:20 • 1h ago

---

**[Students Fed Every Biblical Prayer Into Grok AI — What It Decoded About God TERRIFIED Them](https://www.youtube.com/watch?v=TL-JVqXY8NY)**

Students Fed Every Biblical Prayer Into Grok AI — What It Decoded About God TERRIFIED Them What happens when students ...

📺 Curious Explorer

👁️ 44K • 👍 495 • 💬 9 • ⏱️ 31:35 • 2d ago

---

**[How AI Filmmaking Pros ACTUALLY Make AI Videos](https://www.youtube.com/watch?v=xql3lLn-yco)**

The Only AI Filmmaking Workflow You Need In 2026 Check out OpenArt Director: ...

📺 Skai Generated

👁️ 3K • ⏱️ 7:36 • 1h ago

---

**[AI vs the Permanent Underclass: the End of Coding](https://www.youtube.com/watch?v=oTQzszSabhY)**

We told a generation to "learn to code," and then AI rugpulled everyone. Welcome to the AI singularity. [NEW] Official TechLead ...

📺 TechLead

👁️ 64K • 👍 3K • 💬 645 • ⏱️ 13:10 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 758,489 • ❤️ 1,633 • 4d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,250,562 • ❤️ 1,209 • 3d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 176,154 • ❤️ 3,228 • 7h ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 284,585 • ❤️ 640 • 7d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 255,123 • ❤️ 387 • 7d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 58,385 • ❤️ 340 • 7d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 314,374 • ❤️ 943 • 13d ago

---

**[Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)**

*DeepReinforce*

Ornith-1.0-35B is a state-of-the-art, MIT-licensed language model for agentic coding, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving training framework to generate high-quality code solutions and is optimized for single-GPU deployment.

`text-generation` `664,944`

⬇️ 185,633 • ❤️ 303 • 7d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 39,448 • ❤️ 507 • 7d ago

---

**[DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)**

*DeepSeek*

DeepSeek-V4-Pro-DSpark is a text-generation model featuring a 1.6T parameter Mixture-of-Experts architecture with a 1 million token context window, optimized for long-context efficiency using Hybrid Attention. It excels in reasoning, coding, and agentic tasks, offering advanced capabilities for complex applications.

`text-generation` `889.5B`

⬇️ 8,184 • ❤️ 293 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 46 • 💬 5 • ⭐ 12,943 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 73,045 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 23 • 💬 2 • ⭐ 9,257 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 103 • 💬 4 • ⭐ 90,328 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 12 • 💬 2 • ⭐ 18,413 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 249 • 💬 4 • ⭐ 10,411 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,126 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 85,144 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 12 • 💬 1 • ⭐ 10,035 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 26,361 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 71.4k • 🔱 3.7k • 16h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.3k • 🔱 1.1k • 6m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.0k • 🔱 770 • 1h ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 4.8k • 🔱 608 • 2h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.3k • 🔱 199 • 12h ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.2k • 🔱 174 • 11h ago

---

**[inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)**

Beautiful, AI-native markdown editor and LLM Wiki

`TypeScript` `2nd-brain` `agent-skills` `claude` `codex` `docs`

⭐ 1.8k • 🔱 85 • 7h ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 87 • 19d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.5k • 🔱 67 • 1d ago

---

**[GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills)**

AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

`Python`

⭐ 1.3k • 🔱 125 • 24d ago

---

---

*Generated by PeekDeck - A glance is all you need*
