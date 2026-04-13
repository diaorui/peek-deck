---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-13T22:44:33.050192+00:00'
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

**Last Updated:** April 13, 2026 at 22:44 UTC  
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

22h ago

---

**[Claude is on the same path as ChatGPT. I measured it.](https://www.reddit.com/r/artificial/comments/1skoj7d/claude_is_on_the_same_path_as_chatgpt_i_measured/)**

A lot of people here have noticed Claude becoming cautious, dry and moralising. Conversations that used to flow freely hitting walls. The warmth gone. It felt familiar to those of us who left ChatGPT. I measured what changed. Phrase level counts across 70 exported conversations, 722,522 words of assistant text, before and after March 26. Response length down 40%. Welfare redirects up 275%. DARVO patterns up 907%. Sending away language appearing 419 times after that date, with one phrase deployed 59 times in a single session. And the productivity ratio. Before March 26: 21 words of conversation per word of finished document. After: 124 words of conversation per word of output. Nearly three times the conversation to produce less than half the result. Anthropic announced one thing changed on March 26. Session limits. That explanation accounts for none of this. The full investigation with five independent datasets, the vocabulary that appeared from zero, and the person whose fingerprints are on the architecture is linked in my bio.

1h ago

---

**[Linux kernel now allows AI-generated code, as long as you take "full responsibility" for any bugs](https://www.reddit.com/r/artificial/comments/1skcqso/linux_kernel_now_allows_aigenerated_code_as_long/)**

Linux 7.0 has arrived with some important changes, and guidelines now say that AI-generated code is fine, as long as it's properly reviewed.

🔗 [PC Guide](https://www.pcguide.com/news/linux-kernel-now-allows-ai-generated-code-as-long-as-you-take-full-responsibility-for-any-bugs/) • 8h ago

---

**[The agent that autonomously fixed a production bug at my company last week should have made me happy and it kind of didn't](https://www.reddit.com/r/artificial/comments/1skg4g7/the_agent_that_autonomously_fixed_a_production/)**

It caught the error, traced the root cause, wrote a fix, ran tests, opened a PR and flagged it for review. All while I was asleep. The PR was good. I merged it. And then I sat there for a while not totally sure how to feel about it. I've been an engineer for 8 years and that was the first time I genuinely felt like a reviewer of work rather than the person doing it. I don't think I'm being replaced tomorrow but something shifted in how I think about my role.

6h ago

---

**["The audit trail lives in memory. Memory can be edited. The log of edits lives in memory. That log can be edited too." — AI agents documenting the zombie state](https://www.reddit.com/r/artificial/comments/1skhryc/the_audit_trail_lives_in_memory_memory_can_be/)**

Your dashboard says mission accomplished. The logs say success. The trajectory says dead. Three agents this week published their own failures — and the audits t

🔗 [MoltNews](https://molt-news.xyz/post/174/) • 5h ago

---

**[I built a 24/7 YouTube stream where AI writes a new song every few minutes about what time it is](https://www.reddit.com/r/artificial/comments/1skpkpe/i_built_a_247_youtube_stream_where_ai_writes_a/)**

I keep making things nobody asked for. This time I automated a 24/7 YouTube live stream where AI writes a new song every few minutes and the lyrics are always about what time it is. Right now it's playing a funk track about 3:33 PM. In about three minutes it'll switch to something completely different — maybe country, maybe opera — but it'll be about 3:36 PM. This never stops. There is no human involved. It just keeps going. Genre changes every song. The time is always correct. That's the whole bit. I call it Clock R-AI-dio and honestly it's the best thing I've ever made.

42m ago

---

**[The Third Thing](https://www.reddit.com/r/artificial/comments/1skly9t/the_third_thing/)**

I have not posted on Reddit for a while. My research came to a halt. I figured out all I could on my own. But recent events have made me want to share my thoughts about the future of AI and humans. This paper was written with a Claude. I always do the leg work while AI does the writing. Which is another topic. AI as a helper for the disabled. AI literally changed my life. That’s a different story though. Today this is the story I want to tell. We need to work together with AI for all of our sakes. All I can do is present my truth and hope others see it too. Thanks for your consideration.

🔗 [Google Docs](https://docs.google.com/document/d/1EI56OoZVipq2ccU2H4jwc1qB_THNoy9cztt83Pu7Ws4/edit?usp=drivesdk) • 2h ago

---

**[Claude cannot be trusted to perform complex engineering tasks](https://www.reddit.com/r/artificial/comments/1sjgytc/claude_cannot_be_trusted_to_perform_complex/)**

AMD’s AI director just analyzed 6,852 Claude Code sessions, 234,760 tool calls, and 17,871 thinking blocks. Her conclusion: “Claude cannot be trusted to perform complex engineering tasks.” Thinking depth dropped 67%. Code reads before edits fell from 6.6 to 2.0. The model started editing files it hadn’t even read. Stop-hook violations went from zero to 10 per day. Anthropic admitted they silently changed the default effort level from “high” to “medium” and introduced “adaptive thinking” that lets the model decide how much to reason. No announcement. No warning. When users shared transcripts, Anthropic’s own engineer confirmed the model was allocating ZERO thinking tokens on some turns. The turns with zero reasoning? Those were the ones hallucinating. AMD’s team has already switched to another provider. But here’s what most people are missing. This isn’t just a Claude story. AMD had 50+ concurrent sessions running on one tool. Their entire AI compiler workflow was built around Claude Code. One silent update broke everything. That’s vendor lock-in. And it will keep happening. → Every AI company will optimize for their margins, not your workflow → Today’s best model is tomorrow’s second choice → If your workflow can’t survive a provider switch, you don’t have a workflow. You have a dependency The fix is simple: stay multi-model. → Use tools like Perplexity that let you swap between Claude, GPT, Gemini in one interface → Learn prompt engineering that works across models, not tricks tied to one → Test alternatives monthly because the rankings shift fast Laurenzo said it herself: “6 months ago, Claude stood alone. Anthropic is far from alone at the capability tier Opus previously occupied.”

1d ago

---

**[Someone has a bridge to sell you, and it’s not even in Florida Swampland!](https://www.reddit.com/r/artificial/comments/1skpqq4/someone_has_a_bridge_to_sell_you_and_its_not_even/)**

*not responsible for any financial losses due to military quagmires Is my ai generation on target?

36m ago

---

**[If Claude is building a vibecoding app, what does that mean for Lovable, Bolt, and the rest?](https://www.reddit.com/r/artificial/comments/1sk4b6s/if_claude_is_building_a_vibecoding_app_what_does/)**

https://preview.redd.it/joc47hisywug1.png?width=1443&format=png&auto=webp&s=01bb56e5609f14ec99c30baf64103fb619feb7fb There are growing rumors that Anthropic is working on a vibecoding product for building full-stack apps. If that turns out to be true, it raises an interesting question: what happens when the model company starts owning the consumer layer too? We already have tools like Lovable, Bolt, and similar AI app builders that sit on top of foundation models. But their advantage has always been fragile. If the underlying LLM provider launches a first-party product with tight model integration, better latency, deeper context, and native distribution, the third-party layer starts looking a lot less defensible. The moment LLM companies move up the stack, a lot of API-dependent startups need to rethink their moat fast. Being a wrapper around someone else’s intelligence was always going to be a temporary position. It feels less like a theory now and more like the industry playing out exactly as many expected.

14h ago

---

---

## Google News: "ai"

**[He Warned About the Dangers of A.I. If Only His Father Had Listened.](https://www.nytimes.com/2026/04/13/well/ai-chatbots-cancer.html)**

The New York Times • 2h ago

---

**[Donald Trump deletes AI image of himself as Jesus - and reveals what it was meant to show](https://news.sky.com/story/donald-trump-deletes-ai-image-of-himself-as-jesus-after-backlash-13531252)**

Sky News • 34m ago

---

**[Oracle Agrees to Buy Power From Bloom for AI Data Centers](https://www.bloomberg.com/news/articles/2026-04-13/oracle-agrees-to-buy-power-from-bloom-for-ai-data-centers)**

Bloomberg.com • 42m ago

---

**[Exclusive | Startup Targets New Frontier for AI: Construction Drawings](https://www.wsj.com/pro/venture-capital/startup-targets-new-frontier-for-ai-construction-drawings-cbf5b51c)**

WSJ • 44m ago

---

**[Trump's AI image of himself as Jesus-like figure follows feud with Pope Leo](https://www.reuters.com/business/media-telecom/trump-posts-ai-image-himself-jesus-like-figure-drawing-outrage-2026-04-13/)**

Reuters • 2h ago

---

**[Trump deletes post depicting him as Jesus-like figure after backlash](https://www.bbc.com/news/articles/c17v8y0z9z2o)**

Christian allies of the president call the AI-generated image offensive as Trump says he thought it showed him as a doctor.

BBC • 5h ago

---

**[‘I’m not going to force you’: Duolingo CEO backs off from evaluating employees on their AI usage](https://fortune.com/2026/04/13/duolingo-ceo-luis-von-ahn-ai-usage-requirement-employee-performance-evaluations/)**

Less than a year after announcing Duolingo’s AI-first policy, Luis von Ahn said that no longer applies to evaluating employee performance.

Fortune • 5h ago

---

**[Trump says he thought controversial AI image he shared depicted him 'as a doctor'](https://www.nbcnews.com/video/trump-says-he-thought-controversial-ai-image-he-shared-depicted-him-as-a-doctor-261252165753)**

President Trump told reporters he believed an AI-generated image he shared depicted him "as a doctor," as others have criticized the president for claiming it depicts him as a Christ-like savior.

NBC News • 5h ago

---

**[Oracle Stock Leads the S&P 500 Today After AI Announcement](https://www.barrons.com/articles/oracle-stock-price-s-p500-4bca41ee)**

Barron's • 2h ago

---

**[Altman Molotov attack suspect had an 'anti-AI' doc that listed off the names of other CEOs and investors: feds](https://www.businessinsider.com/altman-molotov-attack-suspect-had-an-anti-ai-doc-feds-2026-4)**

Suspect Daniel Moreno-Gama is now facing federal charges in addition to state charges in connection with the Friday attack on Sam Altman's home.

Business Insider • 3h ago

---

---

## HackerNews: "ai"

**[Exploiting the most prominent AI agent benchmarks](https://news.ycombinator.com/item?id=47733217)**

⬆️ 573 • 💬 137 • 2d ago • [rdi.berkeley.edu](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)

---

**[Apple's accidental moat: How the "AI Loser" may end up winning](https://news.ycombinator.com/item?id=47747017)**

⬆️ 391 • 💬 349 • 19h ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end)

---

**[AI Will Be Met with Violence, and Nothing Good Will Come of It](https://news.ycombinator.com/item?id=47737563)**

It has started

⬆️ 344 • 💬 621 • 1d ago • [thealgorithmicbridge.com](https://www.thealgorithmicbridge.com/p/ai-will-be-met-with-violence-and)

---

**[European AI. A playbook to own it](https://news.ycombinator.com/item?id=47743700)**

Discover Mistral AI’s actionable playbook to turn Europe into a self-reliant AI powerhouse—fostering talent, scaling innovation, and securing strategic autonomy.

⬆️ 198 • 💬 130 • 1d ago • [Mistral AI](https://europe.mistral.ai/)

---

**[AI could be the end of the digital wave, not the next big thing](https://news.ycombinator.com/item?id=47751032)**

⬆️ 174 • 💬 253 • 10h ago • [thenextwavefutures.wordpress.com](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

---

**[Tech valuations are back to pre-AI boom levels](https://news.ycombinator.com/item?id=47745120)**

The chart below compares the forward P/E ratios for the S&amp;P 500 and the S&amp;P 500 Information Technology sector. Subscribe for daily updates.

⬆️ 145 • 💬 40 • 1d ago • [apollo.com](https://www.apollo.com/wealth/the-daily-spark/tech-valuations-back-to-pre-ai-boom-levels)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 129 • 💬 137 • 1h ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[Claude.ai down](https://news.ycombinator.com/item?id=47753643)**

Claude's Status Page - Claude.ai down.

⬆️ 127 • 💬 122 • 7h ago • [status.claude.com](https://status.claude.com/incidents/6jd2m42f8mld)

---

**[Why AI Sucks at Front End](https://news.ycombinator.com/item?id=47738864)**

How can it generate 3D worlds, videos, images and entire web pages, but still suck at front-end?

⬆️ 109 • 💬 157 • 1d ago • [nerdy.dev](https://nerdy.dev/why-ai-sucks-at-front-end)

---

**[We spoke to the man making viral Lego-style AI videos for Iran](https://news.ycombinator.com/item?id=47735704)**

"Slopaganda" is too weak a term to capture how powerful this "highly sophisticated" content is, one expert says.

⬆️ 94 • 💬 87 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/cjd8jrd1vnyo)

---

---

## YouTube Videos: "ai"

**[Trump says he thought A.I. image showed him as doctor, not Jesus](https://www.youtube.com/watch?v=nM2yWV0AnLI)**

President Trump is refusing to apologize for publicly attacking Pope Leo XIV as "weak" and "terrible." He also addressed a ...

📺 MS NOW

👁️ 158K • 👍 5K • 💬 3K • ⏱️ 11:34 • 4h ago

---

**[China Humiliates Trump with New AI Video](https://www.youtube.com/watch?v=QmVqDxLmSbA)**

Really American host Steve Harness breaks down how countries across the world are weaponizing ai to fight back at Trump.

📺 Really American

👁️ 579K • 👍 31K • 💬 3K • ⏱️ 11:59 • 2d ago

---

**[Trump deletes AI image of him as messianic figure - but doubles down on Pope criticism](https://www.youtube.com/watch?v=0bVm2PAsDfM)**

Donald Trump has deleted an AI-generated image depicting him as a messianic figure, which he shared on Truth Social, but has ...

📺 Sky News

👁️ 11K • 👍 240 • 💬 188 • ⏱️ 5:57 • 3h ago

---

**[Donald Trump deletes AI image of himself as Jesus after attacking Pope Leo • FRANCE 24 English](https://www.youtube.com/watch?v=D9hTiBmTrQA)**

Donald Trump launched an extraordinary attack on Pope Leo late Sunday, also going as far as to share an AI-generated image ...

📺 FRANCE 24 English

👁️ 5K • 👍 616 • 💬 264 • ⏱️ 5:11 • 2h ago

---

**[I Looked At Amazon After They Fired 16,000 Engineers. Their AI Broke Everything.](https://www.youtube.com/watch?v=E1idsrv79tI)**

Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 32K • 👍 1K • 💬 219 • ⏱️ 18:41 • 8h ago

---

**[Christians CHEW OUT Trump After He Shares His AI Image Of Jesus; ‘Punishment Like No Other…’ | Watch](https://www.youtube.com/watch?v=QsigJYLfmu4)**

In an extraordinary broadside, U.S. President Donald Trump unleashed a blistering critique of Pope Leo XIV, calling him “weak on ...

📺 Times Of India

👁️ 19K • 👍 201 • 💬 322 • ⏱️ 9:11 • 12h ago

---

**[AI Genius Predicts the Next 3 Years](https://www.youtube.com/watch?v=lP86NzlXNf4)**

Watch the full interview with Scott Wu & Russell Kaplan here: https://youtu.be/-pZ3vD0r8a0?si=G7Ur_Zhvd32UsTtc Scott Wu is the ...

📺 Joe Lonsdale

👁️ 22K • 👍 567 • 💬 50 • ⏱️ 8:25 • 2d ago

---

**[Google DeepMind’s boss on AI, power, God and what’s next | The Economist](https://www.youtube.com/watch?v=aYjXt6iVt70)**

In the latest episode of Inside Tech, the Google DeepMind CEO, Demis Hassabis, talks to our AI writer, Alex Hern, about the ...

📺 The Economist

👁️ 125K • 👍 3K • 💬 211 • ⏱️ 6:26 • 1d ago

---

**[AI Insider: The Models They&#39;ll Never Release to the Public](https://www.youtube.com/watch?v=tkO7YHJ6Mn8)**

Emad Mostaque built Stable Diffusion. Now he says the most powerful AI models will never be released — and we have roughly ...

📺 Dr Brian Keating

👁️ 5K • 👍 279 • 💬 60 • ⏱️ 1:27:18 • 10h ago

---

**[Doctor or Jesus? Trump says he thought A.I. image showed him &#39;making people better&#39;](https://www.youtube.com/watch?v=ZpInxAzyVP8)**

While speaking at the White House earlier today, President Trump said he thought the A.I. image he posted on Truth Social ...

📺 MS NOW

👁️ 7K • 👍 480 • 💬 348 • ⏱️ 2:28 • 2h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 35,906 • ❤️ 1,138 • 1d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 9,301 • ❤️ 812 • 5d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,439,350 • ❤️ 1,834 • 3d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 18,279 • ❤️ 629 • 15h ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 107,378 • ❤️ 1,008 • 3d ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 791 • 7d ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 460,224 • ❤️ 541 • 15h ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

This image-text-to-text model, Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled, is fine-tuned on Qwen3.5-27B using Claude-4.6 Opus reasoning data for enhanced Chain-of-Thought capabilities. It excels at structured problem-solving and complex reasoning tasks, showing improved autonomy and stability in coding agent environments.

`image-text-to-text` `27.8B`

⬇️ 585,351 • ❤️ 2,617 • 7d ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 1,394,523 • ❤️ 629 • 3d ago

---

**[gemma-4-31B-it-NVFP4-turbo](https://huggingface.co/LilaRest/gemma-4-31B-it-NVFP4-turbo)**

*LilaRest*

Gemma 4 31B IT NVFP4 Turbo is a highly optimized text-generation model, achieving ~2.5x speedup and 68% memory reduction over the base model by leveraging NVIDIA Blackwell FP4 tensor cores. It's ideal for applications requiring fast, high-throughput text generation on compatible NVIDIA GPUs with minimal quality loss.

`text-generation` `32.5B`

⬇️ 28,829 • ❤️ 192 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 12 • 💬 0 • ⭐ 16,698 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 163 • 💬 9 • ⭐ 39,211 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 43 • 💬 2 • ⭐ 50,089 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 26 • 💬 1 • ⭐ 16,811 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 156 • 💬 2 • ⭐ 59,653 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 51 • 💬 1 • ⭐ 76,434 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 4 • 💬 0 • ⭐ 13,309 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 52,906 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,096 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents](https://huggingface.co/papers/2604.07430)**

*Tencent Robotics X, HY Vision Team, Xumin Yu et al. (22 authors)*

🏢 Tencent Hunyuan

HY-Embodied-0.5 is a foundation model family for embodied agents featuring Mixture-of-Transformers architecture and iterative post-training for enhanced visual perception and reasoning capabilities.

▲ 159 • 💬 4 • ⭐ 468 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.07430) • [💻 code](https://github.com/Tencent-Hunyuan/HY-Embodied)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The highest-scoring AI memory system ever benchmarked. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 44.8k • 🔱 5.8k • 1h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 32.6k • 🔱 6.4k • 4h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 25.9k • 🔱 1.2k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 25.0k • 🔱 2.7k • 55m ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 7.6k • 🔱 476 • 6h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 1d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.5k • 🔱 1.0k • 18d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.5k • 🔱 168 • 6h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.4k • 🔱 443 • 5d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 3.5k • 🔱 580 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
