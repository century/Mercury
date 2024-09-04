#!/bin/bash

# Directory containing images (relative path)
IMAGE_DIR="string"

# Create an output directory for processed images (relative path)
OUTPUT_DIR="string2"
mkdir -p "$OUTPUT_DIR"

# Loop through all images in the directory
for img in "$IMAGE_DIR"/*; do
    # Get the filename without the path
    filename=$(basename "$img")
    
    # Convert the image using 'magick'
    magick "$img" \
        -colorspace Gray \                  # Convert image to grayscale
        -threshold 50% \                    # Apply a 50% threshold
        -fill "#ffffff" -opaque "white" \   # Replace white with #ffffff
        -fill "#202020" -opaque "black" \   # Replace black with #202020
        "$OUTPUT_DIR/$filename"             # Save the output image
done

echo "Processing complete. Converted images are saved in $OUTPUT_DIR."
