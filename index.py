from PIL Image

def images_to_pdf(image_paths, output_pdf):

       image_list = [Image.open(image).convert('RGB') for image in image_paths]

     if image_list:
         image_list[0].save(output_pdf, save_all=True, append_images=image_list[1:])

    print(f"PDF saved successfully as {output_pdf}")

image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]

output_pdf = "output.pdf"

images_to_pdf(image_paths, output_pdf)