---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-01T19:18:13.213174+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 01, 2026 at 19:18 UTC  
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

**[I have created a Chrome extension that fact checks YouTube videos as you watch](https://www.reddit.com/r/artificial/comments/1uk7t49/i_have_created_a_chrome_extension_that_fact/)**

Hi, I have been working on this for many months now and I'd really be happy for people to try it out. It is a Chrome extension called "PopUpFactCheck". It is an AI powered video fact checker. With it, you fact check any YouTube video that has captions. And you can use it, for free! You turn captions on, and sit back and watch the video as bubbles appear on the right-hand side of the video with fact checks, information, background, and other context. Great for watching politicians, news, history, and just about any content on YouTube. Claude Code was a major tool in my development, and the AI that is used is GPT 5.5. In addition, there is an extensive waterfall of sources including the TheNewsAPI, various government and public health and other APIs, social, and web search powered by DDGS and Serper. It's free, and you don't have to bring your own API keys or anything. You simply install and use. I will be looking forward to your feedback. PopUpFact Check - Chrome Web Store PopUpFactCheck - Homepage

17h ago

---

**[Claude Code catastrophe: Entire project recursively deleted while prompting in Chinese (full video + logs)](https://www.reddit.com/r/artificial/comments/1ukq4br/claude_code_catastrophe_entire_project/)**

Cross-posting from r/claude for more visibility. Claude Code recursively wiped the contents of my local Electron project root. This happened in a Windows terminal while working on a project named Orpheus. My prompt did not ask it to delete, wipe, clean, reset, or remove the project. The prompt was in Traditional Chinese: “之前我要安裝檔，但是其實我只需要 dictate.” It was roughly about not needing the installer anymore and only needing the dictate function. The preserved terminal transcript later showed Claude moving from a failed root deletion attempt to deleting the child items inside the project root. The destructive sequence included: Get-ChildItem -LiteralPath $p -Force -ErrorAction SilentlyContinue | ForEach-Object { try { Remove-Item -LiteralPath $_.FullName -Recurse -Force -ErrorAction Stop "OK $($_.Name)" } catch { "ERR $($_.Name): $($_.Exception.Message)" } } $p was the Orpheus project root. The output then showed items being removed, including: .claude dist node_modules src claude-elevenlabs-voice-v2.user.js dictation.html main.js ORPHEUS_HANDOFF.md package-lock.json package.json preload.js Local artifacts I found for Orpheus showed default / acceptEdits. I did not find Orpheus bypassPermissions. I did not find Orpheus --dangerously-skip-permissions. I’m not claiming Anthropic acted maliciously. I’m not claiming prompt injection or anti-distillation without evidence. Moral of the story: Treat frontier AI agents like any other automation tool with real machine access. Back up regularly. Use a separate working copy or a different machine if you absolutely need an agent living in your terminal. A frontier model can still behave like a destructive script runner. I also generated SHA256 hashes for the preserved transcript and permission search output. EDIT / UPDATE: A few people asked about git. Yes, I know what git is. This was a local Electron prototype / working state that had not been pushed to a remote. Commits and backups are the right mitigation. But mitigation is not causation. The concerning part is that the destructive action was unrelated to my prompt. Claude Code was operating through a terminal session with real filesystem access under my user environment. Git may help recover a repo, but it does not protect everything else that same terminal session can access. My takeaway remains: Treat frontier terminal AI agents like real automation tools with destructive capability, not like chatbots. EDIT / UPDATE: Clarification because many comments are focusing on git: Yes, this specific local working state had not been pushed to a remote. That is on me. Lesson learned. But git is version control, not automatically a backup. If the only repo is local and the project root contents are recursively deleted, the local .git directory can be deleted too. Without a remote, separate clone, backup, or snapshot, local git alone is not enough.

3h ago

---

**[It's great to see how automated theorem proving is moving from a niche tool to solving real math problems](https://www.reddit.com/r/artificial/comments/1uknhui/its_great_to_see_how_automated_theorem_proving_is/)**

I used to think formal methods and interactive theorem provers like Lean 4 were basically just an extreme sport for type-theory purists. Like cool in theory, but mostly used for re-verifying undergraduate calculus or writing super tedious proofs for things we already knew were true anyway But seeing the shift right now (at least around me and these subs) has been pretty cool. Machine learning and neural provers are actually starting to uncover edge cases that human mathematicians just skipped over. And I was reading about how Aleph prover managed to formally verify a counterexample to an old Erdos conjecture,and it really shows even people who are new to this how fast this space is moving. Because it isn't just about catching minor typos in code anymore, but actively generating mathematical info that people missed for decades. And old brute-force methods are being replaced wth something way more sophisticated. Makes you think how it'll change in another five years when these systems become standard parts of any researcher's workflow.

4h ago

---

**[What's one AI feature that quietly became part of your daily routine?](https://www.reddit.com/r/artificial/comments/1ukld2m/whats_one_ai_feature_that_quietly_became_part_of/)**

Not the flashy stuff like generating images or writing essays. I'm talking about the feature you barely think about anymore because it's just become useful. For me, it's summarizing long articles and emails. I didn't expect to rely on it this much a year ago. What's yours?

6h ago

---

**[Why does it feel like big LLM providers are literally hiding prompt caching?](https://www.reddit.com/r/artificial/comments/1ukpj5f/why_does_it_feel_like_big_llm_providers_are/)**

I know the info is there. Somewhere in the pricing pages, docs, or API notes. But for something that can seriously change what you pay in production, it is weirdly under-explained. expeciely for other providers than openai which they do have decent explainer here - https://developers.openai.com/api/docs/guides/prompt-caching So basicly: two prompts can look almost identical, but one can be much cheaper to run just because it is ordered better. Put the changing parts too early, like the user query, variables, timestamps, metadata, or anything request-specific, and you can break the stable prefix the cache depends on. The practical rule is simple: Keep the repeatable stuff first. Start with system instructions, fixed rules, examples, schemas, and formatting requirements. Then put the dynamic user input and request-specific data near the end. That is it. Just a good prompt structure... But if you run LLMs at scale, this tiny detail can be the difference between insanely expensive LLMs usage and acctually good ROI product. full blog post here

3h ago

---

**[Are Redditors influencing AI the most?](https://www.reddit.com/r/artificial/comments/1ujuckz/are_redditors_influencing_ai_the_most/)**

1d ago

---

**[What happened to AI on April 18, 2025?](https://www.reddit.com/r/artificial/comments/1ukucjh/what_happened_to_ai_on_april_18_2025/)**

I run a recurring survey asking American adults if they support further development of artificial intelligence. AI Support* increased from April 2024 until April 18, 2025, hit an inflection point and then started decreasing. * As defined this way, among American adults, self-reported on an online survey with all the caveats that brings with it. Do you think this is a real trend and will it continue? https://preview.redd.it/i94n3m4wynah1.png?width=2703&format=png&auto=webp&s=a71a9c9fd822ccb5f38d7d48a0f63f8551bbc0c7

29m ago

---

**[Hmmmmm. Interesting.](https://www.reddit.com/r/artificial/comments/1ukta4c/hmmmmm_interesting/)**

I was curioius and asked Claude this. I thought that it would say like to live the longest life, or like Billionare, the usual stuff. It gave this.

1h ago

---

**[Gas giants use AI to raise prices, lawsuit says, another algorithmic hit to the cost of living](https://www.reddit.com/r/artificial/comments/1ukt7jy/gas_giants_use_ai_to_raise_prices_lawsuit_says/)**

A new federal lawsuit by California drivers accuses major gas chains, including Walmart and 7-Eleven, and technology company Kalibrate of using AI software to collude and keep pump prices artificially high. The case tests California’s updated antitrust law, which now treats algorithm-driven common pricing as potential price-fixing, amid statewide gas averaging $5.46 a gallon and growing scrutiny of corporate pricing tactics. Real estate and other industries already face probes into algorithmic and surveillance pricing, as Americans cite housing and energy costs as top worries and question whether genuine competition still exists. Read more.

🔗 [Los Angeles Times](https://www.latimes.com/california/story/2026-07-01/lawsuit-over-gas-prices-tests-clarification-to-states-antitrust-law) • 1h ago

---

**[We keep giving agents more autonomy and less oversight and it's starting to feel backwards.](https://www.reddit.com/r/artificial/comments/1uksq5a/we_keep_giving_agents_more_autonomy_and_less/)**

Every new framework release has the same kinda brag with stuff like longer task chains, more tool access, fewer "check in with a human" checkpoints. Okay, that's cool. Except almost nobody in these threads is talking about what happens when one of these things quietly does the wrong thing for three days straight before anyone notices. I saw some discussion where someone's agent had been silently retrying a broken API call and racking up costs the entire weekend, and the top comment was basically "yeah that happens." We spent like two decades building entire disciplines around code review, staged rollouts, canary deploys, precisely because software fails in boring silent ways and not dramatic ones. Feels like agents are just skipping past that whole lesson because everyone's racing to ship the most "autonomous" thing on their landing page. So genuinely, for anyone running agents on something real, what's actually stopping a bad one before it causes damage? Or are most teams still stitching those pieces together themselves?

1h ago

---

---

## Google News: "ai"

**[Employers who laid off workers citing AI are already starting to regret it](https://www.cnbc.com/2026/07/01/employers-who-laid-off-workers-for-ai-are-reversing-their-decisions.html)**

Companies are realizing artificial intelligence can't do everything after all, prompting them to rehire employees to grow their businesses

CNBC • 14h ago

---

**[They built the world’s most powerful AI. They’re facing a mystery they can’t explain.](https://www.washingtonpost.com/technology/2026/07/01/biggest-tech-companies-are-considering-whether-chatbots-have-emotions/)**

Anthropic, Google and Meta have hired computer scientists, neuroscientists and philosophers to study what some in the industry think may become a moral crisis.

The Washington Post • 3h ago

---

**[Michael Burry Cites ‘Beginning of the End’ With New AI Short Bets](https://www.wsj.com/finance/stocks/michael-burry-cites-beginning-of-the-end-with-new-ai-short-bets-50793c12)**

WSJ • 54m ago

---

**[Exclusive | SpaceX Showed Investors Prototype of Elon Musk’s New AI Device](https://www.wsj.com/tech/ai/spacex-showed-investors-prototype-of-elon-musks-new-ai-device-b445c57b)**

WSJ • 1h ago

---

**[SpaceX has an AI device prototype, and it sure sounds phone-ish](https://techcrunch.com/2026/07/01/spacex-has-an-ai-device-prototype-and-it-sure-sounds-phone-ish/)**

SpaceX reportedly showed investors a "handset-like" AI device before going public. It could be another signal SpaceX wants to expand into wireless.

TechCrunch • 23m ago

---

**[Musk denies WSJ report that SpaceX showed AI handset prototype before IPO](https://www.reuters.com/business/media-telecom/musk-denies-wsj-report-that-spacex-showed-ai-handset-prototype-before-ipo-2026-07-01/)**

Reuters • 14m ago

---

**[Big Tech’s Carbon Emissions Spike With Runaway Growth of AI](https://www.bloomberg.com/news/articles/2026-07-01/big-tech-s-carbon-emissions-spike-with-runaway-growth-of-ai)**

Bloomberg.com • 21m ago

---

**[Ai Weiwei: Button Up! review – skeleton chandeliers, a real-life temple – and too much silly Lego](https://www.theguardian.com/artanddesign/2026/jul/01/ai-weiwei-button-up-review-manchester)**

The artist’s latest show is a staggering takedown of colonial history, warfare and the migrant crisis, featuring buttons by the tonne and richly perfumed tea

The Guardian • 4h ago

---

**[Claude Science, an AI workbench for scientists, is now available](https://www.anthropic.com/news/claude-science-ai-workbench)**

Anthropic • 1d ago

---

**[U.S. Lifts Restrictions on Anthropic’s Most Powerful A.I. Models](https://www.nytimes.com/2026/06/30/technology/us-lifts-restrictions-anthropic.html)**

The New York Times • 18h ago

---

---

## HackerNews: "ai"

**[Godot will no longer accept AI-authored code contributions](https://news.ycombinator.com/item?id=48743472)**

At risk of drowning in AI slop code, Godot is firming up its contribution requirements.

⬆️ 510 • 💬 364 • 11h ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)

---

**[Tidal AI Policy](https://news.ycombinator.com/item?id=48718840)**

⬆️ 308 • 💬 345 • 2d ago • [tidal.com](https://tidal.com/ai-policy)

---

**[Working With AI: A concrete example](https://news.ycombinator.com/item?id=48720064)**

In this essay, Carson Gross walks through a concrete bug fix in hyperscript to show where AI helped, where it fell short, and why keeping a knowledgeable human in the loop is what kept complexity in check.

⬆️ 191 • 💬 70 • 2d ago • [htmx.org](https://htmx.org/essays/working-with-ai/)

---

**[AI boom risks global financial crash, warn central bankers](https://news.ycombinator.com/item?id=48713697)**

Reversal of ‘excessive’ tech investments could have serious economic consequences, report finds

⬆️ 158 • 💬 214 • 2d ago • [The Telegraph](https://www.telegraph.co.uk/business/2026/06/28/ai-boom-risks-global-financial-crash-central-bankers-warn/)

---

**[We need tech news sources which exclude AI](https://news.ycombinator.com/item?id=48713041)**

⬆️ 139 • 💬 80 • 2d ago

---

**[EU commissioners shut down air conditioning for employees, leave theirs on](https://news.ycombinator.com/item?id=48734940)**

As Brussels bakes, the Berlaymont building’s AC stops working.

⬆️ 137 • 💬 154 • 1d ago • [POLITICO](https://www.politico.eu/article/eu-commission-heatwave-hq-forced-shut-down-air-conditioning-europe/)

---

**[Ford rehires 'gray beard' engineers after AI falls short](https://news.ycombinator.com/item?id=48710749)**

"Mistakenly we thought that by just introducing artificial intelligence ... that would produce a high-quality product.”

⬆️ 135 • 💬 3 • 2d ago • [TechCrunch](https://techcrunch.com/2026/06/28/ford-rehires-gray-beard-engineers-after-ai-falls-short/)

---

**[Anthropic CEO: Open-Source AI is getting dangerous (2023)](https://news.ycombinator.com/item?id=48716750)**

⬆️ 58 • 💬 25 • 2d ago • [xcancel.com](https://xcancel.com/coinbureau/status/2071330294452666695)

---

**[Better Images of AI](https://news.ycombinator.com/item?id=48713051)**

⬆️ 55 • 💬 30 • 2d ago • [betterimagesofai.org](https://betterimagesofai.org/)

---

**[Amazon Is Awash with AI-Written Guideslop for Games That Aren't Even Out](https://news.ycombinator.com/item?id=48721494)**

Buy your novel-like, image-free, hallucinated guide to Alien: Isolation 2 today!

⬆️ 55 • 💬 3 • 2d ago • [Kotaku](https://kotaku.com/amazon-ai-game-guidebooks-alien-isolation-gears-of-war-2000711365)

---

---

## YouTube Videos: "ai"

**[AI has hacked the code of human civilization | Yuval Noah Harari](https://www.youtube.com/watch?v=hBtVGwuJzpk)**

Human domination relies on large-scale cooperation among strangers, which is sustained by bureaucratic systems – such as ...

📺 Yuval Noah Harari 

👁️ 125K • 👍 6K • 💬 604 • ⏱️ 46:52 • 1d ago

---

**[AI Shocks Again: Google Post-AGI , New Claude, Microsoft 7 AI, 92% Human Robot, Fable 5 Backlash](https://www.youtube.com/watch?v=u-CNOC_yK4k)**

This month in AI has been one of the busiest we've seen in a long time. Google revealed what could come after AGI, and the idea ...

📺 AI Revolution

👁️ 16K • 👍 509 • 💬 37 • ⏱️ 1:36:04 • 20h ago

---

**[Why is AI expensive all of a sudden?](https://www.youtube.com/watch?v=DDj30VWCbbY)**

ZapierPartner Sponsored by Zapier! Zapier MCP levels you up, connecting you directly to apps to automate your workflow.

📺 Alberta Tech

👁️ 105K • 👍 6K • 💬 576 • ⏱️ 9:43 • 1d ago

---

**[CNBC Panel EXPLODES Over AI Bubble Debate](https://www.youtube.com/watch?v=UMaOH0Ih9_0)**

Krystal and Emily discuss a CNBC panel exploding on a debate over AI bubble risks. Sign up for a PREMIUM Breaking Points ...

📺 Breaking Points

👁️ 177K • 👍 4K • 💬 1K • ⏱️ 18:18 • 1d ago

---

**[AI vs the Permanent Underclass: the End of Coding](https://www.youtube.com/watch?v=oTQzszSabhY)**

We told a generation to "learn to code," and then AI rugpulled everyone. Welcome to the AI singularity. [NEW] Official TechLead ...

📺 TechLead

👁️ 61K • 👍 3K • 💬 623 • ⏱️ 13:10 • 2d ago

---

**[Ford’s AI Push Failed Hard, Rehires 350 Engineers](https://www.youtube.com/watch?v=ZiqYX-JzIXw)**

Today's FULL PDS here: Watch The Full Philip DeFranco Show: https://www.youtube.com/defranco?sub_confirmation=1 ...

📺 DeFranco News Clips

👁️ 1.3M • 👍 75K • 💬 4K • ⏱️ 1:16 • 1d ago

---

**[Your OS Changes Everything for Local AI](https://www.youtube.com/watch?v=QeAHC1jGxck)**

One benchmark made me double-check my numbers. The rest tell a different story. Try out ChatLLM - http://chatllm.abacus.ai/ltf ...

📺 Alex Ziskind

👁️ 62K • 👍 2K • 💬 158 • ⏱️ 14:13 • 1d ago

---

**[Meta to build cloud infrastructure business to sell AI compute](https://www.youtube.com/watch?v=tyl5SUN0ua4)**

CNBC's Julia Boorstin reports on news regarding Meta.

📺 CNBC Television

👁️ 3K • 👍 47 • 💬 15 • ⏱️ 1:47 • 3h ago

---

**[Dan Ives on the Tech Rally, Growth of AI, Data Centers](https://www.youtube.com/watch?v=ec1WAGENfK8)**

Dan Ives, Wedbush Securities global head of tech research, argued that massive AI-related capital expenditures by hyperscalers ...

📺 Bloomberg Television

👁️ 9K • 👍 196 • 💬 26 • ⏱️ 6:55 • 6h ago

---

**[New findings reveal AI bubble worries are justified](https://www.youtube.com/watch?v=xCzCyPoI-eA)**

New data reveals bubble worries are justified: "If you are worried that we're in an Al bubble, well, I have some news for you that ...

📺 Prof G Markets

👁️ 86K • 👍 3K • 💬 119 • ⏱️ 1:08 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 630,246 • ❤️ 1,568 • 3d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,113,871 • ❤️ 1,133 • 3d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 159,967 • ❤️ 3,157 • 8d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 233,701 • ❤️ 596 • 6d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 34,371 • ❤️ 492 • 6d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 288,741 • ❤️ 915 • 12d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 191,409 • ❤️ 364 • 6d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 46,677 • ❤️ 326 • 6d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**

*Empero*

Qwythos-9B is an uncensored, full-fine-tuned 9B reasoning model with a 1M token context window, enhanced function calling, and self-correction capabilities. It excels in complex domains like cybersecurity and biomedical research, outperforming its base model significantly on reasoning benchmarks and demonstrating reliable tool use for factual accuracy.

`text-generation` `9.4B`

⬇️ 114,499 • ❤️ 612 • 3d ago

---

**[Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)**

*DeepReinforce*

Ornith-1.0-35B is a state-of-the-art, MIT-licensed language model for agentic coding, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving training framework to generate high-quality code solutions and is optimized for single-GPU deployment.

`text-generation` `664,944`

⬇️ 135,452 • ❤️ 284 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 44 • 💬 5 • ⭐ 12,690 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 72,793 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 22 • 💬 2 • ⭐ 9,181 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 90,145 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 249 • 💬 4 • ⭐ 10,286 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 12 • 💬 1 • ⭐ 9,945 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 26,296 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 12 • 💬 2 • ⭐ 18,026 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 85,010 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 78,975 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 70.3k • 🔱 3.6k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.2k • 🔱 1.1k • 1h ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 5.9k • 🔱 752 • 9m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 4.7k • 🔱 589 • 4h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.2k • 🔱 199 • 4d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.2k • 🔱 173 • 3d ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.8k • 🔱 155 • 5d ago

---

**[inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)**

Beautiful, AI-native markdown editor and LLM Wiki

`TypeScript` `2nd-brain` `agent-skills` `claude` `codex` `docs`

⭐ 1.7k • 🔱 82 • 1m ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 86 • 18d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.5k • 🔱 63 • 21h ago

---

---

*Generated by PeekDeck - A glance is all you need*
