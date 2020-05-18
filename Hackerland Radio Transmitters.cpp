#include <bits/stdc++.h>
using namespace std;
#define gc getchar_unlocked
#define fo(i,n) for(i=0;i<n;i++)
#define Fo(i,k,n) for(i=k;i<n;i++)
#define ll long long
#define si(x)	scanf("%d",&x)
#define sl(x)	scanf("%I64d",&x)
#define ss(s)	scanf("%s",s)
#define pf(s)	printf("%d",s)
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define clr(x) memset(x, 0, sizeof(x))
#define tr(it, a) for(auto it = a.begin(); it != a.end(); it++)
#define PI 3.1415926535897932384626
typedef pair<int, int>	pii;
typedef pair<ll, ll>	pll;
typedef vector<int>		vi;
typedef vector<ll>		vl;
typedef vector<pii>		vpii;
typedef vector<pll>		vpll;
typedef vector<vi>		vvi;
typedef vector<vl>		vvl;
const int mod = 1000000007;
const int N = 2e5;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,k,j;
    si(n);
    si(k);
    vi v(n);
    fo(j,n)
    si(v[j]);
    sort(v.begin(),v.end());
    int i=0,count=0;
    while(i<n)
    {
        count++;
        int l=v[i]+k;
        while(i<n && v[i]<=l)i++;

        i--;
        l=v[i]+k;
        while(i<n&&v[i]<=l)i++;
    }
    cout<<count;
}
