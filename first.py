import re



def verify_text(test_text, list_keys):
    # Регулярное выражение для поиска ключей в фигурных скобках
    pattern = r'\{([a-zA-Z_]+)\}'

    # Найти все ключи в фигурных скобках
    keys_in_text = re.findall(pattern, test_text)

    # Проверить каждый ключ
    for key in keys_in_text:
        if key not in list_keys:
            return f"Ошибка: ключ '{key}' некорректен"

    # Проверка на наличие всех парных фигурных скобок
    stack = []
    for char in test_text:
        if char == '{':
            stack.append(char)
        elif char == '}':
            if not stack:
                return "Ошибка: Некорректная пара фигурных скобок"
            stack.pop()

    if stack:
        return "Ошибка: Некорректная пара фигурных скобок"

    return "Тест пройден"
