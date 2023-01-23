from links import image_urls, number_of_images, indexes
import time
import requests
import concurrent.futures


def download_image(image_url, index):
    print(f'Processing {index}/{number_of_images}')
    image_bytes = requests.get(image_url).content
    image_name = image_url.split('/')[-1]
    image_save_name = f'images/{image_name}.jpg'

    with open(image_save_name, 'wb') as image_file:
        image_file.write(image_bytes)
        print(f'{image_name} was downloaded!')


if __name__ == '__main__':
    application_start_time = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, image_urls, indexes)

    application_end_time = time.perf_counter()

    print(
        f'Finished program in {round(application_end_time - application_start_time, 4)} second(s)!')
