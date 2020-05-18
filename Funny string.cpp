#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        bool flag=true;
        string s;
        string s1;
        cin>>s;
        s1=s;
        reverse(s.begin(),s.end());
        for(int i=1;i<s.size();i++)
        {
            if(abs(int(s[i])-int(s[i-1]))==abs(int(s1[i])-int(s1[i-1])))
                continue;
            else
                {
                    flag=false;
                    break;
                }
        }
        if(flag)
            cout<<"Funny";
        else
            cout<<"not funnny";
    }
}
