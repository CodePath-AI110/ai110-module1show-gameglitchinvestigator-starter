# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
When I put in 50 it told me to guess lower when I really should have guessed higher. Should be in check guess function.
I noticed that history, attempts, and attempts left were not updating properly. Bug should be in update score.
The new game button didn't work at all. Should have a reset funciton.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess `50` when the secret number is higher | The game should say to guess higher. | The game said to guess lower. | No console error. |
| Enter one or more guesses | History and attempt counts should update after each guess, including attempts left. | History, attempts, and attempts left did not update properly. | No console error. |
| Click the New Game button | The game should reset and start a new round. | Nothing happened; the game did not reset. | No console error. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot in VSCode
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I told it to fix the hint algorithm and that it was giving inverted advice. I verified the result by manually testing it and i asked it to make test cases and those passed.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
I asked it to make the attempts and history match, and at first the bug it gave me was very buggy. It would only accept every other attempt. Also the test cases it gave did really test what i asked it to test. I rewrote the prompt and it gave me the code i have now.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I had the AI make test cases, and when those passed, then i manually went in and checked. Thats when I noticed that the submission button was still buggy and went back to fix that bug.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
When I ran the pytest to check if the history was updating, it said it was valid, but when i ran it on my computer I was actually thrown an import error.
- Did AI help you design or understand any tests? How?
The AI helped me understand where the bug was and how they were linked to each other. When it was editing the code it summarized what was wrong and why the change would fix it. I was able to follow along and learn as it fixed the bug.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
