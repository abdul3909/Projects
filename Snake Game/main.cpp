#include <iostream>
#include<windows.h>  //Library used to add sleep function 
#include<conio.h>
#include<stdlib.h>   //Library used for random numbers

using namespace std;
//Taking Global Variables


bool gameOver;
//Taking constant variables for arena width and height
const int width = 20;
const int height = 20;
//taking an array for the size of snake
int tailX[50], tailY[50];
int nTail;
//Variables for position of player and fruit
int x, y, FruitX, FruitY, score;
//Setting enumerators for fixed direction
enum eDirection { STOP = 0, LEFT, RIGHT, UP, DOWN };
eDirection dir;


void Settings()
{
	//1
	//Setting the game to start
	//Setting gameover to false to start the game
	gameOver = false;
	//Setting direction to stop so snake will not be moving at the start of game
	dir = STOP;
	//Setting the location of snake at the centre of arena at the start of game
	x = width / 2;
	y = height / 2;
	//using random operator to randomize our fruit in the map
	FruitX = rand() % width;
	FruitY = rand() % height;
	//Setting score to zero
	score = 0;



}

void Visual()
{
	//Clearing the screen
	system("cls");
	//Drawing our arena in which snake can move
	for (int i = 0; i < width + 2; i++)

		cout << "#";

	cout << endl;

	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{
			if (j == 0)
				cout << "#";



			if (i == y && j == x)   //Drawing snake head
				cout << "O";

			else if (i == FruitY && j == FruitX)    //Adding food in the arena
				cout << "*";

			//Drawing snake tail
			else
			{
				bool printtail = false;

				for (int k = 0; k < nTail; k++)
				{
					if (tailX[k] == j && tailY[k] == i)
					{
						cout << "o";
						printtail = true;
					}
				}


				if (!printtail)

					cout << " ";
			}



			if (j == width - 1)
				cout << "#";

		}
		cout << endl;
	}
	for (int i = 0; i < width + 2; i++)
	{
		cout << "#";
	}
	cout << endl;
	//Adding total score at the bottom of arena
	cout << "Score: " << score << endl;

}

void Input()

//Adding function for the movement of snake
//if keyboard is hit
{
	if (_kbhit())
	{
		switch (_getch())   //Getting character values 
		{
		case'a':
			dir = LEFT;
			break;
		case'd':
			dir = RIGHT;
			break;
		case'w':
			dir = UP;
			break;
		case's':
			dir = DOWN;
			break;
		case'x':
			gameOver = true;
			//Printing the message on screen if keyboard is hit
			system("cls");
			cout << "******GAME OVER******" << endl;
			cout << "\nYour score is: " << score << endl;
			cout << "\n*****BEST OF LUCK*****\n" << endl;
			break;
		}
	}
}

void logic()
//Adding a logic part for the tail to follow the next member
{
	int prevX = tailX[0];
	int prevY = tailY[0];
	prevX = x;
	prevY = y;
	int prev2X, prev2Y;
	for (int i = 0; i < nTail; i++)
	{
		prev2X = tailX[i];
		prev2Y = tailY[i];
		tailX[i] = prevX;
		tailY[i] = prevY;
		prevX = prev2X;
		prevY = prev2Y;

	}


	//adding switch statments for the direction of snake
	//Along the x axis and y axis

	switch (dir)
	{
	case LEFT:
		x--;
		break;

	case RIGHT:
		x++;
		break;
	case UP:
		y--;
		break;
	case DOWN:
		y++;
		break;
	default:
		break;
	}

	//Adding functionality for the snake to pass by the walls
	if (x >= width)
		x = 0;
	else if (x < 0)
		x = width - 1;

	if (y >= width)
		y = 0;
	else if (y < 0)
		y = width - 1;

	//Adding Game over functionality if the snake hit itself
	for (int i = 0; i < nTail; i++)

		if (tailX[i] == x && tailY[i] == y)
		{
			
			gameOver = true;
			//Adding outputs if the game is over
			system("cls");
			cout << "***OOOPS....You have been hit***" << endl;
			cout << "\n******GAME OVER******" << endl;
			cout << "\nYour score is: " << score << endl;
			cout << "\n\n*****GOOD LUCK*****\n " << endl;
		}


	//Adding randon function for the random alloction of fruit
	//in the arena if it is eaten by snake
	if (x == FruitX && y == FruitY)
	{
		score++;
		FruitX = rand() % width;
		FruitY = rand() % height;
		nTail++;  //Increasing the tail everytime the snake eat fruit
	}


}

int main()
{
	//Main Funtion
	Settings();
	while (!gameOver)
	{
		Visual();
		Input();
		logic();
		//Adding Sleep function to slow down the speed of snake
		//and blinking of screen
		Sleep(30); 
	}
	return 0;
}
