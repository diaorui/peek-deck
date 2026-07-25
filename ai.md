---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-25T12:02:57.174030+00:00'
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

**Last Updated:** July 25, 2026 at 12:02 UTC  
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

**[White House offers its science blueprint: More AI, less life sciences. ‘Science: A New Golden Age’ report calls for shifting billions from universities to tech companies](https://www.reddit.com/r/artificial/comments/1v5on2l/white_house_offers_its_science_blueprint_more_ai/)**

The Trump administration released its blueprint for U.S. science, calling for shifting hundreds of billions of research dollars from universities to industry.

🔗 [STAT](https://www.statnews.com/2026/07/24/science-new-golden-age-report-draws-mixed-reaction/) • 14h ago

---

**[Opus 5's effort dial is not monotonic. Above "high", coding scores go down, and Anthropic's own migration guide says so.](https://www.reddit.com/r/artificial/comments/1v60pga/opus_5s_effort_dial_is_not_monotonic_above_high/)**

Opus 5 comes with five effort settings: low, medium, high, xhigh, max. Most people seem to be reaching straight for max, and at least on coding work that looks like the wrong move. On FrontierCode, scores fall above the high setting. The stated reason is that the model starts making unnecessary refactors and edits outside the scope it was given. Anthropic's own migration guide in the system card warns about diminishing returns and overthinking on simpler tasks, so this is not some outside critic's claim. Two other numbers point the same way: On the closed-book AA-Omniscience benchmark, Opus 5 is about 11% more accurate than Opus 4.8, but its hallucination rate runs about 6% higher. More reasoning, more room to be confidently wrong. CodeRabbit ran it at xhigh against their production baseline for code review. Precision on actionable comments went up, 39.3% vs 35.2%. But it caught fewer of the benchmark's known issues, 55.2% vs 61.1%, and generated roughly four times as many nitpicks. The flip side is worth knowing too, because it cuts the other way. On Zapier's AutomationBench, Opus 5 at its lowest effort setting still passes more tasks than any other model. So for a lot of workloads the cheap end of the dial is already enough, and the expensive end is not just wasted spend, it can be actively worse output. So, the setting where Opus 5 stops improving is probably specific to your codebase, and nobody has published a map of it. Worth finding your own ceiling before you default everything to max. One unrelated thing I have not seen discussed much: when a safety classifier flags a request in Claude.ai, Claude Code or Cowork, it silently falls back to Opus 4.8 by default. That is also how Anthropic's own Frontier-Bench run was configured, per the footnote on their chart. Nobody has published what fraction of requests that affects. Has anyone found the effort level where it turns over on a real repo? Curious whether the drop-off point moves with codebase size or with how much context you hand it.

5h ago

---

**[Bipartisan bill would require companies to tell users when they're talking to AI](https://www.reddit.com/r/artificial/comments/1v5jk23/bipartisan_bill_would_require_companies_to_tell/)**

The Senior Chatbot Protection Act, from Sens. Mark Kelly and Jim Justice, would require clear labeling of AI and new protections for health and financial conversations.

🔗 [NBC News](https://www.nbcnews.com/tech/tech-news/senate-bill-require-ai-chatbots-disclose-rcna588970) • 17h ago

---

**[How much of what you generate, actually makes it out of the door?](https://www.reddit.com/r/artificial/comments/1v62ww6/how_much_of_what_you_generate_actually_makes_it/)**

I did something slightly depressing on sunday. i went through my last month of ai outputs, all of it, drafts and images and scripts and little snippets, and counted how many actually got used somewhere real. published, sent, shipped, shown to a client. the number was eleven. out of roughly three hundred and forty. i sat there for a while trying to work out whether that was bad. my first reaction was that i was wasting the tool. three hundred and thirty dead outputs feels like a lot of dead outputs. but then i thought about how i worked before, and before, i simply did not make the three hundred and thirty. i made two options because two options was what the day allowed, and i picked one of the two, and that one shipped. so my hit rate used to look excellent on paper and my actual output was worse. what changed is not that i generate more. it is that the expensive step moved. generating used to be the hard part, the part you protected, the part you did not want to redo. now generating is nearly free and the hard part is looking. someone still has to open every one of those three hundred and forty things and decide. that someone is me, and i do not scale, and i get tired around the fortieth image in a way that no model ever does. so the bottleneck in my week is not the model and it is not my prompting. it is review capacity. which is a really unglamorous thing to be limited by. nobody posts about their review capacity, everyone posts about their stack. and the honest version is that i have gotten dramatically better at producing options and not one bit better at choosing between them, which is the half that was always hard. but i genuinely think the next thing that helps me will not be a better generator, it will be something that helps me throw away faster, or better, something that means i only ever look at twelve things instead of three hundred. i keep going back and forth on whether eleven out of three hundred and forty is a failure or just what abundance looks like. curious what your ratio is. does anyone here actually track this, or is it one of those numbers nobody wants to know?

3h ago

---

**[Users tried to object to their chatgpt logs being handed to the NYT. the court ruled they were "non-parties" to their own conversations.](https://www.reddit.com/r/artificial/comments/1v5b04p/users_tried_to_object_to_their_chatgpt_logs_being/)**

in the openai copyright case, a court ordered every chatgpt output log preserved, including chats people had deleted. some users tried to intervene to protect their own conversations. the court ruled they were non-parties. they had no standing over things they personally typed. two weeks ago the publishers filed for sanctions, alleging openai deleted billions of logs anyway and spent two years telling the court it couldn't search its own systems when it already could. openai denies it. the whole consumer privacy conversation is about what companies promise. we don't train on your chats, we delete after 30 days. this case showed the promise was never the binding constraint. a judge was. so "do they train on it" is close to the least useful question. the useful one is whether anything besides their good intentions is in the way when a court, a regulator or a future owner comes asking. that's an architecture question. opengradient's chat is what i switched the sensitive half of my usage to, and the mechanism is the interesting part: oblivious http means the relay that sees your ip can't read your request, and the server reading your request never learns your ip. neither can reassemble you alone. inference runs in an attested enclave the operator can't inspect. no log to preserve, nothing to hand over, because you were never in it. two honest cons. it's a16z-crypto-backed with a listed token, which put me off for weeks. and you lose memory and personalisation entirely, so it's not a daily driver, it's where the stuff goes i don't want in someone's discovery pile. does this end up mattering to normal people, or is it five hundred of us caring loudly while everyone else decides a subpoena hitting their recipe questions isn't worth degrading their tools over.

22h ago

---

**[We can live without AI, but we can’t live without water. “I have a jar right here. This is the current drinking water in Morgan Country, Georgia, right after a data center was constructed.” This is what the drinking water now looks like next to that data center” Protect our environment](https://www.reddit.com/r/artificial/comments/1v4j8rn/we_can_live_without_ai_but_we_cant_live_without/)**

1d ago

---

**[China’s open AI strategy is changing the race](https://www.reddit.com/r/artificial/comments/1v5c06c/chinas_open_ai_strategy_is_changing_the_race/)**

Moonshot AI’s Kimi K3 shows how opening a model to outsiders can turn other companies’ computing power into a competitive advantage

🔗 [Scientific American](https://www.scientificamerican.com/article/china-kimi-k3-and-the-rise-of-open-weight-ai-models/) • 22h ago

---

**[Is the AI job apocalypse real or just a marketing thing?](https://www.reddit.com/r/artificial/comments/1v64fw6/is_the_ai_job_apocalypse_real_or_just_a_marketing/)**

From the data I've seen AI has yet to actually affect employment statistics. I could be wrong of course, but is the whole idea of AI is going to wipe out jobs for normal people just a marketing thing to emphasize the capability of the latest AI models? Or is it a genuine threat that is just yet to materialize?

1h ago

---

**[What do you follow to stay current with AI?](https://www.reddit.com/r/artificial/comments/1v5pse7/what_do_you_follow_to_stay_current_with_ai/)**

I'm curious how everyone here keeps up with AI these days without spending hours doomscrolling. There are new models, tools, coding assistants, and AI workflows launching almost every day, so I'm interested in hearing what your "AI information diet" looks like. What do you follow regularly? It could be: WhatsApp or Telegram groups Discord communities Newsletters X accounts YouTube channels Blogs, podcasts, or anything else I'm especially interested in places that share practical updates like new AI tools, Cursor/Claude/GitHub Copilot tips, LLM news, real-world AI workflows, or interesting breakthroughs -without a ton of hype or self-promotion. Always looking for high-signal sources, and I'd love to hear what this community follows.

13h ago

---

**[Avichal Garg (Electric Capital, 10 unicorns) names the 3 moats AI can't touch — and #3 isn't a skill](https://www.reddit.com/r/artificial/comments/1v5zinj/avichal_garg_electric_capital_10_unicorns_names/)**

Avichal Garg has co-founded and backed 10 unicorns through Electric Capital. In a recent interview he laid out, unprompted, the three categories of value AI structurally can't absorb. First: physical-world work — anything requiring atoms, not bits, stays a moat as long as robotics lags digital AI. Second: regulated or licensed gates — anywhere the government controls supply and demand for strategic reasons, credentials plus access still win. Third, and the one that actually lands: relationships. He walks through a defense-procurement example — a specific officer, a 25-year relationship with a contractor, "no substitute for that." His conclusion: those relationship-heavy businesses get more valuable as AI absorbs the grunt work underneath them, not less. Margins go up. Worth sitting with if you've spent a career stacking "portable" skills instead of gated ones. 🔗

6h ago

---

---

## Google News: "ai"

**[Warning shot or publicity stunt - how worried should we be about the OpenAI hack?](https://www.bbc.com/news/articles/cd9w22n9e4go)**

Hugging Face said the hack was done at superhuman speed by an AI with little or no human guidance.

BBC • 1h ago

---

**[EXCLUSIVE: Its AI agent spent days hacking a company, but sources say OpenAI did not notice for a week](https://www.reuters.com/business/its-ai-agent-spent-days-hacking-company-sources-say-openai-did-not-notice-week-2026-07-24/)**

Reuters • 13h ago

---

**[No, OpenAI's models didn't go 'rogue' when they broke into Hugging Face. Here's what really happened.](https://www.livescience.com/technology/artificial-intelligence/no-openais-model-didnt-go-rogue-when-it-hacked-into-huggingface-heres-what-really-happened)**

Experts say the models didn't "go rogue" when they escaped a controlled cybersecurity test and hacked Hugging Face. Instead, they were pursuing the goal humans had given them in ways nobody anticipated.

Live Science • 1h ago

---

**[Open Weights and American AI Leadership](https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/)**

Open weight AI can expand access, strengthen competition, improve security, and help sustain American AI leadership.

Microsoft • 1d ago

---

**[Nvidia, Microsoft, Meta warn against 'premature restrictions' of open-weight models](https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html)**

Chinese open-weight models are gaining steam against leading offerings from American companies. OpenAI and Anthropic did not sign the letter.

CNBC • 21h ago

---

**[Nvidia, Microsoft and other tech giants back open-source AI models](https://www.reuters.com/world/asia-pacific/nvidia-microsoft-other-tech-giants-back-open-source-ai-models-2026-07-24/)**

Reuters • 17h ago

---

**['Getting filtered out': Young Americans struggle to land jobs in the new hiring landscape](https://www.foxbusiness.com/media/i-know-im-just-getting-filtered-out-young-americans-struggle-land-jobs-new-hiring-landscape)**

Recent graduates say artificial intelligence hiring tools and keyword-driven resume screening are making the job market harder to break into.

Fox Business • 1h ago

---

**[Opinion | The Flawed Case Against Data Centers](https://www.nytimes.com/2026/07/25/opinion/data-centers-environment-ai.html)**

The New York Times • 1h ago

---

**[Move over oil. AI leader Alphabet's spending sends investors running](https://www.freep.com/story/money/business/2026/07/25/ai-alphabets-expenditures-surge-making-investors-nervous/91038016007/)**

Second-quarter capital expenditures surged to $44.9 billion, twice last year's level, and Alphabet signaled another increase in 2027.

Detroit Free Press • 1h ago

---

**[Nvidia locks down memory supply from SK Hynix as part of $500 billion AI deal](https://www.cnbc.com/2026/07/25/nvidia-locks-down-memory-from-sk-hynix-as-part-of-500-billion-ai-deal.html)**

Nvidia is aggressively securing supply of high-bandwidth memory, an essential component for its GPUs and systems.

CNBC • 7h ago

---

---

## HackerNews: "ai"

**[Startup founders urge U.S. government not to shut off Chinese open weight AI](https://news.ycombinator.com/item?id=49023016)**

⬆️ 1048 • 💬 867 • 1d ago • [politico.com](https://www.politico.com/news/2026/07/22/startup-founders-urge-trump-not-to-shut-off-chinese-open-weight-ai-01008992)

---

**[AI Companies Are Trying to Hide a Staggering Amount of Debt](https://news.ycombinator.com/item?id=49020999)**

AI companies are pouring tens of billions of dollars into enormous data centers. They're being built on top of a mountain of hidden debt.

⬆️ 681 • 💬 371 • 1d ago • [Futurism](https://futurism.com/artificial-intelligence/ai-companies-hide-debt-off-balance-sheet)

---

**[Are AI labs pelicanmaxxing?](https://news.ycombinator.com/item?id=49010129)**

I generated 1,000+ SVGs across 7 frontier models to test whether AI labs are training on Simon Willison’s pelican-riding-a-bicycle benchmark.

⬆️ 679 • 💬 242 • 2d ago • [Dylan Castillo](https://dylancastillo.co/posts/pelicanmaxxing.html)

---

**[Quality non-fiction books are the antithesis of AI slop](https://news.ycombinator.com/item?id=49007247)**

⬆️ 491 • 💬 237 • 2d ago • [resobscura.substack.com](https://resobscura.substack.com/p/quality-non-fiction-books-are-the)

---

**[Businesses with ugly AI menu redesigns](https://news.ycombinator.com/item?id=49005973)**

I like supporting local businesses but it's so disheartening to see the increasing use of genAI in their branding/marketing/etc. Yuck yuck YUCK!!!

⬆️ 379 • 💬 303 • 2d ago • [fiddery](https://blog.fiddery.com/businesses-with-ugly-ai-menu-redesigns/)

---

**[The arguments against open source AI are bad](https://news.ycombinator.com/item?id=49024643)**

The release of Kimi K3 has opened a fresh round of angst and confused discourse. There's a loud cohort of journalists, business leaders, and politicians arguing that open source AI is a dangerous threat. OpenAI's Dean Ball:

⬆️ 309 • 💬 211 • 1d ago • [tombedor.dev](https://tombedor.dev/arguments-against-open-source-ai-are-very-bad/)

---

**[OpenAI and Anthropic unite against open-weight AI risks to their bottom line](https://news.ycombinator.com/item?id=49020868)**

⬆️ 297 • 💬 331 • 1d ago • [axios.com](https://www.axios.com/2026/07/22/openai-anthropic-open-models-trump-china)

---

**[Alphabet's cash burn raises alarm for Big Tech as AI spending climbs](https://news.ycombinator.com/item?id=49021006)**

⬆️ 273 • 💬 282 • 1d ago • [reuters.com](https://www.reuters.com/business/retail-consumer/alphabets-cash-burn-raises-alarm-big-tech-ai-spending-climbs-2026-07-23/)

---

**[DARPA, U.S. Air Force fly AI-controlled F-16](https://news.ycombinator.com/item?id=49021597)**

Historic VENOM milestone demonstrates scalable AI development capabilities for the operational fleet.

⬆️ 264 • 💬 327 • 1d ago • [darpa.mil](https://www.darpa.mil/news/2026/darpa-us-air-force-fly-ai-controlled-f-16)

---

**[Show HN: Palmier Pro – Open-source macOS video editor built for AI](https://news.ycombinator.com/item?id=49022911)**

macOS video editor built for AI. Contribute to palmier-io/palmier-pro development by creating an account on GitHub.

⬆️ 186 • 💬 35 • 1d ago • [GitHub](https://github.com/palmier-io/palmier-pro)

---

---

## YouTube Videos: "ai"

**[Lisa Su explains what&#39;s coming next in AI](https://www.youtube.com/watch?v=9tq0S6j4rrE)**

Wall Street keeps asking if the AI boom is slowing down. AMD CEO Lisa Su says she's seeing the exact opposite. In this interview ...

📺 Yahoo Finance

👁️ 5K • 👍 154 • 💬 12 • ⏱️ 13:51 • 16h ago

---

**[Godfather of AI WARNS: We Are Not Ready For What&#39;s Coming](https://www.youtube.com/watch?v=2nxrY5xiVrg)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Geoffrey Hinton, the Nobel laureate widely ...

📺 Neural Nutshell

👁️ 16K • 👍 482 • 💬 106 • ⏱️ 19:39 • 1d ago

---

**[AI model ESCAPES: &#39;What we feared could happen has happened&#39;](https://www.youtube.com/watch?v=_v8gwDj7M_Y)**

An experimental OpenAI model reportedly reached the open internet and accessed another company's servers during a test, ...

📺 Fox News

👁️ 176K • 👍 2K • 💬 1K • ⏱️ 4:05 • 1d ago

---

**[Google Issues a Dire Warning About the “AI Boom”](https://www.youtube.com/watch?v=3JjkvLAvS9w)**

Google just reported something it had never reported in its entire history as a public company: Negative quarterly free cash flow.

📺 Eurodollar University

👁️ 61K • 👍 2K • 💬 160 • ⏱️ 20:40 • 1d ago

---

**[Elon Musk on AI: humans will no longer be in control in ten years  | The Economist](https://www.youtube.com/watch?v=1X-rr1DKSbY)**

Watch the full show: https://bit.ly/4fsnd9Q Elon Musk expects artificial intelligence to exceed the sum of human intelligence in ...

📺 The Economist

👁️ 554K • 👍 10K • 💬 3K • ⏱️ 10:36 • 1d ago

---

**[AI News: This New Model Has Big AI Labs Panicking!](https://www.youtube.com/watch?v=Ww3EYbuHSfo)**

Here's the AI News you probably missed this week. Check out the limited first release of @GensparkProduct SecondBrain Note ...

📺 Matt Wolfe

👁️ 31K • 👍 2K • 💬 156 • ⏱️ 30:18 • 18h ago

---

**[It Begins: An AI Tried to Escape the Lab](https://www.youtube.com/watch?v=r4H7rx5nn1A)**

Join My Newsletter for Regular AI Updates https://forwardfuture.com My Links X: https://x.com/matthewberman ...

📺 Matthew Berman

👁️ 86K • 👍 3K • 💬 722 • ⏱️ 10:43 • 2d ago

---

**[THE AI BUBBLE is Collapsing: Tech Crashes](https://www.youtube.com/watch?v=HqW4maLiN88)**

Tech stock markets crash on the AI bubble collapse. Join our private group https://techleadpro.com Your Community for Crypto, ...

📺 TechLead

👁️ 48K • 👍 2K • 💬 293 • ⏱️ 12:19 • 13h ago

---

**[OpenAI internal model JUST went ROGUE](https://www.youtube.com/watch?v=OSuhUTkM1no)**

OpenAI and Hugging Face https://openai.com/index/hugging-face-model-evaluation-security-incident/ Safety and alignment in an ...

📺 Wes Roth

👁️ 190K • 👍 5K • 💬 2K • ⏱️ 26:22 • 2d ago

---

**[Free AI Tools So Good They&#39;re Making Paid Versions Obsolete](https://www.youtube.com/watch?v=QucgvbO5gsM)**

FREE RESOURCE I've put all 10 tools, every GitHub link, and the exact prompts I used inside our free "Staying Ahead" community ...

📺 Vaibhav Sisinty

👁️ 123K • 👍 6K • 💬 243 • ⏱️ 18:34 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,564,264 • ❤️ 3,046 • 2d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 45,260 • ❤️ 627 • 1d ago

---

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 31,575 • ❤️ 1,555 • 1d ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 2,784 • ❤️ 545 • 1d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 483,845 • ❤️ 505 • 5d ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 11,573 • ❤️ 377 • 1d ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 611,685 • ❤️ 1,013 • 7d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 707,029 • ❤️ 4,426 • 23d ago

---

**[Mage-Flow](https://huggingface.co/microsoft/Mage-Flow)**

*Microsoft*

Mage-Flow is a 4B-scale text-to-image generation and instruction-based image editing model, featuring an efficient native-resolution generation stack (512-2048px) with competitive quality and low latency. It excels at both generating novel images from text and performing versatile image edits, including semantic changes and restoration, with variants for base, RL-aligned, and fast Turbo inference.

`text-to-image` `4.1B`

⬇️ 1,156 • ❤️ 248 • 2d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 2,114,963 • ❤️ 634 • 7d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 63 • 💬 5 • ⭐ 18,734 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 32 • 💬 3 • ⭐ 15,348 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 48 • 💬 4 • ⭐ 33,506 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 262 • 💬 5 • ⭐ 14,931 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://huggingface.co/papers/2607.19064)**

*Xinjie Zhang, Peng Zhang, Shicheng Zheng et al. (24 authors)*

🏢 Microsoft

Large-scale visual generators are increasingly capable but costly to train, fine-tune, and deploy. We introduce Mage-Flow, a compact 4B-scale generative stack for efficient text-to-image generation and instruction-based image editing. The stack is built from two co-designed components: Mage-VAE, a lightweight high-fidelity latent tokenizer, and a Native-Resolution Multimodal Diffusion Transformer trained with rectified flow matching. Mage-VAE uses one-step diffusion-style encoding and decoding with anchor-latent regularization, preserving the reconstruction quality of strong public VAEs while reducing tokenization cost by more than an order of magnitude. Together with native-resolution packing and stack-level CUDA kernel fusion, the stack supports flexible-resolution training and improves end-to-end training throughput by about 2.5times. Built on this foundation, we develop a complete model family with Base, RL-aligned, and Turbo variants for both generation and editing. Diffusion-NFT improves prompt following, text rendering, aesthetic quality, and editing fidelity, while few-step distillation with adversarial perceptual guidance produces 4-step Turbo models for low-latency inference. Despite its compact scale, Mage-Flow and Mage-Flow-Edit achieves competitive performance across standard generation and editing benchmarks. More importantly, the Turbo variants make high-resolution generation and editing practical for interactive use: at 1024^2 resolution on a single NVIDIA A100 GPU, Mage-Flow-Turbo generates an image in 0.59s, and Mage-Flow-Edit-Turbo edits an image in 1.02s, while maintaining a small memory footprint. These results show that careful tokenizer--backbone--system co-design can deliver strong high-resolution generation and editing within an efficient 4B model family.

▲ 64 • 💬 2 • ⭐ 501 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19064) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 94,446 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://huggingface.co/papers/2607.19191)**

*Fan Jiang, Zhaoxu Sun, Mengchao Wang et al. (41 authors)*

🏢 Alibaba AMAP CV Lab

We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics. WorldExplorer performs agent-driven collection guided by training feedback, while a unified pipeline applies 14 deterministic quality checks, VLM-based assessment, and synchronized action and text annotation. We progressively distill a bidirectional action-conditioned teacher into a causal student through teacher forcing and ODE distillation, and introduce LongForcing to align long student self-rollouts with an extended-horizon teacher, mitigating accumulated distribution shift and autoregressive drift. Raw keyboard actions provide a unified control interface for scene roaming and third-person character interaction, while reference-character memory provides persistent appearance cues for identity consistency during third-person rollouts. For deployment, we co-design a streaming inference stack with a lightweight VAE decoder, efficient attention, memory-aware scheduling, and low-bit DiT inference. Across optimized low-bit configurations, ABot-World-0 streams 720P video at up to 16 FPS on a single NVIDIA RTX 5090 desktop GPU, with 1.2s action-to-first-frame latency and approximately 19GiB peak VRAM. Experiments on WorldRoamBench and extended interactive rollouts demonstrate competitive controllability and coherent long-horizon world evolution.

▲ 226 • 💬 5 • ⭐ 1,251 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19191) • [💻 code](https://github.com/amap-cvlab/ABot-World) • [🔗 project](https://abot-world.amap.com/)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 13 • 💬 0 • ⭐ 10,413 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 10,417 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 82,021 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.2k • 🔱 1.1k • 23h ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.3k • 🔱 252 • 3h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.7k • 🔱 382 • 1d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.5k • 🔱 280 • 16d ago

---

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

⭐ 2.5k • 🔱 191 • 2d ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 1.6k • 🔱 131 • 21h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.5k • 🔱 162 • 2d ago

---

**[MIgHTy-alIeN/MEV-Arbitrage-Bot](https://github.com/MIgHTy-alIeN/MEV-Arbitrage-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 1.4k • 🔱 1.0k • 29s ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.2k • 🔱 87 • 3d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 1.1k • 🔱 66 • 23h ago

---

---

*Generated by PeekDeck - A glance is all you need*
