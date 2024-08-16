import pygame
import constant


class Character:
    def __init__(self, x, y, animation):

        self.animation = animation
        # Image of the character in the game
        self.frame_index = 0
        self.updateTime = pygame.time.get_ticks()

        # Time when the game started
        self.image = animation[self.frame_index]

        self.shape = self.image.get_rect()
        self.shape.center = (x, y)
        self.flip = False

    def update_animation(self):
        cooldownAnimation = 100
        self.image = self.animation[self.frame_index]
        if pygame.time.get_ticks() - self.updateTime > cooldownAnimation:
            self.updateTime = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation):
                self.frame_index = 0

    def draw(self, window):
        # pygame.draw.rect(window, constant.colorCharacter, self.shape, width=1)
        imageFlip = pygame.transform.flip(self.image, self.flip, False)
        window.blit(imageFlip, self.shape)

    def move(self, deltaX, deltaY):
        if deltaX < 0:
            self.flip = True
        if deltaX > 0:
            self.flip = False

        self.shape.x = self.shape.x + deltaX
        self.shape.y = self.shape.y + deltaY
