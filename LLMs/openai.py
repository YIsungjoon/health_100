from langchain_openai import ChatOpenAI

def generate_response(input_text, openai_api_key):
                    llm = ChatOpenAI(
                        temperature=0,
                        model_name="gpt-3.5-turbo-0125",
                        api_key=openai_api_key
                    )
                    return llm.predict(input_text)