# ducky-assistant
Built for my CS5914 AI Tools for Software Delivery course, taken for my Master of Engineering in Computer Science degree at Virginia Tech (Spring 2024)

Ducky is an **AI personal software development assistant**.
Ducky can answer any questions about software development, generate code, help developers learn new topics, and assist with debugging. 

Ducky can also perform some automated tasks - in this case, it takes advantage of **autogen tools and FastAPI** to grab a daily coding problem from LeetCode,
understand the problem, write code that will effectively solve the problem, and provide an output of the problem and a possible solution, along with an
explanation of why it was solved in that particular manner. 

Ducky is built in Python and uses the Streamlit framework for a UI, FastAPI tools, OpenAI tools, and AutoGen tools. 
