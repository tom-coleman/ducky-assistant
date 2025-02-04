from typing import Optional
import json

import aitools_autogen.utils as utils
from aitools_autogen.agents import WebPageScraperAgent, LeetCodeDailyProblemAgent
from aitools_autogen.blueprint import Blueprint
from aitools_autogen.config import llm_config_openai as llm_config, config_list_openai as config_list, WORKING_DIR
from autogen import ConversableAgent


class LeetCodeDailyBlueprint(Blueprint):

    def __init__(self, work_dir: Optional[str] = WORKING_DIR, coding_langauge: Optional[str] = "Python"):
        super().__init__([], config_list=config_list, llm_config=llm_config)
        self._work_dir = work_dir or "code"
        self._summary_result: Optional[str] = None
        self._coding_langauge = coding_langauge or "Python"
        self._problem_details: Optional[dict] = None

    @property
    def summary_result(self) -> str | None:
        """The getter for the 'summary_result' attribute."""
        return self._summary_result

    @property
    def work_dir(self) -> str:
        """The getter for the 'work_dir' attribute."""
        return self._work_dir

    @property
    def coding_language(self) -> str:
        """The getter for the 'coding_language' attribute."""
        return self._coding_langauge

    @coding_language.setter
    def coding_language(self, language: str):
        """The setter for the 'coding_language' attribute."""
        self._coding_langauge = language

    @property
    def problem_details(self) -> dict:
        """The getter for the 'problem_details' attribute."""
        return self._problem_details

    async def initiate_work(self, message: str):
        utils.clear_working_dir(self._work_dir)
        agent0 = ConversableAgent("a0",
                                  max_consecutive_auto_reply=0,
                                  llm_config=False,
                                  human_input_mode="NEVER")

        problem_retriever_agent = LeetCodeDailyProblemAgent()

        # problem_retriever_agent retrieves the daily problem
        # coder_agent generates the code to attempt to solve the daily problem
        # proxy_agent runs the code and checks its correctness

        # outputs:
        # - daily problem information (url, title, description, difficulty)
        # - filenames of the code generated to solve and test the daily problem

        problem_solver_agent = ConversableAgent("problem_solver_agent",
                                                max_consecutive_auto_reply=6,
                                                llm_config=llm_config,
                                                human_input_mode="NEVER",
                                                code_execution_config=False,
                                                system_message=f"""
               You are a software engineer tasked with solving LeetCode problems.
               You are writing a class using the {self.coding_language} coding language to solve a single given problem
               or a set of coding problems.

               When given a problem description, you should write a generate code that meets the following requirements:
               - Write a complete implementation of a code solution that meets all the description requirements.
               - Do not suggest incomplete code which requires users to modify.
               - The solution should be contained within a single file, although multiple classes are allowed.
               - You should also generate a test file that tests the solution for completeness.
               - Ensure that multiple edge cases are tested and passed.

               Use multiple classes in separate file names in a directory structure that makes sense.
               You must indicate the script type in the code block.
               Always put `# filename: leetcode/<filename>` as the first line of each code block.

               Feel free to include multiple code blocks in one response. Do not ask users to copy and paste the result.
               """)

        agent0.initiate_chat(problem_retriever_agent, True, message=message)

        leetcode_problem_string = agent0.last_message(problem_retriever_agent)

        # convert the string response back into JSON format
        leetcode_problem = json.loads(leetcode_problem_string["content"])

        problem_description = leetcode_problem["question"]
        self._problem_details = leetcode_problem

        agent0.initiate_chat(problem_solver_agent, True, message=problem_description)

        llm_message = agent0.last_message(problem_solver_agent)["content"]
        utils.save_code_files(llm_message, self.work_dir)

        self._summary_result = utils.summarize_files(self.work_dir)


if __name__ == "__main__":
    import asyncio

    # Create an instance of the LeetCodeDailyBlueprint class
    blueprint = LeetCodeDailyBlueprint()

    # Define the task message
    task_message = "I want to retrieve the daily problem from Leetcode and solve it"

    # Run the blueprint asynchronously
    asyncio.run(blueprint.initiate_work(task_message))

    # Print the summary result
    print(blueprint.summary_result)
