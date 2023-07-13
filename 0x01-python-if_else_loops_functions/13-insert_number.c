#include "lists.h"
#include <stddef.h>

/**
 * insert_node - functuon that inserts a number into
 * a sorted singly linked list.
 * @head: pointer to the head of the list.
 * @number: the number to insert.
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *cur_node = *head;
	listint_t *prev_node = NULL;

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (cur_node != NULL && cur_node->n < number)
	{
		prev_node = cur_node;
		cur_node = cur_node->next;
	}

	new_node->next = cur_node;
	prev_node->next = new_node;

	return (new_node);
}

