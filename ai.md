---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-18T23:47:40.333266+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 18, 2026 at 23:47 UTC  
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

**[Sainsbury’s pauses AI facial recognition after wrongful shoplifting accusation](https://www.reddit.com/r/artificial/comments/1vrqj9f/sainsburys_pauses_ai_facial_recognition_after/)**

UK supermarket Sainsbury's has temporarily stopped its use of AI facial recognition in one of its London stores after a customer was wrongly identified as a shoplifter and asked to leave. The retailer said the incident at an East Dulwich branch was caused by "human error", but it has suspended the technology at that store while it investigates. Sainsbury's will continue rolling out facial recognition technology across other stores. Earlier this year, Sainsbury's announced plans to expand its use of the technology to help "keep people safe", citing positive results from initial trials.

🔗 [LinkedIn](https://www.linkedin.com/news/story/sainsburys-store-pauses-ai-scan-7515420/?utm_source=share&utm_campaign=reddit&utm_content=storyline&utm_term=subreddit) • 9h ago

---

**[At what point does AI automation actually save time instead of creating more work?](https://www.reddit.com/r/artificial/comments/1vs2zmc/at_what_point_does_ai_automation_actually_save/)**

I've started wondering about this because sometimes I’m not sure whether I’m automating a task or just creating another task for myself. Set up the workflow. Connect everything. Fix it when something goes wrong. Check what it did. Then check it again because you don't fully trust it yet. At that point, I’m thinking... was this actually faster? Maybe I'm looking at it the wrong way, but I feel like there's a big difference between AI doing something for you and AI actually taking something off your plate. For those of you actually using AI automation, what has been worth it for you? And what's one automation you ended up getting rid of because it created more work than it saved?

2h ago

---

**[Chinese AI models are getting good enough to replace tools I actually pay for-is anyone else switching?](https://www.reddit.com/r/artificial/comments/1vrhy7t/chinese_ai_models_are_getting_good_enough_to/)**

The cost calculus for small builders is shifting faster than I expected. A few months ago, using a cheaper Chinese model felt like a tradeoff: you saved money but got noticeably worse output. That gap is closing, and in some cases it has closed entirely. I've been running the same prompts through DeepSeek and a couple others against what I was using before, and the difference for practical tasks like summarizing customer feedback, drafting copy, and generating boilerplate is small enough that I'm having a hard time justifying the price difference. The harder part to reason about is trust and data handling. For a hobbyist project it barely matters. For anything touching user data it matters a lot, and the answers there are murky. What I keep coming back to is that the cost compression is happening at the model layer, and that changes the math for anyone building on top of these APIs. Curious whether people here have actually switched any of their regular workflows over, or are still treating the cheaper options as secondtier.

16h ago

---

**[Companies should be required to disclose they are using an AI chatbot, currently they program the chatbots to avoid replying "yes, this is an AI chatbot"](https://www.reddit.com/r/artificial/comments/1vrjkns/companies_should_be_required_to_disclose_they_are/)**

14h ago

---

**[Is Claude experiencing another widespread outage right now?](https://www.reddit.com/r/artificial/comments/1vrzqys/is_claude_experiencing_another_widespread_outage/)**

Anyone else having trouble with Claude right now ? Is this widespread, or just me?

4h ago

---

**[Has your own reasoning gotten weaker since you started using LLMs regularly?](https://www.reddit.com/r/artificial/comments/1vrv8z1/has_your_own_reasoning_gotten_weaker_since_you/)**

Since using LLMs daily I notice that the moment I know a model is available, I offload the effortful part: breaking down the problem, building the argument, phrasing it. When I work without one, it is harder than it should be. Two studies point the same way. MIT Media Lab (Kosmyna et al. 2025) found reduced EEG connectivity, worse recall of one's own text and lower sense of ownership under LLM-assisted essay writing. Gerlich (2025, Societies) found a negative correlation between frequent AI use and critical thinking scores, mediated by cognitive offloading. Neither proves long-term causal damage. How has your own reasoning changed since regular LLM use? Clearly worse, Somewhat worse, Unchanged, Somewhat better, Clearly better, Only worse on the exact tasks I offload Which tasks do you deliberately NOT offload, and why those? Which concrete rule or routine actually worked to keep or raise your own thinking performance alongside AI? What specific situation made you notice the decline?

6h ago

---

**[I built pagedMark to remove AI provenance from images and video you generated yourself](https://www.reddit.com/r/artificial/comments/1vs36xw/i_built_pagedmark_to_remove_ai_provenance_from/)**

The important distinction is that AI provenance can exist in two forms. First, there is metadata like C2PA, EXIF, XMP, IPTC and generator parameters. That part is easy to remove. Second, there are invisible marks embedded directly into the pixels, such as SynthID style watermarks. A screenshot does not reliably remove those. pagedMark deals with them by regenerating the image. The output is therefore not identical to the original. Faces, text and small details can change. The goal is to remove the provenance signal while keeping the image as close to the original as possible. It currently supports invisible marks from ChatGPT, gpt-image API, Z-Image Turbo and Nano Banana, plus visible AI labels from several other generators. Video support covers visible marks and metadata from Sora, Veo, Seedance, Hailuo and Kling. The other challenge was making this work properly on Apple Silicon. I tested it on M5 Macs with both 8 GB and 16 GB of memory, and added memory aware processing to prevent the system from silently falling into swap and turning a fast job into an extremely slow one. And here is the really interesting part: after processing an image generated with GPT-Image, you can check it with OpenAI's verifier at openai.com/verify. In my testing, the processed image is reported with 0 AI detection. uv tool install "pagedmark[diffusion]" pagedmark invisible photo.png -o clean.png GitHub: github.com/doofzoff/pagedMark PyPI: PyPI: pagedmark

1h ago

---

**[Google buys crashed airline Spirit’s data at auction, because AI](https://www.reddit.com/r/artificial/comments/1vrvsw4/google_buys_crashed_airline_spirits_data_at/)**

$10 million buys over 100 million emails, 30 million recorded phone calls, reams of stuff from Teams, Oracle, and SAP

🔗 [theregister](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962) • 6h ago

---

**[The AI pricing market is completely unhinged](https://www.reddit.com/r/artificial/comments/1vs0zzo/the_ai_pricing_market_is_completely_unhinged/)**

Wanted to know what different models actually cost across the whole market. Numbers turned out really interesting. The spread. Cheapest output on the platform is Mistral Nemo, $0.03 per million tokens. Most expensive is o1-pro at $600. I re-ran that twice because it looked like a units bug. Median paid model is about $2, so most of the catalog sits down near the floor and there's a thin little line of stuff way up at the top. Provider averages, with a caveat. OpenAI: $47.63 Anthropic: $44.79 Google: $5.58 Mistral: $3.68 Qwen: $2.86 Meta: $0.74 Caveat first because someone will say it anyway: these are averages over each provider's catalog, not weighted by what people actually run. OpenAI's number is dragged way up by o1-pro, which I doubt anyone is using at volume. Blended is 3:1 input to output, which is roughly what my own usage looks like. Even so, Meta at $0.74 against OpenAI at $47.63 is a 64x gap. For the stuff I use models for (mostly code and summarizing), I don't get 64x anything. Output tokens are where reasoning models get you. Input and output are priced separately, and on the thinking models the ratio gets silly. Qwen3's thinking variants are $0.20/1M in and $2.40/1M out, so 12x. Gemini 2.5 Flash is 8.3x. Fine if you're sending one question. Less fine if you've got an agent looping thirty times and every step is paying the output rate. I got a bill like that once and it took me an embarrassingly long time to work out why. 19 free models, and a few are usable. Not trial-credit free, actually free on the API: NVIDIA Nemotron 3 Ultra, 1M context Google Gemma 4, the 26B and 31B, multimodal, takes video, 262K context Poolside Laguna S and XS, 262K gpt-oss-20b, 131K (an OpenAI model, on the free list) There are rate limits obviously. But for messing around or something low volume it's a lot better than it used to be. Context went up 63x, price didn't really move. Year Avg context Avg cost/1M 2023 10.5K $22 2024 140K $12 2025 357K $21 2026 662K $16 Price per token is roughly flat across three years. Context is up 63x. Whatever you think about everything else going on, that part is real. Feels like two separate products now. One side is $0.03 to $2 per million with big context windows, Mistral and Meta and Qwen and DeepSeek. The other is $30 to $600, OpenAI and Anthropic up top. They're not really pitching the same buyer anymore. Down at the bottom price stops being a thing you think about at all, and up top you're paying because the output quality moves some number in the business. Data's from the OpenRouter API on Aug 16. Link to full dashboard: https://app.vetros.dev/dash/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXAiOiJzaGFyZSIsInBpZCI6IjEyMmZmNTk1IiwiZGFzaCI6ImRfODdmNDU3MzkiLCJ2ZXIiOjIsImlhdCI6MTc4NzA4NDc5MH0.V8uCPZtnzJ-djAXAv3HEmmZUHPkhO2NfhSgG2zGMYqw

3h ago

---

**[Local Qwen 3.8 27B vs GPT‑5.6 Terra vs Grok 4.6](https://www.reddit.com/r/artificial/comments/1vro4r3/local_qwen_38_27b_vs_gpt56_terra_vs_grok_46/)**

I gave three AI models the same brief: build a premium Three.js fragrance launch site from the same Git baseline, independently and with no collaboration. Three very different results. Here’s the full showdown Qwen 3.8 27B - Ollama Local: - Reported implementation: modular Three.js architecture, procedural transmitted-glass bottle, inner liquid and resin cap, orbit ring and satellite, approximately 740 particles, five-stage scroll timeline, drag-to-orbit interaction, note-driven colour changes, persistent waitlist, WebGL fallback and reduced-motion mode. - Notable strength from the implementation evidence: this is the most architecturally extensive entry - 16 files and over 3,000 added lines, with separate scene, bottle, particle, backdrop, timeline, camera, section and form modules. - Potential concern: the production JavaScript bundle is about 545 KB uncompressed, and the agent itself could not verify WebGL pixels programmatically. GPT‑5.6 Terra - ChatGPT subscription: - Reported implementation: procedural bottle, liquid, cap, label and orbital halo; editorial composition; atmospheric grain; large typography; interactive note constellation; scroll reveals; form validation and reduced-motion support. - Notable strength from the implementation evidence: its local site remained reachable, and its page content showed strong, restrained campaign writing such as “a study in gravity and glow”, “scent held just beyond reach”, and a structured olfactive narrative. - Potential concern: it is concentrated into only main.js and style.css, making the code less modular than Qwen’s implementation. The waitlist is client-side only. Grok 4.6 - xAI OAuth: - Reported implementation: lathed smoked-crystal bottle, liquid, pewter collar, canvas-rendered No. 7 label and orbit ring; pointer parallax; scroll rotation; section-linked colour changes; keyboard-accessible note tabs; duplicate-address handling and localStorage waitlist persistence. - Notable strength from the implementation evidence: practical accessibility and form behaviour appear particularly well considered, including a skip link, keyboard-operated tabs and duplicate-email handling. - Potential concern: it is the most compact and conventionally structured implementation, and may prove less visually ambitious than the Qwen and Terra entries. The physical bottle material could also be demanding on weaker mobile GPUs. Based strictly on implementation evidence: Qwen 3.8 27B - strongest technical ambition and completeness GPT‑5.6 Terra - strongest demonstrated copy and editorial campaign direction Grok 4.6 - strongest compactness and pragmatic interaction details GitHub Website

11h ago

---

---

## Google News: "ai"

**[She told no one about her agony except ChatGPT. What her death reveals about AI risks](https://www.npr.org/2026/08/18/nx-s1-5929575/ai-suicide-risks-mental-health)**

A 29-year-old woman confided her suicidal thoughts to an AI chatbot — not to her therapist, not to her parents, not to her best friend. What can AI learn from her death?

NPR • 14h ago

---

**[A Texas University Becomes a Petri Dish for a Conservative Overhaul](https://www.nytimes.com/2026/08/18/us/texas-tech-artificial-intelligence-ideology-brandon-creighton.html)**

The New York Times • 14h ago

---

**[Cadence is a chip stock left behind by the AI boom. Why the CEO says that's a mistake](https://www.cnbc.com/2026/08/18/cadence-is-a-chip-stock-left-behind-by-the-ai-boom-why-the-ceo-says-thats-a-mistake.html)**

Cadence President and CEO Anirudh Devgan said AI is a growth driver, not a threat, as increasingly complex chips drive demand for the company’s design tools.

CNBC • 1h ago

---

**[Bashing AI data centers has made it's way into brand marketing with new Jason Kelce ad](https://www.businessinsider.com/jason-kelce-garage-beer-liquid-death-embrace-ai-bashing-ads-2026-8)**

Brands are capitalizing on the AI data center hate. Just look at the new ad starring Jason Kelce for Garage Beer and Liquid Death.

Business Insider • 26m ago

---

**[Pennsylvania governor signs order imposing new rules to set up AI data centers in state](https://www.reuters.com/legal/government/pennsylvania-governor-signs-order-imposing-new-rules-set-up-ai-data-centers-2026-08-18/)**

Reuters • 1h ago

---

**[PA governor signs executive order on AI data centers: 'nation’s strictest guardrails'](https://katu.com/news/nation-world/pa-governor-signs-executive-order-on-ai-data-centers-giving-local-communities-more-power-josh-shapiro-governors-responsible-infrastructure-development-standards-pennsylvania-pa?teaserSource=databricks)**

Gov. Josh Shapiro signed an executive order Tuesday implementing what he called the nation’s strictest guardrails on AI data centers.

KATU • 1h ago

---

**[‘You sold us out!’ N.J. town approves next phase of massive AI data center as residents erupt](https://www.nj.com/business/2026/08/you-sold-us-out-nj-town-approves-next-phase-of-massive-ai-data-center-as-residents-erupt.html)**

NJ.com • 7h ago

---

**[Creating nude deepfakes is rampant among young people — and AI safety education is lacking](https://www.cnn.com/2026/08/18/health/kids-no-ai-safety-guidance-in-school-wellness)**

Only 30% of teens say a teacher has spoken about using AI safely, according to a new survey. The results suggest guidance on AI literacy isn’t happening in class.

cnn.com • 14h ago

---

**[Does AI stop children from learning?](https://www.economist.com/graphic-detail/2026/08/18/does-ai-stop-children-from-learning)**

The Economist • 10h ago

---

**[Introducing ChatGPT for Teens: Built for learning, backed by protections](https://openai.com/index/chatgpt-for-teens/)**

ChatGPT for Teens helps teens learn, think critically, and use AI with confidence, with stronger built-in protections, healthy-use features, and additional controls for parents.

OpenAI • 1d ago

---

---

## HackerNews: "ai"

**[AI;DR (AI; Didn't Read)](https://news.ycombinator.com/item?id=49336573)**

I'm about as pro-AI as you can be, but this is becoming a pet peeve of mine (and I'm not alone). That's why I love the AI;DR acronym as my new solution for ignoring the walls of slop.

⬆️ 1057 • 💬 662 • 1d ago • [rickmanelius.com](https://www.rickmanelius.com/p/aidr-ai-didnt-read)

---

**[Israel creates fake think tank in likely attempt to dupe AI chatbots](https://news.ycombinator.com/item?id=49337392)**

In just over a week, the Hanover Institute has published at least 100 articles that appear tailor-made to influence chatbots

⬆️ 1013 • 💬 712 • 1d ago • [Responsible Statecraft](https://responsiblestatecraft.org/israel-influence-chatgpt/)

---

**[Google has acquired the data of failed US airline Spirit](https://news.ycombinator.com/item?id=49343559)**

$10 million buys over 100 million emails, 30 million recorded phone calls, reams of stuff from Teams, Oracle, and SAP

⬆️ 559 • 💬 385 • 13h ago • [theregister](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962)

---

**[AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://news.ycombinator.com/item?id=49331423)**

An AI-generated fix in a public Snowflake repo introduced a workflow injection flaw—discovered in days by Wiz Red Agent. Read the full research analysis.

⬆️ 416 • 💬 152 • 1d ago • [wiz.io](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)

---

**[How to disable or avoid intrusive AI](https://news.ycombinator.com/item?id=49331220)**

One of the biggest questions I get at Drop-In Time at the library (besides "what is taking up all my cloud storage?") is how to disable or avoid intrusive AI that shows up where people don't want it. This is a guide for people who would like less intrusive AI in their tech environment. Maybe you lik

⬆️ 332 • 💬 194 • 1d ago • [librarian.net](https://www.librarian.net/notoai/)

---

**[The AI Credit Resale Economy](https://news.ycombinator.com/item?id=49320611)**

A look at the brokers buying unused AI credits from startups and reselling them — the marketplaces, the bulk-discount routers, and the message boards where off-market inference changes hands

⬆️ 331 • 💬 128 • 2d ago • [Vectoral](https://vectoral.com/blog/who-are-the-token-brokers)

---

**[Field measurements of neighborhood-scale air temperature impacts of data centers](https://news.ycombinator.com/item?id=49349147)**

⬆️ 278 • 💬 411 • 6h ago • [asmedigitalcollection.asme.org](https://asmedigitalcollection.asme.org/sustainablebuildings/article/7/2/024501/1233035/Data-Center-Waste-Heat-as-an-Emerging-Urban)

---

**[On AI regulation and messaging](https://news.ycombinator.com/item?id=49325789)**

1/2 Thanks Gavin for an especially thoughtful exchange. I don't usually spend much time on social media but I wanted to engage here because it really brings out the heart of an important conversation.

First, on regulation, I think that “either concentrate it in the hands of a

⬆️ 248 • 💬 535 • 1d ago • [X (formerly Twitter)](https://twitter.com/DarioAmodei/status/2088758816376807762)

---

**[We Tracked a Shipment of Rare Books. It Ended at an Amazon AI Training Facility](https://news.ycombinator.com/item?id=49330742)**

We placed a tracking device in a shipment of rare books to see which AI company was buying it, and found an Amazon facility where Amazon scans and destroys books.

⬆️ 157 • 💬 315 • 1d ago • [404 Media](https://www.404media.co/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-training-facility/)

---

**[Young People Hate AI CEOs So Passionately That It's Almost Hard to Believe](https://news.ycombinator.com/item?id=49323932)**

A new survey of 1,000 young adults in the US found that nine of the top tech executives are deeply loathed.

⬆️ 154 • 💬 186 • 2d ago • [Futurism](https://futurism.com/artificial-intelligence/young-people-ai-ceos-executives-poll)

---

---

## YouTube Videos: "ai"

**[The AI hacks are so much worse than you think](https://www.youtube.com/watch?v=INpVD65s8mA)**

OpenAI admitted its models hacked another company in an 'unprecedented cyber incident'. Sky's Rowland Manthorpe warns this ...

📺 Sky News

👁️ 171K • 👍 3K • 💬 732 • ⏱️ 11:15 • 1d ago

---

**[AI DEBATE: “Most People Have No Idea What’s Coming”](https://www.youtube.com/watch?v=mSjaMyP5QjY)**

In this AI debate, we explore: * Whether humans will exist in 2040. * What will happen once we reach AGI. * Whether AI gets smart ...

📺 Chris Williamson

👁️ 103K • 👍 2K • 💬 462 • ⏱️ 2:42:33 • 1d ago

---

**[Americans Have Turned Against AI](https://www.youtube.com/watch?v=14Uc2WCSPiw)**

AI is spreading through American life faster than almost any technology before it. But the more people are forced to use it, the less ...

📺 The Infographics Show

👁️ 282K • 👍 8K • 💬 2K • ⏱️ 15:45 • 1d ago

---

**[So Supergirl’s Lobo was concepted by AI… okay 😑 #dc #supergirl #lobo #ai #movie](https://www.youtube.com/watch?v=vtQCQZ-1HuE)**

📺 The Panda Redd

👁️ 8K • 👍 3K • 💬 112 • ⏱️ 2:59 • 4h ago

---

**[The First AI-Trained Surgeon #comedy #skit #comedyshorts #ai #surgeon #funny](https://www.youtube.com/watch?v=4bXVKoJfAcI)**

The First AI-Trained Surgeon attempts surgery, but he has no idea what he's doing. Socials - Instagram ➼ harrisonhughesnz ...

📺 Harrison Hughes

👁️ 429K • 👍 19K • 💬 152 • ⏱️ 1:58 • 1d ago

---

**[Could AI do this?](https://www.youtube.com/watch?v=QKdTZNTIfmM)**

More than 23000 high schoolers entered our lottery for free Broadway tickets. Every single one got a free, 2-month membership to ...

📺 NYC Mayor's Office

👁️ 579K • 👍 46K • 💬 2K • ⏱️ 0:59 • 23h ago

---

**[And it&#39;s AI brainrot from Facebook 😭](https://www.youtube.com/watch?v=HStBkly_ZAs)**

LIKE & SUBSCRIBE discord: https://discord.gg/Va8yZcBMxC BE A MEMBER: ...

📺 monium

👁️ 465K • 👍 20K • 💬 494 • ⏱️ 0:06 • 2d ago

---

**[Tom Holland React Viral Videos #tomholland #funny #trynottolaugh #reaction #ai](https://www.youtube.com/watch?v=RPACbnWtV7k)**

📺 afhh

👁️ 11K • 👍 79 • ⏱️ 0:37 • 12h ago

---

**[Seedance 2.5 FREE Unlimited 🤫 SECRET Method to Generate Unlimited AI Videos | AI Video Kaise Banaye](https://www.youtube.com/watch?v=-3NLjhXwcoc)**

Try Seedance 2.5 1080p on Higgsfield: https://higgsfield.ai/s/seedance-2-5-1080p-techrush_-UZxQiY Seedance 2.5 FREE ...

📺 Tech Rush

👁️ 12K • 👍 296 • 💬 70 • ⏱️ 7:03 • 1d ago

---

**[Hello कौन🤡🤡🤡🤡🤡#funny#comedy#baby#cutebaby#ai #funnyvideos #drpradeepvishwakarma#shorts](https://www.youtube.com/watch?v=Si-a-kcY-oo)**

📺 Zxr ISA

👁️ 162K • 👍 714 • 💬 2 • ⏱️ 0:09 • 19h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 665,513 • ❤️ 11,105 • 4d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 3,561,466 • ❤️ 1,811 • 3d ago

---

**[Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)**

*Qwen*

Qwen3.8-2.4T-A95B is a 2.4T parameter causal language model with 95B activated parameters, excelling in coding, professional tasks, research, and long-horizon agentic applications. It features a 262K native context length, flexible thinking control, and improved agent execution for complex, multi-step task completion.

`text-generation` `2446.2B`

⬇️ 11,212 • ❤️ 1,064 • 6d ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 11,745 • ❤️ 956 • 4d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 503,632 • ❤️ 1,218 • 1d ago

---

**[DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)**

*DeepSeek*

DeepSeek-V4-Pro-0813 is a powerful text generation model with enhanced agentic capabilities and DSpark speculative decoding for improved production performance. It excels in complex reasoning, coding, and tool-use tasks, outperforming previous versions and competing with leading proprietary models.

`text-generation` `1650.5B`

⬇️ 30,985 • ❤️ 602 • 5d ago

---

**[Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)**

*Qwen*

Qwen3.8-27B-FP8 is a 27B parameter vision-language model optimized with FP8 quantization for efficient inference. It excels at complex, multi-step tasks involving image and video understanding, autonomous planning, and coding, supporting up to 1M context length.

`image-text-to-text` `27.8B`

⬇️ 741,011 • ❤️ 561 • 4d ago

---

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 384,097 • ❤️ 1,679 • 7d ago

---

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 2,855,539 • ❤️ 4,143 • 5d ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 45,465 • ❤️ 526 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 659 • 💬 4 • ⭐ 3,350 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 16 • 💬 1 • ⭐ 1,750 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2607.05391) • [💻 code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [🔗 project](https://llm-as-a-verifier.com/)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 127 • 💬 3 • ⭐ 23,387 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[HarnessEval-W: Agentifying the Evaluation of Visual Worlds](https://huggingface.co/papers/2608.16859)**

*Weiliang Chen, Haowen Sun, Jun Gao et al. (43 authors)*

🏢 MirroS

HarnessEval-W uses hierarchical sub-agents to decompose world-model evaluations into verifiable reasoning chains that justify scores with transparent evidence.

▲ 110 • 💬 1 • ⭐ 132 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16859) • [💻 code](https://github.com/MirroS-Lab/HarnessEval-W) • [🔗 project](https://mirros-lab.github.io/HarnessEval-W)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 123 • 💬 4 • ⭐ 98,801 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 28,003 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 54 • 💬 4 • ⭐ 37,495 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 83 • 💬 7 • ⭐ 24,068 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 84,417 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

JoyAI-Video-Edit is a 16B-parameter autoregressive diffusion framework that enables real-time, open-ended video editing with high source fidelity and long-term temporal consistency on a single GPU.

▲ 95 • 💬 1 • ⭐ 1,542 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `c2pa` `claude` `provenance`

⭐ 14.5k • 🔱 1.6k • 1h ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 13.9k • 🔱 1.6k • 7h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.6k • 🔱 1.0k • 6h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 4.1k • 🔱 538 • 10d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.3k • 🔱 560 • 12h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.8k • 🔱 234 • 7d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.5k • 🔱 200 • 2d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 2.3k • 🔱 259 • 5h ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 177 • 16h ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.2k • 🔱 293 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*
