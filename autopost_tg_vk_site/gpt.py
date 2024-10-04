from openai import OpenAI


def gpt(query, api_gpt, system_prompt, user_prompt):
    """
    Функция для взаимодействия с API GPT.

    Параметры:
    url_query (str): Ссылка на новость.
    api_gpt (str): API ключ.
    system_prompt (str): Промпт для системы.
    user_prompt (str): Промпт для генерации ответа.
    """

    client = OpenAI(
        api_key=api_gpt,
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt.format(query)},
            {"role": "user", "content": user_prompt.format(query)}
        ]
    )

    return chat_completion.choices[0].message.content


