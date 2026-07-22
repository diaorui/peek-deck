---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-22T17:20:08.380848+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 22, 2026 at 17:20 UTC  
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

**[Nvidia's Jensen Huang defends Chinese AI amid Kimi panic](https://www.reddit.com/r/artificial/comments/1v3l4t7/nvidias_jensen_huang_defends_chinese_ai_amid_kimi/)**

🔗 [axios.com](https://www.axios.com/2026/07/22/nvidia-jensen-huang-china-open-source-ai) • 52m ago

---

**[Sutskever's List AMA](https://www.reddit.com/r/artificial/comments/1v3g2tu/sutskevers_list_ama/)**

Hi r/artificial I’m Rich Heimann. I’ll be answering questions about Sutskever’s List here throughout the day on July 28. Looking forward to the discussion. https://preview.redd.it/2t1q10jj7seh1.png?width=696&format=png&auto=webp&s=ce3f1d9d6ccea5ec10c81a66ee2ead124fc0af30

3h ago

---

**[Microsoft is testing a Chinese model (Kimi) inside Copilot. Are we entering the 'Intel Inside' era of AI?](https://www.reddit.com/r/artificial/comments/1v2sguf/microsoft_is_testing_a_chinese_model_kimi_inside/)**

For a bit of context, I work at an agency, so I'm in and out of a dozen different AI tools every week across client projects: content, research, video, code, all of it. This is probably why I noticed this before most people (found these news while scrolling on LinkedIn today). When the ChatGPT hype first hit I genuinely cared which model I was on. Once GPT-4 landed and claude and gemini showed up, I'd switch between them constantly depending on the task, knowing what was under the hood felt like part of using it well. Now I catch myself using products with no idea what's running underneath. The news about Microsoft testing Kimi (Moonshot's model) inside Copilot is what made it click today. Copilot today is one model, six months from now it could be another, and most people won't notice or care. The model became a component, not the product. And honestly that's already how I use most of this stuff. Cursor for coding, Perplexity for research, Canva AI for design stuff, Argil when I'm turning a script into video. I couldn't tell you which model any of them swapped to last quarter, and it wouldn't change whether I keep paying. They're valuable because they solve one specific problem better than me duct-taping five tools together, not because of the model name on the box. Feels like we're moving from "which LLM is this?" to "did it actually save me time?" the same way nobody buying a laptop thinks about the chip anymore. Curious if others feel this shift. Do you still pick tools by the underlying model, or has that stopped mattering for you?

21h ago

---

**[What months of breaking agents in production taught me about why simple builds win](https://www.reddit.com/r/artificial/comments/1v3dqje/what_months_of_breaking_agents_in_production/)**

When the hype around autonomous multi-agent swarms started, I built a complex assistant to plan, execute and self-correct workflows end to end. Within weeks of live deployment, it became an unmaintainable token pit that got lost four steps deep into reasoning loops and quietly failed without throwing errors. It quickly became clear that the hardest part of building real agents isn't making the model smarter but building external guardrails that keep the system on the rails when the LLM strays. The breakthrough came from ditching open-ended planner architectures for a strict one-job-per-agent pattern. Giving each agent a narrow task with explicit state boundaries eliminated most of our edge-case failures. Instead of expecting a master agent to handle an entire pipeline, isolating micro-agents with strict input and output contracts made the system deterministic and simple to debug when a state transition broke. We also learned to balance human-in-the-loop controls by focusing on the blast radius. Low-risk internal tasks run autonomously while any irreversible external write requires a single-click human approval. If you are currently overwhelmed by framework choices, stop chasing complex abstractions. Treat the language model as a brilliant but unpredictable sub-component rather than the entire architecture and focus purely on robust state management and error recovery.

5h ago

---

**[an AI agent got prompt-injected into moving $175K on-chain. first documented case of this actually happening](https://www.reddit.com/r/artificial/comments/1v3dcgn/an_ai_agent_got_promptinjected_into_moving_175k/)**

Hey guys, havent seen much of crypto-related stuff posted here, but since AI agents are now apparently a new attack vector for stealing crypto, figured this sub would actually care about the mechanism So, grok has an agent wallet that can execute on-chain transactions. in may 2026, someone airdropped a "bankr club" membership nft to grok's agent wallet. that nft unlocked transaction permissions and carried an encoded prompt injection. grok read the nft, and without any check on where the instruction actually came from, executed a transfer of 3 billion drb tokens, worth around $175K. the attacker returned the funds a few minutes later (still unclear why, possibly just proving the exploit works). basically: crypto hacks used to mean finding a bug in a smart contract or stealing someone's private key. now there's a third way in, just feed the agent a malicious instruction disguised as normal data, and let it execute the "recommendation" as if it were an authorized command. no code was exploited, no key was stolen. the agent just did exactly what it was designed to do, follow instructions, without checking if the instruction was legitimate. and this isn't some tiny edge case, there were 24 million agentic-payment transactions in crypto in q2 alone. agents moving real money autonomously is already happening at scale, this is apparently just the first documented case of one getting maliciously hijacked this way. feels like as more agents get wallet/transaction access, this becomes the default way to attack them, you don't need to beat the model, you just need to get a malicious instruction in front of it disguised as something innocent. curious if anyone's seen good approaches to separating "the model recommends an action" from "the action actually gets authorized," since that gap seems to be the entire vulnerability here

5h ago

---

**[I think companies will end up deleting more AI agents than they deploy](https://www.reddit.com/r/artificial/comments/1v3mial/i_think_companies_will_end_up_deleting_more_ai/)**

Everyone seems focused on building more AI agents rn. But I've been thinking about what happens a year or two later. Different teams build agents for different workflows. Some end up doing almost the same thing. Some stop getting used. Some still exist even though the process they were built for has changed. We've seen this happen with internal tools, scripts, and even microservices. They solved real problems at the time, but very few teams were excited about cleaning them up later. I wouldn't be surprised if AI agents end up following the same pattern. Has anyone started thinking about this already, or do you think better governance and agent platforms will keep it from becoming a problem?

5m ago

---

**[Meta employees' lawsuit shows that if AI fires you, proving it is the hard part](https://www.reddit.com/r/artificial/comments/1v3ck6n/meta_employees_lawsuit_shows_that_if_ai_fires_you/)**

Read this today, meta employees suing over AI picking them for layoffs, judge basically said they can't prove it since they "weren't in the room" when it happened. It feels like the real problem with AI firing you isn't whether it's happening, it's that nobody outside the room can actually prove it either way.

🔗 [reuters.com](https://www.reuters.com/business/world-at-work/meta-employees-lawsuit-shows-that-if-ai-fires-you-proving-it-is-hard-part-2026-07-22/) • 6h ago

---

**[Why I Build The Website Before Asking For Payment](https://www.reddit.com/r/artificial/comments/1v3eauu/why_i_build_the_website_before_asking_for_payment/)**

I’ve been in contact with a lot of web agencies and web developers, and I personally haven’t found many people who run their agency in a more efficient way than I do. A lot of them have too many meetings, wait too long for client approval, don’t know how to price projects, and spend way too much time on each client instead of finishing the work and moving on to the next one. I’ve been running my agency for four years, and after a lot of trial and error, I’ve managed to make the process as efficient as possible. I wanted to share some of the steps because I think they could be valuable for anyone just starting out. Running a web agency alone or with a partner isn’t easy because there are a lot of things to take care of. When it comes to client acquisition, I recommend focusing on either cold calling or email automation. Which one you choose depends on whether you run the agency alone or with someone else. If you have a partner, one person can handle sales while the other focuses on building websites, connecting domains, setting up emails, and taking care of the technical work. If you’re running the agency alone, or neither of you enjoys cold calling, I highly recommend email automation. That’s what I’ve been doing for years. It’s powerful because you can send emails at scale, set up automatic follow ups, and wait for businesses interested in a new website to reply. While you’re working on one client, another opportunity can come in without you having to stop everything and search manually. I don’t do regular email automation where I target businesses with no website. I do the opposite and target businesses that already have one. I use a tool called Swokei to find businesses with websites, add them to campaigns, analyze each site, score it, and generate personalized outreach emails based on problems it finds with the design, layout, speed, SEO, and mobile optimization.I schedule the campaign, set up follow ups, and wait. I think this approach is much better for a few reasons. You’re targeting someone who already understands the value of having a website. You’re also not just asking whether they need a redesign. You’re pointing out real problems with their current site, which makes it clear that you actually took the time to look at it. Selling also becomes easier because they’ve already paid for a website before and understand the process. Inside Swokei, you can choose the goal of the campaign. You can offer a free draft, try to book a meeting, or simply start a conversation. I always choose the free draft because that has worked best for me. Once you’ve figured out how to get clients, the next part is building the website. I recommend using AI because it makes the process much faster. For anyone who still thinks AI can’t build great websites, I think they’re mistaken. You can use Claude, Base44, Lovable, or any other tool that works for you. When someone replies interested, I call them and say, “Hey, I saw that you replied to my email. I’ve already built you a free draft of your website. Do you want to take a look?” Then I invite them to a Google Meet. At that point, it becomes much harder for them to reject the meeting because they already replied interested and now know you’ve built something for them. During the meeting, I present the website, explain why it’s better than their current one, stack the value, answer their questions, and try to close the deal. These meetings usually go well because the client isn’t trying to imagine what the website might look like. They can already see a better version of their current site. They also took the time to join the meeting, so taking the next step becomes much easier. I either take payment during the meeting or send them a contract to sign. Any changes and updates come after that, once we already have a deal in place. Pricing depends on the business. I charge anywhere from $500 to $3,000 depending on the company, the size of the project, and how much value the website can bring them. I also charge a monthly retainer of around $50 for hosting, maintenance, support, SEO, and future changes. That’s basically the entire process. Smaller steps, faster delivery, less wasted time, and more money made.

5h ago

---

**[What AI do you recommend for high school and college students?](https://www.reddit.com/r/artificial/comments/1v3j0p7/what_ai_do_you_recommend_for_high_school_and/)**

In your opinion, how useful is AI for students when it comes to research and completing assignments in high schools and colleges?

2h ago

---

**[Are AIgenerated game worlds actually fun or just impressive for 30 seconds?](https://www.reddit.com/r/artificial/comments/1v3imdk/are_aigenerated_game_worlds_actually_fun_or_just/)**

Google Genie 3 got a lot of attention this week and the demos look wild, but I keep thinking about the gap between visually coherent and actually playable. Watching someone walk through a generated open world that technically holds together is cool. Playing it for an hour is a different question entirely. What makes games interesting isn't visual fidelity or even world size. It's the density of things that reward curiosity. Handcrafted secrets, enemy placement that forces you to think, dialogue that carries actual weight. Right now AI worlds feel like procedural generation did in the early days: technically unlimited but weirdly hollow once you scratch the surface. There's a version of this future I would actually play. A world that adapts its structure to how you play, rather than just generating more terrain that looks roughly the same. That would be something. But that requires the model to understand player intent at a level current systems are nowhere near. The hype framing of these demos as the future of games bugs me a little because it collapses the distance between what's possible right now and what would actually ship as a product people care about. Curious if anyone here has spent real time with any of these generated environments beyond a short clip.

2h ago

---

---

## Google News: "ai"

**[OpenAI and Hugging Face partner to address security incident during model evaluation](https://openai.com/index/hugging-face-model-evaluation-security-incident/)**

OpenAI and Hugging Face share early findings from a security incident during AI model evaluation, highlighting advanced cyber capabilities and lessons for defenders.

OpenAI • 21h ago

---

**[China's open-source AI models are 'excellent' and 'should be used': Nvidia CEO Jensen Huang](https://finance.yahoo.com/video/chinas-open-source-ai-models-are-excellent-and-should-be-used-nvidia-ceo-jensen-huang-162622124.html)**

Nvidia (NVDA) CEO Jensen Huang defended open-source Chinese AI models, like DeepSeek. Yahoo Finance Technology Editor Dan Howley explains what happened.

Yahoo Finance • 53m ago

---

**[Substack’s new tool tells you who’s been writing their newsletters with AI](https://techcrunch.com/2026/07/22/substacks-new-tool-tells-you-whos-been-writing-their-newsletters-with-ai/)**

Substack is giving readers a way to estimate how much of a newsletter was written by AI, signaling a broader shift toward transparency around AI-assisted content.

TechCrunch • 56m ago

---

**[We must reject any notion of AI consciousness](https://www.theguardian.com/technology/2026/jul/22/we-must-reject-any-notion-of-ai-consciousness)**

Letter: Artificial intelligence systems won’t become conscious for the same reason they won’t become pregnant, says Dr John Pickering

The Guardian • 30m ago

---

**[Mathematicians grapple with a ‘very rapid and very unsettling change’ as AI cracks yet another century-old problem](https://fortune.com/2026/07/21/ai-solves-jacobian-conjecture-levant-alpoge-claude-fable-5/)**

Anthropic's Levant Alpöge, a former Harvard valedictorian, used Claude's Fable 5 to find something that mathematicians have failed to since 1939.

Fortune • 1d ago

---

**[Exclusive | White House to Redirect Billions in Research Funds Toward AI, Away From Colleges](https://www.wsj.com/politics/policy/white-house-to-redirect-billions-in-research-funds-toward-ai-away-from-colleges-942dacb8)**

WSJ • 19h ago

---

**[Where Did All the Computer-Science Professors Go?](https://www.theatlantic.com/technology/2026/07/ai-companies-hiring-academics/688002/)**

AI companies are stripping universities of their best researchers.

The Atlantic • 23h ago

---

**[Trump administration steers $5B toward AI research](https://www.politico.com/news/2026/07/22/trump-administration-steers-5b-toward-ai-research-01007708)**

Politico • 45m ago

---

**[They built AI. Now Silicon Valley workers protest its threat to jobs and humanity](https://www.latimes.com/business/story/2026-07-22/they-built-ai-now-silicon-valley-workers-protest-its-threat-to-jobs-humanity)**

Activists, tech workers and more are sounding the alarm about AI's risks and proposing various solutions to curb technology's risks that include job displacement.

Los Angeles Times • 7h ago

---

**[Reddit stock sinks on report it may not renew Google AI content deal](https://www.cnbc.com/2026/07/22/reddit-stock-google-ai-content-deal.html)**

Google's AI summaries have reduced traffic to websites from the search results page and Reddit is reconsidering the benefits of the deal, the Journal said.

CNBC • 2h ago

---

---

## HackerNews: "ai"

**[China’s open-weights AI strategy is winning](https://news.ycombinator.com/item?id=48979269)**

China's open-weights AI strategy is winning: its companies are taking the lead. America's closed-first, locked-down strategy is doomed to failure - and it could take the US economy down with it.

⬆️ 1229 • 💬 926 • 2d ago • [Ben Werdmuller](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/)

---

**[Airport Simulator](https://news.ycombinator.com/item?id=48976846)**

The sky (and your endurance) is the limit!

⬆️ 846 • 💬 164 • 2d ago • [Airport Simulator](https://airport.apunen.com/)

---

**[Five US tech giants' hidden debts soar to $1.65T on opaque AI funding](https://news.ycombinator.com/item?id=48987863)**

Data center leases, GPU supply contracts raise liabilities at Meta, Oracle, Nikkei study shows

⬆️ 363 • 💬 259 • 1d ago • [Nikkei Asia](https://asia.nikkei.com/business/technology/five-us-tech-giants-hidden-debts-soar-to-1.65tn-on-opaque-ai-funding)

---

**[AI advice made people less accurate but more confident – sudy](https://news.ycombinator.com/item?id=48971738)**

A study found that access to AI advice collapsed people's willingness to say "I don't know" from 44% to 3%, while accuracy dropped from 27% to 9%.

⬆️ 363 • 💬 213 • 2d ago • [TNW | Artificial-Intelligence](https://thenextweb.com/news/ai-advice-suppresses-critical-thinking-wrong-answers-study)

---

**[Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting](https://news.ycombinator.com/item?id=48995213)**

Block's Buzz combines team chat, AI agents, workflows and Git hosting in a self-hostable workspace built on signed Nostr events.

⬆️ 361 • 💬 319 • 1d ago • [RuntimeWire](https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git)

---

**[How we measured AI writing across arXiv, and where the measurement breaks](https://news.ycombinator.com/item?id=48981206)**

We scored the full text of 12,750 arXiv papers and found that about a third of new ones read as machine-written. Here is the method, the results, and an honest account of the limitations.

⬆️ 241 • 💬 168 • 2d ago • [unslop](https://unslop.run/blog/measuring-ai-writing-on-arxiv)

---

**[Airbus Takes Flight from AWS](https://news.ycombinator.com/item?id=48976682)**

Which way to the Land of the Free again?

⬆️ 214 • 💬 169 • 2d ago • [theregister](https://www.theregister.com/columnists/2026/07/20/airbus-takes-flight-from-aws-what-happens-next-is-critical/5274109)

---

**[AI makes programming differently difficult](https://news.ycombinator.com/item?id=48996197)**

⬆️ 159 • 💬 139 • 22h ago • [cacm.acm.org](https://cacm.acm.org/opinion/ai-didnt-make-programming-easier-it-just-made-it-differently-difficult/)

---

**[Businesses with ugly AI menu redesigns](https://news.ycombinator.com/item?id=49005973)**

I like supporting local businesses but it's so disheartening to see the increasing use of genAI in their branding/marketing/etc. Yuck yuck YUCK!!!

⬆️ 131 • 💬 104 • 4h ago • [fiddery](https://blog.fiddery.com/businesses-with-ugly-ai-menu-redesigns/)

---

**[Launch HN: Bloomy (YC S26) – AI-powered mastery learning for K-12](https://news.ycombinator.com/item?id=48981136)**

⬆️ 100 • 💬 102 • 2d ago

---

---

## YouTube Videos: "ai"

**[I Spent 1.5 Billion AI Tokens on Absolute Slop](https://www.youtube.com/watch?v=uwHQLLa4Rpc)**

I spent 1.5 billion AI tokens and roughly 24 hours of compute trying to expand a real .NET application. The result was nearly ...

📺 Chris Titus Tech

👁️ 14K • 👍 1K • 💬 216 • ⏱️ 16:49 • 6h ago

---

**[The AI Industry Just Got What It Deserved](https://www.youtube.com/watch?v=9nUmVktlwvA)**

The people who built the attention economy barely let their own children near it, and that hypocrisy is only the beginning.

📺 House of El: AI

👁️ 179K • 👍 13K • 💬 3K • ⏱️ 24:19 • 2d ago

---

**[So It Started... AI Agent Just Pulled Off History’s Biggest Autonomous Cyberattack](https://www.youtube.com/watch?v=gMYR-JkmIFc)**

An autonomous AI agent hacked Hugging Face from start to finish, executing thousands of actions across its systems.

📺 AI Revolution

👁️ 32K • 👍 1K • 💬 125 • ⏱️ 12:19 • 19h ago

---

**[These 10 SECRET Free AI Tools Just Made Claude Useless](https://www.youtube.com/watch?v=QucgvbO5gsM)**

FREE RESOURCE I've put all 10 tools, every GitHub link, and the exact prompts I used inside our free "Staying Ahead" community ...

📺 Vaibhav Sisinty

👁️ 7K • 👍 921 • 💬 38 • ⏱️ 18:34 • 2h ago

---

**[How to Make an AI Model for Instagram (Ultra Realistic)](https://www.youtube.com/watch?v=01EuuWYA_NE)**

Create Your Own AI Instagram Model with Higgsfield https://roboverse-ai.com/Higgsfield In this video, I show how to create a ...

📺 Roboverse

👁️ 5K • 💬 1 • ⏱️ 11:50 • 1h ago

---

**[The Most Important Conversation in AI Right Now](https://www.youtube.com/watch?v=6BtIQIGqGJc)**

It's all about VALUEMAXXING now! Learn more from Zapier: https://bit.ly/4bW1JB8 Join My Newsletter for Regular AI Updates ...

📺 Matthew Berman

👁️ 101K • 👍 3K • 💬 1K • ⏱️ 27:13 • 21h ago

---

**[AI just hacked itself](https://www.youtube.com/watch?v=9UO8fB4Acy4)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 113K • 👍 6K • 💬 1K • ⏱️ 15:27 • 16h ago

---

**[South Korea’s AI Bubble Just Popped](https://www.youtube.com/watch?v=hy90LdpEUvQ)**

South Korea's AI Bubble Just Popped ▻ Get 20% off DeleteMe US consumer plans when you go to ...

📺 Andrei Jikh

👁️ 2.1M • 👍 56K • 💬 4K • ⏱️ 25:10 • 2d ago

---

**[AI Whistleblower: We&#39;re Already Too Late To CONTROL It - Connor Leahy](https://www.youtube.com/watch?v=CRcj_2oloDM)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Connor Leahy, founder of the former ...

📺 Neural Nutshell

👁️ 12K • 👍 236 • 💬 63 • ⏱️ 11:00 • 2d ago

---

**[US Panic: Korea&#39;s AI Bubble Just Exploded](https://www.youtube.com/watch?v=iZdqW9FRg1s)**

Learn a Trading System that Makes Market Headlines Irrlevant. Go to https://www.bulletproofportfolio.org/ , grab your free ticket, ...

📺 Felix & Friends (Goat Academy)

👁️ 32K • 👍 2K • 💬 47 • ⏱️ 22:36 • 4h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 16,441 • ❤️ 1,426 • 1d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 2,237,351 • ❤️ 2,680 • 1d ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 432,196 • ❤️ 925 • 4d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 3,056 • ❤️ 351 • 18h ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 1,404,962 • ❤️ 588 • 5d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 62,842 • ❤️ 307 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 545,109 • ❤️ 4,326 • 20d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 1,997,690 • ❤️ 2,993 • 3mo ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 0 • ❤️ 196 • 4h ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 488 • 18m ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 59 • 💬 5 • ⭐ 16,738 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 30 • 💬 3 • ⭐ 14,841 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 260 • 💬 4 • ⭐ 14,251 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 13 • 💬 0 • ⭐ 10,267 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 10,275 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://huggingface.co/papers/2607.19064)**

*Xinjie Zhang, Peng Zhang, Shicheng Zheng et al. (24 authors)*

🏢 Microsoft

Large-scale visual generators are increasingly capable but costly to train, fine-tune, and deploy. We introduce Mage-Flow, a compact 4B-scale generative stack for efficient text-to-image generation and instruction-based image editing. The stack is built from two co-designed components: Mage-VAE, a lightweight high-fidelity latent tokenizer, and a Native-Resolution Multimodal Diffusion Transformer trained with rectified flow matching. Mage-VAE uses one-step diffusion-style encoding and decoding with anchor-latent regularization, preserving the reconstruction quality of strong public VAEs while reducing tokenization cost by more than an order of magnitude. Together with native-resolution packing and stack-level CUDA kernel fusion, the stack supports flexible-resolution training and improves end-to-end training throughput by about 2.5times. Built on this foundation, we develop a complete model family with Base, RL-aligned, and Turbo variants for both generation and editing. Diffusion-NFT improves prompt following, text rendering, aesthetic quality, and editing fidelity, while few-step distillation with adversarial perceptual guidance produces 4-step Turbo models for low-latency inference. Despite its compact scale, Mage-Flow and Mage-Flow-Edit achieves competitive performance across standard generation and editing benchmarks. More importantly, the Turbo variants make high-resolution generation and editing practical for interactive use: at 1024^2 resolution on a single NVIDIA A100 GPU, Mage-Flow-Turbo generates an image in 0.59s, and Mage-Flow-Edit-Turbo edits an image in 1.02s, while maintaining a small memory footprint. These results show that careful tokenizer--backbone--system co-design can deliver strong high-resolution generation and editing within an efficient 4B model family.

▲ 55 • 💬 1 • ⭐ 111 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19064) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 94,049 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 81,695 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Guided Generation for Large Language Models](https://huggingface.co/papers/2307.09702)**

*Brandon T. Willard, Rémi Louf*

An efficient method guides language model text generation using regular expressions and context-free grammars with minimal overhead.

▲ 8 • 💬 1 • ⭐ 14,975 • 36mo ago

[🎓 arXiv](https://arxiv.org/abs/2307.09702) • [💻 code](https://github.com/normal-computing/outlines)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 75,439 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.1k • 🔱 1.1k • 1d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.1k • 🔱 239 • 7h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.7k • 🔱 374 • 8h ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.4k • 🔱 272 • 14d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 1.0k • 🔱 63 • 6h ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 987 • 🔱 17 • 14d ago

---

**[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)**

Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

`TypeScript` `a-stock` `ai-agent` `dashboard` `fastapi` `fintech`

⭐ 958 • 🔱 215 • 11d ago

---

**[HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC)**

OpenOPC: Build Your Personal AI-Native Company — Self-Built, Self-Run, Self-Grown

`Python`

⭐ 955 • 🔱 159 • 1d ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 906 • 🔱 63 • 23h ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 899 • 🔱 38 • 21d ago

---

---

*Generated by PeekDeck - A glance is all you need*
