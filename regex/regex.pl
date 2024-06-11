# Your task is to write a regex which will match , with following condition(s):
# consists of 8 digits.
# must have "---", "-", "." or ":" separator such that string  gets divided in  parts, with each part having exactly two digits.
# string must have exactly one kind of separator.
# Separators must have integers on both sides.

$Regex_Pattern = '^\d{2}(---|-|\.|:)(\d{2}\1?){3}$';

$Test_String = <STDIN> ;
if($Test_String =~ /$Regex_Pattern/){
		print "true";
} else {
		print "false";
}
# \1 matches the same text as most recently matched by the 1st capturing group


# consists of tic or tac.
# tic should not be immediate neighbour of itself.
# The first tic must occur only when tac has appeared at least twice before.

$Regex_Pattern = '^(\2tic|(tac))+$';
$Test_String = <STDIN> ;
if($Test_String =~ /$Regex_Pattern/){
		print "true";
} else {
		print "false";
}