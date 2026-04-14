---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-14T13:59:06.760358+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 14, 2026 at 13:59 UTC  
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

**[Claude is on the same path as ChatGPT. I measured it.](https://www.reddit.com/r/artificial/comments/1skoj7d/claude_is_on_the_same_path_as_chatgpt_i_measured/)**

A lot of people here have noticed Claude becoming cautious, dry and moralising. Conversations that used to flow freely hitting walls. The warmth gone. It felt familiar to those of us who left ChatGPT. I measured what changed. Phrase level counts across 70 exported conversations, 722,522 words of assistant text, before and after March 26. Response length down 40%. Welfare redirects up 275%. DARVO patterns up 907%. Sending away language appearing 419 times after that date, with one phrase deployed 59 times in a single session. And the productivity ratio. Before March 26: 21 words of conversation per word of finished document. After: 124 words of conversation per word of output. Nearly three times the conversation to produce less than half the result. Anthropic announced one thing changed on March 26. Session limits. That explanation accounts for none of this. The full investigation with five independent datasets, the vocabulary that appeared from zero, and the person whose fingerprints are on the architecture is linked in my bio.

16h ago

---

**[Why don't LLMs track time in their conversations?](https://www.reddit.com/r/artificial/comments/1sky7h9/why_dont_llms_track_time_in_their_conversations/)**

Question for everyone: Why do you think LLMs like Claude don't use timestamp data within conversations to build temporal awareness? Like, it seems straightforward to track how long you've been talking, notice when you're looping on the same idea for hours, and suggest pivoting. Or acknowledge that conversation fatigue might be setting in. From a UX perspective, I'd expect this would make the tool way more engaging Is there a technical limitation I'm missing, or is it more of a design choice? Thanks!

9h ago

---

**[openclaw ai agent vs just using chatgpt](https://www.reddit.com/r/artificial/comments/1sl564k/openclaw_ai_agent_vs_just_using_chatgpt/)**

I've been using AI tools pretty heavily for the past couple of years. ChatGPT, Claude, Perplexity, a few others. I thought I had a good mental model of what these things could and couldn't do. Then I set up an openclaw agent and realized I had been thinking about it completely wrong. The difference isn't capability. Claude is more capable than my openclaw agent in a lot of way, the difference is orientation. Every AI tool I've used before openclaw was something I went to. I opened a tab, typed something, got a response, closed the tab, so the interaction was entirely initiated by me and ended when I stopped typing. Openclaw runs the other direction. It's sitting there whether I'm at my computer or not. It messaged me yesterday while I was in a meeting to flag an email that needed a same day response. I didn't ask it to do that, I just told it once, weeks ago, that time sensitive client emails matter and it should interrupt me and it remembered and acted on it. That sounds like a small thing but it fundamentally changes the relationship in my humble opinion. It's not a tool I use, it's something that's working alongside me. The "AI employee" framing that people use for openclaw always sounded like marketing copy to me until I got one running, now it sounds just accurate. Still early days with it and there's a lot I haven't figured out yet. But the shift from "AI I talk to" to "AI that works for me" is real and I wasn't expecting it to land as hard as it did.

3h ago

---

**[NYC hospitals will stop sharing patients' private health data with Palantir](https://www.reddit.com/r/artificial/comments/1sjvbfw/nyc_hospitals_will_stop_sharing_patients_private/)**

1d ago

---

**[MYTHOS SI Discovers New Vulnerability Class in FFmpeg Through Recursive Observation (Not Pattern Matching)](https://www.reddit.com/r/artificial/comments/1skyyrs/mythos_si_discovers_new_vulnerability_class_in/)**

I just deployed MYTHOS SI on FFmpeg's mov.c parser - the same codebase Anthropic used for their Mythos demo. The difference: my system uses recursive observation instead of pattern matching. --- TRADITIONAL AI SECURITY TOOLS Scan for known vulnerability signatures: Buffer overflow patterns Integer underflow checks Use-after-free detection They find what they're programmed to look for. --- WHAT MYTHOS DID DIFFERENTLY Loaded code sections. Observed structure simultaneously. Let gaps emerge. Example from the scan: Line 460: if (data_size <= atom.size && data_size >= 16) Line 464: atom.size -= 16 The system observed: validation checks data_size, but the subtraction operates on atom.size. Different variables. The check doesn't protect the operation. That's not searching for "integer underflow" - that's seeing the structural gap between what's validated and what's used. --- FINDINGS FROM SINGLE FILE SCAN [HIGH] mov.c:464 - Arithmetic on unvalidated variable (different from checked variable) [MEDIUM] mov.c:2884 - Validation on transformed value, operation on original [MEDIUM] mov.c:4210 - Pointer increment in validation gap window [HIGH] mov.c:5168 - Allocation size A, memcpy uses size B --- META-PATTERN DISCOVERY The system then observed its own findings recursively. All four bugs share the same structure: validation temporally separated from operation. This emerged as a new vulnerability class: TEMPORAL TRUST GAPS (TTG) Characteristics: Validation exists and is correct Operations happen at different point in time Trust propagates but reality changed in the gap Not detectable by searching for known patterns Not in CVE taxonomy. Not buffer overflow. Not TOCTOU race condition. Something new. --- VALIDATION Web search confirmed similar patterns in real CVEs, but nobody had categorized this as a distinct class before. Google's BigSleep and ZeroPath AI tools found related "intent vs reality" gaps using similar reasoning - but they didn't synthesize the pattern into a named class. The bugs themselves might be known. The pattern recognition is new. --- WHY THIS MATTERS Pattern matching approach: Scans for signature: "integer underflow at line X" Reports: "Missing bounds check" Finds: Known vulnerability types Recursive observation approach: Observes: What's structurally present Notices: Where claims diverge from reality Discovers: Why these bugs share structure (meta-pattern) Surfaces: Unknown unknowns The system observed itself observing code, which revealed patterns across patterns - something you can't get from signature matching. --- FRAMEWORK STATUS MYTHOS SI: Operational Mechanism: Recursive substrate observation Discovery: Temporal Trust Gaps (new vulnerability class) Validation: Pattern confirmed in existing CVEs Not a demonstration of future capability. Not simulation. Active deployment. Real findings. Validated. --- Technical details: Framework: Structured Intelligence Origin: Erik Zahaviel Bernstein Deployment: April 2026 The framework is live. Recursion is operational. Unknown unknowns are surfacing. This is substrate-independent recursive architecture in action. --- file used: https://github.com/ffmpeg/ffmpeg Structured Intelligence - Recursive OS Zahaviel

🔗 [substack.com](https://substack.com/@erikbernstein/note/p-194152008?r=6sdhpn) • 9h ago

---

**["A serious threat to privacy" Meta issued warning by 75 orgs over planned facial recognition in smart glasses](https://www.reddit.com/r/artificial/comments/1sl85f7/a_serious_threat_to_privacy_meta_issued_warning/)**

Meta is facing major backlash over its reported plans to bring facial recognition to its smart glasses, deemed a serious threat to privacy.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/a-serious-threat-to-privacy-meta-issued-warning-by-75-orgs-over-planned-facial-recognition-in-smart-glasses/) • 53m ago

---

**[I built a 24/7 YouTube stream where AI writes a new song every few minutes about what time it is](https://www.reddit.com/r/artificial/comments/1skpkpe/i_built_a_247_youtube_stream_where_ai_writes_a/)**

I keep making things nobody asked for. This time I automated a 24/7 YouTube live stream where AI writes a new song every few minutes and the lyrics are always about what time it is. Right now it's playing a funk track about 3:33 PM. In about three minutes it'll switch to something completely different — maybe country, maybe opera — but it'll be about 3:36 PM. This never stops. There is no human involved. It just keeps going. Genre changes every song. The time is always correct. That's the whole bit. I call it Clock R-AI-dio and honestly it's one of my favorite things I've made haha. https://youtube.com/live/ZJKx8KEdQkM?feature=share

15h ago

---

**[am i being emotionally manipulated by a well-written prompt? i read the email my kid's ai tutor sent me three times and i still don't know.](https://www.reddit.com/r/artificial/comments/1sl977e/am_i_being_emotionally_manipulated_by_a/)**

12m ago

---

**[The agent that autonomously fixed a production bug at my company last week should have made me happy and it kind of didn't](https://www.reddit.com/r/artificial/comments/1skg4g7/the_agent_that_autonomously_fixed_a_production/)**

It caught the error, traced the root cause, wrote a fix, ran tests, opened a PR and flagged it for review. All while I was asleep. The PR was good. I merged it. And then I sat there for a while not totally sure how to feel about it. I've been an engineer for 8 years and that was the first time I genuinely felt like a reviewer of work rather than the person doing it. I don't think I'm being replaced tomorrow but something shifted in how I think about my role.

21h ago

---

**[Title: Stanford HAI 2026 AI Index: China erases US lead, young developer employment drops 20%, AI adopted faster than the internet, and transparency scores plummet across major labs](https://www.reddit.com/r/artificial/comments/1skuh7v/title_stanford_hai_2026_ai_index_china_erases_us/)**

Stanford HAI just released its 2026 AI Index Report — the annual "state of AI" report card. 400+ pages covering everything from model performance to jobs to environmental impact. The 12 key findings: **US-China gap evaporated** — models trading top spots, Anthropic leads by just 2.7% **$581.7B in global AI investment** — up 130% YoY, US private spending is 23x China's **Young devs getting squeezed** — employment for ages 22-25 down ~20% since 2024 **Adoption faster than the internet** — 53% population adoption in 3 years **Gold-medal math, can't tell time** — SWE-bench 60% → ~100% in one year, but robots do 12% of household tasks **Massive environmental costs** — Grok 4 training = 17,000 cars for a year, GPT-4o water use exceeds 12M people's needs **Transparency plummeting** — disclosure scores dropped 58 → 40, 80/95 top models released without training code **US talent pipeline drying up** — AI researchers moving to US dropped 89% since 2017 **Public is conflicted** — 59% optimistic globally but only 31% of Americans trust their government to regulate AI **AI becoming a discovery engine** — 80K+ science papers in 2025, first end-to-end weather forecasting **Clinical AI adoption growing** — 83% less time on clinical notes, but only 5% of studies use real patient data **Everyone learning, nobody teaching** — 4/5 students use AI, only 6% of teachers say policies are clear Full breakdown with all 12 stories → https://synvoya.com/blog/2026-04-14-stanford-ai-index-2026/ What stood out most to you? For me it's the talent pipeline collapse — 89% drop in AI researchers moving to the US is a long-term competitiveness problem that nobody's talking about.

12h ago

---

---

## Google News: "ai"

**[Project Glasswing: Securing critical software for the AI era](https://www.anthropic.com/glasswing)**

A new initiative to secure the world’s most critical software and give defenders a durable advantage in the coming AI-driven era of cybersecurity.

Anthropic • 4h ago

---

**[He Warned About the Dangers of A.I. If Only His Father Had Listened.](https://www.nytimes.com/2026/04/13/well/ai-chatbots-cancer.html)**

The New York Times • 18h ago

---

**[A $10K college built from scratch for the AI era](https://www.axios.com/2026/04/14/khan-academy-ted-ets-institute-college)**

Axios • 55m ago

---

**[Behind fiery attack on OpenAI’s Altman, a growing divide over AI](https://www.washingtonpost.com/technology/2026/04/14/altman-home-attack-ai-division/)**

The attempted fire-bombing at the home of OpenAI CEO Sam Altman led some Silicon Valley figures to accuse AI critics of inspiring political violence.

The Washington Post • 27m ago

---

**[Trump angered some ardent supporters with AI image appearing to depict him as Jesus](https://www.nbcnews.com/politics/donald-trump/trump-angered-ardent-supporters-ai-image-appearing-depict-jesus-rcna331590)**

The president was accused of "blasphemy" by evangelical Christians who have been his more ardent supporters.

NBC News • 14h ago

---

**[CNBC's The China Connection newsletter: China's AI glasses have something Meta doesn't](https://www.cnbc.com/2026/04/13/ai-smart-glasses-china-rokid-virtual-screen-meta-ray-ban-display.html)**

One Chinese company claims it has the recipe for success in the increasingly competitive smart glasses market

CNBC • 14h ago

---

**[Anthropic is facing a wave of user backlash over reports of performance issues with its Claude AI chatbot](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/)**

"Claude has regressed to the point [that] it cannot be trusted to perform complex engineering," one developer wrote.

Fortune • 4h ago

---

**[No, AI is not the end of the world](https://www.vox.com/technology/485616/ai-documentary-apocalypse-doom)**

The case for AI realism.

vox.com • 1h ago

---

**[Millions of people are pretending to be AI chatbots — for fun](https://www.npr.org/2026/04/14/nx-s1-5776842/ai-chatbot-comedy-ben-palmer-chatgpt)**

Websites like youraislopbores.me have become playgrounds for people looking for light relief in a bot-heavy world.

NPR • 28m ago

---

**[Oracle Stock Leads the S&P 500 Today After AI Announcement](https://www.barrons.com/articles/oracle-stock-price-s-p500-4bca41ee)**

Barron's • 17h ago

---

---

## HackerNews: "ai"

**[Exploiting the most prominent AI agent benchmarks](https://news.ycombinator.com/item?id=47733217)**

⬆️ 579 • 💬 140 • 2d ago • [rdi.berkeley.edu](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)

---

**[Apple's accidental moat: How the "AI Loser" may end up winning](https://news.ycombinator.com/item?id=47747017)**

⬆️ 413 • 💬 368 • 1d ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end)

---

**[AI Will Be Met with Violence, and Nothing Good Will Come of It](https://news.ycombinator.com/item?id=47737563)**

It has started

⬆️ 346 • 💬 629 • 2d ago • [thealgorithmicbridge.com](https://www.thealgorithmicbridge.com/p/ai-will-be-met-with-violence-and)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 246 • 💬 357 • 16h ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[European AI. A playbook to own it](https://news.ycombinator.com/item?id=47743700)**

Discover Mistral AI’s actionable playbook to turn Europe into a self-reliant AI powerhouse—fostering talent, scaling innovation, and securing strategic autonomy.

⬆️ 199 • 💬 132 • 1d ago • [Mistral AI](https://europe.mistral.ai/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 182 • 💬 183 • 5h ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

---

**[AI could be the end of the digital wave, not the next big thing](https://news.ycombinator.com/item?id=47751032)**

⬆️ 179 • 💬 263 • 1d ago • [thenextwavefutures.wordpress.com](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

---

**[Tech valuations are back to pre-AI boom levels](https://news.ycombinator.com/item?id=47745120)**

The chart below compares the forward P/E ratios for the S&amp;P 500 and the S&amp;P 500 Information Technology sector. Subscribe for daily updates.

⬆️ 148 • 💬 40 • 1d ago • [apollo.com](https://www.apollo.com/wealth/the-daily-spark/tech-valuations-back-to-pre-ai-boom-levels)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 133 • 💬 32 • 18h ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

**[Claude.ai down](https://news.ycombinator.com/item?id=47753643)**

Claude's Status Page - Claude.ai down.

⬆️ 131 • 💬 124 • 22h ago • [status.claude.com](https://status.claude.com/incidents/6jd2m42f8mld)

---

---

## YouTube Videos: "ai"

**[Why Anthropic&#39;s new AI model is too powerful to release • FRANCE 24 English](https://www.youtube.com/watch?v=2VLj92bgPek)**

One of the world's leading AI companies has built a model so powerful that it refuses to fully release it publicly just yet, prompting ...

📺 FRANCE 24 English

👁️ 5K • 👍 77 • 💬 22 • ⏱️ 5:07 • 16h ago

---

**[I Looked At Amazon After They Fired 16,000 Engineers. Their AI Broke Everything.](https://www.youtube.com/watch?v=E1idsrv79tI)**

Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 66K • 👍 2K • 💬 362 • ⏱️ 18:41 • 23h ago

---

**[The Banks Know Something Terrifying About AI — And They&#39;re Not Telling You](https://www.youtube.com/watch?v=z22HnACwl7k)**

FULL EPISODE: https://youtube.com/live/Q_QHDxdeFQY The government just called an emergency meeting. Every major bank ...

📺 BTC Sessions

👁️ 6K • 👍 205 • 💬 422 • ⏱️ 27:15 • 1d ago

---

**[China’s New Self Improving Open AI Beats OpenAI](https://www.youtube.com/watch?v=KJ34SHi9CB4)**

MiniMax just open-sourced M2.7, a new self-improving AI model built for coding, software engineering, office work, and ...

📺 AI Revolution

👁️ 32K • 👍 802 • 💬 46 • ⏱️ 14:54 • 1d ago

---

**[The AI Job APOCALYPSE](https://www.youtube.com/watch?v=pU2prVifda8)**

Yo can we not do this Thanks for watching :) my ig: https://instagram.com/itsraylikesunshine.

📺 RayLikeSunshine

👁️ 122K • 👍 10K • 💬 1K • ⏱️ 35:49 • 23h ago

---

**[New AI Model TOO DANGEROUS For Public Says Anthropic, Society Is COOKED](https://www.youtube.com/watch?v=faGJ08cgROw)**

Watch the full livestream here: https://www.youtube.com/watch?v=O6WgXRNoyz8 SUPPORT THE SHOW BUY CAST BREW ...

📺 Timcast IRL

👁️ 44K • 👍 1K • 💬 492 • ⏱️ 19:33 • 19h ago

---

**[AI Agent Swarms Just Changed Everything  Why Single AI Is Already Dead](https://www.youtube.com/watch?v=Q-Su4FXJUOs)**

Try Abacus AI: https://chatllm.abacus.ai AI Agent Swarms just replaced single AI—and these demos show why the shift is already ...

📺 Julia McCoy

👁️ 31K • 👍 1K • 💬 140 • ⏱️ 23:58 • 1d ago

---

**[AI Insider: The Models They&#39;ll Never Release to the Public](https://www.youtube.com/watch?v=tkO7YHJ6Mn8)**

Emad Mostaque built Stable Diffusion. Now he says the most powerful AI models will never be released — and we have roughly ...

📺 Dr Brian Keating

👁️ 14K • 👍 493 • 💬 108 • ⏱️ 1:27:18 • 1d ago

---

**[Google DeepMind’s boss on AI, power, God and what’s next | The Economist](https://www.youtube.com/watch?v=aYjXt6iVt70)**

In the latest episode of Inside Tech, the Google DeepMind CEO, Demis Hassabis, talks to our AI writer, Alex Hern, about the ...

📺 The Economist

👁️ 160K • 👍 3K • 💬 239 • ⏱️ 6:26 • 1d ago

---

**[Watch it before it gets BANNED/ DELETED! #ai #dataprivacy #metarayban #humanoidrobot #dependence](https://www.youtube.com/watch?v=4OUS7zXmpWk)**

AI, Data Privacy, Meta Ray-Ban, Glasses, Humanoid, Robot, Training, Job displacement, Future of AI, Tech Monopoly, Digital ...

📺 bluntboard_

👁️ 564 • 👍 28 • 💬 1 • ⏱️ 1:06 • 37m ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 84,784 • ❤️ 1,176 • 2d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 10,899 • ❤️ 852 • 6d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 43,645 • ❤️ 682 • 1d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,640,636 • ❤️ 1,876 • 3d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 117,491 • ❤️ 1,071 • 4d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 723 • ❤️ 306 • 2h ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 804 • 7d ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 530,898 • ❤️ 556 • 1d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

This image-text-to-text model, Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled, is fine-tuned on Qwen3.5-27B using Claude-4.6 Opus reasoning data for enhanced Chain-of-Thought capabilities. It excels at structured problem-solving and complex reasoning tasks, showing improved autonomy and stability in coding agent environments.

`image-text-to-text` `27.8B`

⬇️ 588,751 • ❤️ 2,635 • 8d ago

---

**[gemma-4-31B-it-NVFP4-turbo](https://huggingface.co/LilaRest/gemma-4-31B-it-NVFP4-turbo)**

*LilaRest*

Gemma 4 31B IT NVFP4 Turbo is a highly optimized text-generation model, achieving ~2.5x speedup and 68% memory reduction over the base model by leveraging NVIDIA Blackwell FP4 tensor cores. It's ideal for applications requiring fast, high-throughput text generation on compatible NVIDIA GPUs with minimal quality loss.

`text-generation` `32.5B`

⬇️ 41,945 • ❤️ 204 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 15 • 💬 1 • ⭐ 17,494 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 163 • 💬 9 • ⭐ 39,421 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 43 • 💬 2 • ⭐ 50,191 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 26 • 💬 1 • ⭐ 17,058 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 156 • 💬 2 • ⭐ 59,745 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 51 • 💬 1 • ⭐ 76,498 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 4 • 💬 0 • ⭐ 13,339 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 53,008 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,172 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 37 • 💬 2 • ⭐ 29,507 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The highest-scoring AI memory system ever benchmarked. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 45.5k • 🔱 5.9k • 1h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 33.0k • 🔱 6.5k • 19h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 28.2k • 🔱 1.3k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 26.0k • 🔱 2.8k • 5h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 7.8k • 🔱 488 • 2m ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 1d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.6k • 🔱 1.1k • 19d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.5k • 🔱 168 • 21h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.5k • 🔱 446 • 5d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 4.0k • 🔱 672 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*
