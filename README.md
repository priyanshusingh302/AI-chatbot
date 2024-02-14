# Django AI Chatbot API

This Django API provides an AI chatbot service that uses the Mistral-7B-OpenOrca.Q4_0.gguf language model for natural language processing.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/priyanshusingh302/AI-chatbot-Backend
    ```

2. Navigate to the project directory:

    ```bash
    cd AI-chatbot-Backend
    ```

3. Install dependencies using pipenv:

    ```bash
    pipenv install
    ```

4. Activate the virtual environment:

    ```bash
    pipenv shell
    ```
5. Change working directory:

    ```bash
    cd chatbot
    ```
    
6. Run the Django development server using the following command:

    ```bash
    python manage.py runserver
    ```

## Usage

### Endpoint

- `/chat`

### Request Method

- POST

### Request Payload

The API expects a JSON payload with the following structure:

```json
{
  "prompt": "string",
  "context": "string"
}
```

- `prompt`: The user's question or prompt.
- `context` (optional): Additional context for the prompt.

### Response
The API returns a JSON response with the following structure:\
```json
{
  "response": "string"
}
```
## Implementation Details
The API endpoint /chat is defined in the Django view function chat. It processes incoming POST requests containing user prompts and optional context. The request data is validated using the StringInputSerializer serializer.

### Dependencies
- Django
- Django REST Framework
- langchain

### Configuration
- Set the `local_path` variable to the path of the Mistral-7B-OpenOrca.Q4_0.gguf model.
- Configure the `template` for formatting the response.
- Ensure that the `CallbackManager` and `StreamingStdOutCallbackHandler` are properly configured.

### Logic Overview
- `local_path`: Path to the Mistral-7B-OpenOrca.Q4_0.gguf model.
- `callback_manager`: Manages callback handlers for processing outputs.
- `template`: Template structure for the context, question, and answer.
- `prompt`: PromptTemplate for defining the template and input variables.
- `llm`: GPT4All instance initialized with the local model and callback manager.
- `llm_chain`: LLMChain instance for managing the prompt and model interactions.

### Error Handling
- The API handles invalid requests and responds with appropriate HTTP status codes and error messages.

Note
Adjust configurations and dependencies as per your environment and requirements.
Further customization and enhancements can be made based on specific project needs.
