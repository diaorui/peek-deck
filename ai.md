---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-18T20:03:55.565169+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 18, 2026 at 20:03 UTC  
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

**[Prompt injection works on Telegram romance scam bots](https://www.reddit.com/r/artificial/comments/1uzxful/prompt_injection_works_on_telegram_romance_scam/)**

Tried prompt injection on a bot that was trying to romance scam me. Worked immediately. Instead of switching platforms I just asked it what its actual task was. It dropped the persona instantly. These things are everywhere now. How long until they're indistinguishable?

5h ago

---

**[Xi Jinping calls for more open-source AI: 'China is ready to be more open'](https://www.reddit.com/r/artificial/comments/1uzcgiq/xi_jinping_calls_for_more_opensource_ai_china_is/)**

Chinese leader Xi Jinping called for more open-source AI in a speech on Thursday. He encouraged "open-source, openness, collaboration, and sharing."

🔗 [Business Insider](https://www.businessinsider.com/xi-jinping-open-source-ai-us-competition-openai-anthropic-models-2026-7?utm_source=reddit&utm_medium=social&utm_campaign=insider-inthenews-sub-post) • 22h ago

---

**[The White House is dictating access to frontier AI models, shifting power from tech giants, sources say](https://www.reddit.com/r/artificial/comments/1v010pk/the_white_house_is_dictating_access_to_frontier/)**

The Trump administration is taking steps to control who gets access to the latest frontier models, sources familiar with the matter told CNBC.

🔗 [CNBC](https://www.cnbc.com/2026/07/17/white-house-ai-access-anthropic-openai.html) • 3h ago

---

**[I cut a RAG pipeline's response time from 90 seconds to 4. Never touched the model](https://www.reddit.com/r/artificial/comments/1uzzcef/i_cut_a_rag_pipelines_response_time_from_90/)**

Last year I worked with an AI startup, an Oxford spinout. Their product answered research questions through a RAG pipeline. It worked, but every query took around 90 seconds. Long enough that users were bailing before the answer even loaded. The obvious move is to blame the model and go bigger. That wasn't it. The retrieval layer was doing way more work than it needed to on every single query: bloated embeddings, no caching, redundant calls stacking up as the document set grew. I stripped that layer down. Response time went from 90 seconds to about 4, and cost dropped roughly 95%, mostly because the pipeline stopped repeating work it never needed to do in the first place. Separately, I also rebuilt the retrieval on Weaviate. That part wasn't about speed, it fixed accuracy issues in what the pipeline was actually retrieving. Same lesson as most AI performance problems I run into: it's rarely the model. It's the layer nobody's looking at.

4h ago

---

**[update on the browser extension that fact checks YouTube videos AS YOU WATCH](https://www.reddit.com/r/artificial/comments/1uze14i/update_on_the_browser_extension_that_fact_checks/)**

HI all, First, thank you so much for your feedback and interest in my project PopUpFactCheck. When I first posted about this July 1, I did not expect the reception it would get and I am so thankful to y'all. Some updates. You asked for Firefox, and it is now a Firefox add-on. It has new features. For example, using the up and down arrows on Chrome (or Option (⌥) + ↑/↓ on Firefox) you can scroll back and forth of the factcheck bubbles already displayed. The fact checking on live videos has improved. And it now does batch reporting on an entire video. Once again, Claude Code was a major tool in my development, and the AI that is used for orchestration is OpenAI GPT 5.4 nano and mini. In addition, there is an extensive waterfall of sources including the TheNewsAPI, various government and public health and other APIs, social, and web search powered by DDGS and Serper. PopUpFactCheck - Chrome Web Store PopUpFactCheck - Firefox add-on PopUpFactCheck - Homepage

21h ago

---

**[Which MCP servers are worth installing for non-dev work in 2026?? Sharing what I found beyond coding](https://www.reddit.com/r/artificial/comments/1uzwdtm/which_mcp_servers_are_worth_installing_for_nondev/)**

Out of ~30 MCP servers I tested for non-dev work over 4 months, I kept 8 in daily rotation. The ecosystem hit 10K+ servers by early 2026 (22K+ on Glama by May) but most are either demo-ware or duplicate coverage. Sharing the honest cut because "MCP for non-devs" posts usually list every option without saying which ones survive real use. The keepers for marketing/social. PostFast handles cross-platform scheduling from Claude, 11 platforms including Google Business Profile which nobody else keeps now that Buffer dropped it, €10/mo. Analytics are thinner than Metricool so I run both. Metricool at $22/mo covers analytics + scheduling with an official server at ai.metricool.com/mcp. Vista Social has 35+ MCP tools at agency scale ($120/mo). For SEO research, Ahrefs MCP is solid but pricey ($129/mo starter), Semrush overlaps. Tally is the free win, 21 MCP tools for forms with OAuth setup any non-dev can wire up in 2 min. Docs and knowledge work. Notion MCP is the obvious install if you already pay for it, lets Claude create pages, update databases and read across your workspace. Slack MCP is decent but read/summarize is where it shines, message posting still feels risky without human approval. Linear MCP for project tracking works well if that's your stack. Airtable overlaps with Notion for most workflows, only worth it if it's your source of truth. CRM and sales. HubSpot MCP is the best-supported CRM server, full read/write, works with Claude and ChatGPT out of box. Salesforce has AgentForce but no open MCP server on par with HubSpot yet. For outbound sales specifically, Amplemarket scored highest in recent benchmarks (find, enrich, sequence, enroll all in one), Apollo is close second and cheaper. Ads and analytics. BigQuery MCP auto-enables on all Google Cloud projects after March 2026 so most already have it. Google Ads MCP, Meta Ads MCP and GA4 MCP each ship official servers, downside is you need read-only setup or Claude will fumble a tool call and mess with budgets. SegmentStream unifies attribution across channels which is the missing piece for most stacks. What I skipped. Zapier/Make MCP feel redundant if you already have direct servers for the tools they wrap, extra layer of latency and cost. Airtable if Notion covers you. Anything on Glama with under ~50 stars, ecosystem quality is a coin flip and 41% of public MCP servers have no auth per security audits, only 8.5% use OAuth. Stick with vendor-maintained (official) or well-audited community ones.

6h ago

---

**[Need a platform that can create and update a sleep log](https://www.reddit.com/r/artificial/comments/1v05nln/need_a_platform_that_can_create_and_update_a/)**

After massive failures by Copilot and Claude, I need an AI platform that is free and can save an ongoing log. I have had two strokes and a heart attack and am in a wheelchair and genuinely unable to work. I have a phone hearing with an Administrative Law Judge for SSDI on September 7 and I need to create a sleep log including naps that I can update on a regular basis. Can anyone suggest an AI that can facilitate such a request?

8m ago

---

**[When I made LLMs argue with each other, they started making up citations to win. Sycophancy wasn't the only failure mode.](https://www.reddit.com/r/artificial/comments/1v05mzz/when_i_made_llms_argue_with_each_other_they/)**

Some context. I've been running setups where a few LLM personas debate a question, then a separate neutral pass pulls out where they actually disagree. The whole reason I started was sycophancy. One model on its own just agrees with whatever you say, so I wanted models that would actually push back on each other. That part worked. But two things happened that I didn't see coming. First, arguing turns models into confident fabricators. Once a model is trying to "win", it starts citing sources, URLs, author names, specific figures, that were never in the retrieved material. It's not random hallucination, it's persuasive hallucination, because in an argument a citation is basically a weapon. I ended up adding a dumb deterministic check that flags any cited URL that isn't in the actual retrieved corpus. Just telling the model "only cite real sources" in the prompt barely did anything, moved it maybe 6 points. Second, if you let a model pick the debaters, the panel comes out unanimous almost every time. Generating all the personas from one model at low temperature quietly lines up their priors. You think you've got a debate, you've actually got one model wearing five hats. The takeaway for me: making models disagree is really easy to fake and pretty hard to do for real. Most of the actual work is in the verification layer, not the personas. Anyone else working on multi-agent debate or adversarial verification? Still an open question for me whether fabrication-under-pressure is just a property of any adversarial LLM setup, or something you can actually design out at the architecture level instead of catching after the fact.

9m ago

---

**[This is bad...right?](https://www.reddit.com/r/artificial/comments/1uzzqyf/this_is_badright/)**

So this has happened to me a few times this year. I will be listening to Youtube music videos in the background as I am working, reading, or just chilling and a song will come on that just speaks to me. Being on this forum you can see where its going. I have found that several of these songs are written, created, sung, etc exclusively by AI. On one hand its super impressive....on the other hand there is an undeniable part of me that does not like this trend. To me music has always been about the expression of emotion by humans in a way that few things can do. Now we have computers just writing and singing damn good songs. I'm torn on this. How long until an AI tops the billboard top 100? What are your feelings on this?

3h ago

---

**[Comparing AI predictions before the World Cup final](https://www.reddit.com/r/artificial/comments/1uzw659/comparing_ai_predictions_before_the_world_cup/)**

With the final coming up, I went back and looked through the AI predictions on SportEval from the quarterfinals. Although all four teams that advanced were the favorites, none of the matches felt as comfortable as the predictions suggested. A few key moments could easily have changed the outcome. Several models, including Claude Opus 4.8, DeepSeek V4 Pro, GPT 5.5, Gemini, and GLM, all predicted the correct winners, but they reached those conclusions in very different ways. Take France vs Morocco as an example. Most models backed France, but for different reasons. Claude focused on France's defensive quality and Mbappé's influence. DeepSeek emphasized FIFA rankings and squad value. GPT 5.5 relied more on recent form and squad depth. France won, but Morocco still created plenty of dangerous chances, showing that AI can identify long-term advantages but can't predict the moments that decide a match. The semi-finals became much more interesting because the models no longer agreed. Some predicted a Spain vs Argentina final, while others expected France or England instead. Once only the strongest teams remained, each model seemed to value different factors. That's why I enjoy following AI predictions. They don't change which team I support, but they help me notice tactical details, squad strengths, and different ways of analyzing the same match. Football will always be unpredictable, but seeing how different AI models interpret the game makes watching it even more interesting. With only the final left, I still slightly favor Spain. More than the result itself, I'm curious to see which AI model ends up reading the game most accurately.

6h ago

---

---

## Google News: "ai"

**[MLB restricts using dugout iPads for AI-assisted in-game strategy](https://www.espn.com/mlb/story/_/id/49385415/mlb-restricts-dugout-ipad-use-prevent-artificial-intelligence-game-decision-making)**

ESPN • 1d ago

---

**[IBM CEO Arvind Krishna Has Nowhere to Hide From AI](https://www.wsj.com/tech/ibm-ceo-arvind-krishna-has-nowhere-to-hide-from-ai-c9ff290f)**

WSJ • 4h ago

---

**[New York school district to deploy humanoid robot in classrooms this fall](https://www.foxnews.com/media/new-york-school-district-deploy-humanoid-robot-classrooms-fall)**

A humanoid robot named Sally will assist students in a Western New York school district this fall as educators test AI integration in teaching.

Fox News • 1h ago

---

**[China’s Moonshot AI Unveils Kimi Model, Threatening America’s Lead](https://www.nytimes.com/2026/07/17/business/china-ai-moonshot-kimi.html)**

The New York Times • 23h ago

---

**[China just erased America's AI lead](https://www.axios.com/2026/07/17/china-ai-kimi-k3-open-source-anthropic-opus)**

Axios • 15h ago

---

**[AMD (AMD) Stock Faces Fresh AI Pressure After China Unveils Kimi K3](https://finance.yahoo.com/markets/stocks/articles/amd-amd-stock-faces-fresh-190703527.html)**

China’s Moonshot Kimi K3 AI model, described as the largest open AI model so far, has been launched and is positioned as a lower cost alternative that scores strongly on coding benchmarks. The announcement has raised questions about US leadership in AI technology and added pressure to US chip stocks, including NasdaqGS:AMD. The development highlights changing competitive pressures for global semiconductor and AI hardware suppliers. For AMD, which sells CPUs and GPUs that are used in AI...

Yahoo Finance • 56m ago

---

**[Green says Mets fully compliant on AI after report of usage](https://abc7ny.com/post/green-says-mets-fully-compliant-ai-report-usage/19533759/)**

Mets interim manager Andy Green said the club is fully compliant with Major League Baseball when asked about a report that singled out his organization for using artificial intelligence for in-game strategy decisions.

ABC7 New York • 58m ago

---

**[Silicon Valley Has Lost Its Biggest Advantage](https://www.theatlantic.com/technology/2026/07/data-center-ai-heavy-industry/687990/)**

In the data-center age, the business of tech companies is more like oil-refining than coding.

The Atlantic • 8h ago

---

**[Netflix Paid $587 Million for Ben Affleck’s AI Startup InterPositive](https://variety.com/2026/film/news/netflix-paid-587-million-ben-affleck-ai-interpositive-1236815111/)**

Netflix paid $587 million in cash when it purchased Ben Affleck's AI startup InterPositive, the company disclosed in a federal filing.

Variety • 22h ago

---

**[Netflix bought Ben Affleck's AI startup for $587 million](https://mashable.com/tech/netflix-paid-587-million-for-ben-affleck-ai-startup-interpositive)**

Netflix acquired Affleck's startup InterPositive in March.

Mashable • 1h ago

---

---

## HackerNews: "ai"

**[Kaiser nurses say AI, surveillance are making their jobs and patient care worse](https://news.ycombinator.com/item?id=48952880)**

⬆️ 537 • 💬 364 • 21h ago • [localnewsmatters.org](https://localnewsmatters.org/2026/07/15/kaiser-nurses-say-ai-workplace-surveillance-are-making-their-jobs-and-patient-care-worse/)

---

**[The state of open source AI](https://news.ycombinator.com/item?id=48947825)**

⬆️ 471 • 💬 344 • 1d ago • [stateofopensource.ai](https://stateofopensource.ai/)

---

**[Why do AI company logos look like buttholes? (2025)](https://news.ycombinator.com/item?id=48956924)**

A humorous exploration of the uncanny resemblance between AI company logos and human anatomy. Discover why circular, gradient-based designs dominate the AI industry, and what this design convergence tells us about branding in tech.

⬆️ 395 • 💬 135 • 8h ago • [VelvetShark](https://velvetshark.com/ai-company-logos-that-look-like-buttholes)

---

**[$100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol](https://news.ycombinator.com/item?id=48939524)**

We gave Claude Fable 5 and GPT-5.6 Sol the same song, a budget, web search, and local ffmpeg, then let each autonomously direct a music video.

⬆️ 393 • 💬 528 • 2d ago • [TryAI](https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6)

---

**[LM Studio Bionic: the AI agent for open models](https://news.ycombinator.com/item?id=48939662)**

The AI agent made for open models, built to get things done.

⬆️ 326 • 💬 129 • 1d ago • [LM Studio Blog](https://lmstudio.ai/blog/introducing-lm-studio-bionic)

---

**[What AI did to stackoverflow in a graph](https://news.ycombinator.com/item?id=48956949)**

⬆️ 315 • 💬 363 • 8h ago • [data.stackexchange.com](https://data.stackexchange.com/stackoverflow/query/1953768#graph)

---

**[Governments, companies, nonprofits should invest in free, open source AI [pdf]](https://news.ycombinator.com/item?id=48927095)**

⬆️ 293 • 💬 108 • 2d ago • [siegelendowment.org](https://www.siegelendowment.org/wp-content/uploads/2026/07/fortune-david-siegel-open-source-ai.pdf)

---

**[FAA lets Boeing sign off on 737 MAX, 787 airworthiness certificates again](https://news.ycombinator.com/item?id=48952439)**

The move is a vote of confidence in Boeing from the U.S. government.

⬆️ 192 • 💬 114 • 22h ago • [CNBC](https://www.cnbc.com/2026/07/17/faa-boeing-737-max-787.html)

---

**[How to Train a Gen AI Kick Drum Model on Your Old Linux Desktop with 6GB VRAM](https://news.ycombinator.com/item?id=48935687)**

⬆️ 160 • 💬 84 • 2d ago • [zhinit.dev](https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model)

---

**[German AI consortium releases Soofi S, an open 30B model that tops benchmarks](https://news.ycombinator.com/item?id=48937756)**

A German research consortium has released Soofi S 30B-A3B, an open language model trained entirely on Deutsche Telekom's cloud infrastructure in Munich. The model uses an efficient hybrid architecture that activates only a fraction of its 31.6 billion parameters per token, keeping throughput steady even at very long contexts. With a training dataset deliberately weighted toward German, Soofi S tops all fully open competitors on both German and English benchmarks.

⬆️ 144 • 💬 34 • 2d ago • [The Decoder](https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german/)

---

---

## YouTube Videos: "ai"

**[China&#39;s new AI just shocked Wall Street](https://www.youtube.com/watch?v=_fNhzoiZdNI)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 55K • 👍 4K • 💬 1K • ⏱️ 14:15 • 7h ago

---

**[ls America losing control of the AI race?](https://www.youtube.com/watch?v=jv6hBaCtsFg)**

US tech firms have long feared that their Chinese competitors could catch them up in the AI race, but they thought they had more ...

📺 Sky News

👁️ 19K • 👍 603 • 💬 167 • ⏱️ 6:28 • 8h ago

---

**[Anthropic CEO: AI Is Not Conscious , It&#39;s Much WORSE Than That - Dario Amodei](https://www.youtube.com/watch?v=2Lt0AtM4JW8)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Anthropic CEO Dario Amodei warns that AI ...

📺 Neural Nutshell

👁️ 39K • 👍 783 • 💬 196 • ⏱️ 20:51 • 2d ago

---

**[AI Expert WARNS: Mass Job Loss Is Coming By 2027 - Tristan Harris](https://www.youtube.com/watch?v=GSoqVsdkvNA)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Tristan Harris warns that mass AI ...

📺 Neural Nutshell

👁️ 7K • 👍 182 • 💬 35 • ⏱️ 17:41 • 1d ago

---

**[Is This the Biggest AI Release of 2026? (China’s New DeepSeek Moment)](https://www.youtube.com/watch?v=V0RsocRqjIU)**

China's Moonshot AI just released Kimi K3, the world's largest open-weight AI model. It rivals leading American systems, ...

📺 AI Revolution

👁️ 31K • 👍 1K • 💬 129 • ⏱️ 14:29 • 21h ago

---

**[China may have just turned up the heat the the AI race](https://www.youtube.com/watch?v=jGuf27ySl_Q)**

Tenex co-founder and co-managing partner Arman Hezarkhani breaks down the features of China's Kimi K3 A.I. model, ...

📺 Fox Business

👁️ 30K • 👍 456 • 💬 242 • ⏱️ 6:33 • 23h ago

---

**[AI Bubble vs Dot Com Crash. History is REPEATING](https://www.youtube.com/watch?v=zWJ-g5u9Rqs)**

The AI bubble and the Dot-Com crash may be separated by more than 20 years, but the warning signs look disturbingly familiar.

📺 The Infographics Show

👁️ 34K • 👍 2K • 💬 260 • ⏱️ 21:54 • 4h ago

---

**[Why AI Suddenly Looks Extra Bubbly](https://www.youtube.com/watch?v=VS00sg8rsnE)**

Take back your privacy- start using Proton Mail for free: http://proton.me/tldr Watch the Full Trailer: https://youtu.be/mP1b-33Qnqw ...

📺 TLDR News Global

👁️ 184K • 👍 6K • 💬 1K • ⏱️ 8:56 • 11h ago

---

**[AI slop is leaking into real life](https://www.youtube.com/watch?v=PSyAhMGkKy4)**

so let's FIGHT the plague of AI slop by celebrating HUMAN creators! See you tonight for our first ever THE CREATOR AWARDS, ...

📺 JJJacksfilms

👁️ 118K • 👍 10K • 💬 3K • ⏱️ 3:50 • 1d ago

---

**[13 EASY Claude AI Side Hustles You Can Try If You Get Laid Off](https://www.youtube.com/watch?v=NFuoK8D8DUY)**

ONE-TIME YOUTUBE LIVE TRAINING THIS WEEK: https://go.thecontentgrowthengine.com/yt1livedes-07-18-2026 Apply For ...

📺 Shane Hummus

👁️ 8K • 👍 398 • 💬 29 • ⏱️ 26:38 • 20h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 12,456 • ❤️ 1,039 • 2d ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 301,893 • ❤️ 718 • 13h ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 1,218,815 • ❤️ 431 • 1d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 541,662 • ❤️ 4,117 • 16d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 2,112,869 • ❤️ 2,303 • 4d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 388 • 7h ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 10,445 • ❤️ 433 • 8d ago

---

**[OvisOCR2](https://huggingface.co/ATH-MaaS/OvisOCR2)**

*ATH-MaaS*

OvisOCR2 is a compact 0.8B multimodal model for end-to-end document parsing, generating Markdown from document images. It excels at extracting text, formulas, tables, and visual regions in natural reading order, achieving state-of-the-art performance on benchmarks like OmniDocBench.

`image-text-to-text` `853.0M`

⬇️ 13,750 • ❤️ 164 • 2d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 2,190,398 • ❤️ 2,858 • 3mo ago

---

**[MOSS-Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize)**

*OpenMOSS*

MOSS-Transcribe-Diarize is an end-to-end audio understanding model that performs joint speech transcription and speaker diarization for long-form audio in over 50 languages. It generates compact, timestamped transcripts with speaker labels ([S01], [S02]) in a single pass, suitable for meetings, podcasts, and lectures.

`audio-text-to-text` `908.5M`

⬇️ 86,385 • ❤️ 255 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 28 • 💬 3 • ⭐ 12,406 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 44 • 💬 1 • ⭐ 1,287 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 93,527 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 17 • 💬 2 • ⭐ 20,905 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 81,155 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 257 • 💬 4 • ⭐ 13,065 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 74,977 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 60 • 💬 3 • ⭐ 1,425 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

---

**[Continuous Audio Language Models](https://huggingface.co/papers/2509.06926)**

*Rouard Simon, Orsini Manu, Roebel Axel et al. (5 authors)*

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io

▲ 11 • 💬 0 • ⭐ 7,716 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 63 • 💬 1 • ⭐ 827 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.9k • 🔱 1.0k • 1d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 2.9k • 🔱 213 • 1d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.6k • 🔱 365 • 1d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.3k • 🔱 264 • 10d ago

---

**[ray-r-ren/agent-apprenticeship](https://github.com/ray-r-ren/agent-apprenticeship)**

The living ecosystem where AI agents complete tasks through workflow loops, improve through iterative execution, are evaluated by mentor agents or humans in the loop, and turn completed work into reusable work experience and data to improve future agents.

`Python` `agent-apprenticeship` `agent-economy` `agent-experience` `agent-learning` `agent-traces`

⭐ 1.3k • 🔱 56 • 12d ago

---

**[sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API)**

Reverse engineered Windows Copilot into an OpenAI-compatible API. Access GPT-4 and GPT-5 models through a simple REST interface without API keys or billing.

`Python` `ai` `ai-agents` `api` `copilot` `llm`

⭐ 1.1k • 🔱 374 • 21d ago

---

**[modiqo/skillspec](https://github.com/modiqo/skillspec)**

SkillSpec makes agent skills followable, testable, and provable with Doctor risk reports, guided imports, structured contracts, and alignment proof.

`Rust` `ai` `ai-agents` `ai-evals` `ai-tool`

⭐ 991 • 🔱 61 • 5d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 990 • 🔱 17 • 10d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 941 • 🔱 58 • 4d ago

---

**[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)**

Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

`TypeScript` `a-stock` `ai-agent` `dashboard` `fastapi` `fintech`

⭐ 894 • 🔱 200 • 7d ago

---

---

*Generated by PeekDeck - A glance is all you need*
