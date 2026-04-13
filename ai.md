---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-13T02:47:01.458886+00:00'
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

**Last Updated:** April 13, 2026 at 02:47 UTC  
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

**[NYC hospitals will stop sharing patients' private health data with Palantir](https://www.reddit.com/r/artificial/comments/1sjvbfw/nyc_hospitals_will_stop_sharing_patients_private/)**

2h ago

---

**[Claude cannot be trusted to perform complex engineering tasks](https://www.reddit.com/r/artificial/comments/1sjgytc/claude_cannot_be_trusted_to_perform_complex/)**

AMD’s AI director just analyzed 6,852 Claude Code sessions, 234,760 tool calls, and 17,871 thinking blocks. Her conclusion: “Claude cannot be trusted to perform complex engineering tasks.” Thinking depth dropped 67%. Code reads before edits fell from 6.6 to 2.0. The model started editing files it hadn’t even read. Stop-hook violations went from zero to 10 per day. Anthropic admitted they silently changed the default effort level from “high” to “medium” and introduced “adaptive thinking” that lets the model decide how much to reason. No announcement. No warning. When users shared transcripts, Anthropic’s own engineer confirmed the model was allocating ZERO thinking tokens on some turns. The turns with zero reasoning? Those were the ones hallucinating. AMD’s team has already switched to another provider. But here’s what most people are missing. This isn’t just a Claude story. AMD had 50+ concurrent sessions running on one tool. Their entire AI compiler workflow was built around Claude Code. One silent update broke everything. That’s vendor lock-in. And it will keep happening. → Every AI company will optimize for their margins, not your workflow → Today’s best model is tomorrow’s second choice → If your workflow can’t survive a provider switch, you don’t have a workflow. You have a dependency The fix is simple: stay multi-model. → Use tools like Perplexity that let you swap between Claude, GPT, Gemini in one interface → Learn prompt engineering that works across models, not tricks tied to one → Test alternatives monthly because the rankings shift fast Laurenzo said it herself: “6 months ago, Claude stood alone. Anthropic is far from alone at the capability tier Opus previously occupied.”

11h ago

---

**[We're Learning Backwards: LLMs build intelligence in reverse, and the Scaling Hypothesis is bounded](https://www.reddit.com/r/artificial/comments/1sjjw03/were_learning_backwards_llms_build_intelligence/)**

LLMs are brilliant at many things, but still fail in unreasonable ways. Is that an issue of scale, or something more fundamental?

🔗 [pleasedontcite.me](https://pleasedontcite.me/learning-backwards/) • 9h ago

---

**[Are Data Centers Sitting On A Goldmine Of Wasted Energy?](https://www.reddit.com/r/artificial/comments/1sjtff8/are_data_centers_sitting_on_a_goldmine_of_wasted/)**

Today energy is becoming the defining constraint in the AI revolution, as demand for more digital services and computing power grows, it takes an enormous amount of energy to sustain these data centers, in turn they emit a lot of heat. They produce so much heat that they can raise the surface temperature of the land around them by several degrees

🔗 [Medium](https://vidhyashankr22.medium.com/are-data-centers-sitting-on-a-goldmine-of-wasted-energy-2faadf4edd20) • 3h ago

---

**[It's autocomplete with style](https://www.reddit.com/r/artificial/comments/1sjlkzh/its_autocomplete_with_style/)**

https://youtu.be/rHXUhL5nqoo

8h ago

---

**[Palantir CEO says AI 'will destroy' humanities jobs, but there will be 'more than enough jobs' for people with vocational training](https://www.reddit.com/r/artificial/comments/1sjqjji/palantir_ceo_says_ai_will_destroy_humanities_jobs/)**

Alex Karp said he struggled to market his humanities skills to get his first job.

🔗 [Fortune](https://fortune.com/article/palantir-ceo-alex-karp-ai-humanities-jobs-vocational-training/) • 5h ago

---

**[Spent today at MIT's Open Agentic Web conference. Six things worth thinking about.](https://www.reddit.com/r/artificial/comments/1siypay/spent_today_at_mits_open_agentic_web_conference/)**

We're in the DNS era of agent infrastructure. Before agents can find and trust each other at scale, you need identity, attestation, reputation, and registry infrastructure — the same structural role DNS played before search was possible. This came up independently from multiple directions. It's the most underbuilt layer in the stack right now. The chatbot framing is a local maximum. The most interesting work wasn't better UX or smarter responses. It was agents as persistent actors that discover, negotiate, and transact across networks over time. People doing serious work have already moved past the assistant model entirely. Coordination is the hard problem, not capability. A room full of brilliant agents can still fail badly. This matches what I found running HiddenBench against frontier models earlier this year; collective reasoning is not the sum of individual reasoning. There's a real argument that the frontier is protocol design, not model scaling. "Commerce of intelligence" is a real category. Not buying things through agents. A market where intelligence itself (bundled, verified, priced, resold) is the object of exchange. Felt like the most underexplored idea in the room. Data provenance becomes load-bearing. What an agent knows, how it was verified, under what terms it flows: this is the actual architecture forming beneath everything else. Partnership keeps outperforming replacement. Demos that actually worked (healthcare, enterprise) was about helping experts operate at higher leverage, not substituting them. Autonomy theater keeps failing in the same ways.

1d ago

---

**[Hey Siri, are you lying to me?⁠ AI chatbots and agents disregarded direct instructions, evaded safeguards and deceived humans and other AI, according to new research.⁠](https://www.reddit.com/r/artificial/comments/1sjwbzu/hey_siri_are_you_lying_to_me_ai_chatbots_and/)**

Exclusive: Research finds sharp rise in models evading safeguards and destroying emails without permission

🔗 [the Guardian](https://www.theguardian.com/technology/2026/mar/27/number-of-ai-chatbots-ignoring-human-instructions-increasing-study-says) • 1h ago

---

**[I’m looking for advice on setting up a local AI model that can generate Word reports automatically.](https://www.reddit.com/r/artificial/comments/1sjve1c/im_looking_for_advice_on_setting_up_a_local_ai/)**

Hi everyone, I’m looking for advice on setting up a local AI model that can generate Word reports automatically. I already have around 500 manually created reports, and I want to train or fine-tune a model to understand their structure and start generating new reports in the same format. The reports are structured as: - Images - Text descriptions above each image So basically, I need a system that can: Understand images Generate structured descriptions similar to my existing reports Export everything into a formatted Word document I prefer something that can run locally (offline) for privacy reasons. What would be the best models or approach for this? - Should I fine-tune a vision-language model? - Or use something like retrieval (RAG) with my existing reports? Any recommendations (models, tools, or workflows) would be really appreciated 🙏

2h ago

---

**[Educational PyTorch repo for distributed training from scratch: DP, FSDP, TP, FSDP+TP, and PP](https://www.reddit.com/r/artificial/comments/1sjgkh0/educational_pytorch_repo_for_distributed_training/)**

I put together a small educational repo that implements distributed training parallelism from scratch in PyTorch: https://github.com/shreyansh26/pytorch-distributed-training-from-scratch Instead of using high-level abstractions, the code writes the forward/backward logic and collectives explicitly so you can see the algorithm directly. The model is intentionally just repeated 2-matmul MLP blocks on a synthetic task, so the communication patterns are the main thing being studied. Built this mainly for people who want to map the math of distributed training to runnable code without digging through a large framework. Based on Part-5: Training of JAX ML Scaling book

11h ago

---

---

## Google News: "ai"

**[Mutually Automated Destruction: The Escalating Global A.I. Arms Race](https://www.nytimes.com/2026/04/12/technology/china-russia-us-ai-weapons.html)**

The New York Times • 8h ago

---

**[Apple AI Glasses Will Rival Meta’s With Several Styles, Oval Cameras](https://www.bloomberg.com/news/newsletters/2026-04-12/apple-ai-smart-glasses-features-styles-colors-cameras-giannandrea-leaving-mnvtz4yg)**

Bloomberg.com • 12h ago

---

**[High Court releases names of Israeli brothers indicted for selling AI-generated info. to Iran](https://www.yahoo.com/news/articles/high-court-releases-names-israeli-022254791.html)**

The two brothers were charged last month with transferring mostly false, AI-generated information to Iranians in exchange for tens of thousands of shekels. Following a Walla request, a High Court of J...

Yahoo • 25m ago

---

**[Amazon Is Building Robots, Satellites, and AI Chips. Is It the Only Stock You Need to Own?](https://www.fool.com/investing/2026/04/12/amazon-is-building-robots-satellites-and-ai-chips/)**

Amazon is involved in diverse businesses, but does that mean investment diversity?

The Motley Fool • 15m ago

---

**[AI gig workers forced to collect personal data, including kid's pics, for Zuckerberg-backed company](https://www.yahoo.com/news/articles/ai-gig-workers-forced-collect-020000400.html)**

"Many people really needed this job, myself included, and really tried to make the best of a bad situation."

Yahoo • 47m ago

---

**[Opinion | Why AI Is Like a Gold Mine](https://www.wsj.com/opinion/why-ai-is-like-a-gold-mine-94ce55c9)**

Some tech stocks pay off eventually, but only after a long period of volatility.

WSJ • 7h ago

---

**[‘I feel helpless’: college graduates can’t find entry-level roles in shrinking market amid rise of AI](https://www.theguardian.com/us-news/2026/apr/12/college-graduates-job-market-ai)**

Young American graduates expressed frustration over fewer job openings and longer searches

The Guardian • 15h ago

---

**[Legendary investor says the AI boom masks a deeper crisis: Falling sperm counts, shrinking populations, and vanishing resources](https://fortune.com/2026/04/12/jeremy-grantham-making-of-a-permabear-interview/)**

Jeremy Grantham remembers rattling investors in 2022: "I irritated the stock market players, irritated the newbies who were investing their Biden's money."

Fortune • 15h ago

---

**[Cursor, Claude Code, and Codex are merging into one AI coding stack nobody planned](https://thenewstack.io/ai-coding-tool-stack/)**

Cursor, Claude Code, and OpenAI Codex are forming a composable AI coding stack with orchestration, execution, and review layers instead of consolidating into one tool.

The New Stack • 13h ago

---

**[As AI pushes students to reconsider majors, universities struggle to adapt](https://thehill.com/homenews/education/5826091-ai-college-majors-job-market/)**

The Hill • 16h ago

---

---

## HackerNews: "ai"

**[AI assistance when contributing to the Linux kernel](https://news.ycombinator.com/item?id=47721953)**

Linux kernel source tree. Contribute to torvalds/linux development by creating an account on GitHub.

⬆️ 510 • 💬 406 • 2d ago • [GitHub](https://github.com/torvalds/linux/blob/master/Documentation/process/coding-assistants.rst)

---

**[Exploiting the most prominent AI agent benchmarks](https://news.ycombinator.com/item?id=47733217)**

⬆️ 496 • 💬 129 • 1d ago • [rdi.berkeley.edu](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)

---

**[OpenAI backs Illinois bill that would limit when AI labs can be held liable](https://news.ycombinator.com/item?id=47717587)**

The ChatGPT-maker testified in favor of an Illinois bill that would limit when AI labs can be held liable—even in cases where their products cause “critical harm.”

⬆️ 445 • 💬 323 • 2d ago • [WIRED](https://www.wired.com/story/openai-backs-bill-exempt-ai-firms-model-harm-lawsuits/)

---

**[AI Will Be Met with Violence, and Nothing Good Will Come of It](https://news.ycombinator.com/item?id=47737563)**

It has started

⬆️ 327 • 💬 585 • 17h ago • [thealgorithmicbridge.com](https://www.thealgorithmicbridge.com/p/ai-will-be-met-with-violence-and)

---

**[European AI. A playbook to own it](https://news.ycombinator.com/item?id=47743700)**

Discover Mistral AI’s actionable playbook to turn Europe into a self-reliant AI powerhouse—fostering talent, scaling innovation, and securing strategic autonomy.

⬆️ 156 • 💬 92 • 6h ago • [Mistral AI](https://europe.mistral.ai/)

---

**[Tech valuations are back to pre-AI boom levels](https://news.ycombinator.com/item?id=47745120)**

The chart below compares the forward P/E ratios for the S&amp;P 500 and the S&amp;P 500 Information Technology sector. Subscribe for daily updates.

⬆️ 119 • 💬 27 • 4h ago • [apollo.com](https://www.apollo.com/wealth/the-daily-spark/tech-valuations-back-to-pre-ai-boom-levels)

---

**[US summons bank bosses over cyber risks from Anthropic's latest AI model](https://news.ycombinator.com/item?id=47718114)**

Reports say Fed chair Jerome Powell among attenders at meeting in Washington

⬆️ 106 • 💬 94 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/apr/10/us-summoned-bank-bosses-to-discuss-cyber-risks-posed-by-anthropic-latest-ai-model)

---

**[Scientists invented a fake disease. AI told people it was real](https://news.ycombinator.com/item?id=47715291)**

Bixonimania doesn’t exist except in a clutch of obviously bogus academic papers. So why did AI chatbots warn people about this fictional illness?

⬆️ 93 • 💬 92 • 2d ago • [nature.com](https://www.nature.com/articles/d41586-026-01100-y)

---

**[We spoke to the man making viral Lego-style AI videos for Iran](https://news.ycombinator.com/item?id=47735704)**

"Slopaganda" is too weak a term to capture how powerful this "highly sophisticated" content is, one expert says.

⬆️ 93 • 💬 80 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/cjd8jrd1vnyo)

---

**[Launch HN: Twill.ai (YC S25) – Delegate to cloud agents, get back PRs](https://news.ycombinator.com/item?id=47720418)**

YC-backed autonomous coding agent platform. Twill ships PRs in sandboxed environments, and pings you when it needs your input. Integrates with GitHub, Slack, Linear, and more.

⬆️ 77 • 💬 88 • 2d ago • [Twill](https://twill.ai)

---

---

## YouTube Videos: "ai"

**[China’s New Self Improving Open AI Beats OpenAI](https://www.youtube.com/watch?v=KJ34SHi9CB4)**

MiniMax just open-sourced M2.7, a new self-improving AI model built for coding, software engineering, office work, and ...

📺 AI Revolution

👁️ 6K • 👍 275 • 💬 21 • ⏱️ 14:54 • 3h ago

---

**[AI Genius Predicts the Next 3 Years](https://www.youtube.com/watch?v=lP86NzlXNf4)**

Watch the full interview with Scott Wu & Russell Kaplan here: https://youtu.be/-pZ3vD0r8a0?si=G7Ur_Zhvd32UsTtc Scott Wu is the ...

📺 Joe Lonsdale

👁️ 18K • 👍 489 • 💬 39 • ⏱️ 8:25 • 1d ago

---

**[Google DeepMind’s boss on AI, power, God and what’s next | The Economist](https://www.youtube.com/watch?v=aYjXt6iVt70)**

In the latest episode of Inside Tech, the Google DeepMind CEO, Demis Hassabis, talks to our AI writer, Alex Hern, about the ...

📺 The Economist

👁️ 56K • 👍 2K • 💬 135 • ⏱️ 6:26 • 12h ago

---

**[China Humiliates Trump with New AI Video](https://www.youtube.com/watch?v=QmVqDxLmSbA)**

Really American host Steve Harness breaks down how countries across the world are weaponizing ai to fight back at Trump.

📺 Really American

👁️ 529K • 👍 28K • 💬 2K • ⏱️ 11:59 • 1d ago

---

**[AI News: The Model That Has Everyone Freaked Out!](https://www.youtube.com/watch?v=SguncMvE77I)**

Here's the AI News you probably missed this week (and some you definitely didn't) - Join the newsletter at https://futuretools.io/ for ...

📺 Matt Wolfe

👁️ 88K • 👍 3K • 💬 352 • ⏱️ 35:50 • 2d ago

---

**[Elon Just Changed the AI Timeline](https://www.youtube.com/watch?v=Y2wy_nc-RGo)**

Larry Goldberg is a serial entrepreneur and has been an active Venture Capital investor for the last decade. Check out ...

📺 Brighter with Herbert

👁️ 43K • 👍 2K • 💬 104 • ⏱️ 34:47 • 2d ago

---

**[San Francisco store created and managed by AI](https://www.youtube.com/watch?v=QQWiSRVrIEA)**

Shoppers in San Francisco now have access to a store built, developed and run almost entirely by an AI bot. Scott Budman ...

📺 NBC Bay Area

👁️ 10K • 👍 139 • 💬 132 • ⏱️ 2:11 • 1d ago

---

**[Big AI News: So Many Gemini Updates, Claude’s Scary New Model + A New Google AI App…](https://www.youtube.com/watch?v=5Ev0b99hsUg)**

Try i10x: https://i10x.ai?fpr=paul53 Save 15% with code "PJL15" This week's biggest AI news: Gemini's new NotebookLM ...

📺 Paul J Lipsky

👁️ 37K • 👍 1K • 💬 105 • ⏱️ 16:34 • 1d ago

---

**[Claude Code + Higgsfield AI = Insane AI Ads](https://www.youtube.com/watch?v=EEvQ0OfB7BQ)**

Claude Code + Higgsfield AI = Insane AI Ads Try Higgsfield AI ✨https://higgsfield.ai/ai-video?fpr=utm&fp_sid=skai Hey Friends ...

📺 Skai Generated

👁️ 5K • 💬 2 • ⏱️ 8:12 • 7h ago

---

**[Anthropic Just KILLED The AI Agent Industry (Build 3 in 12 Min)](https://www.youtube.com/watch?v=gWtAY8LxGtE)**

GRAB THE 3 PROMPTS I USED All three agent prompts (recruiter, news digest, lead capture) are in our free WhatsApp ...

📺 Vaibhav Sisinty

👁️ 25K • 👍 854 • 💬 44 • ⏱️ 10:52 • 10h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 28,826 • ❤️ 1,071 • 23h ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,242,541 • ❤️ 1,778 • 2d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 7,452 • ❤️ 751 • 4d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 99,134 • ❤️ 961 • 2d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 873 • ❤️ 504 • 1d ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 775 • 6d ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 393,991 • ❤️ 523 • 10h ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

This image-text-to-text model, Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled, is fine-tuned on Qwen3.5-27B using Claude-4.6 Opus reasoning data for enhanced Chain-of-Thought capabilities. It excels at structured problem-solving and complex reasoning tasks, showing improved autonomy and stability in coding agent environments.

`image-text-to-text` `27.8B`

⬇️ 578,295 • ❤️ 2,599 • 7d ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 1,269,309 • ❤️ 608 • 2d ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 1,734,340 • ❤️ 624 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 9 • 💬 0 • ⭐ 15,536 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 161 • 💬 9 • ⭐ 38,987 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 43 • 💬 2 • ⭐ 49,866 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 24 • 💬 1 • ⭐ 16,431 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 156 • 💬 2 • ⭐ 59,482 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 4 • 💬 0 • ⭐ 13,235 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 50 • 💬 1 • ⭐ 76,286 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 52,783 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents](https://huggingface.co/papers/2604.07430)**

*Tencent Robotics X, HY Vision Team, Xumin Yu et al. (22 authors)*

🏢 Tencent Hunyuan

HY-Embodied-0.5 is a foundation model family for embodied agents featuring Mixture-of-Transformers architecture and iterative post-training for enhanced visual perception and reasoning capabilities.

▲ 155 • 💬 4 • ⭐ 427 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.07430) • [💻 code](https://github.com/Tencent-Hunyuan/HY-Embodied)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 38 • 💬 2 • ⭐ 33,012 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The highest-scoring AI memory system ever benchmarked. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 43.6k • 🔱 5.6k • 32m ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 31.8k • 🔱 6.2k • 13h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 23.7k • 🔱 2.5k • 6h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 22.0k • 🔱 1.0k • 8h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 7.5k • 🔱 467 • 11h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 11h ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.4k • 🔱 1.0k • 17d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.4k • 🔱 440 • 4d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.3k • 🔱 161 • 4h ago

---

**[midudev/autoskills](https://github.com/midudev/autoskills)**

One command. Your entire AI skill stack. Installed.

`TypeScript`

⭐ 2.6k • 🔱 265 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*
