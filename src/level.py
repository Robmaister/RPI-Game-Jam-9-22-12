import tileset

class Level(object):
    def __init__(self, filepath):
        self.tileset = tileset.Tileset(filepath)
        
    def get_walls(self):
        return self.tileset.get_walls()
    
    def draw(self, screen):
        self.tileset.render(screen)