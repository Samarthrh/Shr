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

// Function to search for a value in the linked list
struct Node* searchNode(struct Node* head, int value) {
    struct Node* current = head;

    // Traverse the list to find the node with the specified value
    while (current != NULL) {
        if (current->data == value) {
            return current; // Node with the value found
        }
        current = current->next;
    }

    return NULL; // Value not found
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

    // Search for a value in the linked list
    int searchValue;
    printf("Enter a value to search: ");
    scanf("%d", &searchValue);

    struct Node* result = searchNode(head, searchValue);

    // Display the search result
    if (result != NULL) {
        printf("Value %d found in the linked list.\n", searchValue);
    } else {
        printf("Value %d not found in the linked list.\n", searchValue);
    }

    // Free the memory allocated for the linked list
    freeList(head);

    return 0;
}
