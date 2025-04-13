import math
import secrets
import string


def calculate_entropy(password, all_chars):
    """
    Расчёт энтропии пароля по формуле length * log2(N)
    """
    L = len(password)
    N = len(all_chars)  # Уникальные символы в пуле

    entropy = L * math.log2(N)

    return entropy

def password_generator(length=32):
    if length < 32:
        raise ValueError("Длина пароля должна быть не менее 32 символов для обеспечения безопасности.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Общий набор
    all_chars = lowercase + uppercase + digits + special_chars

    # Генерация самого пароля с помощью secrets
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special_chars)
    ]

    remaining_length = length -4
    if remaining_length > 0:
        password += [secrets.choice(all_chars) for _ in range(remaining_length)]

    secrets.SystemRandom().shuffle(password) # перемешиваем для большей сложности
    password_to_str = ''.join(password)

    entropy = calculate_entropy(password_to_str, all_chars)

    return password_to_str, entropy

# Вывод программы
print("Генератор паролей высокой энтропии(меры сложности пароля)")
try:
    length_input = input("Введите желаемую строку пароля >= 32: ")
    length_by_user = int(length_input)

    password, entropy = password_generator(length_by_user)
    print(password)
    print(f"\nЭнтропия - {entropy:.2f} бит")
except ValueError as e:
    print(e)
