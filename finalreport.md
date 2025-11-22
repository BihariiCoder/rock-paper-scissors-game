ASHISH RANJAN<br>
25BHI10057<br>
DATE OF SUBMISSION- 25 NOV 2025<br>
FACULTY- SASMITA PADHY <br>
PROJECT FINAL SUBMISSION REPORT<br>
ROCK PAPER SCISSORS GAME<br>
Introduction  <br>
- Brief overview of the project purpose: creating a simple, interactive rock-paper-scissors game to practice Python programming basics and game logic.<br>

Problem Statement  <br>
- Develop a command-line game that lets a user play rock-paper-scissors against the computer, teaching core programming concepts like conditionals, input/output, and randomness.<br>

Functional Requirements  <br>
- Accept valid user inputs (rock, paper, scissors)  
- Generate a random computer choice  
- Compare inputs and declare win, lose, or tie outcome  
- Display choices and game result to the user  

Non-functional Requirements  <br>
- Run on standard Python 3 interpreter without additional dependencies  
- Provide a user-friendly command-line interface  
- Handle inputs case-insensitively  

System Architecture  <br>
- Simple script-based architecture involving user input, game logic, and output display components  

Design Diagrams  <br>
- Use Case Diagram: user input, game processing, display result  
- Workflow Diagram: start -> input -> computer choice -> compare -> output -> end  
- Sequence Diagram: user input -> game logic -> output result  
- Class/Component Diagram: (optional) main script with functions for input, logic, output  
- ER Diagram: not applicable (no database used)  

Design Decisions & Rationale  <br>
- Chose console interface for simplicity and educational clarity  
- Used random.choice for computer moves for easy randomness  
- Straightforward if-elif logic for determining game outcome  

Implementation Details  <br>
- Python script using random module  
- User input collected via input() function and converted to lowercase  
- Decision logic implemented with if-elif-else statements  

Screenshots / Results  <br>
- Include sample screenshots showing game prompt, computer choice, and result messages  

Testing Approach  <br>
- Tested with all valid inputs (rock, paper, scissors)  
- Verified win, lose, tie logic correctness  
- Tested input case insensitivity  

Challenges Faced  <br>
- Ensuring user input is case-insensitive  
- Preventing invalid inputs (optional for later improvement)  

Learnings & Key Takeaways  <br>
- Understanding use of modules like random  
- Practiced control flow with conditionals  
- Improved basic user interaction design in Python  

Future Enhancements  <br>
- Add input validation and error handling  
- Implement score tracking across multiple rounds  
- Create a GUI version using Tkinter or Pygame  
- Allow multiplayer mode  

References  <br>
- Python official documentation  
- Tutorials on rock-paper-scissors game implementation in Python  


