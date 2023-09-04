#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 * If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *paced_slow = list;
	listint_t *paced_fast = list;

	while (paced_slow && paced_fast && paced_fast->next)
	{
		paced_slow = paced_slow->next;
		paced_fast = paced_fast->next->next;
		if (paced_slow == paced_fast)
			return (1);
	}
	return (0);
}
