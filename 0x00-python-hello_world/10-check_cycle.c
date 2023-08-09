#include "lists.h"

/**
 * check_if_has_cycle - checks if a linked listint_t has cycle
 * @listint_t: listint_t to check
 *
 * Return: 1 listint_t has cycle, 0 otherwise
 */
int check_cycle(listint_t *list);
{
	listint_t *first = list;
	listint_t *last = list;

	if (!list)
		return (0);

	while (first && last && last->next)
	{
		first = first->next;
		last = last->next->next;
		if (first == last)
			return (1);
	}

	return (0);
}
