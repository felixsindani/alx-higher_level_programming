#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct lists - singly linked list
 * @a: interger
 * @next: ptr to next node
 * Description: singly linked list node struct
 */
typedef struct lists
{
	int a;
	struct lists *next;
} lists;
size_t print_listint(const lists *h);
lists *add_nodeint(lists **head, const int a);
void free_listint(lists *head);
int check_cycle(lists *list);

#endif

