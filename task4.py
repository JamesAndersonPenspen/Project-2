class Vector:
    def __init__(vector1,*components):
        vector1.components = list(components)

    def __str__(self):
        