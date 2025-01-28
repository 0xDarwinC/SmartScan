# can pass into this on front end when create an Item object
    # MIGHT CREATE ANOTHER CLASS CALLED IMAGE INTAKE TO DO SO 
class Item: 
    # all of the attributes for each item. NOTE: all of these attributes except the last two are used in the current system. The only two we are adding are the image as a link/image path and the AI Description list 
    def __init__(self, incident, title, description, location, void, type, weight, RRDD, SLIC, discoDate, image, AIDescription):
        self.incident = incident
        self.title = title
        self.description = description
        self.location = location
        self.void = void 
        self.type = type
        self.weight = weight
        self.RRDD = RRDD
        self.SLIC = SLIC
        self.discoDate = discoDate
        self.image = image
        self.AIDescription = AIDescription
        # self.bounds = bounds
        self.keywords = AIDescription.split(",")
        self.match = False
        self.matchedItems = []

     # iterates through the AIDescription keywords and see if it matches a given searchWord -- provided from front end
    def searchMatch(self, searchWord):
        for word in self.Item.getKeywords():
            if searchWord == word:
                self.match = True
                self.matchedItems += [self.Item]

    def hasMatch(self):  
        return self.match

    def extract_objects(self, data):
        import re
        object_pattern = re.compile(r"([\w\s]+) \(confidence: ([\d\.]+)\)\nNormalized bounding polygon vertices:\n- \(([\d\.,\s]+)\)")
        matches = object_pattern.findall(data)
        objects = []
        for match in matches:
            name = match[0].strip()
            confidence = float(match[1])
            vertices = [tuple(map(float, vertex.strip().lstrip('(').rstrip(')').split(','))) for vertex in match[2].strip().split('\n- ')]
            objects.append({
                'name': name,
                'confidence': confidence,
                'vertices': vertices
            })
        return objects


    # Getter and setter for 'incident'
    def get_incident(self):
        return self.incident

    def set_incident(self, incident):
        self.incident = incident

    # Getter and setter for 'title'
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    # Getter and setter for 'description'
    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    # Getter and setter for 'location'
    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    # Getter and setter for 'void'
    def get_void(self):
        return self.void

    def set_void(self, void):
        self.void = void

    # Getter and setter for 'type'
    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    # Getter and setter for 'weight'
    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    # Getter and setter for 'RRDD'
    def get_RRDD(self):
        return self.RRDD

    def set_RRDD(self, RRDD):
        self.RRDD = RRDD

    # Getter and setter for 'SLIC'
    def get_SLIC(self):
        return self.SLIC

    def set_SLIC(self, SLIC):
        self.SLIC = SLIC

    # Getter and setter for 'discoDate'
    def get_discoDate(self):
        return self.discoDate

    def set_discoDate(self, discoDate):
        self.discoDate = discoDate

    # Getter and setter for 'image'
    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image

    # Getter and setter for 'AIDescription'
    def get_AIDescription(self):
        return self.AIDescription
    
    # def set_AIDescription(self, AIDescription):
    #     self.AIDescription = AIDescription

    # getter for keywords
    def get_keywords(self):
        return self.keywords

    
    # Getter and setter for 'bounds' -- THIS IS GOING TO BE 4 COORDINATES, NEED TO CHANGE
    # IDEA: COULD TRIGGER A HIGHLIGHTING FEATURE
    def get_AIDescription(self):
        return self.AIDescription
    # def set_bounds(self, bounds):
    #     self._bounds = bounds


    # SPLIT BOUNDS FUNCTION TO SEPARATE COORDINATES

    