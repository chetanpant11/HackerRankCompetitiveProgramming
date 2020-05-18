#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s="hackerrank";
    string ss;
    cin>>ss;
    int j=0;
    int count1=0;
    for(int i=0;i<ss.size();i++)
    {
        if(ss[i]==s[j])
            {count1++;
            j++;
            }
        if(j==s.size()-1)
            break;
    }
    cout<<count1;
    if(count1==s.size()-1)
        cout<<"YES";
    else
        cout<<"NO";

}
