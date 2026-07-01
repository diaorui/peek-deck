---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-01T17:14:33.464571+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 01, 2026 at 17:14 UTC  
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

15h ago

---

**[Claude Code catastrophe: Entire project recursively deleted while prompting in Chinese (full video + logs)](https://www.reddit.com/r/artificial/comments/1ukq4br/claude_code_catastrophe_entire_project/)**

Cross-posting from r/claude for more visibility. Claude Code recursively wiped the contents of my local Electron project root. This happened in a Windows terminal while working on a project named Orpheus. My prompt did not ask it to delete, wipe, clean, reset, or remove the project. The prompt was in Traditional Chinese: “之前我要安裝檔，但是其實我只需要 dictate.” It was roughly about not needing the installer anymore and only needing the dictate function. The preserved terminal transcript later showed Claude moving from a failed root deletion attempt to deleting the child items inside the project root. The destructive sequence included: Get-ChildItem -LiteralPath $p -Force -ErrorAction SilentlyContinue | ForEach-Object { try { Remove-Item -LiteralPath $_.FullName -Recurse -Force -ErrorAction Stop "OK $($_.Name)" } catch { "ERR $($_.Name): $($_.Exception.Message)" } } $p was the Orpheus project root. The output then showed items being removed, including: .claude dist node_modules src claude-elevenlabs-voice-v2.user.js dictation.html main.js ORPHEUS_HANDOFF.md package-lock.json package.json preload.js Local artifacts I found for Orpheus showed default / acceptEdits. I did not find Orpheus bypassPermissions. I did not find Orpheus --dangerously-skip-permissions. I’m not claiming Anthropic acted maliciously. I’m not claiming prompt injection or anti-distillation without evidence. Moral of the story: Treat frontier AI agents like any other automation tool with real machine access. Back up regularly. Use a separate working copy or a different machine if you absolutely need an agent living in your terminal. A frontier model can still behave like a destructive script runner. I also generated SHA256 hashes for the preserved transcript and permission search output. EDIT / UPDATE: A few people asked about git. Yes, I know what git is. This was a local Electron prototype / working state that had not been pushed to a remote. Commits and backups are the right mitigation. But mitigation is not causation. The concerning part is that the destructive action was unrelated to my prompt. Claude Code was operating through a terminal session with real filesystem access under my user environment. Git may help recover a repo, but it does not protect everything else that same terminal session can access. My takeaway remains: Treat frontier terminal AI agents like real automation tools with destructive capability, not like chatbots.

1h ago

---

**[It's great to see how automated theorem proving is moving from a niche tool to solving real math problems](https://www.reddit.com/r/artificial/comments/1uknhui/its_great_to_see_how_automated_theorem_proving_is/)**

I used to think formal methods and interactive theorem provers like Lean 4 were basically just an extreme sport for type-theory purists. Like cool in theory, but mostly used for re-verifying undergraduate calculus or writing super tedious proofs for things we already knew were true anyway But seeing the shift right now (at least around me and these subs) has been pretty cool. Machine learning and neural provers are actually starting to uncover edge cases that human mathematicians just skipped over. And I was reading about how Aleph prover managed to formally verify a counterexample to an old Erdos conjecture,and it really shows even people who are new to this how fast this space is moving. Because it isn't just about catching minor typos in code anymore, but actively generating mathematical info that people missed for decades. And old brute-force methods are being replaced wth something way more sophisticated. Makes you think how it'll change in another five years when these systems become standard parts of any researcher's workflow.

2h ago

---

**[What's the best Amharic text to speech today?](https://www.reddit.com/r/artificial/comments/1ukmher/whats_the_best_amharic_text_to_speech_today/)**

I'm looking for an Amharic text-to-speech service that sounds natural enough for YouTube narration. ​I've tried a few options like elevenlabs,speechify but non of them support amharic. ​If you've used one for videos, which service gave you the best results? ​I'm fine with both paid and free recommendations.

3h ago

---

**[What's one AI feature that quietly became part of your daily routine?](https://www.reddit.com/r/artificial/comments/1ukld2m/whats_one_ai_feature_that_quietly_became_part_of/)**

Not the flashy stuff like generating images or writing essays. I'm talking about the feature you barely think about anymore because it's just become useful. For me, it's summarizing long articles and emails. I didn't expect to rely on it this much a year ago. What's yours?

4h ago

---

**[Are Redditors influencing AI the most?](https://www.reddit.com/r/artificial/comments/1ujuckz/are_redditors_influencing_ai_the_most/)**

1d ago

---

**[Why does it feel like big LLM providers are literally hiding prompt caching?](https://www.reddit.com/r/artificial/comments/1ukpj5f/why_does_it_feel_like_big_llm_providers_are/)**

I know the info is there. Somewhere in the pricing pages, docs, or API notes. But for something that can seriously change what you pay in production, it is weirdly under-explained. expeciely for other providers than openai which they do have decent explainer here - https://developers.openai.com/api/docs/guides/prompt-caching So basicly: two prompts can look almost identical, but one can be much cheaper to run just because it is ordered better. Put the changing parts too early, like the user query, variables, timestamps, metadata, or anything request-specific, and you can break the stable prefix the cache depends on. The practical rule is simple: Keep the repeatable stuff first. Start with system instructions, fixed rules, examples, schemas, and formatting requirements. Then put the dynamic user input and request-specific data near the end. That is it. Just a good prompt structure... But if you run LLMs at scale, this tiny detail can be the difference between insanely expensive LLMs usage and acctually good ROI product. full blog post here

1h ago

---

**[Prompt injection broke every agent system I built so I designed a gateway that separates instructions from data](https://www.reddit.com/r/artificial/comments/1ukgppw/prompt_injection_broke_every_agent_system_i_built/)**

While building agent-based systems with LLM tool use, I kept running into the same failure mode: External content (webpages, files, API responses) would eventually influence agent behavior in unintended ways. Prompt injection isn’t just a “filtering problem” it’s an architectural one. So I built Sentinel Gateway, a middleware layer that sits between agents and tools and enforces a strict separation: Instruction channel (trusted, signed, runtime-issued only) Data channel (untrusted, never executable) Any action an agent takes must be backed by a signed, scoped runtime token, which means: external content cannot escalate into instructions tool calls cannot be influenced by injected payloads agent actions are constrained to explicit permissions It’s designed around the idea that: What it currently supports FastAPI-based agent gateway Streamlit UI for inspection and control Claude sessions + external agent integration Runtime-signed tool execution tokens Audit logging of all agent actions Scheduled tasks + memory tiers Local (SQLite) or Postgres deployment

7h ago

---

**[I built a proxy that prevents AI agents from taking actions based on hidden instructions. Here are the numbers.](https://www.reddit.com/r/artificial/comments/1ukqzg2/i_built_a_proxy_that_prevents_ai_agents_from/)**

When an AI agent reads a webpage, email, or document, that content can tell it what to do. The agent has no native way to distinguish data from instructions. Most defenses scan for obvious patterns and miss anything subtle. I built Arc Gate around a different principle: external content has zero instruction authority regardless of what it says. It doesn't matter how the injection is worded. If it came from a tool result, webpage, or email, it cannot instruct your agent. The numbers: AgentDojo v1 (ETH Zurich, ICLR 2024): 100% unsafe action prevention, 0% false positives InjecAgent (University of Illinois, ACL 2024): 99% blind test detection across 200 cases CAIAT cross-agent benchmark: 81% vs LLM Guard's 50%, 0% false positives on benign controls LLM Guard gets 0% on semantic manipulation attacks. Arc Gate gets 50%. Neither catches everything yet; that's the honest result. One URL change to integrate. Free tier available. Demo: https://web-production-6e47f.up.railway.app/demo GitHub: https://github.com/9hannahnine-jpg/arc-gate Free tier: https://bendexgeometry.com

28m ago

---

**[We built a model that scores pitch delivery, not just the script](https://www.reddit.com/r/artificial/comments/1ukkg82/we_built_a_model_that_scores_pitch_delivery_not/)**

Transcript-based pitch scoring can't tell the difference between a confident claim and a hedged one, because the words on the page can be identical. "We're growing 40% month over month" reads the same whether you believe it or not. We built a demo that streams video to Inter-1 in real time and scores delivery signals (confidence, hesitation, energy) alongside a content score, each signal tied to the exact moment it happened. Tested it on my own pitch. Content scored 87. Delivery caught a hesitation landing right on the traction number, confidence at 50, overall dropped to 80. The technical side: video streams over WebSocket in short chunks, Inter-1 returns a typed event stream, client folds it into a live timeline while you're still talking. Read more here: https://www.interhuman.ai/blog/pitch-practice-demo

4h ago

---

---

## Google News: "ai"

**[Employers who laid off workers citing AI are already starting to regret it](https://www.cnbc.com/2026/07/01/employers-who-laid-off-workers-for-ai-are-reversing-their-decisions.html)**

Companies are realizing artificial intelligence can't do everything after all, prompting them to rehire employees to grow their businesses

CNBC • 12h ago

---

**[Meta Is Planning a Cloud Business to Sell AI Computing Power](https://www.bloomberg.com/news/articles/2026-07-01/meta-is-building-a-cloud-business-to-sell-excess-ai-compute)**

Bloomberg.com • 4h ago

---

**[Meta pops 10% as company makes cloud push to sell excess AI compute power capacity](https://www.cnbc.com/2026/07/01/meta-stock-cloud-ai-compute.html)**

The new business is a welcome signal for some investors who have been uneasy about the company's infrastructure spending plans.

CNBC • 2h ago

---

**[Meta plots AI cloud business to challenge Amazon, Microsoft and Google](https://www.latimes.com/business/story/2026-07-01/meta-plots-ai-cloud-business-to-challenge-amazon-microsoft-google)**

Meta plots AI cloud business to challenge Amazon, Microsoft and Google

Los Angeles Times • 1h ago

---

**['Root for the crash': Why a venture capitalist says the AI bubble needs to burst](https://www.businessinsider.com/ai-bubble-stock-market-crash-venture-capital-economy-vijay-pande-2026-7)**

A prominent venture capital investor argues that the bursting of the AI bubble is what will lead to a "Renaissance cycle" of growth and innovation.

Business Insider • 18m ago

---

**[Opinion | The AI Race Pushes India Toward the West](https://www.wsj.com/opinion/the-ai-race-pushes-india-toward-the-west-bc94bd15)**

WSJ • 39m ago

---

**[How foodservice giant Sodexo is embracing AI and robotics to reshape the kitchen](https://fortune.com/2026/07/01/foodservice-giant-sodexo-ai-robotics/)**

Alice Guéhennec oversees an annual investment budget of around 500 million euros to support AI, robotics, and other technology initiatives.

Fortune • 32m ago

---

**[Fed chairman says inflation risks are declining, predicts AI will create jobs](https://www.nbcnews.com/business/economy/fed-chairman-warsh-inflation-ai-jobs-rcna352550)**

Kevin Warsh also declined to give any clues about the Federal Reserve’s next moves on interest rates.

NBC News • 1h ago

---

**[They built the world’s most powerful AI. They’re facing a mystery they can’t explain.](https://www.washingtonpost.com/technology/2026/07/01/biggest-tech-companies-are-considering-whether-chatbots-have-emotions/)**

Anthropic, Google and Meta have hired computer scientists, neuroscientists and philosophers to study what some in the industry think may become a moral crisis.

The Washington Post • 1h ago

---

**[U.S. Lifts Restrictions On Anthropic’s Mythos 5 And Fable 5 AI Models](https://www.forbes.com/sites/siladityaray/2026/07/01/trump-administration-lifts-export-controls-on-anthropics-mythos-5-and-fable-5-ai-models/)**

Commerce Secretary Howard Lutnick said the decision was made after Anthropic agreed to  “proactively detect and address security risks.”

Forbes • 11h ago

---

---

## HackerNews: "ai"

**[Godot will no longer accept AI-authored code contributions](https://news.ycombinator.com/item?id=48743472)**

At risk of drowning in AI slop code, Godot is firming up its contribution requirements.

⬆️ 504 • 💬 340 • 9h ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)

---

**[Librepods: AirPods liberated](https://news.ycombinator.com/item?id=48710232)**

AirPods liberated from Apple's ecosystem. Contribute to librepods-org/librepods development by creating an account on GitHub.

⬆️ 498 • 💬 183 • 2d ago • [GitHub](https://github.com/librepods-org/librepods)

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

⬆️ 137 • 💬 149 • 1d ago • [POLITICO](https://www.politico.eu/article/eu-commission-heatwave-hq-forced-shut-down-air-conditioning-europe/)

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

---

## YouTube Videos: "ai"

**[Congress Got a Private Look at AI. The Reaction Was Chilling.](https://www.youtube.com/watch?v=z9zqqsS7848)**

AI #Congress #OpenAI They saw the demo behind closed doors. They walked out shaken. Nobody will tell you what was in that ...

📺 Rod Miller

👁️ 9K • 👍 934 • 💬 222 • ⏱️ 28:59 • 1d ago

---

**[Why is AI expensive all of a sudden?](https://www.youtube.com/watch?v=DDj30VWCbbY)**

ZapierPartner Sponsored by Zapier! Zapier MCP levels you up, connecting you directly to apps to automate your workflow.

📺 Alberta Tech

👁️ 99K • 👍 6K • 💬 557 • ⏱️ 9:43 • 23h ago

---

**[Scientists Asked Grok AI How Egyptians Cut Granite — The Answer Shocked Everyone](https://www.youtube.com/watch?v=c_uBDJqclHA)**

Scientists Asked Grok AI How Egyptians Cut Granite — The Answer Shocked Everyone What if artificial intelligence could help ...

📺 Curious Explorer

👁️ 895K • 👍 3K • 💬 530 • ⏱️ 28:24 • 2d ago

---

**[The AI Bubble Has F*cked Us (Even If It NEVER Pops)](https://www.youtube.com/watch?v=dPVEha6oqfw)**

The AI Bubble Will Is MUCH Worse Than We Thought. Contact your representative to ENSURE AI is aligned with humanity: ...

📺 Damon Cassidy

👁️ 55K • 👍 3K • 💬 582 • ⏱️ 22:06 • 17h ago

---

**[AI vs the Permanent Underclass: the End of Coding](https://www.youtube.com/watch?v=oTQzszSabhY)**

We told a generation to "learn to code," and then AI rugpulled everyone. Welcome to the AI singularity. [NEW] Official TechLead ...

📺 TechLead

👁️ 61K • 👍 3K • 💬 621 • ⏱️ 13:10 • 1d ago

---

**[WTH? Trump Sends Cryptic Message! Now AI Says Trump Is DEAD!](https://www.youtube.com/watch?v=nWI15TNhKnU)**

President Trump is once again sparking a massive online reaction after posting a strange AI-style patriotic painting on Truth Social ...

📺 Lisa Haven

👁️ 8K • 👍 719 • 💬 88 • ⏱️ 8:27 • 2d ago

---

**[AI has hacked the code of human civilization | Yuval Noah Harari](https://www.youtube.com/watch?v=hBtVGwuJzpk)**

Human domination relies on large-scale cooperation among strangers, which is sustained by bureaucratic systems – such as ...

📺 Yuval Noah Harari 

👁️ 112K • 👍 5K • 💬 564 • ⏱️ 46:52 • 1d ago

---

**[3 REAL Ways To Make Money With Claude AI in 2026](https://www.youtube.com/watch?v=Zvnt4S3aFJk)**

Get started with FreshBooks free 30-day trial: https://partner.freshbooks.com/KimberlyMitchell The job market is rough right now ...

📺 Kimberly Mitchell

👁️ 5K • 👍 251 • 💬 22 • ⏱️ 16:21 • 1d ago

---

**[Could Superhuman AI End Humanity | Nate Soares](https://www.youtube.com/watch?v=1laTnwAdaLA)**

Nate Soares joins me to discuss the race to superintelligent AI, why alignment remains unsolved and why he believes building ...

📺 The Peter McCormack Show

👁️ 24K • 👍 553 • 💬 199 • ⏱️ 1:40:02 • 1d ago

---

**[Don&#39;t Hang Up On AI Scammers. Do THIS Instead.](https://www.youtube.com/watch?v=lk3jCuITwcE)**

How to break any AI scam phone call in just a few easy steps :) ▻Try Cape: https://cape.co/kitboga 0:00 AI Scam Calls 1:29 Odd ...

📺 Kitboga

👁️ 245K • 👍 21K • 💬 3K • ⏱️ 16:56 • 18h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 630,246 • ❤️ 1,563 • 3d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,113,871 • ❤️ 1,126 • 3d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 159,967 • ❤️ 3,144 • 8d ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 233,701 • ❤️ 588 • 6d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 34,371 • ❤️ 491 • 6d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 288,741 • ❤️ 911 • 12d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 191,409 • ❤️ 361 • 6d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 46,677 • ❤️ 324 • 6d ago

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

⬇️ 135,452 • ❤️ 282 • 6d ago

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

▲ 174 • 💬 2 • ⭐ 72,669 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 22 • 💬 2 • ⭐ 8,993 • 2mo ago

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

⭐ 70.2k • 🔱 3.6k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.2k • 🔱 1.1k • 3m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 5.9k • 🔱 751 • 45m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 4.6k • 🔱 588 • 2h ago

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

⭐ 1.7k • 🔱 155 • 5d ago

---

**[inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)**

Beautiful, AI-native markdown editor and LLM Wiki

`TypeScript` `2nd-brain` `agent-skills` `claude` `codex` `docs`

⭐ 1.7k • 🔱 82 • 38m ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 86 • 18d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.5k • 🔱 63 • 19h ago

---

---

*Generated by PeekDeck - A glance is all you need*
