#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to a pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow = NULL, *mid_node = NULL;
	listint_t *second_half, *temp;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);

	slow = *head;
	fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	second_half = slow;
	prev_slow->next = NULL;
	reverse_list(&second_half);
	is_palindrome = compare_lists(*head, second_half);
	reverse_list(&second_half);

	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second_half;
	}
	else
		prev_slow->next = second_half;

	return (is_palindrome);
}

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to a pointer to the head of the linked list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - Compares two linked lists
 * @head1: Pointer to the head of the first linked list
 * @head2: Pointer to the head of the second linked list
 * Return: 1 if the lists are identical, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1, *temp2 = head2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n != temp2->n)
			return (0);

		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}
