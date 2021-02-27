import base64


def encode_image(image):

	with open(image, "rb") as img_file:

		my_string = base64.b64encode(img_file.read())

	with open(r'E:\prog\testfile.txt', 'w') as File:

		File.write((my_string.decode('utf-8')))


if __name__ == '__main__':

	file = input("enter the path for image: ") #r'C:\Users\User\Desktop\jiko\dog-breed-identification\train\000bec180eb18c7604dcecc8fe0dba07.jpg'

	encode_image(file)