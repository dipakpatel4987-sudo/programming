#include<stdio.h>

int main()
{
    int choice, quantity;
    char more;
    float totalBill = 0;

    printf("=====================================\n");
    printf("       WELCOME TO FOOD CAFE\n");
    printf("=====================================\n");

    do
    {
       
        printf("\n----------- FOOD MENU -----------\n");
        printf("1. Pizza      - Rs.250\n");
        printf("2. Burger     - Rs.120\n");
        printf("3. Sandwich   - Rs.100\n");
        printf("4. Pasta      - Rs.180\n");
        printf("5. Cold Drink - Rs.50\n");
        printf("---------------------------------\n");

       
        printf("Enter your choice (1-5): ");
        scanf("%d", &choice);

        
        printf("Enter quantity: ");
        scanf("%d", &quantity);

        
        switch(choice)
        {
            case 1:
                totalBill += 250 * quantity;
                printf("Pizza Added Successfully!\n");
                break;

            case 2:
                totalBill += 120 * quantity;
                printf("Burger Added Successfully!\n");
                break;

            case 3:
                totalBill += 100 * quantity;
                printf("Sandwich Added Successfully!\n");
                break;

            case 4:
                totalBill += 180 * quantity;
                printf("Pasta Added Successfully!\n");
                break;

            case 5:
                totalBill += 50 * quantity;
                printf("Cold Drink Added Successfully!\n");
                break;

            default:
                printf("Invalid Choice!\n");
        }

       
        printf("Current Total Bill = Rs. %.2f\n", totalBill);

        
        printf("\nDo you want to order more? (Y/N): ");
        scanf(" %c", &more);

    } while(more == 'Y' || more == 'y');

   
    printf("\n=====================================\n");
    printf("          FINAL FOOD BILL\n");
    printf("=====================================\n");
    printf("Total Amount = Rs. %.2f\n", totalBill);
    printf("Thank You! Visit Again.\n");
    printf("=====================================\n");

    return 0;
}
