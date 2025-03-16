# import os
# import argparse
# from PIL import Image

# def rotate_image(input_path, output_folder):
#     """
#     Rotates an input image by 2 degrees clockwise until completing a full 360 degrees.
#     Saves each rotated image to the specified output folder.
    
#     Args:
#         input_path (str): Path to the input image file
#         output_folder (str): Path to the folder where rotated images will be saved
#     """
#     # Create output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)
    
#     # Open the original image
#     try:
#         original_image = Image.open(input_path)
#         print(f"Successfully opened image: {input_path}")
#     except Exception as e:
#         print(f"Error opening image: {e}")
#         return
    
#     # Get the base filename without extension
#     base_filename = os.path.splitext(os.path.basename(input_path))[0]
    
#     # Perform rotations from 0 to 358 degrees in 2-degree increments
#     for angle in range(0, 360, 2):
#         # Create a copy of the original image and rotate it
#         rotated_image = original_image.copy()
#         rotated_image = rotated_image.rotate(-angle, expand=False, resample=Image.BICUBIC)
        
#         # Save the rotated image with angle in filename
#         output_path = os.path.join(output_folder, f"{base_filename}_rotated_{angle:03d}.png")
#         try:
#             rotated_image.save(output_path)
#             print(f"Saved rotated image ({angle} degrees): {output_path}")
#         except Exception as e:
#             print(f"Error saving image at {angle} degrees: {e}")
    
#     print(f"Rotation complete! All images saved to: {output_folder}")

# if __name__ == "__main__":
#     # Set up argument parser
#     parser = argparse.ArgumentParser(description="Rotate an image by 2 degrees incrementally for a full 360 degrees")
#     parser.add_argument("input_image", help="Path to the input image file")
#     parser.add_argument("output_folder", help="Path to the folder where rotated images will be saved")
    
#     # Parse arguments
#     args = parser.parse_args()
    
#     # Perform the rotation
#     rotate_image(args.input_image, args.output_folder)


import os
from PIL import Image

def is_image_file(filename):
    """Check if a file is an image based on its extension."""
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def rotate_image(input_path, output_folder, base_filename):
    """
    Rotates an input image by 2 degrees clockwise until completing a full 360 degrees.
    Saves each rotated image to the specified output folder.
    
    Args:
        input_path (str): Path to the input image file
        output_folder (str): Path to the folder where rotated images will be saved
        base_filename (str): Base filename for the output files
    """
    # Open the original image
    try:
        original_image = Image.open(input_path)
        print(f"Successfully opened image: {input_path}")
    except Exception as e:
        print(f"Error opening image: {e}")
        return False
    
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
            return False
    
    return True

def process_folder(input_folder, output_folder):
    """
    Process all image files in the input folder and rotate them.
    
    Args:
        input_folder (str): Path to the folder containing images
        output_folder (str): Path to the folder where rotated images will be saved
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all files in the input folder
    files = os.listdir(input_folder)
    image_files = [f for f in files if is_image_file(f)]
    
    if not image_files:
        print(f"No image files found in {input_folder}")
        return
    
    print(f"Found {len(image_files)} image file(s) to process.")
    
    successful = 0
    failed = 0
    
    # Process each image file
    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        base_filename = os.path.splitext(image_file)[0]
        
        print(f"\nProcessing image: {image_file}")
        if rotate_image(input_path, output_folder, base_filename):
            successful += 1
            print(f"Successfully rotated {image_file}")
        else:
            failed += 1
            print(f"Failed to rotate {image_file}")
    
    print("\n" + "=" * 50)
    print(f"Processing complete!")
    print(f"Successfully rotated: {successful} image(s)")
    print(f"Failed to rotate: {failed} image(s)")
    print(f"All rotated images saved to: {output_folder}")
    print("=" * 50)

def main():
    print("=" * 50)
    print("FOLDER IMAGE ROTATION TOOL")
    print("=" * 50)
    print("This tool will rotate all images in a folder by 2 degrees clockwise")
    print("until completing a full 360 degrees (180 rotated images per original).")
    print()
    
    # Get input folder path
    while True:
        input_folder = input("Enter the path to the folder containing images: ").strip()
        
        # Remove quotes if the user added them
        input_folder = input_folder.strip('"\'')
        
        if not os.path.isdir(input_folder):
            print("Error: Folder not found. Please enter a valid folder path.")
        else:
            files = os.listdir(input_folder)
            image_files = [f for f in files if is_image_file(f)]
            if not image_files:
                print("Warning: No image files found in this folder.")
                if input("Do you want to choose a different folder? (y/n): ").lower() == 'y':
                    continue
            break
    
    # Get output folder path
    while True:
        output_folder = input("Enter the path to save rotated images: ").strip()
        
        # Remove quotes if the user added them
        output_folder = output_folder.strip('"\'')
        
        try:
            # Create output folder if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)
            print(f"Output folder will be: {output_folder}")
            break
        except Exception as e:
            print(f"Error creating output folder: {e}")
            print("Please enter a valid folder path.")
    
    # # Confirm before proceeding
    # print("\nReady to process images:")
    # print(f"Input folder: {input_folder}")
    # print(f"Output folder: {output_folder}")
    
    # confirm = input("\nProceed? (y/n): ").lower()
    # if confirm != 'y' and confirm != 'yes':
    #     print("Operation cancelled.")
    #     return
    
    # Process the folder
    process_folder(input_folder, output_folder)

if __name__ == "__main__":
    main()