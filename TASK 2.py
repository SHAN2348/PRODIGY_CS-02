def encrypt_image(image_path, key):
    """
    Encrypts an image by swapping pixel values and applying XOR operation.

    Args:
        image_path (str): Path to the image file.
        key (int): XOR key.

    Returns:
        str: Path to the encrypted image.
    """
    image = Image.open(image_path)
    pixels = image.load()

    # Swap pixel values of each row
    for y in range(image.height):
        for x in range(image.width // 2):
            left_pixel = pixels[x, y]
            right_pixel = pixels[image.width - x - 1, y]
            pixels[x, y] = right_pixel
            pixels[image.width - x - 1, y] = left_pixel

    # Apply XOR operation to each pixel
    for x in range(image.width):
        for y in range(image.height):
            pixel = pixels[x, y]
            pixels[x, y] = tuple(val ^ key for val in pixel)

    encrypted_image_path = "encrypted_" + image_path
    image.save(encrypted_image_path)
    return encrypted_image_path

def decrypt_image(image_path, key):
    """
    Decrypts an image by applying XOR operation and swapping pixel values.

    Args:
        image_path (str): Path to the encrypted image file.
        key (int): XOR key.

    Returns:
        str: Path to the decrypted image.
    """
    image = Image.open(image_path)
    pixels = image.load()

    # Apply XOR operation to each pixel
    for x in range(image.width):
        for y in range(image.height):
            pixel = pixels[x, y]
            pixels[x, y] = tuple(val ^ key for val in pixel)

    # Swap pixel values of each row
    for y in range(image.height):
        for x in range(image.width // 2):
            left_pixel = pixels[x, y]
            right_pixel = pixels[image.width - x - 1, y]
            pixels[x, y] = right_pixel
            pixels[image.width - x - 1, y] = left_pixel

    decrypted_image_path = "decrypted_" + image_path
    image.save(decrypted_image_path)
    return decrypted_image_path

def main():
    while True:
        print("\nImage Encryption Tool")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            image_path = input("Enter the image file path: ")
            key = int(input("Enter the XOR key: "))
            encrypted_image_path = encrypt_image(image_path, key)
            print(f"Encrypted image saved as: {encrypted_image_path}")
        elif choice == '2':
            image_path = input("Enter the encrypted image file path: ")
            key = int(input("Enter the XOR key: "))
            decrypted_image_path = decrypt_image(image_path, key)
            print(f"Decrypted image saved as: {decrypted_image_path}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()