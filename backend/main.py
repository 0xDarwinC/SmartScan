from Item import Item

def main():
    # Read AI Description from file
    with open("mockAI_Description.txt", "r") as file:
        AIDescription = file.read().strip()

    # Example mock data for other components
    incident = "mock_incident",
    title = "Balloon",
    description = "undetailed description",
    location = "mock_location",
    void = False,
    type = "mock_type",
    weight = 1.5
    RRDD = "mock_RRDD",
    SLIC = "mock_SLIC",
    discoDate = "2023-01-01",
    image =  "path/to/image.jpg",
    AIDescription = "AIDescription"


    # Create an Item object with mock data
    mockItem = Item(incident, title, description, location, void, type, weight, RRDD, SLIC, discoDate, image, AIDescription)

    # Extracted object data
    objects = mockItem.extract_objects(mockItem.get_AIDescription())

    # Summarize extracted data (assuming vertices are formatted as a list of tuples)
    for obj in objects:
        description = obj['name']
        confidence = obj['confidence']
        vertices = obj['vertices']  # Assuming vertices are directly accessible as a list of tuples

        # Print the extracted data
        print(f"Description: {description}")
        print(f"Confidence: {confidence}")
        print(f"Vertices: {vertices}")

    # Print the attributes of the mockItem object
    print(f"Incident: {mockItem.get_incident()}")
    print(f"Title: {mockItem.get_title()}")
    print(f"Description: {mockItem.get_description()}")
    print(f"Location: {mockItem.get_location()}")
    print(f"Void: {mockItem.get_void()}")
    print(f"Type: {mockItem.get_type()}")
    print(f"Weight: {mockItem.get_weight()}")
    print(f"RRDD: {mockItem.get_RRDD()}")
    print(f"SLIC: {mockItem.get_SLIC()}")
    print(f"Disco Date: {mockItem.get_discoDate()}")
    print(f"Image: {mockItem.get_image()}")
    print(f"AI Description: {mockItem.get_AIDescription()}")
    
    print(f"Keywords: {mockItem.get_keywords()}")  # Assuming keywords is an attribute of the Item class
    # print(f"Match: {mockItem.get_match()}")  # Assuming match is an attribute of the Item class
    print(f"Matched Items: {mockItem.matchedItems}")  # Assuming matchedItems is an attribute of the Item class

if __name__ == "__main__":
    main()
    
#     # # Summarize extracted data
#     # for obj in objects:
#     #     description = {obj['name']}
#     #     confidence = {obj['confidence']}
#     #     vertices = []
#     #     for vertex in obj['vertices']:
#     #         verticies += {vertex}
#     #     # Print the created Item object
#     # print(f"Incident: {mockItem.incident}")
#     # print(f"Title: {mockItem.title}")
#     # print(f"Description: {mockItem.description}")
#     # print(f"Location: {mockItem.location}")
#     # print(f"Void: {mockItem.void}")
#     # print(f"Type: {mockItem.type}")
#     # print(f"Weight: {mockItem.weight}")
#     # print(f"RRDD: {mockItem.RRDD}")
#     # print(f"SLIC: {mockItem.SLIC}")
#     # print(f"Disco Date: {mockItem.discoDate}")
#     # print(f"Image: {mockItem.image}")
#     # print(f"AI Description: {mockItem.AIDescription}")
#     # print(f"Bounds: {mockItem.bounds}")
#     # print(f"Keywords: {mockItem.keywords}")
#     # print(f"Match: {mockItem.match}")
#     # print(f"Matched Items: {mockItem.matchedItems}")
    
    
            


# # def main():
# #     # Simulated input for AI Description
# #     AIDescription = """
# #     Balloon (confidence: 0.7191542387008667)
# #     Normalized bounding polygon vertices:
# #     - (0.46484375, 0.0390625)
# #     - (0.57421875, 0.0390625)
# #     - (0.57421875, 0.234375)
# #     - (0.46484375, 0.234375)

# #     Electric Blue (confidence: 0.6439419984817505)
# #     Normalized bounding polygon vertices:
# #     - (0.0283203125, 0.0)
# #     - (0.50390625, 0.0)
# #     - (0.50390625, 0.9998292922973633)
# #     - (0.0283203125, 0.9998292922973633)
# #     """

# #     # Extracted object data
# #     objects = extract_objects(AIDescription)

# #     # Initialize variables to store extracted data
# #     descriptions = []
# #     confidences = []
# #     vertices_list = []

# #     # Iterate over each object and store extracted data
# #     for obj in objects:
# #         descriptions.append(obj['name'])
# #         confidences.append(obj['confidence'])
# #         vertices_list.append(obj['vertices'])

# #     # Example mock data for other components
# #     mock_data = {
# #         'incident': "mock_incident",
# #         'title': "Balloon",  # Assuming title is fixed for this example
# #         'description': descriptions[0],  # Assuming we take the first description
# #         'location': "mock_location",
# #         'void': False,
# #         'type': "mock_type",
# #         'weight': 1.5,
# #         'RRDD': "mock_RRDD",
# #         'SLIC': "mock_SLIC",
# #         'discoDate': "2023-01-01",
# #         'image': "path/to/image.jpg",
# #         'AIDescription': descriptions,  # List of all descriptions
# #         'confidence': confidences,  # List of all confidences
# #         'vertices': vertices_list  # List of all vertices lists
# #     }

# #     # Create an Item object with mock data
# #     item = Item(**mock_data)

# #     # Print the created Item object
# #     print(f"Incident: {item.incident}")
# #     print(f"Title: {item.title}")
# #     print(f"Description: {item.description}")
# #     print(f"Location: {item.location}")
# #     print(f"Void: {item.void}")
# #     print(f"Type: {item.type}")
# #     print(f"Weight: {item.weight}")
# #     print(f"RRDD: {item.RRDD}")
# #     print(f"SLIC: {item.SLIC}")
# #     print(f"Disco Date: {item.discoDate}")
# #     print(f"Image: {item.image}")
# #     print(f"AI Descriptions: {item.AIDescription}")
# #     print(f"Confidences: {item.confidence}")
# #     print(f"Vertices: {item.vertices}")
# #     print(f"Keywords: {item.keywords}")
# #     print(f"Match: {item.match}")
# #     print(f"Matched Items: {item.matchedItems}")