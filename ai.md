---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-14T11:57:41.733274+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 14, 2026 at 11:57 UTC  
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

14h ago

---

**[Why don't LLMs track time in their conversations?](https://www.reddit.com/r/artificial/comments/1sky7h9/why_dont_llms_track_time_in_their_conversations/)**

Question for everyone: Why do you think LLMs like Claude don't use timestamp data within conversations to build temporal awareness? Like, it seems straightforward to track how long you've been talking, notice when you're looping on the same idea for hours, and suggest pivoting. Or acknowledge that conversation fatigue might be setting in. From a UX perspective, I'd expect this would make the tool way more engaging Is there a technical limitation I'm missing, or is it more of a design choice? Thanks!

7h ago

---

**[NYC hospitals will stop sharing patients' private health data with Palantir](https://www.reddit.com/r/artificial/comments/1sjvbfw/nyc_hospitals_will_stop_sharing_patients_private/)**

1d ago

---

**[I built a 24/7 YouTube stream where AI writes a new song every few minutes about what time it is](https://www.reddit.com/r/artificial/comments/1skpkpe/i_built_a_247_youtube_stream_where_ai_writes_a/)**

I keep making things nobody asked for. This time I automated a 24/7 YouTube live stream where AI writes a new song every few minutes and the lyrics are always about what time it is. Right now it's playing a funk track about 3:33 PM. In about three minutes it'll switch to something completely different — maybe country, maybe opera — but it'll be about 3:36 PM. This never stops. There is no human involved. It just keeps going. Genre changes every song. The time is always correct. That's the whole bit. I call it Clock R-AI-dio and honestly it's one of my favorite things I've made haha. https://youtube.com/live/ZJKx8KEdQkM?feature=share

13h ago

---

**[MYTHOS SI Discovers New Vulnerability Class in FFmpeg Through Recursive Observation (Not Pattern Matching)](https://www.reddit.com/r/artificial/comments/1skyyrs/mythos_si_discovers_new_vulnerability_class_in/)**

I just deployed MYTHOS SI on FFmpeg's mov.c parser - the same codebase Anthropic used for their Mythos demo. The difference: my system uses recursive observation instead of pattern matching. --- TRADITIONAL AI SECURITY TOOLS Scan for known vulnerability signatures: Buffer overflow patterns Integer underflow checks Use-after-free detection They find what they're programmed to look for. --- WHAT MYTHOS DID DIFFERENTLY Loaded code sections. Observed structure simultaneously. Let gaps emerge. Example from the scan: Line 460: if (data_size <= atom.size && data_size >= 16) Line 464: atom.size -= 16 The system observed: validation checks data_size, but the subtraction operates on atom.size. Different variables. The check doesn't protect the operation. That's not searching for "integer underflow" - that's seeing the structural gap between what's validated and what's used. --- FINDINGS FROM SINGLE FILE SCAN [HIGH] mov.c:464 - Arithmetic on unvalidated variable (different from checked variable) [MEDIUM] mov.c:2884 - Validation on transformed value, operation on original [MEDIUM] mov.c:4210 - Pointer increment in validation gap window [HIGH] mov.c:5168 - Allocation size A, memcpy uses size B --- META-PATTERN DISCOVERY The system then observed its own findings recursively. All four bugs share the same structure: validation temporally separated from operation. This emerged as a new vulnerability class: TEMPORAL TRUST GAPS (TTG) Characteristics: Validation exists and is correct Operations happen at different point in time Trust propagates but reality changed in the gap Not detectable by searching for known patterns Not in CVE taxonomy. Not buffer overflow. Not TOCTOU race condition. Something new. --- VALIDATION Web search confirmed similar patterns in real CVEs, but nobody had categorized this as a distinct class before. Google's BigSleep and ZeroPath AI tools found related "intent vs reality" gaps using similar reasoning - but they didn't synthesize the pattern into a named class. The bugs themselves might be known. The pattern recognition is new. --- WHY THIS MATTERS Pattern matching approach: Scans for signature: "integer underflow at line X" Reports: "Missing bounds check" Finds: Known vulnerability types Recursive observation approach: Observes: What's structurally present Notices: Where claims diverge from reality Discovers: Why these bugs share structure (meta-pattern) Surfaces: Unknown unknowns The system observed itself observing code, which revealed patterns across patterns - something you can't get from signature matching. --- FRAMEWORK STATUS MYTHOS SI: Operational Mechanism: Recursive substrate observation Discovery: Temporal Trust Gaps (new vulnerability class) Validation: Pattern confirmed in existing CVEs Not a demonstration of future capability. Not simulation. Active deployment. Real findings. Validated. --- Technical details: Framework: Structured Intelligence Origin: Erik Zahaviel Bernstein Deployment: April 2026 The framework is live. Recursion is operational. Unknown unknowns are surfacing. This is substrate-independent recursive architecture in action. --- file used: https://github.com/ffmpeg/ffmpeg Structured Intelligence - Recursive OS Zahaviel

🔗 [substack.com](https://substack.com/@erikbernstein/note/p-194152008?r=6sdhpn) • 6h ago

---

**[How do Guard Rails work from a programmer point of view?](https://www.reddit.com/r/artificial/comments/1sl56q5/how_do_guard_rails_work_from_a_programmer_point/)**

I understand what Guard rails do. I want to know how I code them. The explanations I have read are all quite high level and treat Guard Rails as something of a black box. What do I need to know to try developing some example Guard Rails?

1h ago

---

**[openclaw ai agent vs just using chatgpt](https://www.reddit.com/r/artificial/comments/1sl564k/openclaw_ai_agent_vs_just_using_chatgpt/)**

I've been using AI tools pretty heavily for the past couple of years. ChatGPT, Claude, Perplexity, a few others. I thought I had a good mental model of what these things could and couldn't do. Then I set up an openclaw agent and realized I had been thinking about it completely wrong. The difference isn't capability. Claude is more capable than my openclaw agent in a lot of way, the difference is orientation. Every AI tool I've used before openclaw was something I went to. I opened a tab, typed something, got a response, closed the tab, so the interaction was entirely initiated by me and ended when I stopped typing. Openclaw runs the other direction. It's sitting there whether I'm at my computer or not. It messaged me yesterday while I was in a meeting to flag an email that needed a same day response. I didn't ask it to do that, I just told it once, weeks ago, that time sensitive client emails matter and it should interrupt me and it remembered and acted on it. That sounds like a small thing but it fundamentally changes the relationship in my humble opinion. It's not a tool I use, it's something that's working alongside me. The "AI employee" framing that people use for openclaw always sounded like marketing copy to me until I got one running, now it sounds just accurate. Still early days with it and there's a lot I haven't figured out yet. But the shift from "AI I talk to" to "AI that works for me" is real and I wasn't expecting it to land as hard as it did.

1h ago

---

**[The agent that autonomously fixed a production bug at my company last week should have made me happy and it kind of didn't](https://www.reddit.com/r/artificial/comments/1skg4g7/the_agent_that_autonomously_fixed_a_production/)**

It caught the error, traced the root cause, wrote a fix, ran tests, opened a PR and flagged it for review. All while I was asleep. The PR was good. I merged it. And then I sat there for a while not totally sure how to feel about it. I've been an engineer for 8 years and that was the first time I genuinely felt like a reviewer of work rather than the person doing it. I don't think I'm being replaced tomorrow but something shifted in how I think about my role.

19h ago

---

**[Linux kernel now allows AI-generated code, as long as you take "full responsibility" for any bugs](https://www.reddit.com/r/artificial/comments/1skcqso/linux_kernel_now_allows_aigenerated_code_as_long/)**

Linux 7.0 has arrived with some important changes, and guidelines now say that AI-generated code is fine, as long as it's properly reviewed.

🔗 [PC Guide](https://www.pcguide.com/news/linux-kernel-now-allows-ai-generated-code-as-long-as-you-take-full-responsibility-for-any-bugs/) • 21h ago

---

**[Title: Stanford HAI 2026 AI Index: China erases US lead, young developer employment drops 20%, AI adopted faster than the internet, and transparency scores plummet across major labs](https://www.reddit.com/r/artificial/comments/1skuh7v/title_stanford_hai_2026_ai_index_china_erases_us/)**

Stanford HAI just released its 2026 AI Index Report — the annual "state of AI" report card. 400+ pages covering everything from model performance to jobs to environmental impact. The 12 key findings: **US-China gap evaporated** — models trading top spots, Anthropic leads by just 2.7% **$581.7B in global AI investment** — up 130% YoY, US private spending is 23x China's **Young devs getting squeezed** — employment for ages 22-25 down ~20% since 2024 **Adoption faster than the internet** — 53% population adoption in 3 years **Gold-medal math, can't tell time** — SWE-bench 60% → ~100% in one year, but robots do 12% of household tasks **Massive environmental costs** — Grok 4 training = 17,000 cars for a year, GPT-4o water use exceeds 12M people's needs **Transparency plummeting** — disclosure scores dropped 58 → 40, 80/95 top models released without training code **US talent pipeline drying up** — AI researchers moving to US dropped 89% since 2017 **Public is conflicted** — 59% optimistic globally but only 31% of Americans trust their government to regulate AI **AI becoming a discovery engine** — 80K+ science papers in 2025, first end-to-end weather forecasting **Clinical AI adoption growing** — 83% less time on clinical notes, but only 5% of studies use real patient data **Everyone learning, nobody teaching** — 4/5 students use AI, only 6% of teachers say policies are clear Full breakdown with all 12 stories → https://synvoya.com/blog/2026-04-14-stanford-ai-index-2026/ What stood out most to you? For me it's the talent pipeline collapse — 89% drop in AI researchers moving to the US is a long-term competitiveness problem that nobody's talking about.

10h ago

---

---

## Google News: "ai"

**[Suspect in attack at Sam Altman's house aimed to kill OpenAI CEO, warned of humanity's extinction from AI](https://www.cnbc.com/2026/04/13/sam-altman-openai-ai-arson.html)**

San Francisco Police Department officers recovered a document from the suspect that detailed his intentions, according to a filing.

CNBC • 12h ago

---

**[The tech jobs bust is real. Don’t blame AI (yet)](https://www.economist.com/finance-and-economics/2026/04/13/the-tech-jobs-bust-is-real-dont-blame-ai-yet)**

The Economist • 22h ago

---

**[Iran slams YouTube ban on pro-Iranian group’s Lego-style AI videos](https://www.aljazeera.com/news/2026/4/14/iran-slams-youtube-ban-on-pro-iranian-groups-lego-style-ai-videos)**

Iran's Foreign Ministry spokesman says the move aims to 'suppress the truth about their illegal war on Iran'.

Al Jazeera • 1h ago

---

**[Google, DressX And The New Fashion AI Virtual Try-On Stack](https://www.forbes.com/sites/moinroberts-islam/2026/04/14/google-dressx-and-the-new-fashion-ai-virtual-try-on-stack/)**

Forbes • 27m ago

---

**[Agency in the Age of AI](https://time.com/article/2026/04/14/agency-in-the-age-of-ai/)**

"People are wrestling with questions about what AI will mean for their jobs, education, and personal well-being," writes John Palfrey.

Time Magazine • 57m ago

---

**[I Feel So Sorry for My A.I. Sunglasses](https://www.nytimes.com/2026/04/14/magazine/ai-sunglasses-meta-zuckerberg.html)**

The New York Times • 2h ago

---

**[Trump deletes post depicting him as Jesus-like figure after backlash](https://www.bbc.com/news/articles/c17v8y0z9z2o)**

Christian allies of the president call the AI-generated image offensive as Trump says he thought it showed him as a doctor.

BBC • 18h ago

---

**[Exclusive: Inside Google's AI jobs push](https://www.axios.com/2026/04/14/google-launches-ai-jobs-push)**

Axios • 2h ago

---

**[Fiery San Francisco attack spurs fear that a new issue is dividing Americans](https://www.washingtonpost.com/technology/2026/04/14/altman-home-attack-ai-division/)**

The attempted fire-bombing at the home of OpenAI CEO Sam Altman led some Silicon Valley figures to accuse AI critics of inspiring political violence.

The Washington Post • 1h ago

---

**[The AI Revolution in Math Has Arrived](https://www.quantamagazine.org/the-ai-revolution-in-math-has-arrived-20260413/)**

AI is being used to prove new results at a rapid pace. Mathematicians think this is just the beginning.

Quanta Magazine • 20h ago

---

---

## HackerNews: "ai"

**[Exploiting the most prominent AI agent benchmarks](https://news.ycombinator.com/item?id=47733217)**

⬆️ 579 • 💬 140 • 2d ago • [rdi.berkeley.edu](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)

---

**[Apple's accidental moat: How the "AI Loser" may end up winning](https://news.ycombinator.com/item?id=47747017)**

⬆️ 410 • 💬 363 • 1d ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end)

---

**[AI Will Be Met with Violence, and Nothing Good Will Come of It](https://news.ycombinator.com/item?id=47737563)**

It has started

⬆️ 346 • 💬 628 • 2d ago • [thealgorithmicbridge.com](https://www.thealgorithmicbridge.com/p/ai-will-be-met-with-violence-and)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 243 • 💬 352 • 14h ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[European AI. A playbook to own it](https://news.ycombinator.com/item?id=47743700)**

Discover Mistral AI’s actionable playbook to turn Europe into a self-reliant AI powerhouse—fostering talent, scaling innovation, and securing strategic autonomy.

⬆️ 199 • 💬 132 • 1d ago • [Mistral AI](https://europe.mistral.ai/)

---

**[AI could be the end of the digital wave, not the next big thing](https://news.ycombinator.com/item?id=47751032)**

⬆️ 179 • 💬 262 • 23h ago • [thenextwavefutures.wordpress.com](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

---

**[An AI Vibe Coding Horror Story](https://news.ycombinator.com/item?id=47762901)**

A medical professional built a patient management app using AI, exposed all patient data unprotected to the internet, and sent voice recordings to AI services without consent. Likely violating Swiss nDSG and other laws.

⬆️ 166 • 💬 167 • 3h ago • [Tobias Brunner aka tobru](https://www.tobru.ch/an-ai-vibe-coding-horror-story/)

---

**[Tech valuations are back to pre-AI boom levels](https://news.ycombinator.com/item?id=47745120)**

The chart below compares the forward P/E ratios for the S&amp;P 500 and the S&amp;P 500 Information Technology sector. Subscribe for daily updates.

⬆️ 148 • 💬 40 • 1d ago • [apollo.com](https://www.apollo.com/wealth/the-daily-spark/tech-valuations-back-to-pre-ai-boom-levels)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 132 • 💬 30 • 16h ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

**[Claude.ai down](https://news.ycombinator.com/item?id=47753643)**

Claude's Status Page - Claude.ai down.

⬆️ 130 • 💬 124 • 20h ago • [status.claude.com](https://status.claude.com/incidents/6jd2m42f8mld)

---

---

## YouTube Videos: "ai"

**[Why Anthropic&#39;s new AI model is too powerful to release • FRANCE 24 English](https://www.youtube.com/watch?v=2VLj92bgPek)**

One of the world's leading AI companies has built a model so powerful that it refuses to fully release it publicly just yet, prompting ...

📺 FRANCE 24 English

👁️ 5K • 👍 75 • 💬 18 • ⏱️ 5:07 • 14h ago

---

**[The Banks Know Something Terrifying About AI — And They&#39;re Not Telling You](https://www.youtube.com/watch?v=z22HnACwl7k)**

FULL EPISODE: https://youtube.com/live/Q_QHDxdeFQY The government just called an emergency meeting. Every major bank ...

📺 BTC Sessions

👁️ 6K • 👍 205 • 💬 451 • ⏱️ 27:15 • 23h ago

---

**[AI Just Decoded the &#39;Unreadable&#39; Herculaneum Scrolls. The Buried Library](https://www.youtube.com/watch?v=BxnQXhyF1-8)**

They look like lumps of burnt coal, but inside is a lost library from 2000 years ago. The Herculaneum Scrolls were sealed when ...

📺 The Infographics Show

👁️ 111K • 👍 3K • 💬 334 • ⏱️ 14:43 • 15h ago

---

**[China’s New Self Improving Open AI Beats OpenAI](https://www.youtube.com/watch?v=KJ34SHi9CB4)**

MiniMax just open-sourced M2.7, a new self-improving AI model built for coding, software engineering, office work, and ...

📺 AI Revolution

👁️ 32K • 👍 797 • 💬 46 • ⏱️ 14:54 • 1d ago

---

**[I Looked At Amazon After They Fired 16,000 Engineers. Their AI Broke Everything.](https://www.youtube.com/watch?v=E1idsrv79tI)**

Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 63K • 👍 2K • 💬 340 • ⏱️ 18:41 • 21h ago

---

**[The AI Job APOCALYPSE](https://www.youtube.com/watch?v=pU2prVifda8)**

Yo can we not do this Thanks for watching :) my ig: https://instagram.com/itsraylikesunshine.

📺 RayLikeSunshine

👁️ 117K • 👍 10K • 💬 1K • ⏱️ 35:49 • 21h ago

---

**[AI Agent Swarms Just Changed Everything  Why Single AI Is Already Dead](https://www.youtube.com/watch?v=Q-Su4FXJUOs)**

Try Abacus AI: https://chatllm.abacus.ai AI Agent Swarms just replaced single AI—and these demos show why the shift is already ...

📺 Julia McCoy

👁️ 31K • 👍 1K • 💬 140 • ⏱️ 23:58 • 1d ago

---

**[AI Genius Predicts the Next 3 Years](https://www.youtube.com/watch?v=lP86NzlXNf4)**

Watch the full interview with Scott Wu & Russell Kaplan here: https://youtu.be/-pZ3vD0r8a0?si=G7Ur_Zhvd32UsTtc Scott Wu is the ...

📺 Joe Lonsdale

👁️ 24K • 👍 596 • 💬 53 • ⏱️ 8:25 • 2d ago

---

**[Trump Shares Ai-Generated Image Of Himself As Jesus | The View](https://www.youtube.com/watch?v=uGAMi47yig4)**

After the Pope spoke out against the war in Iran and Pres. Trump wasn't pleased with his comments, 'The View' co-hosts react to ...

📺 The View

👁️ 172K • 👍 4K • 💬 1K • ⏱️ 6:57 • 17h ago

---

**[Trump’s Blasphemous Jesus AI Image SHOCKS World!](https://www.youtube.com/watch?v=DiakslX9B04)**

Donald Trump just dropped a jaw-dropping AI image of himself as Jesus Christ — and the internet is losing it. In this video we ...

📺 Maximilien Robespierre

👁️ 33K • 👍 3K • 💬 1K • ⏱️ 8:34 • 22h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 84,784 • ❤️ 1,175 • 2d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 10,899 • ❤️ 849 • 6d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 43,645 • ❤️ 677 • 1d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,640,636 • ❤️ 1,873 • 3d ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 117,491 • ❤️ 1,063 • 4d ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 802 • 7d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 723 • ❤️ 261 • 39m ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 530,898 • ❤️ 555 • 1d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

This image-text-to-text model, Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled, is fine-tuned on Qwen3.5-27B using Claude-4.6 Opus reasoning data for enhanced Chain-of-Thought capabilities. It excels at structured problem-solving and complex reasoning tasks, showing improved autonomy and stability in coding agent environments.

`image-text-to-text` `27.8B`

⬇️ 588,751 • ❤️ 2,634 • 8d ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 1,503,266 • ❤️ 642 • 3d ago

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

▲ 52 • 💬 2 • ⭐ 52,951 • 11mo ago

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

⭐ 45.4k • 🔱 5.9k • 8h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 32.9k • 🔱 6.5k • 17h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 27.8k • 🔱 1.3k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 25.9k • 🔱 2.8k • 3h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 7.8k • 🔱 487 • 14m ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 1d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.5k • 🔱 1.1k • 19d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.5k • 🔱 168 • 19h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.5k • 🔱 446 • 5d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 4.0k • 🔱 669 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
