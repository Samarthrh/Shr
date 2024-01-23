#include <stdio.h>
#include <stdlib.h>

// Define a node structure
struct Node {
    int data;
    struct Node* next;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to delete a node with a specific value from the linked list
struct Node* deleteNode(struct Node* head, int value) {
    struct Node* current = head;
    struct Node* previous = NULL;

    // Search for the node with the specified value
    while (current != NULL && current->data != value) {
        previous = current;
        current = current->next;
    }

    // If the value is not found, return the original head
    if (current == NULL) {
        printf("Value %d not found in the linked list.\n", value);
        return head;
    }

    // If the node to be deleted is the head
    if (previous == NULL) {
        head = current->next;
    } else {
        // Link the previous node to the next node, skipping the current node
        previous->next = current->next;
    }

    // Free the memory allocated for the deleted node
    free(current);
    
    printf("Value %d deleted from the linked list.\n", value);

    return head;
}

// Function to display the linked list
void displayList(struct Node* head) {
    struct Node* current = head;

    // Traverse the list and print each node's data
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }

    printf("NULL\n");
}

// Function to free the memory allocated for the linked list
void freeList(struct Node* head) {
    struct Node* current = head;
    struct Node* nextNode;

    // Traverse the list and free each node
    while (current != NULL) {
        nextNode = current->next;
        free(current);
        current = nextNode;
    }
}

int main() {
    // Create a sample linked list: 1 -> 2 -> 3 -> 4 -> NULL
    struct Node* head = createNode(1);
    head->next = createNode(2);
    head->next->next = createNode(3);
    head->next->next->next = createNode(4);

    // Display the linked list
    printf("Linked List: ");
    displayList(head);

    // Delete a node with a specific value
    int deleteValue;
    printf("Enter a value to delete: ");
    scanf("%d", &deleteValue);

    // Update the head after deletion
    head = deleteNode(head, deleteValue);

    // Display the updated linked list
    printf("Updated Linked List: ");
    displayList(head);

    // Free the memory allocated for the linked list
    freeList(head);

    return 0;
}
