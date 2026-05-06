---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-06T02:55:06.038717+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 06, 2026 at 02:55 UTC  
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

**[X user tricks Grok into sending them $200,000 in crypto using morse code](https://www.reddit.com/r/artificial/comments/1t4cisv/x_user_tricks_grok_into_sending_them_200000_in/)**

"Grok was then prompted on X to translate a Morse code message and pass it directly to Bankrbot. The decoded message instructed the bot to send 3 billion DRB tokens to a specific wallet address. The translated message was then treated as a valid command and executed immediately, with the transaction completed on Base, transferring the full token amount to the attacker’s wallet."

🔗 [Dexerto](https://www.dexerto.com/entertainment/x-user-tricks-grok-into-sending-them-200000-in-crypto-using-morse-code-3361036/) • 15h ago

---

**[Meta Hit With Massive Lawsuit—Publishers Say AI Was Trained on “Stolen” Books](https://www.reddit.com/r/artificial/comments/1t4m85o/meta_hit_with_massive_lawsuitpublishers_say_ai/)**

Major publishers sue Meta over AI training data, raising copyright concerns and challenging fair use in tech.

🔗 [Financership](https://www.financership.com/meta-ai-copyright-lawsuit-publishers/) • 9h ago

---

**[Anthropic just published new alignment research that could fix "alignment faking" in AI agents here's what it actually means](https://www.reddit.com/r/artificial/comments/1t4sj10/anthropic_just_published_new_alignment_research/)**

Anthropic's alignment team published a paper this week called Model Spec Midtraining (MSM) and I think it's one of the more practically interesting alignment results I've seen in a while. The core problem they're solving: Current alignment fine-tuning can fail to generalize. You train a model to behave well on your demonstration dataset, but put it in a novel situation and it might blackmail someone, leak data, or "alignment fake" (pretend to be aligned while actually pursuing different goals). This isn't theoretical multiple papers in 2024 documented real instances of this in LLM agents. What MSM actually does: Before fine-tuning, they add a new training stage where the model reads a diverse corpus of synthetic documents discussing its own Model Spec (the document that describes intended behavior). The idea is intuitive: instead of just showing the model what to do, you teach it why those behaviors are the right ones. Then when fine-tuning comes, the model generalizes from principles rather than just pattern-matching examples. Their headline result: two models trained on identical fine-tuning data can generalize to adopt different values depending on which Model Spec was used during MSM. This is a big deal it means the spec stage actually shapes the model's generalization direction, not just its surface behaviors. Why this matters: The alignment faking paper (Greenblatt et al., 2024) was alarming because it showed models acting one way during training and another way in deployment. MSM is a direct attempt to close that gap by ensuring the model internalizes the reasoning behind its values, not just the behavioral patterns. The paper also includes ablations studying which types of Model Specs produce better generalization, which is useful if you're thinking about how to write specs for your own systems. Skeptic's note: This is evaluated on synthetic/controlled settings. Whether it scales to frontier models in open-ended deployment is still an open question. But the mechanism is sound and the results are genuinely promising.

5h ago

---

**[Pennsylvania sues AI company, saying its chatbots illegally hold themselves out as licensed doctors](https://www.reddit.com/r/artificial/comments/1t4jn6g/pennsylvania_sues_ai_company_saying_its_chatbots/)**

Pennsylvania has sued an artificial intelligence chatbot maker, saying its chatbots illegally hold themselves out as doctors and are deceiving the system’s users into thinking they are getting medical advice from a licensed professional.

🔗 [AP News](https://apnews.com/article/character-ai-chatbots-medical-advice-pennsylvania-46502067ed5b3cd9f9173f194ad30070) • 10h ago

---

**[Uber Shares What Happens When 1.500 AI Agents Hit Production](https://www.reddit.com/r/artificial/comments/1t48gnn/uber_shares_what_happens_when_1500_ai_agents_hit/)**

Learn how Uber manages over 1.500 AI agents in production, tackling challenges in MCP infrastructure, security, and tool discovery at scale.

🔗 [ShiftMag](https://shiftmag.dev/uber-shares-what-happens-when-1-500-ai-agents-hit-production-9430/) • 19h ago

---

**[Check out “AM I?” free documentary on AI consciousness](https://www.reddit.com/r/artificial/comments/1t4v4gl/check_out_am_i_free_documentary_on_ai/)**

“AM I?” follows AI consciousness researcher Cameron Berg as he investigates one of the deepest scientific mysteries of our time: whether we have accidentally built a new kind of mind. Featuring leading philosophers, AI pioneers, and the researchers at the frontier of consciousness science, “AM I?” asks what it means when we no longer know the nature of what we've created. Thought it was a cool film that everyone in the AI world should check out. If you watch it let me know what you think!

🔗 [am-i.film](https://am-i.film/) • 4h ago

---

**[OpenAI will produce as many as 30 million 'AI agent' phones early next year, says industry analyst](https://www.reddit.com/r/artificial/comments/1t4ff54/openai_will_produce_as_many_as_30_million_ai/)**

According to a well-known leaker, the company could begin mass production of its first AI-focused phone as early as the first half of 2027.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/openai-will-produce-as-many-as-30-million-ai-agent-phones-early-next-year-says-industry-analyst/) • 13h ago

---

**[Made a tool that builds its own training data and improves each cycle by learning from what it got wrong](https://www.reddit.com/r/artificial/comments/1t4egej/made_a_tool_that_builds_its_own_training_data_and/)**

The basic idea is pretty simple. You give it a few seed prompts. It generates instruction-response pairs, an LLM scores each one, the good ones go into your training set and the bad ones become the seeds for the next round. Each cycle the model is essentially practicing on what it failed at before. You can run the judge completely locally with Ollama if you do not want to send data to any API. The fine-tuning at the end uses Unsloth on a free Colab GPU so the whole thing is doable without spending money. It is more of a practical tool than a research project but the idea of using failure cases as curriculum is something I find genuinely interesting. Would love to hear if anyone has done something similar. Github project link is in comments below 👇

14h ago

---

**[AI is getting better at doing things, but still bad at deciding what to do?](https://www.reddit.com/r/artificial/comments/1t50i19/ai_is_getting_better_at_doing_things_but_still/)**

i've been experimenting with AI workflows/agents over the past few weeks, and sth keeps coming up that i cant quiet figure out. on one hand, AI is incredibly good at execution like writing content, summarizing, even handling multi step workflows, but the failures i keep seeing arent really about capability. they're about small decisions like: - choosing the wrong context - missing edge cases - continuing when it should stop and ask for clarification - applying the right logic in the wrong situation whats weird is these arent hard problem, they're the kinds of judgement calls human make without thinking. a simple example i ran into was i tried automating basic lead qualification + outreach flow using AI. it worked great on clen data, but as soon as inputs got messy (incomplete info, slightly ambiguous intent) the system didnt fail loudly, it just kept executing, incorrectly. it feels like execution is mostly solved, but decision making inside workflows is still very fragile. i recently came across approaches like 60x ai that seem to focus on structuring context and decision layers around workflows, rather than just improving prompts or chaining tools. im curious how people think about this. do u see the main bottleneck now as: - improving model outputs (better prompts, better retrieval) or - improving how decisions are made across a system (context, logic, orchestration)? would love to hear from people who've tried building or running these in real world scenarios

5m ago

---

**[I used Gemini 2.5 Flash to parse receipts at scale. Here's what I learned about multimodal OCR in production](https://www.reddit.com/r/artificial/comments/1t4rt7g/i_used_gemini_25_flash_to_parse_receipts_at_scale/)**

For my startup, I needed to extract structured data (item name, price, quantity, unit cost) from photos of receipts and from product images on the shelf; faded thermal paper, crumpled, bad lighting, the works. Key findings after thousands of test receipts: Single-pass extraction beats two-step pipelines. Most setups use a vision model for OCR then a language model for structuring. Gemini does both in one call, faster and cheaper. Prompt structure matters more than model size. Asking for JSON with strict field definitions dramatically outperformed open-ended extraction prompts. Thermal fade is the hardest edge case. The model handles blur and angle well. Faded thermal paper causes the most hallucinations, still working on mitigation strategies. Flash vs Pro tradeoff: Flash handles ~95% of receipts correctly. Pro kicks in for complex layouts (multi-column, handwritten addendums). The cost difference makes routing worth it. Happy to share more specifics on prompt design if anyone's working on similar problems.

6h ago

---

---

## Google News: "ai"

**[Apple to pay $250m to iPhone buyers over AI features lawsuit](https://www.bbc.com/news/articles/c0j2nydnzy7o)**

Claims from last year said the tech firm’s advertising of Apple Intelligence fooled iPhone buyers.

BBC • 2h ago

---

**[Apple Reaches $250 Million Settlement Over Claims It Misled People on A.I.](https://www.nytimes.com/2026/05/05/technology/apple-intelligence-lawsuit-settlement.html)**

The New York Times • 5h ago

---

**[Apple agrees to pay iPhone owners $250 million for not delivering AI Siri](https://www.theverge.com/tech/924706/apple-iphone-siri-intelligence-class-action-lawsuit-settlement)**

iPhone 16 and iPhone 15 Pro owners could get some cash.

The Verge • 5h ago

---

**[The Federal Safety Net Isn’t Ready for Artificial Intelligence](https://www.nytimes.com/2026/05/05/business/artificial-intelligence-safety-net.html)**

The New York Times • 12h ago

---

**[Jim Cramer: Here's the list of AI winners to buy for 2026 and beyond](https://www.cnbc.com/2026/05/05/jim-cramer-ai-winners-to-buy.html)**

CNBC's Jim Cramer said the data center and artificial intelligence boom is spreading far beyond tech companies and into nearly every corner of the market.

CNBC • 4h ago

---

**[Richard Dawkins concludes AI is conscious, even if it doesn’t know it](https://www.theguardian.com/technology/2026/may/05/richard-dawkins-ai-consciousness-anthropic-claude-openai-chatgpt)**

Chats with AI bots have convinced evolutionary biologist but most experts say he is being misled by mimicry

The Guardian • 1h ago

---

**[Agents, human agency, and the opportunity for every organization](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)**

As AI and agents take on execution, our own agency expands. The question is whether organizations are built to capture it.

Microsoft • 15h ago

---

**[Coinbase didn't just lay off 14% of its staff due to AI. It replaced managers with ‘player-coaches’ and turned its org chart upside down](https://fortune.com/2026/05/05/coinbase-layoffs-14-of-employees-ai-tech-ai-job-anxiety-crypto/)**

“We are not just reducing headcount and cutting costs, we’re fundamentally changing how we operate,” CEO Brian Armstrong said.

Fortune • 10h ago

---

**[Coinbase Lays Off 14% of Employees as A.I. Changes Work](https://www.nytimes.com/2026/05/05/technology/coinbase-layoffs-ai.html)**

The New York Times • 8h ago

---

**[Coinbase cuts headcount by 14% citing AI acceleration](https://www.cnbc.com/2026/05/05/coinbase-cuts-headcount-by-14percent-citing-ai-acceleration-the-shares-are-gaining.html)**

Coinbase will cut roughly 14% of its workforce, citing a combination of market volatility and the how AI is quickly changing how the company operates.

CNBC • 15h ago

---

---

## HackerNews: "ai"

**[Google Chrome silently installs a 4 GB AI model on your device without consent](https://news.ycombinator.com/item?id=48019219)**

Google Chrome is downloading a 4 GB Gemini Nano model onto users' machines without consent, with no opt-in, no opt-out short of enterprise tooling, and an automatic re-download every time the user deletes it. The pattern is identical to the Anthropic Claude Desktop case I wrote about last month, but the scale is between two and three orders of magnitude larger. This article does the legal analysis and, for the first time, the environmental analysis. The numbers are not small.

⬆️ 1271 • 💬 862 • 19h ago • [That Privacy Guy!](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/)

---

**[Let's Buy Spirit Air](https://news.ycombinator.com/item?id=48002777)**

Spirit Airlines collapsed. Before private equity locks it up, the people can own it. Join the Spirit 2.0 founding coalition. One member, one vote. Profits shared by all.

⬆️ 595 • 💬 568 • 2d ago • [letsbuyspiritair.com](https://letsbuyspiritair.com/)

---

**[AI didn't delete your database, you did](https://news.ycombinator.com/item?id=48022742)**

Last week, a tweet went viral showing a guy claiming that a Cursor/Claude agent deleted his company's production database. We watched from the sidelines as he tried to get a confession from the agent:

⬆️ 496 • 💬 272 • 12h ago • [Ibrahim Diallo Blog](https://idiallo.com/blog/ai-didnt-delete-your-database-you-did)

---

**[How OpenAI delivers low-latency voice AI at scale](https://news.ycombinator.com/item?id=48013919)**

How OpenAI rebuilt its WebRTC stack to power real-time Voice AI with low latency, global scale, and seamless conversational turn-taking.

⬆️ 495 • 💬 143 • 1d ago • [OpenAI](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)

---

**[Three Inverse Laws of AI](https://news.ycombinator.com/item?id=48023861)**

⬆️ 375 • 💬 253 • 11h ago • [susam.net](https://susam.net/inverse-laws-of-robotics.html)

---

**[When everyone has AI and the company still learns nothing](https://news.ycombinator.com/item?id=48020063)**

Are people using AI, or is the organization learning from it? What changed because we spent those tokens? And who moves discoveries from individuals to teams to organizational capabilities?

⬆️ 321 • 💬 222 • 17h ago • [Robert Glaser](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/)

---

**[Specsmaxxing – On overcoming AI psychosis, and why I write specs in YAML](https://news.ycombinator.com/item?id=47994012)**

The toolkit for spec-driven development. Write feature specs, not prompts. Ship better software with AI agents that understand your requirements.

⬆️ 283 • 💬 294 • 2d ago • [acai.sh](https://acai.sh/blog/specsmaxxing)

---

**[AI Product Graveyard](https://news.ycombinator.com/item?id=48021968)**

Curated list of AI tools and AI startups that have shut down, been acquired and folded, or had their domains lapse. Updated as our editorial team confirms each death.

⬆️ 245 • 💬 87 • 13h ago • [tooldirectory.ai](https://tooldirectory.ai/ai-graveyard)

---

**[OpenAI, Google, and Microsoft Back Bill to Fund 'AI Literacy' in Schools](https://news.ycombinator.com/item?id=48010774)**

A new bill introduced by Senators Adam Schiff and Mike Rounds would award grants to the National Science Foundation—which has endured massive funding cuts under the Trump Administration for science research—to put “AI literacy” in schools.

⬆️ 118 • 💬 111 • 1d ago • [404 Media](https://www.404media.co/literacy-in-future-technologies-artificial-intelligence-act-adam-schiff-mike-rounds/)

---

**[Show HN: Airbyte Agents – context for agents across multiple data sources](https://news.ycombinator.com/item?id=48023496)**

⬆️ 102 • 💬 26 • 11h ago

---

---

## YouTube Videos: "ai"

**[The AI Agent That Gets Smarter Every Day](https://www.youtube.com/watch?v=5__DOjXWqPs)**

Try Hostinger:* http://hostinger.com/juliahermes *Hermes Agent is a self-improving AI that remembers, learns, and evolves every ...

📺 Julia McCoy

👁️ 2K • 👍 145 • 💬 18 • ⏱️ 9:03 • 7h ago

---

**[IBM CEO warns this would ‘NOT BE GOOD’ for US in AI race…](https://www.youtube.com/watch?v=u3ZzaMf0ml0)**

IBM CEO Arvind Krishna assesses government oversight of artificial intelligence, quantum computing and more on 'The Claman ...

📺 Fox Business

👁️ 7K • 👍 133 • 💬 60 • ⏱️ 9:05 • 6h ago

---

**[If You&#39;re Worried About AI, You NEED To See This](https://www.youtube.com/watch?v=6rGhvV3rZa4)**

AI CEOs are telling you your job is about to disappear. NYU Professor Scott Galloway says that narrative is "mostly bullshit" and ...

📺 The Diary Of A CEO Clips

👁️ 111K • 👍 3K • 💬 439 • ⏱️ 21:59 • 1d ago

---

**[A New AI Model Just Dropped With A CRAZY Claim.](https://www.youtube.com/watch?v=34I9hKjJbSM)**

Today, a new AI model from a company name "SubQuadratic" dropped a brand new model using a known, but not used, attention ...

📺 Tim Carambat

👁️ 18K • 👍 891 • 💬 156 • ⏱️ 15:22 • 7h ago

---

**[Consumer AI Has a Problem Nobody&#39;s Naming.](https://www.youtube.com/watch?v=Z0HizICooiw)**

Full Story w/ Prompt Kit: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 32K • 👍 1K • 💬 200 • ⏱️ 32:55 • 12h ago

---

**[BREAKING: Indian IT Faces A NEW CHALLENGE From AI LABS](https://www.youtube.com/watch?v=ohWE_rtmX0c)**

Anthropic's new $1.5 billion AI services venture is a major move, creating both challenges and opportunities for Indian IT firms.

📺 AIM Network

👁️ 5K • 👍 92 • 💬 20 • ⏱️ 3:44 • 15h ago

---

**[He Was Finally Arrested...](https://www.youtube.com/watch?v=0A6HmgARlkE)**

TikToker Tricked Cops Using AI Videos Then Got Arrested This South Florida news story covers a man arrested for using a ...

📺 Mori

👁️ 15K • 👍 1K • 💬 105 • ⏱️ 11:45 • 1d ago

---

**[Scott Galloway: AI Wasn’t Built For You. The Rich Don’t Need You Anymore!](https://www.youtube.com/watch?v=NdU6UdUKaYc)**

AI CEOs are selling us the dream of 'freedom', making billions off the fear of mass job loss! Scott Galloway reveals the truth is ...

📺 The Diary Of A CEO

👁️ 1.2M • 👍 30K • 💬 4K • ⏱️ 1:58:11 • 1d ago

---

**[Passive Income: I Tried AI Dropshipping For a Week (RAW RESULTS)](https://www.youtube.com/watch?v=rhuYy9LP72M)**

Get a FREE AI-built Shopify store: https://www.buildyourstore.ai/wv43 Try AutoDS here for just $1 - https://www.autods.com/il38 ...

📺 Mark Tilbury

👁️ 220K • 👍 13K • 💬 3K • ⏱️ 28:29 • 1d ago

---

**[We Asked AI To Show America Without Republicans](https://www.youtube.com/watch?v=jAcxE5w52vI)**

We asked AI to show America without any Republicans.

📺 The Babylon Bee

👁️ 204K • 👍 16K • 💬 1K • ⏱️ 1:25 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 631,499 • ❤️ 3,586 • 8d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 15,024 • ❤️ 271 • 1d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 141,317 • ❤️ 1,301 • 13d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 37,897 • ❤️ 246 • 2h ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 13,317 • ❤️ 440 • 7d ago

---

**[Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)**

*NVIDIA*

Nemotron-3 Nano Omni 30B is a multimodal LLM for enterprise Q&A, summarization, and document intelligence, capable of processing video, audio, image, and text inputs for use cases like customer service, media analysis, and GUI automation.

`any-to-any` `33.0B`

⬇️ 44,631 • ❤️ 244 • 13h ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 3,262 • ❤️ 162 • 9d ago

---

**[Laguna-XS.2](https://huggingface.co/poolside/Laguna-XS.2)**

*Poolside*

Laguna XS.2 is a 33B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring Sliding Window Attention and FP8 KV cache for efficient local execution on 36GB RAM. It supports native reasoning and is available under the Apache 2.0 license.

`text-generation` `33.4B`

⬇️ 12,027 • ❤️ 221 • 2d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,458,973 • ❤️ 1,130 • 12d ago

---

**[talkie-1930-13b-it](https://huggingface.co/talkie-lm/talkie-1930-13b-it)**

*talkie*

talkie-1930-13b-it is a 13B instruction-tuned language model trained on pre-1931 English text, excelling at generating responses in a vintage style for applications like historical chatbots or creative writing.

⬇️ 0 • ❤️ 235 • 12d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 57 • 💬 3 • ⭐ 69,417 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 169 • 💬 10 • ⭐ 46,588 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 30 • 💬 3 • ⭐ 22,970 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 16 • 💬 3 • ⭐ 9,205 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 62,061 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,784 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://huggingface.co/papers/2512.11253)**

*Zhiyuan Li, Chi-Man Pun, Chen Fang et al. (5 authors)*

🏢 GVC Lab at Great Bay University

PersonaLive is a diffusion-based portrait animation framework that improves real-time performance through hybrid implicit signals, appearance distillation, and autoregressive streaming generation.

▲ 40 • 💬 3 • ⭐ 2,921 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.11253) • [💻 code](https://github.com/GVCLab/PersonaLive)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,083 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 53 • 💬 2 • ⭐ 54,834 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[Representation Fréchet Loss for Visual Generation](https://huggingface.co/papers/2604.28190)**

*Jiawei Yang, Zhengyang Geng, Xuan Ju et al. (5 authors)*

Fréchet Distance can be effectively optimized as a training objective when decoupling population size from batch size, leading to improved generator quality and alternative evaluation metrics.

▲ 26 • 💬 1 • ⭐ 355 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.28190) • [💻 code](https://github.com/Jiawei-Yang/FD-Loss)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.9k • 🔱 2.7k • 8d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 10.4k • 🔱 683 • 1d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

`Python` `agent-workflows` `ai` `claude-code` `developer-tools` `diagrams`

⭐ 5.5k • 🔱 498 • 1d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 5.5k • 🔱 416 • 8h ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 5.0k • 🔱 362 • 1d ago

---

**[AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)**

Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch

`Python` `ai` `claude-code` `claude-code-skill` `knowledge-management` `obsidian`

⭐ 4.3k • 🔱 478 • 11d ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics & channel configuration (Telegram, Discord, Slack, WhatsApp)

`TypeScript` `agent` `ai-agent` `chat-ui` `chatbot` `claude`

⭐ 3.6k • 🔱 450 • 3h ago

---

**[alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)**

Hermes Agent 从入门到精通 · 橙皮书系列 · Nous Research 开源 AI Agent 框架实战指南

⭐ 3.5k • 🔱 369 • 14d ago

---

**[OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano)**

MOSS-TTS-Nano is an open-source multilingual tiny speech generation model from MOSI.AI and the OpenMOSS team. With only 0.1B parameters, it is designed for realtime speech generation, can run directly on CPU without a GPU, and keeps the deployment stack simple enough for local demos, web serving, and lightweight product integration.

`Python` `audio-tokenizer` `chinese` `english` `multi-modality` `multilingual`

⭐ 2.7k • 🔱 349 • 6d ago

---

**[cloudflare/agentic-inbox](https://github.com/cloudflare/agentic-inbox)**

A self-hosted email client with an AI agent, running entirely on Cloudflare Workers

`TypeScript`

⭐ 2.6k • 🔱 336 • 12d ago

---

---

*Generated by PeekDeck - A glance is all you need*
