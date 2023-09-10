#include "lists.h"

/**
 * reverse_list - reverses the second half of the list
 * @head_rev: head of the second half
 * Return: void function
 */
void reverse_list(listint_t **head_rev)
{
	listint_t *prev;
	listint_t *curr;
	listint_t *next;

	prev = NULL;
	curr = *head_rev;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*head_rev = prev;
}

/**
 * compare_list_int - compares each int of the list
 * @head1: head of the first half
 * @head2: head of the second half
 * Return: 1 if both are equals, 0 if not
 */
int compare_list_int(listint_t *head1, listint_t *head2)
{
	listint_t *tmp1;
	listint_t *tmp2;

	tmp1 = head1;
	tmp2 = head2;

	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (tmp1 == NULL && tmp2 == NULL)
	{
		return (1);
	}

	return (0);
}


/**
 * is_palindrome - checks if a linked list
 * is a palindrome
 * @head: the pointer to the head of a list
 * Return: 0 if it is not a palindrome
 * ******* 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scan_half, *middle;
	int is_palin;

	slow = fast = prev_slow = *head;
	middle = NULL;
	is_palin = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scan_half = slow;
		prev_slow->next = NULL;
		reverse_list(&scan_half);
		is_palin = compare_list_int(*head, scan_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scan_half;
		}
		else
		{
			prev_slow->next = scan_half;
		}
	}

	return (is_palin);
}
