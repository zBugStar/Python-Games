import pygame
import constant
import math


class Weapon:
    def __init__(self, image, imageBullet):
        self.imageBullet = imageBullet
        self.imageOriginal = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.imageOriginal, self.angle)
        self.shape = self.image.get_rect()
        self.shot = False
        self.last_shot = pygame.time.get_ticks()

    def update(self, character):
        bullet = None
        self.shape.center = character.shape.center

        if not character.flip:
            self.shape.x = self.shape.x + character.shape.width / 2
            self.shape.y = self.shape.y + character.shape.height / 4.5
            self.rotateWeapon(False)
        if character.flip:
            self.shape.x = self.shape.x - character.shape.width / 2
            self.shape.y = self.shape.y + character.shape.height / 4.5
            self.rotateWeapon(True)

        # Move pistol with teh mouse
        mouse = pygame.mouse.get_pos()
        distanceX = mouse[0] - self.shape.centerx
        distanceY = -(mouse[1] - self.shape.centery)
        self.angle = math.degrees(math.atan2(distanceY, distanceX))

        if (pygame.mouse.get_pressed()[0] and self.shot == False
                and (pygame.time.get_ticks() - self.last_shot > constant.coolDownBullet)):

            bullet = Bullet(self.imageBullet, self.shape.centerx, self.shape.centery, self.angle)
            self.shot = True
            self.last_shot = pygame.time.get_ticks()

        # reset the click

        if not pygame.mouse.get_pressed()[0]:
            self.shot = False

        return bullet

    def rotateWeapon(self, rotate):
        if rotate:
            image_flip = pygame.transform.flip(self.imageOriginal, True, False)
            self.image = pygame.transform.rotate(image_flip, self.angle)
            if self.angle > 90:
                self.image = pygame.transform.flip(self.image, False, True)

        else:
            image_flip = pygame.transform.flip(self.imageOriginal, False, False)
            self.image = pygame.transform.rotate(image_flip, self.angle)
            if self.angle < -90:
                self.image = pygame.transform.flip(self.image, False, True)

    def draw(self, window):
        self.image = pygame.transform.rotate(self.image, self.angle)
        window.blit(self.image, self.shape)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.imageOriginal = image
        self.angle = angle
        self.image = pygame.transform.rotate(self.imageOriginal, self.angle)
        self.shape = self.image.get_rect()
        self.shape.center = (x, y)

        self.deltaX = constant.velocity_bullet * math.cos(math.radians(self.angle))
        self.deltaY = -constant.velocity_bullet * math.sin(math.radians(self.angle))

    def update(self):
        self.shape.x += self.deltaX
        self.shape.y += self.deltaY

    def draw(self, window):
        window.blit(self.image, (self.shape.centerx, self.shape.centery - int(self.image.get_height())))
