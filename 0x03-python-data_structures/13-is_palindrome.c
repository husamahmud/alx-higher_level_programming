#include "lists.h"

/**
 * listint_len - length of linked list
 * @h: head of the list
 * Return: length of a list
 */
size_t listint_len(const listint_t *h)
{
	const listint_t *curr;
	int count = 0;

	curr = h;
	while (curr)
	{
		count++;
		curr = curr->next;
	}
	return (count);
}

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i, j;
	int n;
	int flag = 1;
	listint_t *temp = *head;
	int arr[2000] = {0};

	if (!*head)
		return (flag);

	n = listint_len(*head);
	for (i = 0; i < n; i++)
	{
		arr[i] = temp->n;
		temp = temp->next;
	}
	for (i = 0, j = n - 1; i < n && j > i; i++)
	{
		if (arr[i] != arr[j--])
			flag = 0;
	}
	return (flag);
}
