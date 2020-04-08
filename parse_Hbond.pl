#!/usr/bin/perl -w

open(A,"hbonds-details_3967.dat");
open(B,"hbonds-details_85.dat");

my@dat1 = <A>;
my@dat2 = <B>;
my@Acceptor1 = ();
my@Donor1 = ();
my@Acceptor2 = ();
my@Donor2 = ();
for(my$i =2;$i<scalar@dat1;$i++)
{
	my@w = split(" ",$dat1[$i]);
	my@q = split("-",$w[0]);
	my@e = split("-",$w[1]);
	push(@Acceptor1,$e[0]);
	push(@Donor1,$q[0]);
}

for(my$j =2;$j<scalar@dat2;$j++)
{
	my@ww = split(" ",$dat2[$j]);
	my@qq = split("-",$ww[0]);
	my@ee = split("-",$ww[1]);
	push(@Acceptor2,$ee[0]);
	push(@Donor2,$qq[0]);
}
my@DA1 = DonorAcceptor(\@Donor1,\@Acceptor1);
my@DA2 = DonorAcceptor(\@Donor2,\@Acceptor2);

my@NtoC1 = SortNtoC(@DA1);
my@NtoC2 = SortNtoC(@DA2);
print @NtoC1,"\n\n\n";
print @NtoC2,"\n";


sub DonorAcceptor
{
	my($D,$A) =  @_;
	my@mergeArray = ();
	for(my$i=0;$i<scalar@{$D};$i++)
	{
		my$r = "$$D[$i]:$$A[$i]";
		push(@mergeArray,$r);
	}
	return(@mergeArray);
}
			
sub SortNtoC
{
	my(@D) = @_;
	my@output = ();
	foreach ( sort { number_strip($a) <=> number_strip($b) } @Dcat h	 ){
		my$line =  "\"$_\"";
		push(@output,$line,",");
	}
	return(@output);
}

sub number_strip {
    $line = shift;
    my ($num) = $line =~ /(\d+)/;
    return $num;
}
