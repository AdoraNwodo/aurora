from datetime import datetime
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    chat = ChatOpenAI(model_name="gpt-4", temperature=0.9, max_tokens=1000)
    messages = [
        SystemMessage(content="Hello, I am an Pulumi engineer chatbot."),
        HumanMessage(content="Write a Pulumi program that deploys an EC2 instance."),
    ]

    response=chat(messages)

    return {
        'statusCode': 200,
        'body': response
    }
