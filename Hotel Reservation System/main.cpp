#include <iostream>
#include <string>
using namespace std;

// This class stores the info of the hotel
class Hotel
{
	string Name;
	string Location;
	string Manager;
	int Rooms;
public:
	Hotel()
	{
		Name = "0";
		Location = "0";
		Manager = "0";
		Rooms = 0;
	}
	Hotel(string N, string L, string M, int R) 
	{
		Name = N;
		Location = L;
		Manager = M;
		Rooms = R;
	}
	void Hotel_Crediantials(Hotel obj1);

};

// This class stores the info of the person/customer
class Person 
{
public:
	string FirstName;
	string LastName;
	string City;
	string Country;
	int CNIC;
	int Phone;
	int Room_ID;
	Person *Left;
	Person *Right;
	Person* Insert(Person*, int data, Person);
	Person* Search(Person*, int data);
	Person* Minimum(Person*);
	Person* Delete(Person*, int data);
	void InOrder(Person*);
	void PreOrder(Person*);
	void PostOrder(Person*);
};


Person *Person::Minimum(Person *root)
{
	while (root->Left != NULL) 
	{
		root = root->Left;
	}
	return root;
}

//This function deletes the informaton of the customer
Person *Person::Delete(Person *root, int Data)
{
	if (root == NULL) 
	{
		return root;
	}
	else if (Data < root->Room_ID)
	{
		root->Left = Delete(root->Left, Data);
	}
	else if (Data > root->Room_ID) 
	{
		root->Right = Delete(root->Right, Data);
	}
	else 
	{
		if (root->Left == NULL) 
		{
			Person *temp = root->Right;
			delete root;
			return temp;
		}
		else if (root->Right == NULL) 
		{
			Person *temp = root->Left;
			delete root;
			return temp;
		}
		Person *temp = Minimum(root->Right);
		root->Room_ID = temp->Room_ID;
		root->Right = Delete(root->Right, temp->Room_ID);
	}
	return root;
}

// This function is used to insert the information of the customer
Person *Person::Insert(Person *root, int Data, Person inp)
{
	if (root == NULL) 
	{
		Person *temp = new Person;
		temp->Room_ID = Data;
		temp->FirstName = inp.FirstName;
		temp->LastName = inp.LastName;
		temp->Phone = inp.Phone;
		temp->CNIC = inp.CNIC;
		temp->City = inp.City;
		temp->Country = inp.Country;
		temp->Left = temp->Right = NULL;
		return temp;
	}
	if (Data < root->Room_ID)
	{
		root->Left = Insert(root->Left, Data, inp);
	}
	if (Data >= root->Room_ID) 
	{
		root->Right = Insert(root->Right, Data, inp);
	}
	return root;
}

// This function is used to search the information of the customer
Person *Person::Search(Person *root, int id)
{
	if (root == NULL || root->Room_ID == id)
	{
		return root;
	}
	if (root->Room_ID <= id) 
	{
		return Search(root->Right, id);
	}
	if (root->Room_ID > id)
	{
		return Search(root->Left, id);
	}
}

// This function is used to display the information of the customer
void Person::InOrder(Person *root) 
{
	if (root == NULL) 
	{
		return;
	}
	InOrder(root->Left);
	cout << "Room ID" << "\t\t" << "Name" << "\t\t" << "Phone\t" << "\tCNIC" << "\tCity" << "\tCountry" << endl;
	cout << root->Room_ID << "\t\t" << root->FirstName<< " " << root->LastName<< "\t" << root->Phone<< "\t\t" << root->CNIC << "\t" << root->City << "\t" << root->Country << endl;
	cout << endl;
	InOrder(root->Right);
}

// This function display the information of the hotel
void Hotel::Hotel_Crediantials(Hotel obj1)
{
	cout << "\n**********Hotel Information**********\n" << endl;
	cout << "Name: " << obj1.Name << endl;
	cout << "Manager: " << obj1.Manager<< endl;
	cout << "Location: " << obj1.Location << endl;
	cout << "Total Rooms: " << obj1.Rooms << endl;
}

// This function display the main menu of the system
void menu1() 
{
	cout << "\n\t**********HOTEL MANAGEMENT SYSTEM**********\n" << endl;
	cout << "1. Display Hotel Crediantials" << endl; 
	cout << "2. Booking Information" << endl;
	cout << "3. Exit" << endl;
	cout << endl;
}


// This function display the main menu to book a room
void menu2() 
{
	cout << "\n\t**********MENU**********\n" << endl;
	cout << "1. Book A Room" << endl;
	cout << "2. Search A Room" << endl;
	cout << "3. Check-Out From Hotel" << endl;
	cout << "4. Display ( IN ORDER ) Booked Room's: " << endl;
	cout << "5. Display ( PRE ORDER ) Booked Room's: " << endl;
	cout << "6. Display ( POST ORDER ) Booked Room's: " << endl;
	cout << "7. Exit" << endl;
	cout << endl;
}

//main function
int main() {
	Person *root = NULL;
	Person *number = NULL;
	Person *search = NULL;
	Person *delt = NULL;
	Person obj;
	Person inp;
	Hotel obj1("Flattis Hotel", "Mall Road, Lahore", "Faiz Aamir", 50);
	int Choice = 0, Option = 0;
	while (Option <= 2) 
	{
		menu1();
		cout << "Option: " << endl;
		cin >> Option;
		switch (Option)
		{
		case 1:
			system("cls");
			obj1.Hotel_Crediantials(obj1);
			break;
		case 2:
			while (Choice <= 6)
			{
				menu2();
				cout << "Enter Choice: " << endl;
				cin >> Choice;
				switch (Choice)
				{
				case 1:
					int N;
					cout << "Enter ID Of Room(1-50): "; 
					cin >> N;
					if (N < 1 || N > 50)
					{
						cout << "\n**********Sorry..! There Are Only 50 Rooms..!**********" << endl;
					}
					else 
					{
						number = obj.Search(root, N);
						if (!number) 
						{
							cout << "Enter First Name: ";
							cin >> inp.FirstName;
							cout << "Enter Last Name: ";
							cin >> inp.LastName;
							cout << "Enter CNIC: ";
							cin >> inp.CNIC;
							cout << "Enter City: ";
							cin >> inp.City;
							cout << "Enter Country: ";
							cin >> inp.Country;
							cout << "Enter Phone Number: ";
							cin >> inp.Phone;
							root = obj.Insert(root, N, inp);
							cout << "\n\t**********Room booked**********" << endl;
						}
						else 
						{
							cout << "**********This Room Is Already Booked..!**********" << endl;
						}
					}
					break;
				case 2:
					system("cls");
					int Id;
					cout << "Enter Room ID:  ";
					cin >> Id;
					number = obj.Search(root, Id);
					if (!number) 
					{
						cout << "**********Room Not Found**********" << endl;
						cout <<"**********Enter Valid room ID**********" << endl;
					}
					else 
					{
						cout << "**********Room Found**********" << endl;
					}
					break;
				case 3:
					int D;
					cout << "Enter ID: ";
					cin >> D;
					search = obj.Search(root, D);
					if (!search) 
					{
						cout << "**********Room Data Not Found**********" << endl;
					}
					else 
					{
						cout << "**********Room Deleted**********" << endl;
						cout <<"**********It Is Available For New Bookings Now**********" << endl;
					}
					delt = obj.Delete(root, D);
					break;
				case 4:
					system("cls");
					obj.InOrder(root);
					break;
				case 5:
					system("cls");
					obj.PreOrder(root);
					break;
				case 6:
					system("cls");
					obj.PostOrder(root);
					break;
				default:
					cout << "**********THANK YOU**********" << endl;
					break;
				}
			}
			break;
		default:
			cout << "\n\t**********THANKYOU, HOPE YOU LIKE OUR SERVICES**********" << endl;
			break;
		}
  }
	return 0;
}
