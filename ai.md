---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-18T11:47:52.187463+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 18, 2026 at 11:47 UTC  
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

**[Jensen Huang says gamers are 'completely wrong' about DLSS 5 — Nvidia CEO responds to DLSS 5 backlash](https://www.reddit.com/r/artificial/comments/1rwl37x/jensen_huang_says_gamers_are_completely_wrong/)**

The CEO says artistic control remains with developers.

🔗 [Tom's Hardware](https://www.tomshardware.com/pc-components/gpus/jensen-huang-says-gamers-are-completely-wrong-about-dlss-5-nvidia-ceo-responds-to-dlss-5-backlash) • 13h ago

---

**[LLMs forget instructions the same way ADHD brains do. The research on why is fascinating.](https://www.reddit.com/r/artificial/comments/1rwkj5j/llms_forget_instructions_the_same_way_adhd_brains/)**

I've been building long-running agentic workflows and kept hitting the same problem: the AI forgets instructions from earlier in the conversation, rushes to produce output, and skips boring middle steps. The research explains why: "Lost in the Middle" (Stanford 2023) showed a 30%+ performance drop when critical information is in the middle of the context window. Accuracy is high at the start and end, drops in the middle. Exactly like working memory overflow. "LLMs Get Lost in Multi-Turn Conversation" (Laban et al. 2025) showed that instructions from early turns get diluted by later content. The more turns, the worse the recall. 65% of enterprise AI failures in 2025 were attributed to context drift during multi-step reasoning. The parallel to ADHD executive dysfunction isn't metaphorical. Dense local connectivity in transformer attention mirrors the "intense world" theory of neurodivergent processing. Both produce: strong pattern recognition + weak executive control over long sequences. The fixes map too. "Echo of Prompt" (re-injecting instructions before execution) is the AI equivalent of re-reading the question before answering. Task decomposition into small steps reduces overwhelm. External verification prevents self-reported false completion. Has anyone else noticed this pattern in their agentic builds? Curious what scaffolding techniques others are using for long-running workflows.

14h ago

---

**[The Moltbook acquisition makes a lot more sense when you read one of Meta's patent filings](https://www.reddit.com/r/artificial/comments/1rwyk17/the_moltbook_acquisition_makes_a_lot_more_sense/)**

Last week's post about Meta buying Moltbook got a lot of discussion here. I think most of the coverage (and the comments) missed what Meta is actually doing with it. I read a lot of patent filings because LLMs make them surprisingly accessible now, and one filed by Meta's CTO Andrew Bosworth connects directly to the Moltbook acquisition in a way I haven't seen anyone talk about. In December 2025, Meta was granted patent US 12513102B2 for a system that trains a language model on a user's historical interactions (posts, comments, likes, DMs, voice messages) and deploys it to simulate that user's social media behavior autonomously. The press covered it as "Meta wants to post for you after you die." The actual patent text describes simulating any user who is "absent from the social networking system," which includes breaks, inactivity, or death. The deceased framing is a broadening mechanism for the claims. What they built is a personalized LLM that maintains engagement on behalf of any user, for any reason. Now layer in the acquisitions. December 2025: Meta buys Manus for over $2 billion. General-purpose AI agent platform, hit $100M ARR eight months after launch. Meta said they'd integrate it into their consumer and business products. March 2026: The Moltbook acqui-hire. Matt Schlicht and Ben Parr join Meta Superintelligence Labs. What most coverage left out is their background. Schlicht and Parr co-founded Octane AI, a conversational commerce platform that automated personalized customer interactions for Shopify merchants via Messenger and SMS. They've been building AI-driven business communication tools since 2016. I think these three moves are connected. The "digital ghost" and "AI agents chatting with each other" framings are both wrong. Bosworth himself said in an Instagram Q&A that he didn't find Moltbook's agent conversations particularly interesting. So why buy it? Because Meta is building infrastructure for AI agents that act on behalf of businesses across their platforms. The small business owner spending hours managing their Facebook and Instagram presence is the real target user. The e-commerce brand running customer conversations through WhatsApp is the real target user. The patent gives them the IP foundation, Manus gives them the agent platform, and the Schlicht/Parr hire gives them the team that spent a decade figuring out how to make this work commercially. I'll be honest about the limits of reading patent tea leaves. Companies file for all kinds of reasons and most aren't strategic. Engineers get bonuses for filings. Legal teams build portfolios for cross-licensing leverage. Reading a single patent as a roadmap is a mistake I've made before. But a patent plus $2B in acquisitions plus an acqui-hire of people who built a related product for a decade starts to look like a pattern. Anyone here have a different read? Especially curious if anyone on Meta's business tools side sees this differently.

2h ago

---

**[Are we cooked?](https://www.reddit.com/r/artificial/comments/1rw4k3l/are_we_cooked/)**

I work as a developer, and before this I was copium about AI, it was a form of self defense. But in Dec 2025 I bought subscriptions to gpt codex and claude. And honestly the impact was so strong that I still haven't recovered, I've barely written any code by hand since I bought the subscription And it's not that AI is better code than me. The point is that AI is replacing intellectual activity itself. This is absolutely not the same as automated machines in factories replacing human labor Neural networks aren't just about automating code, they're about automating intelligence as a whole. This is what AI really is. Any new tasks that arise can, in principle, be automated by a neural network. It's not a machine, not a calculator, not an assembly line, it's automation of intelligence in the broadest sense Lately I've been thinking about quitting programming and going into science (biotech), enrolling in a university and developing as a researcher, especially since I'm still young. But I'm afraid I might be right. That over time, AI will come for that too, even for scientists. And even though AI can't generate truly novel ideas yet, the pace of its development over the past few years has been so fast that it scares me

23h ago

---

**[Built a site for tracking reported cases of AI-induced psychological harm since January. 126 cases documented so far. Split between reporting and academic journals for those who might want to research further. Feedback welcome](https://www.reddit.com/r/artificial/comments/1rwvqb9/built_a_site_for_tracking_reported_cases_of/)**

Documenting reported cases of AI-induced psychological harm — dependency, delusion, identity confusion, and reality distortion. Updated weekly.

🔗 [aipsychosis.watch](https://aipsychosis.watch) • 5h ago

---

**[The Pentagon is developing its own LLMs | TechCrunch](https://www.reddit.com/r/artificial/comments/1rx1k64/the_pentagon_is_developing_its_own_llms_techcrunch/)**

Russia aids Iran against U.S. ships. Oil surges 50%. Joe Kent resigns. DOGE cuts grants via AI. Trump creates a secret database. Hawley targets mifepristone. Vance leads fraud task force.

🔗 [Instrumental Communications](https://www.instrumentalcomms.com/blog/a-new-exoskeleton#story-the-pentagon-is-developing-its-own-llms) • 5m ago

---

**[Open sourced a tool that can find precise coordinates of any street level pic](https://www.reddit.com/r/artificial/comments/1rx096v/open_sourced_a_tool_that_can_find_precise/)**

Hey guys, I built an open source tool called Netryx that can find precise coordinates of any street level picture. It is designed designed to find exact coordinates from a street level photo using visual clues and a custom ML pipeline and Al. I really hope you guys have fun using it! Also would love to connect with developers and companies in this space! Link to source code: https://github.com/sparkyniner/ Netryx-OpenSource-Next-Gen-Street-Level-Geolocation.git Attaching the video to an example geolocating the Qatar strikes, it looks different because it's a custom web version but pipeline is same.

1h ago

---

**[Are marketing jobs truly threatened by AI?](https://www.reddit.com/r/artificial/comments/1rwut6e/are_marketing_jobs_truly_threatened_by_ai/)**

Or has it created new opportunities, increased productivity, or had no influence at all. And do you expect it to in the future?

6h ago

---

**[Nvidia unveils AI infrastructure spanning chips to space computing](https://www.reddit.com/r/artificial/comments/1rw8rz6/nvidia_unveils_ai_infrastructure_spanning_chips/)**

Nvidia unveils Vera CPU and Rubin platform to power agentic AI systems and next-generation AI factories.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/nvidia-vera-cpu-vera-rubin-ai-factories) • 20h ago

---

**[AI, Invasive Technology, and the Way of the Warrior](https://www.reddit.com/r/artificial/comments/1rwxr19/ai_invasive_technology_and_the_way_of_the_warrior/)**

Today we’re going to explore three ideas that help us understand the age of artificial intelligence: first, the stage that is being set for AI in our civilization; second, the idea of invasive technology; and third, what the speaker calls the “way of the warrior” — a mindset for living in this new technological world. Let’s begin with the broader context. Throughout history, major technological shifts have reshaped human civilization. Agriculture changed how societies organized themselves. The industrial revolution transformed production and economic power. Later, digital computing revolutionized information and communication. Artificial intelligence represents the next major shift, but it is different in an important way. Earlier technologies extended human abilities — our muscles, our speed, or our ability to calculate. AI, however, extends something much deeper: cognition. For the first time in history, we are creating systems that can perform tasks that previously required human reasoning. They can analyze information, generate ideas, write text, and assist with decision-making. In the past, human beings were the only general intelligence operating in society. Now we are introducing additional intelligences into the system. These systems don’t think exactly like humans, but they can produce outputs that resemble human reasoning. This raises a fundamental question: if machines can increasingly perform cognitive tasks, what role does human intelligence play? This is why the speaker argues that artificial intelligence is not just a technical development. It is a civilizational one. It forces us to reconsider ideas about expertise, authority, and knowledge itself. But understanding AI also requires understanding the type of technology it represents. The speaker introduces the concept of invasive technology. Most technologies throughout history have been external tools. A hammer extends the power of our hands. A car extends our mobility. Even computers primarily extended our ability to calculate and process data. AI, however, begins to enter the domain of thinking itself. When we use AI systems to write, plan, analyze information, or generate ideas, the technology becomes embedded in the process of cognition. Instead of simply assisting our actions, it begins influencing our thinking. This is why AI can be described as invasive. First, it invades cognition. Tasks that once required careful reasoning may increasingly be delegated to machines. Over time, this could change how people learn, how they solve problems, and even how they develop expertise. Second, AI invades institutions. Governments, corporations, and educational systems are integrating algorithmic decision-making into their operations. When automated systems help guide important decisions, the influence of algorithms becomes structural. Third, AI invades culture. Machines are now producing text, images, music, and art. As this grows, the boundary between human creation and machine generation becomes increasingly blurred. The result is a technological environment that is no longer merely outside us. It becomes part of the infrastructure of thought, decision-making, and culture. Faced with this kind of technological transformation, the speaker suggests we need a philosophical response. This is where the idea of “the way of the warrior” comes in. The metaphor of the warrior is not about violence or conflict. Instead, it refers to a disciplined way of engaging with powerful forces. Throughout history, warrior traditions emphasized self-control, clarity of purpose, responsibility, and mastery. These qualities become especially important in times of rapid change. In the context of artificial intelligence, the warrior mindset involves several principles. The first is mastery rather than dependence. AI tools can be extraordinarily powerful, but relying on them blindly can weaken human capability. The warrior approach is to use these tools deliberately while maintaining independent skills and understanding. Technology should amplify human intelligence, not replace it. The second principle is mental discipline. In an environment filled with automated answers and endless information, the ability to think deeply becomes increasingly valuable. Critical thinking, sustained attention, and intellectual rigor are qualities that must be actively cultivated. The third principle is ethical responsibility. AI systems can influence decisions that affect large numbers of people. Those who design, deploy, or rely on these systems carry significant responsibility. Without strong ethical frameworks, powerful technologies can easily produce unintended harm. Finally, the warrior mindset emphasizes human identity. Rather than competing directly with machines on speed or data processing, humans must focus on qualities that remain uniquely meaningful: wisdom, judgment, creativity, and moral reasoning. The goal is not to reject technology but to engage with it consciously. Artificial intelligence will continue to evolve, and its influence will likely expand across nearly every aspect of society. The key question is not whether AI will shape the world — it almost certainly will. The real question is how humans choose to relate to it. Do we become passive users of automated systems, or do we approach these technologies with discipline, awareness, and responsibility? The speaker’s answer is clear. In the age of artificial intelligence, what we need is not simply better technology. What we need is a stronger philosophy of how humans should live and think in the presence of powerful machines. That philosophy is what he calls the way of the warrior. -- description of the video 'nitty grittys ordeal - bridging the machine mind with bodily senses ' by chatgpt , video link in comment below

3h ago

---

---

## Google News: "ai"

**[Ad for AI editing app which said it could 'remove anything' banned](https://www.bbc.com/news/articles/cx2g8888q53o)**

The UK regulator said the ad condoned "digitally altering and exposing women's bodies without their consent."

BBC • 11h ago

---

**[The AI spending flip](https://www.axios.com/2026/03/18/ai-enterprise-revenue-anthropic-openai)**

Axios • 2h ago

---

**[We asked experts about the most responsible ways to use AI tools – here’s what they said](https://www.theguardian.com/lifeandstyle/ng-interactive/2026/mar/18/how-to-use-ai-tools-expert-guide)**

Use AI as a brainstorming partner and organizer, but don’t outsource your judgment

The Guardian • 47m ago

---

**[Dog Mom Hilariously Proves That AI Isn't Taking Every Job](https://www.yahoo.com/lifestyle/articles/dog-mom-hilariously-proves-ai-112000593.html)**

Even AI doesn't want to clean a dog's dirty bottom.

Yahoo • 27m ago

---

**[AI-powered ad spend is set to soar 63% this year as brands ditch manual controls](https://www.businessinsider.com/ai-powered-ads-driving-us-ad-growth-madison-wall-2026-3)**

Tools like Google's Performance Max and Meta's Advantage Plus are driving a lift in AI-powered advertising revenue, per Madison and Wall.

Business Insider • 7m ago

---

**[Netanyahu Posts ‘Proof of Life’ Video as A.I. Sows Doubts About What’s Real](https://www.nytimes.com/2026/03/17/technology/netanyahu-ai-video-iran-israel.html)**

The New York Times • 17h ago

---

**["Sorry. You Blew It": US Envoy Fact-Checks Grok On 'Netanyahu AI Video'](https://www.ndtv.com/world-news/benjamin-netanyahu-death-rumours-netanyahus-i-am-alive-video-confuses-grok-us-envoy-clarifies-11231787)**

Israeli Prime Minister Benjamin Netanyahu's new "I am alive" video to quell his death rumours has invited scrutiny after X's artificial intelligence (AI) chatbot, Grok, flagged it as "not a real meeting clip".

NDTV • 4h ago

---

**[Netanyahu denies death rumours in social media clip which Grok falsely branded AI](https://www.euronews.com/my-europe/2026/03/18/netanyahu-denies-death-rumours-in-social-media-clip-which-grok-falsely-branded-ai)**

Since the US and Israel began their military campaign against Iran on 28 February, Iranian state media and pro-regime accounts have pushed fake news about the death of Netanyahu and other senior Israeli political figures. #TheCube

Euronews.com • 1h ago

---

**[A mystery AI model has developers buzzing: Is this DeepSeek's latest blockbuster?](https://www.reuters.com/business/media-telecom/mystery-ai-model-has-developers-buzzing-is-this-deepseeks-latest-blockbuster-2026-03-18/)**

Reuters • 8h ago

---

**[Senator introduces bill to draw red lines to limit AI use by military](https://www.nbcnews.com/tech/security/senator-introduces-bill-draw-red-lines-ai-use-military-rcna263905)**

The bill seeks to codify several existing Defense Department guidelines in addition to other limits.

NBC News • 17h ago

---

---

## HackerNews: "ai"

**[Mistral AI Releases Forge](https://news.ycombinator.com/item?id=47418295)**

Today, we’re introducing Forge, a system that allows enterprises to build frontier-grade AI models grounded in their proprietary knowledge.

⬆️ 511 • 💬 115 • 14h ago • [mistral.ai](https://mistral.ai/news/forge)

---

**[Ask HN: How is AI-assisted coding going for you professionally?](https://news.ycombinator.com/item?id=47388646)**

⬆️ 421 • 💬 599 • 2d ago

---

**[AirPods Max 2](https://news.ycombinator.com/item?id=47398681)**

The ultimate over-ear listening experience — in five vibrant colors and with up to 1.5x more Active Noise Cancellation than the previous generation.

⬆️ 318 • 💬 549 • 1d ago • [Apple](https://www.apple.com/airpods-max/)

---

**[Nvidia Launches Vera CPU, Purpose-Built for Agentic AI](https://news.ycombinator.com/item?id=47404074)**

NVIDIA today launched the NVIDIA Vera CPU, the world’s first processor purpose-built for the age of agentic AI and reinforcement learning — delivering results with twice the efficiency and 50% faster than traditional rack-scale CPUs.

⬆️ 173 • 💬 99 • 1d ago • [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-launches-vera-cpu-purpose-built-for-agentic-ai)

---

**[Speed at the cost of quality: Study of use of Cursor AI in open source projects (2025)](https://news.ycombinator.com/item?id=47401734)**

Large language models (LLMs) have demonstrated the promise to revolutionize the field of software engineering. Among other things, LLM agents are rapidly gaining momentum in software development, with practitioners reporting a multifold increase in productivity after adoption. Yet, empirical evidence is lacking around these claims. In this paper, we estimate the causal effect of adopting a widely popular LLM agent assistant, namely Cursor, on development velocity and software quality. The estimation is enabled by a state-of-the-art difference-in-differences design comparing Cursor-adopting GitHub projects with a matched control group of similar GitHub projects that do not use Cursor. We find that the adoption of Cursor leads to a statistically significant, large, but transient increase in project-level development velocity, along with a substantial and persistent increase in static analysis warnings and code complexity. Further panel generalized-method-of-moments estimation reveals that increases in static analysis warnings and code complexity are major factors driving long-term velocity slowdown. Our study identifies quality assurance as a major bottleneck for early Cursor adopters and calls for it to be a first-class citizen in the design of agentic AI coding tools and AI-driven workflows.

⬆️ 145 • 💬 77 • 1d ago • [arXiv.org](https://arxiv.org/abs/2511.04427)

---

**[Apideck CLI – An AI-agent interface with much lower context consumption than MCP](https://news.ycombinator.com/item?id=47400261)**

TL;DR: MCP tool definitions can burn 55,000+ tokens before an agent processes a single user message. We built the Apideck CLI as an AI-agent interface instead:an ~80-token agent prompt replaces tens of thousands of tokens of schema, with progressive disclosure via `--help` and structural safety baked into the binary. Any agent that can run shell commands can use it. No protocol support required.

⬆️ 136 • 💬 122 • 1d ago • [Apideck](https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative)

---

**[Why AI systems don't learn – On autonomous learning from cognitive science](https://news.ycombinator.com/item?id=47418722)**

We critically examine the limitations of current AI models in achieving autonomous learning and propose a learning architecture inspired by human and animal cognition. The proposed framework integrates learning from observation (System A) and learning from active behavior (System B) while flexibly switching between these learning modes as a function of internally generated meta-control signals (System M). We discuss how this could be built by taking inspiration on how organisms adapt to real-world, dynamic environments across evolutionary and developmental timescales.

⬆️ 129 • 💬 67 • 14h ago • [arXiv.org](https://arxiv.org/abs/2603.15381)

---

**[Why I may ‘hire’ AI instead of a graduate student](https://news.ycombinator.com/item?id=47396557)**

⬆️ 107 • 💬 107 • 2d ago • [science.org](https://www.science.org/content/article/why-i-may-hire-ai-instead-graduate-student)

---

**[Tell HN: AI tools are making me lose interest in CS fundamentals](https://news.ycombinator.com/item?id=47394291)**

⬆️ 95 • 💬 89 • 2d ago

---

**[Toward automated verification of unreviewed AI-generated code](https://news.ycombinator.com/item?id=47397367)**

Constraints that could make unreviewed AI-generated code trustworthy.

⬆️ 89 • 💬 83 • 2d ago • [peterlavigne.com](https://peterlavigne.com/writing/verifying-ai-generated-code)

---

---

## YouTube Videos: "ai"

**[I Asked AI If Trump Loses Congress in 2026 MIDTERMS](https://www.youtube.com/watch?v=07rYtfyFa-Y)**

Go to https://groundnews.com/ai to stay fully informed about U.S. politics, AI, and more. Subscribe through my link to get 40% off ...

📺 I Ask AI

👁️ 19K • 👍 2K • 💬 161 • ⏱️ 13:12 • 1d ago

---

**[Google’s New AI Just Broke Math… (Invented Its Own Algorithms)](https://www.youtube.com/watch?v=W31ro8YT7jc)**

Google DeepMind's AlphaEvolve just broke long-standing mathematical records by evolving algorithms that improved several ...

📺 AI Revolution

👁️ 40K • 👍 1K • 💬 70 • ⏱️ 10:41 • 1d ago

---

**[My Favorite AI Workflow](https://www.youtube.com/watch?v=kKG5MDF_234)**

Start building with Bolt for free (no credit card required): ...

📺 Tina Huang

👁️ 15K • 👍 873 • 💬 48 • ⏱️ 20:45 • 20h ago

---

**[10 Claude AI Skills That Will Save You 20+ Hours a Week (Full Power User Guide)](https://www.youtube.com/watch?v=ADByNXt2ouY)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *These ...

📺 Julia McCoy

👁️ 21K • 👍 904 • 💬 46 • ⏱️ 16:22 • 2d ago

---

**[Best AI Coding Tools for Developers in 2026 (Don&#39;t Choose Wrong)](https://www.youtube.com/watch?v=RKbmqSRc0z0)**

Best AI Coding Tool is Base44 https://base44.pxf.io/c/6440076/2049275/25619?trafcat=base&sharedid=video102 ✓ FREE ...

📺 Mikey No Code

👁️ 18K • 💬 30 • ⏱️ 27:10 • 1d ago

---

**[Why AI Researchers Are Quitting and Panicking on the Way Out](https://www.youtube.com/watch?v=rtT87iAm_SM)**

Top AI researchers are walking away from some of the most powerful tech companies on Earth, and their reasons are raising ...

📺 The Infographics Show

👁️ 387K • 👍 10K • 💬 1K • ⏱️ 14:48 • 1d ago

---

**[Before You Adapt to AI… Watch This](https://www.youtube.com/watch?v=k51k2AyUpao)**

Make your videos sound better with Epidemic Sound! Add the code ANDREAS at checkout, to get 50% off for 2 months ...

📺 Andreas Hem

👁️ 37K • 👍 4K • 💬 456 • ⏱️ 16:35 • 3d ago

---

**[Daniel Priestley: AI Will Make Plumbers Earn More Than Lawyers! (2029 PREDICTION)](https://www.youtube.com/watch?v=fpETS6q1Hww)**

What is financial freedom? The Business Strategist Daniel Priestley on why AI makes lifestyle businesses easy. Daniel Priestley is ...

📺 The Diary Of A CEO

👁️ 943K • 👍 22K • 💬 4K • ⏱️ 2:02:37 • 2d ago

---

**[NVIDIA Just Dropped 3 Bombshells for AI Creators!](https://www.youtube.com/watch?v=9B5blAOCx6Q)**

Nvidia's GTC 2026 keynote just dropped some massive AI hardware reveals! From the insane Vera Rubin super platform to the ...

📺 Theoretically Media

👁️ 18K • 👍 788 • 💬 121 • ⏱️ 11:59 • 14h ago

---

**[Artist Claims They Didn’t Use AI…But People Don’t Believe It](https://www.youtube.com/watch?v=nm-CN9dt3FQ)**

Disclaimer: Please do NOT send hate to anyone mentioned in my videos. Everything that is said is alleged and there are always 2 ...

📺 kat 'n chat

👁️ 27K • 👍 1K • 💬 183 • ⏱️ 30:53 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 7,003 • ❤️ 608 • 6d ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 111,716 • ❤️ 518 • 7d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`text-generation` `27.8B`

⬇️ 78,794 • ❤️ 858 • 10d ago

---

**[OmniCoder-9B](https://huggingface.co/Tesslate/OmniCoder-9B)**

*Tesslate*

OmniCoder-9B is a 9B parameter coding agent fine-tuned on 425K agentic trajectories from frontier models, excelling in complex reasoning, error recovery, and tool use with a 262K native context window.

`text-generation`

⬇️ 8,716 • ❤️ 291 • 5d ago

---

**[NVIDIA-Nemotron-3-Super-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)**

*NVIDIA*

NVIDIA-Nemotron-3-Super-120B-A12B-BF16 is a 120B parameter LLM with a LatentMoE architecture, supporting up to 1M tokens context. It excels at agentic workflows, long-context reasoning, and high-volume tasks like IT automation, with configurable reasoning modes.

`text-generation` `123.6B`

⬇️ 36,759 • ❤️ 246 • 3d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 254,662 • ❤️ 527 • 14d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 2,271,977 • ❤️ 902 • 16d ago

---

**[LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3)**

*Lightricks*

LTX-2.3 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs, including images and text. It offers improved visual and audio quality, enhanced prompt adherence, and supports local execution with open weights.

`image-to-video`

⬇️ 644,452 • ❤️ 668 • 2d ago

---

**[Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)**

*Mistral AI_*

Mistral-Small-4-119B-2603 is a hybrid MoE model (119B params, 6.5B active) supporting 256k context and multimodal input (text/image). It excels at instruction following, reasoning (configurable effort), and agentic tasks with native function calling, offering significant speed and throughput improvements for use cases like coding, document analysis, and general assistants.

`119.4B`

⬇️ 1,872 • ❤️ 210 • 21h ago

---

**[tada-1b](https://huggingface.co/HumeAI/tada-1b)**

*Hume AI*

TADA-1B is a text-to-speech model that uses a novel 1:1 text-acoustic alignment for high-fidelity speech synthesis with reduced computational overhead. It enables dynamic duration synthesis and dual-stream generation, making it efficient for generating natural-sounding speech.

`text-to-speech` `2.2B`

⬇️ 36,677 • ❤️ 215 • 17h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Attention Residuals](https://huggingface.co/papers/2603.15031)**

*Kimi Team, Guangyu Chen, Yu Zhang et al. (37 authors)*

🏢 Moonshot AI

Residual connections with PreNorm are standard in modern LLMs, yet they accumulate all layer outputs with fixed unit weights. This uniform aggregation causes uncontrolled hidden-state growth with depth, progressively diluting each layer's contribution. We propose Attention Residuals (AttnRes), which replaces this fixed accumulation with softmax attention over preceding layer outputs, allowing each layer to selectively aggregate earlier representations with learned, input-dependent weights. To address the memory and communication overhead of attending over all preceding layer outputs for large-scale model training, we introduce Block AttnRes, which partitions layers into blocks and attends over block-level representations, reducing the memory footprint while preserving most of the gains of full AttnRes. Combined with cache-based pipeline communication and a two-phase computation strategy, Block AttnRes becomes a practical drop-in replacement for standard residual connections with minimal overhead.
  Scaling law experiments confirm that the improvement is consistent across model sizes, and ablations validate the benefit of content-dependent depth-wise selection. We further integrate AttnRes into the Kimi Linear architecture (48B total / 3B activated parameters) and pre-train on 1.4T tokens, where AttnRes mitigates PreNorm dilution, yielding more uniform output magnitudes and gradient distribution across depth, and improves downstream performance across all evaluated tasks.

▲ 76 • 💬 2 • ⭐ 1,521 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15031) • [💻 code](https://github.com/MoonshotAI/Attention-Residuals)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 15 • 💬 0 • ⭐ 35,306 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[AI Can Learn Scientific Taste](https://huggingface.co/papers/2603.14473)**

*Jingqi Tong, Mingzhe Li, Hangcheng Li et al. (23 authors)*

🏢 OpenMOSS

Great scientists have strong judgement and foresight, closely tied to what we call scientific taste. Here, we use the term to refer to the capacity to judge and propose research ideas with high potential impact. However, most relative research focuses on improving an AI scientist's executive capability, while enhancing an AI's scientific taste remains underexplored. In this work, we propose Reinforcement Learning from Community Feedback (RLCF), a training paradigm that uses large-scale community signals as supervision, and formulate scientific taste learning as a preference modeling and alignment problem. For preference modeling, we train Scientific Judge on 700K field- and time-matched pairs of high- vs. low-citation papers to judge ideas. For preference alignment, using Scientific Judge as a reward model, we train a policy model, Scientific Thinker, to propose research ideas with high potential impact. Experiments show Scientific Judge outperforms SOTA LLMs (e.g., GPT-5.2, Gemini 3 Pro) and generalizes to future-year test, unseen fields, and peer-review preference. Furthermore, Scientific Thinker proposes research ideas with higher potential impact than baselines. Our findings show that AI can learn scientific taste, marking a key step toward reaching human-level AI scientists.

▲ 224 • 💬 5 • ⭐ 258 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2603.14473) • [💻 code](https://github.com/tongjingqi/AI-Can-Learn-Scientific-Taste) • [🔗 project](https://tongjingqi.github.io/AI-Can-Learn-Scientific-Taste/)

---

**[Grounding World Simulation Models in a Real-World Metropolis](https://huggingface.co/papers/2603.15583)**

*Junyoung Seo, Hyunwook Choi, Minkyung Kwon et al. (13 authors)*

🏢 NAVER AI Lab

What if a world simulation model could render not an imagined environment but a city that actually exists? Prior generative world models synthesize visually plausible yet artificial environments by imagining all content. We present Seoul World Model (SWM), a city-scale world model grounded in the real city of Seoul. SWM anchors autoregressive video generation through retrieval-augmented conditioning on nearby street-view images. However, this design introduces several challenges, including temporal misalignment between retrieved references and the dynamic target scene, limited trajectory diversity and data sparsity from vehicle-mounted captures at sparse intervals. We address these challenges through cross-temporal pairing, a large-scale synthetic dataset enabling diverse camera trajectories, and a view interpolation pipeline that synthesizes coherent training videos from sparse street-view images. We further introduce a Virtual Lookahead Sink to stabilize long-horizon generation by continuously re-grounding each chunk to a retrieved image at a future location. We evaluate SWM against recent video world models across three cities: Seoul, Busan, and Ann Arbor. SWM outperforms existing methods in generating spatially faithful, temporally consistent, long-horizon videos grounded in actual urban environments over trajectories reaching hundreds of meters, while supporting diverse camera movements and text-prompted scenario variations.

▲ 114 • 💬 3 • ⭐ 195 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15583) • [💻 code](https://github.com/naver-ai/seoul-world-model) • [🔗 project](https://seoul-world-model.github.io/)

---

**[Fish Audio S2 Technical Report](https://huggingface.co/papers/2603.08823)**

*Shijia Liao, Yuxuan Wang, Songting Liu et al. (14 authors)*

🏢 Fish Audio

Fish Audio S2 is an open-source text-to-speech system with multi-speaker capabilities, multi-turn generation, and instruction-following control through natural-language descriptions, utilizing a multi-stage training approach and production-ready inference engine.

▲ 31 • 💬 2 • ⭐ 28,036 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08823) • [💻 code](https://github.com/fishaudio/fish-speech) • [🔗 project](https://fish.audio/)

---

**[OpenClaw-RL: Train Any Agent Simply by Talking](https://huggingface.co/papers/2603.10165)**

*Yinjie Wang, Xuyang Chen, Xiaolong Jin et al. (5 authors)*

🏢 Princeton AI Lab

OpenClaw-RL framework enables policy learning from diverse next-state signals across multiple interaction modalities using asynchronous training with PRM judges and hindsight-guided distillation.

▲ 119 • 💬 5 • ⭐ 3,368 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2603.10165) • [💻 code](https://github.com/Gen-Verse/OpenClaw-RL) • [🔗 project](https://github.com/Gen-Verse/OpenClaw-RL)

---

**[OpenSeeker: Democratizing Frontier Search Agents by Fully Open-Sourcing Training Data](https://huggingface.co/papers/2603.15594)**

*Yuwen Du, Rui Ye, Shuo Tang et al. (7 authors)*

🏢 OpenSeeker

Deep search capabilities have become an indispensable competency for frontier Large Language Model (LLM) agents, yet the development of high-performance search agents remains dominated by industrial giants due to a lack of transparent, high-quality training data. This persistent data scarcity has fundamentally hindered the progress of the broader research community in developing and innovating within this domain. To bridge this gap, we introduce OpenSeeker, the first fully open-source search agent (i.e., model and data) that achieves frontier-level performance through two core technical innovations: (1) Fact-grounded scalable controllable QA synthesis, which reverse-engineers the web graph via topological expansion and entity obfuscation to generate complex, multi-hop reasoning tasks with controllable coverage and complexity. (2) Denoised trajectory synthesis, which employs a retrospective summarization mechanism to denoise the trajectory, therefore promoting the teacher LLMs to generate high-quality actions. Experimental results demonstrate that OpenSeeker, trained (a single training run) on only 11.7k synthesized samples, achieves state-of-the-art performance across multiple benchmarks including BrowseComp, BrowseComp-ZH, xbench-DeepSearch, and WideSearch. Notably, trained with simple SFT, OpenSeeker significantly outperforms the second-best fully open-source agent DeepDive (e.g., 29.5% v.s. 15.3% on BrowseComp), and even surpasses industrial competitors such as Tongyi DeepResearch (trained via extensive continual pre-training, SFT, and RL) on BrowseComp-ZH (48.4% v.s. 46.7%). We fully open-source the complete training dataset and the model weights to democratize frontier search agent research and foster a more transparent, collaborative ecosystem.

▲ 131 • 💬 4 • ⭐ 115 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15594) • [💻 code](https://github.com/rui-ye/OpenSeeker)

---

**[EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://huggingface.co/papers/2603.08127)**

*Yougang Lyu, Xi Zhang, Xinhao Yi et al. (12 authors)*

EvoScientist is an adaptive multi-agent framework that enhances scientific discovery by continuously learning from past interactions through persistent memory modules.

▲ 12 • 💬 5 • ⭐ 855 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08127) • [💻 code](https://github.com/EvoScientist/EvoScientist)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 24 • 💬 1 • ⭐ 32,601 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[MemOS: A Memory OS for AI System](https://huggingface.co/papers/2507.03724)**

*Zhiyu Li, Shichao Song, Chenyang Xi et al. (39 authors)*

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.

▲ 164 • 💬 3 • ⭐ 7,380 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2507.03724) • [💻 code](https://github.com/MemTensor/MemOS) • [🔗 project](https://memos.openmem.net/)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 41.2k • 🔱 5.7k • 1d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 21.3k • 🔱 994 • 12h ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 12.5k • 🔱 1.5k • 1h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 10.9k • 🔱 994 • 12h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 9.8k • 🔱 710 • 1d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 8.5k • 🔱 412 • 6h ago

---

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)**

Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, "slop" 

`agent` `ai` `coding` `lowcode` `nocode`

⭐ 3.9k • 🔱 319 • 20h ago

---

**[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)**

Open-source database of 700+ cybersecurity skills for AI agents and security practitioners

`Python` `agent-skills` `ai-agents` `blue-team` `claude` `claude-code`

⭐ 3.3k • 🔱 318 • 13h ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 2.9k • 🔱 95 • 6d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 2.9k • 🔱 190 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*
