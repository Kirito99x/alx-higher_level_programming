#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *current_cycle = list;
	listint_t *check_cycle = list;

	if (!list)
		return (0);

	while (current_cycle && check_cycle && check_cycle->next)
	{
		current_cycle = current_cycle->next;
		check_cycle = check_cycle->next->next;
		if (current_cycle == check_cycle)
			return (1);
	}

	return (0);
}
