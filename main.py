from classes import *
from variables import *
from settings import *
import random


while run:
    win.fill((0, 0, 0))
    win.blit(bg, (0, 0))
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for e in enem:
        if e.y in range(-300, 500) and e.hp > 0:
            e.y -= e.vel
        else:
            score += 1
            enem.pop(enem.index(e))
    for eny in enem2:
        if eny.y in range(-300, 500) and eny.hp > 0:
            eny.y -= eny.vel
        else:
            score += 1
            enem2.pop(enem2.index(eny))

    if hp == 40:
        if (len(healing)) < 1:
            temp = random.randint(1, 100)
            if temp > 50:
                if score < 20000:
                    healing.append(heal(10, 460, -30, 30, (255, 255, 0)))
                if score > 20000:
                    healing.append(heal(870, 460, -30, 30, (255, 255, 0)))
            else:
                if score < 20000:
                    healing.append(heal(460, 460, -30, 30, (255, 255, 0)))
                if score > 20000:
                    healing.append(heal(190, 460, -30, 30, (255, 255, 0)))
    if len(healing) > 0:
        for he in healing:
            if (x == he.x + 30) or (x == he.x) or (x + 50 == he.x):
                bonus.play()
                hp += 40
                score += 150
                healing.pop(healing.index(he))

    for bullet in bullets:
        if bullet.y in range(0, 500):
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    for bullet in bullets:
        for e in enem:
            enm = pygame.Rect(e.x, e.y, e.wig, e.hig)
            bull = pygame.Rect(bullet.x, bullet.y, bullet.wig, bullet.hig)
            if enm.colliderect(bull):
                bullets.pop(bullets.index(bullet))
                e.hp -= 50
                win.blit(anim[0], (bullet.x, bullet.y + 25))
                if e.hp > 0:
                    shortExplosion.play()
                else:
                    score += 1000
                    enem.pop(enem.index(e))
                    win.blit(anim[1], (bullet.x, bullet.y + 25))
                    explosion.play()
    for bullet in bullets:
        for eny in enem2:
            enym = pygame.Rect(eny.x, eny.y, eny.wig, eny.hig)
            bull = pygame.Rect(bullet.x, bullet.y, bullet.wig, bullet.hig)
            if enym.colliderect(bull):
                bullets.pop(bullets.index(bullet))
                eny.hp -= 50
                win.blit(anim[0], (bullet.x, bullet.y + 25))
                if eny.hp > 0:
                    shortExplosion.play()
                else:
                    score += 1000
                    enem2.pop(enem2.index(eny))
                    win.blit(anim[1], (bullet.x, bullet.y + 25))
                    explosion.play()
    for en in enem:
        e = pygame.Rect(en.x, en.y, en.wig, en.hig)
        me = pygame.Rect((x, y), (h, w))
        if me.colliderect(e) or e.colliderect(me):
            hurt.play()
            enem.pop(enem.index(en))
            hp -= 20
            if hp <= 0:
                run = False
    for vr in enem2:
        eny = pygame.Rect(vr.x, vr.y, vr.wig, vr.hig)
        me = pygame.Rect((x, y), (h, w))
        if me.colliderect(eny) or eny.colliderect(me):
            hurt.play()
            enem2.pop(enem2.index(vr))
            hp -= 20
            if hp <= 0:
                run = False

    if y < 500:
        facing = -2
        if score < 20000:
            if len(enem) < 16:
                enem.append(enemy(random.randint(5, 995), random.randint(-200, 0), 10, 30, (0, 255, 0), facing, 100))
        else:
            if len(enem) < 30:
                enem.append(enemy(random.randint(5, 995), random.randint(-200, 0), 10, 30, (0, 255, 0), facing, 100))

    if y < 500:
        facing = -2
        if score < 20000:
            if len(enem2) < 20:
                enem2.append(
                    enemy2(random.randint(5, 995), random.randint(-200, 0), 10, 30, (0, 255, 0), facing, 100))
        else:
            if len(enem2) < 45:
                enem2.append(
                    enemy2(random.randint(5, 995), random.randint(-200, 0), 10, 30, (0, 255, 0), facing, 100))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        facing = 3
        if len(bullets) < 5:
            bullets.append(sn(x + 25, y + 5, 10, 10, (0, 255, 255), facing))
            shot.play()
    if keys[pygame.K_LEFT] and x > 10:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 990 - h:
        x += speed
        right = True
        left = False
    else:
        right = False
        left = False
    for bullet in bullets:
        win.blit(bomb, (bullet.x, bullet.y))
    for e in enem:
        win.blit(staloktit, (e.x - 36, e.y - 38))
    for eny in enem2:
        win.blit(staloktit2, (eny.x - 36, eny.y - 38))

    for he in healing:
        win.blit(heart2, (he.x - 17, he.y - 60))

    font = pygame.font.Font(None, 20)
    text = font.render("HP: ", True, (255, 0, 0))
    text2 = font.render(str(hp), True, (255, 0, 0))
    text3 = font.render(str(score), True, (255, 0, 0))
    text4 = font.render("SCORE: ", True, (255, 0, 0))

    win.blit(text, [10, 20])
    win.blit(text2, [70, 20])
    win.blit(text3, [70, 40])
    win.blit(text4, [10, 40])


    def animation():
        if left:
            win.blit(goLeft, (x, y - 20))
        elif right:
            win.blit(goRight, (x, y - 20))
        else:
            win.blit(idle, (x, y - 20))


    animation()

    pygame.display.update()
