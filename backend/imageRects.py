import re
from PIL import Image, ImageDraw, ImageFont

# Example Google Cloud Vision API output
vision_output = """
Number of objects found: 2

Balloon (confidence: 0.7191542387008667)
Normalized bounding polygon vertices:
- (0.46484375, 0.0390625)
- (0.57421875, 0.0390625)
- (0.57421875, 0.234375)
- (0.46484375, 0.234375)

Electric Blue (confidence: 0.6439419984817505)
Normalized bounding polygon vertices:
- (0.0283203125, 0.0)
- (0.50390625, 0.0)
- (0.50390625, 0.9998292922973633)
- (0.0283203125, 0.9998292922973633)
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
        vertices = [tuple(map(float, re.findall(r"[\d\.]+", vertex))) for vertex in vertices_str]
        objects.append({
            'name': name,
            'confidence': confidence,
            'vertices': vertices
        })
    return objects

# Convert normalized vertices to image coordinates
def convert_normalized_vertices(vertices, width, height):
    return [(int(x * width), int(y * height)) for x, y in vertices]

# Path to the image file
image_path = r"C:\Users\jdog1\Downloads\IMG_0692.jpg"

# Open the image
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

# Font for the labels (optional, you can choose a different font)
try:
    font = ImageFont.truetype("arial.ttf", 110)  # Increased font size to 30
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

    print(f"Object: {name}")
    print(f"Vertices: {vertices}")
    
    # Check if vertices are valid
    if len(vertices) < 2:
        print(f"Skipping object {name} due to insufficient vertices.")
        continue
    
    # Draw the rectangle
    draw.polygon(vertices, outline="red", width=20)
    
    # Calculate the upper left corner position for the label
    min_x = min([x for x, y in vertices])
    min_y = min([y for x, y in vertices])
    
    # Label the object with name and confidence
    label = f"{name} (Confidence: {confidence:.2f})"
    draw.text((min_x, min_y), label, fill="red", font=font)

# Save or display the image
output_path = r"C:\Users\jdog1\Downloads\output_IMG_0692_with_confidence.jpg"
image.save(output_path)
image.show()
