import os
from PIL import Image, ImageDraw, ImageFont
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from extras.cleanup import cleanup


def multi_img(id, time):
    folder_path = "assets/temp/images/generated_images/"
    output_path = "assets/temp/images/chosen_images/"
    images_list = os.listdir(folder_path)

    if len(images_list) > 1:
        chose = ""
        while chose.lower() != "no" and chose.lower() != "n":
            # Create a list to hold the image files and their creation dates
            images = []

            # Loop through all files in the folder
            for filename in images_list:
                # Check if the file is an image
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    # Open the image file and get its creation date
                    image_path = os.path.join(folder_path, filename)
                    image = Image.open(image_path)
                    creation_date = os.path.getctime(image_path)

                    # Add the image file and its creation date to the list
                    images.append((creation_date, image))

            # Sort the images by creation date
            images.sort()

            # Combine the images into one image side by side with text labels
            width = sum(image.size[0] for _, image in images)
            height = max(image.size[1] for _, image in images)
            combined_image = Image.new("RGB", (width, height), color="white")
            x = 0

            # Create the draw object
            draw = ImageDraw.Draw(combined_image)
            font = ImageFont.truetype("arial.ttf", size=50)

            for i, (creation_date, image) in enumerate(images):
                combined_image.paste(image, (x, 0))
                draw.line((x, 0, x, height), fill=(0, 0, 0))
                draw.line((width - x - 1, 0, width - x - 1, height), fill=(0, 0, 0))
                x += image.size[0]

                # Add a text label with the creation date of the image
                label = f"Image number : {i+1}"
                text_width, text_height = draw.textsize(label, font=font)
                text_x = (x - image.size[0]) + ((image.size[0] - text_width) // 2)  # Center the text horizontally within the individual image
                text_y = image.size[1] - text_height - 10  # Move the text to the bottom with a margin of 10 pixels
                outline_color = (0, 0, 0)  # Black outline color
                fill_color = (255, 255, 255)  # White fill color
                stroke_width = 2  # Stroke width in pixels
                # Draw the text label with an outline and fill
                for stroke_x in range(-stroke_width, stroke_width + 1):
                    for stroke_y in range(-stroke_width, stroke_width + 1):
                        draw.text((text_x + stroke_x, text_y + stroke_y), label, font=font, fill=outline_color)
                draw.text((text_x, text_y), label, font=font, fill=fill_color)
            
            # Show the combined image in a new window
            combined_image.show()

            choice = ""
            while not choice.isdigit():
                # Let the user choose which image to pick
                choice = input("Enter the number of the image you want to pick : ")
                combined_image.close()
                
                if not choice.isdigit():
                    print("unknown choice")

            chosen_image = images[int(choice) - 1][1]
            chosen_image.show()

            chose = input("Want to change image to another from the given or type 'c' or 'change' to generate new image? y(yes)/n(no)/c(change) : ")

            # If user chooses the image, return its path
            if chose.lower() in ["no", "n"]:
                path_to_the_image = os.path.join(output_path, f"chosen_image_{id}.png")
                chosen_image.save(path_to_the_image)
                
                return path_to_the_image, chose.lower()
            
            elif chose.lower() in ["yes", "y"]:
                pass
            
            elif chose.lower() in ["c", "change"]:
                return None, chose.lower()
            else:
                print("Unknown choice")
    
    elif len(images_list) == 1:

        # Loop through all files in the folder
        for filename in images_list:
            image = Image.open(folder_path + filename)
            image.show(image)

            sure = ""
            while sure.lower() != "yes" and sure.lower() != "no" and sure.lower() != "n" and sure.lower() != "y":
                sure = input("Is this image ok (if typed 'no' generate new image)? y(yes)/n(no) : ")

                if sure.lower() == "yes" or sure.lower() == "y":
                    path_to_the_image = os.path.join(output_path, f"chosen_image_{id}.png")
                    image.save(path_to_the_image)

                    return path_to_the_image, "n"
                elif sure.lower() in ["no", "n"]:
                    return None, "c"
                else:
                    print("Unknown choice")
    elif len(images_list) == None:
        print("An error occurred")
        exit()
