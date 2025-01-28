import pygame

class Button():
    def __init__(self, surface=None, x=None, y=None, size_width=None, size_height=None, base_color=None, hover_color=None, text_input=None, font=None):
        self.surface = surface
        self.x_pos = x
        self.y_pos = y
        self.size_width = size_width
        self.size_height = size_height
        self.base_color = base_color
        self.hover_color = hover_color
        self.text_input = text_input
        self.font = font
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.surface is None:
            self.surface = self.text
        else:
            self.surface = pygame.transform.smoothscale(self.surface, (size_width, size_height))
        
        self.rect = self.surface.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.surface is not None:
            screen.blit(self.surface, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hover_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
