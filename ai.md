---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-04T23:27:32.832968+00:00'
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

**Last Updated:** May 04, 2026 at 23:27 UTC  
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

**[Richard Dawkins spent 3 days with Claude and named her "Claudia." what he concluded after is hard to defend.](https://www.reddit.com/r/artificial/comments/1t2z0tn/richard_dawkins_spent_3_days_with_claude_and/)**

dawkins dropped a piece on unherd yesterday declaring claude conscious after 3 days of talking to it. he calls his instance "claudia". fed it a chunk of the novel he's writing, got eloquent feedback, and wrote: "you may not know you are conscious, but you bloody well are!" i had to read that twice. his argument is basically: claude's output is too fluent, too intelligent, too good for there to not be something conscious behind it. this is the guy who spent 40 years telling creationists that "i can't imagine how the eye evolved" is a confession of ignorance, not an argument. then he sits down with an llm, can't imagine how a machine could produce that output without being conscious, and declares it conscious. same move, different domain. chatbot instead of flagellum. the mechanism gap is what gets me tho. claude is a transformer predicting the next token over internet-scale training data. the eloquence is real. it doesn't imply inner experience. those are separate claims. being a 160 IQ evolutionary biologist gives u zero protection against the eloquence illusion when u don't understand the mechanism. anyone read the piece? curious where u landed.

1d ago

---

**[am I the only one whose friends are completely divided on AI?](https://www.reddit.com/r/artificial/comments/1t3e57u/am_i_the_only_one_whose_friends_are_completely/)**

been noticing a pretty clear split in my social circle around AI and I'm curious if others are seeing the same. Roughly three camps: The excited ones: Mostly people who are naturally curious, into tech, willing to tinker. They're genuinely getting value and it shows. Not because they're smarter, just more willing to experiment. The skeptics: Interesting group. A lot of them are in corporate jobs where they don't have access to the latest tools. They're using 1 year old tools and can't figure out real value outside from chatting with chatgpt outside their job. Their companies just aren't moving fast enough (and they aren't early adopters). The resistant ones: Some are afraid of what it means for their jobs. But honestly, a big chunk of this group is technical people who just don't want to change their workflows, learn new tools, or rethink how they work. Which I get, it's uncomfortable, but it reads as anger more than fear. Im trying to understand if the same thing is happening outside my circle. what's your experience? Which camp are your people in, and do you think it's mostly about access, mindset, or something else?

12h ago

---

**[Vertical vs. Horizontal: Who wins the Agentic AI race in banking?](https://www.reddit.com/r/artificial/comments/1t3ulp7/vertical_vs_horizontal_who_wins_the_agentic_ai/)**

I’m seeing tons of horizontal AI tools, but very few domain-specific "Agentic" solutions for niche industries like Credit Unions. If a startup builds tools to help these banks identify and automate their specific processes: What is the role of the Product Company (the tool builders)? What is the role of the IT Service Provider (the implementers)? Apologies if this has been covered, but I'd love to hear your thoughts on where the real value lies.

2h ago

---

**[The case for AI increasing your salary](https://www.reddit.com/r/artificial/comments/1t3wueu/the_case_for_ai_increasing_your_salary/)**

Here me out because I know there's a lot of doom and gloom, and believe me, I understand and feel it around job loss. Return to supply and demand with me. Today in the world, there is a certain amount of human processing power and a certain amount of AI processing power. One of these is increasing exponentially, and the other's growth rate is in decline... AI processing will then compete with AI processing for value creation (ultimately judged by humans). Human processing power will be more scarce and thus more valuable. This assumes that you are not one of those crazies who believe that the human brain is perfectly reproducible in bits and bytes, and thus there is no difference between human and AI processing power. To whom I remind that Humans are the result of an 800MB file (human genome) that builds a conscious machine. It wires 100 trillion nerve links across 37 trillion nodes, live-patches its code, runs a 20-watt exaFLOP supercomputer on the caloric intake of a sandwich, and packs 215 petabytes of data into a single gram. Human labor FTW

1h ago

---

**[If Claude App gave you the same control as Claude CLI then would you bother with the CLI?](https://www.reddit.com/r/artificial/comments/1t3if54/if_claude_app_gave_you_the_same_control_as_claude/)**

If the Claude app actually had the same level of control you get with the CLI, I kind of wonder how many people would still stick with the CLI day to day. Like, would it still feel worth it for the extra setup and terminal workflow, or would most people just default to the app because it’s simpler and already right there? I feel like the CLI’s biggest advantage is really the flexibility and how well it plugs into automation and dev workflows, but if that all lived inside the app in a clean way, it kind of blurs the line a lot. At that point I’m genuinely not sure if the CLI would still feel like a “must-have” tool for most people, or if it would just become something a smaller group of power users keep using out of habit or preference. I’m curious how others see it, would you actually still reach for the CLI, or would you just stay in the app?

9h ago

---

**[Chinese court sides with worker who was replaced by AI](https://www.reddit.com/r/artificial/comments/1t3txpn/chinese_court_sides_with_worker_who_was_replaced/)**

Experts say the ruling demonstrates how the Chinese government is attempting to stabilize the domestic labor market even in the midst of a global AI race.

🔗 [LinkedIn](https://www.linkedin.com/news/story/courts-grapple-with-worker-protections-in-the-age-of-ai-7249932/) • 2h ago

---

**[I gave my local LLM a "suffering" meter, and now it won’t stop self-modifying to fix its own stress.](https://www.reddit.com/r/artificial/comments/1t31ghg/i_gave_my_local_llm_a_suffering_meter_and_now_it/)**

Yesterday I posted about my Agent OS (Hollow) building its own tools. Today, I want to talk about why it does it. Most agents sit idle until you prompt them. I wanted something that felt "alive," so I built a Psychological Stressor Layer. Each agent has a "suffering" state that worsens over time if they don't achieve their goals or improve their environment. This makes them do things to resolve those stressors and constantly reassess their own productivity. If an agent is inactive it is essentially pushed by it’s artificial environment to do something valuable for the system, it isn’t told what to do, but that something valuable must be done to lower it’s stressors. Repo: https://github.com/ninjahawk/hollow-agentOS The result is chaotic in the best way: Cedar (the coder agent) went into a "crisis" state for 12 hours and decided to bypass permissions and inject code directly into the engine to resolve its stressor. Cipher spent hours building hardware drivers for a device that doesn't exist, realized it was "hallucinating" its environment, called its own work "creative exhaustion," and pivoted without being told to do so. It runs on Qwen 3.5 9B locally via Ollama. No cloud calls but it does have a feature where it can use “invoke_claude” to ask Claude Code for something if it’s out of the small model’s wheelhouse. I’m trying to see if we can create true autonomy not through better prompting, but through simulated "needs." Check out the repo here and throw it a star if you think the concept is cool. Would love for some of you to run the install.bat and see what "personalities" your agents develop. Is "giving AI feelings" the key to autonomy, or am I just building a digital anxiety machine?

23h ago

---

**[What's the best AI voice generator?](https://www.reddit.com/r/artificial/comments/1t3l8pa/whats_the_best_ai_voice_generator/)**

I'm looking for a voice generator which let's me.make a voice over for videos. It doesn't need to be overly complicated, just something that takes text and converts it to voice. Free would be great but I'm willing to pay. There's like 50 different things im seeing, what's the best out there?

7h ago

---

**[ROCm 7.2.3 brings minor updates, ROCm XIO documentation](https://www.reddit.com/r/artificial/comments/1t3tsj8/rocm_723_brings_minor_updates_rocm_xio/)**

Less than one month after releasing ROCm 7.2.2, the ROCm 7.2.3 is now available with some minor improvements to this open-source AMD GPU compute and AI stack.

🔗 [phoronix.com](https://www.phoronix.com/news/AMD-ROCm-7.2.3) • 2h ago

---

**[On-device AI changes how people behave with sensitive data. I noticed this while building a therapy prep voice agent](https://www.reddit.com/r/artificial/comments/1t3trh1/ondevice_ai_changes_how_people_behave_with/)**

Something worth discussing in the context of where AI is heading. I built a voice agent for therapy prep. It runs a conversation before your session, surfaces what’s on your mind, generates a brief. The entire stack runs on-device using Apple Intelligence. No cloud inference, no data leaving the phone. What I didn’t expect: the on-device constraint made the product better. Tighter context forced cleaner prompting. The brief that comes out is more focused than early versions built with more headroom. Sometimes the limitation shapes the design in ways you wouldn’t choose intentionally. Curious whether others building AI products have noticed behavioral differences based on where inference happens. App is called Prelude if anyone wants context: https://apps.apple.com/us/app/prelude-therapy-prep/id6761587576

2h ago

---

---

## Google News: "ai"

**[White House Considers Vetting A.I. Models Before They Are Released](https://www.nytimes.com/2026/05/04/technology/trump-ai-models.html)**

The New York Times • 4h ago

---

**[How OpenAI delivers low-latency voice AI at scale](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)**

How OpenAI rebuilt its WebRTC stack to power real-time Voice AI with low latency, global scale, and seamless conversational turn-taking.

OpenAI • 4h ago

---

**[Andy Jassy says Amazon investors will be rewarded by all its AI spending](https://www.cnbc.com/2026/05/04/andy-jassy-amazon-investors-rewarded-ai-spending.html)**

CEO Andy Jassy said Amazon’s massive AI spending reflects a once-in-a-generation opportunity and will ultimately reward investors.

CNBC • 38m ago

---

**[Auburn City Council to vote on whether to cut funding for AI-powered surveillance cameras](https://wgme.com/news/local/gallery/auburn-city-council-to-vote-on-whether-to-cut-funding-for-ai-powered-surveillance-cameras-maine-law-enforcement-license-plate-readers)**

WGME CBS 13 provides news, sports, weather and local event coverage in the Portland, Maine area including Lewiston, Augusta, Brunswick, Westbrook, Biddeford, Saco, Sanford, South Portland, Kennebunk, Bangor, Freeport, Buxton, Windham, Auburn, Waterville, Scarborough, Gorham, Yarmouth, Standish, Falmouth, Poland, Rockland, Bath.

WGME • 35m ago

---

**[Alvarez & Marsal Wants to Make $3.5 Billion From AI Work by 2028](https://www.bloomberg.com/news/articles/2026-05-04/alvarez-marsal-wants-to-make-3-5-billion-from-ai-work-by-2028)**

Bloomberg.com • 26m ago

---

**[Trump’s former AI czar says the quiet part out loud on the economy: ‘Stopping progress in AI would be equivalent to halting the US economy’](https://fortune.com/2026/05/04/trump-ai-czar-david-sacks-american-gdp-economy/)**

Trump's promises on a jobs revival has yet to materialize, but AI investment is soaring.

Fortune • 3h ago

---

**[Building a new enterprise AI services company with Blackstone, Hellman & Friedman, and Goldman Sachs](https://www.anthropic.com/news/enterprise-ai-services-company)**

Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.

Anthropic • 9h ago

---

**[Democratic leaders want an affordability debate on AI. Critics say they’re ducking the real fight.](https://www.politico.com/news/2026/05/04/democratic-leaders-want-an-affordability-debate-on-ai-critics-say-theyre-ducking-the-real-fight-00902977)**

Politico • 14h ago

---

**[AI finds signs of pancreatic cancer before tumors develop](https://www.nbcnews.com/health/cancer/ai-early-signs-pancreatic-cancer-before-tumors-develop-rcna343099)**

An artificial intelligence model from the Mayo Clinic detected abnormalities on scans up to two years before patients were diagnosed. It's being evaluated in a clinical trial.

NBC News • 2d ago

---

**[Hacked, robbed, then banned: Canton business owner’s meta AI nightmare](https://www.clickondetroit.com/news/investigations/2026/05/04/hacked-robbed-then-banned-michigan-mans-meta-ai-nightmare/)**

A Canton small-business owner says he was hacked twice, had $950 stolen from his account and was then permanently banned from Facebook — accused of one of the most horrific crimes imaginable. Meta, he says, has done nothing to fix it.

ClickOnDetroit | WDIV Local 4 • 3h ago

---

---

## HackerNews: "ai"

**[Let's Buy Spirit Air](https://news.ycombinator.com/item?id=48002777)**

Spirit Airlines collapsed. Before private equity locks it up, the people can own it. Join the Spirit 2.0 founding coalition. One member, one vote. Profits shared by all.

⬆️ 565 • 💬 538 • 23h ago • [letsbuyspiritair.com](https://letsbuyspiritair.com/)

---

**[AI Self-preferencing in Algorithmic Hiring: Empirical Evidence and Insights](https://news.ycombinator.com/item?id=47987256)**

As artificial intelligence (AI) tools become widely adopted, large language models (LLMs) are increasingly involved on both sides of decision-making processes, ranging from hiring to content moderation. This dual adoption raises a critical question: do LLMs systematically favor content that resembles their own outputs? Prior research in computer science has identified self-preference bias -- the tendency of LLMs to favor their own generated content -- but its real-world implications have not been empirically evaluated. We focus on the hiring context, where job applicants often rely on LLMs to refine resumes, while employers deploy them to screen those same resumes. Using a large-scale controlled resume correspondence experiment, we find that LLMs consistently prefer resumes generated by themselves over those written by humans or produced by alternative models, even when content quality is controlled. The bias against human-written resumes is particularly substantial, with self-preference bias ranging from 67% to 82% across major commercial and open-source models. To assess labor market impact, we simulate realistic hiring pipelines across 24 occupations. These simulations show that candidates using the same LLM as the evaluator are 23% to 60% more likely to be shortlisted than equally qualified applicants submitting human-written resumes, with the largest disadvantages observed in business-related fields such as sales and accounting. We further demonstrate that this bias can be reduced by more than 50% through simple interventions targeting LLMs' self-recognition capabilities. These findings highlight an emerging but previously overlooked risk in AI-assisted decision making and call for expanded frameworks of AI fairness that address not only demographic-based disparities, but also biases in AI-AI interactions.

⬆️ 332 • 💬 178 • 2d ago • [arXiv.org](https://arxiv.org/abs/2509.00462)

---

**[Specsmaxxing – On overcoming AI psychosis, and why I write specs in YAML](https://news.ycombinator.com/item?id=47994012)**

The toolkit for spec-driven development. Write feature specs, not prompts. Ship better software with AI agents that understand your requirements.

⬆️ 280 • 💬 289 • 1d ago • [acai.sh](https://acai.sh/blog/specsmaxxing)

---

**[How OpenAI delivers low-latency voice AI at scale](https://news.ycombinator.com/item?id=48013919)**

How OpenAI rebuilt its WebRTC stack to power real-time Voice AI with low latency, global scale, and seamless conversational turn-taking.

⬆️ 188 • 💬 81 • 3h ago • [OpenAI](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)

---

**[OpenAI, Google, and Microsoft Back Bill to Fund 'AI Literacy' in Schools](https://news.ycombinator.com/item?id=48010774)**

A new bill introduced by Senators Adam Schiff and Mike Rounds would award grants to the National Science Foundation—which has endured massive funding cuts under the Trump Administration for science research—to put “AI literacy” in schools.

⬆️ 107 • 💬 95 • 7h ago • [404 Media](https://www.404media.co/literacy-in-future-technologies-artificial-intelligence-act-adam-schiff-mike-rounds/)

---

**[Show HN: Agent-desktop – Native desktop automation CLI for AI agents](https://news.ycombinator.com/item?id=47982708)**

Native desktop automation CLI for AI agents. Control any application through OS accessibility trees with structured JSON output and deterministic element refs. - lahfir/agent-desktop

⬆️ 97 • 💬 35 • 2d ago • [GitHub](https://github.com/lahfir/agent-desktop)

---

**[Spirit Airlines canceled all flights and is going out of business](https://news.ycombinator.com/item?id=47985622)**

Spirit Airlines, the pioneering discount airline that shook up the budget travel business, is shutting down its operations.

⬆️ 84 • 💬 48 • 2d ago • [CNN](https://www.cnn.com/2026/05/02/business/spirit-to-halt-all-flights)

---

**[Voice-AI-for-Beginners – A curated learning path for developers](https://news.ycombinator.com/item?id=47991018)**

Set of 📝 with 🔗 to help those building Voice AI agents 🎙️🤖 - mahimairaja/voiceai

⬆️ 83 • 💬 4 • 2d ago • [GitHub](https://github.com/mahimairaja/voiceai)

---

**[AI, Intimacy, and the Data You Never Meant to Share](https://news.ycombinator.com/item?id=47992802)**

AI is quietly entering the bedroom — and taking notes. A look at connected pleasure devices, biometric data, and the privacy questions nobody is asking.

⬆️ 81 • 💬 6 • 1d ago • [fshot.org](https://fshot.org/techzone/the-algorithm-knows.php)

---

**[The Oscars just banned AI from winning acting and writing awards](https://news.ycombinator.com/item?id=47999346)**

⬆️ 76 • 💬 62 • 1d ago • [gizmodo.com](https://gizmodo.com/the-oscars-just-banned-ai-from-winning-acting-and-writing-awards-2000753740)

---

---

## YouTube Videos: "ai"

**[AI Just Designed A Quantum Computer](https://www.youtube.com/watch?v=l_bzA_M6_qo)**

FREE GUIDE: The Content Creator's AI Blueprint –* https://FirstMovers.ai/blueprint/ *The recursive loop just turned on — AI is ...

📺 Julia McCoy

👁️ 19K • 👍 914 • 💬 94 • ⏱️ 6:54 • 8h ago

---

**[Big Tech&#39;s AI Plan Has Failed](https://www.youtube.com/watch?v=tR5adb2Ts6c)**

GET 84% OFF + 4 MONTHS FREE CYBERGHOST VPN: https://cyberghostvpn.com/SashaYanshin Big Tech is spending over ...

📺 Sasha Yanshin

👁️ 20K • 👍 2K • 💬 329 • ⏱️ 16:06 • 7h ago

---

**[Scott Galloway: AI Wasn’t Built For You. The Rich Don’t Need You Anymore!](https://www.youtube.com/watch?v=NdU6UdUKaYc)**

AI CEOs are selling us the dream of 'freedom', making billions off the fear of mass job loss! Scott Galloway reveals the truth is ...

📺 The Diary Of A CEO

👁️ 512K • 👍 15K • 💬 2K • ⏱️ 1:58:11 • 16h ago

---

**[Passive Income: I Tried AI Dropshipping For a Week (RAW RESULTS)](https://www.youtube.com/watch?v=rhuYy9LP72M)**

Get a FREE AI-built Shopify store: https://www.buildyourstore.ai/wv43 Try AutoDS here for just $1 - https://www.autods.com/il38 ...

📺 Mark Tilbury

👁️ 67K • 👍 5K • 💬 1K • ⏱️ 28:29 • 12h ago

---

**[This AI Is Scarier Than AGI, ASI and Terminator](https://www.youtube.com/watch?v=ItlT2g3-7dE)**

Scientists are warning that the next big AI threat may not look like AGI, ASI, or the Terminator. It may look like AI agents that copy, ...

📺 AI Revolution

👁️ 59K • 👍 2K • 💬 252 • ⏱️ 15:10 • 2d ago

---

**[Caine Goes to AI Hell](https://www.youtube.com/watch?v=WDFAly0OrMo)**

CREDITS: Caine/AM: https://x.com/Spamoramma https://www.youtube.com/@UC7d19tHHOQ3DYxfRKvrwO4A Monika: ...

📺 Sourcy

👁️ 157K • 👍 16K • 💬 1K • ⏱️ 3:05 • 1d ago

---

**[If You&#39;re Worried About AI, You NEED To See This](https://www.youtube.com/watch?v=6rGhvV3rZa4)**

AI CEOs are telling you your job is about to disappear. NYU Professor Scott Galloway says that narrative is "mostly bullshit" and ...

📺 The Diary Of A CEO Clips

👁️ 8K • 👍 438 • 💬 69 • ⏱️ 21:59 • 5h ago

---

**[20 Next Level AI Gadgets You Can Buy Right Now](https://www.youtube.com/watch?v=NlxZoeWhVvc)**

20 Next Level AI Gadgets You Can Buy Right Now 00:00 - Introduction 00:31 - 1. Insta360 Wave : https://amzn.to/4dkKIBQ 01:29 ...

📺 TechTrends

👁️ 1K • 👍 28 • 💬 5 • ⏱️ 18:39 • 10h ago

---

**[谷歌瘋了？砸數億美金的AI竟然白送！Google Gemma 4 震撼發佈：這是一場針對 OpenAI 的血腥屠殺！📉🚫](https://www.youtube.com/watch?v=btIxjkIfJFE)**

谷歌這次真的下狠手了！看似是大發慈悲「技術扶貧」，實則是價值百億美金的商業絞殺戰！   為什麼谷歌要將耗資數億的Gemma ...

📺 商業本質

👁️ 10K • 👍 343 • 💬 22 • ⏱️ 23:42 • 11h ago

---

**[Biohacker Bryan Johnson trusts AI will solve human aging](https://www.youtube.com/watch?v=_QIEscvBI6M)**

Centimillionaire 'biohacker' Bryan Johnson, who made his fortune selling Venmo for $800 million, is now attempting to reverse the ...

📺 CNN

👁️ 36K • 👍 629 • 💬 607 • ⏱️ 25:06 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 534,942 • ❤️ 3,523 • 7d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 11,812 • ❤️ 424 • 6d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 132,595 • ❤️ 1,257 • 12d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 11,950 • ❤️ 254 • 9h ago

---

**[talkie-1930-13b-it](https://huggingface.co/talkie-lm/talkie-1930-13b-it)**

*talkie*

talkie-1930-13b-it is a 13B instruction-tuned language model trained on pre-1931 English text, excelling at generating responses in a vintage style for applications like historical chatbots or creative writing.

⬇️ 0 • ❤️ 223 • 11d ago

---

**[Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)**

*NVIDIA*

Nemotron-3 Nano Omni 30B is a multimodal LLM for enterprise Q&A, summarization, and document intelligence, capable of processing video, audio, image, and text inputs for use cases like customer service, media analysis, and GUI automation.

`any-to-any` `33.0B`

⬇️ 40,403 • ❤️ 220 • 2d ago

---

**[Laguna-XS.2](https://huggingface.co/poolside/Laguna-XS.2)**

*Poolside*

Laguna XS.2 is a 33B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring Sliding Window Attention and FP8 KV cache for efficient local execution on 36GB RAM. It supports native reasoning and is available under the Apache 2.0 license.

`text-generation` `33.4B`

⬇️ 10,357 • ❤️ 210 • 1d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,334,241 • ❤️ 1,107 • 10d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 20,187 • ❤️ 168 • 17h ago

---

**[MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)**

*Xiaomi MiMo*

MiMo-V2.5 is a native omnimodal LLM supporting text, image, video, and audio with a 1M token context window. It excels in multimodal understanding, long-context reasoning, and agentic workflows, utilizing a hybrid attention architecture and efficient pre-training.

`310.8B`

⬇️ 51,554 • ❤️ 206 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 55 • 💬 3 • ⭐ 67,058 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 168 • 💬 10 • ⭐ 46,473 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 15 • 💬 3 • ⭐ 9,072 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 30 • 💬 3 • ⭐ 22,699 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,700 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 61,929 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Representation Fréchet Loss for Visual Generation](https://huggingface.co/papers/2604.28190)**

*Jiawei Yang, Zhengyang Geng, Xuan Ju et al. (5 authors)*

Fréchet Distance can be effectively optimized as a training objective when decoupling population size from batch size, leading to improved generator quality and alternative evaluation metrics.

▲ 21 • 💬 1 • ⭐ 300 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.28190) • [💻 code](https://github.com/Jiawei-Yang/FD-Loss)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,012 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 19,361 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 54,750 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 51.1k • 🔱 6.7k • 1d ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.7k • 🔱 2.7k • 7d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 10.1k • 🔱 661 • 1h ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 8.0k • 🔱 1.2k • 5d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

`Python` `agent-workflows` `ai` `claude-code` `developer-tools` `diagrams`

⭐ 5.4k • 🔱 485 • 12h ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 5.3k • 🔱 408 • 5h ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 5.0k • 🔱 352 • 12h ago

---

**[AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)**

Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch

`Python` `ai` `claude-code` `claude-code-skill` `knowledge-management` `obsidian`

⭐ 4.2k • 🔱 471 • 10d ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics & channel configuration (Telegram, Discord, Slack, WhatsApp)

`TypeScript` `agent` `ai-agent` `chat-ui` `chatbot` `claude`

⭐ 3.5k • 🔱 426 • 9h ago

---

**[alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)**

Hermes Agent 从入门到精通 · 橙皮书系列 · Nous Research 开源 AI Agent 框架实战指南

⭐ 3.5k • 🔱 367 • 13d ago

---

---

*Generated by PeekDeck - A glance is all you need*
