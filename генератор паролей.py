import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return "Ошибка: выберите хотя бы один тип символов!"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("=== Генератор паролей ===")
    length = int(input("Длина пароля (по умолчанию 12): ") or 12)
    use_digits = input("Использовать цифры? (y/n): ").lower() != 'n'
    use_symbols = input("Использовать символы? (y/n): ").lower() != 'n'

    password = generate_password(length, use_digits, use_symbols)
    print(f"\nВаш пароль: {password}")
    input("\nНажми Enter, чтобы выйти...")