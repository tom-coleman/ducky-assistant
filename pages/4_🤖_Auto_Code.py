import asyncio
import streamlit as st
from asyncio import sleep

import helpers.sidebar
import helpers.util
from aitools_autogen.blueprint_generate_core_client import CoreClientTestBlueprint
from aitools_autogen.blueprint_project8 import LeetCodeDailyBlueprint
from aitools_autogen.config import llm_config_openai as llm_config
from aitools_autogen.utils import clear_working_dir

st.set_page_config(
    page_title="Auto Code",
    page_icon="🤖",
    layout="wide"
)

# Add comments to explain the purpose of the code sections

# Show sidebar
helpers.sidebar.show()

# Add sidebar options to review, debug, or modify code.
blueprint_choice = st.sidebar.selectbox("Which blueprint do you want to use?", ["Leetcode Daily Problem",
                                                                                "Core Client Test"])

if blueprint_choice == "Core Client Test":
    st.session_state.blueprint = CoreClientTestBlueprint()
elif blueprint_choice == "Leetcode Daily Problem":
    st.session_state.blueprint = LeetCodeDailyBlueprint()


async def run_blueprint(ctr, seed: int = 42) -> str:
    await sleep(3)
    llm_config["seed"] = seed
    await st.session_state.blueprint.initiate_work(message=task)
    return st.session_state.blueprint.summary_result

blueprint_ctr, parameter_ctr = st.columns(2, gap="large")
with blueprint_ctr:
    st.markdown("# Run Blueprint")
    if blueprint_choice == "Core Client Test":
        url = st.text_input("Enter a OpenAPI Schema URL to test:",
                            value="https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main/examples/v3.0/uspto.yaml")
    elif blueprint_choice == "Leetcode Daily Problem":
        language_choice = st.selectbox("Coding language to use:", ["Python", "Java", "C++", "JavaScript", "Typescript",
                                                                   "C", "C#", "Dart", "Erlang", "Elixir", "Go", "Kotlin",
                                                                   "PHP", "Racket", "Ruby", "Rust", "Swift", "Scala"])
        st.session_state.blueprint.coding_language = language_choice

    agents = st.button("Start the Agents!", type="primary")

with parameter_ctr:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### Other Options")
    clear = st.button("Clear the autogen cache...&nbsp; ⚠️", type="secondary")
    seed = st.number_input("Enter a seed for the random number generator:", value=42)

dynamic_ctr = st.empty()
results_ctr = st.empty()

if clear:
    with results_ctr:
        st.status("Clearing the agent cache...")
    clear_working_dir("../.cache", "*")

if agents:
    with results_ctr:
        st.status("Running the Blueprint...")

    if blueprint_choice == "Core Client Test":
        task = f"""
                I want to retrieve the Open API specification from
                {url}
                """
    elif blueprint_choice == "Leetcode Daily Problem":
        task = "I want to retrieve the daily problem from Leetcode and solve it"

    text = asyncio.run(run_blueprint(ctr=dynamic_ctr, seed=seed))
    st.balloons()

    with results_ctr:
        if blueprint_choice == "Leetcode Daily Problem":
            problem_details = st.session_state.blueprint.problem_details
            output = f"""\
# LeetCode Daily Problem: {problem_details['questionTitle']}
### Difficulty: {problem_details['difficulty']}
### [View this LeetCode Problem]({problem_details['questionLink']})
{text}
"""
            st.markdown(output, unsafe_allow_html=True)
        else:
            st.markdown(text)
