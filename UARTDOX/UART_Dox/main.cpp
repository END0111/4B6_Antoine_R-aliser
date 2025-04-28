/////////////////////////////
 /// @file main.cpp
 /// @brief Programme principal pour la communication UART et l'affichage sur PORTB (C++).
 /// @warning Ce programme initialise la communication UART, reçoit un caractère,
 /// @attention le renvoie via UART et affiche sa valeur ASCII sur le PORTB.
 /// @author Esteban Lemus-Lane
 /// @date 2025-04-05

 #define F_CPU 1000000UL
 #include <avr/io.h>
 #include <avr/sfr_defs.h>
 #include "lib_uart.h"
 
  ///
  /// @brief Fonction principale du programme (C++).
  /// @note Initialise la communication UART, configure le PORTB en sortie, et attend la réception de caractères via UART.
  /// @return Code de sortie du programme (0 en cas de succès).
  ///
 int main(void) {
     char serialCharacter; /*< Caractère reçu via UART. */
 
     DDRB = 0xff; /*< Configure le PORTB en sortie. */
     initUSART(); /*< Initialise la communication UART. */
     printString("Bonjour, taper un caractère:"); /*< Affiche un message d'invite. */
 
     while (1) {
         serialCharacter = receiveByte(); /*< Lit un caractère depuis UART. */
         transmitByte(serialCharacter); /*< Renvoie le caractère via UART. */
         PORTB = serialCharacter; /*< Affiche le code ASCII sur le PORTB. */
     }
 
     return (0);
 }
 