# views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StringInputSerializer
from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

local_path = 'D:\Programing\LLM\mistral-7b-openorca.Q4_0.gguf' 
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
template = """Question: {question}
            Answer: Let's think step by step.
            """
prompt = PromptTemplate(template=template, input_variables=["question"])
llm = GPT4All(model=local_path, callback_manager=callback_manager, verbose=True)
llm_chain = LLMChain(prompt=prompt, llm=llm)

@api_view(['POST'])
def remove_spaces(request):
    if request.method == 'POST':
        serializer = StringInputSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.validated_data['promt']

            processed_string = llm_chain.run(question)
            return Response({'response': processed_string}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
