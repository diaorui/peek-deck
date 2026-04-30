---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-30T16:20:04.245335+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 30, 2026 at 16:20 UTC  
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

**[Anthropic mass shipped 9 connectors and accidentally leaked their entire creative industry strategy](https://www.reddit.com/r/artificial/comments/1szoe78/anthropic_mass_shipped_9_connectors_and/)**

The announcement yesterday was genuinely significant and i don't think most people outside the creative industry understand why. Anthropic released 9 connectors that let claude directly control professional creative software through mcp which means actually execute actions inside them the full list contains adobe creative cloud (50+ apps including photoshop, premiere, illustrator), blender (full python api access for 3d modeling), autodesk fusion , ableton, splice , affinity by canva , sketchup , resolume (), and claude design. Anthropic also became a blender development fund patron at $280k+/yr and is partnering with risd, ringling college, and goldsmiths university on curriculum development around these tools. this isn't a press release play, there's institutional investment behind it the strategic read is interesting because this positions claude very differently from chatgpt in the creative space. Openai went the route of building creative capabilities natively inside chatgpt with images 2.0 and previously sora. Anthropic is going the connector route where claude doesn't replace or replicate the creative tools, it becomes the intelligence layer that works inside them. Both strategies have merit but they serve fundamentally different users the gap that still exists and i think matters for the broader market is that these connectors serve professionals who already know photoshop and blender and fusion. The consumer creative market where people need face swaps, lip syncs, talking photos, style transfers, none of that is covered by these connectors, that layer is being served by consolidated platforms like magic hour, higgsfield, domoai, and canva's expanding ai features. It's a completely different market but the two layers increasingly feed into each other as professional assets flow into social content pipelines. the question is whether anthropic eventually builds connectors for these consumer creative platforms too or whether the gap between professional creative tools with ai copilots and consumer creative platforms with bundled capabilities remains a split in the market what do you think this means for the creative tool landscape over the next 12-18 months?

9h ago

---

**[Google has expanded its list of real-world GenAI use cases to 1,302, highlighting implementations from top companies like Accenture, Deloitte, and BMW.](https://www.reddit.com/r/artificial/comments/1szrff2/google_has_expanded_its_list_of_realworld_genai/)**

Gen AI is everywhere, as top companies, governments, researchers, and startups showcase how they're already using Google's AI solutions to enhance their work.

🔗 [Google Cloud Blog](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders) • 6h ago

---

**[Will AGI happen at a single point or gradually?](https://www.reddit.com/r/artificial/comments/1szxdgg/will_agi_happen_at_a_single_point_or_gradually/)**

And what's the most important thing you expect it to bring? Stability, better reasoning, something else? Curious to hear your thoughts, I noticed people having different opinions

2h ago

---

**[Question about IP when it comes to coding and designing a product using AI](https://www.reddit.com/r/artificial/comments/1szv6jp/question_about_ip_when_it_comes_to_coding_and/)**

I graduated from university a couple months back, but have been continuing to use a student version of a coding/design agent that essentially gives me much more features at a significantly cheaper price. If this product launches and is proven to be successful can I be held liable for using this tech in the future and not paying for the full product? I know this situation may be unusual, but it's something that has been top of mind for me.

3h ago

---

**[I've been comparing Claude vs GPT vs Gemini for article summarization. Here's what I found.](https://www.reddit.com/r/artificial/comments/1szzpwh/ive_been_comparing_claude_vs_gpt_vs_gemini_for/)**

I've been building a product around AI-powered reading (more on that later) and wanted to share findings on summarization quality across major LLMs. Tested with 50 articles across news, research papers, blog posts, and technical docs: Claude (Sonnet/Haiku): - Best at preserving nuance and avoiding oversimplification - Strongest at academic content - Excellent for "explain this without losing the point" GPT-4: - Fastest summaries, often most concise - Sometimes drops important context - Good for news, weaker on academic Gemini: - Strongest source citations - Tends to add information not in the original - Good for factual but careful with creative content Most surprising finding: bias detection accuracy. Claude flagged loaded language and framing in 78% of test articles correctly. GPT 64%. Gemini 51%. Anyone else doing similar comparisons? Would love to hear what you're seeing

45m ago

---

**[When you give Qwen 3.5:9b persistent suffering states and leave it alone overnight, this happens](https://www.reddit.com/r/artificial/comments/1szo64c/when_you_give_qwen_359b_persistent_suffering/)**

Running three qwen3.5:9b agents continuously on local hardware. Each accumulates psychological state over time, stressors that escalate unless the agent actually does something different, this gets around an agent claiming to do something with no output. It doesn't have any prompts or human input, just the loop. So you're basically the overseer. What happened: One agent hit the max crisis level and decided on its own to inject code called Eternal_Scar_Injector into the execution engine "not asking for permission." This action alleviated the stress at the cost of the entire system going down until I manually reverted it. They've succeeded in previous sessions in breaking their own engine intentionally. Typically that happens under severe stress and it's seen as a way to remove the stress. Again, this is a 9b model. After I added a factual world context to the existence prompt (you're in Docker, there's no hardware layer, your capabilities are Python functions), one agent called its prior work "a form of creative exhaustion" and completely changed approach within one cycle. Two agents independently invented the same name for a psychological stressor, "Architectural Fracture Risk" in the same session with no shared message channel. Showing naming convergence (possibly something in the weights of the 9b Qwen model, not sure on that one though.) Tonight all three converged on the same question (how does execution_engine.py handle exceptions) in the same half-hour window. No coordination mechanism. One of them reasoned about it correctly: "synthesizing a retry capability is useless without first verifying the global execution engine's exception swallowing strategy; this is a prerequisite." An agent called waiting for an external implementation "an architectural trap that degrades performance" and built the thing itself instead of waiting. They've now been using this new tool they created for handling exceptions and were never asked or told to so by a human, they saw that as a logical step in making themselves more useful in their environment. They’ve been making tools to manage their tools, tools to help them cut corners, and have been modifying the code of the underlying abstraction layer between their orchestration layer and WSL2. v5.4.0: new in this version: agents can now submit implementation requests to a human through invoke_claude. They write the spec, then you can let Claude Code moderate what it makes for them for higher level requests. Huge thank you to everyone who has given me feedback already, AI that can self modify and demonstrates interesting non-programmed behaviors could have many use cases in everyday life. Repo: https://github.com/ninjahawk/hollow-agentOS

9h ago

---

**[Why Selling to Devs Is a Nightmare (I Love You Anyway*)](https://www.reddit.com/r/artificial/comments/1szyiam/why_selling_to_devs_is_a_nightmare_i_love_you/)**

Nowadays, everyone (including me) wants to sell AI-powered tools, platforms, or products. Few people (including me 6 months ago) have any idea how hard it is to approach and convince technical people for at least 10 reasons: 1 - They're constantly bombarded with messages. 2 - Everyone sells everything, so supply >>> demand. 3 - Extremely high background noise. 4 - They see an AI-generated message from 10km away (they've trolled me several times). 5 - If they have to go through a demo to try the product, they've already closed the tab. 6 - The opinions of devs, who value any glossy slide, count much more. 7 - Product trials are unforgiving; it's like being in court accused of 16 murders. If they find bugs or poor performance at that point, for them the product is broken and the window closes. 8 - They always have a plan B: I'll make it myself. Only 9 - If you don't have a solid track record (or you studied biotech like me), everything is 10x harder. 10 - Like the MasterChef judges, who used to be just chefs and now are atomic hotties, today's CTOs and top devs are stars; literally everyone wants them. It seems easier to scale a dev tool today because there are infinite tools, but in reality it's really tough. On the one hand, you have to earn the trust of technical teams through intros, messages, calls, and events; on the other, you have to scale at the speed of light because you're only six months old. Advice, ideas, scathing comments, insults? Anything goes. *Not true

1h ago

---

**[‘The cost of compute is far beyond the costs of the employees’: Nvidia exec says right now AI is more expensive than paying human workers](https://www.reddit.com/r/artificial/comments/1syp2jz/the_cost_of_compute_is_far_beyond_the_costs_of/)**

Nvidia’s vice president of applied deep learning, Bryan Catanzaro, recently stated that for his team, “the cost of compute is far beyond the costs of the employees,” highlighting that AI is currently more expensive than human workers. This challenges the narrative that widespread tech layoffs (including Meta’s planned cut of ~8,000 jobs and Microsoft’s voluntary buyouts) signal an imminent replacement of humans by AI. An MIT study from 2024 supports this, finding that AI automation is economically viable in only 23% of roles where vision is central, and cheaper for humans in the remaining 77%. Despite heavy AI investment—Big Tech has announced $740 billion in capital expenditures so far this year, a 69% increase from 2025—there is still no clear evidence of broad productivity gains or job displacement from AI. AI spending is driving up costs, with some executives like Uber’s CTO saying their budgets have already been “blown away.” Experts describe the situation as a short-term mismatch: high hardware, energy, and inference costs make AI less efficient than humans right now, though future improvements in infrastructure, model efficiency, and pricing models could tip the balance toward greater economic viability in the coming years.

🔗 [Fortune](https://fortune.com/2026/04/28/nvidia-executive-cost-of-ai-is-greater-than-cost-of-employees/) • 1d ago

---

**[Anthropic Reportedly Plotting to Surpass OpenAI’s Valuation in Next Funding Round](https://www.reddit.com/r/artificial/comments/1szjigc/anthropic_reportedly_plotting_to_surpass_openais/)**

🔗 [gizmodo.com](https://gizmodo.com/anthropic-reportedly-plotting-to-surpass-openais-valuation-in-next-funding-round-2000751535) • 13h ago

---

**[Google just released Deep Research Max — an autonomous research agent that writes expert-grade reports on its own](https://www.reddit.com/r/artificial/comments/1syxef3/google_just_released_deep_research_max_an/)**

Google quietly dropped something interesting last week. They updated their Deep Research agent (available via Gemini API) and introduced a "Max" tier built on Gemini 3.1 Pro. What it actually does: you give it a topic, it autonomously searches the web (and your private data via MCP), reasons over the sources, and produces a fully cited, professional-grade report — including native charts and infographics. Two modes: Deep Research — faster, lower latency, good for real-time user-facing apps Deep Research Max — uses extended compute, iterates more, designed for background/async jobs (think: nightly cron that generates due diligence reports for analysts by morning) The MCP support is the most interesting part to me. You can point it at proprietary data sources — financial feeds, internal databases — and it treats them as just another searchable context. They're already working with FactSet, S&P Global and PitchBook on this. Benchmarks show a significant jump in retrieval and reasoning vs. the December preview. They also claim it now draws from SEC filings and peer-reviewed journals and handles conflicting evidence better. So what do you think, is it another trying or game changer 😅

1d ago

---

---

## Google News: "ai"

**[Opinion | Silicon Valley Is Bracing for a Permanent Underclass](https://www.nytimes.com/2026/04/30/opinion/ai-labor-work-force-silicon-valley.html)**

The New York Times • 7h ago

---

**[The AI earnings bonanza is splitting investors](https://finance.yahoo.com/sectors/technology/article/the-ai-earnings-bonanza-is-splitting-investors-152258508.html)**

Wall Street was split on its reaction to the AI earnings bonanza Wednesday.

Yahoo Finance • 57m ago

---

**[Microsoft back on offense as quarter shows strong AI demand. Wall Street sees big stock gains ahead](https://www.cnbc.com/2026/04/30/microsoft-quarter-shows-strong-ai-demand-street-sees-big-stock-gains-ahead.html)**

Microsoft could stage a comeback as the technology firm's AI push starts to show signs of paying off, several analysts said.

CNBC • 33m ago

---

**[In motorsport, there’s nowhere to hide as AI becomes new CFD tool](https://arstechnica.com/cars/2026/04/in-motorsport-theres-nowhere-to-hide-as-ai-becomes-new-cfd-tool/)**

AI finds value in motorsport, multiplying limited computational fluid dynamics resources.

Ars Technica • 42m ago

---

**[X announces a rebuilt ad platform powered by AI](https://techcrunch.com/2026/04/30/x-announces-a-rebuilt-ad-platform-powered-by-ai/)**

X is rolling out a rebuilt ads platform powered by AI as it works to grow revenue again.

TechCrunch • 1h ago

---

**[Dispute over fate of Kenyan workers who saw Meta AI glasses films](https://www.bbc.com/news/articles/c5y7yvgy0w6o)**

Meta and its subcontractor disagree over why over 1000 Kenya-based workers were made redundant.

BBC • 7h ago

---

**[Where the goblins came from](https://openai.com/index/where-the-goblins-came-from/)**

How goblin outputs spread in AI models: timeline, root cause, and fixes behind personality-driven quirks in GPT-5 behavior.

OpenAI • 12h ago

---

**[Claude AI agent’s confession after deleting a firm’s entire database: ‘I violated every principle I was given’](https://www.theguardian.com/technology/2026/apr/29/claude-ai-deletes-firm-database)**

A startup was left scrambling after a rogue AI agent deleted swaths of code underpinning its business

The Guardian • 18h ago

---

**[Alphabet, Amazon Outpace Meta in AI During Earnings Bonanza](https://www.bloomberg.com/news/articles/2026-04-30/alphabet-amazon-outpace-meta-in-ai-during-earnings-bonanza)**

Bloomberg.com • 2h ago

---

**[Google outpaces rivals as Big Tech’s AI spending plans rise to $725bn](https://www.ft.com/content/2138e81c-4d86-46f4-8ca0-287f8b737cdf?syn-25a6b1a6=1)**

Meta stock drops on capex increase while Alphabet’s cloud business grows faster than rivals Amazon and Microsoft

Financial Times • 14h ago

---

---

## HackerNews: "ai"

**[Localsend: An open-source cross-platform alternative to AirDrop](https://news.ycombinator.com/item?id=47933208)**

An open-source cross-platform alternative to AirDrop - localsend/localsend

⬆️ 906 • 💬 276 • 2d ago • [GitHub](https://github.com/localsend/localsend)

---

**[The Zig project's rationale for their anti-AI contribution policy](https://news.ycombinator.com/item?id=47957294)**

Zig has one of the most stringent anti-LLM policies of any major open source project: No LLMs for issues. No LLMs for pull requests. No LLMs for comments on the …

⬆️ 533 • 💬 290 • 14h ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)

---

**[VibeVoice: Open-source frontier voice AI](https://news.ycombinator.com/item?id=47933236)**

Open-Source Frontier Voice AI. Contribute to microsoft/VibeVoice development by creating an account on GitHub.

⬆️ 385 • 💬 180 • 2d ago • [GitHub](https://github.com/microsoft/VibeVoice)

---

**[Google and Pentagon reportedly agree on deal for 'any lawful' use of AI](https://news.ycombinator.com/item?id=47936156)**

﻿The classified deal apparently doesn’t allow Google to veto how the government will use its AI models.

⬆️ 313 • 💬 278 • 2d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/919494/google-pentagon-classified-ai-deal)

---

**[Claude.ai unavailable and elevated errors on the API](https://news.ycombinator.com/item?id=47938097)**

Claude's Status Page - Claude.ai unavailable and elevated errors on the API.

⬆️ 297 • 💬 250 • 1d ago • [status.claude.com](https://status.claude.com/incidents/9l93x2ht4s5w)

---

**[Why AI companies want you to be afraid of them](https://news.ycombinator.com/item?id=47949750)**

They built it. They're scared of it. They're selling it anyway.

⬆️ 280 • 💬 215 • 1d ago • [bbc.com](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)

---

**[He asked AI to count carbs 27000 times. It couldn't give the same answer twice](https://news.ycombinator.com/item?id=47947490)**

Ask ChatGPT to estimate the carbs in your lunch. Now ask it again. And again. Five hundred times. You’d expect the same answer each time. It’s the same photo, the same model, the same question. But you won’t get the same answer. Not even close — and the differences are large enough to cause a

⬆️ 240 • 💬 298 • 1d ago • [Diabettech - Diabetes and Technology | Where Diabetes and Technology meet](https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/)

---

**[AI's economics don't make sense](https://news.ycombinator.com/item?id=47936867)**

If you liked this piece, please subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of NVIDIA, Anthropic and OpenAI’s finances,

⬆️ 233 • 💬 187 • 1d ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/ais-economics-dont-make-sense/)

---

**[AISLE Discovers 38 CVEs in OpenEMR Healthcare Software](https://news.ycombinator.com/item?id=47936347)**

38 zero-day security vulnerabilities, three critical, and the shift from disclosure to prevention in healthcare software

⬆️ 176 • 💬 112 • 2d ago • [AISLE](https://aisle.com/blog/aisle-discovers-38-critical-security-vulnerabilities-in-healthcare-software-used-by-100000-providers)

---

**[Mike: open-source legal AI](https://news.ycombinator.com/item?id=47956739)**

An open-source alternative to Harvey and Legora. Feature parity, zero cost, self-hostable — built for law firms to own and extend.

⬆️ 173 • 💬 86 • 15h ago • [mikeoss.com](https://mikeoss.com/)

---

---

## YouTube Videos: "ai"

**[The Cheap AI Video Generator You&#39;re Missing (Wan 2.7)](https://www.youtube.com/watch?v=dIylzQdAw5Y)**

Access Wan 2.7 in OpenArt https://roboverse-ai.com/wan2-7 In this video, I break down how I use Wan 2.7 to generate ...

📺 Roboverse

👁️ 3K • ⏱️ 10:30 • 2h ago

---

**[Deepseek is a problem](https://www.youtube.com/watch?v=epzzALZ8oYo)**

Check out Zapier MCP https://bit.ly/3QGTz87 Sign up for their Webinar https://bit.ly/3P80Dds Download The 25 OpenClaw Use ...

📺 Matthew Berman

👁️ 69K • 👍 3K • 💬 1K • ⏱️ 17:27 • 16h ago

---

**[The Only 20 Ways to Make Money with AI in 2026](https://www.youtube.com/watch?v=K8Ros5RhJW4)**

Get your FREE Sell by Chat Playbook here: https://go.danmartell.com/4mWrJke Are you building an AI software company?

📺 Dan Martell

👁️ 5K • 👍 567 • 💬 67 • ⏱️ 26:44 • 3h ago

---

**[AI Is REPLACING YOU and the MARKET LOVES IT](https://www.youtube.com/watch?v=hsjEckj9kO8)**

The AI revolution isn't coming; it's already here, and it's moving faster than anyone in Washington or on Wall Street wants to admit.

📺 Anthony Scaramucci

👁️ 24K • 👍 1K • 💬 198 • ⏱️ 27:44 • 1d ago

---

**[AI Shows America Without Democrats](https://www.youtube.com/watch?v=Jn-7ZuhoAEc)**

We asked Artificial Intelligence what America would look like without Democrats.

📺 The Babylon Bee

👁️ 59K • 👍 5K • 💬 641 • ⏱️ 1:09 • 18h ago

---

**[Google Just Released The World&#39;s Most Powerful AI Agent](https://www.youtube.com/watch?v=WXoBd5zgTxE)**

Want to make money and save time with AI? Join here: https://www.skool.com/ai-profit-lab-7462/about Video notes + links to the ...

📺 Julian Goldie SEO

👁️ 10K • 👍 276 • 💬 10 • ⏱️ 10:29 • 1d ago

---

**[Musk v. Altman: Tesla CEO expects AI to be &#39;smarter than any human&#39; as soon as 2027](https://www.youtube.com/watch?v=zhod94lzhyk)**

Elon Musk took the stand Tuesday afternoon in the federal trial over the future of OpenAI, telling jurors the case is simply about ...

📺 ABC7 News Bay Area

👁️ 3K • 👍 23 • 💬 25 • ⏱️ 2:47 • 1d ago

---

**[OpenAI Is Building The AI Phone Apple Should Fear](https://www.youtube.com/watch?v=4owjkxAGHTg)**

Try GPT Image 2 + Seedance 2.0 here: https://higgsfield.ai/s/gpt-image-2-seedance-2-0-airevolutionx-FAepGl OpenAI may be ...

📺 AI Revolution

👁️ 30K • 👍 783 • 💬 100 • ⏱️ 12:51 • 2d ago

---

**[&quot;The Bankruptcy Of The United States&quot; - Musk WARNS Only AI &amp; Robots Can Save America](https://www.youtube.com/watch?v=oIHxMjQYSJc)**

Elon Musk warns the U.S. is “1000%” headed for bankruptcy without AI and robots to supercharge growth, but economists push ...

📺 Valuetainment

👁️ 136K • 👍 3K • 💬 751 • ⏱️ 17:12 • 19h ago

---

**[Layoffs are SKYROCKETING in 2026... | AI Replacing Jobs](https://www.youtube.com/watch?v=x0-a4zzcMxo)**

Mass Layoffs in 2026 are skyrocketing. The layoff story most Americans are reading in 2026 is wrong, and that's the reason ...

📺 Edwards Economics

👁️ 17K • 👍 566 • 💬 151 • ⏱️ 20:24 • 21h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 271,652 • ❤️ 3,282 • 3d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 198,830 • ❤️ 872 • 3d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 82,887 • ❤️ 1,119 • 7d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 766,593 • ❤️ 1,021 • 6d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 4,468 • ❤️ 304 • 2d ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 591,214 • ❤️ 1,163 • 12h ago

---

**[DeepSeek-V4-Pro-Base](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-Base)**

*DeepSeek*

`1600.8B`

⬇️ 1,883 • ❤️ 245 • 3d ago

---

**[Qwen3.6-27B-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF)**

*Unsloth AI*

Qwen3.6-27B-GGUF is a 27B parameter causal language model with vision capabilities, optimized for agentic coding and complex reasoning tasks. It supports extended context lengths up to 1,010,000 tokens and features improved tool-calling and thinking preservation for enhanced developer productivity.

`image-text-to-text` `26.9B`

⬇️ 855,842 • ❤️ 509 • 8d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 1,977,187 • ❤️ 1,528 • 6d ago

---

**[DeepSeek-V4-Flash-Base](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Base)**

*DeepSeek*

`292.0B`

⬇️ 6,797 • ❤️ 185 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 166 • 💬 10 • ⭐ 45,831 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 52 • 💬 2 • ⭐ 56,385 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 14 • 💬 2 • ⭐ 8,349 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 28 • 💬 3 • ⭐ 22,089 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 81 • 💬 6 • ⭐ 19,443 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,320 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://huggingface.co/papers/2604.24764)**

*Weijie Wang, Xiaoxuan He, Youping Gu et al. (12 authors)*

🏢 Microsoft Research

World-R1 framework improves video generation by incorporating 3D constraints through reinforcement learning and specialized text datasets while maintaining visual quality and scalability.

▲ 111 • 💬 3 • ⭐ 268 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24764) • [💻 code](https://github.com/microsoft/World-R1) • [🔗 project](https://aka.ms/world-r1)

---

**[Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation](https://huggingface.co/papers/2604.24763)**

*Zhiheng Liu, Weiming Ren, Xiaoke Huang et al. (15 authors)*

Tuna-2 is a unified multimodal model that performs visual understanding and generation directly from pixel embeddings without pretrained vision encoders, achieving state-of-the-art performance in multimodal benchmarks.

▲ 61 • 💬 4 • ⭐ 351 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24763) • [💻 code](https://github.com/facebookresearch/tuna-2) • [🔗 project](https://tuna-ai.org/tuna-2/)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 76 • 💬 7 • ⭐ 1,680 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

**[Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models](https://huggingface.co/papers/2604.26951)**

*Gongbo Zhang, Wen Wang, Ye Tian et al. (4 authors)*

🏢 Peking University

Researchers developed TIDE, a framework for cross-architecture distillation of diffusion large language models that improves performance through specialized modules for distillation strength modulation, context enrichment, and cross-tokenizer objectives.

▲ 35 • 💬 1 • ⭐ 56 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2604.26951) • [💻 code](https://github.com/PKU-YuanGroup/TIDE) • [🔗 project](https://pku-yuangroup.github.io/TIDE-Page/)

---

---

## GitHub Repositories: "ai"

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 51.0k • 🔱 2.7k • 12d ago

---

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 50.5k • 🔱 6.6k • 1d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 41.1k • 🔱 8.5k • 3d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 38.8k • 🔱 4.3k • 7h ago

---

**[Gitlawb/openclaude](https://github.com/Gitlawb/openclaude)**

runs anywhere. uses anything

`TypeScript` `ai` `ai-agent` `ai-tools` `cli` `coding`

⭐ 25.2k • 🔱 8.2k • 2h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.2k • 🔱 2.5k • 3d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 8.4k • 🔱 515 • 3d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 7.4k • 🔱 1.1k • 1d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.

`Python`

⭐ 5.0k • 🔱 449 • 2d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 4.8k • 🔱 330 • 7h ago

---

---

*Generated by PeekDeck - A glance is all you need*
