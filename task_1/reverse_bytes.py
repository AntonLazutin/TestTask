def get_reversed_bytes(integer):
    return integer.to_bytes(2, 'little')


if __name__ == "__main__":
    print(get_reversed_bytes(int(input("Введите целое число: "))))
