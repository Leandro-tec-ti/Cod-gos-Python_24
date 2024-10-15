# Exercicio 21
# Faça um programa que abra e reproduza o audio de um arquivo mp3.
import pygame
pygame.init()
pygame.mixer.music.load("Gustavo Guanabara/musica021.mp3")
pygame.mixer.music.play()
pygame.event.wait()