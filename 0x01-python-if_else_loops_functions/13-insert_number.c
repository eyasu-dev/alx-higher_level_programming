#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: a pointer to the new node or NULL on failure.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_list;
	listint_t *current_head;

	current_head = *head;

	new_list = malloc(sizeof(listint_t));
	if (new_list == NULL)
		return (NULL);

	new_list->n = number;

	if (current_head == NULL || current_head->n >= number)
	{
		new_list->next = current_head;
		*head = new_list;
		return (new_list);
	}

	while (current_head->next && current_head->next->n < number)
		current_head = current_head->next;

	new_list->next = current_head->next;
	current_head->next = new_list;

	return (new_list);
}
