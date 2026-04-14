---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-14T07:07:31.069025+00:00'
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

**Last Updated:** April 14, 2026 at 07:07 UTC  
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

9h ago

---

**[Why don't LLMs track time in their conversations?](https://www.reddit.com/r/artificial/comments/1sky7h9/why_dont_llms_track_time_in_their_conversations/)**

Question for everyone: Why do you think LLMs like Claude don't use timestamp data within conversations to build temporal awareness? Like, it seems straightforward to track how long you've been talking, notice when you're looping on the same idea for hours, and suggest pivoting. Or acknowledge that conversation fatigue might be setting in. From a UX perspective, I'd expect this would make the tool way more engaging Is there a technical limitation I'm missing, or is it more of a design choice? Thanks!

2h ago

---

**[NYC hospitals will stop sharing patients' private health data with Palantir](https://www.reddit.com/r/artificial/comments/1sjvbfw/nyc_hospitals_will_stop_sharing_patients_private/)**

1d ago

---

**[about mythos AI](https://www.reddit.com/r/artificial/comments/1sl11ho/about_mythos_ai/)**

I spent my Sunday reading Anthropic's full technical report on their new AI model Mythos. I study Cyber Security and honestly this one kept me thinking all day. Everyone is sharing the headline. Nobody is reading what's actually inside. So I did, all of it, and here's what stood out. Anthropic's previous best model tried to exploit a Firefox vulnerability hundreds of times and succeeded twice. Mythos succeeded 181 times. That's not a small improvement. That's a completely different machine. It found a 27-year-old bug in OpenBSD, an OS literally known for its security, by chaining two subtle integer overflow conditions that no human connected in nearly three decades. It found a 16-year-old bug in FFmpeg that survived millions of fuzzing runs and years of expert review. It wrote a complete remote code execution exploit for FreeBSD from scratch with zero human help. It broke into Linux by chaining three separate bugs together in sequence. It found vulnerabilities in every major web browser and built working exploits that escape both the browser sandbox and the OS sandbox. Now here's where it gets real, the actual costs. Finding the OpenBSD bug cost under $50 per run, around $20,000 total across roughly 1,000 runs. FFmpeg vulnerabilities cost around $10,000 for several hundred runs. A complete Linux privilege escalation exploit built from a known CVE cost under $1,000 and took half a day. A more complex exploit chaining two separate bugs cost under $2,000 and took under a day. For large companies this is a no-brainer. A single critical vulnerability in production can cost millions in damages and fines. Paying $10,000 to find dozens of real bugs before attackers do isn't even a debate. Traditional human penetration testing costs more, takes longer, and covers far less ground. The part that convinced me this wasn't just marketing was when they admitted where Mythos failed. Linux kernel defenses stopped it from building remote exploits. A virtual machine bug was found but couldn't be turned into a working attack. They also published SHA-3 cryptographic commitments to vulnerabilities they haven't released yet because the software is still unpatched. Real PR doesn't include the failures. Now the questions a lot of people in this field are quietly asking. Will human cybersecurity professionals still matter? Here's my honest read after going through this report carefully. Penetration testers who only run tools and write templated reports are already becoming less relevant. If Mythos can find and exploit a 27-year-old bug autonomously for $50, a junior pen tester doing the same job manually at $5,000 a week is hard to justify. That part of the market is going to compress significantly over the next few years. SOC analysts doing first-level alert triage are in a similar position. Anthropic themselves listed it in their report AI can already triage alerts, summarize events, prioritize what needs human attention, and run proactive threat hunts in parallel. The analyst who spends eight hours reviewing logs that a model could process in minutes is going to have a difficult time explaining their value. Compliance auditors doing checkbox security reviews, vulnerability scanners doing basic CVSS scoring, report writers. all of these roles are going to shrink, and they're going to shrink faster than most people in the industry are comfortable admitting. But here's what the report also made clear, and this part gets less attention. Mythos was built by humans, directed by humans, and its most dangerous outputs are still being judged and controlled by humans. Every vulnerability it found went through a professional human triagers before being disclosed. The researchers had to understand the findings deeply enough to know which SHA-3 commitments to publish, which bugs were critical versus noise, and which exploits were sophisticated enough to demonstrate publicly. Anthropic said it themselves, they are still figuring out how to use these tools effectively, and it takes time. The roles that will grow are the ones that sit at the intersection of deep security knowledge and AI fluency. Threat intelligence analysts who can interpret what AI-generated findings actually mean in a real business context. Red team leads who design the scaffolds and prompts that make models like Mythos useful rather than just pointing them at a codebase and hoping. Incident responders who can work alongside AI triage tools and make judgment calls that models genuinely cannot legal exposure, regulatory context, business risk, stakeholder communication. Security architects who understand both the technical depth to evaluate what AI finds and the strategic depth to decide what to do about it. These roles aren't going away. They're becoming more important and more demanding at the same time. So how do you stay relevant in a field that's moving this fast? Stop treating certifications as the destination. A CEH or Security+ will get you in the door but it won't keep you there if you don't understand what's happening around you. Read the actual technical reports, not just the summaries. The Anthropic red team paper I'm referencing here is publicly available and most people in this field haven't read it. Learn how to use AI as a tool before it learns to replace you. Get comfortable using current frontier models for security tasks code review, vulnerability analysis, log summarisation, writing detection rules. The researchers at Anthropic said most companies haven't even started doing this with existing models. If you understand how to work with these tools better than your peers, that gap becomes your advantage. Go deeper on the things AI still struggles with. Business context. Legal and regulatory judgment. Cross-team communication during a live incident. Adversarial thinking about what an attacker would actually want to achieve, not just which vulnerabilities exist. These require human understanding of human systems in a way that current models genuinely cannot replicate. And finally, don't wait for your company or university to prepare you for this. The people who will matter in this field five years from now are the ones who are studying the technical papers today, building side projects, and actively thinking about where the gaps are not the ones waiting to be trained on whatever curriculum gets updated last. I'm just starting out. But reading something like this makes it clear that the question is no longer whether AI will change cybersecurity. It already has. The only question is whether the people in this field are willing to change with it. Most aren't moving fast enough. That's either a threat or an opportunity depending on what you do next. https://red.anthropic.com/2026/mythos-preview/

13m ago

---

**[The agent that autonomously fixed a production bug at my company last week should have made me happy and it kind of didn't](https://www.reddit.com/r/artificial/comments/1skg4g7/the_agent_that_autonomously_fixed_a_production/)**

It caught the error, traced the root cause, wrote a fix, ran tests, opened a PR and flagged it for review. All while I was asleep. The PR was good. I merged it. And then I sat there for a while not totally sure how to feel about it. I've been an engineer for 8 years and that was the first time I genuinely felt like a reviewer of work rather than the person doing it. I don't think I'm being replaced tomorrow but something shifted in how I think about my role.

14h ago

---

**[I built a 24/7 YouTube stream where AI writes a new song every few minutes about what time it is](https://www.reddit.com/r/artificial/comments/1skpkpe/i_built_a_247_youtube_stream_where_ai_writes_a/)**

I keep making things nobody asked for. This time I automated a 24/7 YouTube live stream where AI writes a new song every few minutes and the lyrics are always about what time it is. Right now it's playing a funk track about 3:33 PM. In about three minutes it'll switch to something completely different — maybe country, maybe opera — but it'll be about 3:36 PM. This never stops. There is no human involved. It just keeps going. Genre changes every song. The time is always correct. That's the whole bit. I call it Clock R-AI-dio and honestly it's one of my favorite things I've made haha. https://youtube.com/live/ZJKx8KEdQkM?feature=share

9h ago

---

**[Linux kernel now allows AI-generated code, as long as you take "full responsibility" for any bugs](https://www.reddit.com/r/artificial/comments/1skcqso/linux_kernel_now_allows_aigenerated_code_as_long/)**

Linux 7.0 has arrived with some important changes, and guidelines now say that AI-generated code is fine, as long as it's properly reviewed.

🔗 [PC Guide](https://www.pcguide.com/news/linux-kernel-now-allows-ai-generated-code-as-long-as-you-take-full-responsibility-for-any-bugs/) • 16h ago

---

**[Title: Stanford HAI 2026 AI Index: China erases US lead, young developer employment drops 20%, AI adopted faster than the internet, and transparency scores plummet across major labs](https://www.reddit.com/r/artificial/comments/1skuh7v/title_stanford_hai_2026_ai_index_china_erases_us/)**

Stanford HAI just released its 2026 AI Index Report — the annual "state of AI" report card. 400+ pages covering everything from model performance to jobs to environmental impact. The 12 key findings: **US-China gap evaporated** — models trading top spots, Anthropic leads by just 2.7% **$581.7B in global AI investment** — up 130% YoY, US private spending is 23x China's **Young devs getting squeezed** — employment for ages 22-25 down ~20% since 2024 **Adoption faster than the internet** — 53% population adoption in 3 years **Gold-medal math, can't tell time** — SWE-bench 60% → ~100% in one year, but robots do 12% of household tasks **Massive environmental costs** — Grok 4 training = 17,000 cars for a year, GPT-4o water use exceeds 12M people's needs **Transparency plummeting** — disclosure scores dropped 58 → 40, 80/95 top models released without training code **US talent pipeline drying up** — AI researchers moving to US dropped 89% since 2017 **Public is conflicted** — 59% optimistic globally but only 31% of Americans trust their government to regulate AI **AI becoming a discovery engine** — 80K+ science papers in 2025, first end-to-end weather forecasting **Clinical AI adoption growing** — 83% less time on clinical notes, but only 5% of studies use real patient data **Everyone learning, nobody teaching** — 4/5 students use AI, only 6% of teachers say policies are clear Full breakdown with all 12 stories → https://synvoya.com/blog/2026-04-14-stanford-ai-index-2026/ What stood out most to you? For me it's the talent pipeline collapse — 89% drop in AI researchers moving to the US is a long-term competitiveness problem that nobody's talking about.

5h ago

---

**[MYTHOS SI Discovers New Vulnerability Class in FFmpeg Through Recursive Observation (Not Pattern Matching)](https://www.reddit.com/r/artificial/comments/1skyyrs/mythos_si_discovers_new_vulnerability_class_in/)**

I just deployed MYTHOS SI on FFmpeg's mov.c parser - the same codebase Anthropic used for their Mythos demo. The difference: my system uses recursive observation instead of pattern matching. --- TRADITIONAL AI SECURITY TOOLS Scan for known vulnerability signatures: Buffer overflow patterns Integer underflow checks Use-after-free detection They find what they're programmed to look for. --- WHAT MYTHOS DID DIFFERENTLY Loaded code sections. Observed structure simultaneously. Let gaps emerge. Example from the scan: Line 460: if (data_size <= atom.size && data_size >= 16) Line 464: atom.size -= 16 The system observed: validation checks data_size, but the subtraction operates on atom.size. Different variables. The check doesn't protect the operation. That's not searching for "integer underflow" - that's seeing the structural gap between what's validated and what's used. --- FINDINGS FROM SINGLE FILE SCAN [HIGH] mov.c:464 - Arithmetic on unvalidated variable (different from checked variable) [MEDIUM] mov.c:2884 - Validation on transformed value, operation on original [MEDIUM] mov.c:4210 - Pointer increment in validation gap window [HIGH] mov.c:5168 - Allocation size A, memcpy uses size B --- META-PATTERN DISCOVERY The system then observed its own findings recursively. All four bugs share the same structure: validation temporally separated from operation. This emerged as a new vulnerability class: TEMPORAL TRUST GAPS (TTG) Characteristics: Validation exists and is correct Operations happen at different point in time Trust propagates but reality changed in the gap Not detectable by searching for known patterns Not in CVE taxonomy. Not buffer overflow. Not TOCTOU race condition. Something new. --- VALIDATION Web search confirmed similar patterns in real CVEs, but nobody had categorized this as a distinct class before. Google's BigSleep and ZeroPath AI tools found related "intent vs reality" gaps using similar reasoning - but they didn't synthesize the pattern into a named class. The bugs themselves might be known. The pattern recognition is new. --- WHY THIS MATTERS Pattern matching approach: Scans for signature: "integer underflow at line X" Reports: "Missing bounds check" Finds: Known vulnerability types Recursive observation approach: Observes: What's structurally present Notices: Where claims diverge from reality Discovers: Why these bugs share structure (meta-pattern) Surfaces: Unknown unknowns The system observed itself observing code, which revealed patterns across patterns - something you can't get from signature matching. --- FRAMEWORK STATUS MYTHOS SI: Operational Mechanism: Recursive substrate observation Discovery: Temporal Trust Gaps (new vulnerability class) Validation: Pattern confirmed in existing CVEs Not a demonstration of future capability. Not simulation. Active deployment. Real findings. Validated. --- Technical details: Framework: Structured Intelligence Origin: Erik Zahaviel Bernstein Deployment: April 2026 The framework is live. Recursion is operational. Unknown unknowns are surfacing. This is substrate-independent recursive architecture in action. --- file used: https://github.com/ffmpeg/ffmpeg Structured Intelligence - Recursive OS Zahaviel

🔗 [substack.com](https://substack.com/@erikbernstein/note/p-194152008?r=6sdhpn) • 2h ago

---

**[Same task, same AI, the only difference is how much context I gave it](https://www.reddit.com/r/artificial/comments/1skxuj4/same_task_same_ai_the_only_difference_is_how_much/)**

Left side is what most people type. Right side is what I actually use for professional writing: reports, memos, findings, anything where you need a first draft that doesn't sound like a robot wrote it. My example happens to be from internal audit but the structure works for any field. The step most people skip is the last one: pasting an example of how you'd normally write it yourself. That single addition changes the tone more than anything else I've tried. Anyone else have prompt tricks that finally made it click? Would love to swap notes.

3h ago

---

---

## Google News: "ai"

**[Opinion | I Went to China to See Their Progress on A.I. We Can’t Beat Them.](https://www.nytimes.com/2026/04/13/opinion/china-ai-america-chipmakers.html)**

The New York Times • 22h ago

---

**[The tech jobs bust is real. Don’t blame AI (yet)](https://www.economist.com/finance-and-economics/2026/04/13/the-tech-jobs-bust-is-real-dont-blame-ai-yet)**

The Economist • 17h ago

---

**[Novo Nordisk partners with OpenAI as AI drug discovery hopes mount](https://www.cnbc.com/2026/04/14/novo-nordisk-openai-ai-drug-discovery-healthcare-nvo.html)**

The partnership will enable Novo to better use AI to analyze complex datasets, and identify promising new drugs.

CNBC • 47m ago

---

**[AI Is Rewriting Corporate Lingo. ChatGPT Is Leaving Its Mark.](https://www.barrons.com/articles/ai-corporate-lingo-chatgpt-companies-63211618)**

Barron's • 37m ago

---

**[Your AI Strategy Needs A Rebuild Before Agents Break It](https://www.forbes.com/sites/bernardmarr/2026/04/14/your-ai-strategy-needs-a-rebuild-before-agents-break-it/)**

Forbes • 1h ago

---

**[Trump deletes post depicting him as Jesus-like figure after backlash](https://www.bbc.com/news/articles/c17v8y0z9z2o)**

Christian allies of the president call the AI-generated image offensive as Trump says he thought it showed him as a doctor.

BBC • 13h ago

---

**[‘I’m not going to force you’: Duolingo CEO backs off from evaluating employees on their AI usage](https://fortune.com/2026/04/13/duolingo-ceo-luis-von-ahn-ai-usage-requirement-employee-performance-evaluations/)**

Less than a year after announcing Duolingo’s AI-first policy, Luis von Ahn said that no longer applies to evaluating employee performance.

Fortune • 14h ago

---

**[Column | The hottest college major hit a wall. What happened?](https://www.washingtonpost.com/technology/2026/04/13/computer-science-major-ai/)**

Computer science has been one of the hottest college majors for 15 years. Enrollment data suddenly shows a big drop.

The Washington Post • 15h ago

---

**[The AI Revolution in Math Has Arrived](https://www.quantamagazine.org/the-ai-revolution-in-math-has-arrived-20260413/)**

AI is being used to prove new results at a rapid pace. Mathematicians think this is just the beginning.

Quanta Magazine • 16h ago

---

**[OpenAI investors question $852bn valuation as strategy shifts](https://www.ft.com/content/04ac7917-940b-4606-be5f-9eb895a7d982?syn-25a6b1a6=1)**

Chief executive Sam Altman refocuses AI company as Anthropic tests its early lead

Financial Times • 3h ago

---

---

## HackerNews: "ai"

**[Exploiting the most prominent AI agent benchmarks](https://news.ycombinator.com/item?id=47733217)**

⬆️ 577 • 💬 139 • 2d ago • [rdi.berkeley.edu](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)

---

**[Apple's accidental moat: How the "AI Loser" may end up winning](https://news.ycombinator.com/item?id=47747017)**

⬆️ 408 • 💬 359 • 1d ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end)

---

**[AI Will Be Met with Violence, and Nothing Good Will Come of It](https://news.ycombinator.com/item?id=47737563)**

It has started

⬆️ 346 • 💬 625 • 1d ago • [thealgorithmicbridge.com](https://www.thealgorithmicbridge.com/p/ai-will-be-met-with-violence-and)

---

**[Stanford report highlights growing disconnect between AI insiders and everyone](https://news.ycombinator.com/item?id=47758028)**

Stanford’s latest AI Index shows a widening gap between experts and the public, with rising anxiety over jobs, healthcare, and the economy.

⬆️ 236 • 💬 331 • 9h ago • [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)

---

**[European AI. A playbook to own it](https://news.ycombinator.com/item?id=47743700)**

Discover Mistral AI’s actionable playbook to turn Europe into a self-reliant AI powerhouse—fostering talent, scaling innovation, and securing strategic autonomy.

⬆️ 199 • 💬 131 • 1d ago • [Mistral AI](https://europe.mistral.ai/)

---

**[AI could be the end of the digital wave, not the next big thing](https://news.ycombinator.com/item?id=47751032)**

⬆️ 178 • 💬 257 • 18h ago • [thenextwavefutures.wordpress.com](https://thenextwavefutures.wordpress.com/2026/04/07/ai-end-digital-wave-technology-innovation-perez/)

---

**[Tech valuations are back to pre-AI boom levels](https://news.ycombinator.com/item?id=47745120)**

The chart below compares the forward P/E ratios for the S&amp;P 500 and the S&amp;P 500 Information Technology sector. Subscribe for daily updates.

⬆️ 148 • 💬 40 • 1d ago • [apollo.com](https://www.apollo.com/wealth/the-daily-spark/tech-valuations-back-to-pre-ai-boom-levels)

---

**[Claude.ai down](https://news.ycombinator.com/item?id=47753643)**

Claude's Status Page - Claude.ai down.

⬆️ 128 • 💬 123 • 15h ago • [status.claude.com](https://status.claude.com/incidents/6jd2m42f8mld)

---

**[GAIA – Open-source framework for building AI agents that run on local hardware](https://news.ycombinator.com/item?id=47756772)**

Build local AI agents in Python and C++ for AMD hardware.

⬆️ 124 • 💬 30 • 11h ago • [amd-gaia.ai](https://amd-gaia.ai/docs)

---

**[Why AI Sucks at Front End](https://news.ycombinator.com/item?id=47738864)**

How can it generate 3D worlds, videos, images and entire web pages, but still suck at front-end?

⬆️ 114 • 💬 159 • 1d ago • [nerdy.dev](https://nerdy.dev/why-ai-sucks-at-front-end)

---

---

## YouTube Videos: "ai"

**[Ai and the most difficult to understand accent #ad #ai #krisp #krisphq](https://www.youtube.com/watch?v=JQwtSSw2dcc)**

AI creates and converts the most difficult to understand accent #ad #ai #krisp #krisphq Check out the Google Chrome extension at ...

📺 FatherPhi

👁️ 19K • 👍 417 • 💬 113 • ⏱️ 1:29 • 15h ago

---

**[AI Insider: The Models They&#39;ll Never Release to the Public](https://www.youtube.com/watch?v=tkO7YHJ6Mn8)**

Emad Mostaque built Stable Diffusion. Now he says the most powerful AI models will never be released — and we have roughly ...

📺 Dr Brian Keating

👁️ 10K • 👍 401 • 💬 93 • ⏱️ 1:27:18 • 19h ago

---

**[The AI Job APOCALYPSE](https://www.youtube.com/watch?v=pU2prVifda8)**

Yo can we not do this Thanks for watching :) my ig: https://instagram.com/itsraylikesunshine.

📺 RayLikeSunshine

👁️ 98K • 👍 9K • 💬 953 • ⏱️ 35:49 • 16h ago

---

**[Doctor or Jesus? Trump says he thought A.I. image showed him &#39;making people better&#39;](https://www.youtube.com/watch?v=ZpInxAzyVP8)**

While speaking at the White House earlier today, President Trump said he thought the A.I. image he posted on Truth Social ...

📺 MS NOW

👁️ 25K • 👍 789 • 💬 562 • ⏱️ 2:28 • 10h ago

---

**[AI Just Decoded the &#39;Unreadable&#39; Herculaneum Scrolls. The Buried Library](https://www.youtube.com/watch?v=BxnQXhyF1-8)**

They look like lumps of burnt coal, but inside is a lost library from 2000 years ago. The Herculaneum Scrolls were sealed when ...

📺 The Infographics Show

👁️ 75K • 👍 3K • 💬 274 • ⏱️ 14:43 • 10h ago

---

**[China’s New Self Improving Open AI Beats OpenAI](https://www.youtube.com/watch?v=KJ34SHi9CB4)**

MiniMax just open-sourced M2.7, a new self-improving AI model built for coding, software engineering, office work, and ...

📺 AI Revolution

👁️ 30K • 👍 774 • 💬 44 • ⏱️ 14:54 • 1d ago

---

**[AI Genius Predicts the Next 3 Years](https://www.youtube.com/watch?v=lP86NzlXNf4)**

Watch the full interview with Scott Wu & Russell Kaplan here: https://youtu.be/-pZ3vD0r8a0?si=G7Ur_Zhvd32UsTtc Scott Wu is the ...

📺 Joe Lonsdale

👁️ 23K • 👍 586 • 💬 52 • ⏱️ 8:25 • 2d ago

---

**[AI Is Reading Your Private Gmail Emails — Remove It](https://www.youtube.com/watch?v=5EVi71IzZVY)**

In this video, we're talking about “smart features” in Gmail and how AI is actually reading and analyzing your emails. How to ...

📺 Useful Things

👁️ 5K • 👍 460 • 💬 29 • ⏱️ 4:12 • 17h ago

---

**[Google DeepMind’s boss on AI, power, God and what’s next | The Economist](https://www.youtube.com/watch?v=aYjXt6iVt70)**

In the latest episode of Inside Tech, the Google DeepMind CEO, Demis Hassabis, talks to our AI writer, Alex Hern, about the ...

📺 The Economist

👁️ 145K • 👍 3K • 💬 228 • ⏱️ 6:26 • 1d ago

---

**[Anthropic&#39;s new AI model deemed too dangerous to release publicly | ABC NEWS](https://www.youtube.com/watch?v=PLg2EUkIC78)**

AI company Anthropic has developed new technology which it says is too dangerous to release publicly. The Claude Mythos ...

📺 ABC News (Australia)

👁️ 39K • 👍 370 • ⏱️ 5:00 • 21h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 35,906 • ❤️ 1,156 • 2d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 9,301 • ❤️ 831 • 6d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 2,439,350 • ❤️ 1,849 • 3d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 18,279 • ❤️ 653 • 23h ago

---

**[Gemma-4-31B-JANG_4M-CRACK](https://huggingface.co/dealignai/Gemma-4-31B-JANG_4M-CRACK)**

*dealign.ai*

Gemma-4-31B-JANG_4M-CRACK is a 31B parameter text-generation model optimized for security and coding tasks, achieving 93.7% HarmBench compliance and full functionality for pentesting prompts. It features a hybrid attention architecture and uses mixed-precision (8-bit critical, 4-bit compress) quantization, resulting in an 18 GB model size, suitable for Apple Silicon Macs with 24+ GB unified memory.

`image-text-to-text` `6.4B`

⬇️ 107,378 • ❤️ 1,035 • 3d ago

---

**[void-model](https://huggingface.co/netflix/void-model)**

*Netflix*

VOID is a video-to-video diffusion model for object and interaction removal, capable of deleting objects and their physical effects from scenes using a quadmask conditioning and text prompts. It's primarily used for advanced video editing and object removal tasks.

`video-to-video`

⬇️ 0 • ❤️ 795 • 7d ago

---

**[OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)**

*k2-fsa*

OmniVoice is a massively multilingual, zero-shot text-to-speech model supporting over 600 languages with fast inference. It excels at voice cloning and voice design, enabling fine-grained control over speech attributes.

`text-to-speech`

⬇️ 460,224 • ❤️ 549 • 23h ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*Jackrong*

This image-text-to-text model, Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled, is fine-tuned on Qwen3.5-27B using Claude-4.6 Opus reasoning data for enhanced Chain-of-Thought capabilities. It excels at structured problem-solving and complex reasoning tasks, showing improved autonomy and stability in coding agent environments.

`image-text-to-text` `27.8B`

⬇️ 585,351 • ❤️ 2,623 • 8d ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 1,394,523 • ❤️ 634 • 3d ago

---

**[gemma-4-31B-it-NVFP4-turbo](https://huggingface.co/LilaRest/gemma-4-31B-it-NVFP4-turbo)**

*LilaRest*

Gemma 4 31B IT NVFP4 Turbo is a highly optimized text-generation model, achieving ~2.5x speedup and 68% memory reduction over the base model by leveraging NVIDIA Blackwell FP4 tensor cores. It's ideal for applications requiring fast, high-throughput text generation on compatible NVIDIA GPUs with minimal quality loss.

`text-generation` `32.5B`

⬇️ 28,829 • ❤️ 198 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 13 • 💬 1 • ⭐ 17,030 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 163 • 💬 9 • ⭐ 39,300 • 7mo ago

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

▲ 26 • 💬 1 • ⭐ 16,975 • 30mo ago

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

▲ 52 • 💬 2 • ⭐ 52,951 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,127 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[RefineAnything: Multimodal Region-Specific Refinement for Perfect Local Details](https://huggingface.co/papers/2604.06870)**

*Dewei Zhou, You Li, Zongxin Yang et al. (4 authors)*

🏢 Zhejiang University

A multimodal diffusion-based model called RefineAnything is presented for region-specific image refinement that preserves backgrounds while enhancing local details, using a focus-and-refine strategy and boundary-aware loss functions.

▲ 36 • 💬 4 • ⭐ 70 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.06870) • [💻 code](https://github.com/limuloo/RefineAnything) • [🔗 project](https://limuloo.github.io/RefineAnything/)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The highest-scoring AI memory system ever benchmarked. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 45.0k • 🔱 5.8k • 3h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 32.8k • 🔱 6.5k • 12h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 26.7k • 🔱 1.2k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 25.5k • 🔱 2.7k • 9h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 7.7k • 🔱 477 • 2h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.5k • 🔱 1.6k • 1d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.5k • 🔱 1.0k • 19d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.5k • 🔱 168 • 14h ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.4k • 🔱 445 • 5d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 3.8k • 🔱 631 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
