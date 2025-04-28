/// @file lib_uart.cpp
/// @brief Bibliothèque pour la communication UART sur microcontrôleur AVR.
/// Cette bibliothèque fournit des fonctions pour initialiser, envoyer et recevoir des données
/// via l'interface UART d'un microcontrôleur AVR.
/// @author Esteban Lemus-Lane
/// @date 2025-04-05
////////////////////////////
#ifndef LIB_UART_H_
#define LIB_UART_H_

#include <stdint.h>
///
/// @brief Initialise la communication UART.
/// Configure le baud rate, le mode asynchrone double vitesse,
/// active l'émission et la réception, et définit le format des données (8 bits, 1 stop bit).
/// @note Cette fonction doit être appelée avant toute autre opération UART.
/// @warning Assurez-vous que le microcontrôleur est configuré pour utiliser la fréquence d'horloge correcte.
///
void initUSART(void);
///
/// @brief Transmet un octet de données via UART.
/// @note Attend que le buffer de transmission soit vide, puis envoie la donnée.
/// @param data L'octet de données à transmettre.
///
void transmitByte(uint8_t data);
///
/// @brief Reçoit un octet de données via UART.
/// @note Attend que le buffer de réception soit plein, puis retourne la donnée reçue.
/// @return L'octet de données reçu.
///
uint8_t receiveByte(void);
///
/// @brief Transmet une chaîne de caractères via UART.
/// @note Transmet chaque caractère de la chaîne jusqu'à rencontrer le caractère nul.
/// @param MY_STRING La chaîne de caractères à transmettre.
///
void printString(const char MY_STRING[]);
