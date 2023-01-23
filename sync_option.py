from links import image_urls, number_of_images
import time
import requests


if __name__ == '__main__':
    application_start_time = time.perf_counter()

    for index, image_url in enumerate(image_urls):
        print(f'Processing {index + 1}/{number_of_images}')
        image_bytes = requests.get(image_url).content
        image_name = image_url.split('/')[-1]
        image_save_name = f'images/{image_name}.jpg'

        with open(image_save_name, 'wb') as image_file:
            image_file.write(image_bytes)
            print(f'{image_name} was downloaded!')

    application_end_time = time.perf_counter()

    print(
        f'Finished program in {round(application_end_time - application_start_time, 4)} second(s)!')
