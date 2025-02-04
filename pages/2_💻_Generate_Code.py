import streamlit as st

st.set_page_config(
    page_title="Generate Code",
    page_icon="💻",
    layout="wide"
)

import asyncio
import io
import helpers.sidebar
import helpers.util
import services.prompts
import services.llm

helpers.sidebar.show()

st.header("Generate Code")
st.write("Here to assist with existing code, based on your individual needs. Using the Pragmatic Programmer "
         "mindset to create code that is easy to understand and maintain.")

prompt = services.prompts.general_ducky_code_starter_prompt()

# Add sidebar options to review, debug, or modify code.
ducky_action = st.sidebar.selectbox("How do you want Ducky to help with your code?", ["👀 Review", "🪲 Debug",
                                                                                      "✏️ Modify"])

# Add a text area to input code
code = st.text_area("Enter your code here:", height=20)

if ducky_action == "👀 Review":
    # Prompt the user for a code review
    prompt = services.prompts.review_prompt(code)
    review_btn = st.button('Review Code')
    if review_btn:
        messages = asyncio.run(helpers.util.run_prompt(prompt, st.empty()))
        st.write("Here is a code review for your code:")
        st.write(messages[-1]['content'])
elif ducky_action == "🪲 Debug":
    # Prompt the user for a debug
    error = st.text_area("Enter the error message you are seeing:", height=5)
    prompt = services.prompts.debug_prompt(code, error)
    debug_btn = st.button('Debug Code')
    if debug_btn:
        messages = asyncio.run(helpers.util.run_prompt(prompt, st.empty()))
        st.write("Here is a debug for your code:")
        st.write(messages[-1]['content'])
elif ducky_action == "✏️ Modify":
    # Prompt the user for a code modification
    instructions = st.text_area("Enter the instructions for modifying your code:", height=5)
    prompt = services.prompts.modify_code_prompt(code, instructions)
    modify_btn = st.button('Modify Code')
    if modify_btn:
        messages = asyncio.run(helpers.util.run_prompt(prompt, st.empty()))
        st.write("Here is the modified code:")
        st.write(messages[-1]['content'])
