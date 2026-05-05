---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-05T20:08:03.580845+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 05, 2026 at 20:08 UTC  
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

🔗 [Dexerto](https://www.dexerto.com/entertainment/x-user-tricks-grok-into-sending-them-200000-in-crypto-using-morse-code-3361036/) • 8h ago

---

**[Pennsylvania sues AI company, saying its chatbots illegally hold themselves out as licensed doctors](https://www.reddit.com/r/artificial/comments/1t4jn6g/pennsylvania_sues_ai_company_saying_its_chatbots/)**

Pennsylvania has sued an artificial intelligence chatbot maker, saying its chatbots illegally hold themselves out as doctors and are deceiving the system’s users into thinking they are getting medical advice from a licensed professional.

🔗 [AP News](https://apnews.com/article/character-ai-chatbots-medical-advice-pennsylvania-46502067ed5b3cd9f9173f194ad30070) • 4h ago

---

**[Made a tool that builds its own training data and improves each cycle by learning from what it got wrong](https://www.reddit.com/r/artificial/comments/1t4egej/made_a_tool_that_builds_its_own_training_data_and/)**

The basic idea is pretty simple. You give it a few seed prompts. It generates instruction-response pairs, an LLM scores each one, the good ones go into your training set and the bad ones become the seeds for the next round. Each cycle the model is essentially practicing on what it failed at before. You can run the judge completely locally with Ollama if you do not want to send data to any API. The fine-tuning at the end uses Unsloth on a free Colab GPU so the whole thing is doable without spending money. It is more of a practical tool than a research project but the idea of using failure cases as curriculum is something I find genuinely interesting. Would love to hear if anyone has done something similar. Github project link is in comments below 👇

7h ago

---

**[Uber Shares What Happens When 1.500 AI Agents Hit Production](https://www.reddit.com/r/artificial/comments/1t48gnn/uber_shares_what_happens_when_1500_ai_agents_hit/)**

Learn how Uber manages over 1.500 AI agents in production, tackling challenges in MCP infrastructure, security, and tool discovery at scale.

🔗 [ShiftMag](https://shiftmag.dev/uber-shares-what-happens-when-1-500-ai-agents-hit-production-9430/) • 12h ago

---

**[OpenAI will produce as many as 30 million 'AI agent' phones early next year, says industry analyst](https://www.reddit.com/r/artificial/comments/1t4ff54/openai_will_produce_as_many_as_30_million_ai/)**

According to a well-known leaker, the company could begin mass production of its first AI-focused phone as early as the first half of 2027.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/openai-will-produce-as-many-as-30-million-ai-agent-phones-early-next-year-says-industry-analyst/) • 6h ago

---

**[Two failure modes I caught in my AI lab in one day. Both involve the system silently lying about its own state.](https://www.reddit.com/r/artificial/comments/1t4cx88/two_failure_modes_i_caught_in_my_ai_lab_in_one/)**

I operate an autonomous lab of evolutionary trading agents. Yesterday I found two bugs that look superficially different but are actually the same class of problem. Sharing because both affect autonomous AI systems specifically and most builders don't see them coming. **Failure mode 1: circular validation.** Setup. 69 real decisions made by the system over 58 days. Standard retrospective evaluation: label each decision as correct, false alarm, or ambiguous based on what happened next. Result. 94% labelled as correct. Looked great. Why it was wrong. 64 of the 65 "correct" labels came from died=True. The agents died because of conditions like "PF below threshold", "losing streak", "hardcore protocol triggered". All of those are also triggers for the original decision. So the system was validating its own decisions using outcomes generated by the same logic that produced the decisions. This is the textbook circular validation problem applied to autonomous decision-making. Three patterns to check for in your own stack: 1. Reward functions that include the agent's own action as input. If the agent gets reward partly because it took action X, and then you measure "did action X work" by looking at reward, you've got the loop. 2. Self-reported state in evaluation. If the agent reports "I think I succeeded" and you use that as ground truth, you're not validating, you're trusting. 3. Pipelines where the model that proposes is the same model that judges. The fix is structural separation. Decisions and outcomes get written by independent components. They cannot share code, logic, or thresholds. Architecture, not statistics. **Failure mode 2: state model divergence.** Same day, different bug. I had been documenting and operating under the belief that my system was off. Closed cleanly. No services running. No crons firing. A grep through my shell config showed me wrong. A bashrc line auto-launched the system on every terminal open. The process was adopted by init, detached from the shell that started it. Invisible to ps unless you knew the exact name. Three days running, generating evolutionary cycles, sending status reports. The connection between failure modes. In both cases, my mental model of the system diverged from the system's actual state. The first divergence was inside the code: the validation logic was structurally aligned with the decision logic, so it told me what I wanted to hear. The second divergence was outside the code: my belief that the system was off came from my memory of turning off services, which is not the same as the system actually being off. Three takeaways for anyone building autonomous systems solo: 1. Validation logic and decision logic must be enforced separate at the architecture level, not at the code review level. Solo builders don't get code review. 2. System state documentation cannot be derived from intent. It has to be derived from actual measurement against the running machine. Every check, fresh. 3. The cost of these bugs scales with how autonomous your system is. A script that runs once when you press play has limited surface area for divergence. A system that operates continuously while you assume otherwise can drift for weeks before you notice. I'm rebuilding the validation layer this week with explicit separation. Decisions table writes hypotheses with explicit predicted outcomes. Outcomes table is written by an observer that reads market data directly and never imports decision logic. There's an architecture test in CI that fails if anyone imports decision-maker code from observer code. The deeper question is whether autonomous systems built solo can ever be trustworthy without external review. My current answer: yes, but only if the architecture forces the separation that a team would force socially. The harder you make it for the system to lie to you, the less it will. Happy to discuss implementation details or share specific patterns if anyone's working on similar problems.

8h ago

---

**[Meta Hit With Massive Lawsuit—Publishers Say AI Was Trained on “Stolen” Books](https://www.reddit.com/r/artificial/comments/1t4m85o/meta_hit_with_massive_lawsuitpublishers_say_ai/)**

Major publishers sue Meta over AI training data, raising copyright concerns and challenging fair use in tech.

🔗 [Financership](https://www.financership.com/meta-ai-copyright-lawsuit-publishers/) • 2h ago

---

**[Qt's latest AI push is letting AI agents deal with performance profiling](https://www.reddit.com/r/artificial/comments/1t4lo3s/qts_latest_ai_push_is_letting_ai_agents_deal_with/)**

The Qt Group announced today the QML Profiler Skill for Agentic Development

🔗 [phoronix.com](https://www.phoronix.com/news/Qt-QML-Profiler-AI-Agent) • 2h ago

---

**[Anthropic Launches Enterprise AI Firm With Wall Street Giants](https://www.reddit.com/r/artificial/comments/1t42w30/anthropic_launches_enterprise_ai_firm_with_wall/)**

Anthropic is launching a new venture focused on selling AI tools to enterprise companies. This effort is being launched in partnership with Goldman Sachs, the Wall Street bank said Monday (May 4), in conjunction with investment firm Blackstone, and private equity group Hellman & Friedman, and will help companies embed Anthropic’s Claude artificial intelligence (AI) model into their businessses. “Enterprise demand for Claude is significantly outpacing any single delivery model,” Krishna Rao, Anthropic’s finance chief, said in a news release provided to PYMNTS. “Our partnerships with the world’s leading systems integrators are central to how Claude reaches large enterprises. This new firm brings additional operating capability to the ecosystem and capital from leading alternative asset managers.” Marc Nachmann, global head of asset and wealth management at Goldman Sachs, said the partnership will allow mid-market companies to employ Anthropic’s tech to bolster their businesses. “By democratizing access to forward-deployed engineers, the new company can help the expansive network of portfolio companies in our Asset Management business and other companies of similar sizes accelerate AI adoption to grow and scale their operations,” he added.

17h ago

---

**[A YouTube video you all might enjoy](https://www.reddit.com/r/artificial/comments/1t4q7m8/a_youtube_video_you_all_might_enjoy/)**

A Bioethicist just made a video about how the movie Interstellar reveals the real existential threat of AI How Interstellar Shows the REAL Existential Risk of AI

22m ago

---

---

## Google News: "ai"

**[Congress Is Doing Little to Prepare for Potential A.I. Job Losses](https://www.nytimes.com/2026/05/05/business/artificial-intelligence-safety-net.html)**

The New York Times • 5h ago

---

**[Richard Dawkins concludes AI is conscious, even if it doesn’t know it](https://www.theguardian.com/technology/2026/may/05/richard-dawkins-ai-consciousness-anthropic-claude-openai-chatgpt)**

Chats with AI bots have convinced evolutionary biologist but most experts say he is being misled by mimicry

The Guardian • 1h ago

---

**[Coinbase Lays Off 14% of Employees as A.I. Changes Work](https://www.nytimes.com/2026/05/05/technology/coinbase-layoffs-ai.html)**

The New York Times • 1h ago

---

**[Coinbase didn't just lay off 14% of its staff due to AI. It replaced managers with ‘player-coaches’ and turned its org chart upside down](https://fortune.com/2026/05/05/coinbase-layoffs-14-of-employees-ai-tech-ai-job-anxiety-crypto/)**

“We are not just reducing headcount and cutting costs, we’re fundamentally changing how we operate,” CEO Brian Armstrong said.

Fortune • 4h ago

---

**[Formerly SF-headquartered crypto giant to lay off 700 workers in AI shift](https://www.sfgate.com/tech/article/coinbase-layoffs-2026-sf-22242957.php)**

SFGATE • 40m ago

---

**[The Elon Musk-OpenAI trial is producing more heat than light in the debate over who should control AI](https://fortune.com/2026/05/05/musk-court-fight-openai/)**

The trial has had a few bombshell moments, but is unlikely to impact where AI is heading—or who controls it.

Fortune • 25m ago

---

**[Coursera CEO Greg Hart at HumanX - enrollment in AI course ‘every four seconds’](https://qz.com/coursera-ceo-humanx-enrollment-in-ai-course-every-four-seconds)**

Coursera chief executive officer Greg Hart at HumanX - enrollment in AI course ‘every four seconds’

qz.com • 3m ago

---

**[Anthropic Unveils AI Agents to Field Financial Services Tasks](https://www.bloomberg.com/news/articles/2026-05-05/anthropic-unveils-ai-agents-to-field-financial-services-tasks)**

Bloomberg.com • 3h ago

---

**[Agents for financial services and insurance](https://www.anthropic.com/news/finance-agents)**

We're releasing ten new Cowork and Claude Code plugins, integrations with the Microsoft 365 suite, new connectors, and an MCP app for financial services and insurance organizations.

Anthropic • 5h ago

---

**[Anthropic Releases New AI Agents for Financial Services Firms](https://www.wsj.com/tech/ai/anthropic-releases-new-ai-agents-for-financial-services-firms-e2829b37)**

WSJ • 2h ago

---

---

## HackerNews: "ai"

**[Google Chrome silently installs a 4 GB AI model on your device without consent](https://news.ycombinator.com/item?id=48019219)**

Google Chrome is downloading a 4 GB Gemini Nano model onto users' machines without consent, with no opt-in, no opt-out short of enterprise tooling, and an automatic re-download every time the user deletes it. The pattern is identical to the Anthropic Claude Desktop case I wrote about last month, but the scale is between two and three orders of magnitude larger. This article does the legal analysis and, for the first time, the environmental analysis. The numbers are not small.

⬆️ 955 • 💬 653 • 12h ago • [That Privacy Guy!](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/)

---

**[Let's Buy Spirit Air](https://news.ycombinator.com/item?id=48002777)**

Spirit Airlines collapsed. Before private equity locks it up, the people can own it. Join the Spirit 2.0 founding coalition. One member, one vote. Profits shared by all.

⬆️ 595 • 💬 566 • 1d ago • [letsbuyspiritair.com](https://letsbuyspiritair.com/)

---

**[How OpenAI delivers low-latency voice AI at scale](https://news.ycombinator.com/item?id=48013919)**

How OpenAI rebuilt its WebRTC stack to power real-time Voice AI with low latency, global scale, and seamless conversational turn-taking.

⬆️ 490 • 💬 141 • 1d ago • [OpenAI](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)

---

**[AI didn't delete your database, you did](https://news.ycombinator.com/item?id=48022742)**

Last week, a tweet went viral showing a guy claiming that a Cursor/Claude agent deleted his company's production database. We watched from the sidelines as he tried to get a confession from the agent:

⬆️ 454 • 💬 241 • 6h ago • [Ibrahim Diallo Blog](https://idiallo.com/blog/ai-didnt-delete-your-database-you-did)

---

**[Specsmaxxing – On overcoming AI psychosis, and why I write specs in YAML](https://news.ycombinator.com/item?id=47994012)**

The toolkit for spec-driven development. Write feature specs, not prompts. Ship better software with AI agents that understand your requirements.

⬆️ 282 • 💬 294 • 2d ago • [acai.sh](https://acai.sh/blog/specsmaxxing)

---

**[Three Inverse Laws of AI](https://news.ycombinator.com/item?id=48023861)**

⬆️ 271 • 💬 174 • 4h ago • [susam.net](https://susam.net/inverse-laws-of-robotics.html)

---

**[When everyone has AI and the company still learns nothing](https://news.ycombinator.com/item?id=48020063)**

Are people using AI, or is the organization learning from it? What changed because we spent those tokens? And who moves discoveries from individuals to teams to organizational capabilities?

⬆️ 246 • 💬 173 • 10h ago • [Robert Glaser](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/)

---

**[AI Product Graveyard](https://news.ycombinator.com/item?id=48021968)**

Curated list of AI tools and AI startups that have shut down, been acquired and folded, or had their domains lapse. Updated as our editorial team confirms each death.

⬆️ 233 • 💬 83 • 7h ago • [tooldirectory.ai](https://tooldirectory.ai/ai-graveyard)

---

**[OpenAI, Google, and Microsoft Back Bill to Fund 'AI Literacy' in Schools](https://news.ycombinator.com/item?id=48010774)**

A new bill introduced by Senators Adam Schiff and Mike Rounds would award grants to the National Science Foundation—which has endured massive funding cuts under the Trump Administration for science research—to put “AI literacy” in schools.

⬆️ 118 • 💬 110 • 1d ago • [404 Media](https://www.404media.co/literacy-in-future-technologies-artificial-intelligence-act-adam-schiff-mike-rounds/)

---

**[Voice-AI-for-Beginners – A curated learning path for developers](https://news.ycombinator.com/item?id=47991018)**

Set of 📝 with 🔗 to help those building Voice AI agents 🎙️🤖 - mahimairaja/voiceai

⬆️ 83 • 💬 4 • 2d ago • [GitHub](https://github.com/mahimairaja/voiceai)

---

---

## YouTube Videos: "ai"

**[If You&#39;re Worried About AI, You NEED To See This](https://www.youtube.com/watch?v=6rGhvV3rZa4)**

AI CEOs are telling you your job is about to disappear. NYU Professor Scott Galloway says that narrative is "mostly bullshit" and ...

📺 The Diary Of A CEO Clips

👁️ 89K • 👍 2K • 💬 367 • ⏱️ 21:59 • 1d ago

---

**[AI Just Designed A Quantum Computer](https://www.youtube.com/watch?v=l_bzA_M6_qo)**

FREE GUIDE: The Content Creator's AI Blueprint –* https://FirstMovers.ai/blueprint/ *The recursive loop just turned on — AI is ...

📺 Julia McCoy

👁️ 42K • 👍 2K • 💬 134 • ⏱️ 6:54 • 1d ago

---

**[Half The Internet Is AI Now...](https://www.youtube.com/watch?v=RaXx2aE9dyw)**

Hello guys and gals, it's me Mutahar again! The Internet is riddled now and over half of the traffic and soon to be websites and ...

📺 SomeOrdinaryGamers

👁️ 113K • 👍 6K • 💬 1K • ⏱️ 23:53 • 20h ago

---

**[AI is getting too realistic](https://www.youtube.com/watch?v=_kP2ax2tudk)**

How can you spot AI photos now that the new GPT Image 2 AI image model is really strong? I'm looking at background details, ...

📺 Jeremy Carrasco

👁️ 1.2M • 👍 93K • 💬 1K • ⏱️ 1:01 • 3d ago

---

**[Passive Income: I Tried AI Dropshipping For a Week (RAW RESULTS)](https://www.youtube.com/watch?v=rhuYy9LP72M)**

Get a FREE AI-built Shopify store: https://www.buildyourstore.ai/wv43 Try AutoDS here for just $1 - https://www.autods.com/il38 ...

📺 Mark Tilbury

👁️ 171K • 👍 11K • 💬 3K • ⏱️ 28:29 • 1d ago

---

**[Scott Galloway: AI Wasn’t Built For You. The Rich Don’t Need You Anymore!](https://www.youtube.com/watch?v=NdU6UdUKaYc)**

AI CEOs are selling us the dream of 'freedom', making billions off the fear of mass job loss! Scott Galloway reveals the truth is ...

📺 The Diary Of A CEO

👁️ 1.0M • 👍 26K • 💬 4K • ⏱️ 1:58:11 • 1d ago

---

**[These New AI Robots Just Got SCARY SMART… And Nobody’s Ready](https://www.youtube.com/watch?v=CQHvcJrC-zs)**

You won't BELIEVE what robots just pulled off this week — and it's genuinely terrifying how fast this is moving. AI robots are no ...

📺 The AI Nexus

👁️ 6K • 👍 152 • 💬 14 • ⏱️ 1:20:29 • 2d ago

---

**[AI Agents Bootcamp With Alicia Lyttle Day 2](https://www.youtube.com/watch?v=a78GxKFa73Y)**

Register officially for the Ai Agents Bootcamp: https://theaiagentsbootcamp.com/&el=Alicia-Lyttle-YouTube.

📺 Alicia Lyttle

👁️ 2K • 👍 180 • 7h ago

---

**[We Asked AI To Show America Without Republicans](https://www.youtube.com/watch?v=jtLMTEg3Hec)**

We asked AI to show an America without any Republicans.

📺 The Babylon Bee

👁️ 215K • 👍 21K • 💬 789 • ⏱️ 1:22 • 21h ago

---

**[&#39;AI psychosis&#39;: Spiralling into delusion using AI on ChatGPT &amp; Elon Musk&#39;s Grok - BBC World Service](https://www.youtube.com/watch?v=arx-sqtggdU)**

What happens when your conversations with AI become more real, more persuasive, than the world around you? Click here to ...

📺 BBC World Service

👁️ 11K • 👍 307 • 💬 78 • ⏱️ 14:45 • 21h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 631,499 • ❤️ 3,563 • 8d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 141,317 • ❤️ 1,290 • 13d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 15,024 • ❤️ 263 • 1d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 37,897 • ❤️ 222 • 3h ago

---

**[Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)**

*NVIDIA*

Nemotron-3 Nano Omni 30B is a multimodal LLM for enterprise Q&A, summarization, and document intelligence, capable of processing video, audio, image, and text inputs for use cases like customer service, media analysis, and GUI automation.

`any-to-any` `33.0B`

⬇️ 44,631 • ❤️ 239 • 7h ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 13,317 • ❤️ 437 • 7d ago

---

**[Laguna-XS.2](https://huggingface.co/poolside/Laguna-XS.2)**

*Poolside*

Laguna XS.2 is a 33B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring Sliding Window Attention and FP8 KV cache for efficient local execution on 36GB RAM. It supports native reasoning and is available under the Apache 2.0 license.

`text-generation` `33.4B`

⬇️ 12,027 • ❤️ 216 • 2d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,458,973 • ❤️ 1,123 • 11d ago

---

**[talkie-1930-13b-it](https://huggingface.co/talkie-lm/talkie-1930-13b-it)**

*talkie*

talkie-1930-13b-it is a 13B instruction-tuned language model trained on pre-1931 English text, excelling at generating responses in a vintage style for applications like historical chatbots or creative writing.

⬇️ 0 • ❤️ 233 • 12d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 3,262 • ❤️ 149 • 8d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 57 • 💬 3 • ⭐ 68,945 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 169 • 💬 10 • ⭐ 46,560 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 16 • 💬 3 • ⭐ 9,175 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 30 • 💬 3 • ⭐ 22,854 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,754 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 62,020 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,083 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Representation Fréchet Loss for Visual Generation](https://huggingface.co/papers/2604.28190)**

*Jiawei Yang, Zhengyang Geng, Xuan Ju et al. (5 authors)*

Fréchet Distance can be effectively optimized as a training objective when decoupling population size from batch size, leading to improved generator quality and alternative evaluation metrics.

▲ 24 • 💬 1 • ⭐ 339 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.28190) • [💻 code](https://github.com/Jiawei-Yang/FD-Loss)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 54,805 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 81 • 💬 6 • ⭐ 19,647 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.8k • 🔱 2.7k • 8d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 10.3k • 🔱 682 • 22h ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 8.0k • 🔱 1.2k • 6d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

`Python` `agent-workflows` `ai` `claude-code` `developer-tools` `diagrams`

⭐ 5.5k • 🔱 492 • 1d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 5.5k • 🔱 414 • 1h ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 5.0k • 🔱 359 • 1d ago

---

**[AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)**

Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch

`Python` `ai` `claude-code` `claude-code-skill` `knowledge-management` `obsidian`

⭐ 4.2k • 🔱 477 • 11d ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics & channel configuration (Telegram, Discord, Slack, WhatsApp)

`TypeScript` `agent` `ai-agent` `chat-ui` `chatbot` `claude`

⭐ 3.6k • 🔱 440 • 11h ago

---

**[alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)**

Hermes Agent 从入门到精通 · 橙皮书系列 · Nous Research 开源 AI Agent 框架实战指南

⭐ 3.5k • 🔱 369 • 14d ago

---

**[OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano)**

MOSS-TTS-Nano is an open-source multilingual tiny speech generation model from MOSI.AI and the OpenMOSS team. With only 0.1B parameters, it is designed for realtime speech generation, can run directly on CPU without a GPU, and keeps the deployment stack simple enough for local demos, web serving, and lightweight product integration.

`Python` `audio-tokenizer` `chinese` `english` `multi-modality` `multilingual`

⭐ 2.7k • 🔱 348 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
