from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os

information = """
Mira Murati (born 1988) is a United States-based, Albanian-born engineer. She is the chief technology officer of OpenAI, the company that develops ChatGPT, an artificial intelligence chatbot.

Early life and education
Murati was born in 1988[1] in Vlorë, Albania, to Albanian parents.[2]

She moved to Victoria, Canada, at the age of 16 in order to attend the Lester B Pearson United World College of the Pacific to complete her high school education.[3][4] She graduated from Thayer School of Engineering at Dartmouth College in 2012 with a Bachelor of Engineering degree in mechanical engineering.[5][6]

Career
Murati started her career as an intern at Goldman Sachs in 2011, and worked at Zodiac Aerospace from 2012 to 2013. She spent three years at Tesla before joining Magic Leap.[7][5] She then joined OpenAI in 2018, later becoming its chief technology officer, where she leads the company's work on ChatGPT, Dall-E, and Codex.[8][7] Her responsibilities include oversight of the company's research, product and safety teams.[9]

She is an advocate for the regulation of AI.[5][10]
"""

if __name__ == "__main__":
    prompt_template = """
        given the infromation {information} about a person from I want you to create:
        1) a short summary 
        2) two interesting facts about them.
    """

    print("Hello Langchain!")
    prompt = PromptTemplate.from_template(prompt_template)
    #prompt.format(information="colorful socks")

    chat = ChatOpenAI(temperature=0, openai_api_key=os.environ["OPENAI_API_KEY"], model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=chat, prompt=prompt)

    print(chain.run(information=information))
