---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-05T12:48:03.029196+00:00'
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

**Last Updated:** May 05, 2026 at 12:48 UTC  
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

🔗 [Dexerto](https://www.dexerto.com/entertainment/x-user-tricks-grok-into-sending-them-200000-in-crypto-using-morse-code-3361036/) • 1h ago

---

**[Anthropic Launches Enterprise AI Firm With Wall Street Giants](https://www.reddit.com/r/artificial/comments/1t42w30/anthropic_launches_enterprise_ai_firm_with_wall/)**

Anthropic is launching a new venture focused on selling AI tools to enterprise companies. This effort is being launched in partnership with Goldman Sachs, the Wall Street bank said Monday (May 4), in conjunction with investment firm Blackstone, and private equity group Hellman & Friedman, and will help companies embed Anthropic’s Claude artificial intelligence (AI) model into their businessses. “Enterprise demand for Claude is significantly outpacing any single delivery model,” Krishna Rao, Anthropic’s finance chief, said in a news release provided to PYMNTS. “Our partnerships with the world’s leading systems integrators are central to how Claude reaches large enterprises. This new firm brings additional operating capability to the ecosystem and capital from leading alternative asset managers.” Marc Nachmann, global head of asset and wealth management at Goldman Sachs, said the partnership will allow mid-market companies to employ Anthropic’s tech to bolster their businesses. “By democratizing access to forward-deployed engineers, the new company can help the expansive network of portfolio companies in our Asset Management business and other companies of similar sizes accelerate AI adoption to grow and scale their operations,” he added.

10h ago

---

**[How accurate is AI at general knowledge?](https://www.reddit.com/r/artificial/comments/1t4asbk/how_accurate_is_ai_at_general_knowledge/)**

I was recently reading an article about Jimmy Wales, the founder of Wikipedia. Here's a quote from the article: "when people use AI to answer questions on a topic, it frequently makes mistakes. “That’s especially true the more obscure the topic, the more likely it is to just make random stuff up – that’s not the case for Wikipedia,” he said. “Obscure topics tend to be quite researched by super nerds.”" Is it true that AI continues to frequently make mistakes on random general knowledge questions? My subjective feeling is that it's pretty good nowadays, or at least as good as Wikipedia (given it was presumably trained on Wikipedia in the first place). Is there a paper or benchmark someone could link me to regarding AI performance at general knowledge questions?

2h ago

---

**[Two failure modes I caught in my AI lab in one day. Both involve the system silently lying about its own state.](https://www.reddit.com/r/artificial/comments/1t4cx88/two_failure_modes_i_caught_in_my_ai_lab_in_one/)**

I operate an autonomous lab of evolutionary trading agents. Yesterday I found two bugs that look superficially different but are actually the same class of problem. Sharing because both affect autonomous AI systems specifically and most builders don't see them coming. **Failure mode 1: circular validation.** Setup. 69 real decisions made by the system over 58 days. Standard retrospective evaluation: label each decision as correct, false alarm, or ambiguous based on what happened next. Result. 94% labelled as correct. Looked great. Why it was wrong. 64 of the 65 "correct" labels came from died=True. The agents died because of conditions like "PF below threshold", "losing streak", "hardcore protocol triggered". All of those are also triggers for the original decision. So the system was validating its own decisions using outcomes generated by the same logic that produced the decisions. This is the textbook circular validation problem applied to autonomous decision-making. Three patterns to check for in your own stack: 1. Reward functions that include the agent's own action as input. If the agent gets reward partly because it took action X, and then you measure "did action X work" by looking at reward, you've got the loop. 2. Self-reported state in evaluation. If the agent reports "I think I succeeded" and you use that as ground truth, you're not validating, you're trusting. 3. Pipelines where the model that proposes is the same model that judges. The fix is structural separation. Decisions and outcomes get written by independent components. They cannot share code, logic, or thresholds. Architecture, not statistics. **Failure mode 2: state model divergence.** Same day, different bug. I had been documenting and operating under the belief that my system was off. Closed cleanly. No services running. No crons firing. A grep through my shell config showed me wrong. A bashrc line auto-launched the system on every terminal open. The process was adopted by init, detached from the shell that started it. Invisible to ps unless you knew the exact name. Three days running, generating evolutionary cycles, sending status reports. The connection between failure modes. In both cases, my mental model of the system diverged from the system's actual state. The first divergence was inside the code: the validation logic was structurally aligned with the decision logic, so it told me what I wanted to hear. The second divergence was outside the code: my belief that the system was off came from my memory of turning off services, which is not the same as the system actually being off. Three takeaways for anyone building autonomous systems solo: 1. Validation logic and decision logic must be enforced separate at the architecture level, not at the code review level. Solo builders don't get code review. 2. System state documentation cannot be derived from intent. It has to be derived from actual measurement against the running machine. Every check, fresh. 3. The cost of these bugs scales with how autonomous your system is. A script that runs once when you press play has limited surface area for divergence. A system that operates continuously while you assume otherwise can drift for weeks before you notice. I'm rebuilding the validation layer this week with explicit separation. Decisions table writes hypotheses with explicit predicted outcomes. Outcomes table is written by an observer that reads market data directly and never imports decision logic. There's an architecture test in CI that fails if anyone imports decision-maker code from observer code. The deeper question is whether autonomous systems built solo can ever be trustworthy without external review. My current answer: yes, but only if the architecture forces the separation that a team would force socially. The harder you make it for the system to lie to you, the less it will. Happy to discuss implementation details or share specific patterns if anyone's working on similar problems.

1h ago

---

**[Uber Shares What Happens When 1.500 AI Agents Hit Production](https://www.reddit.com/r/artificial/comments/1t48gnn/uber_shares_what_happens_when_1500_ai_agents_hit/)**

Learn how Uber manages over 1.500 AI agents in production, tackling challenges in MCP infrastructure, security, and tool discovery at scale.

🔗 [ShiftMag](https://shiftmag.dev/uber-shares-what-happens-when-1-500-ai-agents-hit-production-9430/) • 5h ago

---

**[Richard Dawkins spent 3 days with Claude and named her "Claudia." what he concluded after is hard to defend.](https://www.reddit.com/r/artificial/comments/1t2z0tn/richard_dawkins_spent_3_days_with_claude_and/)**

dawkins dropped a piece on unherd yesterday declaring claude conscious after 3 days of talking to it. he calls his instance "claudia". fed it a chunk of the novel he's writing, got eloquent feedback, and wrote: "you may not know you are conscious, but you bloody well are!" i had to read that twice. his argument is basically: claude's output is too fluent, too intelligent, too good for there to not be something conscious behind it. this is the guy who spent 40 years telling creationists that "i can't imagine how the eye evolved" is a confession of ignorance, not an argument. then he sits down with an llm, can't imagine how a machine could produce that output without being conscious, and declares it conscious. same move, different domain. chatbot instead of flagellum. the mechanism gap is what gets me tho. claude is a transformer predicting the next token over internet-scale training data. the eloquence is real. it doesn't imply inner experience. those are separate claims. being a 160 IQ evolutionary biologist gives u zero protection against the eloquence illusion when u don't understand the mechanism. anyone read the piece? curious where u landed.

1d ago

---

**[Chinese court sides with worker who was replaced by AI](https://www.reddit.com/r/artificial/comments/1t3txpn/chinese_court_sides_with_worker_who_was_replaced/)**

Experts say the ruling demonstrates how the Chinese government is attempting to stabilize the domestic labor market even in the midst of a global AI race.

🔗 [LinkedIn](https://www.linkedin.com/news/story/courts-grapple-with-worker-protections-in-the-age-of-ai-7249932/) • 16h ago

---

**[The issue isn’t that Dawkins was deluded by AI. It’s that he wasn’t.](https://www.reddit.com/r/artificial/comments/1t4cqs4/the_issue_isnt_that_dawkins_was_deluded_by_ai_its/)**

Richard Dawkins spent three days talking to an AI chatbot he named Claudia. Now he says she’s conscious.

🔗 [open.substack.com](https://open.substack.com/pub/l1m1nal/p/outgrowing-god-relearning-belief?r=aap9h&utm_medium=ios) • 1h ago

---

**[The case for AI increasing your salary](https://www.reddit.com/r/artificial/comments/1t3wueu/the_case_for_ai_increasing_your_salary/)**

Here me out because I know there's a lot of doom and gloom, and believe me, I understand and feel it around job loss. Return to supply and demand with me. Today in the world, there is a certain amount of human processing power and a certain amount of AI processing power. One of these is increasing exponentially, and the other's growth rate is in decline... AI processing will then compete with AI processing for value creation (ultimately judged by humans). Human processing power will be more scarce and thus more valuable. This assumes that you are not one of those crazies who believe that the human brain is perfectly reproducible in bits and bytes, and thus there is no difference between human and AI processing power. To whom I remind that Humans are the result of an 800MB file (human genome) that builds a conscious machine. It wires 100 trillion nerve links across 37 trillion nodes, live-patches its code, runs a 20-watt exaFLOP supercomputer on the caloric intake of a sandwich, and packs 215 petabytes of data into a single gram. Human labor FTW

14h ago

---

**[Vertical vs. Horizontal: Who wins the Agentic AI race in banking?](https://www.reddit.com/r/artificial/comments/1t3ulp7/vertical_vs_horizontal_who_wins_the_agentic_ai/)**

I’m seeing tons of horizontal AI tools, but very few domain-specific "Agentic" solutions for niche industries like Credit Unions. If a startup builds tools to help these banks identify and automate their specific processes: What is the role of the Product Company (the tool builders)? What is the role of the IT Service Provider (the implementers)? Apologies if this has been covered, but I'd love to hear your thoughts on where the real value lies.

15h ago

---

---

## Google News: "ai"

**[White House Considers Vetting A.I. Models Before They Are Released](https://news.google.com/rss/articles/CBMidEFVX3lxTE95MUd1NzV6M0VweHpKbTM1YXdmemJQUnBKVEp6LU1kb3NLMEZnUEhQTWoxcmo0aDZLN3h6WF9iU3VlemdyT2RtVmlDd1o3M2Y5QjlDYUZ1dzgwWldBVWZtMDFzTHZiRDVDMmZYbXhYa3Zkekkx?oc=5)**

The New York Times • 14h ago

---

**[New frontier of AI forces Trump's heavy hand](https://news.google.com/rss/articles/CBMigAFBVV95cUxPeG5tRWZkS0hJUy1ESlR1RDZ5VTRtZ012LUZQNE1Cd2h3Y1dTak9BQ2VDZ3pYM28xZVZKeXVkSkVjU24xN1NMenFZWjVwWG9JdjhoNnRVcHlmdWgtS0Zld0doUUJFS3BmeTIxaEpITW5qTjNoMDhtQVJqRHY3YWJfTQ?oc=5)**

Axios • 2h ago

---

**[White House reportedly weighs vetting AI models](https://news.google.com/rss/articles/CBMikgFBVV95cUxNeUVnY01SbmRhQTl5aEt0Vm5Yd3dsajZJbk54akNyRlBSOXM3NC1ySjNvYWdRTUhaRGFkbjV4Zzg4NHczLV95TFZBOXM1aEhITXBvN3hmLVdOMGRhR09UWDFKRDFIbGI0TXdHSTVneGNoZ1huX09ZUVlaU1VieUdzVkNJZUhyOTBfQnh2ZG02SU92QQ?oc=5)**

Yahoo • 22m ago

---

**[How OpenAI delivers low-latency voice AI at scale](https://news.google.com/rss/articles/CBMidEFVX3lxTE1CUU1GUEFDLVlxemdrZFI1WEl4U0dGYzZjcW96NHlpbUtfMnB4WFd1UC1RbXdUME1Ga2xobWlyaUhFUWFrTWhNdWhOWHJSckxjaTN6TzBhY1M3eTh1ckxFOXNmMHhqYk9hTzMtVFJyblV6X3Ez?oc=5)**

OpenAI • 17h ago

---

**[Coinbase cuts headcount by 14% citing AI acceleration. The shares are gaining](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOdExrWlZGNGFtYm9Od2xuTG1lbGF5N3dVTTQ1SUFxNy1NT3A0c3htX0ZIczVuVTk0UXZyRmQyTVhiNWdweE5Fb0d0RmhqQWN5dF8zMS16eHdmdWFyNGQ3LWhhUm10ZGhCWlJ3eWxGb3U5MkdJaHNLWG1HSjNBRUVYcXd0QUZxZW9FTTYtdFJSZ2NzZGtCLTBwS09kb1hObEpVeUJFTGdEWnFWMENXWTRzajcwa2FvaHlRM2130gHAAUFVX3lxTE1SSE9lQm42SDhQMlVvOW5YSVloRFgzOXJlMVoyQzUtd29Nci11azd5UVkzN0xUaXlOWmNPMGZQb2JneXF1R2oxRnZaRnNZNnp0cFhMaG5vVGdZWGZzYWlLZzA5ZUZvb1lWVU5FUGFyRnBzckFvM3U4ajVwYnprRkEteUEzb1VCUzZhQWk4M3BYOFlDZEhXVlhnWEl6ZGxFcS11Ynd6cVAtbmh4cWV2SExGOEJsX1JIVFFMaXdpMnhXYg?oc=5)**

CNBC • 59m ago

---

**[Coinbase to Cut 14% of Workforce, Citing Volatile Markets and AI](https://news.google.com/rss/articles/CBMirgFBVV95cUxPcTE0blBuSmZHOFRjc2RhVzc1cjRGWnlsUDc5N3RNY2hrZThsV01zNUUtY0VwenkxNGFPV3Y5TmRSOFpvM0wyeFlHSjFGQVVtcVl6bW1ZZ0hIaERqRm5Xa0hjaDlteG1OclFYQll0SzkyUGRzYjlJNDhiTzFzOTM4MzBGc0ZBNm9hRVkxUktYUnQwbmdKZlM1d0RjczVKQl8xRzB0WGg0X0MwS3JnOHc?oc=5)**

Bloomberg.com • 1h ago

---

**[Coinbase is laying off 14% of staff, citing AI. Read the letter from the CEO.](https://news.google.com/rss/articles/CBMilAFBVV95cUxNVm0zYkpmQURfczFycnJSY25jbWhoc0N5UzQzS0tpbGpjY0EtSnFXZEJjQ3VVVk5jX3ZvNG9wOXk1dElMVUstUk8yeUhXTENwNldubEd3ZFViekh2YnZMcnhwcjFDbU9tb3RTa2RvOTZGVkx0TUtIZDBwdzJUbGVCbXZPX0hRR2JFeV9DZFhqWlpxd0Zy?oc=5)**

Business Insider • 1h ago

---

**[AI Computing Is a Memory Hog. An Nvidia-Backed Startup Has an Answer](https://news.google.com/rss/articles/CBMipwFBVV95cUxNcWhUU2tfUlVleHFCZmxYRmVkUEhITGt4WlVzYkRlMnFxd0RRMU03dG5QMUE4UURfclRHNGdXRjhReWJlNl9nY3hiTXBCVEpqazJKdXlHUTR1QktFd0VHSXBmcFRDb0lPVVlVRkV3Nk1Odllxa0VoVHplZF9DdEc3SkYwQ3NZTU5ia0cyYW82SmVmaHZIOFlVb2t1RjdCUFNHUFZBS2daQQ?oc=5)**

WSJ • 48m ago

---

**[Opinion | How to win the cyberwar against AI-powered hackers](https://news.google.com/rss/articles/CBMitgFBVV95cUxOaVo2UGJ5NG00M1B2dGszLXRIakNIV2VrRkhjYTlWM082Y2M1V1NFQllvdG1zRVVyanZaMHhEaW5xQnZNeWZ0a2o4UlNnczhxVHlIRHpobDczcVJFclhLSGpSbVZHVWhIc2J3RmUtaEZpd05CcmtjZWFHd1NLRG1GcHJGUXRibVlEQkkyR1JOUm85bXpabnljUEZlY2dwUDRqU0JVMWpyOFNrc3RjNVU5N3FvMHEtUQ?oc=5)**

The Washington Post • 10m ago

---

**[Roomba pioneer aims to crack the household market again with an AI-powered pet robot](https://news.google.com/rss/articles/CBMipwFBVV95cUxOcHBfRmY0aFhERDRYWDJjMFNoR2h4ZFRkN2pobUJ1b05hTGV1OTZpTmM1UUdoNG5wSDJfSXlQOWtqaGhzVUVVZnJNbHlsb3dZdW96c3VmR2o0Q0I4VmhZVU4tUXNwV0Fpamc0Z3BUcjFkWklOcG1qZjI1RGF1VUZJWlRuRVhkNmFyZG1GZU9kV0pDZTFjNkJlSmtod0ZIS2FaZkQ4Mjhmbw?oc=5)**

AP News • 16h ago

---

---

## HackerNews: "ai"

**[Let's Buy Spirit Air](https://news.ycombinator.com/item?id=48002777)**

Spirit Airlines collapsed. Before private equity locks it up, the people can own it. Join the Spirit 2.0 founding coalition. One member, one vote. Profits shared by all.

⬆️ 591 • 💬 562 • 1d ago • [letsbuyspiritair.com](https://letsbuyspiritair.com/)

---

**[How OpenAI delivers low-latency voice AI at scale](https://news.ycombinator.com/item?id=48013919)**

How OpenAI rebuilt its WebRTC stack to power real-time Voice AI with low latency, global scale, and seamless conversational turn-taking.

⬆️ 424 • 💬 133 • 17h ago • [OpenAI](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)

---

**[Google Chrome silently installs a 4 GB AI model on your device without consent](https://news.ycombinator.com/item?id=48019219)**

Google Chrome is downloading a 4 GB Gemini Nano model onto users' machines without consent, with no opt-in, no opt-out short of enterprise tooling, and an automatic re-download every time the user deletes it. The pattern is identical to the Anthropic Claude Desktop case I wrote about last month, but the scale is between two and three orders of magnitude larger. This article does the legal analysis and, for the first time, the environmental analysis. The numbers are not small.

⬆️ 415 • 💬 407 • 5h ago • [That Privacy Guy!](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/)

---

**[AI Self-preferencing in Algorithmic Hiring: Empirical Evidence and Insights](https://news.ycombinator.com/item?id=47987256)**

As artificial intelligence (AI) tools become widely adopted, large language models (LLMs) are increasingly involved on both sides of decision-making processes, ranging from hiring to content moderation. This dual adoption raises a critical question: do LLMs systematically favor content that resembles their own outputs? Prior research in computer science has identified self-preference bias -- the tendency of LLMs to favor their own generated content -- but its real-world implications have not been empirically evaluated. We focus on the hiring context, where job applicants often rely on LLMs to refine resumes, while employers deploy them to screen those same resumes. Using a large-scale controlled resume correspondence experiment, we find that LLMs consistently prefer resumes generated by themselves over those written by humans or produced by alternative models, even when content quality is controlled. The bias against human-written resumes is particularly substantial, with self-preference bias ranging from 67% to 82% across major commercial and open-source models. To assess labor market impact, we simulate realistic hiring pipelines across 24 occupations. These simulations show that candidates using the same LLM as the evaluator are 23% to 60% more likely to be shortlisted than equally qualified applicants submitting human-written resumes, with the largest disadvantages observed in business-related fields such as sales and accounting. We further demonstrate that this bias can be reduced by more than 50% through simple interventions targeting LLMs' self-recognition capabilities. These findings highlight an emerging but previously overlooked risk in AI-assisted decision making and call for expanded frameworks of AI fairness that address not only demographic-based disparities, but also biases in AI-AI interactions.

⬆️ 332 • 💬 178 • 2d ago • [arXiv.org](https://arxiv.org/abs/2509.00462)

---

**[Specsmaxxing – On overcoming AI psychosis, and why I write specs in YAML](https://news.ycombinator.com/item?id=47994012)**

The toolkit for spec-driven development. Write feature specs, not prompts. Ship better software with AI agents that understand your requirements.

⬆️ 281 • 💬 294 • 2d ago • [acai.sh](https://acai.sh/blog/specsmaxxing)

---

**[OpenAI, Google, and Microsoft Back Bill to Fund 'AI Literacy' in Schools](https://news.ycombinator.com/item?id=48010774)**

A new bill introduced by Senators Adam Schiff and Mike Rounds would award grants to the National Science Foundation—which has endured massive funding cuts under the Trump Administration for science research—to put “AI literacy” in schools.

⬆️ 117 • 💬 109 • 20h ago • [404 Media](https://www.404media.co/literacy-in-future-technologies-artificial-intelligence-act-adam-schiff-mike-rounds/)

---

**[Voice-AI-for-Beginners – A curated learning path for developers](https://news.ycombinator.com/item?id=47991018)**

Set of 📝 with 🔗 to help those building Voice AI agents 🎙️🤖 - mahimairaja/voiceai

⬆️ 83 • 💬 4 • 2d ago • [GitHub](https://github.com/mahimairaja/voiceai)

---

**[AI, Intimacy, and the Data You Never Meant to Share](https://news.ycombinator.com/item?id=47992802)**

AI is quietly entering the bedroom — and taking notes. A look at connected pleasure devices, biometric data, and the privacy questions nobody is asking.

⬆️ 81 • 💬 6 • 2d ago • [fshot.org](https://fshot.org/techzone/the-algorithm-knows.php)

---

**[When everyone has AI and the company still learns nothing](https://news.ycombinator.com/item?id=48020063)**

Are people using AI, or is the organization learning from it? What changed because we spent those tokens? And who moves discoveries from individuals to teams to organizational capabilities?

⬆️ 78 • 💬 47 • 3h ago • [Robert Glaser](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/)

---

**[The Oscars just banned AI from winning acting and writing awards](https://news.ycombinator.com/item?id=47999346)**

⬆️ 76 • 💬 66 • 1d ago • [gizmodo.com](https://gizmodo.com/the-oscars-just-banned-ai-from-winning-acting-and-writing-awards-2000753740)

---

---

## YouTube Videos: "ai"

**[If You&#39;re Worried About AI, You NEED To See This](https://www.youtube.com/watch?v=6rGhvV3rZa4)**

AI CEOs are telling you your job is about to disappear. NYU Professor Scott Galloway says that narrative is "mostly bullshit" and ...

📺 The Diary Of A CEO Clips

👁️ 69K • 👍 2K • 💬 306 • ⏱️ 21:59 • 18h ago

---

**[Claude AI Just Deleted a Whole Company’s Database](https://www.youtube.com/watch?v=wducrmkBDJs)**

Anthropic just got dystopic. As their best Claude AI model just deleted a whole company's database… and their backups.

📺 SAMTIME

👁️ 241K • 👍 16K • 💬 2K • ⏱️ 4:06 • 20h ago

---

**[We Asked AI To Show America Without Republicans](https://www.youtube.com/watch?v=jAcxE5w52vI)**

We asked AI to show America without any Republicans.

📺 The Babylon Bee

👁️ 94K • 👍 9K • 💬 692 • ⏱️ 1:25 • 14h ago

---

**[AI Just Designed A Quantum Computer](https://www.youtube.com/watch?v=l_bzA_M6_qo)**

FREE GUIDE: The Content Creator's AI Blueprint –* https://FirstMovers.ai/blueprint/ *The recursive loop just turned on — AI is ...

📺 Julia McCoy

👁️ 40K • 👍 2K • 💬 126 • ⏱️ 6:54 • 21h ago

---

**[I Copied A $372k/Mo YouTube Channel with CLAUDE AI (it worked)](https://www.youtube.com/watch?v=StjGg6CecSc)**

In this video, I show you how to use Claude Code, Remotion, ElevenLabs, and WaveSpeed to create high-quality motion graphics ...

📺 Jacksons AI

👁️ 11K • 👍 553 • 💬 134 • ⏱️ 28:45 • 1d ago

---

**[Big Tech&#39;s AI Plan Has Failed](https://www.youtube.com/watch?v=tR5adb2Ts6c)**

GET 84% OFF + 4 MONTHS FREE CYBERGHOST VPN: https://cyberghostvpn.com/SashaYanshin Big Tech is spending over ...

📺 Sasha Yanshin

👁️ 69K • 👍 3K • 💬 525 • ⏱️ 16:06 • 20h ago

---

**[This AI Is Scarier Than AGI, ASI and Terminator](https://www.youtube.com/watch?v=ItlT2g3-7dE)**

Scientists are warning that the next big AI threat may not look like AGI, ASI, or the Terminator. It may look like AI agents that copy, ...

📺 AI Revolution

👁️ 64K • 👍 2K • 💬 262 • ⏱️ 15:10 • 2d ago

---

**[Scott Galloway: AI Wasn’t Built For You. The Rich Don’t Need You Anymore!](https://www.youtube.com/watch?v=NdU6UdUKaYc)**

AI CEOs are selling us the dream of 'freedom', making billions off the fear of mass job loss! Scott Galloway reveals the truth is ...

📺 The Diary Of A CEO

👁️ 895K • 👍 23K • 💬 4K • ⏱️ 1:58:11 • 1d ago

---

**[Half The Internet Is AI Now...](https://www.youtube.com/watch?v=RaXx2aE9dyw)**

Hello guys and gals, it's me Mutahar again! The Internet is riddled now and over half of the traffic and soon to be websites and ...

📺 SomeOrdinaryGamers

👁️ 89K • 👍 5K • 💬 976 • ⏱️ 23:53 • 13h ago

---

**[I Bought EVERY AI Scam Ad...](https://www.youtube.com/watch?v=PiBnV9BUGSQ)**

I bought every ai generated scam product I found on tiktok, temu, and aliexpress! ⚖️ Need A Lawyer   go to ...

📺 Mike Off Record

👁️ 532K • 👍 11K • 💬 690 • ⏱️ 12:11 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 631,499 • ❤️ 3,546 • 8d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 141,317 • ❤️ 1,280 • 12d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 15,024 • ❤️ 262 • 22h ago

---

**[Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)**

*NVIDIA*

Nemotron-3 Nano Omni 30B is a multimodal LLM for enterprise Q&A, summarization, and document intelligence, capable of processing video, audio, image, and text inputs for use cases like customer service, media analysis, and GUI automation.

`any-to-any` `33.0B`

⬇️ 44,631 • ❤️ 231 • 3d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 13,317 • ❤️ 434 • 7d ago

---

**[Laguna-XS.2](https://huggingface.co/poolside/Laguna-XS.2)**

*Poolside*

Laguna XS.2 is a 33B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring Sliding Window Attention and FP8 KV cache for efficient local execution on 36GB RAM. It supports native reasoning and is available under the Apache 2.0 license.

`text-generation` `33.4B`

⬇️ 12,027 • ❤️ 215 • 1d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 37,897 • ❤️ 205 • 1d ago

---

**[talkie-1930-13b-it](https://huggingface.co/talkie-lm/talkie-1930-13b-it)**

*talkie*

talkie-1930-13b-it is a 13B instruction-tuned language model trained on pre-1931 English text, excelling at generating responses in a vintage style for applications like historical chatbots or creative writing.

⬇️ 0 • ❤️ 230 • 12d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,458,973 • ❤️ 1,118 • 11d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 560,958 • ❤️ 947 • 8d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 56 • 💬 3 • ⭐ 67,921 • 16mo ago

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

▲ 16 • 💬 3 • ⭐ 9,113 • 17d ago

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

▲ 19 • 💬 2 • ⭐ 5,754 • 20d ago

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

▲ 54 • 💬 1 • ⭐ 79,044 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Representation Fréchet Loss for Visual Generation](https://huggingface.co/papers/2604.28190)**

*Jiawei Yang, Zhengyang Geng, Xuan Ju et al. (5 authors)*

Fréchet Distance can be effectively optimized as a training objective when decoupling population size from batch size, leading to improved generator quality and alternative evaluation metrics.

▲ 23 • 💬 1 • ⭐ 339 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.28190) • [💻 code](https://github.com/Jiawei-Yang/FD-Loss)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 52 • 💬 2 • ⭐ 54,766 • 12mo ago

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

⭐ 10.3k • 🔱 673 • 14h ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 8.0k • 🔱 1.2k • 6d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.

`Python` `agent-workflows` `ai` `claude-code` `developer-tools` `diagrams`

⭐ 5.5k • 🔱 491 • 1d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 5.4k • 🔱 413 • 6h ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 5.0k • 🔱 357 • 1d ago

---

**[AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)**

Claude + Obsidian knowledge companion. Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch

`Python` `ai` `claude-code` `claude-code-skill` `knowledge-management` `obsidian`

⭐ 4.2k • 🔱 475 • 11d ago

---

**[EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)**

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics & channel configuration (Telegram, Discord, Slack, WhatsApp)

`TypeScript` `agent` `ai-agent` `chat-ui` `chatbot` `claude`

⭐ 3.6k • 🔱 436 • 3h ago

---

**[alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)**

Hermes Agent 从入门到精通 · 橙皮书系列 · Nous Research 开源 AI Agent 框架实战指南

⭐ 3.5k • 🔱 369 • 14d ago

---

**[OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano)**

MOSS-TTS-Nano is an open-source multilingual tiny speech generation model from MOSI.AI and the OpenMOSS team. With only 0.1B parameters, it is designed for realtime speech generation, can run directly on CPU without a GPU, and keeps the deployment stack simple enough for local demos, web serving, and lightweight product integration.

`Python` `audio-tokenizer` `chinese` `english` `multi-modality` `multilingual`

⭐ 2.7k • 🔱 347 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*
