#include<stdio.h>
#include<stdlib.h>
 
void merge(int A[], int left, int right, int mid)
{
    int i,j,k;
    int l=mid-left+1;
    int r=right-mid;
    int leftarray[l],rightarray[r];
    for(i=0;i<l;i++)
    {
        leftarray[i]=A[left+i];
    }
    for(j=0;j<r;j++)
    {
        rightarray[j]=A[mid+1+j];
    }
    i=0;
    j=0;
    k=left;
    while(i<l && j<r)
    {
        if(leftarray[i]<=rightarray[j])
        {
            A[k]=leftarray[i];
            i++;
        }
        else
        {
            A[k]=rightarray[j];
            j++;
        }
        k++;
    }
    while(i<l)
    {
        A[k]=leftarray[i];
        i++;
        k++;
    }
    while(j<r)
    {
        A[k]=rightarray[j];
        j++;
        k++;
    }
}
 
 
void mergesort(int A[], int left, int right)
{
    if(left<right)
    {
        int mid=left+(right-left)/2;
        mergesort(A, left, mid);
        mergesort(A, mid+1, right);
        merge(A, left, right, mid);    
    }
}
 
int main()
{
    int i,n;
    printf("Enter size of array:");
    scanf("%d",&n);
    int A[n];
    printf("Enter the array");
    for(i=0;i<n;i++)
    {
        scanf("%d",&A[i]);
    }
    mergesort(A,0,n-1);
    printf("The sorted array is:\n");
    for(i=0;i<n;i++)
    {
        printf("%d",A[i]);
    }
    return 0;
}