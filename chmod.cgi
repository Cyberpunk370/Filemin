#!/usr/bin/perl

require './filemin-lib.pl';
&switch_to_remote_user();

&ReadParse();

get_paths();

my @errors;
my $recursive;
if($in{'recursive'} eq 'true') { $recursive = '-R'; } else { $recursive = ''; }

foreach $name (split(/\0/, $in{'name'})) {
    my $perms = $in{'perms'};
    if(system("chmod $perms $cwd/$name $recursive") != 0) {
        push @errors, "$name - $text{'error_chmod'}: $?";
    }
}
if (scalar(@errors) > 0) {
    print_errors(@errors);
} else {
    &redirect("index.cgi?path=$path");
}
