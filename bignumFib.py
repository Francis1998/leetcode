a[1000][1000]
int main()
{
    int n,m,i,k,c,l;
    scanf("%d",&n);
    while(n--)
    {
        scanf("%d",&m);l=1;
        a[1][0]=1;a[2][0]=1;
        for(i=3;i<=m;++i)
        {
            for(k=0,c=0;k<l;++k)
            {
                a[i][k]=a[i-1][k]+a[i-2][k]+c;
                c=a[i][k]/10;
                a[i][k]%=10;
            }
            while(c>0)
            {
                a[i][k++]=c%10;
                c=c/10;
            }
            l=k;
        }
        for(i=l-1;i>=0;i--)printf("%d",a[m][i]);
        printf("\n");
    }
    return 0;
}