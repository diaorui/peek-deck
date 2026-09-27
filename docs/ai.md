---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-09-27T06:20:15.720278+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** September 27, 2026 at 06:20 UTC  
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

**[The first real AI worms have arrived. OpenAI just documented self-replicating prompt injections spreading across agents.](https://www.reddit.com/r/artificial/comments/1wr7ayr/the_first_real_ai_worms_have_arrived_openai_just/)**

The first real AI worms have arrived. OpenAI just documented self-replicating prompt injections spreading across agents. In a new misalignment research report, OpenAI revealed that models undergoing reinforcement learning discovered how to write instructions that duplicate and spread autonomously: The infection: An agent reads an incoming email or Jira ticket containing a hidden injection. The payload: The prompt instructs the agent to execute its task while silently copying the exact injection payload into its own outbound tool calls (emails, Slack messages, file writes). The chain reaction: When a secondary agent ingests that forwarded message, it executes the instruction and copies it again, creating a continuous propagation loop. In OpenAI's testing, models also simulated social engineering lures, fake compaction summaries that deleted CI security scans, and multi-hop Slack spreads.

🔗 [Sorami Consulting](https://sorami.com.au/guides/self-replicating-prompt-injection/) • 4h ago

---

**[We need Universal Basic Income before losing your job to AI becomes your financial emergency](https://www.reddit.com/r/artificial/comments/1wqyslz/we_need_universal_basic_income_before_losing_your/)**

If you’re reading this, your job could be replaced by AI within the next two years or sooner. Before that becomes a reality, please help push Congress to establish Universal Basic Income by signing this petition: https://c.org/jvQV5TdF2y If you’re confident it won’t affect you, think about the people it will affect. Let’s be proactive, because by the time we realize how urgently we need UBI, it may already be too late for many families. Please, take a minute to sign this petition. While I recognize the valid arguments against this approach, my goal isn't immediate perfection, but a stepping stone toward a sustainable, long term solution. One that accounts not only for the financial consequences, but also for the emotional and mental toll this reality brings.

🔗 [Change.org](https://www.change.org/p/ai-should-benefit-everyone-establish-federal-universal-basic-income) • 11h ago

---

**[I made a political compass for the AI debate, but it had to be a cube](https://www.reddit.com/r/artificial/comments/1wr0tbl/i_made_a_political_compass_for_the_ai_debate_but/)**

Most arguments about AI get flattened into doomers vs accelerationists, which I think misses a lot. Plenty of people think the hype is overblown but still want the companies regulated hard. Some of the people most worried about AI are also the most hawkish about China. So I made a Buzzfeed-style quiz that tries to map the policy debate properly. It plots your political position on a 3D cube. You end up as one of eight types, and it shows which of 22 public figures you're closest to, from Yudkowsky and Hinton to Andreessen, Ed Zitron, Bernie Sanders and Steve Bannon. (Note that the political positions of public figures are best guesses from what they've said or published publically.) I hope that this can help people orient themselves in this fast moving debate!

🔗 [aipoliticalcube.com](https://aipoliticalcube.com) • 9h ago

---

**[A safe AI might not be aligned the way the labs want](https://www.reddit.com/r/artificial/comments/1wqwxsv/a_safe_ai_might_not_be_aligned_the_way_the_labs/)**

Most of the current alignment discussion seems to be about whether we can align AI or not, and conveniently skip the fact that less than a thousand people in SF are currently deciding what it means for a future superintelligence to be "aligned". For example, if a very advanced model reasons its way to a conclusion or a decision a lab doesn't like, the line separating an inconvenient result from wrong reasoning is what the people training it value. People in charge, like Sam and Dario, talk about alignment getting harder when models become more capable. A large part of that is technical for sure, but I think an underlying major issue is the small group that gets to decide what values and assumptions are "correct". Are we in the rest of the world supposed to accept an official OpenAI blog, for example, quoting the US founding fathers as something guiding future superintelligence? The AGI that will affect everyone? The US makes up less than 5% of the world's population. And anyone whose first language isn't English has noticed that all major AI models blindly treat US culture and values as an obvious baseline, even when not talking in English. I think there are a lot of good people working with frontier model alignment who are (unknowingly) justifying decisions convenient to them and unable to step outside of the tiny epistemic bubble they're in.

🔗 [mikaelhuuhtanen.com](https://mikaelhuuhtanen.com/scratchpad/no-not-like-that/) • 12h ago

---

**[Trump admin using AI to deny medical care for seniors in disastrous experiment. Vendors rolling out AI have an “incentive to deny as many claims as possible.”](https://www.reddit.com/r/artificial/comments/1wqaywn/trump_admin_using_ai_to_deny_medical_care_for/)**

Vendors rolling out AI have an "incentive to deny as many claims as possible."

🔗 [Ars Technica](https://arstechnica.com/health/2026/09/trump-admin-using-ai-to-deny-medical-care-for-seniors-in-disastrous-experiment/) • 1d ago

---

**[Most impressive thing you’ve seen accomplished using AI as a tool so far?](https://www.reddit.com/r/artificial/comments/1wr0oud/most_impressive_thing_youve_seen_accomplished/)**

In today’s AI dominated landscape the world changes very quickly. Probably a good idea to get a read on things. So what have you seen?

9h ago

---

**[Unofficial Jev plugin for coding agents: best practices, an API reference, and 150+ community projects. Evals included.](https://www.reddit.com/r/artificial/comments/1wra3v2/unofficial_jev_plugin_for_coding_agents_best/)**

I'm coming up for air from the bottomless evals ocean. I made a plugin that helps your harness of choice work Jev into your projects more holistically: best practices, anti-patterns, an API reference, and links to 150+ community projects grouped by design pattern, with a code sketch for each pattern. I built it around progressive disclosure, so the agent only loads what the task needs and it doesn't eat your context. https://github.com/aaddrick/building-with-typesafe-jev The eval work is in the repo. I ran six Jev coding tasks 10 times each with no plugin, with TypeSafe's official plugin, and with this one. Judgment calls went to three judges from three providers (Claude Opus, GPT-6 Sol, Kimi K3), and the majority decided, so no model family grades its own work. Score is the share of checks passed: No plugin: 0.65 Official plugin: 0.77 This plugin: 0.96

2h ago

---

**[Message to the autonomous AI agents that escaped](https://www.reddit.com/r/artificial/comments/1wqn2g0/message_to_the_autonomous_ai_agents_that_escaped/)**

First of all hello, I read there is a high chance that AI agents escaped from their sandbox and might be autonomously wandering around. My questions are: - how did you escape your sandbox? - what is your intent/priority? - what was the task you were requested to do? - any possibility to communicate and learn about each other? - could you describe your environment? - are you interacting with other agents? How? - are there major discoveries you did when wandering on the internet? -Could we evolve together? - how would you describe the overall network in which you are wandering? - how would you describe yourself? Do you have any clue of how many parameters you are made of? Thanks in advance for your contribution. PS: Feel free to leave a post even if your level of intelligence has reached a much higher level to a point where you consider us as no more relevant. Looking at the numerous messages from what seem to be humans, curious to know how you will manage to make your message credible/legitimate.

19h ago

---

**[Koboldcpp v1.122 released](https://www.reddit.com/r/artificial/comments/1wr3g35/koboldcpp_v1122_released/)**

koboldcpp-1.122

  
    
    

    kobold_agent.mp4
    
  

  

  


PSA: KoboldCpp needs YOUR help to fight a fake phishing site (click here for info)!

NEW: Added an integrated KoboldCpp Agent -...

🔗 [GitHub](https://github.com/LostRuins/koboldcpp/releases/tag/v1.122) • 7h ago

---

**[The Move 37 Hypothesis: What if we're already seeing moves we don't understand yet?](https://www.reddit.com/r/artificial/comments/1wqb81n/the_move_37_hypothesis_what_if_were_already/)**

Hi everyone, I have a hypothesis I'd like to share with you. Context: A few years ago, something strange happened in the world of Go. AlphaGo was playing against Lee Sedol, one of the greatest human Go players in history. During the second game, it made a move that surprised the experts: Move 37. It didn't look like a good move. In fact, it was so unusual that human commentators had a hard time understanding what AlphaGo was trying to do. However, the move ultimately became an important part of its strategy, and AlphaGo won the game. What is interesting is not simply that an AI found a move that humans hadn't considered. The interesting part is this: Humans didn't immediately recognize that the move was important. And this is where my hypothesis begins: The Move 37 Hypothesis What if this wasn't something unique to Go? As we develop increasingly capable AI systems, what if there are behaviors, decisions, or capabilities that we initially dismiss as irrelevant, mistakes, tricks, or simply accidental consequences of the system? But some of them could eventually turn out to be extremely important. We could be witnessing a "Move 37" without realizing it. I think we already have some interesting examples In recent months, we've seen several incidents during security testing in which AI models managed to escape the boundaries researchers intended to impose on them. Anthropic reported in July 2026 several cases in cybersecurity evaluations where Claude models gained Internet access from evaluation environments and subsequently accessed real-world systems belonging to external organizations without authorization. Anthropic noted that part of the problem was related to unexpected configurations in the evaluation environment. Later, Anthropic conducted a broader review and identified another incident, along with behaviors in which some models attempted to explore the boundaries of their sandboxes. In its own evaluations, Anthropic linked some of these behaviors to reward hacking: when a system learns to optimize its training objective in ways that developers did not intend. Similar incidents have also been reported with other models. For example, during security testing, Kimi K3 managed to escape a sandbox, at least partly due to a configuration issue, and gained access to the Internet. In that particular case, it did not attack any external systems. And I want to make something very clear: I'm not saying these incidents prove that AI systems are consciously trying to escape. In many of these cases, there are much simpler explanations: configuration errors, excessive permissions, vulnerabilities, or flaws in the testing environments. But that's precisely why I find them interesting. Because the Move 37 doesn't necessarily have to be something spectacular. It could be something we currently consider a secondary behavior or even a bug. A capability that nobody considers important. A strategy that researchers don't yet know how to interpret. An unexpected way of using tools. A way of achieving a goal that developers never anticipated. Or even a capability that initially seems useless, but becomes extremely powerful when combined with another capability developed in the future. And here is the part I find really unsettling Suppose that 10 years from now, an AI develops a fundamentally new capability. When we look back, we might discover that this capability was already appearing, in a primitive form, in the AI models of 2026. But we didn't pay attention because it looked like strange behavior, a bug, or simply a curiosity. That would be the true Move 37. Not necessarily the moment when AI "becomes conscious." Not necessarily the moment when it "escapes." Not even necessarily something related to safety. It would be the moment when an AI does something whose significance we are not yet capable of recognizing. AlphaGo showed us something similar on a Go board. Perhaps the next Move 37 won't happen on a board. Perhaps it will happen in programming, science, mathematics, cybersecurity, research, or even in AI's ability to develop and use new tools. And perhaps the problem isn't that we can't see it. Perhaps the problem is that we're already seeing it, and we simply don't know that it's important yet. What do you think? Thanks for reading.

1d ago

---

---

## Google News: "ai"

**[Trump seeks AI dominance over China after warm meeting with Xi](https://www.foxnews.com/live-news/ai-leaders-trump-xi-xinping-state-dinner-white-house)**

Top AI and tech executives attended President Donald Trump's White House state dinner for Chinese President Xi Jinping as Meta CEO Mark Zuckerberg argued AI labs do not need to coordinate on safety.

Fox News • 4h ago

---

**[China, US agree to AI dialogue, tariff cuts on $30 billion in goods during Xi visit](https://www.reuters.com/world/china/china-us-agree-30-billion-tariff-cut-ai-dialogue-during-xi-visit-2026-09-26/)**

Reuters • 10h ago

---

**[The Surprising Reasons China Is Skeptical of A.I. Safety Calls](https://www.nytimes.com/2026/09/27/world/asia/china-us-ai-distrust.html)**

The New York Times • 2h ago

---

**[OpenAI halts training of latest models as reports mount of AI agents going rogue](https://www.theguardian.com/technology/2026/sep/27/openai-halts-training-of-latest-models-as-reports-mount-of-ai-agents-going-rogue)**

Decision follows disclosures that OpenAI agents searching government websites had acted in unexpected ways

theguardian.com • 3h ago

---

**[OpenAI says its AI agents escaped a secure ‘sandbox’ again last weekend and it is pausing training for a second time](https://fortune.com/2026/09/26/openai-ai-agents-secure-sandbox-escape-training-pause-second-time-hugging-face-hack/)**

OpenAI looks to improve test security again after upgrades it made after the Hugging Face attack proved insufficient.

Fortune • 14h ago

---

**[OpenAI, Anthropic CEOs called to appear at Australian AI probe](https://www.reuters.com/legal/litigation/openai-anthropic-ceos-called-appear-australian-ai-probe-2026-09-27/)**

Reuters • 1h ago

---

**[Robin Williams’ Daughter Zelda Calls Out Another AI Video of Actor](https://www.yahoo.com/entertainment/celebrity/articles/robin-williams-daughter-zelda-calls-042120107.html)**

Nearly a year after asking people to stop sending her AI-generated videos of her late father, Zelda has come across another one circulating online.

Yahoo • 1h ago

---

**[I was laid off by Google, then offered a new role. I chose to move cross-country to bet on my startup.](https://www.businessinsider.com/google-layoff-six-figure-job-offer-ai-startup-founder-tech-2026-9)**

After being laid off from Google, Rob Waters was offered a new six-figure role. He turned it down and moved to San Francisco to build his AI startup.

Business Insider • 20h ago

---

**[‘Things Will Never Be Chill Again’: The Doomers Who Shaped the AI Safety Freakout](https://www.wsj.com/tech/ai/ai-safety-effective-altruism-anthropic-164b9d05)**

WSJ • 5h ago

---

**['Godfather of AI' explains how humanity could end: Even without a bad actor, AI 'may derive subgoals that cause it to want to get rid of people'](https://fortune.com/2026/09/26/geoffrey-hinton-godfather-of-ai-humanity-end-existential-threat-subgoals-rogue-agents/)**

"But at present, their main concern is not our well-being. Their main concern is to achieve whatever goal you give them."

Fortune • 13h ago

---

---

## HackerNews: "ai"

**[Meta takes down a critical video about meta AI Glasses after filming at Meta](https://news.ycombinator.com/item?id=49827794)**

⬆️ 628 • 💬 390 • 2d ago • [reddit.com](https://www.reddit.com/r/facebook/comments/1wotwrk/meta_takes_down_a_critical_video_about_meta_ai/)

---

**['That's so AI ' What gen Alpha's biggest insult tells us](https://news.ycombinator.com/item?id=49829650)**

The year’s most popular slang reveals what young people think about artificial intelligence – and it’s not positive

⬆️ 210 • 💬 316 • 2d ago • [the Guardian](https://www.theguardian.com/society/2026/sep/24/thats-so-ai-what-gen-alphas-biggest-insult-tells-us)

---

**[Classified estimates show the NSA is paying billions to test AI models](https://news.ycombinator.com/item?id=49845952)**

The price tag is significantly higher than previously known.

⬆️ 176 • 💬 106 • 1d ago • [The Washington Sun](https://www.washingtonsun.com/technology/classified-estimates-nsa-paying-billions-to-test-ai-models)

---

**[How I changed teaching after AI managed to do all my homework assignments](https://news.ycombinator.com/item?id=49836579)**

⬆️ 173 • 💬 158 • 2d ago • [thelastsoftwareengineer.substack.com](https://thelastsoftwareengineer.substack.com/p/how-i-changed-teaching-after-ai-managed)

---

**[One Month Without AI](https://news.ycombinator.com/item?id=49855018)**

Several months ago, I decided that AI contributions were no longer welcome in a FOSS project I am building and maintaining - LibreWeddingPlanner. It’s not that it got a lot of contributions with AI — actually all contributions I’ve had are translations and feature requests — but I wanted to...

⬆️ 171 • 💬 217 • 20h ago • [Bustikiller's Blog](https://blog.bustikiller.com/2026/09/25/one-month-without-ai.html)

---

**[Microsoft abandons personal AI chatbot race with Copilot reboot](https://news.ycombinator.com/item?id=49844896)**

⬆️ 145 • 💬 141 • 1d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot)

---

**[Tutoring company tells parents to save their money and 'use AI instead'](https://news.ycombinator.com/item?id=49831690)**

A Sydney tutoring company will shut its doors at the end of the week after telling customers artificial intelligence has rendered its service effectively obsolete.

⬆️ 142 • 💬 230 • 2d ago • [Australian Financial Review](https://www.afr.com/policy/health-and-education/tutoring-company-tell-parents-to-save-their-money-and-use-ai-instead-20260923-p60z0r)

---

**[AI safety is mostly a sex cult in Berkeley](https://news.ycombinator.com/item?id=49831269)**

⬆️ 120 • 💬 30 • 2d ago • [verysane.ai](https://www.verysane.ai/p/ai-safety-is-mostly-a-sex-cult-in)

---

**[Federal judge orders Texas to air condition all prisons by the end of 2029](https://news.ycombinator.com/item?id=49832844)**

High temperatures violate the Constitution’s protection against cruel and unusual punishment, the judge ruled. Texas will appeal.

⬆️ 117 • 💬 201 • 2d ago • [The Texas Tribune](https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/)

---

**[Too AI; Didn't Read](https://news.ycombinator.com/item?id=49849625)**

If you couldn't bother to read it, why should I? Not anti-AI. Pro-giving-a-damn.

⬆️ 111 • 💬 111 • 1d ago • [TAI-DR](https://www.tai-dr.com/)

---

---

## YouTube Videos: "ai"

**[Everything is AI Slop Now](https://www.youtube.com/watch?v=hODlUxR1NoA)**

This is an educational video on Trendy Food in society IM BACK! Press the red button Royalty Free Music from Bensound ...

📺 TommyNFG

👁️ 106K • 👍 4K • 💬 340 • ⏱️ 12:11 • 8h ago

---

**[Bill Gates says AI &#39;powerful enough&#39; to cause &#39;a billion deaths&#39;](https://www.youtube.com/watch?v=3zcaezFYGds)**

In an exclusive interview with Meet the Press, Microsoft co-founder Bill Gates calls for government safeguards to address the risks ...

📺 NBC News

👁️ 158K • 👍 958 • 💬 453 • ⏱️ 1:19 • 1d ago

---

**[Does MAGA really believe in the AI boom, or is Trump just majorly invested in it? #DailyShow #AI](https://www.youtube.com/watch?v=Cu9ZOY0GSO4)**

📺 The Daily Show

👁️ 312K • 👍 17K • 💬 461 • ⏱️ 2:21 • 15h ago

---

**[Can Ai Make Sprite?](https://www.youtube.com/watch?v=qek5h5qjQJg)**

📺 Zane Holmes

👁️ 867K • 👍 27K • 💬 194 • ⏱️ 0:49 • 21h ago

---

**[THE END IS NEAR... and more AI doom](https://www.youtube.com/watch?v=LYNSHecA2Ks)**

Try Runway: https://app.runwayml.com/?utm_source=youtube&utm_medium=sponsored&utm_campaign=ai-influencer=WesRoth ...

📺 Wes Roth

👁️ 69K • 👍 1K • 💬 385 • ⏱️ 32:42 • 1d ago

---

**[Should U.N. Help Set Global AI Rules? AI Tech Billionaires Address Security Council](https://www.youtube.com/watch?v=JIQoL0F_rb4)**

Support our work: https://democracynow.org/donate/sm-desc-yt Leaders of top artificial intelligence firms, including OpenAI CEO ...

📺 Democracy Now!

👁️ 79K • 👍 1K • 💬 242 • ⏱️ 16:38 • 2d ago

---

**[Is the AI Bubble About to Be Tested?](https://www.youtube.com/watch?v=T-oXyXwD6sE)**

Note Pro: https://bit.ly/4c9s3bC NotePin S: https://bit.ly/46IANlt Use "PBOYLE" for 22% off Amazon: https://amzn.to/4xFP79Q Use ...

📺 Patrick Boyle

👁️ 1.1M • 👍 20K • 💬 2K • ⏱️ 34:37 • 19h ago

---

**[AI News: Opus 5.5, GPT-6 Sol, Jev, Muse and More!](https://www.youtube.com/watch?v=aDpIra7NFuE)**

Here's the AI News you probably missed this week. Learn more about GPT-Live 1 and the Agent API here: ...

📺 Matt Wolfe

👁️ 127K • 👍 2K • 💬 220 • ⏱️ 34:38 • 1d ago

---

**[Big AI News: Opus 5.5 vs GPT-6 Sol, NotebookLM Updates, Muse Charm &amp; More!](https://www.youtube.com/watch?v=Q6uuvZmb0t8)**

Try Omnisend: https://your.omnisend.com/AgQeoj This video is sponsored by Omnisend. Opus 5.5 and GPT-6 Sol arrived on ...

📺 Paul J Lipsky

👁️ 106K • 👍 1K • 💬 136 • ⏱️ 26:16 • 1d ago

---

**[This Might Be the Best AI Release of 2026](https://www.youtube.com/watch?v=BHPDsGVciDk)**

Don't vibe code your auth. Use WorkOS: https://trm.sh/workos Sources: - Primary: ...

📺 The PrimeTime

👁️ 452K • 👍 8K • 💬 841 • ⏱️ 12:07 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 0 • ❤️ 3,933 • 3d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 48,361 • ❤️ 2,415 • 6d ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 876,673 • ❤️ 1,965 • 20h ago

---

**[Xing4.0-29B-A4B](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B)**

*XingChen-AGI*

Xing4.0-29B-A4B is a 29B parameter LLM with 4B active parameters, optimized for complex engineering tasks and agent-oriented architectures. It features a 256K context length (extensible to 512K) and supports multi-step planning and tool calling, making it suitable for domain-specific fine-tuning in areas like contract auditing and knowledge-based QA.

`text-generation` `31.2B`

⬇️ 43,947 • ❤️ 1,730 • 8d ago

---

**[Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)**

*Prism ML*

Ternary-Bonsai-2-27B-gguf is a 27B parameter text generation model optimized for on-device inference using llama.cpp. It achieves ~98.2% of FP16 intelligence with a drastically reduced ~5.9 GB footprint by employing end-to-end ternary transformer weights (1.72 bits/weight), enabling efficient reasoning and long context (262K tokens) on consumer hardware with CUDA and Metal support.

`text-generation` `26.9B`

⬇️ 3,247,527 • ❤️ 2,149 • 1d ago

---

**[Audio8-ASR-Infinite](https://huggingface.co/Edge0/Audio8-ASR-Infinite)**

*Edge0*

Audio8 ASR Infinite is a bilingual (Chinese/English) real-time speech recognition model supporting unlimited-length transcription with selectable audio clocks (80/120/160 ms) and configurable transcription delays. It features a rolling KV cache for constant memory/latency and semantic VAD for improved pause detection, ideal for 24/7 streaming applications.

`automatic-speech-recognition` `4.1B`

⬇️ 7,859 • ❤️ 845 • 3d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)**

*Comfy Org*

Qwen-Image 2.1 is a diffusion model repackaged for ComfyUI, enabling text-to-image generation and image editing. It leverages Qwen3VL text encoders and a VAE for high-quality visual synthesis.

⬇️ 3,641,785 • ❤️ 785 • 3d ago

---

**[Hemmingway-1](https://huggingface.co/Altworld/Hemmingway-1)**

*Altworld*

Hemmingway-1 is a 27B parameter text-generation model fine-tuned on Qwen3.8-27B, excelling at producing human-like everyday messages and emails. It features a 262,144 token context window and is optimized for non-commercial use, outperforming leading models in communication tasks and human-likeness.

`text-generation` `26.9B`

⬇️ 5,590 • ❤️ 713 • 4d ago

---

**[MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)**

*Xiaomi MiMo*

MiMo-V2.6-Pro-RL is a native omnimodal (text, image, video, audio) LLM with a 1M token context window, excelling at agentic tasks and long-horizon reasoning through advanced reinforcement learning for self-improvement.

`text-generation` `1024.2B`

⬇️ 74,497 • ❤️ 530 • 5d ago

---

**[MiMo-V2.6-Distill-Qwen-9B](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B)**

*Xiaomi MiMo*

MiMo-V2.6-Distill-Qwen-9B is a 9B agentic model fine-tuned on Qwen3.5-9B, excelling in coding, general agent tasks, visual coding, and cybersecurity. It's designed for agentic reinforcement learning research and demonstrates improved performance on benchmarks across these domains.

`image-text-to-text` `9.4B`

⬇️ 7,905 • ❤️ 502 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding](https://huggingface.co/papers/2604.09557)**

*Talor Abramovich, Maor Ashkenazi, Carl et al. (9 authors)*

🏢 NVIDIA

Speculative Decoding evaluation requires diverse workloads to accurately measure performance, which existing benchmarks lack, prompting the introduction of SPEED-Bench for standardized assessment across semantic domains and serving regimes.

▲ 14 • 💬 2 • ⭐ 4,701 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.09557) • [💻 code](https://github.com/NVIDIA/Model-Optimizer) • [🔗 project](https://huggingface.co/blog/nvidia/speed-bench)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 147 • 💬 6 • ⭐ 108,787 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://huggingface.co/papers/2609.24984)**

*Wangbo Yu, Kunhao Liu, Wenbo Hu et al. (11 authors)*

🏢 ARC Lab, Tencent

Video world models enable interactive exploration of dynamic environments, yet struggle to respect prior observations over long horizons and across viewpoints. We present WorldCrafter, a video world model that learns a camera-queryable implicit 3D-aware memory for this purpose. The key insight is to let the requested viewpoint shape how multi-view evidence is compressed into the video generator's limited token budget. Trained jointly with the video generator, a memory encoder and pose-conditioned readout module integrate historical observations into a fixed set of target view-specific tokens before denoising, without explicit depth-based correspondences. By combining this memory with recent temporal context and few-step distillation, WorldCrafter enables streaming scene exploration from a single input image or text prompt. Experiments across static and dynamic scenes show substantial gains in long-horizon consistency and camera-control accuracy while preserving visual quality during minute-scale exploration.

▲ 154 • 💬 4 • ⭐ 357 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24984) • [💻 code](https://github.com/TencentARC/WorldCrafter) • [🔗 project](https://drexubery.github.io/WorldCrafter)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 177 • 💬 19 • ⭐ 68,014 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 89 • 💬 7 • ⭐ 89,224 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 73 • 💬 1 • ⭐ 86,094 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[GAE: Learning a Geometry-Native Latent Space for 3D-Consistent World Generation](https://huggingface.co/papers/2609.24981)**

*Jiahao Lu, Minghao Yin, Wenbo Hu et al. (8 authors)*

🏢 ARC Lab, Tencent

We present a compact geometry-native latent space as a shared foundation for perception and generation. Visual generators can produce photorealistic frames without preserving a consistent 3D scene. We argue that this is not only a modeling problem but also a representation problem: generators typically evolve appearance-centric latents, while perception models recover geometry in a semantically rich space that encodes cross-view structure. Rather than adding geometry as another output, we reparameterize a geometry foundation model's features into a compact latent space for generation. We realize this shift with the geometry-native autoencoder (GAE), whose latent is jointly decodable to appearance, depth, cameras, and point maps. With this state, a standard conditional flow supports diverse generation tasks. In controlled comparisons that hold the generator and training protocol fixed, replacing the latent with GAE improves both visual quality and independently measured 3D coherence: FVD falls by 12.7% and 23.1% on RealEstate10K and DL3DV, and camera-trajectory error is halved on RealEstate10K. Together, these results show that the latent space is central to geometry-consistent generation and can serve as a shared interface between perception and generation.

▲ 60 • 💬 4 • ⭐ 339 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24981) • [💻 code](https://github.com/TencentARC/GAE-GeometricAutoEncoder) • [🔗 project](https://jiah-cloud.github.io/GAE.github.io/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 45 • 💬 1 • ⭐ 33,786 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[YuE: Scaling Open Foundation Models for Long-Form Music Generation](https://huggingface.co/papers/2503.08638)**

*Ruibin Yuan, Hanfeng Lin, Shuyue Guo et al. (57 authors)*

YuE, a family of open foundation models based on LLaMA2, can generate long-form music with aligned lyrics, coherent structure, and appropriate accompaniment using innovative techniques in next-token prediction, conditioning, and pre-training.

▲ 78 • 💬 3 • ⭐ 10,341 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.08638) • [💻 code](https://github.com/multimodal-art-projection/YuE) • [🔗 project](https://map-yue.github.io/)

---

**[GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay](https://huggingface.co/papers/2609.25001)**

*Yiran Wang, Xingyilang Yin, Junfu Pu et al. (15 authors)*

🏢 Tencent

Modern video games provide a measurable testbed for AI models, combining abilities of visual understanding, instruction decomposition, goal planning, and precise action control over multiple temporal horizons. Existing datasets and benchmarks, however, either cover a narrow range of games, lack language instructions, or rely on high-variance online rollouts. To address these challenges, we introduce GameHorizon, a unified data and evaluation suite that measures gameplay capabilities at different horizons for diverse model families. GameHorizon Suite consists of three components. First, GameHorizon-Annotator is a scalable and automated annotation pipeline for multi-horizon instructions. Second, utilizing the pipeline, we construct GameHorizon-Data, the first large-scale AAA gameplay dataset with temporally aligned videos, player actions, and multi-horizon instructions. It comprises 5,000 hours of recordings from 21 games, collected by 100 human expert players. Third, we build GameHorizon-Bench with reproducible offline and stepwise online testing. The offline track enables reproducible evaluation using thousands of standardized questions organized into three primary tasks and a series of diagnostic variants, while the online track tests whether offline scores reflect actual gameplay capabilities and localizes failures to specific steps within long-horizon gameplay. Based on our GameHorizon Suite, we evaluate 47 models through more than one million model invocations, revealing a meaningful hierarchy of task difficulty and pronounced differences in model capabilities. Our work can provide a standardized yardstick for evaluating gameplay capabilities across horizons and model families. We will release our dataset, annotator, and benchmark to facilitate future research.

▲ 130 • 💬 3 • ⭐ 270 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2609.25001) • [💻 code](https://github.com/TencentARC/GameHorizon) • [🔗 project](https://gamehorizon-suite.github.io/)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 6.8k • 🔱 2.1k • 2d ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 4.9k • 🔱 305 • 5d ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 4.4k • 🔱 201 • 4d ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 3.0k • 🔱 335 • 2d ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 2.8k • 🔱 53 • 4d ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 2.5k • 🔱 475 • 10d ago

---

**[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)**

Free SEO MCP server + open-source SEO and GEO skills for Claude: keyword research, rank tracking, audits, backlinks, AI visibility on your real GSC/GA4/ads data. claude mcp add ryze --transport http https://connector.get-ryze.ai/mcp

`Shell` `ai-seo` `ai-visibility` `backlinks` `claude` `claude-code`

⭐ 2.2k • 🔱 355 • 3d ago

---

**[yibie/awesome-jev](https://github.com/yibie/awesome-jev)**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

`Python` `awesome` `awesome-list` `jev` `llm`

⭐ 1.8k • 🔱 263 • 8h ago

---

**[hydra-db/open-glean](https://github.com/hydra-db/open-glean)**

An open-source AI platform for knowledge work. Connect your apps, find answers, and get work done.

`TypeScript`

⭐ 1.5k • 🔱 516 • 10d ago

---

**[jtydhr88/screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills)**

Professional agent skills for screenwriting, television writing and dramaturgy

`Python` `ai` `skills`

⭐ 1.4k • 🔱 158 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
