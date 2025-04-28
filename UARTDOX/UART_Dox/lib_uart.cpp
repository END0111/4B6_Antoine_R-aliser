/////////////////////////////
/// @author Esteban Lemus-Lane
/// @date 2025-04-05
/// @file lib_uart.cpp
/// @brief Bibliothèque pour la communication UART sur microcontrôleur AVR.
/// @warning Cette bibliothèque est conçue pour être utilisée avec des microcontrôleurs AVR.
/// @attention Elle fournit des fonctions pour initialiser, envoyer et recevoir des données

#define F_CPU 1000000UL
#include <avr/io.h>
#include <avr/sfr_defs.h>
#include <util/delay.h>
#include "lib_uart.h"

///@brief Initialise la communication UART. 
///@note Configure le baud rate, le mode asynchrone double vitesse,
///@param initUART : valeur de la variable de configuration du microcontoleur

void initUSART(void) {
	UBRR0 = 12;              /* baud rate 9600 */
	UCSR0A |= (1 << U2X0);      /* mode asynchrone double vitesse */
	UCSR0B |= (1 << TXEN0) | (1 << RXEN0);    /* Activer émission et réception  USART */
	UCSR0C |= (1 << UCSZ01) | (1 << UCSZ00);   /* 8 data bits, 1 stop bit, valeur au reset*/
}
 ///@brief Transmet un octet de données via UART.
 ///@note Attend que le buffer de transmission soit vide, puis envoie la donnée.
 ///@param data L'octet de données à transmettre.
void transmitByte(uint8_t data) {
	loop_until_bit_is_set(UCSR0A, UDRE0);  /* Attendre que le buffer de transmission soit vide */
	UDR0 = data;                      /* envoyer la donnée */
}
 ///@brief Reçoit un octet de données via UART.
 ///@note Attend que le buffer de réception soit plein, puis retourne la donnée reçue.
 ///@return L'octet de données reçu.
uint8_t receiveByte(void) {
	loop_until_bit_is_set(UCSR0A, RXC0);  /* Attendre que le buffer de réception soit plein */
	return UDR0;                                /* retourner la valeur lue */
}
///@brief Transmet une chaîne de caractères via UART.    
///@note Transmet chaque caractère de la chaîne jusqu'à rencontrer le caractère nul.
///@param MY_STRING La chaîne de caractères à transmettre.
void printString(const char MY_STRING[]) {
	uint8_t i = 0;               
	while (MY_STRING[i]) {               /* Transmettre des caractères de la chaine */
		transmitByte(MY_STRING[i]);
		i++;
	}
    
}