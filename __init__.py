# -*- coding: utf-8 -*-
#import random
import jugador
import juego
import computador

jugador1 = computador.Computadora("Computador 1", "1", "2")
#jugador2 = jugador.Jugador("jugador 2", "2")
jugador2 = computador.Computadora("Computador 2", "2", "1")

partida = juego.Juego(jugador1, jugador2, 2)
partida.jugar()