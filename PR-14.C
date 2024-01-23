#include<stdio.h>
#include<conio.h>
//Represent a node of singly linked list  
struct node{  
    int data;  
    struct node *next;  
};      
   
//Represent the head and tail of the singly linked list  
struct node *head, *tail = NULL;  
   
//addNode() will add a new node to the list  
void addNode(int data) {  
    //Create a new node  
    struct node *newNode = (struct node*)malloc(sizeof(struct node));  
    newNode->data = data;  
    newNode->next = NULL;  
      
    //Checks if the list is empty  
    if(head == NULL) {  
        //If list is empty, both head and tail will point to new node  
        head = newNode;  
        tail = newNode;  
    }  
    else {  
        //newNode will be added after tail such that tail's next will point to newNode  
        tail->next = newNode;  
        //newNode will become new tail of the list  
        tail = newNode;  
    }  
}  
   
//countNodes() will count the nodes present in the list  
int countNodes() {  
    int count = 0;  
    //Node current will point to head  
    struct node *current = head;  
      
    while(current != NULL) {  
        //Increment the count by 1 for each node  
        count++;  
        current = current->next;  
    }  
    return count;  
}  
      
//display() will display all the nodes present in the list  
void display() {
    //Node current will point to head
    struct node *current = head;

    if(head == NULL) {
	printf("List is empty\n");
	return;
    }
    printf("mandaliya akshar:\n");
    printf("226090307073:\n");
    printf("Nodes of singly linked list: \n");
    while(current != NULL) {
	//Prints each node by incrementing pointer
	printf("%d ", current->data);
	current = current->next;
    }
    printf("\n");
}

int main()
{
    //Add nodes to the list
    addNode(1);
    addNode(2);
    addNode(3);
    addNode(4);
clrscr();
    //Displays the nodes present in the list
    display();

    //Counts the nodes present in the given list
    printf("Count of nodes present in the list: %d", countNodes());


	getch();
}