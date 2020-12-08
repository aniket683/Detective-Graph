#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;

int main(){
	ifstream infile("test.graph");
	int vertex, edges, k;
	infile >> vertex >> edges >> k;
	cout << vertex << edges << k;
	// vector<vector<bool> > graph(vertex);
	bool graph[vertex+1][vertex+1];
	int a, b;
	vector< pair <int,int> > vect;
	while(infile >> a >> b){
		vect.push_back(make_pair(min(a,b),max(a,b)));
		graph[min(a,b)][max(a,b)] = true;
	}
	ofstream myfile;
	myfile.open ("clauses.txt");
	
	for(int j=2;j<=vertex;j++){
		for(int i=1;i<j;i++){
			int coord = i+(j-1)*(j-2)/2;
			if(graph[i][j]){
				string s = to_string(coord);
				myfile << s << "\n";
			}
			else{
				string s = to_string(-1*coord);
				myfile << s << "\n";
			}
		}
	}



	myfile.close();
	// for(int i = 0; i < vect.size(); i++)
	// 	cout << vect[i].first << " " 
	// 		 <<	vect[i].second << "\n";
	// cout << vect.size();
	return 0;
}