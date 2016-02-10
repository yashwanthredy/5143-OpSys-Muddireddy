#!/bin/bash
#file containing a list of words on system
WORDFILE="/usr/share/dict/words"
#Number of words in $WORDFILE
wordCount=$( cat "$WORDFILE" | wc -w )
#randomly generates a number in range of total word count
rnum=$((RANDOM%$wordCount+1))
#gives the prescribed word from the wordfile
sed -n "$rnum p" $WORDFILE;



