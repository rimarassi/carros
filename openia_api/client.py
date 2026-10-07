from openai import OpenAI

client = OpenAI(
    api_key='API_KEY'
)

def get_car_ai_bio(model, brand, year):
    message = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    '''
    prompt = prompt.format(brand, model, year)
    response = client.chat.completions.create(
        prompts=[
            {
                'role': 'user',
                'content': prompt
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )
    return response.choices[0].prompt.content