Project Name: The Music Generator

Team Members: Alexis O'Neill, Aldrin Dancel Carlos, Raquel Zempoalteca

Class: CST 205

Date: 3/15/17

Github Repo: https://github.com/CSUMB-SP17-CST205/team29-proj2

C9 Link: https://ide.c9.io/aleoneill/lexi-csumb#openfile-README.md

TA: Michael


## Welcome to our Music Finder!

Our purpose is to help the users find new music, or even reminisce in some of 
the songs you used to listen to as a chlid. We created this program to help you
find new music in 3 different ways..

## Finding Music by Genre

In this portion of the program, we give the user a list of music genres to choose
from. The program then returns a list of some of the top songs from that genre. 
This is done by using the unofficial Billboard API.

(Reference it here: https://github.com/guoguo12/billboard-charts)

We did this so that the list of songs would be updated without having to 
constantly update it manually. We set each genre equal to a chartList and created
a dictionaryto store the list of songs when that genre is called.

However, because not all of the listed genres were found on Billboard, we had to 
resort to embedding a Spotify playlist that we felt fit best with that genre.

Because the Billboard API only lists the song by giving the song name and artist,
it lacks accessibility because the user cannot listen to that song on demand 
without having to look it up on Youtube or some other website. With Spotify 
embedded, the user can easily listen to the song on demand.

## Finding Music by Mood

This portion of the program is similar to that of the genre portion. We give the
user a list of moods, and return some songs that we felt go best with that mood
along with its own personal message from us.

We did this by creating a dictionary per mood that holds a list of songs and
the artist(s) that follows. However, like the gene portion, this portion only
displays snogs, and does not give the user the option to listen to the song on
the spot without having to pull up Youtube (or some other website).

However, because of how we formatted this, it is easily accessible for us to
continuously update the list and add songs or even moods without a hassle.

## Finding Random Music

This portion is a basic random song generator. We manually embedded over 500
songs from a whole bunch of genres and times. It will randomly display a Youtube
video of a song, giving the user the option to listen to it on the spot. If the
user does not like what we displayed, we gave them the option to reload the page
and display a new song from our dictionary of songs. The list of songs were
recommended by those around us (credit is given at the bottom of the .py file)
and created a well done random song generator.

Genre of the songs embedded go as follows:

Pop, Country, Rock, Religious, Metal, K-Pop, J-Pop, Oldies, Classic Rock,
Game Scores, Movie Scores, Reggae, Dance, Dubstep, Electronic, Trance, Classical,
Latin, R & B and Indie.

## Continuing On With the Project

As time goes on, we plan to update the program and make it better by adding a
Youtube search bar, so the user can look up the song if they so choose, create
an option for playlist and rating system per song, and even a rating system
for the program.
