# colsplit.py

A simple script to format a text file into columns, by specifying the number of columns to show and the separator to use.

There are several ways to achieve the same result using terminal commands, such as awk, split, paste, etc. But the idea behind this small tool is to get an easiest way to accomplish that.


## Installing

Not installing needed. Simply copy the script into some of your PATH's directories, such as /usr/local/bin, $HOME/bin, etc.

	$ git clone https://ks4v3r@bitbucket.org/ks4v3r/colsplit.git
	$ cd colsplit
	$ sudo cp colsplit.py /usr/local/bin


Give it executable bit permissions:

	$ sudo chmod +x /usr/local/bin/colsplit.py
	

And test it:

	$ colsplit.py -h 
	usage: colsplit.py [-h] [-c COLUMNS] [-s SEPARATOR] filename

	Splits a text file in columns.

	positional arguments:
	  filename              Text file to split in columns.

	optional arguments:
	  -h, --help            show this help message and exit
	  -c COLUMNS, --columns COLUMNS
		                Number of columns.
	  -s SEPARATOR, --separator SEPARATOR
		                Searator to use. Default is ' '.


## Usage

Using *colsplit.py* with no arguments, will give us a brief help on usage:

	$ colsplit.py
	usage: colsplit.py [-h] [-c COLUMNS] [-s SEPARATOR] filename
	colsplit.py: error: the following arguments are required: filename


For view extra help, use the *"-h"* or *"--help"* option, as before:

	$ colsplit.py -h 
	...


Let's say we have a big text file with hundreds of IP addresses, words, or any other data. We want to show this data in columns format in order to improve readability or save some space.

Our example text file contains one word in each line:

	$ head rockyou.txt
	123456
	12345
	123456789
	password
	iloveyou
	princess
	1234567
	rockyou
	12345678
	abc123


The most basic usage of *colsplit.py* is specifying the text file to split in columns and the number of columns you want to show.

	$ colsplit.py -c 5 rockyou.txt
	123456	12345	123456789	password	iloveyou
	princess	1234567	rockyou	12345678	abc123
	nicole	daniel	babygirl	monkey	lovely
	jessica	654321	michael	ashley	qwerty
	111111	iloveu	000000	michelle	tigger


By default *colsplit.py* uses the character "\t" (tab) to separate columns, but you can specify your own. You can use a comma chacter as a separator, as in the next example:

	$ colsplit.py -c 5 -s "," rockyou.txt
	123456,12345,123456789,password,iloveyou
	princess,1234567,rockyou,12345678,abc123
	nicole,daniel,babygirl,monkey,lovely
	jessica,654321,michael,ashley,qwerty
	111111,iloveu,000000,michelle,tigger


## *Colsplitting* the standard output

We can redirect the standard output of other terminal programs to *colsplit.py*, using *pipes*. Let's say, we need to sort alfabetically the first 500 lines in the *rockyou.txt* file and show in a format of 10 columns, comma separated only the first 100 sorted lines:

	$ head -n 500 rockyou.txt | sort | head -n 100 | colsplit.py -c 10 -s',' -
	00000,000000,0123456,0123456789,101010,11111,111111,112233,121212,123123
	123321,12345,123456,1234567,12345678,123456789,1234567890,12345678910,123456a,123654
	123abc,131313,147258,147258369,159357,159753,222222,232323,246810,252525
	333333,456789,50cent,5201314,55555,555555,654321,666666,696969,777777
	7777777,789456,789456123,888888,88888888,987654,987654321,999999,aaaaaa,aaliyah
	abc123,abcdef,abigail,adidas,adrian,adriana,albert,alberto,alejandra,alejandro
	alexander,alexandra,alexis,alicia,alyssa,amanda,america,amigos,amorcito,amores
	andrea,andreea,andres,andrew,angel,angel1,angela,angelica,angelito,angelo
	angels,anthony,anthony1,antonio,apples,arsenal,asdfgh,asdfghjkl,ashley,asshole
	august,austin,babyblue,babyboy,babydoll,babygirl,babygirl1,babygurl,babyko,badboy


Note that we use the hyphen character (-) to specify the standard input as the file to read.


## Saving the *Colsplitted* output

We can redirect the output of *colsplit.py* to a file and create for example, a ".csv" file:

	$ colsplit.py -c 8 -s "," rockyou.txt > rockyou.csv
	$ head -n 7 rockyou.csv
	123456,12345,123456789,password,iloveyou,princess,1234567,rockyou
	12345678,abc123,nicole,daniel,babygirl,monkey,lovely,jessica
	654321,michael,ashley,qwerty,111111,iloveu,000000,michelle
	tigger,sunshine,chocolate,password1,soccer,anthony,friends,butterfly
	purple,angel,jordan,liverpool,justin,loveme,fuckyou,123123
	football,secret,andrea,carlos,jennifer,joshua,bubbles,1234567890
	superman,hannah,amanda,loveyou,pretty,basketball,andrew,angels


Now we can import that .csv file to Excel or use other csv parsing tools on it.

