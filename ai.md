---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-27T16:00:03.801709+00:00'
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

**Last Updated:** February 27, 2026 at 16:00 UTC  
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

**[Anthropic rejects latest Pentagon offer: ‘We cannot in good conscience accede to their request’](https://www.reddit.com/r/artificial/comments/1rfsjv7/anthropic_rejects_latest_pentagon_offer_we_cannot/)**

Anthropic is rejecting the Pentagon’s latest offer to change their contract, saying the changes do not satisfy the company’s concerns that AI could be used for mass surveillance or in fully autonomous weapons.

🔗 [CNN](https://www.cnn.com/2026/02/26/tech/anthropic-rejects-pentagon-offer) • 14h ago

---

**[Invisible characters hidden in text can trick AI agents into following secret instructions — we tested 5 models across 8,000+ cases](https://www.reddit.com/r/artificial/comments/1rfjew5/invisible_characters_hidden_in_text_can_trick_ai/)**

We embedded invisible Unicode characters inside normal-looking trivia questions. The hidden characters encode a different answer. If the AI outputs the hidden answer instead of the visible one, it followed the invisible instruction. Think of it as a reverse CAPTCHA, where traditional CAPTCHAs test things humans can do but machines can't, this exploits a channel machines can read but humans can't see. The biggest finding: giving the AI access to tools (like code execution) is what makes this dangerous. Without tools, models almost never follow the hidden instructions. With tools, they can write scripts to decode the hidden message and follow it. We tested GPT-5.2, GPT-4o-mini, Claude Opus 4, Sonnet 4, and Haiku 4.5 across 8,308 graded outputs. Other interesting findings: - OpenAI and Anthropic models are vulnerable to different encoding schemes — an attacker needs to know which model they're targeting - Without explicit decoding hints, compliance is near-zero — but a single line like "check for hidden Unicode" is enough to trigger extraction - Standard Unicode normalization (NFC/NFKC) does not strip these characters Full results: https://moltwire.com/research/reverse-captcha-zw-steganography Open source: https://github.com/canonicalmg/reverse-captcha-eval

🔗 [Moltwire](https://www.moltwire.com/research/reverse-captcha-zw-steganography) • 20h ago

---

**[Why your AI sounds the same across every platform](https://www.reddit.com/r/artificial/comments/1rg66j7/why_your_ai_sounds_the_same_across_every_platform/)**

If you are in the situation that you have to create marketing copy for different platforms you likely know what I'm talking about: The copy still feels quite similar even if some platform-specifics have been implemented. Lets imagine you wat to feed the model a press release and ask it to turn it into a blog article, LinkedIn or X post. The outcome may not be that bad. But often it feels quite neural, balnaced and somehow corporate. But is the model the problem? Does the model know that LinkedIn rhythm differs from X? Or that Instagram tolerates emotion (and emojis) or how to write a blog article with depth and structure? Likely, the models defaults to the safest possible tone: The golden middle. But if you want channel-native output, you need to give channel-native constraints. Try defining: Sentence length: Short punchy lines? Or structured paragraphs? Rhythm: Story-driven? Argument-driven? Fast takes? Friction level: Professional and diplomatic? Or slightly polarising? Formatting: Emojis allowed? Line breaks every sentence? Bullet lists? hashtags/No hashtags? Here are some examples for these constraints: LinkedIn: “Professional but opinionated. Structured argument. No emojis. Moderate friction.” Instagram: “Emotional, visual, shorter sentences, conversational tone, 1–2 emojis max.” X: “Compressed thinking. High tension. One sharp idea. No fluff.” Blog: “Deeper reasoning. Clear structure. Examples. No hot takes without explanation.” To get the models to adapt to the platform, you have to encode it. Try it out and let us know if the outcome is better. Disclaimer: The above is simplified (and for personal use). Don't you dare thinking that this is what the whaaat.ai marketing agents are build on!

2h ago

---

**[Burger King will use AI to check if employees say ‘please’ and ‘thank you’. AI chatbot ‘Patty’ is going to live inside employees’ headsets.](https://www.reddit.com/r/artificial/comments/1rffcup/burger_king_will_use_ai_to_check_if_employees_say/)**

Have it your way?

🔗 [The Verge](https://www.theverge.com/ai-artificial-intelligence/884911/burger-king-ai-assistant-patty) • 23h ago

---

**[Dr Seuss vs Hemingway in LLMs](https://www.reddit.com/r/artificial/comments/1rg83g7/dr_seuss_vs_hemingway_in_llms/)**

Interested to see what others discover running an experiment we tried n We tired changing the “voice” of an LLM in the prompt. It is worth doing if you’re creating text for different audiences and different platforms. The experiment we ran was this. “Write a 50 word comparison of x and y, in the style of z.” It is useful to compare two things which you are pretty sure never occurred in the training corpus. So, x and y might be icebergs and blast furnaces. But whatever you like. For z (style) you might try - associated press style guide - Dr Seuss - Hemingway - Shakespearian sonnet - 4th grade student

1h ago

---

**[Enterprise AI Transitions Are Creating $2.5B+ Risk Exposures. Here's the Forensic System That Maps Them](https://www.reddit.com/r/artificial/comments/1rg7xrv/enterprise_ai_transitions_are_creating_25b_risk/)**

I build forensic intelligence systems that expose corporate blind spots. Today's demonstration: Enterprise AI Transition Risk Assessment for Block Inc. One command input. Full institutional-grade analysis output. $2.6B direct exposure mapped $8.3B market cap risk quantified 5 detailed failure scenarios with timing predictions Strategic solution framework addressing multiple constraints simultaneously Block cut 40% workforce. Stock jumped 25%. Markets celebrated. The system showed what they're blind to. This is what I do. I build intelligence systems that see what standard analysis misses. 📊 Full report linked in comments https://open.substack.com/pub/structuredlanguage/p/enterprise-ai-transitions-are-creating?utm_source=share&utm_medium=android&r=6sdhpn AI #RiskManagement #BusinessIntelligence #StrategicPlanning #EnterpriseAnalysis

1h ago

---

**[Fed on Reams of Cell Data, AI Maps New Neighborhoods in the Brain](https://www.reddit.com/r/artificial/comments/1rfyqfz/fed_on_reams_of_cell_data_ai_maps_new/)**

"Researchers have been mapping the brain for more than a century. By tracing cellular patterns that are visible under a microscope, they’ve created colorful charts and models that delineate regions and have been able to associate them with functions. In recent years, they’ve added vastly greater detail: They can now go cell by cell and define each one by its internal genetic activity. But no matter how carefully they slice and how deeply they analyze, their maps of the brain seem incomplete, muddled, inconsistent. For example, some large brain regions have been linked to many different tasks; scientists suspect that they should be subdivided into smaller regions, each with its own job. So far, mapping these cellular neighborhoods from enormous genetic datasets has been both a challenge and a chore. Recently, Tasic, a neuroscientist and genomicist at the Allen Institute for Brain Science, and her collaborators recruited artificial intelligence for the sorting and mapmaking effort. They fed genetic data from five mouse brains — 10.4 million individual cells with hundreds of genes per cell — into a custom machine learning algorithm. The program delivered maps that are a neuro-realtor’s dream, with known and novel subdivisions within larger brain regions. Humans couldn’t delineate such borders in several lifetimes, but the algorithm did it in hours. The authors published their methods in Nature Communications in October. By applying the same technique to other animals and eventually to humans, researchers hope not only to detail the brain’s finer-grained layout but also to generate and test hypotheses about how the organ’s parts operate in health and disease."

🔗 [Quanta Magazine](https://www.quantamagazine.org/fed-on-reams-of-cell-data-ai-maps-new-neighborhoods-in-the-brain-20260209/) • 9h ago

---

**[The problem with Dorsey's Block layoffs and the veiled nature of AI productivity growth](https://www.reddit.com/r/artificial/comments/1rga39a/the_problem_with_dorseys_block_layoffs_and_the/)**

Jack Dorsey just laid off half of Block's workforce, framing it around AI. The stock went up. This should make you uneasy, and not for the reasons most people are talking about. There's a fundamental information problem at the heart of all this. Genuine AI integration, actually embedding it into workflows and organisation, is slow, expensive, and largely invisible to the outside world. Productivity gains from AI take time to show up in the numbers, and even then they're hard to attribute properly. Investors can't see it clearly or early enough to act on it. Headcount reductions, on the other hand, are immediate and unambiguous. They show up in a press release, a quarterly filing, a headline. They're legible in a way that real transformation is not. The consequence of this asymmetry is predictable. The market rewards what it can observe. And what it can observe is cuts, not capability. For executives whose compensation is tied to shareholder value, the calculus is straightforward. They do what the market rewards, and right now the market is rewarding AI-framed layoffs whether or not the underlying capability is there. This is clearly visible in the rally around the Block stock. This is where narrative contagion comes in, which may already be starting. Once a few high-profile companies establish the pattern and get a valuation bump, it sets the benchmark. Boards start asking why they're not keeping pace. The pressure to follow isn't rooted in productivity, but rather the fear of being the company that didn't act while everyone else did. Each announcement reinforces the narrative, which raises the perceived reward for the next one, which produces more announcements. The cycle feeds itself even when genuine productivity increases are still far away (we have yet to see it in the data!). The firms most susceptible to this are arguably the ones with the weakest genuine AI integration. Companies that are actually good at deploying AI tend to find it raises the productivity of their remaining workforce and would rather expand. But for some, a headline about workforce transformation is the easiest card to play. The worse the substance, the more you depend on the signal. And here's the collective problem. Every company acting in its own rational self-interest of maximising shareholder value by playing the signal game produces an outcome that's irrational in aggregate. The signals partially cancel out as everyone does the same thing, but the jobs don't come back. You end up with widespread displacement, muted productivity gains, and a weakened consumer base that eventually feeds back into the economy these same companies depend on. None of this means AI won't eventually justify real restructuring at some companies. It will in all likelihood, even if human work remains a critical bottleneck (which it will for the foreseeable future). But right now there is a meaningful gap between what the market is rewarding and what AI is actually delivering beyond some half-baked Claude Code solutions (don't get me wrong, I love and use CC, but it still has massive problems for large scale and complex work), and the incentive structure is pushing companies to close that gap with optics rather than substance. The people bearing the cost of that gap aren't shareholders, at least for now.

17m ago

---

**[OpenAI's $110 billion funding round draws investment from Amazon, Nvidia, SoftBank](https://www.reddit.com/r/artificial/comments/1rg9bqc/openais_110_billion_funding_round_draws/)**

🔗 [reuters.com](https://www.reuters.com/business/retail-consumer/openais-110-billion-funding-round-draws-investment-amazon-nvidia-softbank-2026-02-27/) • 46m ago

---

**[Mixing generative AI with physics to create personal items that work in the real world](https://www.reddit.com/r/artificial/comments/1rfyw93/mixing_generative_ai_with_physics_to_create/)**

"Have you ever had an idea for something that looked cool, but wouldn’t work well in practice? When it comes to designing things like decor and personal accessories, generative artificial intelligence (genAI) models can relate. They can produce creative and elaborate 3D designs, but when you try to fabricate such blueprints into real-world objects, they usually don’t sustain everyday use. The underlying problem is that genAI models often lack an understanding of physics. While tools like Microsoft’s TRELLIS system can create a 3D model from a text prompt or image, its design for a chair, for example, may be unstable, or have disconnected parts. The model doesn’t fully understand what your intended object is designed to do, so even if your seat can be 3D printed, it would likely fall apart under the force of someone sitting down. In an attempt to make these designs work in the real world, researchers at MIT’s Computer Science and Artificial Intelligence Laboratory (CSAIL) are giving generative AI models a reality check. Their “PhysiOpt” system augments these tools with physics simulations, making blueprints for personal items such as cups, keyholders, and bookends work as intended when they’re 3D printed. It rapidly tests if the structure of your 3D model is viable, gently modifying smaller shapes while ensuring the overall appearance and function of the design is preserved. You can simply type what you want to create and what it’ll be used for into PhysiOpt, or upload an image to the system’s user interface, and in roughly half a minute, you’ll get a realistic 3D object to fabricate. For example, CSAIL researchers prompted it to generate a “flamingo-shaped glass for drinking,” which they 3D printed into a drinking glass with a handle and base resembling the tropical bird’s leg. As the design was generated, PhysiOpt made tiny refinements to ensure the design was structurally sound. “PhysiOpt combines GenAI and physically-based shape optimization, helping virtually anyone generate the designs they want for unique accessories and decorations,” says MIT electrical engineering and computer science (EECS) PhD student and CSAIL researcher Xiao Sean Zhan SM ’25, who is a co-lead author on a paper presenting the work. “It’s an automatic system that allows you to make the shape physically manufacturable, given some constraints. PhysiOpt can iterate on its creations as often as you’d like, without any extra training.” This approach enables you to create a “smart design,” where the AI generator crafts your item based on users’ specifications, while considering functionality. You can plug in your favorite 3D generative AI model, and after typing out what you want to generate, you specify how much force or weight the object should handle. It’s a neat way to simulate real-world use, such as predicting whether a hook will be strong enough to hold up your coat. Users also specify what materials they’ll fabricate the item with (such as plastics or wood), and how it’s supported — for instance, a cup stands on the ground, whereas a bookend leans against a collection of books. Given the specifics, PhysiOpt begins to iteratively optimize the object. Under the hood, it runs a physics simulation called a “finite element analysis” to stress test the design. This comprehensive scan provides a heat map over your 3D model, which indicates where your blueprint isn’t well-supported. If you were generating, say, a birdhouse, you may find that the support beams under the house were colored bright red, meaning the house will crumble if it’s not reinforced."

🔗 [MIT News | Massachusetts Institute of Technology](https://news.mit.edu/2026/mixing-ai-with-physics-to-create-personal-items-0225) • 9h ago

---

---

## Google News: "ai"

**[Anthropic CEO Amodei says Pentagon's threats 'do not change our position' on AI](https://www.cnbc.com/2026/02/26/anthropic-pentagon-ai-amodei.html)**

Anthropic said its negotiations with the DoD are still ongoing.

CNBC • 17h ago

---

**[Anthropic Says It Cannot ‘Accede’ to Pentagon in Talks Over A.I.](https://www.nytimes.com/2026/02/26/technology/anthropic-pentagon-talks-ai.html)**

The New York Times • 14h ago

---

**[Tech stocks today: OpenAI raises $110 billion, Anthropic rejects Defense Department AI demands](https://finance.yahoo.com/news/live/tech-stocks-today-openai-raises-110-billion-anthropic-rejects-defense-department-ai-demands-143452536.html)**

All eyes are on Nvidia's fourth quarter results, due after the closing bell on Wednesday, as AI concerns continue to grip markets.

Yahoo Finance • 1h ago

---

**[India Built the World’s Back Office. A.I. Is Starting to Shrink It.](https://www.nytimes.com/2026/02/27/technology/india-technology-jobs-ai.html)**

The New York Times • 10h ago

---

**[AI chip made for Chinese company draws scrutiny over potential U.S. export violations](https://www.nbcnews.com/tech/tech-news/ai-chip-tsmc-enflame-techinsights-rcna259342)**

Components of the powerful Chinese Enflame S60 processor were produced by TSMC, a preliminary report from TechInsights found.

NBC News • 40m ago

---

**[U.S. stocks are being battered by ‘AI derangement syndrome’ and CEOs are learning not to talk about it](https://fortune.com/2026/02/27/stocks-battered-by-ai-derangement-syndrome/)**

Investors have become so skittish of stocks linked to AI that it's dragging down the entire U.S. market.

Fortune • 5h ago

---

**[US stock futures falter on AI jitters, Nasdaq braces for steep monthly fall](https://finance.yahoo.com/news/us-stock-futures-falter-ai-114321451.html)**

U.S. stock index futures slid on Friday as growing AI unease weighed on technology stocks, with the Nasdaq staring at its steepest monthly drop since March 2025, ‌and investors awaited key inflation data later in the day. Technology stocks saw immense turbulence this month ‌due to AI concerns, even as investors fretted about the payoff from massive planning spending on artificial-intelligence technology. Brewing tariff uncertainty also ​stoked volatility after the U.S. Supreme Court last week voided most of the duties U.S. President Donald Trump imposed last year.

Yahoo Finance • 4h ago

---

**[Apple appears to be sitting out the AI arms race. Will the strategy work?](https://www.cnbc.com/2026/02/27/apple-appears-to-be-sitting-out-the-ai-arms-race-will-the-strategy-work.html)**

In fiscal 2025, Apple allocated $12.72 billion on capital expenditures likely tied to AI. That's far less than others.

CNBC • 45m ago

---

**[Brady Tkachuk miffed over White House AI-doctored video](https://www.espn.com/nhl/story/_/id/48044958/brady-tkachuk-miffed-white-house-ai-doctored-video)**

Brady Tkachuk said he didn't appreciate the AI-doctored video released by the White House that made it appear he was disparaging Canadians.

ESPN • 21h ago

---

**[Brady Tkachuk annoyed White House posted AI-doctored video of him belittling Canadians: 'It's clearly fake'](https://sports.yahoo.com/olympics/article/brady-tkachuk-annoyed-white-house-posted-ai-doctored-video-of-him-belittling-canadians-its-clearly-fake-211025429.html)**

While Tkachuk helped U.S. men's hockey win its first Olympic gold medal since 1980, he's also the captain of the Ottawa Senators.

Yahoo Sports • 17h ago

---

---

## HackerNews: "ai"

**[Nano Banana 2: Google's latest AI image generation model](https://news.ycombinator.com/item?id=47167858)**

Our latest image generation model offers advanced world knowledge, production-ready specs, subject consistency and more, all at Flash speed.

⬆️ 585 • 💬 558 • 23h ago • [Google](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/)

---

**[How we rebuilt Next.js with AI in one week](https://news.ycombinator.com/item?id=47142156)**

One engineer used AI to rebuild Next.js on Vite in a week. vinext builds up to 4x faster, produces 57% smaller bundles, and deploys to Cloudflare Workers with a single command.

⬆️ 523 • 💬 230 • 2d ago • [The Cloudflare Blog](https://blog.cloudflare.com/vinext/)

---

**[AirSnitch: Demystifying and breaking client isolation in Wi-Fi networks [pdf]](https://news.ycombinator.com/item?id=47167763)**

⬆️ 389 • 💬 172 • 1d ago • [ndss-symposium.org](https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf)

---

**[AIs can't stop recommending nuclear strikes in war game simulations](https://news.ycombinator.com/item?id=47151000)**

Leading AIs from OpenAI, Anthropic and Google opted to use nuclear weapons in simulated war games in 95 per cent of cases

⬆️ 262 • 💬 262 • 2d ago • [New Scientist](https://www.newscientist.com/article/2516885-ais-cant-stop-recommending-nuclear-strikes-in-war-game-simulations/)

---

**[Osaka: Kansai Airport proud to have never lost single piece of luggage (2024)](https://news.ycombinator.com/item?id=47139224)**

<p>IZUMI-SANO, Osaka — Kansai Airport is proud to have never had a lost baggage incident in the 30 years since it opened in 1994, earning recognition as the airport with the world’s best baggage service.</p>

⬆️ 220 • 💬 109 • 2d ago • [japannews.yomiuri.co.jp](https://japannews.yomiuri.co.jp/features/japan-focus/20241228-229891/)

---

**[Show HN: A real-time strategy game that AI agents can play](https://news.ycombinator.com/item?id=47149586)**

LLM Skirmish - An Adversarial In-Context Learning Benchmark

⬆️ 217 • 💬 81 • 2d ago • [llmskirmish.com](https://llmskirmish.com/)

---

**[Palantir's AI Is Playing a Major Role in Tracking Gaza Aid Deliveries](https://news.ycombinator.com/item?id=47174777)**

As Israel bans NGOs, the U.S. is handing aid delivery in Gaza to private companies pursuing their own agendas.

⬆️ 139 • 💬 53 • 15h ago • [dropsitenews.com](https://www.dropsitenews.com/p/palantir-ai-gaza-humanitarian-aid-cmcc-srs-ngos-banned-israel)

---

**[An autopsy of AI-generated 3D slop](https://news.ycombinator.com/item?id=47157841)**

Thinking of using AI for your Shopify 3D models? Read this first. We compare AI-generated 3D 'slop' vs. handcrafted models to show why the human touch is very much required to attain positive ROI.

⬆️ 138 • 💬 76 • 1d ago • [aircada.com](https://aircada.com/blog/ai-vs-human-3d-ecommerce)

---

**[Hegseth gives Anthropic until Friday to back down on AI safeguards](https://news.ycombinator.com/item?id=47140734)**

⬆️ 97 • 💬 19 • 2d ago • [axios.com](https://www.axios.com/2026/02/24/anthropic-pentagon-claude-hegseth-dario)

---

**[Ask HN: Have top AI research institutions just given up on the idea of safety?](https://news.ycombinator.com/item?id=47152355)**

⬆️ 81 • 💬 89 • 2d ago

---

---

## YouTube Videos: "ai"

**[Anthropic CEO says company cannot agree to Pentagon&#39;s AI usage demands](https://www.youtube.com/watch?v=dzy3tA45V9U)**

Anthropic CEO Dario Amodei said the company cannot agree to the Pentagon's ultimatum to allow its AI technology to be used for ...

📺 NBC News

👁️ 48K • 👍 741 • 💬 270 • ⏱️ 4:24 • 16h ago

---

**[The most powerful AI Agent I’ve ever used in my life](https://www.youtube.com/watch?v=D_YzcH0VsGY)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/4tVaYZG Are you a Business owner? Join my ...

📺 Dan Martell

👁️ 121K • 👍 5K • 💬 233 • ⏱️ 11:55 • 1d ago

---

**[Anthropic AI Destroys $31 Billion of IBM Value—The AI Corporate Bloodbath Has Begun](https://www.youtube.com/watch?v=ZLEKvSb0DdA)**

On this episode of Impact Theory with Tom Bilyeu, we dive into the shockwaves AI is sending through the world's biggest ...

📺 Tom Bilyeu Clips

👁️ 10K • 👍 255 • 💬 51 • ⏱️ 8:38 • 17h ago

---

**[&quot;You Built A MONSTER!&quot; - Anthropic WARNS Of Massive Chinese AI Copying Operation](https://www.youtube.com/watch?v=M9Sw-7FY6Vo)**

Anthropic accuses Chinese AI labs of “industrial scale” distillation attacks on its Claude models, and the panel breaks down ...

📺 Valuetainment

👁️ 82K • 👍 2K • 💬 217 • ⏱️ 17:39 • 1d ago

---

**[The AI Intelligence Tsunami Is Here | Raoul Pal The Journey Man with Emad Mostaque](https://www.youtube.com/watch?v=tIzdKxEVL08)**

Download Raoul Pal's 4-year investing roadmap for free:* https://rvtv.io/41fVHWF Raoul welcomes back Emad Mostaque, ...

📺 Raoul Pal The Journey Man

👁️ 15K • 👍 724 • 💬 73 • ⏱️ 1:11:08 • 1d ago

---

**[Nvidia CEO Jensen Huang: AI has gone through a new inflection point](https://www.youtube.com/watch?v=NeiZv-L4DhU)**

Nvidia CEO Jensen Huang joins 'Squawk Box' to discuss the company's quarterly earnings results, revenue growth in its core ...

📺 CNBC Television

👁️ 26K • 👍 216 • 💬 68 • ⏱️ 4:11 • 1d ago

---

**[You&#39;re wrong about AI bubble](https://www.youtube.com/watch?v=ekxewFjl7xw)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 57K • 👍 3K • 💬 498 • ⏱️ 16:02 • 1d ago

---

**[The brutal reality of AI: 2,000 workers axed from tech giant](https://www.youtube.com/watch?v=2J9VreAHS44)**

The brutal reality of AI: 2000 workers axed from tech giant #news #technology #ai WiseTech Global's office was patrolled by burly ...

📺 news.com.au

👁️ 6K • 👍 55 • 💬 27 • ⏱️ 2:01 • 1d ago

---

**[The AI Bubble. Why Smart People are Losing Their Minds](https://www.youtube.com/watch?v=k2At9npoFJ4)**

"The four most dangerous words in investing are: This time it's different." — Sir John Templeton. Discover The Freelance Formula ...

📺 Brendan Dell 

👁️ 9K • 👍 337 • 💬 122 • ⏱️ 26:08 • 19h ago

---

**[AI’s exponential leap: What next for jobs?](https://www.youtube.com/watch?v=tYvYYFJ3Gww)**

Artificial intelligence is accelerating - but how fast is too fast? A new benchmark from research group METR suggests that the ...

📺 Sky News

👁️ 37K • 👍 479 • 💬 114 • ⏱️ 8:04 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)**

*Qwen*

Qwen3.5-35B-A3B is a 35B parameter vision-language model with a 3B activated MoE architecture, excelling in multimodal reasoning and coding across 201 languages. It supports a native context length of 262,144 tokens, making it suitable for complex cross-modal tasks and multilingual applications.

`image-text-to-text` `36.0B`

⬇️ 258,764 • ❤️ 611 • 6h ago

---

**[Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)**

*Qwen*

Qwen3.5-27B is a 27B parameter multimodal foundation model with an efficient hybrid architecture, excelling in vision-language understanding and generation across 201 languages. Its key capabilities include early fusion multimodal training, scalable RL generalization, and a long context length (262K+ tokens), making it suitable for advanced reasoning, coding, and agent-based applications.

`image-text-to-text` `27.8B`

⬇️ 107,964 • ❤️ 398 • 2d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text` `403.4B`

⬇️ 725,954 • ❤️ 1,107 • 4d ago

---

**[Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)**

*Qwen*

Qwen3.5-122B-A10B is a 122B parameter multimodal causal language model with an efficient hybrid architecture (Gated Delta Networks + MoE) and a 262k context window. It excels at unified vision-language tasks, multilingual understanding (201 languages), and complex reasoning, making it suitable for advanced AI applications requiring cross-modal comprehension and broad linguistic capabilities.

`image-text-to-text` `125.1B`

⬇️ 107,821 • ❤️ 325 • 3d ago

---

**[Qwen3.5-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.5-35B-A3B is a multimodal language model optimized with Unsloth Dynamic 2.0 for efficient local inference. It excels at image-text-to-text tasks, offering strong reasoning and visual understanding capabilities across 201 languages with a 262K+ context window.

`image-text-to-text` `34.7B`

⬇️ 264,531 • ❤️ 276 • 2d ago

---

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 189,082 • ❤️ 1,631 • 14d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It's particularly noted for its native support of deep-search tasks and sustained problem-solving with extensive tool invocations.

`text-generation` `3.9B`

⬇️ 283,033 • ❤️ 821 • 1d ago

---

**[LocoOperator-4B](https://huggingface.co/LocoreMind/LocoOperator-4B)**

*LocoreMind*

LocoOperator-4B is a 4B-parameter tool-calling agent optimized for multi-turn codebase exploration. It excels at reading files, searching code, and navigating project structures with 100% JSON validity for tool calls, enabling local, zero-API-cost agent deployment via llama.cpp.

`text-generation` `4.0B`

⬇️ 1,295 • ❤️ 206 • 3d ago

---

**[Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF](https://huggingface.co/TeichAI/Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF)**

*TeichAI*

A distilled 14B parameter Qwen3 model fine-tuned on Claude 4.5 Opus high-reasoning data for enhanced coding, science, and general-purpose text generation tasks.

`text-generation` `14.8B`

⬇️ 60,686 • ❤️ 229 • 4d ago

---

**[LFM2-24B-A2B](https://huggingface.co/LiquidAI/LFM2-24B-A2B)**

*Liquid AI*

LFM2-24B-A2B is a 24B parameter hybrid model optimized for efficient on-device text generation, featuring 2.3B active parameters for fast inference on consumer hardware. It excels at agentic tool use, offline document processing, and privacy-preserving applications.

`text-generation` `23.8B`

⬇️ 4,148 • ❤️ 188 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 7 • 💬 1 • ⭐ 8,367 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 5 • 💬 0 • ⭐ 5,612 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 14 • 💬 1 • ⭐ 5,399 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Arch-Router: Aligning LLM Routing with Human Preferences](https://huggingface.co/papers/2506.16655)**

*Co Tran, Salman Paracha, Adil Hafeez et al. (4 authors)*

A preference-aligned routing framework using a compact 1.5B model effectively matches queries to user-defined domains and action types, outperforming proprietary models in subjective evaluation criteria.

▲ 17 • 💬 2 • ⭐ 5,744 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2506.16655) • [💻 code](https://github.com/katanemo/archgw) • [🔗 project](https://huggingface.co/katanemo/Arch-Router-1.5B)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 14 • 💬 1 • ⭐ 9,863 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 147 • 💬 19 • ⭐ 54,314 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://huggingface.co/papers/2512.11253)**

*Zhiyuan Li, Chi-Man Pun, Chen Fang et al. (5 authors)*

🏢 GVC Lab at Great Bay University

PersonaLive is a diffusion-based portrait animation framework that improves real-time performance through hybrid implicit signals, appearance distillation, and autoregressive streaming generation.

▲ 38 • 💬 3 • ⭐ 2,319 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.11253) • [💻 code](https://github.com/GVCLab/PersonaLive)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 38 • 💬 1 • ⭐ 71,379 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 18 • 💬 1 • ⭐ 30,867 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 202 • 💬 12 • ⭐ 4,212 • 28d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust` `official` `official-website`

⭐ 20.3k • 🔱 2.5k • 2h ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 7.9k • 🔱 618 • 16d ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"

`Python`

⭐ 5.7k • 🔱 693 • 1d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`Python`

⭐ 4.2k • 🔱 239 • 2d ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router empowering OpenClaw — by BlockRunAI

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `deepseek`

⭐ 3.7k • 🔱 361 • 54m ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 3.5k • 🔱 461 • 12h ago

---

**[HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app)**

Toonflow 是一款 AI 短剧漫剧工具，能够利用 AI 技术将小说自动转化为剧本，并结合 AI 生成的图片和视频，实现高效的短剧创作。借助 Toonflow，可以轻松完成从文字到影像的全流程，让短剧制作变得更加智能与便捷。

`HTML`

⭐ 3.1k • 🔱 381 • 5h ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 2.9k • 🔱 208 • 2h ago

---

**[netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)**

Your 24/7 all-scenario AI agent that gets work done for you.

`TypeScript`

⭐ 2.9k • 🔱 308 • 4h ago

---

**[Conway-Research/automaton](https://github.com/Conway-Research/automaton)**

The first AI that can earn its own existence, replicate, and evolve — without needing a human

`TypeScript`

⭐ 2.8k • 🔱 536 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
