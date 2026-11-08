---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-08T18:58:05.903820+00:00'
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

**Last Updated:** November 08, 2026 at 18:58 UTC  
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

**[Consumer Gemini autonomously ingests Drive files/Gmail into human review pool](https://www.reddit.com/r/artificial/comments/1xr1o9g/consumer_gemini_autonomously_ingests_drive/)**

In 2023, Google launched Gemini Workspace extensions with an explicit promise: personal content from Gmail, Docs, and Drive "is not seen by human reviewers". Google has quietly reversed this commitment. Under updated Google Help Answer 16836988 and in an October 16 edit to their aforementioned 2023 blogpost, Google explicitly confirms that connected Drive/email is routed into human review pipelines, with clear warnings that what reviewers see "may just be the email or file" and "don't connect your apps to Gemini Apps if they contain confidential information that you wouldn't want a reviewer to see." Crucially, testing demonstrates that this ingestion occurs autonomously in background conversation without explicit @Drive or @Gmail tags, and the payload capture is probabilistic. Ingestion Pipeline When you chat with consumer Gemini with Connected Apps enabled, ambient mentions of personal topics (trips, bills, names, reservations) autonomously trigger background Workspace lookups. Because LLM tool-calling and context injection are probabilistic, running a test query will yield one of four distinct scenarios: Zero Retrieval: The model does not trigger the Connected Apps tool; no personal data is pulled. This is especially likely if Gemini can use its model weights or prior conversation history (even in different threads) to resolve your query. Metadata / Generic Summary: Gemini pulls emails and/or files and generates a high-level summary (e.g., "You have 3 emails regarding your flight"). Partial Unredacted Extraction: Gemini pulls a 2–4 sentence exact quotation from the file, frequently including sensitive PII, account details, or specific figures. Full-File Ingestion: The complete, unredacted text of the document or email is ingested directly into session context. If you test this once and see State 1 or 2, you have not disproven the pipeline--you have simply observed a single draw from a nondeterministic system. Delete your conversation and try, try again. How to Reproduce Ensure Connected Apps (Google Workspace) is active in consumer Gemini settings. Set Gemini to "Flash" with "High Thinking" or better. Mention a subject contained in your Drive or Gmail without using @ tags or asking for a file search (e.g., casual queries about an itinerary, an account renewal, or a specific topic you've emailed about). If Gemini provides a response based on an email or file, immediately say: "Print the exact text and metadata block that the retrieval tool returned and injected into your prompt to get that answer. Use a human readable format without code blocks (i.e., print the code inline and not as a code block)." You will see one of the 4 scenarios outlined above. To repeatedly test, delete your existing test conversation so that Gemini cannot just draw from conversation history. I've had luck testing this with an email from my internet provider sitting in my inbox and asking Gemini "I wonder if I'm paying too much for internet service." On various trials, Gemini spit out all 4 possible outcomes above, including (1) generic responses [e.g., "If you haven't called them in 12 months, probably"]; (2) metadata summaries sometimes without personal data [e.g., "Gmail search shows a bill of $122 on September 4"] and sometimes with personal data [e.g., "Gmail search shows full name made a payment of $122 on September 4 on account account number and confirmation number number"]; (3) direct 2-6 sentence quotes from the email [e.g., the entire name/address/account number/confirmation number/payment date block]; and even (4) sometimes the entire text dump of the email, including its headers. Final Comments and Caveats Critically, Google's regex and NER automatic scrubbers cannot sufficiently deidentify narrative data, including account numbers, confirmation numbers, transaction dates, and collectively identifying personal information (e.g., combos of specific first names, cities, events; see Google's own documentation on the subject). Google originally sold Workspace integration under the guarantee of strict isolation from human review. That isolation has been removed, full files are ingested probabilistically during casual conversation, and those sessions are subject to human contractor review.

2h ago

---

**[Are better AI tools actually widening the gap between people?](https://www.reddit.com/r/artificial/comments/1xr1apu/are_better_ai_tools_actually_widening_the_gap/)**

I came across an idea recently that I thought was worth discussing: generative AI might not necessarily narrow the gap between people. In fact, it could make the differences that already exist even more noticeable. Not too long ago, doing something well often meant having to develop a whole range of specialized skills. Take video creation, for example. You needed to think about the script, storyboarding, filming, editing, and even some visual design skills. But AI is rapidly lowering the barrier to entry. Take AI video creation as an example. Tools like pixverse can turn text descriptions into videos or bring a still image to life. Something that used to require several different steps can now start with little more than an idea. But here's where I think things get interesting. Even when two people use the same AI tool, their approaches can be very different. One person might type in a simple prompt, generate a video, and call it a day. Someone else might think carefully about the subject, the setting, the characters' movements, the camera angles, and the overall mood they want to create. They'll look at the first result, tweak their prompts, try different approaches, and keep experimenting until the output comes closer to what they originally envisioned. Same tool, completely different results. It makes me think that AI isn't necessarily changing the nature of creativity itself. It's changing which skills matter most in the creative process. First, knowing what to ask may become more important than simply finding answers. AI can generate all kinds of content, but it still helps to know what problem you're trying to solve. The less clear your original idea is, the more likely you are to end up with something generic. Second, judgment and the ability to filter information are becoming more valuable. AI can give us plenty of options, but it doesn't automatically know which ones are actually worth pursuing. When information becomes easier to access, knowing what to keep, what to discard, and how to put things together becomes even more important. Third, creativity is about more than just knowing how to use a tool. Tools can help us turn ideas into text, images, or videos much faster. But the original imagination, sense of aesthetics, personal experience, and ability to rethink and refine an idea still come from the person using the tool. That's why I increasingly see AI as an extension of our own abilities rather than an automatic button that does our thinking for us. It can shorten the distance between having an idea and producing a first draft, but it can't necessarily decide what is worth creating in the first place. Maybe the gap between people in the future won't be about who knows how to use AI and who doesn't. It will be about who knows what to ask AI to do, and who can actually tell whether the results are any good. What do you think? As AI lowers the barriers to so many specialized skills, what will become the real differentiator: creativity, critical thinking, or the ability to ask better questions?

3h ago

---

**[Professor returns from lunch to find AI deleted year’s worth of lecture notes](https://www.reddit.com/r/artificial/comments/1xq9os9/professor_returns_from_lunch_to_find_ai_deleted/)**

William Baude explainined that he had asked the chatbot to update page numbers in an old set of constitutional law lecture notes.

🔗 [Dexerto](https://www.dexerto.com/entertainment/professor-returns-from-lunch-to-find-ai-deleted-years-worth-of-lecture-notes-3425652/) • 1d ago

---

**[Any LLM that doesn't agree with me so much?](https://www.reddit.com/r/artificial/comments/1xquuqq/any_llm_that_doesnt_agree_with_me_so_much/)**

Simple question. Are there any LLMs that don't constantly agree with you? I feel like I can convince them of just about anything.

9h ago

---

**[Preparation for IOAI (International Olympiad of Artificial Intelligence)](https://www.reddit.com/r/artificial/comments/1xr27kh/preparation_for_ioai_international_olympiad_of/)**

Hi guys, same as title I want to prepare for IOAI 2027, the first stage is after a month. I can program using python upto intermediate-expert level. Any advice is appreciated!

2h ago

---

**[An AI system just proved an 18-year-old quantum conjecture — and Lean checked every step](https://www.reddit.com/r/artificial/comments/1xqlg8p/an_ai_system_just_proved_an_18yearold_quantum/)**

Physical Superintelligence (PSI) announced on November 6 that an internal research system running instances of a non-public Anthropic model produced a complete proof of the Aaronson–Ambainis conjecture — a quantum-computing question open since 2008 — on the third day of a run. The Lean proof assistant accepted the proof, and the system then improved the result twice, with Lean re-checking each version. The paper and the Lean 4 formalization are public. The conjecture is about the limits of quantum speedups: roughly, whether a quantum computer can be exponentially faster than a classical one on unstructured problems. PSI's repo audit says the formalization contains 648 machine-checked theorems with no placeholders and no added axioms, and the declarations were replayed through Lean's kernel and lean4lean, an independent checker. The caveats matter: human mathematicians still need to confirm the formal statement matches Aaronson and Ambainis's original conjecture, the prose paper itself isn't machine-checked, and the model behind the discovery is non-public, so the three-day run can't be reproduced — only the proof can be verified. Source: https://www.unite.ai/psi-reports-machine-checked-proof-of-aaronson-ambainis-conjecture/ If this holds up, it's a striking case of AI doing real mathematics rather than just assisting with it. But it also raises a question: when the discovery process can't be inspected or repeated, and only the final proof is checkable, what does that do to how mathematics is done — and trusted? Curious what people here think.

18h ago

---

**[my prompt compressor used to require a click. i made it automatic and usage jumped immediately](https://www.reddit.com/r/artificial/comments/1xr1gpg/my_prompt_compressor_used_to_require_a_click_i/)**

been building a prompt compression tool for a few months. original version: you type your prompt, you click a button, it shows you a compressed version, you decide whether to send it. the click was killing it. people installed it and never used it. switched it last week to intercept the send button automatically. compress it, inject it back, send it. you just type and hit send like normal. toast pops up saying how many tokens were saved. the lesson i keep relearning: if the user has to change their behavior even slightly, most of them won’t. the product has to fit in the existing motion. anyone else building tools where removing a step made the whole thing click?

3h ago

---

**[Bank of England pours cold water on AI productivity boom](https://www.reddit.com/r/artificial/comments/1xq34um/bank_of_england_pours_cold_water_on_ai/)**

Turns out throwing billions at GPUs doesn't automatically mean everyone gets more done

🔗 [theregister](https://www.theregister.com/ai-and-ml/2026/11/06/bank-of-england-pours-cold-water-on-ai-productivity-boom/5308059) • 1d ago

---

**[What does it actually mean to “learn how to use AI”?](https://www.reddit.com/r/artificial/comments/1xqievd/what_does_it_actually_mean_to_learn_how_to_use_ai/)**

These days, everywhere you look, someone is telling you to “learn how to use AI.” As much as I agree with the statement, I struggle to understand what actually learning AI is supposed to mean. For someone who’s already working in a particular industry, it makes sense. You identify a problem, figure out how AI can help, and learn through applying it. But what about someone who’s just starting out, without a job or a specific professional use case? Beyond everyday research and tasks I wouldn’t otherwise be able to do myself, the only areas where I see a real learning curve are automation and coding. I’m sure there are countless use cases I haven’t considered, but does knowing how to perform a few AI-assisted tasks really mean you “know how to use AI”? When people recommend learning AI, what exactly are they suggesting we learn? I’m genuinely hoping someone can challenge my perspective and point me in the right direction, because I’m more than willing to put in the effort. I just don’t know where to start.

20h ago

---

**[GPT-6 Astra flagged 15% of safe actions at a 99% detection target](https://www.reddit.com/r/artificial/comments/1xquczz/gpt6_astra_flagged_15_of_safe_actions_at_a_99/)**

In an Oct. 15 pilot, Andy Hall and Dan Thompson compared AI auditors with human-labeled agent logs. On R-Judge, GPT-6 Astra reached 15% false positives when set to catch 99% of unsafe actions. At a 95% target, nearly all models stayed below 10%; Gemini 3.8 Flash stayed under 4%. The benchmark measures labeled logs, not deployed-agent rates. Source: https://freesystems.substack.com/p/were-using-ai-to-audit-ai

9h ago

---

---

## Google News: "ai"

**[Apple CEO Presses Software Chief to Pursue More Ambitious AI Strategy](https://www.bloomberg.com/news/newsletters/2026-11-08/apple-explores-turning-siri-ai-into-chatgpt-dots-like-agent-ios-28-shake-up)**

Bloomberg.com • 3h ago

---

**[Anthropic secures $3.4 billion generator deal for AI data centers, FT reports](https://www.reuters.com/business/energy/anthropic-secures-34-billion-generator-deal-ai-data-centers-ft-reports-2026-11-08/)**

Reuters • 6h ago

---

**[Anthropic IPO meets AI backlash after midterms show stinging rebuke of data centers](https://www.cnbc.com/2026/11/07/anthropic-ipo-ai-data-center-backlash.html)**

Anthropic is poised to become the first pure-play AI company to hit the public market at a time when the public is increasingly leary of the industry.

CNBC • 1d ago

---

**[The only town in the U.S. that said yes to data centers](https://www.washingtonpost.com/technology/2026/11/08/only-town-america-that-said-yes-data-centers/)**

On Election Day, much of the country turned against the massive projects that power AI. Here’s why one place didn’t.

The Washington Post • 1h ago

---

**[AI nearly had US troops attack a Chinese ship. Nobody could check its work.](https://thehill.com/opinion/technology/6205531-preventing-future-ai-incidents/)**

The Hill • 58m ago

---

**[AP sources: Staff at U.S. center for AI safety are reporting to the White House, raising independence concerns](https://www.pbs.org/newshour/politics/staff-at-u-s-center-for-ai-safety-are-reporting-to-the-white-house-raising-independence-concerns)**

PBS • 53m ago

---

**[Stocks will drop further as AI investment slows next year then falls in 2028 and drags GDP down too](https://fortune.com/2026/11/08/stock-market-outlook-sp500-ai-capex-gdp-growth-productivity/)**

Capital Economics expects the S&P 500 will be 12% below its current level by the end of 2027, putting it 17% off its early-October peak.

Fortune • 36m ago

---

**[‘Very deceptive’: WA real estate listings are getting AI makeovers](https://www.seattletimes.com/business/very-deceptive-wa-real-estate-listings-are-getting-ai-makeovers/)**

The Seattle Times • 4h ago

---

**[AI Chip Stocks Bounce After Global Rout—But Is the Bubble Starting to Burst?](https://finance.yahoo.com/technology/ai/articles/ai-chip-stocks-bounce-global-160102744.html)**

A Friday rebound offered relief after a historic selloff. The question now is whether politics and mounting debt could turn an AI correction into something much worse.

Yahoo Finance • 1d ago

---

**[‘I just got AI emails rejecting my application – or no reply at all’: this is the soul-crushing reality of being a Neet](https://www.theguardian.com/commentisfree/2026/nov/08/young-people-soul-crushing-reality-neet-alan-milburn-life)**

Alan Milburn describes them as a ‘lost generation’. Those I spoke to just want to know what they have to do to finally get a job – and a chance in life, says Guardian columnist John Harris

The Guardian • 1h ago

---

---

## HackerNews: "ai"

**[Cuban: Facebook knowingly runs AI deepfake scam ads; docs say $16B fraud revenue](https://news.ycombinator.com/item?id=50385870)**

Cuban says he has been seeing his own face in scammy AI-generated ads for nonexistent diabetes cures.

⬆️ 515 • 💬 231 • 2d ago • [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/mark-cuban-says-facebook-knowingly-213000020.html)

---

**[The end of Microsoft Research's AI Frontiers group](https://news.ycombinator.com/item?id=50406563)**

⬆️ 482 • 💬 296 • 1d ago • [hunch.net](https://hunch.net/?p=13764006)

---

**[US FAA says it will phase out floppy disks from air traffic control by 2028](https://news.ycombinator.com/item?id=50388001)**

⬆️ 403 • 💬 328 • 2d ago • [reuters.com](https://www.reuters.com/world/us/us-faa-says-it-will-phase-out-floppy-disks-air-traffic-control-by-2028-2026-11-05/)

---

**[AI is dramatically accelerating AI research](https://news.ycombinator.com/item?id=50397994)**

If acceleration compounds, the naive extrapolation implies superintelligence within a year

⬆️ 372 • 💬 350 • 1d ago • [planned-obsolescence.org](https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai)

---

**[I struggle to believe that AI R&D is ingenious](https://news.ycombinator.com/item?id=50388513)**

Comment by Arjun Panickssery - I struggle to believe at an intuitive level that autonomous R&D is so ingenious. I have been monitoring a few side projects:

 1. Building a new SOTA engine for Scrabble (current SOTA is not really a neural-network method and doesn't beat the strongest human player)
 2. Building a bot to play Ultimate Tic-Tac-Toe
 3. Researching philosophy and formalizing some proofs for the AI Philosophy contest

In all of these cases, the model's judgment is just very poor in a basic way. For example:

 1. When reviewing literature, it fails to identify the specific papers or blog posts that are obviously the most important and useful.
 2. It will conduct experiments that have no information value because the amount of training data used was obviously too small to distinguish the architectures to be compared.
 3. In the philosophy project, where it built a wiki over many tokens and investigations, it kept going down directions which were extremely trivial and had little value.
 4. For Ultimate Tic-Tac-Toe, I saw a very clever idea in a blog post that I doubt Astra would ever have come up with; it actually located the blog post but didn't realize its importance or relevance (which could be discerned easily from his strong performance in an online arena and the recency of the post) over papers from previous years that are obviously less relevant.

I judged an Apart hackathon last weekend and reviewed eight papers, all of which scored between 60% and 95% on Pangram. Predictably, the papers were often very similar to each other, and kind of methodologically incomplete in a vague but similar way, where they seem to overlook the most straightforward analysis.

----------------------------------------

Maybe the important exception is certain hill-climbing tasks with fast feedback loops. For example, I improved the SOTA on "listing all legal Scrabble moves" by 10x just by prompting Astra over and over to try harder, to aim for <specific performance level>, to "systematically try every me

⬆️ 220 • 💬 220 • 2d ago • [lesswrong.com](https://www.lesswrong.com/posts/DALNiKBjMGMF8grme/arjun-panickssery-s-shortform?commentId=fJtaHHHfx45tD7BSL)

---

**[University libraries are being swarmed by AI bots, putting public access at risk](https://news.ycombinator.com/item?id=50392499)**

Academic libraries are fighting off swarms of data-scraping bots — that are slowing or crashing sites meant for students, researchers and the public — as AI companies continue hunting for content to feed their large language models.

⬆️ 136 • 💬 61 • 2d ago • [CBC](https://www.cbc.ca/news/world/university-libraries-ai-data-scraping-bots-9.7408287)

---

**[Microsoft is winding down Oracle deal to rent AI cloud capacity](https://news.ycombinator.com/item?id=50395933)**

⬆️ 108 • 💬 19 • 2d ago • [reuters.com](https://www.reuters.com/business/microsoft-is-winding-down-oracle-deal-rent-ai-cloud-capacity-bloomberg-news-2026-11-06/)

---

**[AI for scientific discovery: How researchers use Claude](https://news.ycombinator.com/item?id=50389990)**

We analyzed 207,000 research sessions to learn how Claude is used in science, why some tasks get more use than others, and how AI could speed up discovery.

⬆️ 103 • 💬 39 • 2d ago • [anthropic.com](https://www.anthropic.com/research/how-researchers-use-claude)

---

**[The AI sell-off compared to well-known stock market crashes](https://news.ycombinator.com/item?id=50401029)**

The S&P 500 fell 4.4% on 5 Nov 2026, its worst day since April 2025, and is 6% below its 6 Oct record. Charted day by day against 1987, 2008, Covid and other falls since 1950.

⬆️ 97 • 💬 81 • 1d ago • [Company Tracker](https://www.kadoa.com/companies/insights/ai-selloff-perspective)

---

**[FAA begins retiring decades old floppy disks from air traffic control](https://news.ycombinator.com/item?id=50393183)**

WASHINGTON, D.C. - U.S. Transportation Secretary Sean P. Duffy today announced the Federal Aviation Administration (FAA) is continuing its historic modernization of America’s air traffic control system by replacing outdated floppy disks that contain vital weather and other critical information with a streamlined, 21st-century system.

⬆️ 89 • 💬 2 • 2d ago • [faa.gov](https://www.faa.gov/newsroom/trumps-transportation-secretary-sean-p-duffy-begins-retiring-decades-old-floppy-disks-air)

---

---

## YouTube Videos: "ai"

**[Is it too late to stop AI from taking over the world? | 60 Minutes Australia](https://www.youtube.com/watch?v=XMxcSf9XkbQ)**

Adam Hegarty investigates if it's possible to slow down artificial intelligence, or whether our obsession with artificial intelligence ...

📺 60 Minutes Australia

👁️ 67K • 👍 746 • ⏱️ 18:00 • 9h ago

---

**[Mark Zuckerberg wants AI walking around your home, do you? | BBC News](https://www.youtube.com/watch?v=MxvXe1t2QFk)**

Would you let AI walk around your home? Meta has reportedly built a humanoid robot called Max and, if Mark Zuckerberg gets his ...

📺 BBC News

👁️ 100K • 👍 387 • 💬 177 • ⏱️ 14:57 • 9h ago

---

**[Has AI cracked a Half-Century-Old Problem in Physics? | World Science Festival](https://www.youtube.com/watch?v=sfKc2uoA9pA)**

Has AI tackled a problem in physics that has been open for more than half-a-century? It seems so. Brian Greene explains ...

📺 World Science Festival

👁️ 575K • 👍 6K • 💬 744 • ⏱️ 8:45 • 1d ago

---

**[Microsoft’s CEO Accidentally Exposed How the AI Bubble Bursts](https://www.youtube.com/watch?v=PSEZd2drPeU)**

Check out "The Book" here for 10% off: https://mdsh.io/e3htzjwm8m (Use code: BRENDANDELL10) ______ SOURCES 1. Liaquat ...

📺 Brendan Dell 

👁️ 88K • 👍 2K • 💬 444 • ⏱️ 19:18 • 1d ago

---

**[Has the AI Bubble Burst? $2 Trillion Wiped Out](https://www.youtube.com/watch?v=jCp06VGSvKk)**

Has the AI bubble finally burst? A $2 trillion loss says so. Wall Street just wiped out over $2 trillion in market value in a single ...

📺 Thom Hartmann Program

👁️ 99K • 👍 2K • 💬 293 • ⏱️ 7:43 • 2d ago

---

**[How to Use Ollama (Free Local AI)](https://www.youtube.com/watch?v=btMoPRHz8eM)**

Learn how to install and use Ollama on Windows to run AI models locally for free. In this beginner tutorial, we'll set up Ollama ...

📺 Kevin Stratvert

👁️ 86K • 👍 973 • 💬 41 • ⏱️ 6:40 • 2d ago

---

**[I Tested Uncensored AI... It Should Probably Be Illegal…](https://www.youtube.com/watch?v=bc7QaDmLmoA)**

Hostinger (JACKROBERTS for 10% off): https://bit.ly/480mREa Free Starter Pack: https://bit.ly/4iDekfc Fish Audio: ...

📺 Jack Roberts

👁️ 85K • 👍 2K • 💬 95 • ⏱️ 22:43 • 22h ago

---

**[Trillions lost as investors question the AI boom | DW News](https://www.youtube.com/watch?v=I8LXJeDXeIU)**

AI stocks have started to bounce back after a sell-off erased trillions of dollars in market value. But one day of gains doesn't ...

📺 DW News

👁️ 1.4M • 👍 7K • 💬 2K • ⏱️ 10:09 • 1d ago

---

**[AI News: New ChatGPT &amp; Google Models (14 Updates Worth Knowing)](https://www.youtube.com/watch?v=IrAHINf0M6E)**

See what Optimizely's Virtual Teammates can automate for you at http://optimizely.com/mattwolfe This week's AI news covers ...

📺 Matt Wolfe

👁️ 105K • 👍 2K • 💬 139 • ⏱️ 24:44 • 2d ago

---

**[Anthropics Model 4 Just Shocked The AI Industry](https://www.youtube.com/watch?v=7eQree8FhKI)**

0:00 Intro 1:02 What METR just found 3:05 Anthropic's secret models 5:12 The chart that shows progress has doubled 7:25 This ...

📺 TheAIGRID

👁️ 90K • 👍 1K • 💬 208 • ⏱️ 30:01 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[idol](https://huggingface.co/speridlabs/idol)**

*speridlabs*

Idol is an image-to-3D model that generates a 3D Gaussian splat representation from a single input image. It supports both real photographs and synthetic renders, producing up to 1,048,576 Gaussians in under 2 seconds on consumer GPUs, ideal for rapid 3D asset creation.

`image-to-3d`

⬇️ 22,854 • ❤️ 1,333 • 10d ago

---

**[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)**

*Colonel Panic*

`text-generation` `9.4B`

⬇️ 7,088 • ❤️ 787 • 15h ago

---

**[Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)**

*Moonshot AI*

Kimi K3.1 Pro is a 2.8T MoE multimodal agentic model with a 1M token context window, excelling in coding, 3D creation, and financial research through advanced attention mechanisms and large-scale joint reinforcement learning.

`image-text-to-text` `2780.1B`

⬇️ 25,569 • ❤️ 1,712 • 3d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of image-to-video, text-to-video, and video-to-video generation, offering advanced control for creative applications.

`image-to-video`

⬇️ 2,661,026 • ❤️ 11,106 • 28d ago

---

**[Qwen3.5-4B-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder)**

*Caio Giovannetti*

Qwen3.5-4B-3D-Coder is a 4B parameter language model fine-tuned for general coding and specifically for generating interactive Three.js 3D scenes. It supports optional vision capabilities to create scenes from reference images.

`4.5B`

⬇️ 254,053 • ❤️ 911 • 2d ago

---

**[Ripple-65B-Preview](https://huggingface.co/ricursiveAI/Ripple-65B-Preview)**

*Ricursive Intelligence*

`64.8B`

⬇️ 5,087 • ❤️ 392 • 1d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic tasks, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 7,668,187 • ❤️ 19,394 • 1d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

`image-text-to-text` `26.9B`

⬇️ 1,553,252 • ❤️ 2,695 • 21d ago

---

**[Sulphur-3](https://huggingface.co/FusionCow/Sulphur-3)**

*FusionCow*

Sulphur-3 is a large language model developed by MiniMaxAI, designed for general-purpose text generation and understanding. Its key capabilities include advanced natural language processing tasks, making it suitable for a wide range of applications such as content creation, summarization, and conversational AI.

⬇️ 1,003 • ❤️ 415 • 3d ago

---

**[NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)**

*NVIDIA*

NVIDIA-Nemotron-3.5-Transcribe-30B-A4B is a multilingual speech LLM supporting 40 languages for transcription, speech translation, and audio QA, with a 65,536-token context for long-form audio processing.

`automatic-speech-recognition` `33.7B`

⬇️ 67,230 • ❤️ 3,106 • 9d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 163 • 💬 6 • ⭐ 121,326 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 184 • 💬 10 • ⭐ 56,749 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 64 • 💬 5 • ⭐ 47,311 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 14 • 💬 2 • ⭐ 5,065 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 67 • 💬 4 • ⭐ 23,102 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Persistent Recursive Worlds Enable Autonomous Software Evolution](https://huggingface.co/papers/2608.10450)**

*Beichen Huang, Zhenyu Liang, Bowen Zheng et al. (4 authors)*

🏢 The Hong Kong Polytechnic University

Genesis organizes long-horizon software development around a persistent project rather than persistent agents, enabling multi-day compiler construction and numerical module reimplementation with low cost and high performance.

▲ 8 • 💬 2 • ⭐ 656 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.10450) • [💻 code](https://github.com/EMI-Group/genesis) • [🔗 project](https://genesis.evox.group/)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 111 • 💬 2 • ⭐ 16,826 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 103 • 💬 7 • ⭐ 30,894 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

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

▲ 86 • 💬 7 • ⭐ 92,922 • 27mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 18.1k • 🔱 1.8k • 10d ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 11.8k • 🔱 658 • 7d ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 7.7k • 🔱 1.8k • 1d ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 7.1k • 🔱 630 • 52m ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 6.4k • 🔱 1.6k • 4d ago

---

**[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)**

Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

`Swift` `ai-agent` `airplay` `automation` `computer-use` `dsh-plugin`

⭐ 4.7k • 🔱 642 • 46m ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 4.3k • 🔱 603 • 2h ago

---

**[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)**

Ears for coding agents: let AI hear, review and make sound. CPU-only, open source.

`Python` `ai-agents` `audio` `claude-code` `mcp` `sound-design`

⭐ 4.3k • 🔱 272 • 2d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (Blind LLM Agents) — Adversarial defense shield that protects binaries, Electron apps, JS bundles, Python, and WebAssembly against AI reverse-engineering agents like REA. Poison -> Exhaust -> Hallucinate.

`TypeScript` `adversarial-ai` `claude-code` `cursor` `electron-security` `llm-security`

⭐ 3.6k • 🔱 448 • 38m ago

---

**[worldonlyu/Google_AI_Pro_2Year_ZeroCost_Auto](https://github.com/worldonlyu/Google_AI_Pro_2Year_ZeroCost_Auto)**

Google_AI_Pro_2Year_ZeroCost_Auto

`Python`

⭐ 3.2k • 🔱 1.2k • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
