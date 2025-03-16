import os
import argparse
from PIL import Image

def rotate_image(input_path, output_folder):
    """
    Rotates an input image by 2 degrees clockwise until completing a full 360 degrees.
    Saves each rotated image to the specified output folder.
    
    Args:
        input_path (str): Path to the input image file
        output_folder (str): Path to the folder where rotated images will be saved
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the original image
    try:
        original_image = Image.open(input_path)
        print(f"Successfully opened image: {input_path}")
    except Exception as e:
        print(f"Error opening image: {e}")
        return
    
    # Get the base filename without extension
    base_filename = os.path.splitext(os.path.basename(input_path))[0]
    
    # Perform rotations from 0 to 358 degrees in 2-degree increments
    for angle in range(0, 360, 2):
        # Create a copy of the original image and rotate it
        rotated_image = original_image.copy()
        rotated_image = rotated_image.rotate(-angle, expand=False, resample=Image.BICUBIC)
        
        # Save the rotated image with angle in filename
        output_path = os.path.join(output_folder, f"{base_filename}_rotated_{angle:03d}.png")
        try:
            rotated_image.save(output_path)
            print(f"Saved rotated image ({angle} degrees): {output_path}")
        except Exception as e:
            print(f"Error saving image at {angle} degrees: {e}")
    
    print(f"Rotation complete! All images saved to: {output_folder}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Rotate an image by 2 degrees incrementally for a full 360 degrees")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("output_folder", help="Path to the folder where rotated images will be saved")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Perform the rotation
    rotate_image(args.input_image, args.output_folder)