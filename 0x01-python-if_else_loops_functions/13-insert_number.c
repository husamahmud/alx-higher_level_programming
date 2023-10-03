#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - insert node in a sorted way
 * @head: head of the list
 * @number: data of the list
 * Return: pointer to the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = malloc(sizeof(listint_t));
	listint_t *cur;

	if (!temp)
		return (NULL);
	cur = *head;
	temp->n = number;
	if (!cur)
	{
		*head = temp;
		return (temp);
	}
	if (cur->n > number)
	{
		temp->next = *head;
		*head = temp;
		return (temp);
	}
	while (cur->next)
	{
		if (cur->next->n > number)
		{
			temp->next = cur->next;
			cur->next = temp;
			return (temp);
		}
		cur = cur->next;
	}
	cur->next = temp;
	temp->next = NULL;
	return (temp);
}
