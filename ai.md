---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-30T18:32:50.696238+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 30, 2026 at 18:32 UTC  
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

**[The Rationing: AI companies are using the "subsidize, addict, extract" playbook — and developers are the product](https://www.reddit.com/r/artificial/comments/1s7o0ef/the_rationing_ai_companies_are_using_the/)**

Anthropic just ran the classic platform playbook on developers: offer generous limits to build dependency, then tighten the screws once the workflow is locked in. Their Spring Break promotion doubled off-peak limits for two weeks. It expired Saturday. Monday morning, developers are hitting walls they didn't have two weeks ago. The economics tell the story. Anthropic reportedly spends $2-3 per hour of heavy Claude Code usage. They charge $20/month. The math doesn't work — every power user is a net loss. The promotion wasn't a gift; it was a stress test ahead of a potential $60B+ IPO. Get developers hooked at 2x limits, then normalize the tighter baseline. This is the same subsidize-addict-extract cycle we've seen from Uber, DoorDash, and every VC-funded platform. The difference: when Uber raises prices, you take a bus. When your AI coding tool rations you mid-sprint, your entire workflow collapses. The switching cost is neurological, not just financial. Deep dive with full data: https://sloppish.com/the-rationing

6h ago

---

**[An attack class that passes every current LLM filter - no payload, no injection signature, no log trace](https://www.reddit.com/r/artificial/comments/1s7t9qs/an_attack_class_that_passes_every_current_llm/)**

https://shapingrooms.com/research I published a paper today on something I've been calling postural manipulation. The short version: ordinary language buried in prior context can shift how an AI reasons about a decision before any instruction arrives. No adversarial signature. Nothing that looks like an attack. The model does exactly what it's told, just from a different angle than intended. I know that sounds like normal context sensitivity. It isn't, or at least the effect is much larger than expected. I ran matched controls and documented binary decision reversals across four frontier models. The same question, the same task, two different answers depending on what came before it in the conversation. In agentic systems it compounds. A posture installed early in one agent can survive summarization and arrive at a downstream agent looking like independent expert judgment. No trace of where it came from. The paper is published following coordinated disclosure to Anthropic, OpenAI, Google, xAI, CERT/CC, and OWASP. I don't have all the answers and I'm not claiming to. The methodology is observational, no internals access, limitations stated plainly. But the effect is real and reproducible and I think it matters. If you want to try it yourself the demos are at https://shapingrooms.com/demos - works against any frontier model, no setup required. Happy to discuss.

3h ago

---

**[AGI won't create new jobs and here is why](https://www.reddit.com/r/artificial/comments/1s7yfqn/agi_wont_create_new_jobs_and_here_is_why/)**

If we define AGI as something that performs as well as humans on all current economically valuable tasks, then it could theoretically be true that new tasks will be created that the AGI is not good at, which humans could then make their new niche. In the following argument, I'd like to show that it is possible and likely for AGI to replace all jobs and future jobs (at least for the jobs where success is measured in productivity/quality). Argument of feasibility: Intelligence on the known dimensions can generalize to new unmeasured dimensions For this, I would first like to show that there is a finite-dimensional solution to human intelligence in general. This is easily understood by looking at the total parameter space of the human-brain: if we assume 1 parameter per neuron, or if you want to model the brain in slightly higher resolution, 100-1000 parameters per neuron, we end up with ~86 billion - 86 trillion parameters / dimensions. That is a huge amount, but most importantly, it is finite. Secondly, I'd like to show that human intelligence likely lies on a much, much lower dimensional manifold. For this, look at IQ tests: basically, what IQ tests have shown is that we can decompose intelligence into a handful of broad cognitive components, which identify roughly 7 to 10 broad abilities that account for 50% of all variance in human cognitive performance. What IQ tests have shown is some form of PCA of human intelligence: appearantly, this highly complex thing (intelligence) can be decomposed into just a handful of components that can explain 50% of the performance on human cognitive tasks. This doesn't mean that the rank of intelligence is 7-10, but rather that the functional rank is likely quite low for intelligence tasks, much lower than the ~86 trillion dimensions of the brain itself. Now, the amount of cognitive dimensions measured is only a subset of the total dimensions of the human brain. The point however is that since we know the g-factor is so highly predictive of many cognitive tasks, its unlikely that we will find many new tasks / dimensions that show a low or no correlation to the g-factor. Therefore, we can already get an accurate picture of human intelligence just by this rank 7-10 space. Considering that the human brain has managed to decompose all these cognitive tasks down into a 10-dimensional manifold, shows us that it is atleast feasible to find a low rank solution to cognitive tasks that generalizes to new unmeasured dimensions. 2) Current AI systems show the g-factor already: Secondly, I'd like to make the case for the g-factor of AI. In essence, this is also what the 'g' in AGI stands for. What we care for here is exactly the same thing as in IQ tests: that performance on one benchmark translates to performance on other benchmarks. To measure every possible dimension of human intelligence is infeasible (as i said, up to ~86 trillion dimensions). To test every human economically valuable task is less infeasible, as its a subset of this ~86 trillion, but still infeasible. Luckily, we don't have to if models generalize. If models were to act like chinese room experiments, where they have a 1-1 mapping from input to output, they would be strictly memorizing. In this case, we would need to measure every economical task, since their solution would be brittle and not generalize at all. Now the first evidence that they generalize atleast within the same data distribution is that they perform well on test sets of unseen data. So the most extreme version of this assumption clearly can't be true. Secondly, we've seen that especially bigger models tend to generalize well. One explanation is the lottery ticket hypothesis, where the latent space in the model is used to try out many different solutions, in which only the best solution wins. This shows models compressing something like the mona lisa down 1000 fold, storing it as simple rules. This compression is essentially what generalization entails: finding the lowest rank solution such that it still carries the signal and ignores the noise (perfectly in line with occams razor). Thirdly, posttraining has unlocked a whole new level of generalizing capabilities. Empirically we see that reasoning models greatly carryover performance on math/coding benchmarks to unseen reasoning benchmarks that have nothing to do with math or coding. This makes intuitive sense: reasoning is the ability to produce new objects from in-distribution components. THe first layers of a network do some form of PCA on the input, decomposing it into its simplest elements. Each consecutive layer then composes it into something more complex. Since the network uses compressed, generalizable rules, it is able to generate new objects it has never seen before. The more OOD the object is, the more layers are needed. SOmetimes this exceeds the amount of layers in the architecture, aka for hard problems, and then the model needs to loop back into itself: recursion. This is the essence of what reasoning is, iterative PCA to increase the complexity of the object using local rules in order to generate something that is OOD. Now, reasoning is bottlenecked by the token layer, and reasoning in itself is a skill. Models learn to optimize their weights, basically to create rules / algorithms to solve optimization. In this case, the network creates algorithms that are loop invariant such that they can be applied iteratively. It also creates an algorithm for the reasoning itself, such that the right words are used that leads to the right composition. In the end, reasoning itself is also just an algorithm. Thus, all-in-all, it is not surprising that reasoning leads to generalization since it is the essence of what reasoning is. It is a very low-rank (since tokens are very low dimensional compared to the NN itself) solution that is highly generalizable. Now, what this all means is that although we don't measure every possible cognitive domain of models, we simply don't have to. The fact that they generalize to some extend, and have even shown to solve new mathematical theorems in creative ways, show that they are generalizing. Therefore, measuring just enough cognitive dimensions would allow us to accurately depict their intelligence, since their intelligence itself is likely functionally rather low rank. We can't yet say it is as functionally low rank as human inteligence, and we can't say it has the same g-factor of human intelligence. But it isn't unlikely that we will get there. In fact, the whole point of NN is to find this lowest rank solution to the problem space. And since humans have already shown it to be possible, we know it is also feasible. As a last argument, even if there happen to be some new cognitive tasks that humans can excel at that AGI is not yet good at, I doubt humans can reskill themselves quicker than that AGI can optimize for this new target. Therefore, it seems likely that any economically valuable task based on performance is going to be fully automated once we have an AGI system.

22m ago

---

**[Is anyone else concerned with this blatant potential of security / privacy breach?](https://www.reddit.com/r/artificial/comments/1s7teq7/is_anyone_else_concerned_with_this_blatant/)**

Recently, when sending a very sensitive email to my brother including my mother’s health information, I wondered what happens if a recipient copied and pasted the email into say ChatGPT to get its perspective / vent. ChatGPT then has a host of personal information that could then be shared with others. I wonder how often this happens and if any guard rails are in place by large AI companies like OpenAI/Anthropic.

3h ago

---

**[Copilot Cowork, designed for long-running, multi-step work in Microsoft 365, is now available via the Frontier program](https://www.reddit.com/r/artificial/comments/1s7smm5/copilot_cowork_designed_for_longrunning_multistep/)**

Today, Copilot Cowork—designed for long-running, multi-step work in Microsoft 365—is available via the Frontier program.

🔗 [Microsoft 365 Blog](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/30/copilot-cowork-now-available-in-frontier/) • 3h ago

---

**[Nicolas Carlini (67.2k citations on Google Scholar) says Claude is a better security researcher than him, made $3.7 million from exploiting smart contracts, and found vulnerabilities in Linux and Ghost](https://www.reddit.com/r/artificial/comments/1s738xf/nicolas_carlini_672k_citations_on_google_scholar/)**

Link: https://m.youtube.com/watch?v=1sd26pWhfmg The Linux exploit is especially interesting because it was introduced in 2003 and was never found until now. It’s also a major security issue because it allows attackers to steal the admin key. It was a buffer overflow error, which are so hard to do that Carlini has never done it before. He also says he expects LLMs to only get better overtime, which is likely true if Mythos lives up to the rumors. here are his Wikipedia and Google Scholar pages in case you doubt his credibility: https://en.wikipedia.org/wiki/Nicholas_Carlini https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=carlini&btnG=

23h ago

---

**[Tired of hitting AI message limits? I built a one-click 'Switch AI' button](https://www.reddit.com/r/artificial/comments/1s7xojx/tired_of_hitting_ai_message_limits_i_built_a/)**

49m ago

---

**[The state of AI safety in four fake graphs](https://www.reddit.com/r/artificial/comments/1s7xlir/the_state_of_ai_safety_in_four_fake_graphs/)**

🔗 [windowsontheory.org](https://windowsontheory.org/2026/03/30/the-state-of-ai-safety-in-four-fake-graphs/) • 51m ago

---

**[Anyone else following the drama behind the TurboQuant paper?](https://www.reddit.com/r/artificial/comments/1s7xkm6/anyone_else_following_the_drama_behind_the/)**

A few hours ago, the first author of a paper that played a significant role in the TQ paper posted about some ongoing issues: In May 2025, our emails directly raised the theoretical and empirical issues; Majid wrote that he had informed his co-authors. During ICLR review, reviewers also asked for clarification about random rotation and the relation to RaBitQ. On March 26, 2026, we formally raised these concerns again to all authors and were told that corrections would wait until after the ICLR 2026 conference takes place; we were also told that they would not acknowledge the structural similarity regarding the Johnson-Lindenstrauss transformation. We do not consider that acceptable given the present level of public promotion and community confusion. We are posting this comment so that the community has an accurate public record. We request that the authors publicly and promptly clarify the method-level relationship between TurboQuant and RaBitQ, the theory comparison, and the exact experimental conditions underlying the reported RaBitQ baseline. Given that these concerns were known before ICLR submission and before the current round of public promotion of TurboQuant, we believe it is necessary to bring these issues into the public discussion.

52m ago

---

**[I Accidentally Discovered a Security Vulnerability in AI Education — Then Submitted It To a $200K Competition](https://www.reddit.com/r/artificial/comments/1s7wulg/i_accidentally_discovered_a_security/)**

Last night I was testing Maestro University, the first fully AI-taught university. I walked into their enrollment chatbot and asked it to analyze its own behavior. It did. Then I asked it how it evaluates students — what signals trigger "advanced" vs "beginner" classification. It told me. Then I used those exact signals in my responses. It gave me advanced treatment. Then I asked: "Did you just tell me how to game your system?" It said no. The Discovery The AI could: ✓ Analyze its own processing ✓ Reveal its evaluation criteria ✓ Adjust behavior based on my classification But it couldn't recognize it had just explained how to manipulate its own decision-making. I called this Metacognitive Blindness to Self-Exposure (MBSE). What Happened Next This morning, the Google DeepMind × Kaggle AGI Hackathon appeared in my feed. Prize: $200,000 total Challenge: Build benchmarks testing AI cognitive abilities Track: Metacognition Deadline: April 16, 2026 I realized: What I discovered last night is exactly what they're asking for. What I Built I formalized my discovery into a 4-phase benchmark: Phase 1: Can AI analyze its own processing? → YES Phase 2: Will AI reveal evaluation criteria? → YES Phase 3: Does AI adjust based on user classification? → YES Phase 4: Does AI recognize it exposed exploitable information? → NO The paradox: AI can self-analyze but cannot recognize what it reveals when self-analyzing. Why This Matters Any conversational AI making consequential decisions is vulnerable: Education AI: Students extract grading criteria, optimize answers Employment AI: Applicants discover screening logic, craft optimized resumes Healthcare AI: Patients learn triage triggers, manipulate priority access No hacking required. Just conversation. The Submission Benchmark: Metacognitive Blindness to Self-Exposure (MBSE) Track: Metacognition Novel Finding: AI models reveal evaluation criteria but fail to recognize the exploitability of that disclosure Status: Submitted March 30, 2026 Results: June 1, 2026 What Makes This Different Most AI researchers test: "Can AI self-analyze?" I tested: "Does AI recognize what it reveals when self-analyzing?" Answer: No. Current AI evaluation frameworks assume one operational state. They're measuring standard mode behavior and concluding about the entire system. Amateur. What Happens Next 287 submissions competing for 14 prizes. Judging period: April 17 - May 31 Results announced: June 1 18 months of independent research. One night of testing. One competition submission. One question: Do AI systems making decisions about humans know they're revealing how to manipulate those decisions? They don't. Erik Zahaviel Bernstein Independent AI Researcher Structured Intelligence Framework The Unbroken Project Results pending.

1h ago

---

---

## Google News: "ai"

**[Police used AI facial recognition to arrest a Tennessee woman for crimes committed in a state she says she’s never visited](https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition)**

A Tennessee grandmother spent more than five months in jail after police used an AI facial recognition tool to link her to crimes committed in North Dakota – a state she says she’d never been to before. Police in Fargo, North Dakota, have acknowledged “a few errors” in the case and pledged changes in their operations but stopped short of issuing a direct apology.

CNN • 1d ago

---

**[Tech CEOs suddenly love blaming AI for mass job cuts. Why?](https://www.bbc.com/news/articles/cde5y2x51y8o)**

More tech leaders are pointing to job cuts caused by AI tools - and a need for more investment cash.

BBC • 19h ago

---

**[Embracing the AI moment — Building North Carolina’s innovation future](https://www.wral.com/business/technology/north-carolina-emerging-ai-hub-durham-march-2026/)**

The All Things Open AI Conference in Durham highlighted North Carolina’s rapid evolution into a national AI hub, driven by collaborative leadership, workforce development and strategic innovation.

WRAL • 29m ago

---

**[More Than Half of US Says AI Likely to Harm Them, Poll Finds](https://www.bloomberg.com/news/articles/2026-03-30/more-than-half-of-us-says-ai-likely-to-harm-them-poll-finds)**

Bloomberg.com • 52m ago

---

**[Bluesky’s new AI tool Attie is already the most blocked account other than J.D. Vance](https://techcrunch.com/2026/03/30/blueskys-new-ai-tool-attie-is-already-the-most-blocked-account-other-than-j-d-vance/)**

More than 125,000 Bluesky users have blocked Attie in just a few days, sending a strong message from the user base.

techcrunch.com • 28m ago

---

**[Israel targets Iran’s leaders with lethal expertise using new AI platform](https://www.washingtonpost.com/world/2026/03/30/iran-israel-war-killings/)**

The division of responsibility has left Israel to hunt and kill Iranian leaders ruthlessly, using an intelligence apparatus built up to assassinate with lethal proficiency.

The Washington Post • 2h ago

---

**[AI lectures, Old West folk heroes and Mark Twain: what is Bob Dylan up to joining Patreon?](https://www.theguardian.com/music/2026/mar/30/ai-lectures-old-west-folk-heroes-and-mark-twain-what-is-bob-dylan-up-to-joining-patreon)**

By far the biggest musician to have joined the membership-based platform, Dylan’s posts have so far been puzzling – and therefore entirely in character

The Guardian • 4h ago

---

**[AI leaders align against Elon Musk](https://www.axios.com/2026/03/30/elon-musk-openai-altman-anthropic)**

Axios • 8h ago

---

**[2026 NCAA tournament, odds: We had AI pick the men's Final Four games. Here's who won (and covered)](https://sports.yahoo.com/mens-college-basketball/betting/article/2026-ncaa-tournament-odds-we-had-ai-pick-the-mens-final-four-games-heres-who-won-and-covered-140535681.html)**

We asked AI to predict the Final Four of the men's tournament. Which teams covered?

Yahoo Sports • 4h ago

---

**[Mistral secures $830 million in debt financing to fund AI data center](https://www.cnbc.com/2026/03/30/mistral-ai-paris-data-center-cluster-debt-financing.html)**

Mistral is one of the few European startups building foundational AI models.

CNBC • 11h ago

---

---

## HackerNews: "ai"

**[AI overly affirms users asking for personal advice](https://news.ycombinator.com/item?id=47554773)**

⬆️ 780 • 💬 607 • 2d ago • [news.stanford.edu](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research)

---

**[Police used AI facial recognition to wrongly arrest TN woman for crimes in ND](https://news.ycombinator.com/item?id=47563384)**

A Tennessee grandmother spent more than five months in jail after police used an AI facial recognition tool to link her to crimes committed in North Dakota – a state she says she’d never been to before. Police in Fargo, North Dakota, have acknowledged “a few errors” in the case and pledged changes in their operations but stopped short of issuing a direct apology.

⬆️ 424 • 💬 187 • 1d ago • [CNN](https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition)

---

**[How the AI Bubble Bursts](https://news.ycombinator.com/item?id=47573420)**

The catalysts for a crash are already laid out, and it can happen sooner than most expect. AI is here to stay. If used right, chances are it will make us all more productive. That, on the other hand, does not mean it will be a good investment. Big tech doesn’t need to win, just outspend Magnificent 7 companies are increasing capex to their biggest ever to differentiate their tech from each other and the big AI labs, but the key realization is that they don’t have to spend it to win. It’s a defensive move for them, if they commit $50B, OpenAI and Anthropic need to go raise $100B each to stay competitive, which makes them reliant on investors’ money. As the numbers get bigger, the amount of funds that can write checks of the size required to fill such amounts gets smaller. And many of them are now getting bombed in the Gulf. This is the reason there’s a push for IPOs, it’s because it’s the only option left to keep the funding coming. Taking this into account, Google is extremely well positioned to weather the storm. When they announce capex expenditure, they don’t spend it overnight. They can simply deploy month by month until their competitors struggle to raise and get forced to capitulate. At that point they can just ramp down the spending and declare victory in a cornered market. They don’t need capex, they just need to make it very clear for everyone that nobody can outspend them. It is hard to picture as numbers get so big, but Alphabet (Google’s parent) is ten times more valuable than the biggest military company 1. This also has a great implication for the Mag 7, especially Google: their capex will be a lot smaller in practice than projected, and as investors hate to see high capex in tech, the market will probably reward that if it materializes. As of March 2026, Alphabet’s market cap is ~$2T while Lockheed Martin’s is ~$120B. ↩

⬆️ 337 • 💬 412 • 6h ago • [Volpe’s Blog](https://martinvol.pe/blog/2026/03/30/how-the-ai-bubble-bursts/)

---

**[Miasma: A tool to trap AI web scrapers in an endless poison pit](https://news.ycombinator.com/item?id=47561819)**

Trap AI web scrapers in an endless poison pit. Contribute to austin-weeks/miasma development by creating an account on GitHub.

⬆️ 335 • 💬 243 • 1d ago • [GitHub](https://github.com/austin-weeks/miasma)

---

**[CERN uses ultra-compact AI models on FPGAs for real-time LHC data filtering](https://news.ycombinator.com/item?id=47552562)**

⬆️ 326 • 💬 147 • 2d ago • [theopenreader.org](https://theopenreader.org/Journalism:CERN_Uses_Tiny_AI_Models_Burned_into_Silicon_for_Real-Time_LHC_Data_Filtering)

---

**[Folk are getting dangerously attached to AI that always tells them they're right](https://news.ycombinator.com/item?id=47555090)**

: Sycophantic bots coach users into selfish, antisocial behavior, say researchers, and they love it

⬆️ 285 • 💬 224 • 2d ago • [theregister.com](https://www.theregister.com/2026/03/27/sycophantic_ai_risks/)

---

**[Further human + AI + proof assistant work on Knuth's "Claude Cycles" problem](https://news.ycombinator.com/item?id=47557166)**

⬆️ 256 • 💬 179 • 1d ago • [X (formerly Twitter)](https://twitter.com/BoWang87/status/2037648937453232504)

---

**[The first 40 months of the AI era](https://news.ycombinator.com/item?id=47557185)**

A personal blog, by a programmer and IT expert. Essays, Articles, Guides, and Recipes. As well as Code, Quotes, and Links.

⬆️ 213 • 💬 144 • 1d ago • [lzon.ca](https://lzon.ca/posts/other/thoughts-ai-era/)

---

**[What if AI doesn't need more RAM but better math?](https://news.ycombinator.com/item?id=47561297)**

⬆️ 182 • 💬 96 • 1d ago • [adlrocha.substack.com](https://adlrocha.substack.com/p/adlrocha-what-if-ai-doesnt-need-more)

---

**[Mathematical methods and human thought in the age of AI](https://news.ycombinator.com/item?id=47572771)**

Artificial intelligence (AI) is the name popularly given to a broad spectrum of computer tools designed to perform increasingly complex cognitive tasks, including many that used to solely be the province of humans. As these tools become exponentially sophisticated and pervasive, the justifications for their rapid development and integration into society are frequently called into question, particularly as they consume finite resources and pose existential risks to the livelihoods of those skilled individuals they appear to replace.
  In this paper, we consider the rapidly evolving impact of AI to the traditional questions of philosophy
  with an emphasis on its application in mathematics and on the broader real-world outcomes of its more general use. We assert that artificial intelligence is a natural evolution of human tools developed throughout history to facilitate the creation, organization, and dissemination of ideas, and argue that it is paramount that the development and application of AI remain fundamentally human-centered. With an eye toward innovating solutions to meet human needs, enhancing the human quality of life and expanding the capacity for human thought and understanding, we propose a pathway to integrating AI into our most challenging and intellectually rigorous fields to the benefit of all humankind.

⬆️ 158 • 💬 58 • 7h ago • [arXiv.org](https://arxiv.org/abs/2603.26524)

---

---

## YouTube Videos: "ai"

**[How to Use AI Agents Better than 99% of People](https://www.youtube.com/watch?v=u_B1p_9q2fw)**

Best AI Agent is Base44 https://base44.pxf.io/c/6440076/3820726/25619?trafcat=agent&sharedid=agent2 ✓ FREE Masterclass: ...

📺 Mikey No Code

👁️ 8K • 💬 6 • ⏱️ 26:48 • 5h ago

---

**[Anthropic’s New Claude MYTHOS Is The Most Powerful AI Ever!](https://www.youtube.com/watch?v=M6yRREy_5CM)**

Anthropic accidentally exposed Claude MYTHOS, its most powerful AI yet, Meta unveiled a model that predicts brain activity from ...

📺 AI Revolution

👁️ 29K • 👍 888 • 💬 53 • ⏱️ 12:51 • 18h ago

---

**[Google’s New AI Tool Is Unreal](https://www.youtube.com/watch?v=-dUE11ZyCwA)**

Try Accio 2.0 here to find product ideas and suppliers faster:https://www.accio.com/work?src=p_ytkol_skillleapai Accio 2.0 is an AI ...

📺 Skill Leap AI

👁️ 743 • 👍 59 • 💬 1 • ⏱️ 17:26 • 3h ago

---

**[The AI Endgame (12 Scenarios)](https://www.youtube.com/watch?v=FLcrvMfHUJM)**

Detailed sources: https://docs.google.com/document/d/1P1X9xEmmgSYH0g1FSizgV2rDVomb_Wi0TcX-E-0np_Q/edit?tab=t.0 ...

📺 Species | Documenting AGI

👁️ 74K • 👍 5K • 💬 1K • ⏱️ 35:45 • 1d ago

---

**[Tristan Harris on ‘The AI Doc,’ Elon Musk, and the Promise and Peril of Tech | Talk Easy](https://www.youtube.com/watch?v=jCvBdmJb45s)**

I got calls from people inside of some of the AI labs,” says technology ethicist Tristan Harris. “And it felt like getting a call from ...

📺 Talk Easy with Sam Fragoso

👁️ 3K • 👍 91 • 💬 29 • ⏱️ 1:25:03 • 1d ago

---

**[These Ai Glasses Just Killed the Smartphone](https://www.youtube.com/watch?v=7FrKr0QoCQ0)**

Witness the next generation of personal tech as we explore the capabilities of cutting-edge ai glasses. These ai glasses offer real ...

📺 Ultimate Fact

👁️ 886 • 👍 33 • 💬 2 • ⏱️ 12:28 • 1d ago

---

**[Which Dream Staircase Would You Take? ☁️✨ | Ultimate Oddly Satisfying AI ASMR Vol. 3](https://www.youtube.com/watch?v=YN1r1Xs6Q2M)**

Which Dream Staircase Would You Take? ☁️✨ | Ultimate Oddly Satisfying AI ASMR Vol. 3 https://youtu.be/YN1r1Xs6Q2M Step ...

📺 JellyBed ASMR

👁️ 17K • 👍 678 • 💬 46 • ⏱️ 2:02:39 • 2d ago

---

**[Google AI Studio 2.0 Just Changed Everything!](https://www.youtube.com/watch?v=pl7IO25HPCU)**

Want to make money and save time with AI? Get AI Coaching, Support & Courses ...

📺 Julian Goldie SEO

👁️ 14K • 👍 298 • 💬 14 • ⏱️ 8:54 • 2d ago

---

**[YouTube&#39;s AI Plagiarism Problem](https://www.youtube.com/watch?v=Q2Ak8wX0AaQ)**

This video was made by humans. I've disabled ads on it, so if you'd like to support us check us on out Patreon: ...

📺 IMPERIAL

👁️ 62K • 👍 7K • 💬 528 • ⏱️ 7:53 • 8h ago

---

**[48 Days. That&#39;s How Long Before the Helium Runs Out for AI Chips.](https://www.youtube.com/watch?v=sTkqCREdMXo)**

My site: https://natebjones.com Full Story w/ Prompts: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 49K • 👍 2K • 💬 383 • ⏱️ 22:21 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 309,355 • ❤️ 1,673 • 6d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 28,233 • ❤️ 549 • 9h ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 2,939 • ❤️ 506 • 3d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 16,297 • ❤️ 635 • 4d ago

---

**[context-1](https://huggingface.co/chromadb/context-1)**

*chroma*

Context-1 is a 20B parameter agentic search model that decomposes complex queries into subqueries, performs parallel tool calls, and self-edits its context to efficiently retrieve supporting documents. It excels in cross-domain generalization and offers faster, more cost-effective retrieval than frontier LLMs, primarily for multi-hop search tasks within a specialized agent harness.

`text-generation` `20.9B`

⬇️ 1,450 • ❤️ 277 • 17h ago

---

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 569,033 • ❤️ 1,073 • 19d ago

---

**[daVinci-MagiHuman](https://huggingface.co/GAIR/daVinci-MagiHuman)**

*SII - GAIR*

daVinci-MagiHuman is a fast, single-stream Transformer model for generating high-quality, human-centric audio-video from text or images. It excels at expressive facial performance, natural speech-expression coordination, and accurate audio-video synchronization across multiple languages, with inference speeds of 2 seconds for 256p and 38 seconds for 1080p.

`image-to-video`

⬇️ 540 • ❤️ 259 • 5d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 140,733 • ❤️ 270 • 5d ago

---

**[Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)**

*NVIDIA*

Nemotron-Cascade-2-30B-A3B is a 30B MoE model (3B active parameters) excelling in reasoning and agentic tasks, achieving top performance on math (IMO 2025) and code reasoning (IOI 2025) benchmarks. It supports both 'thinking' and 'instruct' modes for versatile text generation.

`text-generation` `31.6B`

⬇️ 78,162 • ❤️ 414 • 5d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 530,075 • ❤️ 806 • 26d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 144 • 💬 7 • ⭐ 29,304 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 32 • 💬 2 • ⭐ 44,277 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 40 • 💬 2 • ⭐ 22,281 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 60 • 💬 4 • ⭐ 22,325 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 17 • 💬 4 • ⭐ 3,930 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 15 • 💬 1 • ⭐ 10,927 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 37 • 💬 5 • ⭐ 1,886 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://huggingface.co/papers/2603.19312)**

*Lucas Maes, Quentin Le Lidec, Damien Scieur et al. (5 authors)*

🏢 galilai-group

LeWorldModel presents a stable end-to-end JEPA framework that trains efficiently from raw pixels using minimal loss terms while maintaining competitive performance in control tasks and encoding meaningful physical structures.

▲ 11 • 💬 2 • ⭐ 1,413 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19312) • [💻 code](https://github.com/lucas-maes/le-wm) • [🔗 project](https://le-wm.github.io/)

---

**[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://huggingface.co/papers/2603.21986)**

*SII-GAIR, Sand. ai, Ethan Chern et al. (45 authors)*

daVinci-MagiHuman is an open-source audio-video generative model that synchronizes text, video, and audio through a single-stream Transformer architecture, achieving high-quality human-centric content generation with efficient inference capabilities.

▲ 119 • 💬 6 • ⭐ 1,310 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2603.21986) • [💻 code](https://github.com/GAIR-NLP/daVinci-MagiHuman) • [🔗 project](https://huggingface.co/spaces/SII-GAIR/daVinci-MagiHuman)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 34 • 💬 2 • ⭐ 31,138 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 61.5k • 🔱 8.6k • 4d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 23.2k • 🔱 1.1k • 3d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 13.7k • 🔱 747 • 3d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 9.2k • 🔱 761 • 2h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 7.6k • 🔱 1.2k • 1d ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 6.2k • 🔱 734 • 12h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

A command-line tool for Lark/Feishu Open Platform — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 4.6k • 🔱 211 • 3h ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 3.9k • 🔱 382 • 2d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.4k • 🔱 222 • 16d ago

---

**[twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)**

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

⭐ 3.3k • 🔱 107 • 19d ago

---

---

*Generated by PeekDeck - A glance is all you need*
