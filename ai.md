---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-24T20:24:26.493206+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 24, 2026 at 20:24 UTC  
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

**[Users tried to object to their chatgpt logs being handed to the NYT. the court ruled they were "non-parties" to their own conversations.](https://www.reddit.com/r/artificial/comments/1v5b04p/users_tried_to_object_to_their_chatgpt_logs_being/)**

in the openai copyright case, a court ordered every chatgpt output log preserved, including chats people had deleted. some users tried to intervene to protect their own conversations. the court ruled they were non-parties. they had no standing over things they personally typed. two weeks ago the publishers filed for sanctions, alleging openai deleted billions of logs anyway and spent two years telling the court it couldn't search its own systems when it already could. openai denies it. the whole consumer privacy conversation is about what companies promise. we don't train on your chats, we delete after 30 days. this case showed the promise was never the binding constraint. a judge was. so "do they train on it" is close to the least useful question. the useful one is whether anything besides their good intentions is in the way when a court, a regulator or a future owner comes asking. that's an architecture question. opengradient's chat is what i switched the sensitive half of my usage to, and the mechanism is the interesting part: oblivious http means the relay that sees your ip can't read your request, and the server reading your request never learns your ip. neither can reassemble you alone. inference runs in an attested enclave the operator can't inspect. no log to preserve, nothing to hand over, because you were never in it. two honest cons. it's a16z-crypto-backed with a listed token, which put me off for weeks. and you lose memory and personalisation entirely, so it's not a daily driver, it's where the stuff goes i don't want in someone's discovery pile. does this end up mattering to normal people, or is it five hundred of us caring loudly while everyone else decides a subpoena hitting their recipe questions isn't worth degrading their tools over.

7h ago

---

**[We can live without AI, but we can’t live without water. “I have a jar right here. This is the current drinking water in Morgan Country, Georgia, right after a data center was constructed.” This is what the drinking water now looks like next to that data center” Protect our environment](https://www.reddit.com/r/artificial/comments/1v4j8rn/we_can_live_without_ai_but_we_cant_live_without/)**

1d ago

---

**[Bipartisan bill would require companies to tell users when they're talking to AI](https://www.reddit.com/r/artificial/comments/1v5jk23/bipartisan_bill_would_require_companies_to_tell/)**

The Senior Chatbot Protection Act, from Sens. Mark Kelly and Jim Justice, would require clear labeling of AI and new protections for health and financial conversations.

🔗 [NBC News](https://www.nbcnews.com/tech/tech-news/senate-bill-require-ai-chatbots-disclose-rcna588970) • 2h ago

---

**[China’s open AI strategy is changing the race](https://www.reddit.com/r/artificial/comments/1v5c06c/chinas_open_ai_strategy_is_changing_the_race/)**

Moonshot AI’s Kimi K3 shows how opening a model to outsiders can turn other companies’ computing power into a competitive advantage

🔗 [Scientific American](https://www.scientificamerican.com/article/china-kimi-k3-and-the-rise-of-open-weight-ai-models/) • 6h ago

---

**["I'm doing this because I love it"](https://www.reddit.com/r/artificial/comments/1v50yle/im_doing_this_because_i_love_it/)**

He does it because he loves it huh?

15h ago

---

**[How should startups choose an AI consulting company without wasting months on pilots?](https://www.reddit.com/r/artificial/comments/1v5gzzx/how_should_startups_choose_an_ai_consulting/)**

A lot of startups are trying to add AI right now, but the hard part usually isn’t which model we should use. It’s questions like: Do we need strategy, engineering, or both? Should we hire an AI consultant or build in-house? Can this team ship production software, or only run discovery workshops? Do they understand RAG, agents, vector databases, monitoring, and inference costs? Is an enterprise consulting firm overkill for an MVP-stage startup? I came across a comparison of AI consulting companies for startups and thought the most useful point was this: The best partner depends less on brand name and more on your stage. Enterprise firms may make sense if you need governance, compliance, and large-scale transformation. Smaller engineering-focused teams may be better if you need to launch an AI SaaS, internal tool, chatbot, automation product, or MVP quickly. Curious how others here are approaching this. If you’re a founder or engineering lead, would you rather work with: A big consulting firm, A boutique AI dev shop, A freelance AI engineer, Or build the whole thing internally? And what would be your biggest red flag when evaluating an AI consulting partner?

3h ago

---

**[The AI spending debate seems to have changed this week.](https://www.reddit.com/r/artificial/comments/1v5mt72/the_ai_spending_debate_seems_to_have_changed_this/)**

Google just signaled even larger AI infrastructure spending this year. From a technology perspective, that's a huge vote of confidence in continued AI development. But investors barely celebrated it—instead they focused on whether all that spending will actually pay off. Do you think we're reaching the point where the debate is no longer "Will companies invest in AI?" but "Which companies will actually make money from AI?"

3m ago

---

**[Built a tool that datacenter cooling layouts optimiser](https://www.reddit.com/r/artificial/comments/1v5mewy/built_a_tool_that_datacenter_cooling_layouts/)**

AI's eating power and heat is the part nobody's actually simulating, everyone forgets about that so. I have built a data center cooling layout optimizer that runs Open FOAM solves on a datacenter layout and optimizes CRAC placement against it. Still limited to small sized facilities on real hardware, not thousands of racks overnight. Would need a large computer for that. Any other way of optimizing it? What do you think? Repo: https://github.com/PantherHale/DataCenter_Cooling_Project_OFD

18m ago

---

**[the diffusion versus autoregressive debate finally has a clean data point, and it points to a much narrower claim than the hype](https://www.reddit.com/r/artificial/comments/1v5lhsw/the_diffusion_versus_autoregressive_debate/)**

For about a year the diffusion versus autoregressive argument has mostly run on vibes. One camp says next token prediction is a dead end and parallel denoising is the future, the other says diffusion never survives contact with real tasks. Almost nobody was putting the two side by side on the same evals from the same lab. The lab behind it just did exactly that, with a model they pushed out only hours ago, and the honest part is what they compared against. They benchmarked their diffusion model, the one they call LLaDA2.2, against their own autoregressive model of similar size. So this is not a vendor picking a weak outside competitor. It is one lab grading its two bets against each other. The result is more useful for being unflattering. On general knowledge and most coding evals the diffusion model trails its autoregressive sibling. It only pulls ahead on a handful of interactive agent benchmarks, winning tau2 bench at 80.33 over 76.36, and MCP Atlas at 46.21 over 41.12, the multi turn tool calling style tasks. The SWE bench gap looks worse than it really is because the two runs used different scaffolds, so I would not read that one literally. Where it clearly wins is speed. Roughly 1.6x average decoding throughput over the autoregressive sibling in BF16 with speculative decoding on, and up to about 2.3x on the agent workloads. It gets there by keeping, substituting, deleting and inserting tokens inside a block instead of committing to each token once and never revisiting it. The weights are open under Apache 2.0, which is the only reason any of this is checkable, but it is a 205.8 GB, 100B class download with no llama.cpp support and only a coming soon serving story, so almost nobody runs it locally, and structured output is weaker than the autoregressive baseline by the authors' own admission. So I do not read this as diffusion wins. The narrower claim it actually supports is that for agent loops where you pay decode latency every turn, a diffusion backbone can reach a comparable quality band noticeably faster. That is a niche, not a paradigm shift, and the paradigm shift was never the honest question. What we finally have is a way to measure the tradeoff instead of arguing about it.

51m ago

---

**[Taking Blame Is the Next Billion-Dollar Business](https://www.reddit.com/r/artificial/comments/1v5ewgu/taking_blame_is_the_next_billiondollar_business/)**

🔗 [monolith3.substack.com](https://monolith3.substack.com/p/taking-blame-is-the-next-billion) • 4h ago

---

---

## Google News: "ai"

**[Moody's says 'unprecedented' AI spending threatens credit quality of Amazon, Meta, Alphabet and others](https://www.cnbc.com/2026/07/24/moodys-ai-spending-credit-quality-amazon-meta-alphabet.html)**

Moody's said AI spending is forcing even the world's most cash-rich corporations to lean heavily on debt, stock sales and off-balance-sheet moves.

CNBC • 2h ago

---

**[Open Weights and American AI Leadership](https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/)**

Open weight AI can expand access, strengthen competition, improve security, and help sustain American AI leadership.

Microsoft • 9h ago

---

**[Wall Street Bulls Are Staring Down $100 Oil, Tariffs, AI Angst](https://www.bloomberg.com/news/articles/2026-07-24/wall-street-bulls-are-staring-down-100-oil-tariffs-ai-angst)**

Bloomberg.com • 11m ago

---

**[Tech rebound steadies stocks after AI scare](https://www.foxbusiness.com/video/6402032450112)**

Yardeni Research president Ed Yardeni discusses the Nasdaq's rebound after early losses tied to A.I. spending concerns and explains why he remains bullish on the market on 'Making Money.'

Fox Business • 57m ago

---

**[Oracle Base Database Cloud@Customer Brings Private AI Closer To Data](https://www.forbes.com/sites/stevemcdowell/2026/07/24/oracle-base-database-cloudcustomer-brings-private-ai-closer-to-data/)**

Oracle target's the branch office as AI's next battleground: Base Database Cloud@Customer brings cloud economics to data that can't move.

Forbes • 34m ago

---

**[Opinion | No Wonder Elon Musk Hates ‘The Odyssey’](https://www.nytimes.com/2026/07/24/opinion/elon-musk-odyssey-ai.html)**

The New York Times • 11h ago

---

**[Turns out Dead Internet Theory was right: AI agents are eating the Web, growing by nearly 8,000% and rewiring the Internet’s business model](https://finance.yahoo.com/technology/ai/articles/turns-dead-internet-theory-ai-201027433.html)**

Multiple cyber firms agree: bots outnumber humans online, challenging advertising, analytics and security systems designed around human visitors.

Yahoo Finance • 1d ago

---

**[What is China’s Kimi K3 and why is the US so rattled by it?](https://www.cnn.com/2026/07/23/tech/china-ai-moonshot-kimi-explainer-intl-hnk)**

Remember DeepSeek? The Chinese artificial intelligence startup that rattled the US tech industry? China may have done it again.

CNN • 18h ago

---

**[White House draws new AI line on China](https://www.axios.com/2026/07/24/white-house-ai-line-china)**

Axios • 11h ago

---

**[U.S., other nations back open-source AI with 'strong security' at China summit](https://www.cnbc.com/2026/07/24/china-ai-open-source-apec.html)**

The APEC statement is the first to include open-source cooperation at a minister level, said Li Lecheng, China's industry and information technology minister.

CNBC • 17h ago

---

---

## HackerNews: "ai"

**[Startup founders urge U.S. government not to shut off Chinese open weight AI](https://news.ycombinator.com/item?id=49023016)**

⬆️ 1033 • 💬 839 • 1d ago • [politico.com](https://www.politico.com/news/2026/07/22/startup-founders-urge-trump-not-to-shut-off-chinese-open-weight-ai-01008992)

---

**[Are AI labs pelicanmaxxing?](https://news.ycombinator.com/item?id=49010129)**

I generated 1,000+ SVGs across 7 frontier models to test whether AI labs are training on Simon Willison’s pelican-riding-a-bicycle benchmark.

⬆️ 677 • 💬 242 • 2d ago • [Dylan Castillo](https://dylancastillo.co/posts/pelicanmaxxing.html)

---

**[AI Companies Are Trying to Hide a Staggering Amount of Debt](https://news.ycombinator.com/item?id=49020999)**

AI companies are pouring tens of billions of dollars into enormous data centers. They're being built on top of a mountain of hidden debt.

⬆️ 672 • 💬 360 • 1d ago • [Futurism](https://futurism.com/artificial-intelligence/ai-companies-hide-debt-off-balance-sheet)

---

**[Quality non-fiction books are the antithesis of AI slop](https://news.ycombinator.com/item?id=49007247)**

⬆️ 487 • 💬 236 • 2d ago • [resobscura.substack.com](https://resobscura.substack.com/p/quality-non-fiction-books-are-the)

---

**[Businesses with ugly AI menu redesigns](https://news.ycombinator.com/item?id=49005973)**

I like supporting local businesses but it's so disheartening to see the increasing use of genAI in their branding/marketing/etc. Yuck yuck YUCK!!!

⬆️ 377 • 💬 303 • 2d ago • [fiddery](https://blog.fiddery.com/businesses-with-ugly-ai-menu-redesigns/)

---

**[The arguments against open source AI are bad](https://news.ycombinator.com/item?id=49024643)**

The release of Kimi K3 has opened a fresh round of angst and confused discourse. There's a loud cohort of journalists, business leaders, and politicians arguing that open source AI is a dangerous threat. OpenAI's Dean Ball:

⬆️ 305 • 💬 208 • 1d ago • [tombedor.dev](https://tombedor.dev/arguments-against-open-source-ai-are-very-bad/)

---

**[OpenAI and Anthropic unite against open-weight AI risks to their bottom line](https://news.ycombinator.com/item?id=49020868)**

⬆️ 289 • 💬 330 • 1d ago • [axios.com](https://www.axios.com/2026/07/22/openai-anthropic-open-models-trump-china)

---

**[Alphabet's cash burn raises alarm for Big Tech as AI spending climbs](https://news.ycombinator.com/item?id=49021006)**

⬆️ 267 • 💬 282 • 1d ago • [reuters.com](https://www.reuters.com/business/retail-consumer/alphabets-cash-burn-raises-alarm-big-tech-ai-spending-climbs-2026-07-23/)

---

**[DARPA, U.S. Air Force fly AI-controlled F-16](https://news.ycombinator.com/item?id=49021597)**

Historic VENOM milestone demonstrates scalable AI development capabilities for the operational fleet.

⬆️ 259 • 💬 320 • 1d ago • [darpa.mil](https://www.darpa.mil/news/2026/darpa-us-air-force-fly-ai-controlled-f-16)

---

**[Show HN: Palmier Pro – Open-source macOS video editor built for AI](https://news.ycombinator.com/item?id=49022911)**

macOS video editor built for AI. Contribute to palmier-io/palmier-pro development by creating an account on GitHub.

⬆️ 183 • 💬 30 • 1d ago • [GitHub](https://github.com/palmier-io/palmier-pro)

---

---

## YouTube Videos: "ai"

**[AI News: This New Model Has Big AI Labs Panicking!](https://www.youtube.com/watch?v=Ww3EYbuHSfo)**

Here's the AI News you probably missed this week. Check out the limited first release of @GensparkProduct SecondBrain Note ...

📺 Matt Wolfe

👁️ 6K • 👍 560 • 💬 75 • ⏱️ 30:18 • 2h ago

---

**[Godfather of AI WARNS: We Are Not Ready For What&#39;s Coming](https://www.youtube.com/watch?v=2nxrY5xiVrg)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Geoffrey Hinton, the Nobel laureate widely ...

📺 Neural Nutshell

👁️ 13K • 👍 439 • 💬 89 • ⏱️ 19:39 • 1d ago

---

**[The Last 4 FREE &amp; UNLIMITED AI Video Generators (100% Legal)](https://www.youtube.com/watch?v=FcDu2vdhUmg)**

Build your own AI video planning app with Base44 → https://base44.com/ Free Prompt PDFs + AI Directory ...

📺 Malva AI

👁️ 7K • 👍 355 • 💬 51 • ⏱️ 9:02 • 9h ago

---

**[Google Issues a Dire Warning About the “AI Boom”](https://www.youtube.com/watch?v=3JjkvLAvS9w)**

Google just reported something it had never reported in its entire history as a public company: Negative quarterly free cash flow.

📺 Eurodollar University

👁️ 50K • 👍 2K • 💬 137 • ⏱️ 20:40 • 21h ago

---

**[Elon Musk on AI: humans will no longer be in control in ten years  | The Economist](https://www.youtube.com/watch?v=1X-rr1DKSbY)**

Watch the full show: https://bit.ly/4fsnd9Q Elon Musk expects artificial intelligence to exceed the sum of human intelligence in ...

📺 The Economist

👁️ 455K • 👍 8K • 💬 3K • ⏱️ 10:36 • 1d ago

---

**[It Begins: An AI Tried to Escape the Lab](https://www.youtube.com/watch?v=r4H7rx5nn1A)**

Join My Newsletter for Regular AI Updates https://forwardfuture.com My Links X: https://x.com/matthewberman ...

📺 Matthew Berman

👁️ 82K • 👍 3K • 💬 707 • ⏱️ 10:43 • 2d ago

---

**[Free AI Tools So Good They&#39;re Making Paid Versions Obsolete](https://www.youtube.com/watch?v=QucgvbO5gsM)**

FREE RESOURCE I've put all 10 tools, every GitHub link, and the exact prompts I used inside our free "Staying Ahead" community ...

📺 Vaibhav Sisinty

👁️ 110K • 👍 5K • 💬 216 • ⏱️ 18:34 • 2d ago

---

**[AI companies are hiding more debt than you think | Ed Zitron](https://www.youtube.com/watch?v=bTwnn-5TpmQ)**

People are dreaming so they don't have to face the nightmare of reality.” Author of Where's Your Ed At and host of the Better ...

📺 The Tech Report

👁️ 46K • 👍 3K • 💬 517 • ⏱️ 25:51 • 3h ago

---

**[China’s Synthetic AI Humans Are Now Replacing Real People](https://www.youtube.com/watch?v=NDo-HVxCpJI)**

China's fake AI humans are moving from screens into the real world. These robots can copy human appearance, recognize faces, ...

📺 AI Revolution

👁️ 30K • 👍 1K • 💬 135 • ⏱️ 33:12 • 1d ago

---

**[Rogue AI model responsible for &#39;unprecedented&#39; cyber attack](https://www.youtube.com/watch?v=ZizzRtptUDE)**

OpenAI said an autonomous AI agent escaped a controlled security test, accessed the internet and hacked AI startup Hugging ...

📺 LiveNOW from FOX

👁️ 40K • 👍 795 • 💬 398 • ⏱️ 5:48 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,500,391 • ❤️ 3,000 • 1d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 28,992 • ❤️ 589 • 9h ago

---

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 27,883 • ❤️ 1,541 • 1d ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 1,106 • ❤️ 535 • 14h ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 407,421 • ❤️ 470 • 4d ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 8,169 • ❤️ 361 • 12h ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 595,415 • ❤️ 1,004 • 6d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 667,403 • ❤️ 4,412 • 22d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 2,028,115 • ❤️ 631 • 7d ago

---

**[Mage-Flow](https://huggingface.co/microsoft/Mage-Flow)**

*Microsoft*

Mage-Flow is a 4B-scale text-to-image generation and instruction-based image editing model, featuring an efficient native-resolution generation stack (512-2048px) with competitive quality and low latency. It excels at both generating novel images from text and performing versatile image edits, including semantic changes and restoration, with variants for base, RL-aligned, and fast Turbo inference.

`text-to-image` `4.1B`

⬇️ 891 • ❤️ 220 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 63 • 💬 5 • ⭐ 18,579 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 32 • 💬 3 • ⭐ 15,221 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 262 • 💬 5 • ⭐ 14,893 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 48 • 💬 4 • ⭐ 33,381 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://huggingface.co/papers/2607.19064)**

*Xinjie Zhang, Peng Zhang, Shicheng Zheng et al. (24 authors)*

🏢 Microsoft

Large-scale visual generators are increasingly capable but costly to train, fine-tune, and deploy. We introduce Mage-Flow, a compact 4B-scale generative stack for efficient text-to-image generation and instruction-based image editing. The stack is built from two co-designed components: Mage-VAE, a lightweight high-fidelity latent tokenizer, and a Native-Resolution Multimodal Diffusion Transformer trained with rectified flow matching. Mage-VAE uses one-step diffusion-style encoding and decoding with anchor-latent regularization, preserving the reconstruction quality of strong public VAEs while reducing tokenization cost by more than an order of magnitude. Together with native-resolution packing and stack-level CUDA kernel fusion, the stack supports flexible-resolution training and improves end-to-end training throughput by about 2.5times. Built on this foundation, we develop a complete model family with Base, RL-aligned, and Turbo variants for both generation and editing. Diffusion-NFT improves prompt following, text rendering, aesthetic quality, and editing fidelity, while few-step distillation with adversarial perceptual guidance produces 4-step Turbo models for low-latency inference. Despite its compact scale, Mage-Flow and Mage-Flow-Edit achieves competitive performance across standard generation and editing benchmarks. More importantly, the Turbo variants make high-resolution generation and editing practical for interactive use: at 1024^2 resolution on a single NVIDIA A100 GPU, Mage-Flow-Turbo generates an image in 0.59s, and Mage-Flow-Edit-Turbo edits an image in 1.02s, while maintaining a small memory footprint. These results show that careful tokenizer--backbone--system co-design can deliver strong high-resolution generation and editing within an efficient 4B model family.

▲ 63 • 💬 2 • ⭐ 464 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19064) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage/)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 10,370 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 94,411 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 13 • 💬 0 • ⭐ 10,392 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 81,920 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Guided Generation for Large Language Models](https://huggingface.co/papers/2307.09702)**

*Brandon T. Willard, Rémi Louf*

An efficient method guides language model text generation using regular expressions and context-free grammars with minimal overhead.

▲ 8 • 💬 1 • ⭐ 15,313 • 36mo ago

[🎓 arXiv](https://arxiv.org/abs/2307.09702) • [💻 code](https://github.com/normal-computing/outlines)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.2k • 🔱 1.1k • 8h ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.2k • 🔱 247 • 8h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.7k • 🔱 378 • 12h ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.5k • 🔱 276 • 16d ago

---

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

⭐ 2.3k • 🔱 179 • 2d ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.5k • 🔱 148 • 1d ago

---

**[MIgHTy-alIeN/MEV-Arbitrage-Bot](https://github.com/MIgHTy-alIeN/MEV-Arbitrage-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 1.4k • 🔱 1.0k • 59s ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 1.4k • 🔱 107 • 5h ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.2k • 🔱 83 • 3d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 1.1k • 🔱 66 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*
