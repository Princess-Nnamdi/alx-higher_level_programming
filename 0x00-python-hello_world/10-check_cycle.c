#include "lists.h"

/**
 * check_cycle- function checks if a sinlgy kinked lists has a cycle
 * @list: pointer to head of node
 * Return: 0 on success and 1 on failure
 **/

int check_cycle(listint_t *list)
{
	listint_t *current, *checker;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	checker = current->next;

	while (current && checker->next && checker->next->next)
	{
	if (current == checker)
		return (1);
	current = current->next;
	checker = checker->next->next;
	}
	return (0);
}
