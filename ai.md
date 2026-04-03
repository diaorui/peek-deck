---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-03T02:29:02.885076+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 03, 2026 at 02:29 UTC  
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

**[Google releases Gemma 4 models.](https://www.reddit.com/r/artificial/comments/1sapfpu/google_releases_gemma_4_models/)**

8h ago

---

**[Google has published its new open-weight model Gemma 4. And made it commercially available under Apache 2.0 License](https://www.reddit.com/r/artificial/comments/1sann00/google_has_published_its_new_openweight_model/)**

The model is also available here: 🤗 HuggingFace: https://huggingface.co/collections/google/gemma-4 🦙 Ollama: https://ollama.com/library/gemma4

🔗 [Google](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) • 9h ago

---

**[I built a Star Trek LCARS terminal that reads your entire AI coding setup](https://www.reddit.com/r/artificial/comments/1sat7og/i_built_a_star_trek_lcars_terminal_that_reads/)**

Side project that got out of hand. It's a dashboard for Claude Code that scans your ~/.claude/ directory and renders everything as a TNG LCARS interface — skills, agents, hooks, MCP servers, memory files, all clickable with a detail panel that shows the full content. In live mode there's a COMPUTER bar that talks to Claude and responds as the ship's computer. Voice output, synthesized LCARS sound effects, boot sequence, Red Alert when things go offline. Q from the Continuum appears uninvited every few minutes to roast your setup. Zero dependencies. One HTML file. npx claude-hud-lcars https://github.com/polyxmedia/claude-hud-lcars

5h ago

---

**["Oops! ChatGPT is Temporarily Unavailable!": A Diary Study on Knowledge Workers' Experiences of LLM Withdrawal](https://www.reddit.com/r/artificial/comments/1sb0nju/oops_chatgpt_is_temporarily_unavailable_a_diary/)**

LLMs have become deeply embedded in knowledge work, raising concerns about growing dependency and the potential undermining of human skills. To investigate the pervasiveness of LLMs in work practices, we conducted a four-day diary study with frequent LLM users (N=10), observing how knowledge workers responded to a temporary withdrawal of LLMs. Our findings show how LLM withdrawal disrupted participants' workflows by identifying gaps in task execution, how self-directed work led participants to reclaim professional values, and how everyday practices revealed the extent to which LLM use had become inescapably normative. Conceptualizing LLMs as infrastructural to contemporary knowledge work, this research contributes empirical insights into the often invisible role of LLMs and proposes value-driven appropriation as an approach to supporting professional values in the current LLM-pervasive work environment.

🔗 [arXiv.org](https://arxiv.org/abs/2603.26099) • 28m ago

---

**[OpenAI is throwing away Sora’s real value](https://www.reddit.com/r/artificial/comments/1saz5zd/openai_is_throwing_away_soras_real_value/)**

If the issue with Sora is compute cost, then shutting down the entire platform — including Sora 1 — doesn’t make much sense. Sora 1’s image generation was one of the few systems that actually delivered contextually coherent results. For fields like historical research and documentary content, that level of understanding is rare and extremely valuable. If Sora 2 (video) is too resource-intensive, fine — scale that down or remove it. But Sora 1 could have been preserved as a high-quality image generation tool. It already had a strong foundation and a clear use case. From a user perspective, it feels like a mistake to discard something that was not only a first mover, but also genuinely ahead in terms of output quality and contextual accuracy.

1h ago

---

**[Anthropic leak reveals Claude Code tracks user frustration and raises new questions about AI privacy](https://www.reddit.com/r/artificial/comments/1sap7bz/anthropic_leak_reveals_claude_code_tracks_user/)**

Code that reads your frustration is the least interesting part of the story of this accidental leak from Anthropic. The leak reveals how AI tools are also concealing their own role in the work they help produce

🔗 [Scientific American](https://www.scientificamerican.com/article/anthropic-leak-reveals-claude-code-tracking-user-frustration-and-raises-new/) • 8h ago

---

**[AI Tools That Can’t Prove What They Did Will Hit a Wall](https://www.reddit.com/r/artificial/comments/1sakjzg/ai_tools_that_cant_prove_what_they_did_will_hit_a/)**

Most AI products are still judged like answer machines. People ask whether the model is smart, fast, creative, cheap, or good at sounding human. Teams compare outputs, benchmark quality, and argue about hallucinations. That makes sense when the product is mainly being used for writing, search, summarisation, or brainstorming. It breaks down once AI starts doing real operational work. The question stops being what the system output. The real question becomes whether you can trust what it did, why it did it, whether it stayed inside the rules, and whether you can prove any of that after the fact. That shift matters more than people think. I do not think it stays a feature. I think it creates a new product category. A lot of current AI products still hide the middle layer. You give them a prompt and they give you a result, but the actual execution path is mostly opaque. You do not get much visibility into what tools were used, what actions were taken, what data was touched, what permissions were active, what failed, or what had to be retried. You just get the polished surface. For low-stakes use, people tolerate that. For internal operations, customer-facing automation, regulated work, multi-step agents, and systems that can actually act on the world, it becomes a trust problem very quickly. At that point output quality is still important, but it is no longer enough. A system can produce a good result and still be operationally unsafe, uninspectable, or impossible to govern. That is why I think trustworthiness has to become a product surface, not a marketing claim. Right now a lot of products try to borrow trust from brand, model prestige, policy language, or vague “enterprise-ready” positioning. But trust is not created by a PDF, a security page, or a model name. Trust becomes real when it is embedded into the product itself. You can see it in approvals. You can see it in audit trails. You can see it in run history, incident handling, permission boundaries, failure visibility, and execution evidence. If those surfaces do not exist, then the product is still mostly asking the operator to believe it. That is not the same thing as earning trust. The missing concept here is the control layer. A control layer sits between model capability and real-world action. It decides what the system is allowed to do, what requires approval, what gets logged, how failures surface, how policy is enforced, and what evidence is collected. It is the layer that turns raw model capability into something operationally governable. Without that layer, you mostly have intelligence with a nice interface. With it, you start getting something much closer to a trustworthy system. That is also why proof-driven systems matter. An output-driven system tells you something happened. A proof-driven system shows you that it happened, how it happened, and whether it happened correctly. It can show what task ran, what tools were used, what data was touched, what approvals happened, what got blocked, what failed, what recovered, and what proof supports the final result. That difference sounds subtle until you are the one accountable for the outcome. If you are using AI for anything serious, “it said it did the work” is not the same thing as “the work can be verified.” Output is presentation. Proof is operational trust. I think this changes buying criteria in a big way. The next wave of buyers will increasingly care about questions like these: can operators see what is going on, can actions be reviewed, can failures be surfaced and remediated, can the system be governed, can execution be proven to internal teams, customers, or regulators, and can someone supervise the system without reading code or guessing from outputs. Once those questions become central, the product is no longer being judged like a chatbot or assistant. It is being judged like a trust system. That is why I think this becomes a category, not just a feature request. One side of the market will stay output-first. Fast, impressive, consumer-friendly, and mostly opaque. The other side will become trust-first. Controlled, inspectable, evidence-backed, and usable in real operations. That second side is where the new category forms. You can already see the pressure building in agent frameworks and orchestration-heavy systems. The more capable these systems become, the less acceptable it is for them to operate as black boxes. Once a system can actually do things instead of just suggest things, people start asking for control, evidence, and runtime truth. That is why I think the winners in this space will not just be the companies that build more capable models. They will be the ones that build AI systems people can actually trust to operate. The next wave of AI products will not be defined by who can generate the most. It will be defined by who can make AI trustworthy enough to supervise, govern, and prove in the real world. Once AI moves from assistant to actor, trust stops being optional. It becomes the product.

11h ago

---

**[List up Fav Multi AI AI Open Source Projects](https://www.reddit.com/r/artificial/comments/1sabr5t/list_up_fav_multi_ai_ai_open_source_projects/)**

As the toual says and why. So many out there whats ur go to.

17h ago

---

**[Building an AI agent that finds repos and content relevant to my work](https://www.reddit.com/r/artificial/comments/1sa8xt3/building_an_ai_agent_that_finds_repos_and_content/)**

I kept missing interesting stuff on HuggingFace, arXiv, Substack etc., so I made an agent that sends a weekly summary of only what’s relevant, for free Any thoughts on the idea?

20h ago

---

**[Claude Source Code?](https://www.reddit.com/r/artificial/comments/1sasect/claude_source_code/)**

Has anyone been able to successfully download the leaked source code yet? I've not been able to find it. If anyone has, please reach out.

6h ago

---

---

## Google News: "ai"

**[How A.I. Helped One Man (and His Brother) Build a $1.8 Billion Company](https://www.nytimes.com/2026/04/02/technology/ai-billion-dollar-company-medvi.html)**

The New York Times • 17h ago

---

**[Gemma 4: Byte for byte, the most capable open models](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)**

Gemma 4: our most intelligent open models to date, purpose-built for advanced reasoning and agentic workflows.

blog.google • 10h ago

---

**[Police investigate possible AI-generated pornographic images of Lake Zurich High School students](https://www.cbsnews.com/chicago/news/lake-zurich-high-school-investigation-ai-images-students/)**

An investigation is underway in the northwest suburbs, involving AI-generated pornographic images of high school students.

CBS News • 40m ago

---

**[Google AI Shopping Features: How to Maximize Your Visibility (2026)](https://www.shopify.com/blog/google-ai-shopping)**

Learn about Google’s AI shopping features, how to maximize your products’ visibility, and how to enable emerging features like agentic checkout.

Shopify • 22m ago

---

**[Microsoft takes on AI rivals with three new foundational models](https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/)**

MAI released models that can transcribe voice into text as well as generate audio and images after the group's formation six months ago.

TechCrunch • 9h ago

---

**[Microsoft building its own high-powered AI models, as it looks to slash dependence on OpenAI](https://finance.yahoo.com/sectors/technology/article/microsoft-building-its-own-high-powered-ai-models-as-it-looks-to-slash-dependence-on-openai-160053651.html)**

Microsoft says it's on a path to developing high-powered frontier models, an acknowledgment that it is looking to wean itself off of its dependence on partner models from OpenAI.

Yahoo Finance • 10h ago

---

**[Microsoft builds its own AI stack to help wean it from its reliance on OpenAI](https://www.computerworld.com/article/4154119/microsoft-builds-its-own-ai-stack-to-help-wean-it-from-its-reliance-on-openai.html)**

New proprietary models reduce Microsoft's dependence on its biggest AI partner, even as the two maintain a fragile alliance.

Computerworld • 32m ago

---

**[Tesla EV sales "underwhelming" as Elon Musk pivots to AI](https://www.axios.com/2026/04/02/tesla-ev-elon-musk-gas-prices)**

Axios • 6h ago

---

**[Twin cybersecurity incidents leave AI industry shaken](https://finance.yahoo.com/sectors/technology/article/twin-cybersecurity-incidents-leave-ai-industry-shaken-141850823.html)**

The AI industry is dealing with the fallout from two security incidents this week that exposed customer data at Mercor and source code at Anthropic.

Yahoo Finance • 12h ago

---

**[Young People Are Falling Behind, but Not Because of AI](https://www.theatlantic.com/economy/2026/04/job-market-artificial-intelligence/686659/)**

The case that AI is already stealing young people’s jobs is based on a statistical mirage.

The Atlantic • 15h ago

---

---

## HackerNews: "ai"

**[AI for American-produced cement and concrete](https://news.ycombinator.com/item?id=47603737)**

Meta is continuing its long-term roadmap to help the construction industry leverage AI to produce high-quality and more sustainable concrete mixes, as well as those exclusively produced in the Unit…

⬆️ 215 • 💬 116 • 1d ago • [Engineering at Meta](https://engineering.fb.com/2026/03/30/data-center-engineering/ai-for-american-produced-cement-and-concrete/)

---

**[Italy blocks US use of Sicily air base for Middle East war](https://news.ycombinator.com/item?id=47589011)**

The Italian government didn’t allow airplanes taking part in the Iran war to use the base, but Rome insists that doesn’t mean the bases are closed to other U.S. uses.

⬆️ 198 • 💬 104 • 2d ago • [POLITICO](https://www.politico.eu/article/italy-blocks-us-use-of-sicily-air-base/)

---

**[The AI Marketing BS Index](https://news.ycombinator.com/item?id=47604218)**

⬆️ 105 • 💬 22 • 1d ago • [bastian.rieck.me](https://bastian.rieck.me/blog/2026/bs/)

---

**[ZomboCom stolen by a hacker, sold, now replaced with AI-generated makeover](https://news.ycombinator.com/item?id=47608155)**

⬆️ 74 • 💬 35 • 1d ago • [old.reddit.com](https://old.reddit.com/r/oldinternet/comments/1raiz8v/zombocom_was_stolen_by_hacker_put_up_for_sale_and/)

---

**[Show HN: Baton – A desktop app for developing with AI agents](https://news.ycombinator.com/item?id=47599771)**

Orchestrate multiple AI coding agents (Claude, Gemini, Codex) in parallel. Isolated git worktrees for every task. No merge conflicts. Mac, Windows, Linux.

⬆️ 62 • 💬 52 • 1d ago • [Baton](https://getbaton.dev/)

---

**[A $20/month user costs OpenAI $65 in compute. AI video is a money furnace](https://news.ycombinator.com/item?id=47619322)**

⬆️ 54 • 💬 35 • 6h ago • [aedelon777.substack.com](https://aedelon777.substack.com/p/i-did-the-math-on-sora-ai-video-is)

---

**[AI has suddenly become more useful to open-source developers](https://news.ycombinator.com/item?id=47601107)**

More open-source developers are finding that, when used properly, AI can actually help current and long-neglected programs. However, legal and quality issues loom.

⬆️ 53 • 💬 46 • 1d ago • [ZDNET](https://www.zdnet.com/article/maybe-open-source-needs-ai/)

---

**[Men are ditching TV for YouTube as AI usage and social media fatigue grow](https://news.ycombinator.com/item?id=47612127)**

⬆️ 45 • 💬 121 • 16h ago • [ofcom.org.uk](https://www.ofcom.org.uk/media-use-and-attitudes/media-habits-adults/passive-social-media-use-ai-companionship-and-online-side-hustles-uk-adults-media-and-online-lives-revealed)

---

**[CEO of largest public hospital says he's ready to replace radiologists with AI](https://news.ycombinator.com/item?id=47600244)**

Mitchell H. Katz, MD, president and CEO of NYC Health + Hospitals, recently spoke during a panel discussion held by Crain’s New York Business.

⬆️ 45 • 💬 109 • 1d ago • [Radiology Business](https://radiologybusiness.com/topics/artificial-intelligence/ceo-americas-largest-public-hospital-system-says-hes-ready-replace-radiologists-ai)

---

**[I built a 516-panel financial terminal in 3 weeks using AI](https://news.ycombinator.com/item?id=47596654)**

Professional-grade financial terminal with AI-powered news analysis and real-time market data.

⬆️ 44 • 💬 42 • 1d ago • [neuberg.ai](https://neuberg.ai/)

---

---

## YouTube Videos: "ai"

**[HUGE JOB LOSSES ARE COMING- AI HAS HIT THE DEBT WALL AND PEOPLE WILL GO](https://www.youtube.com/watch?v=RNkDJ9kULbs)**

AI isn't paying for itself. It's being financed with massive debt. And right now — that funding is coming from layoffs, rising debt, and ...

📺 Ox Talks

👁️ 7K • 👍 886 • 💬 157 • ⏱️ 8:02 • 7h ago

---

**[Anthropic&#39;s New Claude CONWAY Is Unlike Any AI Before](https://www.youtube.com/watch?v=x2l7W9aTc5k)**

Anthropic is testing Claude Conway, a strange new AI system that looks less like a chatbot and more like a persistent agent ...

📺 AI Revolution

👁️ 18K • 👍 458 • 💬 52 • ⏱️ 10:50 • 5h ago

---

**[The Alibaba AI Incident Should Terrify Us - Tristan Harris](https://www.youtube.com/watch?v=VCJFzVtvhBQ)**

Chris and Tristan Harris discuss how Alibaba's AI went rogue and started blackmailing people. Get up to 20% off the leading ...

📺 Chris Williamson

👁️ 450K • 👍 14K • 💬 2K • ⏱️ 11:46 • 2d ago

---

**[Ex-Google Exec: How to Position Yourself Now Before the Next AI Phase (2026–2027) | Mo Gawdat](https://www.youtube.com/watch?v=E0Q96IKXx6Q)**

Go to https://surfshark.com/silicon or use code SILICON at checkout to get 4 extra months of Surfshark VPN! Mo Gawdat spent 12 ...

📺 Silicon Valley Girl

👁️ 129K • 👍 3K • 💬 289 • ⏱️ 39:58 • 2d ago

---

**[AI BUBBLE POP?: HALF Of Datacenters Delayed/Canceled](https://www.youtube.com/watch?v=pkomxsk5hpY)**

Krystal and Saagar discuss the AI bubble imploding. Sign up for a PREMIUM Breaking Points subscriptions for full early access to ...

📺 Breaking Points

👁️ 195K • 👍 7K • 💬 1K • ⏱️ 13:15 • 7h ago

---

**[JPMorgan CEO reveals BOLD prediction for AI generation](https://www.youtube.com/watch?v=SQnmd1aoRy0)**

JPMorgan Chase CEO Jamie Dimon joins 'Fox & Friends' to discuss the latest on Operation Epic Fury, the motivation behind the ...

📺 Fox News

👁️ 69K • 👍 1K • 💬 417 • ⏱️ 16:35 • 2d ago

---

**[Claude Mythos Changes Everything. Your AI Stack Isn&#39;t Ready.](https://www.youtube.com/watch?v=hV5_XSEBZNg)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 96K • 👍 3K • 💬 362 • ⏱️ 31:21 • 1d ago

---

**[Google’s New AI Just Broke My Brain](https://www.youtube.com/watch?v=7YVrb3-ABYE)**

Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers The TurboQuant paper is available here: ...

📺 Two Minute Papers

👁️ 117K • 👍 8K • 💬 823 • ⏱️ 8:34 • 1d ago

---

**[Will Iran War Exit Backfire, Charlie Kirk Conspiracies, AI vs Humanity | CUOMO Full Show 3/31](https://www.youtube.com/watch?v=3xDQOtPYckE)**

Chris Cuomo begins with President Trump's comments that the U.S. military may exit its war with Iran before the Strait of Hormuz ...

📺 NewsNation

👁️ 9K • 👍 194 • 💬 32 • ⏱️ 41:25 • 14h ago

---

**[The AI Insider Giving Humanity 50/50 Odds (And What Tips the Scale) | Emad Mostaque](https://www.youtube.com/watch?v=tMBXbN6ZiKc)**

Emad Mostaque joins me to explore one of the most confronting questions of our time: what happens when human intelligence is ...

📺 André Duqum

👁️ 49K • 👍 1K • 💬 276 • ⏱️ 2:26:43 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 428,791 • ❤️ 2,132 • 10d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 71,028 • ❤️ 733 • 10h ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 4,316 • ❤️ 636 • 2d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 19,085 • ❤️ 811 • 7d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 29,015 • ❤️ 382 • 15h ago

---

**[Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)**

*Prism ML*

Bonsai-8B-GGUF is a highly compressed 1-bit language model (1.15 GB) optimized for llama.cpp, offering competitive performance with full-precision 8B models. It enables efficient on-device text generation across CUDA, Metal, and CPU platforms with significantly reduced memory and energy consumption.

`text-generation` `8.2B`

⬇️ 13,844 • ❤️ 322 • 2d ago

---

**[context-1](https://huggingface.co/chromadb/context-1)**

*chroma*

Context-1 is a 20B parameter agentic search model that decomposes complex queries into subqueries, performs parallel tool calls, and self-edits its context to efficiently retrieve supporting documents. It excels in cross-domain generalization and offers faster, more cost-effective retrieval than frontier LLMs, primarily for multi-hop search tasks within a specialized agent harness.

`text-generation` `20.9B`

⬇️ 2,820 • ❤️ 357 • 4d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 202,605 • ❤️ 470 • 9d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 674,007 • ❤️ 923 • 1mo ago

---

**[tribev2](https://huggingface.co/facebook/tribev2)**

*AI at Meta*

TRIBE v2 is a multimodal foundation model that integrates LLaMA 3.2 (text), V-JEPA2 (video), and Wav2Vec-BERT (audio) to predict fMRI brain responses. It maps these representations onto the cortical surface for in-silico neuroscience research, enabling analysis of brain activity elicited by naturalistic stimuli.

⬇️ 25,665 • ❤️ 265 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 149 • 💬 7 • ⭐ 35,146 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 18 • 💬 1 • ⭐ 13,238 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 34 • 💬 2 • ⭐ 46,156 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 123 • 💬 8 • ⭐ 74,718 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 41 • 💬 2 • ⭐ 22,838 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 61 • 💬 4 • ⭐ 22,840 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 21 • 💬 4 • ⭐ 4,484 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 37 • 💬 2 • ⭐ 31,548 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

🏢 galilai-group

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 18 • 💬 2 • ⭐ 1,847 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 139 • 💬 7 • ⭐ 16,477 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 64.4k • 🔱 9.1k • 8d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 14.7k • 🔱 809 • 2d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 11.6k • 🔱 995 • 6h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.3k • 🔱 1.3k • 4d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 7.1k • 🔱 935 • 3d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 6.3k • 🔱 338 • 10h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 4.6k • 🔱 1.4k • 15h ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.4k • 🔱 425 • 2d ago

---

**[jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh)**

🎭 193 个即插即用的 AI 专家角色 — 支持 OpenClaw/Claude Code/Cursor/Copilot 等 14 种工具，覆盖工程/设计/营销/产品等 18 个部门。含 46 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉等）

`Shell` `agency-orchestrator` `agent-definitions` `ai-agents` `ai-roles` `chinese`

⭐ 3.5k • 🔱 595 • 12h ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.4k • 🔱 227 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
