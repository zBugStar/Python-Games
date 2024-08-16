import pygame
import constant
from character import Character
from weapon import Weapon

pygame.init()

window = pygame.display.set_mode((constant.heightWindow, constant.widthWindow))
pygame.display.set_caption("First Game")

clock = pygame.time.Clock()


def scaleImage(image, scala):
    height = image.get_height()
    width = image.get_width()
    newImage = pygame.transform.scale(image, (width * scala, height * scala))
    return newImage


# Import the images

# Player
animation = []
for i in range(1, 8):
    image = pygame.image.load(f"assets//image//characters//player//DinoSprites{i}.png")
    image = scaleImage(image, constant.scala_character)
    animation.append(image)

# Weapon
image_pistol = pygame.image.load("assets//image//weapons//Pistol1.png")
image_pistol = scaleImage(image_pistol, constant.scala_weapon)

# bullet
image_bullet = pygame.image.load("assets//image//weapons//bullet.png")
image_bullet = scaleImage(image_bullet, constant.scala_bullet)

# We create the player
player = Character(constant.spawnCharacterX, constant.spawnCharacterY, animation)

# We create the weapon
pistol = Weapon(image_pistol, image_bullet)

# We sprites group
bulletGroup = pygame.sprite.Group()

# We define motion variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

running = True

while running:
    # We set the frame rate
    clock.tick(constant.FPS)

    # This means that when our character moves, it leaves no trace
    window.fill(constant.backGroundColor)

    # Calculate the motion of the player
    deltaX = 0
    deltaY = 0

    if moveLeft:
        deltaX = constant.velocity_character
    if moveRight:
        deltaX = -constant.velocity_character
    if moveUp:
        deltaY = -constant.velocity_character
    if moveDown:
        deltaY = constant.velocity_character

    if deltaX == 0 and deltaY == 0:
        player.frame_index = 0

    # move the player
    player.move(deltaX, deltaY)

    # Update the status of the player
    player.update_animation()
    # Update the status of the weapon
    bullet = pistol.update(player)
    if bullet:
        bulletGroup.add(bullet)

    for bullet in bulletGroup:
        bullet.update()
        if (bullet.shape.x < 0 or bullet.shape.x > constant.widthWindow or
                bullet.shape.y < 0 or bullet.shape.y > constant.heightWindow):
            bulletGroup.remove(bullet)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Activate the movement of the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moveRight = True
            if event.key == pygame.K_d:
                moveLeft = True
            if event.key == pygame.K_w:
                moveUp = True
            if event.key == pygame.K_s:
                moveDown = True

        # Deactivate the movement of the player
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moveRight = False
            if event.key == pygame.K_d:
                moveLeft = False
            if event.key == pygame.K_w:
                moveUp = False
            if event.key == pygame.K_s:
                moveDown = False

    # Draw the elements
    player.draw(window)
    pistol.draw(window)

    for bullet in bulletGroup:
        bullet.draw(window)

    pygame.display.update()

pygame.quit()
