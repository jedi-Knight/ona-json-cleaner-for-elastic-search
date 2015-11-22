#!/usr/bin/perl
use strict;
use warnings;
use JSON;

use Path::Class;
use autodie; # die if problem reading or writing a file

#my $dir = dir("./"); # /tmp

my $file = file("school.json");

# Read in the entire contents of a file
my $content = $file->slurp();

#$content =~ s/_//g;

# openr() returns an IO::File object to read from
#my $file_handle = $file->openr();

# Read in line at a time
#while( my $line = $file_handle->getline() ) {
 #       print $line;
#}

my $items_array = decode_json $content;

#var_dump($items_array);

#print $content;