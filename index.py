from PIL Image

def images_to_pdf(image_paths, output_pdf):

       image_list = [Image.open(image).convert('RGB') for image in image_paths]