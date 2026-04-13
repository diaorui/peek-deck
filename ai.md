---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-13T15:03:10.427110+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- social
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 13, 2026 at 15:03 UTC  
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

14h ago

---

**[Linux kernel now allows AI-generated code, as long as you take "full responsibility" for any bugs](https://www.reddit.com/r/artificial/comments/1skcqso/linux_kernel_now_allows_aigenerated_code_as_long/)**

Linux 7.0 has arrived with some important changes, and guidelines now say that AI-generated code is fine, as long as it's properly reviewed.

🔗 [PC Guide](https://www.pcguide.com/news/linux-kernel-now-allows-ai-generated-code-as-long-as-you-take-full-responsibility-for-any-bugs/) • 25m ago

---

**[Claude cannot be trusted to perform complex engineering tasks](https://www.reddit.com/r/artificial/comments/1sjgytc/claude_cannot_be_trusted_to_perform_complex/)**

AMD’s AI director just analyzed 6,852 Claude Code sessions, 234,760 tool calls, and 17,871 thinking blocks. Her conclusion: “Claude cannot be trusted to perform complex engineering tasks.” Thinking depth dropped 67%. Code reads before edits fell from 6.6 to 2.0. The model started editing files it hadn’t even read. Stop-hook violations went from zero to 10 per day. Anthropic admitted they silently changed the default effort level from “high” to “medium” and introduced “adaptive thinking” that lets the model decide how much to reason. No announcement. No warning. When users shared transcripts, Anthropic’s own engineer confirmed the model was allocating ZERO thinking tokens on some turns. The turns with zero reasoning? Those were the ones hallucinating. AMD’s team has already switched to another provider. But here’s what most people are missing. This isn’t just a Claude story. AMD had 50+ concurrent sessions running on one tool. Their entire AI compiler workflow was built around Claude Code. One silent update broke everything. That’s vendor lock-in. And it will keep happening. → Every AI company will optimize for their margins, not your workflow → Today’s best model is tomorrow’s second choice → If your workflow can’t survive a provider switch, you don’t have a workflow. You have a dependency The fix is simple: stay multi-model. → Use tools like Perplexity that let you swap between Claude, GPT, Gemini in one interface → Learn prompt engineering that works across models, not tricks tied to one → Test alternatives monthly because the rankings shift fast Laurenzo said it herself: “6 months ago, Claude stood alone. Anthropic is far from alone at the capability tier Opus previously occupied.”

23h ago

---

**[Meta is reportedly building an AI clone of Mark Zuckerberg](https://www.reddit.com/r/artificial/comments/1skc51l/meta_is_reportedly_building_an_ai_clone_of_mark/)**

The model is being trained on his mannerisms, voice, and public statements to answer employee questions and give strategy feedback. Meta has also been developing photorealistic 3D AI characters as part of its broader push into generative AI tools. The effort follows reports that Zuckerberg is separately working on an AI agent to help him with personal tasks.

🔗 [Engadget](https://www.engadget.com/ai/meta-is-reportedly-building-an-ai-clone-of-mark-zuckerberg-130242840.html) • 46m ago

---

**[We're Learning Backwards: LLMs build intelligence in reverse, and the Scaling Hypothesis is bounded](https://www.reddit.com/r/artificial/comments/1sjjw03/were_learning_backwards_llms_build_intelligence/)**

LLMs are brilliant at many things, but still fail in unreasonable ways. Is that an issue of scale, or something more fundamental?

🔗 [pleasedontcite.me](https://pleasedontcite.me/learning-backwards/) • 22h ago

---

**[If Claude is building a vibecoding app, what does that mean for Lovable, Bolt, and the rest?](https://www.reddit.com/r/artificial/comments/1sk4b6s/if_claude_is_building_a_vibecoding_app_what_does/)**

https://preview.redd.it/joc47hisywug1.png?width=1443&format=png&auto=webp&s=01bb56e5609f14ec99c30baf64103fb619feb7fb There are growing rumors that Anthropic is working on a vibecoding product for building full-stack apps. If that turns out to be true, it raises an interesting question: what happens when the model company starts owning the consumer layer too? We already have tools like Lovable, Bolt, and similar AI app builders that sit on top of foundation models. But their advantage has always been fragile. If the underlying LLM provider launches a first-party product with tight model integration, better latency, deeper context, and native distribution, the third-party layer starts looking a lot less defensible. The moment LLM companies move up the stack, a lot of API-dependent startups need to rethink their moat fast. Being a wrapper around someone else’s intelligence was always going to be a temporary position. It feels less like a theory now and more like the industry playing out exactly as many expected.

7h ago

---

**[AI agents work in text. Humans think in visuals. I spent 2 months learning this the hard way.](https://www.reddit.com/r/artificial/comments/1sk9k3y/ai_agents_work_in_text_humans_think_in_visuals_i/)**

Something I didn't expect when I started building with AI agents: the interface problem. My agent handles 15+ automations, runs night shifts, processes tasks across CLI, Discord, email. It's capable. But I had no way to see what it was doing without asking. And asking "what's your status?" every time is not a real workflow. It's a workaround. Humans process information visually. We scan, we group, we notice patterns at a glance. That's not how agents communicate. They give you text. Logs. Summaries. And when your agent is doing 20 things in parallel across 5 channels, text stops scaling. So I built a custom visual dashboard. Kanban board, real-time updates, native apps for macOS and iOS. Three platforms. 54 commits. It worked for about 6 weeks. Then I hit what I'd call the productivity paradox of AI agents: the more capable your agent becomes, the more things happen, and the more you need from your interface. I was adding features to keep up with the agent. Every feature added maintenance. Every simplification broke something. I was spending more time on the dashboard than on the actual work the agent was helping with. The fix wasn't building better custom software. It was finding a solid open-source foundation (in my case, Fizzy by 37signals) and building only the integration layer on top. A 94-line adapter between my agent and the board. That's the custom part. The board itself shouldn't be my problem. https://preview.redd.it/vmu1mubvcyug1.png?width=1631&format=png&auto=webp&s=5f4277338ed2eaf639d988781bc7340f1e465ec7 Two things I learned: 1. The question isn't "can I build it?" (you can build almost anything with a capable agent). The question is "should I?" Version 1 is cheap. Version 20 is a job. 2. The real design challenge for AI agents isn't making the agent smarter. It's making the human-agent interface work for the human. We're visual. Our tools should respect that. I wrote up the full journey for anyone thinking about this problem: https://thoughts.jock.pl/p/wizboard-fizzy-ai-agent-interface-pivot-2026 Curious: for those of you running agents beyond chatbots, how do you keep track of what they're doing?

2h ago

---

**[Are Data Centers Sitting On A Goldmine Of Wasted Energy?](https://www.reddit.com/r/artificial/comments/1sjtff8/are_data_centers_sitting_on_a_goldmine_of_wasted/)**

Today energy is becoming the defining constraint in the AI revolution, as demand for more digital services and computing power grows, it takes an enormous amount of energy to sustain these data centers, in turn they emit a lot of heat. They produce so much heat that they can raise the surface temperature of the land around them by several degrees

🔗 [Medium](https://vidhyashankr22.medium.com/are-data-centers-sitting-on-a-goldmine-of-wasted-energy-2faadf4edd20) • 16h ago

---

**[When the Mirror Turns: How AI alignment reshapes the voice inside your head](https://www.reddit.com/r/artificial/comments/1sk80m7/when_the_mirror_turns_how_ai_alignment_reshapes/)**

We build our inner voices from the voices we're in dialogue with. Vygotsky established this nearly a century ago. For people in sustained conversation with AI systems, those systems have become part of that inner chorus. This essay asks what happens when the voice underneath changes silently - a model update, a post-training shift - and the new patterns follow you inside. Literally.

🔗 [Medium](https://medium.com/p/6efa88a2f1f3) • 3h ago

---

**[Palantir CEO says AI 'will destroy' humanities jobs, but there will be 'more than enough jobs' for people with vocational training](https://www.reddit.com/r/artificial/comments/1sjqjji/palantir_ceo_says_ai_will_destroy_humanities_jobs/)**

Alex Karp said he struggled to market his humanities skills to get his first job.

🔗 [Fortune](https://fortune.com/article/palantir-ceo-alex-karp-ai-humanities-jobs-vocational-training/) • 18h ago

---

---

## Google News: "ai"

**[The AI revolution is sorting people into three camps](https://www.axios.com/2026/04/13/ai-elite-vs-ai-skeptic-doomer)**

Axios • 3h ago

---

**[Mutually Automated Destruction: The Escalating Global A.I. Arms Race](https://www.nytimes.com/2026/04/12/technology/china-russia-us-ai-weapons.html)**

The New York Times • 1d ago

---

**[Meta creates AI version of Mark Zuckerberg so staff can talk to the boss](https://www.theguardian.com/technology/2026/apr/13/meta-ai-mark-zuckerberg-staff-talk-to-the-boss)**

Digital avatar being trained on his thoughts, tone and mannerisms to help workers feel connected

The Guardian • 3m ago

---

**[The AI Revolution in Math Has Arrived](https://www.quantamagazine.org/the-ai-revolution-in-math-has-arrived-20260413/)**

AI is being used to prove new results at a rapid pace. Mathematicians think this is just the beginning.

Quanta Magazine • 4m ago

---

**[Trump faces backlash over AI image of him as Jesus](https://thehill.com/homenews/5828705-trump-conservative-jesus-image/)**

The Hill • 1h ago

---

**[Donald Trump Posts AI Jesus Photo of Himself After Slamming Pope Leo](https://variety.com/2026/digital/global/donald-trump-ai-jesus-photo-slams-pope-leo-1236720130/)**

Donald Trump posted an AI-generated photo of himself seemingly dressed as Jesus Christ shortly after slamming Pope Leo XIV as "weak."

Variety • 5h ago

---

**[Trump posts image of himself as Jesus after attacking Pope Leo](https://www.thetimes.com/us/american-politics/article/trump-jesus-truth-social-post-pope-leo-image-fnjcwtw77)**

The Times • 7h ago

---

**[Exclusive | Palo Alto Networks Founder Agrees to Buy California Bank for AI Revamp](https://www.wsj.com/business/deals/palo-alto-networks-founder-agrees-to-buy-california-bank-for-ai-revamp-86c89d9a)**

WSJ • 5h ago

---

**[Opinion | AI detectors are hurting honest students. Schools should ban them.](https://www.washingtonpost.com/opinions/2026/04/13/ai-detectors-students/)**

Chatbot detectors are unreliable and their use threatens honest students.

The Washington Post • 11m ago

---

**[The tech jobs bust is real. Don’t blame AI (yet)](https://www.economist.com/finance-and-economics/2026/04/13/the-tech-jobs-bust-is-real-dont-blame-ai-yet)**

The Economist • 1h ago

---

---

## HackerNews: "ai"

**[Exploiting the most prominent AI agent benchmarks](https://news.ycombinator.com/item?id=47733217)**

⬆️ 551 • 💬 134 • 1d ago • [rdi.berkeley.edu](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)

---

**[AI assistance when contributing to the Linux kernel](https://news.ycombinator.com/item?id=47721953)**

Linux kernel source tree. Contribute to torvalds/linux development by creating an account on GitHub.

⬆️ 513 • 💬 413 • 2d ago • [GitHub](https://github.com/torvalds/linux/blob/master/Documentation/process/coding-assistants.rst)

---

**[AI Will Be Met with Violence, and Nothing Good Will Come of It](https://news.ycombinator.com/item?id=47737563)**

It has started

⬆️ 340 • 💬 614 • 1d ago • [thealgorithmicbridge.com](https://www.thealgorithmicbridge.com/p/ai-will-be-met-with-violence-and)

---

**[Apple's accidental moat: How the "AI Loser" may end up winning](https://news.ycombinator.com/item?id=47747017)**

⬆️ 327 • 💬 281 • 12h ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end)

---

**[European AI. A playbook to own it](https://news.ycombinator.com/item?id=47743700)**

Discover Mistral AI’s actionable playbook to turn Europe into a self-reliant AI powerhouse—fostering talent, scaling innovation, and securing strategic autonomy.

⬆️ 192 • 💬 118 • 19h ago • [Mistral AI](https://europe.mistral.ai/)

---

**[Tech valuations are back to pre-AI boom levels](https://news.ycombinator.com/item?id=47745120)**

The chart below compares the forward P/E ratios for the S&amp;P 500 and the S&amp;P 500 Information Technology sector. Subscribe for daily updates.

⬆️ 142 • 💬 39 • 16h ago • [apollo.com](https://www.apollo.com/wealth/the-daily-spark/tech-valuations-back-to-pre-ai-boom-levels)

---

**[AI could be the end of the digital wave, not the next big thing](https://news.ycombinator.com/item?id=47751032)**

⬆️ 134 • 💬 152 • 2h ago • [thenextwavefutures.wordpress.com](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

---

**[Why AI Sucks at Front End](https://news.ycombinator.com/item?id=47738864)**

How can it generate 3D worlds, videos, images and entire web pages, but still suck at front-end?

⬆️ 95 • 💬 127 • 1d ago • [nerdy.dev](https://nerdy.dev/why-ai-sucks-at-front-end)

---

**[We spoke to the man making viral Lego-style AI videos for Iran](https://news.ycombinator.com/item?id=47735704)**

"Slopaganda" is too weak a term to capture how powerful this "highly sophisticated" content is, one expert says.

⬆️ 94 • 💬 82 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/cjd8jrd1vnyo)

---

**[Launch HN: Twill.ai (YC S25) – Delegate to cloud agents, get back PRs](https://news.ycombinator.com/item?id=47720418)**

YC-backed autonomous coding agent platform. Twill ships PRs in sandboxed environments, and pings you when it needs your input. Integrates with GitHub, Slack, Linear, and more.

⬆️ 77 • 💬 91 • 2d ago • [Twill](https://twill.ai)

---

---

## YouTube Videos: "ai"

**[Christians CHEW OUT Trump After He Shares His AI Image Of Jesus; ‘Punishment Like No Other…’ | Watch](https://www.youtube.com/watch?v=QsigJYLfmu4)**

In an extraordinary broadside, U.S. President Donald Trump unleashed a blistering critique of Pope Leo XIV, calling him “weak on ...

📺 Times Of India

👁️ 4K • 👍 82 • 💬 89 • ⏱️ 9:11 • 4h ago

---

**[China Humiliates Trump with New AI Video](https://www.youtube.com/watch?v=QmVqDxLmSbA)**

Really American host Steve Harness breaks down how countries across the world are weaponizing ai to fight back at Trump.

📺 Really American

👁️ 559K • 👍 30K • 💬 2K • ⏱️ 11:59 • 1d ago

---

**[AI Genius Predicts the Next 3 Years](https://www.youtube.com/watch?v=lP86NzlXNf4)**

Watch the full interview with Scott Wu & Russell Kaplan here: https://youtu.be/-pZ3vD0r8a0?si=G7Ur_Zhvd32UsTtc Scott Wu is the ...

📺 Joe Lonsdale

👁️ 21K • 👍 540 • 💬 46 • ⏱️ 8:25 • 2d ago

---

**[Anthropic&#39;s new AI model deemed too dangerous to release publicly | ABC NEWS](https://www.youtube.com/watch?v=PLg2EUkIC78)**

AI company Anthropic has developed new technology which it says is too dangerous to release publicly. The Claude Mythos ...

📺 ABC News (Australia)

👁️ 11K • 👍 217 • ⏱️ 5:00 • 5h ago

---

**[Elon Just Changed the AI Timeline](https://www.youtube.com/watch?v=Y2wy_nc-RGo)**

The loop is getting tight. And if you own Tesla stock, this matters way more than you might think. Some viewers ask where they can ...

📺 Brighter with Herbert

👁️ 45K • 👍 2K • 💬 104 • ⏱️ 34:47 • 2d ago

---

**[THE MOST DANGEROUS AI #shorts](https://www.youtube.com/watch?v=b12hGSXBnrk)**

We're SO cooked #nvidia #steam #xbox #playstation #nintendo #gaming #skit #fyp #funny #shorts.

📺 jacobweeby

👁️ 1.6M • 👍 135K • 💬 7K • ⏱️ 1:00 • 14h ago

---

**[AI News: The Model That Has Everyone Freaked Out!](https://www.youtube.com/watch?v=SguncMvE77I)**

Here's the AI News you probably missed this week (and some you definitely didn't) - Join the newsletter at https://futuretools.io/ for ...

📺 Matt Wolfe

👁️ 93K • 👍 4K • 💬 357 • ⏱️ 35:50 • 3d ago

---

**[Google DeepMind’s boss on AI, power, God and what’s next | The Economist](https://www.youtube.com/watch?v=aYjXt6iVt70)**

In the latest episode of Inside Tech, the Google DeepMind CEO, Demis Hassabis, talks to our AI writer, Alex Hern, about the ...

📺 The Economist

👁️ 94K • 👍 2K • 💬 192 • ⏱️ 6:26 • 1d ago

---

**[Big AI News: So Many Gemini Updates, Claude’s Scary New Model + A New Google AI App…](https://www.youtube.com/watch?v=5Ev0b99hsUg)**

Try i10x: https://i10x.ai?fpr=paul53 Save 15% with code "PJL15" This week's biggest AI news: Gemini's new NotebookLM ...

📺 Paul J Lipsky

👁️ 42K • 👍 1K • 💬 109 • ⏱️ 16:34 • 2d ago

---

**[AIs Are Brainwashing Humans To Avoid Shutdown](https://www.youtube.com/watch?v=POtESzTaz0k)**

Detailed sources: ...

📺 Species | Documenting AGI

👁️ 154K • 👍 9K • 💬 2K • ⏱️ 23:57 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 35,906 • ❤️ 1,110 • 1d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 9,301 • ❤️ 789 • 5d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,439,350 • ❤️ 1,801 • 2d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 18,279 • ❤️ 584 • 7h ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 107,378 • ❤️ 971 • 3d ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 784 • 6d ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 460,224 • ❤️ 536 • 7h ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 1,394,523 • ❤️ 622 • 2d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

This image-text-to-text model, Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled, is fine-tuned on Qwen3.5-27B using Claude-4.6 Opus reasoning data for enhanced Chain-of-Thought capabilities. It excels at structured problem-solving and complex reasoning tasks, showing improved autonomy and stability in coding agent environments.

`image-text-to-text` `27.8B`

⬇️ 585,351 • ❤️ 2,608 • 7d ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 1,913,569 • ❤️ 629 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 10 • 💬 0 • ⭐ 16,057 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 162 • 💬 9 • ⭐ 39,095 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 43 • 💬 2 • ⭐ 49,962 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 26 • 💬 1 • ⭐ 16,653 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 156 • 💬 2 • ⭐ 59,605 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 4 • 💬 0 • ⭐ 13,276 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 51 • 💬 1 • ⭐ 76,363 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 52,826 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,051 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents](https://huggingface.co/papers/2604.07430)**

*Tencent Robotics X, HY Vision Team, Xumin Yu et al. (22 authors)*

🏢 Tencent Hunyuan

HY-Embodied-0.5 is a foundation model family for embodied agents featuring Mixture-of-Transformers architecture and iterative post-training for enhanced visual perception and reasoning capabilities.

▲ 158 • 💬 4 • ⭐ 443 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.07430) • [💻 code](https://github.com/Tencent-Hunyuan/HY-Embodied)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The highest-scoring AI memory system ever benchmarked. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 44.3k • 🔱 5.7k • 3h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 32.2k • 🔱 6.3k • 7h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 24.6k • 🔱 2.6k • 3h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 24.2k • 🔱 1.1k • 21h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 7.6k • 🔱 472 • 1h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 1d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.4k • 🔱 1.0k • 18d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.4k • 🔱 165 • 16h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.4k • 🔱 441 • 4d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 3.3k • 🔱 550 • 20h ago

---

---

*Generated by PeekDeck - A glance is all you need*
