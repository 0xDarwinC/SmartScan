import re
from PIL import Image, ImageDraw, ImageFont

# Updated Google Cloud Vision API output with multiple objects
vision_output = """
Number of objects found: 4

Basketball (confidence: 0.7614322900772095)
Normalized bounding polygon vertices: 
- (0.4609375, 0.265625)
- (0.56640625, 0.265625)
- (0.56640625, 0.404296875)
- (0.4609375, 0.404296875)

Bagged packaged goods (confidence: 0.6868757009506226)
Normalized bounding polygon vertices: 
- (0.1708984375, 0.1845703125)
- (0.3828125, 0.1845703125)
- (0.3828125, 0.54296875)
- (0.1708984375, 0.54296875)

Ball (confidence: 0.5645483136177063)
Normalized bounding polygon vertices: 
- (0.4609375, 0.265625)
- (0.56640625, 0.265625)
- (0.56640625, 0.404296875)
- (0.4609375, 0.404296875)

Bottled and jarred packaged goods (confidence: 0.5136691331863403)
Normalized bounding polygon vertices: 
- (0.035888671875, 0.314453125)
- (0.1533203125, 0.314453125)
- (0.1533203125, 0.4765625)
- (0.035888671875, 0.4765625)
"""

# Function to extract objects from vision API output
def extract_objects(data):
    # Pattern to match each object and its vertices
    object_pattern = re.compile(r"([\w\s]+) \(confidence: ([\d\.]+)\)\nNormalized bounding polygon vertices:\n((?:- \([\d\., ]+\)\n)+)")
    matches = object_pattern.findall(data)
    
    objects = []
    for match in matches:
        name = match[0].strip()
        confidence = float(match[1].strip())
        vertices_str = match[2].strip().split('\n')
        vertices = [tuple(map(float, re.findall(r"[\d\.]+", vertex))) for vertex in vertices_str if vertex.strip()]
        
        # Ensure at least one vertex is found; handle potential errors gracefully
        if vertices:
            objects.append({
                'name': name,
                'confidence': confidence,
                'vertices': vertices
            })
        else:
            print(f"Warning: No vertices found for object '{name}'")
    
    return objects

# Convert normalized vertices to image coordinates
def convert_normalized_vertices(vertices, width, height):
    return [(int(float(x) * width), int(float(y) * height)) for x, y in vertices]

# Path to the image file
image_path = "path_to_your_image.jpg"

# Open the image
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

# Font for the labels (optional, you can choose a different font)
try:
    font = ImageFont.truetype("arial.ttf", 30)
except IOError:
    font = ImageFont.load_default()

# Extract objects from the vision output
objects = extract_objects(vision_output)

# Draw rectangles and labels on the image
for obj in objects:
    name = obj['name']
    confidence = obj['confidence']
    vertices = obj['vertices']
    image_width, image_height = image.size
    vertices = convert_normalized_vertices(vertices, image_width, image_height)
    
    # Check if vertices are valid
    if len(vertices) < 2:
        print(f"Skipping object {name} due to insufficient vertices.")
        continue
    
    # Draw the rectangle
    draw.polygon(vertices, outline="red")
    
    # Calculate the upper left corner position for the label
    min_x = min([x for x, y in vertices])
    min_y = min([y for x, y in vertices])
    
    # Label the object with name and confidence
    label = f"{name} (Confidence: {confidence:.2f})"
    draw.text((min_x, min_y), label, fill="red", font=font)

# Save or display the image
output_path = "output_image.jpg"
image.save(output_path)
image.show()
