# ducky-assistant

Ducky is an **AI personal software development assistant**.
Ducky can answer any questions about software development, generate code, help developers learn new topics, and assist with debugging. 

**Things Ducky Can Do**
- Simple chat page for asking any questions about software development.
- "Generate Code" page with custom abilities to Review, Debug, or Modify code snippets.
- Review code ability to provide a code review with sentiment analysis, and respond in a custom format.
- Debug code ability to provide code along with an associated error message, and respond with a fixed version of the code in a custom format.
- Modify code ability to provide code along with instructions for how it should be changed or improved, and respond with a modified version of the code in a custom format.
- "Learning Topics" page for Ducky to explain a software development topic through different choices of an intended audience (5-year-old, high-schooler, adult, etc.) and different choices of output (bullet point notes, article, course syllabus)
- "Auto Code" page where Ducky can solve a daily Leetcode problem using Autogen Agents, providing an output for a full implementation of a code solution along with test cases that verify the solution in newly generated files that are saved. 

Ducky is built in Python and uses the Streamlit framework for a UI, FastAPI tools, OpenAI tools, and AutoGen tools. 

Built for my CS5914 AI Tools for Software Delivery course, taken for my MEng CSA degree at Virginia Tech (Spring 2024)
