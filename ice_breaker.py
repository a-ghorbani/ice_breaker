from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os
from third_parties.linkedin import scrape_linkedin_profile


def generate_summary_and_facts(linkedin_profile_url: str) -> str:
    """
    Generate a summary and two interesting facts from LinkedIn profile data.
    :param linkedin_profile_url: LinkedIn profile URL as a string
    :return: A string containing the summary and facts
    """
    
    prompt_template = """
        Given the LinkedIn information {information} about a person, I want you to create:
        1) a short summary 
        2) two interesting facts about them.
    """

    prompt = PromptTemplate.from_template(prompt_template)

    chat = ChatOpenAI(
        temperature=0,
        openai_api_key=os.environ.get("OPENAI_API_KEY"),
        model_name="gpt-3.5-turbo",
    )

    chain = LLMChain(llm=chat, prompt=prompt)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)

    return chain.run(information=linkedin_data)


if __name__ == "__main__":
    print("Hello Langchain!")
    summary_and_facts = generate_summary_and_facts(linkedin_profile_url="dummy_url")
    print(summary_and_facts)
